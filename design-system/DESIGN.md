# Ember — Design System

A warm, editorial take on shadcn/ui. Stone neutrals, one terracotta brand color, quiet surfaces, generous whitespace. Built on **shadcn/ui + Tailwind CSS v4 + Radix + lucide-react**, with tokens in `globals.css` (OKLCH, light + dark).

> **For Claude Design:** treat this file and `globals.css` as the source of truth. Use only the semantic tokens below — never raw hex/OKLCH in components, never Tailwind palette colors like `bg-orange-500`. Compose from shadcn/ui components and the recipes in §6 before inventing new ones. Design every screen in light **and** dark.

**Files**

| Path | What |
|---|---|
| `DESIGN.md` | This spec — rules, tokens, recipes, patterns |
| `globals.css` | Drop-in shadcn `app/globals.css` (Tailwind v4, light + dark). Requires `tw-animate-css` |
| `showcase.html` | Full single-page specimen |
| `previews/*.html` | One Claude Design card per area (`@dsCard` marker on line 1). Append `?dark` to view dark mode |

---

## 1. Principles

1. **One accent, used sparingly.** Terracotta (`primary`) marks the single most important action or state on a screen. Everything else is neutral.
2. **Quiet surfaces.** Separate areas with `border` hairlines and spacing, not heavy shadows or fills. Shadows are only for floating layers (popover, dialog, toast).
3. **Type does the hierarchy.** Size and weight first, color second. Body text is `foreground`; secondary text is `muted-foreground`. No third gray.
4. **Dense where it works, airy where it reads.** Data views use compact rows (h-9/h-10); marketing and empty states get room to breathe.
5. **Accessible by default.** Every text/background pair passes WCAG AA (≥ 4.5:1), including soft badges. Focus is always visible.

---

## 2. Color tokens

Use as Tailwind utilities: `bg-primary`, `text-muted-foreground`, `border-border`, `ring-ring`, etc. Values are exact copies of `globals.css`.

### Core

| Token | Light | Dark | Use |
|---|---|---|---|
| `background` | `oklch(0.99 0.003 75)` | `oklch(0.155 0.008 60)` | Page canvas |
| `foreground` | `oklch(0.18 0.012 60)` | `oklch(0.965 0.005 75)` | Body text |
| `card` | `oklch(1 0 0)` | `oklch(0.195 0.009 60)` | Cards, panels, table containers |
| `card-foreground` | `oklch(0.18 0.012 60)` | `oklch(0.965 0.005 75)` | |
| `popover` | `oklch(1 0 0)` | `oklch(0.21 0.009 60)` | Menus, popovers, dialogs, toasts |
| `popover-foreground` | `oklch(0.18 0.012 60)` | `oklch(0.965 0.005 75)` | |
| `primary` | `oklch(0.53 0.17 40)` | `oklch(0.7 0.15 45)` | Primary CTA, active state, links, checked controls |
| `primary-foreground` | `oklch(0.99 0.004 75)` | `oklch(0.18 0.03 40)` | |
| `secondary` | `oklch(0.955 0.006 75)` | `oklch(0.26 0.01 60)` | Secondary buttons |
| `secondary-foreground` | `oklch(0.24 0.012 60)` | `oklch(0.965 0.005 75)` | |
| `muted` | `oklch(0.955 0.006 75)` | `oklch(0.26 0.01 60)` | Subtle fills, tab lists, avatar fallback |
| `muted-foreground` | `oklch(0.5 0.014 60)` | `oklch(0.72 0.012 70)` | Helper text, captions, placeholders, table headers |
| `accent` | `oklch(0.945 0.025 50)` | `oklch(0.3 0.035 45)` | Hover/highlight for menu items, ghost & outline buttons |
| `accent-foreground` | `oklch(0.32 0.08 40)` | `oklch(0.93 0.04 55)` | |
| `border` | `oklch(0.91 0.007 70)` | `oklch(1 0 0 / 10%)` | Hairlines, card & table borders |
| `input` | `oklch(0.88 0.009 70)` | `oklch(1 0 0 / 15%)` | Form control borders, switch track (off) |
| `ring` | `oklch(0.53 0.17 40)` | `oklch(0.7 0.15 45)` | Focus rings |

### Status (extensions to stock shadcn)

| Token | Light | Dark |
|---|---|---|
| `destructive` / `-foreground` | `oklch(0.53 0.21 27)` / `oklch(0.99 0.004 75)` | `oklch(0.68 0.19 25)` / `oklch(0.18 0.03 25)` |
| `success` / `-foreground` | `oklch(0.5 0.12 155)` / `oklch(0.99 0.004 75)` | `oklch(0.72 0.14 155)` / `oklch(0.18 0.03 155)` |
| `warning` / `-foreground` | `oklch(0.78 0.15 80)` / `oklch(0.25 0.05 70)` | `oklch(0.82 0.14 80)` / `oklch(0.22 0.05 70)` |
| `info` / `-foreground` | `oklch(0.51 0.13 245)` / `oklch(0.99 0.004 75)` | `oklch(0.72 0.12 245)` / `oklch(0.18 0.03 245)` |

> **Warning is the exception:** `warning` is a light yellow and is **never** used as text in light mode. Soft-warning text is `text-warning-foreground` in light and `dark:text-warning` in dark.

### Charts (use in this order)

| Token | Light | Dark | Hue |
|---|---|---|---|
| `chart-1` | `oklch(0.6 0.17 40)` | `oklch(0.7 0.15 45)` | terracotta |
| `chart-2` | `oklch(0.55 0.1 185)` | `oklch(0.7 0.1 185)` | teal |
| `chart-3` | `oklch(0.42 0.06 250)` | `oklch(0.7 0.08 250)` | slate blue |
| `chart-4` | `oklch(0.8 0.14 85)` | `oklch(0.83 0.13 85)` | ochre |
| `chart-5` | `oklch(0.68 0.12 330)` | `oklch(0.74 0.12 330)` | rose |

Chart colors are for marks only, never for text or as a background behind text.

### Sidebar

| Token | Light | Dark |
|---|---|---|
| `sidebar` | `oklch(0.975 0.004 75)` | `oklch(0.18 0.008 60)` |
| `sidebar-foreground` | `oklch(0.18 0.012 60)` | `oklch(0.965 0.005 75)` |
| `sidebar-primary` / `-foreground` | `oklch(0.53 0.17 40)` / `oklch(0.99 0.004 75)` | `oklch(0.7 0.15 45)` / `oklch(0.18 0.03 40)` |
| `sidebar-accent` / `-foreground` | `oklch(0.945 0.008 70)` / `oklch(0.24 0.012 60)` | `oklch(0.26 0.01 60)` / `oklch(0.965 0.005 75)` |
| `sidebar-border` | `oklch(0.91 0.007 70)` | `oklch(1 0 0 / 10%)` |
| `sidebar-ring` | `oklch(0.53 0.17 40)` | `oklch(0.7 0.15 45)` |

### Surface layering

`background` (page) < `sidebar` < `card` (content containers) < `popover` (anything floating). In dark mode each step is slightly lighter; never put a `card` inside a `card` — use `border` + `muted` fills to nest instead.

---

## 3. Typography

| Role | Font | Tailwind |
|---|---|---|
| UI / body | **Geist** | `font-sans` |
| Code, IDs, numbers in tables | **Geist Mono** | `font-mono tabular-nums` |
| Display (marketing heroes only) | **Instrument Serif** | `font-serif` |

**Loading fonts:** with Next.js use `next/font` (`Geist`, `Geist_Mono` from `next/font/google`, `Instrument_Serif` weight 400) and point `--font-sans`/`--font-mono`/`--font-serif` at the generated variables (e.g. `var(--font-geist-sans)`). Otherwise load from Google Fonts.

| Name | Class | Size / line-height | Weight |
|---|---|---|---|
| Display | `font-serif text-6xl tracking-[-0.02em]` | 60/60 | 400 |
| H1 | `text-4xl font-semibold tracking-tight` | 36/40 | 600 |
| H2 | `text-2xl font-semibold tracking-tight` | 24/32 | 600 |
| H3 | `text-lg font-semibold` | 18/28 | 600 |
| Body | `text-sm` | 14/20 | 400 |
| Body large | `text-base` | 16/24 | 400 |
| Label | `text-sm font-medium` | 14/20 | 500 |
| Caption | `text-xs text-muted-foreground` | 12/16 | 400 |
| Overline | `text-xs font-medium uppercase tracking-wider text-muted-foreground` | 12/16 | 500 |

App UI defaults to `text-sm`. Max line length for prose is `max-w-prose`. Display serif appears at most once per page; italic serif words in `text-primary` are the only allowed emphasis in a display heading.

---

## 4. Spacing, radius, elevation, layout

- **Spacing:** Tailwind 4px grid. `gap-1.5` (6px) between icon and label, `px-3` inside inputs, `p-6` inside cards, `gap-4`/`gap-6` between cards, `space-y-8`/`space-y-12` between sections.
- **Radius:** `--radius: 0.625rem`. `rounded-sm` 6px (badges, tooltips, menu items), `rounded-md` 8px (buttons, inputs, menus), `rounded-lg` 10px (alerts, toasts, tab lists), `rounded-xl` 14px (cards, dialogs, table containers), `rounded-full` (avatars, switches, pills).
- **Elevation** uses Tailwind's default shadows:
  - none or `shadow-xs`: inputs and outline buttons
  - none: cards (border only)
  - `shadow-lg`: popovers, dropdowns, toasts
  - `shadow-xl` with a `bg-black/50` overlay: dialogs and sheets
- **Layout:** content `max-w-6xl mx-auto`, page padding `px-4 sm:px-6 lg:px-8`, top bar `h-14 border-b`, sidebar `w-64` (collapsed rail `w-14`).
- **Breakpoints (Tailwind defaults):** below `md` the sidebar becomes a `Sheet` opened from a menu button. Card grids go 1 → 2 (`sm`) → 3/4 columns (`lg`). Tables scroll horizontally inside their bordered container. Dialogs go full width with `mx-4`.

---

## 5. Interaction states (apply everywhere)

| State | Recipe |
|---|---|
| Focus | `focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 outline-none` |
| Invalid | `aria-invalid:border-destructive aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40` |
| Disabled | `disabled:pointer-events-none disabled:opacity-50` |
| Hover (neutral) | `hover:bg-accent hover:text-accent-foreground` |
| Hover (filled) | `hover:bg-primary/90` (same for `destructive`, `secondary/80`) |
| Selected / active nav | `bg-sidebar-accent text-sidebar-accent-foreground font-medium` |
| Checked controls | `data-[state=checked]:bg-primary data-[state=checked]:text-primary-foreground` |
| Table row hover | `hover:bg-muted/50` |

---

## 6. Component recipes (shadcn/ui)

Install with `npx shadcn@latest add <name>`. Only these variants exist.

**Button**: variants `default` (primary), `secondary`, `outline`, `ghost`, `link`, `destructive`; sizes `sm` (h-8), `default` (h-9), `lg` (h-10), `icon` (size-9). Use at most one `default` button per region. Icons are lucide `size-4` with `gap-2`. Labels are verbs in sentence case.

**Badge**: base `inline-flex items-center gap-1 rounded-sm border px-2 py-0.5 text-xs font-medium`. Add these variants to `components/ui/badge.tsx`:

```ts
default:     "border-transparent bg-primary text-primary-foreground",
secondary:   "border-transparent bg-secondary text-secondary-foreground",
outline:     "text-foreground",
destructive: "border-transparent bg-destructive text-destructive-foreground",
// soft status: 12% fill / 30% border
"destructive-soft": "bg-destructive/12 text-destructive border-destructive/30",
success:     "bg-success/12 text-success border-success/30",
info:        "bg-info/12 text-info border-info/30",
// warning: 20% fill / 50% border, dark text in light mode
warning:     "bg-warning/20 text-warning-foreground border-warning/50 dark:text-warning",
```

Status badges may lead with a `size-1.5 rounded-full bg-current` dot. Use soft variants for status in tables and deltas, and solid ones only for counts or labels that need emphasis.

**Alert**: base `grid grid-cols-[16px_1fr] gap-x-3 gap-y-1 rounded-lg border px-4 py-3 text-sm`, icon `size-4 mt-0.5`, title `font-medium`, description `col-start-2 text-muted-foreground`.

```ts
default:     "bg-card",
destructive: "bg-card text-destructive border-destructive/35 *:data-[slot=alert-description]:text-destructive/90",
success:     "bg-success/8 border-success/30 [&>svg]:text-success *:data-[slot=alert-title]:text-success",
warning:     "bg-warning/12 border-warning/50 [&>svg]:text-warning-foreground dark:[&>svg]:text-warning",
info:        "bg-info/8 border-info/30 [&>svg]:text-info *:data-[slot=alert-title]:text-info",
```

**Input / Textarea / Select**: `h-9 rounded-md border border-input bg-transparent dark:bg-input/30 px-3 shadow-xs`, plus the focus and invalid states from §5. Put a `Label` above, and optionally a caption below (`text-xs text-muted-foreground`, or `text-destructive` for errors).

**Checkbox / Radio / Switch**: `primary` when checked. Checkbox is `size-4 rounded-[4px]`. Switch is `h-[1.15rem] w-8`, with an `input` track when off.

**Card**: `bg-card text-card-foreground border rounded-xl py-6 flex flex-col gap-6`, sections `px-6`. `CardTitle` is `font-semibold`, `CardDescription` is `text-sm text-muted-foreground`, and `CardFooter` aligns actions right (`justify-end gap-2`).

**Tabs**: `TabsList` is `bg-muted rounded-lg p-[3px]`. The active trigger is `bg-background shadow-sm text-foreground` (dark: `dark:bg-input/30 dark:border-input`) and inactive triggers are `text-muted-foreground`. Use tabs for 2 to 5 peer views.

**Table**: put it in a container with `rounded-xl border bg-card overflow-x-auto`. Headers are `h-10 text-muted-foreground font-medium`, rows are `h-10 border-b hover:bg-muted/50`, and numeric columns are `text-right font-mono tabular-nums`.

**Dialog / AlertDialog / Sheet**: `bg-popover rounded-xl border p-6 shadow-xl`, with the title at `text-lg font-semibold`. Actions go bottom-right as `outline` Cancel followed by the primary or `destructive` action.

**Popover / DropdownMenu / Select content**: `bg-popover rounded-md border p-1 shadow-lg`. Items are `h-8 rounded-sm px-2 gap-2`, highlighted with `bg-accent text-accent-foreground`. Destructive items use `text-destructive`. Shortcuts are `ml-auto text-xs text-muted-foreground tracking-widest`.

**Tooltip**: inverted, `bg-foreground text-background text-xs rounded-sm px-2.5 py-1.5`.

**Toast (Sonner)**: placed bottom-right, `bg-popover border rounded-lg shadow-lg`, with the leading icon in the status color.

**Avatar**: `rounded-full` at `size-6`, `size-8` or `size-10`. The fallback is initials in `bg-muted text-muted-foreground`, and the current user is shown as `bg-primary text-primary-foreground`. Stacks overlap with `-ml-2 ring-2 ring-card`.

**Progress / Slider**: the track is `bg-primary/20` and the fill is `bg-primary`. The slider thumb is `size-4 rounded-full border border-primary bg-background shadow-sm`.

**Sidebar**: uses the `sidebar-*` tokens. Items are `h-8 rounded-md px-2 gap-2 text-sm`, with `hover:bg-sidebar-accent` on hover. The active item gets `bg-sidebar-accent font-medium`, and the brand mark uses `bg-sidebar-primary`.

**Charts (shadcn/Recharts)**: series use `chart-1` through `chart-5` in order. Gridlines are `stroke-border`, axis ticks are `text-xs fill-muted-foreground`, and the tooltip follows the popover recipe.

---

## 7. Patterns

- **Page header:** an H1 with a one-line `text-muted-foreground` description on the left, and actions on the right (`outline`, then `default`).
- **Forms:** single column `max-w-xl` with `space-y-6` between fields. The primary action goes bottom-left on full pages and bottom-right in dialogs and cards.
- **Empty states:** centered. A lucide icon sits in a `size-12 rounded-full bg-muted` circle, followed by an H3, one sentence, and one `default` button.
- **Destructive confirm:** an AlertDialog that names the object in `font-medium text-foreground` and says it can't be undone. The `destructive` button goes on the right.
- **Stats:** a Card with an Overline label, the value in `text-3xl font-semibold tracking-tight tabular-nums`, a soft delta badge (`success` when up and good, `destructive-soft` when bad), and an optional sparkline in `chart-*`.

---

## 8. Motion

- Durations: 150ms for hover and press, 200ms for popovers and tabs, 300ms for dialogs and sheets.
- Easing: `ease-out` on enter, `ease-in` on exit. Use `tw-animate-css` (`animate-in fade-in-0 zoom-in-95`, with `slide-in-from-*` for sheets).
- Respect `prefers-reduced-motion` (`motion-reduce:transition-none`).

---

## 9. Iconography & imagery

- Use **lucide-react** only: stroke 2 (1.5 at 24px and up), `size-4` in controls, `size-5` in nav.
- Illustrations, if any, are flat terracotta and stone duotone.
- Photography should be warm, in natural light, with low saturation.

---

## 10. Voice

Use sentence case everywhere, including buttons, titles and menu items. Buttons are verbs ("Save changes", not "OK"). Keep copy short, plain and friendly, with no exclamation marks in UI chrome.
