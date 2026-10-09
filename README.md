# Ember — shadcn/ui design system

A warm, editorial design system for shadcn/ui + Tailwind CSS v4: stone neutrals, one terracotta accent, light and dark.

| Path | What |
|---|---|
| `design-system/DESIGN.md` | The spec — tokens, type, spacing, states, component recipes, patterns |
| `design-system/globals.css` | Drop-in `app/globals.css` for a shadcn project (needs `tw-animate-css`) |
| `design-system/showcase.html` | Full interactive specimen (open in a browser) |
| `design-system/previews/*.html` | Claude Design preview cards (`@dsCard` markers); add `?dark` for dark mode |
| `tools/build_cards.py` | Regenerates `previews/` from `showcase.html` |

## Use with Claude Design

Run `/design-sync` from this repo in Claude Code to sync it into a claude.ai/design design-system project, or upload the `design-system/` folder.

## Use in a shadcn project

```sh
npm i tw-animate-css
cp design-system/globals.css app/globals.css
```

## Regenerate preview cards

```sh
python3 tools/build_cards.py design-system
```
