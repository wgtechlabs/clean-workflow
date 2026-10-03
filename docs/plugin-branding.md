# Plugin branding and verification

## Supported metadata

`.codex-plugin/plugin.json` supplies `interface.displayName: "Clean Workflow"`
and the following plugin-root-relative paths:

| Field | Asset |
| --- | --- |
| `interface.composerIcon` | `./assets/icon.svg` |
| `interface.logo` | `./assets/logo.svg` |
| `interface.logoDark` | `./assets/logo-dark.svg` |

The name was already present before this artwork change. Keep the plugin and
marketplace identifiers `clean-workflow` unchanged. They remain valid in CLI
output, installation selectors, and skill namespaces; their presence there is
not evidence of a broken product display name.

The installed host inspected on 2026-10-03 was Codex **26.930.21537**, build
**12776**, with bundled runtime **0.159.0-alpha.12.1**. Its listing and detail
code use the presentation name with a technical-name fallback and support the
three fields above. Its composer has one icon field, so the tiled icon has its
own contrasting background. Separate dark composer artwork is not relied on.

The [manifest requirements](https://developers.openai.com/plugins/deploy/submission)
and [plugin packaging guidance](https://developers.openai.com/plugins/build/plugins)
describe supported assets and compatibility manifests. No second root manifest
or identifier migration is needed for this change.

## Verification boundaries

On 2026-10-03, supported CLI installation passed in a temporary local
marketplace: stable v1.1.1 baseline, update to the candidate with the same name
and version, then a clean fresh candidate installation. Both candidate stages
returned **Clean Workflow**, resolved all three image fields, and contained
asset bytes identical to the source. All three skill names and bundled
skill/reference contents were unchanged. Cleanup restored the original parsed
configuration and marketplace list and left the production plugin cache
unchanged.

For that local marketplace, host metadata resolved image paths to the source
snapshot; installed-cache files were checked separately. This verifies local
marketplace installation/update behavior, not every distribution channel.

SVG source validation and rendered size/contrast previews establish artwork
structure and appearance in those previews. Host `plugin/read` establishes the
parsed name and resolved image paths. Fresh and update installation tests must
also compare the installed files with these source assets. None of those checks
alone proves the actual desktop plugin surface rendered the image.

Actual installed-plugin screenshots remain **unverified**: the available
computer-use tool rejects access to the Codex app. No alternative capture route
was used to bypass that restriction. Issue #10's installed-UI acceptance remains
pending until the checks below can be completed through an allowed surface.

## Manual installed-UI check

After installing the candidate package through a temporary test marketplace:

1. Record the app version and capture the installed card and detail page. Confirm
   the product name is **Clean Workflow** and the custom symbol loads.
2. Inspect light and dark appearances, including the composer icon at its normal
   size. Confirm contrast and that the stepped passage remains distinguishable.
3. Repeat after updating a baseline installation with the candidate package.
4. Confirm existing `clean-workflow`, `clean-coding`, and `clean-code-review`
   invocations remain available; retain the technical identifiers where expected.
5. Record any surface that still shows the technical name, then remove only the
   temporary test installation and marketplace.

Do not report these screenshot checks as passed from manifest validation alone.
