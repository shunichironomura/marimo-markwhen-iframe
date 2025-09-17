# Reproduction repository for embedding a markwhen HTML inside a marimo notebook

## Prerequisites

- [`mw`](https://github.com/mark-when/mw), the markwhen CLI:
  - Version 1.2.4 was used.
- [`uv`](https://docs.astral.sh/uv/), a Python package and project manager
  - Version 0.8.17 was used.
  - [`marimo`](https://marimo.io/) will be installed using `uv`

## Enviroment

- OS: macOS Tahoe (Version 26.0)
- Architecture: arm64

## Reproduction steps

### Generating `project.html`

`project.html` is already included in this repository, so you can skip this step.

```bash
mw project.mw project.html
```

### Embed `project.html` inside a marimo notebook

Run the following command to start the `notebook.py`:

```bash
uvx marimo==0.15.5 edit notebook.py
```

This will open a marimo notebook in the browser.

In the last cell of the notebook, `project.html` is embedded into the notebook using the [`marimo.iframe`](https://docs.marimo.io/api/html/#marimo.iframe) function.
However, no event is rendered, only the timeline background.

Notice that the events _are_ rendered only for the brief moment.

![Image](https://github.com/user-attachments/assets/9a45e844-2aee-4d01-b1ab-46e9eba63a01)
