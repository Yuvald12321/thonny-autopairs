# Thonny Auto-pairs

An auto-pairing plugin for [Thonny](https://thonny.org/) 5 that adds brackets, quotes, and triple quotes as you type.

[![PyPI](https://img.shields.io/pypi/v/thonny-autopairs.svg)](https://pypi.org/project/thonny-autopairs/)
[![Python](https://img.shields.io/pypi/pyversions/thonny-autopairs.svg)](https://pypi.org/project/thonny-autopairs/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Features

- Auto-closes brackets: `( )`, `[ ]`, and `{ }`
- Auto-closes single and double quotes
- Skips over an existing closing bracket or quote
- Deletes both characters when Backspace is pressed inside an empty pair
- Moves the closing bracket to a new indented line when Enter is pressed inside a pair
- Wraps selected text with brackets or quotes
- Converts `""` or `''` to a triple-quoted pair
- Works in both the editor and Shell
- Configurable under **Tools > Options > Auto-pairs**

## Installation

### From PyPI

Install from Thonny's package manager or with pip:

```shell
pip install thonny-autopairs
```

Restart Thonny after installation.

### Windows installer

Download `thonny-autopairs-setup.exe` from the [latest GitHub release](https://github.com/Yuvald12321/thonny-autopairs/releases/latest).

1. Double-click the installer.
2. If Windows SmartScreen appears, select **More info > Run anyway**.
3. Close and reopen Thonny after installation completes.

The installer is unsigned. If it cannot run or cannot find Thonny, open `thonny-autopairs-windows/install_helper.py` in Thonny and press **Run (F5)**.

### macOS installer

1. Open `thonny-plugins/install.command`.
2. Double-click it in Finder, or run:

   ```shell
   bash install.command
   ```

3. Restart Thonny.

### Manual installation

Copy `thonnycontrib/autopairs.py` into the `thonnycontrib` directory inside Thonny's plugin folder.

**Windows**

In Thonny, open **Tools > Open Thonny data folder...**, then copy the file to:

```text
plugins\Python3XX\site-packages\thonnycontrib\
```

Replace `Python3XX` with the Python version bundled with Thonny, such as `Python313`.

**macOS**

Copy the file to:

```text
~/Library/Thonny/plugins/lib/python/site-packages/thonnycontrib/
```

## Configuration

Open **Tools > Options > Auto-pairs** to configure:

- Auto-close brackets
- Auto-close quotes
- Enable or disable auto-pairs in the Thonny Shell

## Uninstallation

Remove `autopairs.py` from Thonny's `thonnycontrib` plugin directory, then restart Thonny.

For a pip installation, remove the package with:

```shell
pip uninstall thonny-autopairs
```

## Development

Clone the repository and build the distributions locally:

```shell
python -m pip install --upgrade build twine
python -m build
python -m twine check dist/*
```

The package entry point is `thonnycontrib/autopairs.py`. It exports `load_plugin()`, which Thonny discovers when the plugin package is installed.

## Publishing

The `.github/workflows/publish-pypi.yml` workflow builds the source distribution and wheel, then publishes to PyPI using GitHub Trusted Publishing.

Publishing runs after a GitHub release is published or when the workflow is started manually.

The PyPI Trusted Publisher must match:

- Owner: `Yuvald12321`
- Repository: `thonny-autopairs`
- Workflow: `publish-pypi.yml`
- Environment: `pypi`

## License

This project is licensed under the [MIT License](LICENSE).
