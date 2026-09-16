#!/usr/bin/env python3
"""
Test Google Analytics 4 connectivity.

Run after placing the service-account key at credentials/ga4-credentials.json
(or reusing the GSC key), setting GA4_PROPERTY_ID in data_sources/config/.env,
and granting that service account Viewer access on the GA4 property.

    .venv/bin/python test_ga.py
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()
load_dotenv('data_sources/config/.env')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'data_sources', 'modules'))

from google_analytics import GoogleAnalytics


def main():
    prop = os.getenv('GA4_PROPERTY_ID')
    cred = os.getenv('GA4_CREDENTIALS_PATH')
    blog = os.getenv('BLOG_PATH', '/blog/')

    print("=" * 60)
    print("GOOGLE ANALYTICS 4 CONNECTIVITY TEST")
    print("=" * 60)
    print(f"Property ID:     {prop}")
    print(f"Credentials:     {cred}")
    print(f"Blog path:       {blog}")

    if not prop or prop == 'your_property_id_here':
        print("\n❌ GA4_PROPERTY_ID not set in data_sources/config/.env")
        sys.exit(1)

    if not cred or not os.path.exists(cred):
        print("\n❌ Credentials file not found.")
        print("   Create a service-account key and save it to credentials/ga4-credentials.json")
        print("   (or reuse the GSC key). See data_sources/config/.env.example.")
        sys.exit(1)

    try:
        ga = GoogleAnalytics()
    except Exception as e:
        print(f"\n❌ Failed to initialize client: {e}")
        sys.exit(1)

    print("\n✅ Client initialized. Fetching last 28 days of top pages...\n")

    try:
        pages = ga.get_top_pages(days=28, limit=10, path_filter=blog)
    except Exception as e:
        print(f"❌ API call failed: {e}")
        sys.exit(1)

    if not pages:
        print("⚠️  No rows returned. Check the property ID, date range, or blog path filter.")
        sys.exit(0)

    for i, page in enumerate(pages, 1):
        print(f"{i}. {page['title']}")
        print(f"   {page['path']}")
        print(f"   {page['pageviews']:,} pageviews | {page['engagement_rate']:.1%} engagement")
        print()

    print("✅ GA4 integration working.")


if __name__ == "__main__":
    main()
