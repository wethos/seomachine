#!/usr/bin/env python3
"""
Test Google Search Console connectivity.

Run after placing the service-account key at credentials/gsc-credentials.json
and granting that service account access to the wise-step.ro property.

    .venv/bin/python test_gsc.py
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()
load_dotenv('data_sources/config/.env')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'data_sources', 'modules'))

from google_search_console import GoogleSearchConsole


def main():
    site = os.getenv('GSC_SITE_URL')
    cred = os.getenv('GSC_CREDENTIALS_PATH')

    print("=" * 60)
    print("GOOGLE SEARCH CONSOLE CONNECTIVITY TEST")
    print("=" * 60)
    print(f"Site URL:        {site}")
    print(f"Credentials:     {cred}")

    if not cred or not os.path.exists(cred):
        print("\n❌ Credentials file not found.")
        print("   Create a service-account key and save it to credentials/gsc-credentials.json")
        print("   (see the setup steps in data_sources/config/.env.example).")
        sys.exit(1)

    try:
        gsc = GoogleSearchConsole()
    except Exception as e:
        print(f"\n❌ Failed to initialize client: {e}")
        sys.exit(1)

    print("\n✅ Client initialized. Fetching last 28 days of top queries...\n")

    try:
        rows = gsc.get_keyword_positions(days=28, limit=10)
    except Exception as e:
        print(f"❌ API call failed: {e}")
        print("\n   Common causes:")
        print("   - Service account not added as a user on the Search Console property")
        print("   - Search Console API not enabled in the Google Cloud project")
        print("   - GSC_SITE_URL doesn't match the property exactly "
              "(domain property must be 'sc-domain:wise-step.ro')")
        sys.exit(1)

    if not rows:
        print("⚠️  Connected, but no query data returned yet "
              "(new property or no search traffic in the window).")
        print("   The integration works — data will appear as impressions accrue.")
        return

    print(f"Top {len(rows)} queries by impressions:\n")
    print(f"{'Query':<45} {'Pos':>5} {'Impr':>8} {'Clicks':>7}")
    print("-" * 68)
    for kw in rows:
        print(f"{kw['keyword'][:44]:<45} {kw['position']:>5} "
              f"{kw['impressions']:>8,} {kw['clicks']:>7,}")

    print("\n✅ Google Search Console integration is working.")


if __name__ == "__main__":
    main()
