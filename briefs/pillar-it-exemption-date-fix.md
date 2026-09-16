# Pillar fix — the IT exemption date is wrong on two live pages

*Generated 2026-09-03. For the **wise-step.ro Astro repo** (separate from seomachine). Paste below the rule into an agent, or apply by hand — it is two sentences.*

---

Two live pages state the Romanian IT income-tax exemption was removed **in 2024**. That is imprecise, and it is about to contradict four new articles that cite the exact instruments.

## Why this is worth fixing now, not "at next refresh"

The new cost articles carry a callout telling readers to **"check the ordinance, not a blog post — this one included."** Publishing them while the salary pillar still says "removed in 2024" puts two Wise Step pages in disagreement on a statutory date, on the sharpest claim in the piece. That breaches the sourcing bar in `context/brand-voice.md`.

## What is actually true (verified 2026-09-03 against primary texts)

| Step | Instrument | Effect |
|---|---|---|
| Capped | **Legea 296/2023**, 26 October 2023 | Exemption limited to gross monthly income up to **10,000 lei inclusive**, from November 2023 income. The law's own wording: *"Scutirea se aplică la locul unde se află funcţia de bază, pentru veniturile brute lunare de până la 10.000 lei inclusiv."* Source: `https://static.anaf.ro/static/10/Anaf/legislatie/L_296_2023.pdf` |
| Eliminated | **OUG 156/2024**, MO nr. 1334/2024 | Exemption removed entirely for income earned **from January 2025** onward. Source: `https://static.anaf.ro/static/10/Anaf/legislatie/OUG_156_2024.pdf` |

⚠ **Not OUG 115/2023.** An earlier internal note attributed the 10,000 lei cap to OUG 115/2023. That was wrong and has been corrected across our drafts. OUG 115/2023 made separate changes to the IT and construction facilities effective January 2024; it is not the source of the cap.

## Edit 1 — EN pillar

**File:** the source for `https://wise-step.ro/blog/it-salaries-romania-2026/` (grep for `not fully compensated`)

Find:
```
the loss of the 10% income-tax exemption removed in 2024.
```
Replace with:
```
the loss of the 10% income-tax exemption — capped at 10,000 lei gross from November 2023 by Legea 296/2023, then eliminated by OUG 156/2024 for income earned from January 2025.
```

## Edit 2 — RO pillar

**File:** the source for `https://wise-step.ro/ro/blog/it-salaries-romania-2026-ro/` (grep for `nu au fost compensați`)

Find:
```
pierderea scutirii de impozit pe venit de 10% eliminată în 2024.
```
Replace with:
```
pierderea scutirii de impozit pe venit de 10% — plafonată la 10.000 lei brut din noiembrie 2023 prin Legea 296/2023, apoi eliminată prin OUG 156/2024 pentru veniturile obținute din ianuarie 2025.
```

Leave the sentence that follows each one untouched (EN: the net-terms line; RO: *"În termeni neti, mulți au simțit stagnare…"*).

## Do not change

- **The 72% statistic itself.** Only the date claim is wrong. ⚠ But flag for the content owner: it is not recorded which change that 72% measures — the November 2023 cap or the January 2025 removal. Re-check it against its original source at the next data refresh. Do not restate it more precisely than the source supports.
- Anything else on either page. This is a two-sentence correction, not a refresh.

## Worth doing in the same release (optional, same files)

`context/internal-links-map.md` flags that the salary pillar and the salary calculator should link to each other, and that the pairing is missing. Since you are already editing both pillar files:

| From | To |
|---|---|
| `/blog/it-salaries-romania-2026/` | `https://wise-step.ro/salary-calculator/` |
| `/ro/blog/it-salaries-romania-2026-ro/` | `https://wise-step.ro/ro/calculator-salariu/` ← translated slug, no `-ro` suffix; `/ro/salary-calculator/` is a verified 404, do not derive it |

Place each where the page first quotes a gross or net figure. Suggested anchors — EN: "gross-to-net salary calculator"; RO: **"calculator salariu net"** (the highest-volume Romanian term in the portfolio).

## Verify after

1. Both pages return 200 and render.
2. `grep` each for `removed in 2024` / `eliminată în 2024` — expect zero hits.
3. The 72% figure still reads correctly in its sentence.
4. Any added links resolve.
