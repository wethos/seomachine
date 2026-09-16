# Write Command

Use this command to create comprehensive, SEO-optimized long-form blog content.

## Usage
`/write [topic or research brief]`

## What This Command Does
1. Creates complete, well-structured long-form articles (2000-3000+ words)
2. Optimizes content for target keywords and SEO best practices
3. Maintains your brand voice and messaging throughout
4. Integrates internal and external links strategically
5. Includes all meta elements for publishing

## Process

### Pre-Writing Review
- **Research Brief**: Review research brief from `/research` command if available
- **Brand Voice**: Check @context/brand-voice.md for tone and messaging
- **Writing Examples**: Study @context/writing-examples.md for style consistency
- **Style Guide**: Follow formatting rules from @context/style-guide.md
- **SEO Guidelines**: Apply requirements from @context/seo-guidelines.md
- **Target Keywords**: Integrate keywords from @context/target-keywords.md naturally

### Content Structure

#### 1. Headline (H1)
- Include primary keyword naturally
- Create compelling, click-worthy title
- Keep under 60 characters for SERP display
- Promise clear value to reader

#### 2. Introduction (150-250 words)

**CRITICAL: Direct Answer First (AI Search Optimization)**

For any "best/top/how" query, the first 1-2 sentences MUST directly answer the question. AI scrapers (ChatGPT, Perplexity, Gemini) pull from the top of the page. Don't bury the answer behind narrative.

**Example — "best project management tools":**
> The best project management tools in 2026 are Asana, Monday, and ClickUp — each built for different team sizes and workflows. Here's how they compare.

After the direct answer, use a hook to keep human readers engaged.

**Choose ONE hook type for each article:**

**Default to the reversal opener** ("used to be X, now it's Y") when no stronger structure fits — it is the house hook. See `context/brand-voice.md`.

| Hook Type | Example | Best For |
|-----------|---------|----------|
| **Reversal (default)** | "Romania used to be a cost play. In 2026, it's a speed play." | Overturning a lazy assumption |
| **Sourced Statistic** | "IT salaries rose 5% in H1 2026. Inflation ran 10.4%." | Data-driven topics |
| **Contradiction** | "Romania ranks 7th of 11 in CEE for AI. Its high schoolers rank 4th of 108 in the world." | Two true facts that appear to conflict |
| **Bold Statement** | "This is not generic HR." | Positioning and differentiation |
| **Uncomfortable Truth** | "The standard counter-offer lands within 48 hours. Nobody warns you." | Naming friction competitors hide |

Every hook must carry a number, a named fact, or a sourced claim. A hook that is exciting but empty is wrong.

**After the hook, follow the APP Formula:**
- **Agree**: Acknowledge something the reader already believes/feels
- **Promise**: Tell them exactly what they'll learn or gain
- **Preview**: Brief overview of what's coming (can include mini table of contents for long posts)

- **Keyword**: Include primary keyword in first 100 words
- **Credibility**: Establish why you/this article is authoritative

#### 3. Key Takeaways Block (After Introduction)

**REQUIRED: TL;DR block immediately after the introduction, before the first H2 body section.**

This gets pulled into AI-generated summaries and helps both AI and human readers quickly assess the article's value.

```markdown
> **Key Takeaways**
> - [Core finding or recommendation #1]
> - [Core finding or recommendation #2]
> - [Core finding or recommendation #3]
> - [Core finding or recommendation #4 if needed]
> - [Core finding or recommendation #5 if needed]
```

**Rules:**
- 3-5 bullet points
- Each bullet is a standalone claim with specifics (numbers, names, outcomes)
- NOT a table of contents — these are the article's actual conclusions
- Written after the full article is drafted (so the takeaways are accurate)

#### 4. Main Body (1800-2500+ words)
- **Logical Flow**: Organize sections in clear, progressive order
- **H2 Sections**: 4-7 main sections covering comprehensive topic scope
- **H3 Subsections**: Break complex sections into digestible pieces
- **Keyword Integration**: Use primary keyword 1-2% density, variations throughout
- **Depth**: Provide thorough, actionable information at each point
- **Data**: Reference statistics and studies to support claims
- **Visuals**: Note where images, screenshots, or graphics enhance understanding
- **Video (optional, only if genuinely available)**: Embed a video only when Wise Step has published one on the topic. Do NOT embed a third-party video to satisfy a checklist — an unvetted video can contradict our sourced figures on the same page. Skip it and note the gap instead.
- **Lists**: Use bulleted or numbered lists for scannability
- **Formatting**: Bold key concepts, use short paragraphs (2-4 sentences MAX)

**REQUIRED: Concrete grounding (2-3 per article)**

> ⛔ **Never invent a person, company, client, or anecdote.** No fictional names, no "Sarah," no "the team at Acme Corp," no composite case studies presented as real. Fabricated examples are a deal-breaker under `context/brand-voice.md` — every claim earns its place with a number, a named fact, or a source. This rule outranks any engagement technique.

Ground the argument in specifics drawn from one of these **permitted** sources:

1. **First-hand market observation** — what we actually see running searches. "The question we get from clients every week is…" Written in "we" voice, no invented detail.
2. **Named, citable clients and testimonials** — only those already public on Clutch (see `context/features.md`), quoted verbatim and attributed by role and company.
3. **Worked arithmetic on sourced figures** — walk the reader through a real calculation. "A candidate on RON 8,000 net needs RON 8,413 to match last year's purchasing power." This does the memorability job of a story without inventing anyone.
4. **Named market events** — a tax change, a published salary release, a regulation with a date.

**Placement**: one early (grounds the hook), one mid-article (re-engages skimmers), one near the conclusion (reinforces the takeaway).

**REQUIRED: Contextual CTAs (2-3 per article)**

Don't just put one CTA at the end. Embedded CTAs get 121% more conversions than end-only CTAs.

**CTA Placement Strategy:**
| Location | CTA Type | Example |
|----------|----------|---------|
| After first major value section | Soft (learn more) | "The role-level bands are in our [2026 Romanian salary guide]." |
| After comparison/proof section | Medium (engage) | "Want the benchmark for your specific role and stack? That's what our [market intelligence] work covers." |
| End of article | Strong (convert) | "Tell us what you're hiring for and we'll give you a straight read on what it takes to close in this market. [Brief your search]" |

**Honest framing only** — no false urgency, no "limited time," no free-trial language (we don't sell a product). Never publish the fee percentage; public framing is "quoted per engagement." See `context/features.md`.

**CTA Rules:**
- Make CTAs contextual (relate to the section content)
- Vary the format (inline text, bold callout, button-style)
- First CTA should appear within the first 500 words
- Never use generic "Click here" text

#### 5. Conclusion (150-200 words)
- **Recap**: Summarize 3-5 key takeaways
- **Action**: Provide clear next steps for reader
- **CTA**: Include relevant call-to-action (brief a search, book a discovery call) — honest framing, tied to a benchmark or decision
- **Encouragement**: End on empowering, forward-looking note

### SEO Optimization

#### Keyword Placement
- H1 headline
- First paragraph (within first 100 words)
- At least 2-3 H2 headings
- Naturally throughout body (1-2% density)
- Meta title and description
- URL slug

#### Internal Linking (3-5+ links)
- Reference @context/internal-links-map.md for key pages
- Link to relevant pillar content from your site
- Link to related blog articles
- Link to product/service pages where natural
- Use descriptive anchor text with keywords

#### External Linking (2-3 links)
- Link to authoritative sources for statistics
- Reference industry research or studies
- Link to tools or resources mentioned
- Build credibility with quality sources

#### Readability
- Keep sentences under 25 words average
- Use transition words between sections
- Vary sentence length for rhythm
- Write at 8th-10th grade reading level
- Use active voice predominantly
- Break up text with subheadings every 300-400 words

### Target Audience Focus
- **Audience Perspective**: Write for your target audience (defined in @context/brand-voice.md)
- **Practical Application**: Show how information applies to their specific challenges
- **Product Integration**: Naturally mention how your features solve problems (reference @context/features.md)
- **Industry Context**: Reference relevant trends and best practices
- **Technical Accuracy**: Ensure terminology and processes are correct for technical recruitment

### Brand Voice Consistency
- Maintain your brand tone (reference @context/brand-voice.md for specifics)
- Follow your established voice pillars
- Use messaging framework from your context files
- Apply terminology preferences consistently
- Match tone to content type (how-to, strategy, news, etc.)

## Output
Provides a complete, publish-ready article including:

### 1. Article Content
Full markdown-formatted article with:
- H1 headline
- Introduction
- Body sections with H2/H3 structure
- Conclusion with CTA
- Proper formatting and styling

### 2. Meta Elements
```
---
Meta Title: [50-60 character optimized title]
Meta Description: [150-160 character compelling description]
Primary Keyword: [main target keyword]
Secondary Keywords: [keyword1, keyword2, keyword3]
URL Slug: /blog/[optimized-slug]
Internal Links: [list of pages linked from your site]
External Links: [list of external sources]
Word Count: [actual word count]
---
```

### 3. SEO Checklist
- [ ] Primary keyword in H1
- [ ] Primary keyword in first 100 words
- [ ] Primary keyword in 2+ H2 headings
- [ ] Keyword density 1-2%
- [ ] 3-5+ internal links included
- [ ] 2-3 external authority links
- [ ] Meta title 50-60 characters
- [ ] Meta description 150-160 characters
- [ ] Length matches content type per `context/seo-guidelines.md` (standard 1,500-3,000 · pillar 3,000-5,000 · playbook 1,500-2,500 · market take 800-1,200)
- [ ] Proper H2/H3 hierarchy
- [ ] Readability optimized

### 4. AI Search Optimization Checklist
- [ ] **Direct answer**: First 1-2 sentences directly answer the target query
- [ ] **Key Takeaways**: TL;DR block with 3-5 specific bullet points after introduction
- [ ] **Meta description**: Directly answers the query (not just a teaser)
- [ ] **Video**: embedded only if Wise Step published one on the topic (otherwise skip, and say so)
- [ ] **FAQ prompts**: Questions written in natural language people would type into ChatGPT
- [ ] **One idea per section**: Each H2/H3 focuses on a single clear concept
- [ ] **Author attribution**: Named author in frontmatter

### 5. Engagement Checklist
- [ ] **Hook**: Opens with question, scenario, statistic, or bold statement (NOT generic definition)
- [ ] **APP Formula**: Introduction includes Agree, Promise, Preview elements
- [ ] **Concrete grounding**: 2-3 specifics, none of them invented
- [ ] **Contextual CTAs**: 2-3 CTAs placed throughout (not just at end)
- [ ] **First CTA**: Appears within first 500 words
- [ ] **Paragraph length**: No paragraphs exceed 4 sentences
- [ ] **Sentence rhythm**: Mix of short (5-10 words) and longer sentences (15-25 words)

## File Management
After completing the article, automatically save to:
- **File Location**: `drafts/[topic-slug]-[YYYY-MM-DD].md`
- **File Format**: Markdown with frontmatter and formatted content
- **Naming Convention**: Use lowercase, hyphenated topic slug and current date

Example: `drafts/content-marketing-strategies-2025-10-15.md`

## Automatic Content Scrubbing

**CRITICAL**: Immediately after saving the article file, automatically invoke the content scrubber to remove AI watermarks and telltale patterns.

### Why This Matters
AI-generated content often contains invisible Unicode watermarks and characteristic patterns (like em-dash overuse) that can identify it as AI-written. Scrubbing removes these indicators to make content appear naturally human-written.

### Scrubbing Process
1. **Invoke Scrubber**: Run `/scrub [file-path]` on the saved article file
2. **Automatic Execution**: This should happen automatically, not require user action
3. **Timing**: Must occur immediately after file save, before any other processing
4. **Scope**: Scrub the main article file only (not meta or analysis files)

### What Gets Cleaned
- Invisible Unicode watermarks (zero-width spaces, BOMs, format-control characters)
- Em-dashes replaced with contextually appropriate punctuation (commas, semicolons, periods)
- Whitespace normalization and formatting cleanup
- All changes preserve content meaning and markdown structure

### Verification
The scrubber will display statistics:
- Unicode watermarks removed
- Format-control characters removed
- Em-dashes replaced

### Example Workflow
```
1. Write article → Save to drafts/article-name-2025-10-31.md
2. IMMEDIATELY run: /scrub drafts/article-name-2025-10-31.md
3. Verify scrubbing statistics
4. THEN proceed with optimization agents below
```

This ensures all published content is free of AI signatures before any further processing.

## Automatic Agent Execution
After saving the main article, immediately execute optimization agents:

### 1. Content Analyzer Agent (NEW!)
- **Agent**: `content-analyzer`
- **Input**: Full article, meta elements, keywords, SERP data (if available)
- **Output**: Comprehensive analysis covering search intent, keyword density, content length comparison, readability score, and SEO quality rating
- **File**: `drafts/content-analysis-[topic-slug]-[YYYY-MM-DD].md`

This new agent uses 5 specialized analysis modules:
- Search intent analysis
- Keyword density & clustering
- Content length vs competitors
- Readability scoring (Flesch scores)
- SEO quality rating (0-100)

### 2. SEO Optimizer Agent
- **Agent**: `seo-optimizer`
- **Input**: Full article content
- **Output**: SEO optimization report and suggestions
- **File**: `drafts/seo-report-[topic-slug]-[YYYY-MM-DD].md`

### 3. Meta Creator Agent
- **Agent**: `meta-creator`
- **Input**: Article content and primary keyword
- **Output**: Multiple meta title/description options
- **File**: `drafts/meta-options-[topic-slug]-[YYYY-MM-DD].md`

### 4. Internal Linker Agent
- **Agent**: `internal-linker`
- **Input**: Article content
- **Output**: Specific internal linking recommendations
- **File**: `drafts/link-suggestions-[topic-slug]-[YYYY-MM-DD].md`

### 5. Keyword Mapper Agent
- **Agent**: `keyword-mapper`
- **Input**: Article and target keywords
- **Output**: Keyword placement analysis and improvements
- **File**: `drafts/keyword-analysis-[topic-slug]-[YYYY-MM-DD].md`

## Automatic Quality Loop

After saving the initial draft, automatically run the content quality scorer:

### Step 1: Score Content
Run the content scorer to evaluate the draft:
```bash
python data_sources/modules/content_scorer.py drafts/[article-file].md
```

### Step 2: Evaluate Score
The scorer evaluates 5 dimensions (composite score must be ≥70):

| Dimension | Weight | Target |
|-----------|--------|--------|
| Humanity/Voice | 30% | No AI phrases, use contractions |
| Specificity | 25% | Concrete examples, numbers, names |
| Structure Balance | 20% | 40-70% prose (not all lists) |
| SEO Compliance | 15% | Keywords, meta, structure |
| Readability | 10% | Flesch 60-70, grade 8-10 |

### Step 3: Auto-Revise if Needed
If composite score < 70:
1. Review the `priority_fixes` from the scorer
2. Apply the top 3-5 fixes automatically
3. Re-score the content
4. Repeat once more if still below threshold

### Step 4: Route Based on Final Score
- **Score ≥ 70**: Save to `drafts/` and proceed to optimization agents
- **Score < 70 after 2 iterations**: Save to `review-required/` with a `_REVIEW_NOTES.md` file containing the scoring details and remaining issues

### Review-Required Folder
Articles that fail quality threshold after 2 revision attempts go to `review-required/`:
```
review-required/
├── article-name-2025-12-10.md
└── article-name-2025-12-10_REVIEW_NOTES.md
```

The `_REVIEW_NOTES.md` file contains:
- Final composite score
- Dimension breakdown
- Remaining priority fixes
- Reason for human review

## Quality Standards
Every article must meet these requirements:

### Content Requirements
- Length per content type in `context/seo-guidelines.md` — standard post 1,500-3,000, pillar 3,000-5,000, playbook 1,500-2,500, sharp market take 800-1,200. **Never pad to hit a count**; 2,000 sourced words beat 3,000 padded ones. If a research brief sets a tighter target, the brief wins.
- Proper H1/H2/H3 hierarchy
- Primary keyword naturally integrated
- 3-5 internal links to your site content
- 2-3 external authoritative links
- Compelling meta title and description
- Clear introduction and conclusion
- Actionable, valuable information
- Brand voice maintained
- Target audience focused

### Engagement Requirements
- **Compelling hook** in first 1-2 sentences (no generic openings)
- **2-3 concrete groundings** from permitted sources (first-hand observation, public testimonial, worked arithmetic, named market event) — never invented
- **2-3 contextual CTAs** distributed throughout (not just at end)
- **First CTA within 500 words**
- **No paragraphs longer than 4 sentences**
- **Varied sentence rhythm** (mix short punchy + longer flowing)

### Quality Score
- **Composite quality score ≥70**
- Publish-ready quality

This ensures every article is comprehensive, optimized, engaging, and ready to rank while providing genuine value to your target audience.
