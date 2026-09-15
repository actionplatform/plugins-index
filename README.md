# plugins-index

The official index of [Action Platform](https://github.com/actionplatform/action-platform) plugins: one `plugins/<slug>.json` per plugin, served from this repository's raw files. `action-platform plugin search <slug>` and `plugin install <slug>` read it; any other index can be added with `plugin index add <url>`.

## Add a plugin

Open a pull request with `plugins/<slug>.json`:

```json
{
  "name": "slug",
  "description": "One line",
  "author": "you",
  "verified": false,
  "repo": "https://github.com/you/apx-slug",
  "pypi": "apx-slug",
  "latest": "1.0.0",
  "min_core": "0.16",
  "needs": ["net: api.example.com", "env: EXAMPLE_TOKEN"],
  "tags": ["notification"]
}
```

- `pypi` must start with `apx-` (Action Platform extension); the slug must not collide with a core tool or a reserved word (`core platform official admin system test internal`).
- `needs` lists every host the plugin talks to and every environment variable it reads; the CLI shows it before installing.
- `verified` is set by a reviewer after reading the code: no side effects at import, no monkey-patching of `action_platform.*`, `needs` complete. Leave it `false` in the pull request.
- A new version is a pull request bumping `latest`.

Rules for plugin authors: [writing a plugin](https://github.com/actionplatform/action-platform/blob/master/docs/contribute_plugins.md).
