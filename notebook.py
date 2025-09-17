import marimo

__generated_with = "0.15.5"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    from pathlib import Path
    return (mo,)


@app.cell
def _(mo):
    html_path = mo.notebook_dir() / "project.html"
    assert html_path.exists(), f"{html_path} does not exist"
    return (html_path,)


@app.cell
def _(html_path, mo):
    mo.iframe(html_path.read_text(encoding="utf-8"))
    return


if __name__ == "__main__":
    app.run()
