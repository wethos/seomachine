#!/usr/bin/env python3
"""
Research Keyword Volumes — "calculator salarii" / employer-cost cluster

Companion to research_keyword_volumes.py, scoped to the salary-calculator and
employer-cost query families investigated in
research/brief-calculator-salarii-2026-09-02.md.

Requires the machine's public IP to be whitelisted in the DataForSEO panel
(https://app.dataforseo.com/api-access) — otherwise every task returns
"Access denied. Your IP is not whitelisted."

Usage:
    .venv/bin/python research_calculator_salarii_volumes.py

Output: markdown tables to stdout + JSON to output/keyword-volumes-calculator-salarii-<date>.json
"""

import os
import sys
import json
from datetime import datetime
from dotenv import load_dotenv

REPO = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(REPO, "data_sources/config/.env"))
sys.path.insert(0, os.path.join(REPO, "data_sources"))

from modules.dataforseo import DataForSEO

ENDPOINT = "/v3/keywords_data/google_ads/search_volume/live"

# Grouped by intent — the split matters more than the totals. See §1 of the brief.
GROUPS_RO = {
    "tool": [
        "calculator salarii", "calculator salariu", "calculator salariu net",
        "calculator salariu brut net", "calcul salariu net", "din brut in net",
        "brut net", "calculator salariu net 2026", "calculator salariu net brut",
        "calculator venit net",
    ],
    "employer_cost": [
        "cost angajator", "cost total angajator", "cat costa un angajat",
        "costul unui angajat", "calculator cost angajator",
        "calculator taxe salariale", "calculator contributii salariale",
        "impozit pe salariu",
    ],
    "it_qualified": [
        "calculator salariu it", "calculator salariu programator",
        "salariu net programator it", "taxe salariale 2026",
        "salariu brut", "salariu net", "calculator salariu 2026",
        "salariu net 2026", "calculator salariu minim",
    ],
    "adjacent": [
        "calculator salariu freelancer", "calculator pfa", "calculator impozit salariu",
    ],
}

EN = [
    "salary calculator romania", "romania salary calculator",
    "net salary calculator romania", "romania payroll calculator",
    "gross to net romania", "employer cost calculator romania",
    "romania income tax calculator", "cost of hiring in romania",
    "romania employer costs", "cost to hire a developer in romania",
    "employer of record romania", "romania payroll taxes",
]

GEOS = [
    ("Romania", "ro", "ro"),
    ("Romania", "en", "en"),
    ("United Kingdom", "en", "en"),
    ("United States", "en", "en"),
    ("Germany", "en", "en"),
]


def main():
    dfs = DataForSEO()
    total_cost = 0.0
    results = {}

    origin_ro = {kw: g for g, kws in GROUPS_RO.items() for kw in kws}
    ro_keywords = list(origin_ro)

    for loc, lang, kwset in GEOS:
        keywords = ro_keywords if kwset == "ro" else EN
        payload = [{
            "keywords": keywords,
            "location_name": loc,
            "language_code": lang,
            "search_partners": False,
        }]
        print(f"→ {loc} / {lang}: {len(keywords)} keywords", file=sys.stderr)
        resp = dfs._post(ENDPOINT, payload)
        total_cost += resp.get("cost", 0) or 0

        task = dfs._first_task(resp)
        if not task or task.get("status_code") != 20000:
            msg = (task or resp).get("status_message")
            print(f"   ✗ {msg}", file=sys.stderr)
            continue

        for it in (task.get("result") or []):
            kw = it.get("keyword")
            results.setdefault(f"{loc}|{lang}", []).append({
                "intent": origin_ro.get(kw, "en"),
                "keyword": kw,
                "search_volume": it.get("search_volume"),
                "competition": it.get("competition"),
                "cpc": it.get("cpc"),
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

    out_dir = os.path.join(REPO, "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(
        out_dir, f"keyword-volumes-calculator-salarii-{datetime.now():%Y-%m-%d}.json")
    with open(path, "w") as f:
        json.dump({"measured": datetime.now().isoformat(), "cost_usd": total_cost,
                   "results": results}, f, indent=2)

    print(f"\n\n---\n**DataForSEO cost: ${total_cost:.4f}**  ·  JSON: {path}")


if __name__ == "__main__":
    main()
