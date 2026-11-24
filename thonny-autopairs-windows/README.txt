Thonny Bracket and Quote Auto-pairing Plugin (Windows, Thonny 5)

Features
- Automatically close brackets ( [ { and quotes " ', skip closing characters, and delete empty pairs with Backspace
- Press Enter inside brackets to move the closing bracket to the next line
- Wrap selected text with brackets or quotes; typing """ three times creates """|"""
- Enable or disable under Tools > Options > Auto-pairs

Installation
1. Download thonny-autopairs-setup.exe from https://github.com/Yuvald12321/thonny-autopairs/releases/latest and double-click it
   (if Windows protected your PC appears: click More info > Run anyway)
2. When you see "Installation complete," close and reopen Thonny

If the EXE is blocked
  Open install_helper.py in Thonny and press Run (F5).

Manual Installation
  1. In Thonny, select Tools > Open Thonny data folder... to open the Thonny folder.
  2. Copy autopairs.py into plugins\Python3XX\site-packages\thonnycontrib\
     (create the folder if necessary. Python3XX is the Python version bundled with Thonny, for example Python313)

Uninstallation
  Delete autopairs.py from the thonnycontrib folder above and restart Thonny
