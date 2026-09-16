# Agent prompt — SEO/AEO content fixes, salary calculator pages

*Generated 2026-09-03 from `research/brief-calculator-salarii-2026-09-02.md` §8 (seomachine repo). Paste everything below the line into a coding agent working in the **wise-step.ro Astro repo**.*

---

You are working in the Astro repo that builds `wise-step.ro`. Apply a set of SEO/AEO content fixes to the two salary-calculator pages. This is a **content and metadata** task — do not refactor the calculator logic or components.

## The pages

| Locale | Live URL | Find the source file |
|---|---|---|
| EN | `https://wise-step.ro/salary-calculator/` | search for the string `Salary Calculator Romania 2026` |
| RO | `https://wise-step.ro/ro/calculator-salariu/` | search for the string `Calculator Salarii 2026` |

Shared partials are likely — a calculator component and a page shell. Locate both page entry points before editing; if strings live in a shared i18n/content file, edit there and keep the two locales in sync.

## Do NOT touch these — they are already correct

Verified live 2026-09-03. Changing any of them is a regression:

- **Slugs.** `/salary-calculator/` and `/ro/calculator-salariu/` stay exactly as they are. The pages are days old and canonicals are set; a slug change costs more than it earns.
- **hreflang** (`en`, `ro`, `x-default`) and the self-referencing canonicals.
- **Schema `@type` set:** `WebApplication` + `FAQPage` + `BreadcrumbList`. Add properties as instructed below; do not change or remove types.
- **`robots.txt`** — the AI-crawler allowlist (GPTBot, ClaudeBot, PerplexityBot, anthropic-ai, Google-Extended allowed; CCBot, Bytespider, meta-externalagent, Applebot-Extended blocked) is deliberate.
- **`<meta name="robots" content="index, follow">`**, sitemap entries, OG/Twitter tags.
- **The EN title and meta description.** They already match the measured EN keywords (`salary calculator romania` 320/mo, `gross to net romania` 260/mo). **Task 1 is Romanian-only.** Do not "harmonise" the EN title to match the RO one.
- **Calculator math and inputs.** Rates, personal-deduction logic, under-26 handling — all out of scope.

## Constraint on all copy you write

Every factual claim must be backed by a cited source or a concrete number. **Do not invent figures, dates, or statistics.** If a number is needed and not supplied below, leave a `TODO:` marker rather than guessing. All numbers you need are in this document.

---

## Task 1 — Romanian title and headings (highest impact)

The RO page currently targets the 14,800/mo keywords and does not match the 90,500/mo one anywhere in its title, H1 or H2.

Measured Romanian search volume (DataForSEO, 2026-09-03):

| Term | Volume/mo | Currently matched? |
|---|---|---|
| `calculator salariu net` | **90,500** | no |
| `calcul salariu net` | **33,100** | no |
| `calculator salarii` | 14,800 | yes — title + H1 |
| `calculator salariu` | 14,800 | yes — slug |

### Changes, RO page only

**`<title>`** — must stay ≤60 characters.

```
BEFORE: Calculator Salarii 2026 — Salariu Brut în Net | Wise Step Recruiting
AFTER:  Calculator Salariu Net 2026 — Calcul Brut în Net | Wise Step
```
The replacement is exactly 60 chars. The brand suffix is shortened from "Wise Step Recruiting" to "Wise Step" to fit — if house style forbids that, drop the `— Calcul Brut în Net` segment instead and keep the longer brand. **The tokens `Calculator Salariu Net` must survive whichever variant you pick.** Update `og:title` to match.

**`<meta name="description">`** — 150–160 chars. The replacement below is **153**. Note the division of labour: the **title** carries `calculator salariu net` (90,500/mo) and the **description** retains `calculator salarii` (14,800/mo) — the two phrases differ (*salariu* vs *salarii*) and will not both fit naturally in one field, so keep them split across the two.
```
BEFORE: Calculator salarii brut-net pentru România, actualizat pentru 2026. Afișează CAS, CASS, deducerea personală, impozitul pe venit, CAM și costul total al angajatorului.
AFTER:  Calculator salarii 2026: calcul din brut în net pentru România. Vezi CAS, CASS, deducerea personală, impozitul pe venit și costul total pentru angajator.
```

**H1**
```
BEFORE: Calculator Salarii
AFTER:  Calculator salariu net
```

**First H2** (the one directly under the calculator, currently `Calculator de salarii România`)
```
AFTER: Calcul salariu net 2026 pentru România
```

Leave the other RO H2s (`Unde ajung banii.`, `Cele mai frecvente.`, `De reținut`, `Aflați cifra. Apoi negociați.`) unchanged.

**Also ensure the exact phrase `calculator salariu net` appears once in the first ~100 words of visible RO body copy**, naturally. Do not repeat it beyond that — keyword stuffing is a regression, not a fix.

---

## Task 2 — Add sourced citations (both locales)

Currently the only outbound links on either page are the ANPC/ODR footer pair and Google Fonts. Zero sources for the tax figures. This is the single strongest AI-citation signal available and it is entirely absent.

Add these as **visible, followed links** (no `nofollow`, no `sponsored`) inside the existing "Good to know" / "De reținut" section. All three were verified 2026-09-03:

| Claim on the page | Source URL | Link text (RO) | Link text (EN) |
|---|---|---|---|
| IT income-tax exemption was eliminated for income from January 2025 | `https://static.anaf.ro/static/10/Anaf/legislatie/OUG_156_2024.pdf` | OUG 156/2024 | OUG 156/2024 |
| Minimum gross wage 4.325 lei from 1 July 2026 | `https://legislatie.just.ro/Public/DetaliiDocumentAfis/308231` | HG 146/2026 | HG 146/2026 |
| Minimum gross wage 4.050 lei, January–June 2026 | `https://legislatie.just.ro/Public/DetaliiDocument/291450` | HG 1506/2024 | HG 1506/2024 |

Reference detail you may use in the copy, all verified:
- **OUG 156/2024**, published Monitorul Oficial nr. 1334/2024. Eliminated the software-development income-tax exemption for income earned from January 2025.
- **HG 146/2026**, 12 March 2026, Monitorul Oficial Partea I nr. 196 / 13 March 2026. Minimum gross wage 4.325 lei from 1 July 2026; hourly 25,949 lei at 166,667 h/month. Repeals HG 1506/2024.
- **HG 1506/2024**, Monitorul Oficial Partea I nr. 1185 / 28 November 2024. Minimum gross wage 4.050 lei from 1 January 2025.

⚠ **Do not cite press coverage** (ZF, Digi24, StartupCafe, Avocatnet) for any of these. Official sources only.

⚠ **The construction sector has a separate minimum wage (4.582 lei under HG 1506/2024). Do not mention or blend it** — these pages are general/IT-facing and mixing the two figures would make the page wrong.

---

## Task 3 — Freshness signals (both locales)

The pages say "rules in force since 1 July 2026" / "reguli în vigoare de la 1 iulie 2026". That is a *rules* date, not a *verification* date — it does not tell a reader or a crawler when a human last checked the rates.

1. Add a **visible** line near the calculator or at the top of the "Good to know" / "De reținut" section:
   - RO: `Rate verificate: 3 septembrie 2026`
   - EN: `Rates verified: 3 September 2026`
   Use the actual date you make the change, not a hardcoded literal, if the codebase has a build-time or frontmatter date convention — prefer that convention.

2. Add **`dateModified`** to the `WebApplication` JSON-LD node on both pages, ISO-8601, matching the visible date:
   ```json
   "dateModified": "2026-09-03"
   ```
   Keep the existing properties (`applicationCategory`, `offers`, `inLanguage`, `publisher`, `isPartOf`, `browserRequirements`) untouched.

---

## Task 4 — Cross-link the salary guide (both directions)

The calculator currently links only to the blog *index*. The highest-value internal target on the site is the salary guide, and the pairing is missing in both directions.

⚠ **RO URLs on this site follow three different patterns. Do not derive them — copy these exactly.**

| From | To | Notes |
|---|---|---|
| `/salary-calculator/` | `https://wise-step.ro/blog/it-salaries-romania-2026/` | EN → EN |
| `/ro/calculator-salariu/` | `https://wise-step.ro/ro/blog/it-salaries-romania-2026-ro/` | RO blog posts take a **`-ro` suffix** |
| `/blog/it-salaries-romania-2026/` | `https://wise-step.ro/salary-calculator/` | reciprocal |
| `/ro/blog/it-salaries-romania-2026-ro/` | `https://wise-step.ro/ro/calculator-salariu/` | reciprocal — note the RO tool slug is **fully translated with no suffix**; `/ro/salary-calculator/` is a 404 |

Place the calculator→guide link in body copy near the net-salary output, where the reader's next question is naturally "is that the right number for this role?" Use descriptive, varied anchor text — never "click here". Suggested:
- RO: "ghidul nostru de salarii IT 2026", "benzile salariale pe rol"
- EN: "our 2026 Romanian IT salary guide", "salary bands by role"

For the reciprocal links, place them where the guide first quotes a gross or net figure.
- RO anchor, preferred: **"calculator salariu net"** — it is the highest-volume term in the portfolio and the anchor is a useful signal. Vary it if the guide links the calculator more than once.
- EN anchor: "gross-to-net salary calculator", "work out the total employer cost".

---

## Task 5 — Add an income-tax section (RO primary, EN mirror)

`impozit pe salariu` is 390/mo in Romanian and is **one of only two queries in this family that Google answers with an AI Overview** (verified 2026-09-03). The page does not address it directly.

Add one H2 section plus one FAQ entry.

**RO H2** — place before `Cele mai frecvente.`:
```
Cât e impozitul pe salariu în România în 2026
```
Open with a **direct answer in the first sentence** — the AI-Overview surface pulls from the earliest clear answer on the page. The impozit is 10% applied to the taxable base (gross minus CAS 25% minus CASS 10% minus any personal deduction), not to the gross. Then expand with a worked example consistent with the calculator's own output. Keep it to one idea; do not restate the whole contribution breakdown that already exists in "Unde ajung banii."

**New FAQ entry**, RO, phrased as a natural query:
```
Q: Cât e impozitul pe salariu în România?
```
Answer directly in the first sentence, then expand. Two to four sentences total.

**EN:** mirror both, same structure and meaning — translate the sense and the register, not word-for-word.

### ⚠ Schema/DOM parity requirement

The pages carry `FAQPage` JSON-LD. **Every visible FAQ item must have a matching entry in the schema, and vice versa** — Google requires the structured data to match the visible content, and a mismatch risks a manual action. When you add the FAQ entry, add the corresponding `Question` / `acceptedAnswer` object to the `FAQPage` node with the same text, in both locales.

---

## Verification before you finish

Run these against your local build (and against production after deploy):

1. **Both pages still return 200** and render the calculator; run the calculator once in each locale and confirm outputs are unchanged. Task 1–5 must not alter any computed figure.
2. **`<title>` ≤ 60 chars** on the RO page; meta description 150–160.
3. **All three JSON-LD blocks still parse** as valid JSON on both pages, and `@type` values are unchanged. Validate with Google's Rich Results Test.
4. **FAQ parity:** count of visible FAQ items == count of `mainEntity` entries, per locale, with matching text.
5. **hreflang triple intact** on both pages, canonicals still self-referencing.
6. **Every new outbound link resolves** (expect 200; the ANAF link is a PDF).
7. **No new console errors**; no layout regression at mobile width.
8. `grep` the RO page output for `calculator salariu net` — expect it in the title, H1, and once in the opening body copy. If it appears more than ~4 times total, cut back.

## Out of scope — do not build these

- **The reverse "target net + role → required gross" mode.** It is the real differentiator but it is a feature with a design decision behind it, not a content fix. Leave it alone.
- Any change to calculator logic, rates, or input fields.
- Slug changes, redirects, or sitemap edits.
- Restyling, component refactors, or dependency upgrades.

## Commit

One commit per task is fine, or a single commit — your call. Do not push to the default branch; open a branch and a PR describing which of tasks 1–5 landed and anything you left as `TODO:`.
