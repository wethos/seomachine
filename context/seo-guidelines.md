# SEO & AEO Guidelines for Wise Step Content

SEO and AEO (answer-engine) best practices for all Wise Step Recruiting blog content (wise-step.ro), to maximise visibility in both classic search and AI-generated answers on CEE/Romania tech-recruitment queries.

Pairs with `brand-voice.md`, `style-guide.md`, and `internal-links-map.md`. The non-negotiable rule from the brand voice governs everything below: **every factual claim is sourced or backed by a concrete number — no hype, no invented figures.** SEO never overrides that.

**Stack context:** the site is Astro, hosted on Cloudflare Pages. Publishing = commit to GitHub (the human quality gate) → auto-deploy. Content is markdown with frontmatter — there is no WordPress/Yoast layer. All content ships in **English and Romanian**.

## Content Length Requirements

### Target Word Counts
- **Standard blog post**: 1,500–3,000 words (target 2,000–2,500)
- **Pillar / comprehensive guide** (e.g. salary guide, market trends): 3,000–5,000 words max
- **Playbook / how-to** (e.g. hiring playbook): 1,500–2,500 words
- **Sharp market take / news** (tax change, salary movement): 800–1,200 words

### Length Guidelines
- Max ~3,000 for most articles; ~5,000 for pillar content
- If a topic needs more, split into a series
- Aim for the lower end — concise, playbook-shaped content beats padded length

### Quality Over Quantity
- No fluff to hit a count. If a sentence is exciting but empty, cut it.
- Every section earns its place with a benchmark, a number, or an actionable takeaway
- 2,000 sourced words beat 3,000 padded ones

## Keyword Optimization

### Keyword Research (before writing)
1. Identify the primary target keyword
2. Research volume + difficulty (Google Search Console, DataForSEO)
3. Analyse the top 10 ranking competitors (see `competitor-analysis.md` — Human Direct, Hays, Evolve Today are active on content)
4. Identify 3–5 secondary/related keywords
5. List semantic/related terms

### Keyword Density
- **Primary keyword**: ~1–2% (natural integration only — never force)
- **Secondary keywords**: ~0.5–1% each
- **Semantic terms**: sprinkle naturally

### Critical Keyword Placement
Primary keyword must appear in:
- [ ] H1 (near the beginning)
- [ ] First 100 words
- [ ] 2–3 H2 subheadings
- [ ] Conclusion
- [ ] Meta title (within first 60 chars)
- [ ] Meta description
- [ ] URL slug

### Integration Best Practices
- **Humans first**: write for the reader, optimise for search
- **Use variations**: "IT recruitment Romania" → "recruiting IT talent in Romania" → "Romanian tech recruiters"
- **Question formats**: "how to hire remote developers in Romania" vs "hiring remote developers"
- **Semantic support**: for "DevOps recruitment", include "SRE", "cloud engineers", "platform engineering", "CI/CD"

### Keyword Stuffing (Avoid)
❌ "IT recruitment Romania is key. IT recruitment Romania helps companies. Our IT recruitment Romania service delivers IT recruitment Romania results."

✅ "Hiring engineers in Romania has shifted from a cost decision to a speed one. A specialised recruiter reaches the DevOps and data talent that job ads never surface."

## Content Structure Requirements

### Heading Hierarchy

#### H1 (Title)
- One H1 per article
- Primary keyword, naturally, near the start
- ≤60 chars for SERP display
- Sharp and specific — no hype. A reversal or benchmark angle works well.

#### H2 (Main Sections)
- 4–7 H2 sections for standard articles
- 2–3 should include keyword variations
- Descriptive; readers should follow the argument from the H2s alone
- Sentence case (see `style-guide.md`)

#### H3 (Subsections)
- Nested under H2 (never skip H2→H4)
- Break complex sections into digestible chunks

### Article Structure Template

```markdown
# [H1: Sharp Title with Primary Keyword]

[Direct answer: 1–2 sentences answering the query, up front — see AEO section]

## Introduction (150–250 words)
- Hook: reversal opener works ("used to be X — now it's Y")
- Correction/stakes: overturn the lazy assumption, back it with a number
- Promise: the benchmark/timeline/decision the reader leaves with
- Keyword in first 100 words

> **Key Takeaways** (TL;DR block — see AEO section)
> - ...

## [H2: Main Section 1 — keyword variation]
### [H3 if needed]
- Playbook-shaped: tables, timelines, numbered lists
- Sourced data / benchmarks

## [H2: Main Section 2]
...continue with 4–7 total H2 sections...

## FAQ (4–6 questions in natural prompt language)

## Conclusion (150–250 words)
- Recap (3–5 takeaways)
- Keyword
- Honest, concrete CTA (brief a search / book a discovery call)
```

## Meta Elements

### Meta Title
- **Length**: 50–60 chars (including "| Wise Step" if used)
- **Primary keyword**: required
- **Compelling but anti-hype**: earns the click with specificity, not adjectives
- **Unique** across the site; **accurate** to the page

**Format options**:
- `[Primary Keyword]: [Concrete Promise]`
- `How to [Goal] in Romania [Year]`
- `[Number] [Specifics] for [Audience]`
- `[Topic] Guide [Year] | Wise Step`

**Examples**:
- ✅ "IT Salaries in Romania 2026: The Complete Guide"
- ✅ "How to Hire Remote Developers in Romania | Wise Step"
- ❌ "Recruitment Tips and Tricks" (vague, no keyword)
- ❌ "The Ultimate Game-Changing Guide to Hiring the Best Tech Talent Ever" (too long + hype)

### Meta Description
- **Length**: 150–160 chars
- **Primary keyword**, naturally
- **Direct answer**: literally answer the target query (see AEO)
- **Concrete value + CTA**; never cut off mid-sentence

**Formula**: `[Question/stakes]? [Sourced answer/benefit]. [CTA].`

**Examples**:
- ✅ "What do IT engineers earn in Romania in 2026? Full salary bands by role and seniority, sourced from market data. See the complete guide." (150 chars)
- ✅ "Hiring remote developers in Romania? A step-by-step 2026 playbook for AI, ML and data teams — timelines, costs, and pitfalls. Read the playbook." (156 chars)
- ❌ "This post talks about recruitment and hiring in Romania and related topics." (vague, no value, no CTA)

### URL Slug
- Primary keyword; lowercase; hyphens (not underscores); 3–5 words; drop stop words
- **Format**: `/blog/[primary-keyword-phrase]/`
- Mirror the slug on the RO version (confirm the RO path — see `internal-links-map.md`)

**Examples** (match live site patterns):
- ✅ `/blog/it-salaries-romania-2026/`
- ✅ `/blog/hire-remote-developers-romania/`
- ✅ `/blog/headhunting-romania/`
- ❌ `/blog/the-complete-guide-to-it-salaries-in-romania-for-2026/` (too long)

## Internal Linking Strategy

Always check `context/internal-links-map.md` for the current, real link targets before adding links.

### Requirements
- **Minimum**: 3 internal links per article
- **Optimal**: 4–5
- **Maximum**: 7 (more allowed on 3,000+ word pillars)

### Link Types
1. **Pillar blog content (1–2)** — e.g. the salary guide, the CEE trends piece
2. **Related blog posts (2–3)** — build the content web across the 9 live posts
3. **Service page (0–1)** — link to `/services/` only when contextually natural, never forced
4. **Contact / CTA (0–1)** — `/contact/` for "brief a search" / "book a discovery call"

### Best Practices
- **Anchor text**: descriptive, varied, keyword-aware ("our 2026 Romanian salary guide"); never "click here"; don't reuse the exact same anchor for one page
- **Placement**: within body paragraphs; max 2 links per paragraph; distributed, not clustered; early links carry more weight
- **EN↔RO**: link EN posts to EN targets, RO to RO
- Keep links current and functional

## External Linking Strategy

### Requirements
- **Minimum**: 2 external links per article
- **Optimal**: 3–4 authority links
- Purpose: cite sources, support every stat (this is mandatory under our voice, not optional)

### What to Link
- **Statistics / market data**: always cite the source (this is the credibility bar)
- **Research / reports**: link the original
- **Regulation / official info**: e.g. EU AI Act text, ANAF/tax sources, EU institutions
- **Industry authorities**: recognised sector data

### Quality Standards
- **Authority**: credible, recognised sources
  - ✅ Eurostat, INS (Romanian statistics), ANIS, Stack Overflow Developer Survey, official EU/legal sources, established tech-press
  - ❌ Random low-authority blogs, unsourced aggregators
- **Relevance**: must directly support the claim
- **Freshness**: prefer data within 1–2 years
- **Functional**: no broken links

### Link Attributes
- Standard external links: no special attribute
- Sponsored/affiliate: `rel="sponsored"` or `rel="nofollow"`
- UGC: `rel="nofollow"`

## Readability Optimization

Target: **plain but authoritative** — write like an engineer explaining to a peer (see `style-guide.md`).

### Reading Level
- Roughly 8th–10th grade (Flesch-Kincaid) for accessibility — but never dumb down technical accuracy; define non-obvious terms on first use

### Sentence Structure
- Mix short punchy lines (carry the argument) with longer explanatory ones
- Break sentences over ~25 words
- Active voice predominant (80%+)

### Paragraph Structure
- 2–4 sentences; one idea each; no walls of text; mobile-friendly

### Scannability
- Subheading every ~300–400 words
- Lists and tables for anything sequential or comparative (playbook-shaped)
- Bold the load-bearing claim, not everything

## Content Quality Standards

### E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)

#### Experience
- Lean on first-hand experience — the founders have run these searches and been engineers themselves
- Use real placement scenarios and market observations, not generic advice

#### Expertise
- Accurate, specific detail on stacks, roles, and the hiring market
- Back every claim with data or a concrete example
- Actionable: a benchmark, timeline, screening question, or decision

#### Authoritativeness
- Cite credible sources; reference real market data
- Leverage the engineer-founder positioning and our own market intelligence
- Social proof where relevant: 5.0/5 on Clutch (7 reviews) — see `features.md`

#### Trustworthiness
- Honest — name uncomfortable truths (tax changes, counter-offers) instead of a clean story
- Don't overpromise; source every statistic; keep content current

### Originality
- Never plagiarise; add a first-hand, sourced angle competitors don't have
- Current examples, most-recent data, a take that could only be Wise Step's

### Factual Accuracy
- Verify every statistic; keep processes/market facts current; technical terminology must be correct
- Human review + fact-check is the publish gate — nothing ships without passing it

## Image Optimization

### Requirements
- Relevant, clean, compressed (WebP), mobile-friendly (Canva for assets)

### Image SEO
- **File names**: descriptive, keyword-rich — ✅ `it-salaries-romania-2026-by-role.png` ❌ `IMG_1234.png`
- **Alt text**: describe the image, keyword where natural, ≤125 chars, no "image of"
- **Placement**: break up long sections; after the concept, not before

## AEO / AI Search Optimization

AI answer engines (ChatGPT, Perplexity, Gemini, Claude, Google AI Overviews) are a core channel for us — appearing in AI answers on Romania/CEE recruitment queries is an explicit goal. These rules make content perform in both classic search AND AI answers.

### Direct-Answer-First
AI pulls from the earliest clear answer on the page.
- **Answer the query in the first 1–2 sentences**, before the narrative hook
- For "best/how/what" queries, state the answer or thesis immediately
- Put the core answer in the meta description too
- Don't bury the answer behind 200 words of context
- The reversal hook and intro still apply — they come *after* the direct answer

**Before**: "Hiring in Eastern Europe has changed a lot. For years companies… [200 words] …so the answer is speed."
**After**: "In 2026, hire engineers in Romania in ~28–30 days by using a specialised recruiter for the scarce Cloud/DevOps and Data/AI roles job ads can't reach. Here's the playbook."

### TL;DR / Key Takeaways Block
Include after the intro, before the first H2 body section.
```markdown
> **Key Takeaways**
> - [Sourced finding #1 — with a number/name]
> - [Sourced finding #2]
> - [Sourced finding #3]
```
- 3–5 bullets max; each a complete standalone claim (not a teaser)
- Specific numbers/names/outcomes — these are the article's real conclusions up front
- Not a table of contents

### Authority Signaling for AI
Include in every article (in frontmatter for the Astro build to render):
- **Named author** — Calin Muresan (the blog's author voice), not "Team"
- **Reviewer/editor credit** where applicable
- **Visible last-updated date** on the page
- **Year in title** for time-sensitive topics ("IT Salaries in Romania 2026")
- **Sourced claims throughout** — the single strongest signal for us

### One Idea Per Section
AI parses by section — each H2/H3 covers one clear idea, so a specific section can be cited cleanly. Use lists/tables within sections; avoid paragraphs that blend topics.

### FAQ Sections as Prompt Targets
Double duty: Google's People Also Ask + the question format users type into ChatGPT/Perplexity.
- Write questions in natural prompt language (how people actually ask)
- Answer directly in the first sentence, then expand
- 4–6 questions per article
- Source questions from real client questions, Reddit, search suggestions

### Bilingual (EN/RO) for AEO
- Publish both EN and RO — RO captures local queries AI answers in Romanian
- Translate the meaning and the sharp voice, not word-for-word
- Mirror structure, slug, and FAQ across both
- Keep stack/role names identical in both languages

### Content Repurposing for Citation Surface
AI pulls from LinkedIn, Medium, Reddit, Quora, YouTube transcripts — not just the site. Repurpose each article across surfaces (LinkedIn is our primary distribution) with attribution back to wise-step.ro. Handled via `/repurpose`; writers should keep it in mind.

### AI Citation Audit
For competitive topics, audit which sources AI actually cites. See `context/ai-citation-targets.md` and the `/research-ai-citations` command.

## Content Refresh Strategy

### When to Update
- 12+ months old; outdated stats (salary bands move); changed market/regulation; competitor content surpassed ours; rankings declined; new data available

### What to Update
- Last-updated date; stats with current data; examples/benchmarks; SEO focus if the keyword shifted; internal links to newer posts
- Salary and market figures especially — they date fast

## SEO & AEO Checklist for Every Article

### Content
- [ ] Appropriate length for type
- [ ] Primary keyword identified; density ~1–2%
- [ ] 3–5 secondary keywords; semantic terms integrated
- [ ] Unique, first-hand value vs. competitors
- [ ] Every statistic sourced — no unsourced claims or invented figures

### Structure
- [ ] One H1 with keyword; 4–7 H2s; 2–3 with keyword variations
- [ ] Proper H1>H2>H3 hierarchy; sentence-case headings
- [ ] Keyword in first 100 words and conclusion

### Meta
- [ ] Title 50–60 chars with keyword, no hype
- [ ] Description 150–160 chars, answers the query, has CTA
- [ ] Slug has keyword; RO version mirrored
- [ ] All meta unique

### Links
- [ ] 3–5 internal links from `internal-links-map.md`, descriptive varied anchors
- [ ] 2–3 external authority links; every stat cited
- [ ] All functional; EN↔RO matched

### Readability
- [ ] Plain but authoritative; mixed sentence length; active voice
- [ ] Paragraphs 2–4 sentences; subheading every ~300–400 words; lists/tables used

### Images
- [ ] Relevant; descriptive file names; keyword alt text ≤125 chars; WebP/optimised

### AEO
- [ ] Direct answer in first 1–2 sentences (not buried)
- [ ] Key Takeaways block after intro
- [ ] Meta description answers the target query
- [ ] FAQ (4–6) in natural prompt language
- [ ] Named author (Calin Muresan); visible last-updated date
- [ ] Year in title for time-sensitive topics
- [ ] RO version published and mirrored

### Quality (deal-breakers)
- [ ] No spelling/grammar errors
- [ ] Factually accurate; sources cited
- [ ] Brand voice — sharp, anti-hype, could only be Wise Step
- [ ] Actionable takeaway; honest CTA
- [ ] No hype adjectives, corporate fluff, or "family" tone

## SEO Tools & Resources

### Tools we use
- **Rankings/measurement**: Google Search Console
- **Keyword/SERP data**: DataForSEO (via this repo's scripts)
- **Distribution + topic spotting**: LinkedIn
- **Drafting/translation/AEO planning**: Claude (Projects + skills)
- **Visuals**: Canva
- **Publish**: GitHub commit → Cloudflare Pages deploy

### Reference
- Google Search Quality Evaluator Guidelines
- Search Engine Journal, Ahrefs Blog, Backlinko (general SEO)
- Eurostat / INS / ANIS (Romanian & EU market data), Stack Overflow Developer Survey (developer data)

---

**Remember**: SEO and AEO serve the reader. Never trade accuracy, honesty, or a sourced claim for a keyword. The best ranking signal we have is content that could only have been written by engineers who've done the work — sharp, sourced, and genuinely useful.
