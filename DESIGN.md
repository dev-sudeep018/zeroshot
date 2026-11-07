---
name: ZeroShot
description: A dark learning workspace with a separate public introduction.
colors:
  bg: "#101416"
  surface: "#171d20"
  raised: "#1e2629"
  hover: "#253033"
  border: "#303b3f"
  border-strong: "#647571"
  text: "#eceee9"
  muted: "#a5afad"
  subtle: "#95a29f"
  accent: "#b6dac6"
  accent-ink: "#13241b"
  accent-hover: "#cce8d9"
  accent-soft: "#22372d"
  selection: "#345749"
  code: "#d5ded9"
  success: "#91d5a8"
  danger: "#f3a0a6"
  danger-surface: "#362126"
  warning: "#e6c187"
  warning-surface: "#342c1e"
  info: "#9ebee8"
  syntax-keyword: "#c4b7ef"
  syntax-string: "#a5d7b8"
  syntax-number: "#e4bd8d"
  topic-math: "#a7ceba"
  topic-math-surface: "#21332c"
  topic-deep: "#a9bedc"
  topic-deep-surface: "#242e3d"
  topic-engineering: "#d7bd95"
  topic-engineering-surface: "#342e24"
  public-surface: "#141b1c"
  portal-navigation: "#141a1c"
typography:
  display:
    fontFamily: '"Manrope", "Segoe UI", sans-serif'
    fontSize: "clamp(54px, 5.55vw, 78px)"
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "-0.04em"
  headline:
    fontFamily: '"Manrope", "Segoe UI", system-ui, sans-serif'
    fontSize: "30px"
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "-0.03em"
  title:
    fontFamily: '"Manrope", "Segoe UI", system-ui, sans-serif'
    fontSize: "20px"
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "-0.015em"
  body:
    fontFamily: '"Manrope", "Segoe UI", system-ui, sans-serif'
    fontSize: "14px"
    lineHeight: 1.6
  label:
    fontFamily: '"Manrope", "Segoe UI", system-ui, sans-serif'
    fontSize: "12px"
    fontWeight: 600
  code:
    fontFamily: 'Consolas, "Liberation Mono", monospace'
    fontSize: "14px"
    lineHeight: "24px"
rounded:
  compact: "4px"
  field: "6px"
  control: "7px"
  standard: "8px"
  container: "10px"
  working-panel: "12px"
spacing:
  tight: "4px"
  small: "8px"
  control: "12px"
  content: "16px"
  section: "20px"
  roomy: "24px"
  group: "32px"
  page: "40px"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.accent-ink}"
    rounded: "{rounded.control}"
    padding: "11px 17px"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.control}"
    padding: "9px 15px"
  public-primary:
    backgroundColor: "{colors.accent}"
    rounded: "{rounded.field}"
    padding: "14px 21px"
  auth-field:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.field}"
    padding: "10px 13px"
  topic-label:
    rounded: "{rounded.compact}"
    padding: "3px 7px"
  working-panel:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.working-panel}"
    padding: "26px"
---

# Design System: ZeroShot

## Overview

**Creative North Star: "A clear practice workbench"**

A clear practice workbench. Charcoal grounds, warm off-white type, and restrained seafoam actions support reading, experimentation, and code. This records the implemented dark system on 7 November 2026 and supersedes the earlier light-theme notes, following the user's explicit direction.

The public introduction and learning portal share typography, color, and the compact ZeroShot mark. Their navigation and density stay distinct: broad public compositions explain the product; the portal puts the next task, saved work, and tools within reach. Component boundaries use tone and thin lines. Images of fictional users, decorative dashboards, and unsupported claims have no role in this system.

Implementation sources are the global, marketing, portal, and authentication stylesheets, their current components, and the desktop/mobile review captures. This is a visual specification, not a release or accessibility certification.

**Key Characteristics:**

- Charcoal grounds, warm off-white type, and restrained seafoam actions.
- Shared typography and identity with separate public and learning navigation.
- Flat surfaces, thin borders, readable lesson rows, and explicit status text.
- Self-hosted Manrope for the interface and monospace for code.

## Colors

Seafoam is the primary action and selection accent. Use its dark ink for filled actions and its soft surface for selected navigation. The hover shade provides immediate feedback without glow.

Charcoal background, surface, raised, and hover tokens form the neutral depth scale. Warm white carries headings and reading content; muted and subtle text serve secondary explanations and metadata. Strong borders identify editable fields and secondary actions. Public panels and the fixed portal navigation have their own closely related dark surfaces.

Topic colors distinguish mathematics, deep learning, and engineering with muted green, blue, and sand pairs. They support category labels and diagrams rather than recoloring whole pages. Syntax colors belong to code. Success, danger, warning, and information tokens are semantic, with dark error and warning surfaces.

**The Explicit State Rule.** Pair every diagnostic color with meaningful text or an icon. Accent indicates interaction; it does not imply that a lesson has passed.

## Typography

Manrope is self-hosted in the web public fonts directory with its license. Use the existing system fallbacks; no runtime font-provider request is required. Consolas and Liberation Mono carry code, filenames, and numeric operation previews.

The public display role is broad and tightly spaced, with seafoam emphasis inside the headline. Section headings are smaller and remain sentence case. Portal titles are compact; body text preserves a comfortable reading line and long lesson descriptions stay around 68–75 characters wide. Metadata is deliberately smaller than explanatory prose.

At narrow widths, the public headline resolves to 43px and the portal title to 26px. Account inputs use 16px text below 600px, while labels remain visually subordinate. Do not transplant public display scale into task screens.

## Layout

The public site uses a centered container capped at 1376px with 56px side padding, reduced to 36px at 1100px and 22px at 500px. Its desktop header is horizontal. At 800px navigation wraps into a second row and major two-column sections stack. The interactive explanation moves from three columns to two, then a single reading sequence at the narrowest breakpoint.

The portal has a fixed 224px left navigation column above 1099px. The content area begins beside it, with a 64px breadcrumb bar and a centered main region capped at 1360px. Page padding steps from 40px to 28px and then 20px. At 1099px the navigation becomes a top row with a labelled menu button. The expanded menu uses three columns, then two below 720px.

The dashboard's primary learning column and 280px companion column remain distinct until 720px, where they stack. The library uses readable, alternating lesson rows and explicit filters. Coding retains resizable panels and the existing narrow-screen reading/code switch. Account forms are centered at a maximum 420px; account management uses the portal shell and a maximum 960px region.

**The Separate Destinations Rule.** The public home explains ZeroShot and links into `/learn/`; it does not impersonate the learner's personal dashboard. Keep return links visible in both environments.

## Elevation & Depth

The current interface is flat. Tone, spacing, one-pixel borders, and selected fills separate regions. The public preview and next-lesson panel have contained surfaces, while path lists, curriculum rows, and account sections rely on dividers. Do not add floating shadows or ambient glow to ordinary controls.

Hover and selection change color or background. The public diagram and result bars reflect actual inputs; they are not background decoration. Respect the existing reduced-motion rules. Short control transitions communicate state without delaying actions.

## Shapes

Small rectangular controls use gentle corners. Metadata uses the compact radius; form fields and public calls to action use the field radius; portal buttons use the control radius. Larger working panels use the working-panel radius. Rows and account sections remain flat and square-edged.

The compact ZeroShot letter mark and wordmark are reused across public, portal, and authentication headers. Topic diagrams use thin neutral geometry derived from their subject. Avoid adding unrelated decorative symbols.

## Components

- **Actions:** filled seafoam is the primary action, bordered dark surfaces are secondary, and supporting links use text with underline on hover. Disabled buttons visibly dim. Keyboard focus is an explicit two-pixel outline with space from the control.
- **Navigation:** public links show the active destination with text and an underline. Portal navigation shows the active destination with a soft accent fill and persistent label. The narrow portal menu exposes its expanded state and remains keyboard operable.
- **Learning rows:** a title, concise explanation, topic, difficulty, and progress state establish a scan order. Alternate surface tone aids reading without turning every lesson into a floating card.
- **Working panels:** experiments, next lessons, progress, and backups use contained sections only where content needs grouping. Keep the relevant action close to its explanation.
- **Authentication:** visible email/password labels, a password visibility button, request status, and a separate guest action stay readable at mobile widths. Error notices receive focus and use alert semantics; success notices use status semantics. Account copy explicitly explains that sign-in does not synchronize code or progress yet.
- **Feedback:** test results pair color with text, expandable details, and recovery controls. Optional momentum records practice and does not imply expertise or remove progress after a missed week.

## Do's and Don'ts

- Do preserve the dark palette and distinguish the public website from the learning portal.
- Do use real interactive examples and actual learner state where available.
- Do keep focus visible, input labels explicit, and touch actions reachable.
- Do preserve guest learning and accurate local-storage explanations.
- Do keep code, content, and navigation in a readable order on narrow screens.
- Don't reintroduce the rejected light theme or merge the public home into the dashboard.
- Don't fabricate learners, outcomes, testimonials, or synchronization capabilities.
- Don't use color alone to explain success, error, topic, or selection.
- Don't add decorative gradients, glow, or shadow-heavy containers to this flat system.
