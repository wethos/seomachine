# Target Keywords & Topic Clusters

Organises Wise Step Recruiting's target keywords by topic cluster for content planning and SEO/AEO. Update from keyword research and performance.

**Metrics note:** search volume / difficulty are marked **[TBD]** where not yet researched. Pull real figures via this repo's DataForSEO scripts (`research_topic_clusters.py`, `research_serp_analysis.py`, `research_quick_wins.py`) and Google Search Console — never fill in estimated numbers (our voice bars invented figures). Map keywords to the live blog posts in `internal-links-map.md`.

**Measured so far:** Cluster 5 (IT Salaries) — DataForSEO Google Ads live, 2026-08-12. **Clusters 1, 2, 3, 4, 6, 7, 8 — DataForSEO Google Ads live, 2026-08-21**, across five geo/language pairs (RO/en, RO/ro, UK/en, US/en, DE/en); raw JSON in `output/`, re-runnable via `research_keyword_volumes.py`. **All eight clusters now measured.** **Cluster 5 extended 2026-09-03** with the salary-calculator and employer-cost query families (volumes + live Google SERP positions), re-runnable via `research_calculator_salarii_volumes.py`.

**Headline result (2026-08-21) — the portfolio splits cleanly in two.**

*Traffic clusters (candidate-side, huge, already half-built):* **Cluster 7** — `forward deployed engineer` **18,100/mo US**, LOW competition, 22× anything else measured, and two pillar posts already live. **Cluster 8** — `model cv` **8,100/mo RO**, `ats cv checker` 12,100 US, `eu ai act` 480 RO. *(Correction 2026-09-03: `model cv` was recorded here as the largest Romanian term found. It is not — `calculator salariu net` is **90,500/mo RO**, measured in Cluster 5. See that cluster before quoting any "largest term" figure; note the calculator volume is almost entirely unreachable organically.)* Both were filed "low priority / supporting". On volume, they are the biggest assets Wise Step has. Both are candidate-side: measure on citations, links and branded search, **never on briefed searches**.

*Commercial clusters (tiny, expensive, where the leads are):* **Cluster 4 (Executive Search & Headhunting) is the strongest commercial cluster** — the only one with both measurable Romanian demand (`executive search romania` 70/mo, `headhunting romania` 50/mo in each language) and high-value Western demand (`retained executive search` 590/mo US at $80.44 CPC). Cluster 3 (Cloud/DevOps) has almost no Romania-qualified volume, but carries the single highest-value term measured anywhere: `hire devops engineers`, 170/mo US at **$372.04 CPC**. Cluster 1's EN IT-specific terms are near-dead; the RO generalist term `agentie recrutare` (170/mo) carries it, and **Bucharest outranks Timișoara 5:1** on agency queries.

**Standing finding, applies across clusters:** on salary and market topics, Romanian search volume runs roughly 8–15× the English equivalent — and on calculator/tax queries the gap is far wider still (`calculator salariu net` 90,500 RO vs `salary calculator romania` 320 RO/en = **283×**, measured 2026-09-03). The default EN-first order is wrong for this cluster — write RO as the original and translate outward. Re-test before assuming it generalises to the commercial clusters.

**Note on running DataForSEO:** use the venv and load the env file explicitly — `load_dotenv()` alone fails because the credentials live at `data_sources/config/.env`, not the repo root. `.venv/bin/python` with `load_dotenv("data_sources/config/.env")`.

Focus market: **Romania / CEE tech recruitment**, specialisation in Cloud/DevOps and Data/AI, mid-level through executive. Content ships EN + RO.

---

## Topic Cluster Structure

Each cluster has:
- **Pillar keyword**: main, higher-volume, usually commercial
- **Cluster keywords**: 5–10 related subtopics
- **Long-tail**: 10–15 specific lower-volume phrases
- **Intent**: informational / commercial / transactional
- **Pillar URL**: mapped live post, or "To create"

---

## Cluster 1: IT Recruitment Romania (core / commercial)

### Pillar Keyword
- **Keyword**: IT recruitment Romania (aka "IT recruitment agency Romania")
- **Volume / Difficulty**: measured 2026-08-21 — **10/mo** (RO, en). The RO-language generalist terms carry this cluster, not the EN IT-specific ones.
- **Intent**: Commercial
- **Pillar URL**: https://wise-step.ro/blog/ai-recruitment-agency-romania/ (commercial positioning piece; consider a dedicated "IT recruitment agency Romania" pillar)

### Measured volumes — DataForSEO Google Ads live, 2026-08-21

| Keyword | Geo / lang | Monthly volume | Competition | CPC |
|---|---|---|---|---|
| agentie recrutare | RO / ro | **170** | MEDIUM | $0.73 |
| recruitment agency bucharest | RO / en | **50** | HIGH | $1.37 |
| agentie de recrutare bucuresti | RO / ro | **40** | MEDIUM | $0.71 |
| it recruitment romania | US / en | 20 | — | — |
| agentie recrutare it | RO / ro | 10 | LOW | — |
| recrutare it | RO / ro | 10 | LOW | — |
| agentie de recrutare timisoara | RO / ro | 10 | MEDIUM | $0.72 |
| servicii de recrutare | RO / ro | 10 | HIGH | — |
| it recruitment romania | RO / en · UK / en · DE / en | 10 each | — | — |
| it recruitment agency romania | RO / en · UK / en · US / en · DE / en | 10 each | DE HIGH | — |

**Two findings that change targeting:**
1. **Bucharest outranks Timișoara 5:1** (`recruitment agency bucharest` 50 + `agentie de recrutare bucuresti` 40 vs `agentie de recrutare timisoara` 10). The HQ city is not where the demand is. A Bucharest-facing page is justified; a Cluj page is not (`recruitment agency cluj` — no measurable volume).
2. **The generalist RO term beats every IT-specific one.** `agentie recrutare` (170) is 17× `agentie recrutare it` (10). Specialisation is the sales differentiator, not the search entry point — capture the generalist query, qualify on the page.

**No measurable volume** (do not target as primary): tech recruitment agency Romania · software developer recruitment Romania · IT staffing Romania · hire software engineers Romania · tech recruiters Romania · recruitment agency Cluj · best IT recruitment agency in Romania · how to hire developers in Romania · outsourced tech recruitment Romania · IT recruitment services for startups · specialist vs generalist IT recruiter · firma de recrutare it · recrutare it romania · recrutare personal it

### Long-Tail
- best IT recruitment agency in Romania
- how to hire developers in Romania
- IT recruitment services for startups Romania
- outsourced tech recruitment Romania
- recruit engineers for a Romanian office
- specialist vs generalist IT recruiter Romania
- contingency vs retained IT recruitment Romania

### Related Questions (natural prompt language)
- How do I hire software engineers in Romania?
- What does an IT recruitment agency in Romania cost? *(answer without publishing fee % — see `features.md`)*
- Is it better to use a specialist or generalist tech recruiter?
- How long does it take to fill a tech role in Romania? *(28–30 days)*

---

## Cluster 2: AI, ML & Data Science Recruitment

### Pillar Keyword
- **Keyword**: AI recruitment Romania / data science recruitment
- **Volume / Difficulty**: measured 2026-08-21 — **`ai recruitment romania` returned zero in every geo.** The cluster's real volume is one informational term (`data engineer vs data scientist`, 1,600/mo US) and one very-high-CPC commercial term (`ai engineer hiring`, $44.13 US).
- **Intent**: Commercial
- **Pillar URL**: https://wise-step.ro/blog/ai-data-science-recruitment-romania/

### Measured volumes — DataForSEO Google Ads live, 2026-08-21

| Keyword | Geo / lang | Monthly volume | Competition | CPC |
|---|---|---|---|---|
| data engineer vs data scientist | US / en | **1,600** | LOW | $8.24 |
| data engineer vs data scientist | UK / en | **260** | LOW | $0.80 |
| hire machine learning engineers | US / en | **140** | LOW | — |
| data engineer vs data scientist | DE / en | **110** | LOW | $0.24 |
| data scientist recruitment · data science recruitment | UK / en | 50 each | LOW | $1.59 |
| data scientist recruitment · data science recruitment | US / en | 50 each | LOW | $5.80 |
| ai engineer hiring | US / en | 40 | MEDIUM | **$44.13** |
| data engineer recruitment | US / en | 30 | LOW | — |
| data engineer recruitment | UK / en | 20 | MEDIUM | $3.67 |
| data engineer vs data scientist | RO / en | 20 | LOW | — |
| hire machine learning engineers | UK / en | 20 | LOW | — |
| ai engineer hiring | UK / en | 10 | HIGH | $7.19 |
| hire machine learning engineers · ai engineer hiring | RO / en | 10 each | — | — |

**Reading:** the commercial terms are thin but expensive — `ai engineer hiring` at **$44.13 CPC** is the second-highest price measured across all seven clusters (behind `hire devops engineers` at $372). The traffic term is `data engineer vs data scientist` (1,600 US / 260 UK / 110 DE) — a definitional query that a recruiter who actually places both roles can answer better than anyone, and a natural top-of-funnel entry to the existing pillar.

**No measurable volume** (do not target as primary): AI recruitment Romania · MLOps recruitment · data scientist recruitment Romania · applied AI engineer hiring · how to assess an ML engineer · where to find data engineers · hiring data science teams · recruiting AI talent in Europe · ML engineer salary Romania · recrutare data science · inginer machine learning · salariu data scientist · salariu inginer ml · recrutare ai · job data scientist romania

### Long-Tail
- how to hire a machine learning engineer
- where to find data engineers in Romania
- recruiting AI talent in Eastern Europe
- how to assess an ML engineer's skills
- hiring data science teams in Romania
- AI engineer salary vs skills in Romania
- what to look for when hiring a data engineer

### Related Questions
- How do you screen a machine learning engineer?
- Where is the best place to hire AI talent in Europe?
- What's the difference between a data engineer and a data scientist hire?
- How scarce are ML engineers in Romania?

---

## Cluster 3: Cloud & DevOps Recruitment

### Pillar Keyword
- **Keyword**: DevOps recruitment / cloud engineer hiring
- **Volume / Difficulty**: measured 2026-08-21 — **near zero in Romania; the demand is US/UK**. `devops recruitment` 50/mo UK at **$16.80 CPC**, 50/mo US. Romania-qualified variants have no measurable volume.
- **Intent**: Commercial
- **Pillar URL**: To create (strong specialisation fit — no dedicated post yet)

### Measured volumes — DataForSEO Google Ads live, 2026-08-21

| Keyword | Geo / lang | Monthly volume | Competition | CPC |
|---|---|---|---|---|
| devops vs sre | US / en | **210** | LOW | — |
| hire devops engineers | US / en | **170** | LOW | **$372.04** |
| devops recruitment | UK / en | **50** | LOW | **$16.80** |
| devops recruitment | US / en | **50** | LOW | — |
| devops vs sre | UK / en | 30 | LOW | — |
| devops vs sre | DE / en | 20 | LOW | — |
| salariu devops | RO / ro | 20 | LOW | — |
| hire devops engineers | UK / en | 10 | MEDIUM | $7.67 |
| sre recruitment / cloud engineer recruitment | RO·UK·US·DE / en | 10 each | — | — |
| how to hire a devops engineer | UK / en · US / en | 10 each | LOW | — |
| devops engineer salary romania | all four geos | 10 each | LOW | — |
| inginer devops | RO / ro | 10 | LOW | — |

**The commercial reading:** `hire devops engineers` at a **$372 CPC** is the highest-value term measured across every cluster — that is what the market pays per click for this buyer. Volume is 170/mo and it sits in the **US**, not Romania. `devops vs sre` (210 US, 30 UK, 20 DE) is the informational entry point to the same buyer.

**Consequence for this cluster:** the pillar is justified by AEO, specialisation credibility and CPC value — **not by Romanian search traffic, which does not exist here.** Write it geo-neutral ("hiring DevOps and SRE engineers", with Romania as the supply answer) rather than geo-qualified, or it targets a query nobody runs.

**No measurable volume** (do not target as primary): hire DevOps engineers Romania · devops recruitment Romania · platform engineer hiring · Kubernetes engineer recruitment · AWS engineer hiring · hiring platform engineering teams · screening questions for cloud engineers · remote DevOps hiring · recrutare devops · job devops romania · salariu inginer cloud

### Long-Tail
- how to hire a DevOps engineer
- where to find SRE talent in Romania
- screening questions for cloud engineers
- hiring platform engineering teams
- DevOps vs SRE — which role to hire
- cost of hiring a DevOps engineer in Romania
- remote DevOps hiring Eastern Europe

### Related Questions
- How do you assess a DevOps engineer in an interview?
- What's the difference between DevOps and SRE roles?
- Are cloud engineers hard to hire in Romania?

---

## Cluster 4: Executive Search & Headhunting

### Pillar Keyword
- **Keyword**: headhunting Romania / tech executive search
- **Volume / Difficulty**: measured 2026-08-21 — **the strongest commercial cluster we have.** `executive search romania` 70/mo (RO, en, LOW comp, $2.84 CPC); `headhunting romania` 50/mo in RO-en *and* 50/mo in RO-ro = ~100 combined.
- **Intent**: Commercial
- **Pillar URL**: https://wise-step.ro/blog/headhunting-romania/

### Measured volumes — DataForSEO Google Ads live, 2026-08-21

| Keyword | Geo / lang | Monthly volume | Competition | CPC |
|---|---|---|---|---|
| retained executive search | US / en | **590** | LOW | **$80.44** |
| headhunting services | US / en | **320** | MEDIUM | $11.20 |
| retained executive search | UK / en | **90** | LOW | — |
| executive search romania | RO / en | **70** | LOW | $2.84 |
| headhunting | RO / ro | **50** | LOW | — |
| headhunting romania | RO / ro | **50** | HIGH | $0.90 |
| headhunting romania | RO / en | **50** | HIGH | $0.90 |
| headhunting services | UK / en | **50** | LOW | $5.46 |
| hire a cto | US / en | **50** | LOW | $30.54 |
| passive candidate sourcing | US / en | **50** | MEDIUM | $19.12 |
| executive search fees | US / en | 30 | LOW | $40.91 |
| tech executive search | UK / en | 30 | MEDIUM | — |
| passive candidate sourcing | UK / en | 20 | LOW | — |
| retained executive search | DE / en | 20 | LOW | $1.44 |
| tech executive search | US / en | 20 | LOW | — |
| hire a cto | UK / en | 10 | MEDIUM | $22.88 |
| engineering manager recruitment | UK / en | 10 | LOW | $5.32 |
| firma executive search · recrutare manageri | RO / ro | 10 each | LOW | — |

**Why this cluster leads:** it is the only one with measurable Romanian demand (`executive search romania` 70, `headhunting romania` 50+50) **and** high-value Western demand (`retained executive search` 590 US at $80.44 CPC). `headhunting romania` shows HIGH competition — competitors are already paying for it, which confirms the commercial value rather than arguing against it. The pillar already exists; it is under-spoked.

**No measurable volume** (do not target as primary): technical leadership recruitment · how to headhunt a CTO · how to hire a Head of Data · headhunting vs job ads · hire a VP of Engineering (RO/UK/DE — 10/mo US only) · vanatoare de capete recrutare

### Long-Tail
- how to headhunt a CTO
- how to hire a VP of Engineering
- executive search for tech leaders Romania
- reach passive senior engineers
- when to use headhunting vs job ads
- retained executive search for tech roles
- how to hire a Head of Data

### Related Questions
- What is tech headhunting and how does it work?
- How do you reach candidates who aren't job hunting?
- When should I use executive search instead of a job posting?
- How much does executive search cost? *(engagement-based framing)*

---

## Cluster 5: IT Salaries & Market Intelligence

### Pillar Keyword
- **Keyword**: IT salaries Romania (EN) / salarii IT România (RO)
- **Volume / Difficulty**: measured below — high link/traffic value; refresh yearly
- **Intent**: Informational (top-of-funnel, strong lead magnet)
- **Pillar URL**: https://wise-step.ro/blog/it-salaries-romania-2026/ · RO: /ro/blog/it-salaries-romania-2026-ro/
- **Tool asset (live 2026-09-03)**: https://wise-step.ro/salary-calculator/ · RO: https://wise-step.ro/ro/calculator-salariu/ — free gross→net→employer-cost calculator. This cluster now has **two** asset types, and they take different halves of the intent: the pillar owns *how much roles pay*, the calculator owns *what a given gross nets and costs*. Cross-link both ways.

### Measured volumes — DataForSEO Google Ads live, location Romania, 2026-08-12

**Romanian carries this cluster.** Every RO term outperforms its EN equivalent by roughly 8–15×. Plan RO-first for salary content.

| Keyword | Lang | Monthly volume | Competition |
|---|---|---|---|
| salariu mediu net romania | ro | **590** | LOW |
| salariu mediu pe economie | ro | **590** | LOW |
| salarii in it | ro | **170** | LOW |
| salariu it | ro | **110** | LOW |
| salarii it romania | ro | **50** | LOW |
| salariu it romania | ro | 30 | LOW |
| salariu mediu it | ro | 30 | LOW |
| salariu mediu it romania | ro | 30 | LOW |
| salariu programator romania | ro | 20 | LOW |
| asteptari salariale | ro | 20 | LOW |
| negociere salariu | ro | 20 | LOW |
| cat castiga un programator | ro | 20 | LOW |
| cat castiga un programator in romania | ro | 10 | LOW |
| average salary romania | en | **1,300** | LOW |
| it salaries romania | en | 10 | LOW |
| it salary romania | en | 10 | LOW |
| software developer salary romania | en | 10 | LOW |
| romania software developer salary | en (US) | 10 | — |

**No measurable volume** (do not target as primary): salarii it 2026 · salariu net 2026 · salariu mediu romania 2026 · inflatie romania 2026 · cel mai bine platit domeniu romania · romania average it salary · salary expectations romania · romania tech salaries · hire developers romania

**SERP note:** Google serves an **AI Overview** on `salarii it romania` and on `cel mai bine platit domeniu` (verified 2026-08-12). Top organic is salary-listing sites (devjob.ro, paylab.ro, newtech.ro, ejobs.ro) plus a Reddit r/programare salary thread. AEO is the realistic play on this cluster, not classic position-1 ranking.

### Measured volumes — salary-calculator & employer-cost family, DataForSEO Google Ads live, 2026-09-03

Run via `research_calculator_salarii_volumes.py`. Raw JSON: `output/keyword-volumes-calculator-salarii-2026-09-03.json` (volumes) and `output/serp-calculator-salarii-2026-09-03.json` (live Google positions, location Romania, language ro). Full analysis: `research/brief-calculator-salarii-2026-09-02.md`.

⚠ **`competition` in every table on this page is Google Ads advertiser competition, not SEO difficulty.** That distinction is load-bearing here: every calculator term below reads LOW and every calculator SERP is saturated with purpose-built tools.

**Tool intent — the largest volume in the portfolio, and almost none of it is reachable.**

| Keyword | Lang | Monthly volume | Competition | CPC |
|---|---|---|---|---|
| calculator salariu net | ro | **90,500** | LOW | $1.12 |
| calcul salariu net | ro | **33,100** | LOW | $0.59 |
| calculator salarii | ro | **14,800** | LOW | $1.39 |
| calculator salariu | ro | **14,800** | LOW | $1.39 |
| salariu net | ro | **14,800** | LOW | $1.13 |
| brut net | ro | **9,900** | LOW | $1.51 |
| salariu brut | ro | **9,900** | LOW | $0.05 |
| calculator salariu brut net | ro | **4,400** | LOW | $1.15 |
| calculator salariu net 2026 | ro | **2,400** | LOW | $0.87 |
| calculator pfa | ro | **1,900** | LOW | $0.35 |
| calculator salariu 2026 | ro | **1,000** | LOW | $1.21 |
| din brut in net · calculator venit net · calculator salariu minim | ro | 390 each | LOW | $0.35–2.40 |
| salariu net 2026 | ro | 320 | LOW | — |
| calculator salariu net brut | ro | 260 | LOW | $1.37 |
| calculator impozit salariu | ro | 140 | LOW | — |

Calculator family total ≈ **171,000/mo**.

**Employer-cost intent — the query a hiring company would run does not exist.**

| Keyword | Lang | Monthly volume | Competition |
|---|---|---|---|
| impozit pe salariu | ro | **390** | LOW |
| calculator taxe salariale | ro | **260** | LOW |
| taxe salariale 2026 | ro | 30 | LOW |
| calculator contributii salariale | ro | 10 | LOW |

**IT-qualified slice:** `calculator salariu it` **210/mo** (LOW) · `calculator salariu programator` 10/mo. This 210 is the honest ceiling for anything IT-specific in this family.

**English (RO/UK/US/DE):** `salary calculator romania` and `romania salary calculator` **320/mo each in RO/en**, `gross to net romania` 260 RO/en, `net salary calculator romania` 90 RO/en; 10–20/mo everywhere else. `employer of record romania` is 10–20/mo but carries **$81.26 CPC at HIGH competition (RO/en)** — 34× anything else in this family.

**No measurable volume** (do not target as primary): cost angajator · cost total angajator · cat costa un angajat · costul unui angajat · calculator cost angajator · salariu net programator it · calculator salariu freelancer · cost of hiring in romania · cost to hire a developer in romania · employer cost calculator romania · romania employer costs · romania payroll calculator

**SERP note — live Google positions, 2026-09-03.** The split is clean and it decides what is writable:

| Query | Volume | AI Overview | PAA | Editorial ranks? |
|---|---|---|---|---|
| `calculator salariu net` | 90,500 | ❌ | ❌ | ❌ 13/13 tools |
| `calculator salarii` | 14,800 | ❌ | ❌ | ❌ tools only |
| `calculator salariu it` | 210 | ❌ | ❌ | ❌ tools only |
| `calculator taxe salariale` | 260 | ❌ | ❌ | partial |
| `impozit pe salariu` | 390 | ✅ | ✅ | ✅ yes |
| `cat costa un angajat` | 0 | ✅ | ✅ | ✅ yes |

Where the query asks for a **tool**, Google serves tools and no AI layer — `calculator-salarii.ro` holds an exact-match domain at #1 on every tool query tested. Where the query asks a **question**, Google serves an AI Overview and editorial ranks beneath it. **No recruitment agency ranks anywhere in this family** — not Hays, not Human Direct, not Evolve Today.

⚠ **Two intent traps in this family**, both the same shape as `ats cv checker` (Cluster 8) and `externalizare it` (Cluster 6):
1. **The calculator terms want a tool, not an article.** 171,000/mo is not an editorial opportunity. Do not write a post targeting `calculator salarii`. **Update 2026-09-03: the tool now exists** — `/ro/calculator-salariu/` — which is the correct answer to this intent. The trap it closes is the editorial one; it does **not** make the head terms winnable (see below).
2. **`employer of record romania` wants an EOR provider.** Wise Step does not sell EOR. Do not build a page implying otherwise; the only honest version is the comparison that names when we are the wrong answer.

### Tool asset status — shipped 2026-09-03

`/salary-calculator/` (EN) and `/ro/calculator-salariu/` (RO) are live and indexable. Audit and ranked fix list: `research/brief-calculator-salarii-2026-09-02.md` §8.

**Sound already:** hreflang en/ro/x-default with self-referencing canonicals · `WebApplication` + `FAQPage` + `BreadcrumbList` schema · both URLs in the sitemap · robots.txt allowlists GPTBot/ClaudeBot/PerplexityBot/Google-Extended and blocks CCBot/Bytespider · personal-deduction and under-26 logic · FAQ already answers `cât costă un angajat` (an AI-Overview carrier) and the IT-exemption question correctly.

**Open, ranked:** (1) title/H1/H2 match the 14,800 terms and miss `calculator salariu net` 90,500 and `calcul salariu net` 33,100 entirely — fix the title and headings, keep the slug; (2) zero sourced outbound citations, which breaches the `brand-voice.md` bar and forfeits the strongest AI-citation signal; (3) no `dateModified` / visible "rates verified" date; (4) no cross-links to or from the salary pillar; (5) forward-only — the differentiating **net + role → required gross + employer cost** mode is unbuilt; (6) `impozit pe salariu` (390/mo, AI-Overview carrier) unaddressed on the page.

⚠ **Do not re-forecast this cluster off the tool's existence.** The head terms stay out of reach — 13/13 purpose-built tools, exact-match domain at #1, no AI Overview to leapfrog. Expected capture is the long tail (`calculator salariu it` 210, `calculator salariu 2026` 1,000, `taxe salariale 2026` 30), the AI-Overview surface on the question-shaped queries, brand search, and **links** — a free calculator is the most linkable asset on the site, which is what the small commercial clusters cannot build on their own. Measure it on those, not on `calculator salariu net`.

**Maintenance is now a standing obligation, not a project.** Rates moved twice across 2025–26 (HG 1506/2024 → HG 146/2026). The calculator needs a named owner and a scheduled re-verification, or it will silently go wrong.

**What is actually writable here:** the employer-cost/tax question family — tiny on volume (390 + 260), but the **only two queries in this whole set carrying an AI Overview**. Treat it as a citation and authority asset for the Market Intelligence line, measured on citations rather than sessions. Cannibalization division of labour for the resulting piece is set in `research/brief-calculator-salarii-2026-09-02.md` §7.

### Cluster Keywords
1. software developer salary Romania — 10/mo (en) · salariu programator romania 20/mo (ro)
2. DevOps engineer salary Romania — [TBD]
3. data engineer / ML engineer salary Romania — [TBD]
4. tech salary benchmarks CEE — [TBD]
5. CTO / VP Eng salary Romania — [TBD]
6. IT salary guide Romania [year] — [TBD]
7. salary expectations vs offers — asteptari salariale 20/mo (ro), negociere salariu 20/mo (ro)

### Long-Tail
- average software developer salary in Romania [year]
- how much do DevOps engineers earn in Romania
- senior vs junior developer salary Romania
- data scientist salary Romania [year]
- tech salaries Romania vs Western Europe
- remote developer salaries Romania
- what affects IT salaries in Romania

### Related Questions
- How much do software engineers earn in Romania?
- Are Romanian tech salaries rising in [year]?
- How do Romania salaries compare to Western Europe?
- What does a DevOps engineer make in Romania?

*Note: directly competes with Hays' Salary Guide (see `competitor-analysis.md`) — keep our data sourced and current.*

---

## Cluster 6: Hiring in Romania / CEE (remote, first office, team build-out)

### Pillar Keyword
- **Keyword**: hire remote developers Romania / hiring in Eastern Europe
- **Volume / Difficulty**: measured 2026-08-21 — **every EN keyword in this cluster returned zero.** The volume is Romanian and it belongs to a different intent: `externalizare it` 720/mo.
- **Intent**: Informational → commercial
- **Pillar URL**: https://wise-step.ro/blog/hire-remote-developers-romania/ + https://wise-step.ro/blog/it-recruitment-trends-eastern-europe-2026/

### Measured volumes — DataForSEO Google Ads live, 2026-08-21

| Keyword | Geo / lang | Monthly volume | Competition | CPC |
|---|---|---|---|---|
| externalizare it | RO / ro | **720** | MEDIUM | **$4.71** |
| piata it romania | RO / ro | 30 | LOW | — |
| companii it romania | RO / ro | 30 | LOW | — |
| nearshore software development romania | RO / en · UK · US | 10 each | MEDIUM | — |
| nearshoring romania | RO / ro | 10 | LOW | — |

⚠ **Intent warning on `externalizare it` (720/mo).** This is the highest-volume commercial term measured anywhere in clusters 1/3/4/6, but the searcher wants an **IT outsourcing vendor** — a team delivered as a service — not a recruiter who places employees on their payroll. Wise Step does not sell outsourcing. Two honest options: (a) skip it, or (b) write the comparison piece — *outsourcing vs building your own team in Romania* — that names the difference and converts the subset who actually want to hire. Option (b) fits the brand voice (name the friction, tell them when we're the wrong answer) and is the only version worth writing. **Do not chase this term with a page implying we deliver outsourcing.**

**No measurable volume** (do not target as primary): hire remote developers Romania · hiring in Eastern Europe · hire developers Eastern Europe · open a tech office in Romania · build an engineering team Romania · Romania tech talent pool · IT recruitment trends Eastern Europe · Romania vs Poland developers · hire your first engineer in Romania · nearshoring to Romania · Romania software development outsourcing · Eastern Europe developer rates · why hire developers in Romania

### Long-Tail
- how to build a dev team in Romania
- how to open an R&D office in Romania
- pros and cons of hiring in Eastern Europe
- nearshoring engineering to Romania
- Romania vs Poland vs Bulgaria for tech talent
- how to hire your first engineer in Romania
- remote hiring playbook Eastern Europe

### Related Questions
- Is Romania a good place to hire developers?
- How do I set up an engineering team in Romania?
- Why hire engineers in Eastern Europe?
- What's changed about hiring in Romania in [year]? *(cost play → speed play)*

---

## Cluster 7: Emerging Roles & AI-Native Engineering (thought leadership)

### Pillar Keyword
- **Keyword**: forward deployed engineer / applied AI engineer
- **Volume / Difficulty**: measured 2026-08-21 — **the largest traffic opportunity in the entire portfolio.** `forward deployed engineer` **18,100/mo US**, 2,400 UK, 1,900 DE, 140 RO. This cluster was filed under "Low Priority (future)". That was wrong.
- **Intent**: Informational
- **Pillar URL**: https://wise-step.ro/blog/ai-native-engineering/ · https://wise-step.ro/blog/applied-ai-engineer/ — **both already live**

### Measured volumes — DataForSEO Google Ads live, 2026-08-21

| Keyword | Geo / lang | Monthly volume | Competition | CPC |
|---|---|---|---|---|
| forward deployed engineer | US / en | **18,100** | LOW | $6.17 |
| forward deployed engineer | UK / en | **2,400** | LOW | $6.99 |
| what is a forward deployed engineer | US / en | **1,900** | LOW | $3.31 |
| forward deployed engineer | DE / en | **1,900** | LOW | $15.05 |
| applied ai engineer | US / en | **720** | LOW | **$17.04** |
| what is a forward deployed engineer | UK / en | **320** | LOW | $1.93 |
| ai engineer skills | US / en | **210** | LOW | $5.49 |
| ai native engineering | US / en | **170** | MEDIUM | **$13.54** |
| forward deployed engineer | RO / en | **140** | LOW | $11.66 |
| applied ai engineer | UK / en | **140** | LOW | $7.69 |
| what is a forward deployed engineer | DE / en | 70 | LOW | — |
| applied ai engineer | DE / en | 50 | MEDIUM | $7.22 |
| ai native engineering | UK / en | 30 | MEDIUM | $5.87 |
| ai engineer skills | UK / en | 30 | MEDIUM | $1.06 |
| what is an applied ai engineer | US / en | 30 | LOW | — |
| ai engineer skills | DE / en | 20 | MEDIUM | $5.71 |
| ai native engineering · what is an applied ai engineer · ai engineer skills | RO / en | 10 each | LOW–MED | $0.85–1.89 |

**Promote this cluster to a priority build.** Three facts make it the strongest play available:
1. `forward deployed engineer` at 18,100/mo US is **22× the next-largest term** in any cluster we can realistically rank for, at LOW competition. *(Qualified 2026-09-03: the salary-calculator family in Cluster 5 measures larger — `calculator salariu net` 90,500/mo RO — but its SERP is 13/13 purpose-built tools with no AI Overview, so it is not a comparable target. FDE remains the largest **reachable** term.)*
2. **Two of the pillar posts are already published** (`ai-native-engineering`, `applied-ai-engineer`) — this is an expansion, not a cold start.
3. LOW competition on a term with a $6–15 CPC means the SERP has not caught up to the demand yet.

⚠ **Intent caveat — read before reallocating budget.** The `forward deployed engineer` searcher is predominantly an **engineer researching the role**, not an employer hiring one. This cluster is a **traffic, brand-reach and AI-citation engine, not a lead engine.** Treat it exactly as the candidate-side content it is: fund it deliberately, measure it on citations, links and branded search — never on briefed searches. Its commercial job is to make Wise Step the name attached to the role definition, which is what gets cited when an employer later asks an assistant how to hire one.

**No measurable volume** (do not target as primary): AI-native startup hiring · new engineering roles · new tech roles [year] · hiring for AI-first teams · how AI is changing engineering hiring · how to hire a forward deployed engineer · inginer ai · roluri noi in it · meserii viitor it

### Long-Tail
- what is a forward deployed engineer
- how to hire a forward deployed engineer
- what is an applied AI engineer
- new tech roles emerging in [year]
- how AI is changing engineering hiring
- skills to look for in AI-native engineers

### Related Questions
- What is AI-native engineering?
- What does a forward deployed engineer do?
- What new engineering roles are companies hiring for?

---

## Cluster 8: Compliance & Candidate-Side (supporting)

### Pillar Keyword(s)
- **Keywords**: EU AI Act recruitment; ATS-friendly CV
- **Volume / Difficulty**: measured 2026-08-21 — **second-largest cluster in the portfolio, and the largest in Romanian.** `model cv` **8,100/mo RO**; `ats cv checker` **12,100/mo US**; `eu ai act` **480/mo RO**.
- **Intent**: Informational
- **Pillar URLs**: https://wise-step.ro/blog/eu-ai-act-recruitment/ · https://wise-step.ro/blog/ats-friendly-cv/ — **both already live**

### Measured volumes — DataForSEO Google Ads live, 2026-08-21

| Keyword | Geo / lang | Monthly volume | Competition | CPC |
|---|---|---|---|---|
| ats cv checker | US / en | **12,100** | MEDIUM | $5.87 |
| model cv | **RO / ro** | **8,100** | MEDIUM | $1.32 |
| ats resume format | US / en | **2,900** | MEDIUM | $4.63 |
| ats cv checker | UK / en | **2,400** | HIGH | $3.08 |
| ats cv checker | DE / en | **1,600** | MEDIUM | $2.29 |
| ats friendly cv | UK / en | **880** | MEDIUM | $2.47 |
| eu ai act | **RO / ro** | **480** | MEDIUM | $3.39 |
| cv for software engineer | UK / en | **390** | LOW | $1.38 |
| ats friendly cv | DE / en | **390** | MEDIUM | $2.23 |
| ats resume format | UK / en | **170** | MEDIUM | $3.23 |
| ats friendly cv | US / en | **110** | LOW | $4.17 |
| ats resume format | DE / en | 90 | MEDIUM | $1.14 |
| cv ats | **RO / ro** | **90** | MEDIUM | $1.88 |
| ats friendly cv | RO / en | 70 | MEDIUM | $2.18 |
| how to pass ats · cv for software engineer | US / en | 70 each | LOW | $2.06–3.90 |
| ats cv checker | RO / en | **140** | MEDIUM | $0.91 |
| eu ai act recruitment | DE / en | 10 | **HIGH** | **$35.43** |
| cv programator | RO / ro | 10 | MEDIUM | $0.90 |

**Two things to act on, one to avoid:**
1. **`model cv` at 8,100/mo RO is the largest Romanian term we can realistically target** — larger than the whole salary cluster combined. It is a CV-template query from candidates. *(Corrected 2026-09-03: it is no longer the largest Romanian term **measured** — `calculator salariu net` is 90,500/mo RO, Cluster 5 — but that one is a tool query with no editorial foothold, so `model cv` still leads on addressable Romanian volume.)*
2. **`eu ai act` 480/mo RO** — the existing EU AI Act post targets the recruitment-qualified long tail (10/mo). The unqualified Romanian term is 48× bigger, and Wise Step has a legitimate angle on it that no Romanian law blog has: what it means for hiring specifically. Worth a RO-first companion piece.
3. ⚠ **Avoid `ats cv checker` (12,100 US / 2,400 UK / 1,600 DE) as an article target.** That searcher wants a **tool**, not a guide. An article will not satisfy it and will not hold a ranking. Either build an actual CV checker or leave the term alone — do not write a post pretending to be a tool.

**Same intent caveat as Cluster 7:** this is entirely candidate-side. Traffic, links and citations — not briefed searches. It earns the authority the commercial clusters are too small to build on their own.

**No measurable volume** (do not target as primary): EU AI Act hiring compliance · AI in recruitment regulation · tech CV tips · is AI hiring legal · AI hiring compliance · cum sa scrii un cv · cv optimizat pentru ats *(note: the live RO post is at this slug — the traffic term is `cv ats` 90/mo or `model cv` 8,100/mo)*

### Long-Tail
- what the EU AI Act means for recruitment
- is AI hiring legal under the EU AI Act
- how to write a CV that passes ATS
- ATS resume format for developers
- tech CV mistakes to avoid

### Related Questions
- Does the EU AI Act affect how we hire?
- How do I make my CV ATS-friendly?
- Can employers use AI to screen candidates in the EU?

---

## Seasonal / Trending Keywords

- **Yearly refresh (Q4→Q1)**: "IT salaries Romania [next year]", "IT recruitment trends [next year]", "tech hiring outlook [next year]" — update the salary + trends pillars annually
- **Reactive**: tax/legislation changes (2024 tax changes precedent), major layoffs/hiring waves, new AI-role demand spikes, EU AI Act enforcement milestones
- Trending topics feed from LinkedIn scan + `research_trending.py`

---

## Competitor Keyword Gaps

Track where competitors rank and we don't. Run `research_competitor_gaps.py` / `seo_competitor_analysis.py` for real data. See `competitor-analysis.md`.

### Human Direct (humandirect.eu)
- Content overlap: "recruiting software developers in Romania" — [gap check TBD]
- Opportunity: they publish infrequently — out-publish on Cloud/DevOps + Data/AI depth

### Hays Romania (hays.ro)
- Owns: "salary guide Romania" via annual Salary Guide — [gap check TBD]
- Opportunity: sharper, sourced, role-specific salary content; AEO structure they lack

### Evolve Today (evolvetoday.ro)
- Content: HR-trend/lifestyle-adjacent — [gap check TBD]
- Opportunity: own the technical-market/data-backed angle they don't cover

*Populate positions + opportunity ratings after running the gap scripts.*

---

## Keyword Opportunity Pipeline

### High Priority (create/strengthen soon)
1. **DevOps / Cloud recruitment Romania** — no dedicated pillar yet, core specialisation. Action: create Cluster 3 pillar.
2. **IT salaries Romania** — high value, exists; keep refreshed and expand role-level sub-pages.
3. **AI recruitment agency Romania** — commercial intent, exists; strengthen internal links + AEO.
*(Confirm volume/difficulty via DataForSEO before committing order.)*

### Medium Priority (next quarter)
- Role-specific salary sub-pages (DevOps salary, ML engineer salary Romania)
- Executive search sub-topics (hire a CTO, hire a VP Eng)
- City pages if warranted (Timișoara/Bucharest/Cluj) — check search demand first

### Reclassified 2026-08-21 (was "Low Priority (future)")
- ~~Emerging-role thought leadership (FDE, applied AI) — low volume~~ → **wrong on volume.** `forward deployed engineer` is 18,100/mo US at LOW competition, the largest **addressable** term in the portfolio (see the 2026-09-03 qualification in Cluster 7), with two posts already live. Promote to a priority build. Traffic and citation value, not leads.
- ~~Compliance deep-dives beyond EU AI Act~~ → `eu ai act` unqualified is 480/mo RO, 48× the recruitment-qualified variant. RO-first companion piece justified.
- **New:** `model cv` 8,100/mo RO — largest **addressable** Romanian term (see the 2026-09-03 correction in Cluster 8). Candidate-side CV content is the biggest single traffic asset available.
- **New 2026-09-03:** the salary-calculator family (Cluster 5) measures ~171,000/mo RO. The head terms are **not** an editorial opportunity — 13/13 tools on the SERP, exact-match domain at #1, no AI Overview. Logged so nobody re-discovers the headline number and mistakes it for a gap. **A calculator shipped the same day** (`/ro/calculator-salariu/`), which answers the tool intent correctly but does not make the head terms winnable. Target the long tail, the AI-Overview question queries (`impozit pe salariu` 390, `cat costa un angajat`), and links.

---

## Keyword Tracking & Performance

Pull from Google Search Console; don't hand-enter estimates.

### Top Performing (positions 1–10)
- [TBD — export from Search Console]

### To Improve (positions 11–20)
- [TBD — page-2 keywords with opportunity; run `seo_bofu_rankings.py` / GSC]

---

## Keyword Cannibalization Check

Watch for overlap as clusters fill in. Current candidates to monitor:
- `ai-recruitment-agency-romania` vs `ai-data-science-recruitment-romania` — both target AI/data recruitment intent; keep the first commercial ("agency/hire us") and the second informational ("how to recruit"), differentiate H1s and internal-link intent. [Monitor]
- Future salary sub-pages vs the main salary guide — keep sub-pages role-specific, guide as the hub.
- `it-salaries-romania-2026` vs `it-salaries-romania-inflation-2026` (drafted 2026-08-12) — both sit in Cluster 5 and both rank for salary intent. **Division of labour:** the pillar owns *how much roles pay* (bands by role and seniority, refreshed yearly); the inflation piece owns *what that pay is worth and why candidates ask for more* (real-terms erosion, the 50% expectation gap, negotiation playbook). Keep every role-level band out of the inflation piece and link to the pillar instead. Add a reciprocal link from the pillar so the hub-and-spoke is explicit. Differentiate H1s. [Monitor after publish]

---

## Semantic / Related Terms

Include naturally across content for topical authority.

### Recruitment terms
- talent acquisition, headhunting, executive search, sourcing, shortlist, screening, time-to-fill, counter-offer, retained, contingency, placement, replacement guarantee

### Tech role / stack terms
- software engineer, DevOps, SRE, platform engineering, cloud (AWS/Azure/GCP), Kubernetes, CI/CD, data engineer, ML engineer, data scientist, MLOps, backend, Engineering Manager, VP Eng, CTO, Head of Data

### Market terms
- Romania, Timișoara, Bucharest, Cluj, Eastern Europe, CEE, nearshore, remote, talent pool, salary benchmark, R&D centre, tech hub

---

## Usage Guidelines

### Writing new content
1. Identify the cluster; target its pillar or a long-tail keyword
2. Reference the cluster pillar; link related cluster posts (`internal-links-map.md`)
3. Integrate semantic terms naturally; keyword in first 100 words + conclusion
4. Answer the target question directly up front (AEO — see `seo-guidelines.md`)

### Optimising existing content
1. Verify it targets the right keyword; check cannibalization
2. Ensure keyword in critical locations; update if intent shifted
3. Add internal links to/from related cluster content
4. Refresh stats (salary/market data dates fast)

### Content calendar
1. Review the opportunity pipeline (data-fed via DataForSEO/GSC, not guesses)
2. Prioritise achievable, high-value keywords in our specialisation
3. Build clusters systematically; balance pillars with cluster/long-tail articles
4. Publish EN + RO

---

## Maintenance

**Regular updates**:
- Add keyword opportunities monthly (LinkedIn scan + trending scripts)
- Track ranking changes monthly (GSC)
- Refresh volumes/difficulty quarterly (DataForSEO)
- Review competitor gaps quarterly
- Annual refresh of salary/trends pillars

**Open items**: populate competitor gap positions; export GSC positions to replace the tracking [TBD]s. Volume measurement is complete for all eight clusters as of 2026-08-21 — refresh quarterly via `research_keyword_volumes.py`. Cluster 5's salary-calculator / employer-cost extension was measured 2026-09-03 — refresh via `research_calculator_salarii_volumes.py`. **DataForSEO requires the machine's current public IP to be whitelisted** at https://app.dataforseo.com/api-access, or every task returns "Access denied"; the IP changes, so re-check it before assuming a script is broken. **New standing item:** the salary calculator (`/salary-calculator/`, `/ro/calculator-salariu/`) carries live tax rates and needs a named owner plus scheduled re-verification against ANAF/Monitorul Oficial — the minimum wage alone changed twice across 2025–26.

---

**Note**: Living document. Metrics come from research (DataForSEO/GSC), never estimation. Keep clusters aligned to our real specialisation — Cloud/DevOps, Data/AI, and technical leadership in Romania/CEE.
