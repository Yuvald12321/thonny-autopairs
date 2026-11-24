# Thonny Bracket and Quote Auto-pairing Plugin

This is an auto-pairing plugin for Thonny 5. Installation varies by operating system.

## Features

- Automatically closes brackets `( [ {` and quotes `" '`.
- Skips over closing characters when typed.
- Pressing Backspace inside an empty pair deletes both characters.
- Pressing Enter inside brackets moves the closing bracket to the next line.
- Entering a bracket or quote around selected text wraps the selection.
- Typing `"""` three times creates a `"""|"""` pair.
- Enable or disable it under Tools > Options > Auto-pairs.

## Repository Layout

| Folder | Target | Installer |
| --- | --- | --- |
| `thonny-autopairs-windows/` | Windows | `thonny-autopairs-setup.exe` from [Releases](https://github.com/Yuvald12321/thonny-autopairs/releases/latest), or `install_helper.py` |
| `thonny-plugins/` | macOS | `install.command` |

The canonical package is at `thonnycontrib/autopairs.py`. The files under the platform folders are legacy convenience distributions and remain available for manual installation.

## Package Installation

Install the package through Thonny's package manager or pip:

```shell
pip install thonny-autopairs
```

After installation, restart Thonny. The package provides the `thonnycontrib.autopairs` plugin and automatically discovers `load_plugin()`.

## Windows Installation

1. Download `thonny-autopairs-setup.exe` from [Releases](https://github.com/Yuvald12321/thonny-autopairs/releases/latest) and double-click it.
   Because the program is unsigned, Windows protected your PC might appear. Click More info > Run anyway.
2. When you see the installation complete message, close and reopen Thonny.

If the installer cannot find the Thonny installation folder, it asks you to enter the Thonny folder path. To find it, right-click the Thonny shortcut and select Open file location.

If the EXE cannot run in your environment, open `thonny-autopairs-windows/install_helper.py` in Thonny and press Run (F5). Otherwise, use manual installation.

## macOS Installation

1. Double-click `install.command` in the `thonny-plugins/` folder. If it is blocked, right-click and select Open, or run `bash install.command` in Terminal.
2. Restart Thonny.

## Manual Installation

- Windows: In Thonny, select Tools > Open Thonny data folder..., then copy `autopairs.py` into `plugins\Python3XX\site-packages\thonnycontrib\`. `Python3XX` is the Python version bundled with Thonny (for example, `Python313`).
- macOS: Copy `autopairs.py` into `~/Library/Thonny/plugins/lib/python/site-packages/thonnycontrib/`.

## Uninstallation

Delete `autopairs.py` from the installed `thonnycontrib` folder, then restart Thonny.

## License

MIT License. See [LICENSE](LICENSE) for details.
