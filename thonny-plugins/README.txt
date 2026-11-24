Thonny Convenience Plugin (Thonny 5, macOS)

Features
- Automatically close brackets ( [ { and quotes " ', skip closing characters, and delete empty pairs with Backspace
- Press Enter inside brackets to move the closing bracket to the next line
- Wrap selected text with brackets or quotes; typing """ three times creates """|"""
- Enable or disable under Tools > Options > Auto-pairs

Installation
1. Double-click install.command (if blocked: right-click > Open, or run bash install.command in Terminal)
2. Restart Thonny

Manual Installation
  Copy autopairs.py from the thonnycontrib folder to the folder below (create it if necessary)
  ~/Library/Thonny/plugins/lib/python/site-packages/thonnycontrib/

Uninstallation
  Delete autopairs.py from the folder above and restart Thonny
