#!/usr/bin/env python3
"""
Research Keyword Volumes — DataForSEO Google Ads Search Volume (live)

Measures monthly search volume + competition for the Wise Step target-keyword
clusters. Mirrors the method used for Cluster 5 on 2026-08-12.

Usage:
    .venv/bin/python research_keyword_volumes.py [--clusters 1,3,4,6]

Output: markdown tables to stdout + JSON to output/keyword-volumes-<date>.json
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

ENDPOINT = "/v3/keywords_data/google_ads/search_volume/live"

CLUSTERS = {
    "1": {
        "name": "IT Recruitment Romania (core/commercial)",
        "en": [
            "it recruitment romania", "it recruitment agency romania",
            "tech recruitment agency romania", "software developer recruitment romania",
            "it staffing romania", "hire software engineers romania",
            "tech recruiters romania", "recruitment agency timisoara",
            "recruitment agency bucharest", "recruitment agency cluj",
            "best it recruitment agency in romania", "how to hire developers in romania",
            "outsourced tech recruitment romania", "it recruitment services for startups",
            "specialist vs generalist it recruiter",
        ],
        "ro": [
            "agentie recrutare it", "recrutare it", "recrutare it romania",
            "firma de recrutare it", "agentie de recrutare timisoara",
            "agentie de recrutare bucuresti", "recrutare personal it",
            "agentie recrutare", "servicii de recrutare",
        ],
    },
    "2": {
        "name": "AI, ML & Data Science Recruitment",
        "en": [
            "hire machine learning engineers", "data engineer recruitment",
            "ai engineer hiring", "mlops recruitment", "data scientist recruitment",
            "data science recruitment", "ai recruitment romania",
            "how to hire a machine learning engineer", "where to find data engineers",
            "recruiting ai talent in europe", "how to assess an ml engineer",
            "hiring data science teams", "ml engineer salary romania",
            "data engineer vs data scientist", "applied ai engineer hiring",
        ],
        "ro": [
            "recrutare data science", "inginer machine learning", "salariu data scientist",
            "salariu inginer ml", "recrutare ai", "job data scientist romania",
        ],
    },
    "7": {
        "name": "Emerging Roles & AI-Native Engineering",
        "en": [
            "ai native engineering", "forward deployed engineer",
            "what is a forward deployed engineer", "how to hire a forward deployed engineer",
            "applied ai engineer", "what is an applied ai engineer",
            "ai native startup hiring", "new engineering roles",
            "hiring for ai first teams", "new tech roles 2026",
            "how ai is changing engineering hiring", "ai engineer skills",
        ],
        "ro": [
            "inginer ai", "roluri noi in it", "meserii viitor it",
        ],
    },
    "8": {
        "name": "Compliance & Candidate-Side",
        "en": [
            "eu ai act recruitment", "eu ai act hiring", "ai in recruitment regulation",
            "ats friendly cv", "how to pass ats", "ats resume format",
            "tech cv tips", "is ai hiring legal", "ai hiring compliance",
            "ats cv checker", "cv for software engineer",
        ],
        "ro": [
            "cv ats", "cv optimizat pentru ats", "cum sa scrii un cv",
            "eu ai act", "cv programator", "model cv",
        ],
    },
    "3": {
        "name": "Cloud & DevOps Recruitment",
        "en": [
            "devops recruitment", "devops recruitment romania", "hire devops engineers",
            "hire devops engineers romania", "sre recruitment", "cloud engineer recruitment",
            "platform engineer hiring", "kubernetes engineer recruitment",
            "aws engineer hiring", "how to hire a devops engineer", "devops vs sre",
            "screening questions for cloud engineers", "remote devops hiring",
            "hiring platform engineering teams", "devops engineer salary romania",
        ],
        "ro": [
            "recrutare devops", "inginer devops", "salariu devops",
            "salariu inginer cloud", "job devops romania",
        ],
    },
    "4": {
        "name": "Executive Search & Headhunting",
        "en": [
            "headhunting romania", "executive search romania", "tech executive search",
            "hire a cto", "hire a vp of engineering", "technical leadership recruitment",
            "headhunting services", "passive candidate sourcing",
            "engineering manager recruitment", "how to headhunt a cto",
            "retained executive search", "how to hire a head of data",
            "executive search fees", "headhunting vs job ads",
        ],
        "ro": [
            "headhunting", "headhunting romania", "firma executive search",
            "recrutare manageri", "vanatoare de capete recrutare",
        ],
    },
    "6": {
        "name": "Hiring in Romania / CEE",
        "en": [
            "hire remote developers romania", "hiring in eastern europe",
            "hire developers eastern europe", "open a tech office in romania",
            "build an engineering team romania", "nearshore software development romania",
            "romania tech talent pool", "it recruitment trends eastern europe",
            "romania vs poland developers", "hire your first engineer in romania",
            "nearshoring to romania", "romania software development outsourcing",
            "eastern europe developer rates", "why hire developers in romania",
        ],
        "ro": [
            "externalizare it", "nearshoring romania", "piata it romania",
            "companii it romania",
        ],
    },
}

# (location_name, language_code, which keyword set)
GEOS = [
    ("Romania", "en", "en"),
    ("Romania", "ro", "ro"),
    ("United Kingdom", "en", "en"),
    ("United States", "en", "en"),
    ("Germany", "en", "en"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--clusters", default="1,3,4,6")  # or 2,7,8
    args = ap.parse_args()
    picked = [c.strip() for c in args.clusters.split(",")]

    dfs = DataForSEO()
    total_cost = 0.0
    results = {}

    for loc, lang, kwset in GEOS:
        keywords, origin = [], {}
        for c in picked:
            for kw in CLUSTERS[c].get(kwset, []):
                if kw not in origin:
                    keywords.append(kw)
                    origin[kw] = c
        if not keywords:
            continue

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
            print(f"   ✗ {task.get('status_message') if task else resp.get('status_message')}",
                  file=sys.stderr)
            continue

        items = task.get("result") or []
        for it in items:
            kw = it.get("keyword")
            results.setdefault(f"{loc}|{lang}", []).append({
                "cluster": origin.get(kw, "?"),
                "keyword": kw,
                "search_volume": it.get("search_volume"),
                "competition": it.get("competition"),
                "competition_index": it.get("competition_index"),
                "cpc": it.get("cpc"),
                "low_bid": it.get("low_top_of_page_bid"),
                "high_bid": it.get("high_top_of_page_bid"),
            })

    # Report
    for geo, rows in results.items():
        loc, lang = geo.split("|")
        measurable = [r for r in rows if (r["search_volume"] or 0) > 0]
        zero = [r for r in rows if not r["search_volume"]]
        print(f"\n\n## {loc} / {lang} — {len(measurable)} with volume, {len(zero)} at zero\n")
        if measurable:
            print("| Cluster | Keyword | Volume | Competition | CPC |")
            print("|---|---|---|---|---|")
            for r in sorted(measurable, key=lambda x: -(x["search_volume"] or 0)):
                cpc = f"${r['cpc']:.2f}" if r.get("cpc") else "—"
                print(f"| {r['cluster']} | {r['keyword']} | **{r['search_volume']}** | "
                      f"{r['competition'] or '—'} | {cpc} |")
        if zero:
            print(f"\n**No measurable volume:** " + " · ".join(sorted(r["keyword"] for r in zero)))

    out_dir = os.path.join(REPO, "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"keyword-volumes-{datetime.now():%Y-%m-%d}.json")
    with open(path, "w") as f:
        json.dump({"measured": datetime.now().isoformat(), "cost_usd": total_cost,
                   "clusters": picked, "results": results}, f, indent=2)

    print(f"\n\n---\n**DataForSEO cost: ${total_cost:.4f}**  ·  JSON: {path}")


if __name__ == "__main__":
    main()
