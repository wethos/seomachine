#!/usr/bin/env python3
"""
Research Keyword Volumes + SERPs — model routing / inference cost governance

Companion to research_keyword_volumes.py, scoped to the topic investigated in
research/brief-model-routing-inference-cost-2026-09-14.md: routing workloads
off frontier models onto open-weight ones, and whether that is surfacing as a
hireable engineering skill.

Requires the machine's public IP to be whitelisted in the DataForSEO panel
(https://app.dataforseo.com/api-access).

Usage:
    .venv/bin/python research_model_routing_volumes.py [--no-serp]

Output: markdown to stdout + JSON to
  output/keyword-volumes-model-routing-<date>.json
  output/serp-model-routing-<date>.json
"""

import os
import sys
import json
import argparse
from datetime import datetime
from dotenv import load_dotenv

REPO = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(REPO, "data_sources/config/.env"))
sys.path.insert(0, os.path.join(REPO, "data_sources"))

from modules.dataforseo import DataForSEO

VOLUME_ENDPOINT = "/v3/keywords_data/google_ads/search_volume/live"
SERP_ENDPOINT = "/v3/serp/google/organic/live/advanced"

# Grouped by intent — the searcher behind "llm routing" is not the one behind
# "hire llm engineer". The split decides what is writable.
GROUPS_EN = {
    "technique": [
        "llm routing", "model routing", "ai model routing", "llm router",
        "llm gateway", "litellm", "openrouter", "prompt caching",
        "open weight models", "open source llm vs closed source",
        "open source llm", "self hosted llm",
    ],
    "cost": [
        "llm cost optimization", "reduce llm costs", "llm inference cost",
        "ai inference cost", "inference cost", "ai cost optimization",
        "llm cost", "token cost", "ai finops", "finops for ai",
        "ai cost governance", "llm pricing comparison",
    ],
    "role_hiring": [
        "inference engineer", "inference engineering", "llm engineer",
        "llmops engineer", "llmops", "ai platform engineer",
        "ai infrastructure engineer", "mlops engineer", "hire llm engineer",
        "hire ai engineer", "llm engineer job description",
        "ai engineer job description", "llm engineer salary",
        "ai finops engineer", "finops engineer",
    ],
}

GROUPS_RO = {
    "technique_cost": [
        "llm", "modele open source", "costuri ai", "cost ai", "finops",
        "optimizare costuri cloud", "inteligenta artificiala costuri",
    ],
    "role_hiring": [
        "inginer llm", "inginer ai", "ai engineer", "llm engineer",
        "mlops", "salariu ai engineer", "joburi ai", "ai engineer romania",
    ],
}

GEOS = [
    ("Romania", "en", "en"),
    ("Romania", "ro", "ro"),
    ("United Kingdom", "en", "en"),
    ("United States", "en", "en"),
    ("Germany", "en", "en"),
]

# (keyword, location_name, language_code)
SERPS = [
    ("llm routing", "United States", "en"),
    ("llm cost optimization", "United States", "en"),
    ("ai inference cost", "United States", "en"),
    ("inference engineer", "United States", "en"),
    ("llm engineer", "Romania", "en"),
    ("ai finops", "United States", "en"),
]


def run_volumes(dfs):
    total_cost, results = 0.0, {}
    for loc, lang, kwset in GEOS:
        groups = GROUPS_EN if kwset == "en" else GROUPS_RO
        origin = {kw: g for g, kws in groups.items() for kw in kws}
        payload = [{
            "keywords": list(origin),
            "location_name": loc,
            "language_code": lang,
            "search_partners": False,
        }]
        print(f"→ {loc} / {lang}: {len(origin)} keywords", file=sys.stderr)
        resp = dfs._post(VOLUME_ENDPOINT, payload)
        total_cost += resp.get("cost", 0) or 0

        task = dfs._first_task(resp)
        if not task or task.get("status_code") != 20000:
            print(f"   ✗ {(task or resp).get('status_message')}", file=sys.stderr)
            continue

        for it in (task.get("result") or []):
            kw = it.get("keyword")
            results.setdefault(f"{loc}|{lang}", []).append({
                "intent": origin.get(kw, "?"),
                "keyword": kw,
                "search_volume": it.get("search_volume"),
                "competition": it.get("competition"),
                "cpc": it.get("cpc"),
                "monthly_searches": it.get("monthly_searches"),
            })

    for geo, rows in results.items():
        loc, lang = geo.split("|")
        measurable = [r for r in rows if (r["search_volume"] or 0) > 0]
        zero = [r for r in rows if not r["search_volume"]]
        print(f"\n\n## {loc} / {lang} — {len(measurable)} with volume, {len(zero)} at zero\n")
        if measurable:
            print("| Intent | Keyword | Volume | Competition | CPC |")
            print("|---|---|---|---|---|")
            for r in sorted(measurable, key=lambda x: -(x["search_volume"] or 0)):
                cpc = f"${r['cpc']:.2f}" if r.get("cpc") else "—"
                print(f"| {r['intent']} | {r['keyword']} | **{r['search_volume']}** | "
                      f"{r['competition'] or '—'} | {cpc} |")
        if zero:
            print("\n**No measurable volume:** " + " · ".join(sorted(r["keyword"] for r in zero)))
    return total_cost, results


def run_serps(dfs):
    total_cost, out = 0.0, {}
    for kw, loc, lang in SERPS:
        payload = [{"keyword": kw, "location_name": loc, "language_code": lang,
                    "device": "desktop", "depth": 20}]
        print(f"→ SERP {kw} ({loc}/{lang})", file=sys.stderr)
        resp = dfs._post(SERP_ENDPOINT, payload)
        total_cost += resp.get("cost", 0) or 0
        task = dfs._first_task(resp)
        if not task or task.get("status_code") != 20000:
            print(f"   ✗ {(task or resp).get('status_message')}", file=sys.stderr)
            continue
        result = dfs._first_result(task) or {}
        items = result.get("items") or []
        organic = [{"rank": i.get("rank_group"), "domain": i.get("domain"),
                    "title": i.get("title"), "url": i.get("url")}
                   for i in items if i.get("type") == "organic"][:10]
        features = sorted({i.get("type") for i in items if i.get("type") != "organic"})
        paa = []
        for i in items:
            if i.get("type") == "people_also_ask":
                paa += [q.get("title") for q in (i.get("items") or [])]
        out[f"{kw}|{loc}|{lang}"] = {"features": features, "organic": organic, "paa": paa}

        print(f"\n\n### SERP: `{kw}` — {loc}/{lang}\n")
        print(f"Features: {', '.join(features) or 'none'}")
        if paa:
            print("PAA: " + " · ".join(paa))
        print("\n| # | Domain | Title |\n|---|---|---|")
        for o in organic:
            print(f"| {o['rank']} | {o['domain']} | {(o['title'] or '')[:90]} |")
    return total_cost, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-serp", action="store_true")
    args = ap.parse_args()

    dfs = DataForSEO()
    out_dir = os.path.join(REPO, "output")
    os.makedirs(out_dir, exist_ok=True)
    stamp = f"{datetime.now():%Y-%m-%d}"

    cost_v, volumes = run_volumes(dfs)
    with open(os.path.join(out_dir, f"keyword-volumes-model-routing-{stamp}.json"), "w") as f:
        json.dump({"measured": datetime.now().isoformat(), "cost_usd": cost_v,
                   "results": volumes}, f, indent=2)

    cost_s = 0.0
    if not args.no_serp:
        cost_s, serps = run_serps(dfs)
        with open(os.path.join(out_dir, f"serp-model-routing-{stamp}.json"), "w") as f:
            json.dump({"measured": datetime.now().isoformat(), "cost_usd": cost_s,
                       "results": serps}, f, indent=2)

    print(f"\n\n---\n**DataForSEO cost: ${cost_v + cost_s:.4f}**")


if __name__ == "__main__":
    main()
