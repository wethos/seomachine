# Internal Links Map

Catalogs key Wise Step Recruiting pages (wise-step.ro) to reference in blog content for strategic internal linking. Go-to reference when adding internal links to articles.

**RO versions:** verified live 2026-08-12 by crawling `/blog/` and `/ro/blog/`; tool pages added 2026-09-03. There are **three** different rules, and getting them backwards breaks every link in an RO article:

- **RO blog posts** take the EN slug plus a **`-ro` suffix**: `https://wise-step.ro/ro/blog/[en-slug]-ro/`. Example: `/blog/headhunting-romania/` → `/ro/blog/headhunting-romania-ro/`.
- **RO core pages** take **no suffix**: `https://wise-step.ro/ro/[page]/`. Confirmed live: `/ro/services/`, `/ro/contact/`.
- **RO tool pages take a fully translated slug and no suffix** — a third pattern, added 2026-09-03. Confirmed live: `/salary-calculator/` → **`/ro/calculator-salariu/`**. Neither of the first two rules produces this: the core-page rule would give `/ro/salary-calculator/` and the blog rule `/ro/blog/salary-calculator-ro/`. **Both are wrong.** Always take the tool URLs from the Tools section below.
- **Two blog exceptions**, so the RO slug is *not* mechanically derivable — always check the table:
  - `/ro/blog/cv-optimizat-pentru-ats/` — fully translated, no suffix
  - `/ro/blog/eu-ai-act-recrutare-ro/` — slug differs from the EN one *and* takes the suffix
  - `/ro/blog/cat-costa-un-angajat-romania/` — fully translated, no suffix. **Live, verified 200 on 2026-09-03.** Note the EN slug is `employee-taxes-total-cost-romania`, so the pair is not derivable in either direction. **Deliberate:** the mechanical `-ro` form would have been `/ro/blog/cost-of-an-employee-romania-ro/`, which throws away the Romanian keyword on the higher-value half of the pair — `cât costă un angajat` is the phrase that carries a Google AI Overview. Follows the `cv-optimizat-pentru-ats` precedent.

⚠️ This entry previously stated the RO pattern was "same slug as EN, prefixed with `/ro`." That was wrong. Check the table below (or the live `/ro/blog/` index) before adding an RO link — never derive an RO blog URL by prefixing alone. Note that `style-guide.md` still says "mirror the slug in Romanian," which matches only the ATS exception; this file is the authority.

### EN ↔ RO slug map (verified 2026-08-12)

| EN post | RO post |
|---|---|
| /blog/applied-ai-engineer/ | /ro/blog/applied-ai-engineer-ro/ |
| /blog/ai-native-engineering/ | /ro/blog/ai-native-engineering-ro/ |
| /blog/ats-friendly-cv/ | /ro/blog/cv-optimizat-pentru-ats/ ← exception |
| /blog/eu-ai-act-recruitment/ | /ro/blog/eu-ai-act-recrutare-ro/ |
| /blog/ai-recruitment-agency-romania/ | /ro/blog/ai-recruitment-agency-romania-ro/ |
| /blog/it-recruitment-trends-eastern-europe-2026/ | /ro/blog/it-recruitment-trends-eastern-europe-2026-ro/ |
| /blog/it-salaries-romania-2026/ | /ro/blog/it-salaries-romania-2026-ro/ |
| /blog/hire-remote-developers-romania/ | /ro/blog/hire-remote-developers-romania-ro/ |
| /blog/ai-data-science-recruitment-romania/ | /ro/blog/ai-data-science-recruitment-romania-ro/ |
| /blog/headhunting-romania/ | /ro/blog/headhunting-romania-ro/ |
| /blog/employee-taxes-total-cost-romania/ | /ro/blog/cat-costa-un-angajat-romania/ ← exception |

For each page: **URL**, **When to Link**, **Anchor Text Examples**.

---

## Homepage & Core Pages

### Homepage
- **URL**: https://wise-step.ro/
- **When to Link**: Rarely — only when referencing Wise Step broadly
- **Anchor Text Examples**: "Wise Step", "Wise Step Recruiting", "our team"

### About
- **URL**: https://wise-step.ro/about/
- **When to Link**: When discussing the "engineers who recruit" story, founders' backgrounds, or approach
- **Anchor Text Examples**: "engineers who recruit", "our background", "who we are", "former software engineers"

### Services
- **URL**: https://wise-step.ro/services/
- **When to Link**: When discussing what we do — placement, headhunting, team build-out, market intelligence
- **Anchor Text Examples**: "our recruitment services", "how we work", "technical recruitment services"

### Jobs
- **URL**: https://wise-step.ro/jobs/
- **When to Link**: In candidate-facing content, or when discussing open roles / the talent network
- **Anchor Text Examples**: "open roles", "current openings", "see our jobs"

### Contact
- **URL**: https://wise-step.ro/contact/
- **When to Link**: CTAs — inviting readers to brief a search or book a discovery call
- **Anchor Text Examples**: "get in touch", "brief your search", "talk to a founder", "book a discovery call"

### Blog
- **URL**: https://wise-step.ro/blog/
- **When to Link**: When pointing to the broader content library
- **Anchor Text Examples**: "our blog", "more on the tech hiring market", "recruitment insights"

### Privacy / Terms
- **URL**: https://wise-step.ro/privacy/ · https://wise-step.ro/terms/
- **When to Link**: Footer/compliance only — not in editorial content
- **Anchor Text Examples**: "privacy policy", "terms & conditions"

---

## Tools

Free, interactive assets. Different linking logic from blog posts: link them wherever an article states or implies a **specific number**, because the tool is what the reader does next with that number. They are also the site's most linkable pages — a free calculator earns external links that a services page never will.

### Salary calculator (gross → net → employer cost)
- **URL**: https://wise-step.ro/salary-calculator/
- **RO URL**: https://wise-step.ro/ro/calculator-salariu/ ← **fully translated slug, no `-ro` suffix.** Do not derive it; copy it.
- **Live since**: 2026-09-03
- **What it does**: gross monthly salary + dependants + children in school + principal function + under-26 → net salary, full contribution breakdown (CAS 25%, CASS 10%, income tax, personal deduction, taxable base), CAM 2.25%, and total employer cost.
- **When to Link**:
  - Any article quoting a **gross** figure — the reader's immediate next question is what it nets
  - Any article quoting a **net** figure — same in reverse
  - Employer-cost, hiring-budget, or "what does a hire cost" content
  - Salary-negotiation and offer content (candidate-side)
  - **Mandatory both ways with the salary pillar** — `/blog/it-salaries-romania-2026/` should link out to the calculator, and the calculator links back to the pillar. That pairing is currently missing on the live site (see `research/brief-calculator-salarii-2026-09-02.md` §8, fix 4).
- **Anchor Text Examples (EN)**: "salary calculator for Romania", "gross-to-net calculator", "work out the total employer cost", "see what that gross actually nets"
- **Anchor Text Examples (RO)**: "calculator salariu net", "calculator de salarii", "calculează din brut în net", "costul total pentru angajator"

⚠ **Use `calculator salariu net` as the primary RO anchor.** It is the highest-volume term in the entire keyword portfolio (**90,500/mo**, measured 2026-09-03 — see `target-keywords.md` Cluster 5), and the live page does not yet match it in its title or H1. Internal anchors are one of the few levers available before that is fixed. Vary the anchor across articles as usual — do not repeat one phrase site-wide.

---

## Service Lines

All six service lines are described on the single **/services/** page — there are no individual per-service URLs yet. Link the relevant anchor text to `https://wise-step.ro/services/` (deep-link to a section anchor if one exists on-page). If dedicated service pages launch later, add their URLs here.

| Service | Link target | When to Link | Anchor Text Examples |
|---------|-------------|--------------|----------------------|
| Permanent Placement | /services/ | Full-time hiring, junior→senior engineers | "permanent placement", "full-cycle recruitment" |
| Executive Search | /services/ | Leadership hires, confidential/passive candidates | "executive search", "confidential headhunting" |
| Team Build-Out | /services/ | Scaling a team, first office in Romania | "team build-out", "build your engineering team" |
| Contract & Freelance | /services/ | Project-based / contractor needs | "contract & freelance", "specialist contractors" |
| Retained Search | /services/ | Business-critical or hard-to-fill roles | "retained search", "dedicated search engagement" |
| Market Intelligence | /services/ | Salary/talent-density data, market benchmarks | "market intelligence", "salary benchmarking", "talent availability reports" |

*Note: no public pricing page — fees are quoted per engagement. Do not link to or imply a pricing page.*

---

## Pillar Blog Content

Wise Step's best content to link to frequently. All under `https://wise-step.ro/blog/[slug]/`.

### AI-native engineering
- **URL**: https://wise-step.ro/blog/ai-native-engineering/
- **Primary Topic**: What AI-native engineering is + how to hire for it
- **When to Link**: Articles on AI/ML hiring, emerging roles (FDEs, Applied AI Engineers), new skill demand
- **Anchor Text Examples**: "AI-native engineering", "hiring for AI-native roles", "what AI-native engineering means"

### AI recruitment agency Romania
- **URL**: https://wise-step.ro/blog/ai-recruitment-agency-romania/
- **Primary Topic**: AI/data/DevOps recruitment in Romania (core positioning piece)
- **When to Link**: Articles about hiring AI/data/DevOps talent in Romania; strong commercial-intent target
- **Anchor Text Examples**: "AI recruitment agency in Romania", "hiring AI and DevOps talent in Romania"

### AI, ML & Data Science recruitment in Romania
- **URL**: https://wise-step.ro/blog/ai-data-science-recruitment-romania/
- **Primary Topic**: Recruiting AI/ML/data science engineers in Romania
- **When to Link**: Data/AI hiring topics, scarce-role sourcing, technical assessment
- **Anchor Text Examples**: "AI and data science recruitment", "hiring ML engineers in Romania"

### Headhunting services in Romania
- **URL**: https://wise-step.ro/blog/headhunting-romania/
- **Primary Topic**: Headhunting / passive-candidate search in Romania
- **When to Link**: Executive search, passive candidates, senior/leadership hiring
- **Anchor Text Examples**: "headhunting in Romania", "reach passive candidates", "executive search"

### Hire remote developers in Romania
- **URL**: https://wise-step.ro/blog/hire-remote-developers-romania/
- **Primary Topic**: 2026 playbook for hiring remote AI/ML/data teams in Romania
- **When to Link**: Remote hiring, scaling remote teams, first office in Romania
- **Anchor Text Examples**: "hire remote developers in Romania", "remote hiring playbook", "scaling a remote team"

### IT salaries in Romania 2026
- **URL**: https://wise-step.ro/blog/it-salaries-romania-2026/
- **Primary Topic**: Complete guide to Romanian IT salaries 2026
- **When to Link**: Anything referencing salary bands, cost, compensation, market intelligence — high link value
- **Anchor Text Examples**: "IT salaries in Romania", "2026 Romanian salary guide", "developer salary benchmarks"

### IT recruitment trends in Eastern Europe 2026
- **URL**: https://wise-step.ro/blog/it-recruitment-trends-eastern-europe-2026/
- **Primary Topic**: CEE/Eastern Europe tech hiring trends 2026
- **When to Link**: Market-movement takes, "speed play" narrative, CEE hiring context
- **Anchor Text Examples**: "IT recruitment trends in Eastern Europe", "the CEE tech hiring market", "Eastern Europe hiring in 2026"

### EU AI Act and recruitment
- **URL**: https://wise-step.ro/blog/eu-ai-act-recruitment/
- **Primary Topic**: What the EU AI Act means for tech employers hiring in 2026
- **When to Link**: Compliance, AI regulation, hiring-process/legal topics
- **Anchor Text Examples**: "EU AI Act and recruitment", "what the AI Act means for hiring"

### Applied AI Engineer
- **URL**: https://wise-step.ro/blog/applied-ai-engineer/ · RO: /ro/blog/applied-ai-engineer-ro/
- **Primary Topic**: What an applied AI engineer does and what the role costs in 2026
- **When to Link**: Emerging AI roles, AI/ML hiring, compensation for scarce AI profiles
- **Anchor Text Examples**: "what an applied AI engineer does", "hiring applied AI engineers", "the applied AI engineer role"

### ATS-friendly CV in 2026
- **URL**: https://wise-step.ro/blog/ats-friendly-cv/
- **Primary Topic**: Writing an ATS-friendly CV (candidate-side)
- **When to Link**: Candidate-facing content, CV/application advice
- **Anchor Text Examples**: "ATS-friendly CV", "write a CV that passes ATS", "CV tips for 2026"

---

## Internal Linking Best Practices

1. **Link naturally** — only when genuinely relevant and helpful
2. **Vary anchor text** — different phrases for the same URL (see brand-voice: descriptive, no "click here")
3. **3–5 links per post** — strategic, not stuffed
4. **Deep-link** — link to the specific service/blog page, not just the homepage
5. **Early links matter** — links in the first few paragraphs carry more weight
6. **Mirror across EN/RO** — link EN posts to EN targets, RO to RO (confirm RO path first)
7. **Keep this map updated** — add new blog posts and any new service/landing pages as they publish

---

## Quick Reference by Topic

**Salary / compensation / cost** → link:
- /blog/it-salaries-romania-2026/ — the salary guide (primary)
- **/salary-calculator/** · RO **/ro/calculator-salariu/** — the calculator, whenever a specific gross or net figure appears
- /services/ — Market Intelligence line

**AI / ML / data hiring** → link:
- /blog/ai-data-science-recruitment-romania/ — data/AI recruitment
- /blog/ai-recruitment-agency-romania/ — commercial positioning piece
- /blog/ai-native-engineering/ — emerging AI roles

**Senior / leadership / passive candidates** → link:
- /blog/headhunting-romania/ — headhunting
- /services/ — Executive Search + Retained Search

**Remote / scaling / first office in Romania** → link:
- /blog/hire-remote-developers-romania/ — remote hiring playbook
- /services/ — Team Build-Out

**CEE / Eastern Europe market** → link:
- /blog/it-recruitment-trends-eastern-europe-2026/ — trends piece

**Compliance / AI regulation** → link:
- /blog/eu-ai-act-recruitment/ — EU AI Act

**Candidate-facing (CVs, applications, jobs)** → link:
- /blog/ats-friendly-cv/ — ATS CV guide
- **/salary-calculator/** · RO **/ro/calculator-salariu/** — offer evaluation and salary negotiation
- /jobs/ — open roles

**Company / credibility / CTA** → link:
- /about/ — engineers-who-recruit story
- /contact/ — brief a search / book a call

---

*Keep updated as new content publishes or the site restructures. RO URL pattern confirmed and mapped 2026-08-12, third pattern (tool pages) added 2026-09-03 (see top of file) — that open item is closed. Re-crawl `/blog/` and `/ro/blog/` periodically to catch new posts and to confirm the `-ro` suffix convention still holds for anything newly published.*
