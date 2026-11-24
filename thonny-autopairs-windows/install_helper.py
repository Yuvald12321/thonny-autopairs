"""
Copies autopairs.py into Thonny's plugin folder.

- Inside Thonny: open this file and press F5 (Run) with Thonny's default interpreter.
- As thonny-autopairs-setup.exe (built by .github/workflows/release.yml): finds Thonny's
  python.exe and asks it for the plugin folder, because that folder depends on Thonny's
  Python version, portable mode and THONNY_USER_DIR.
"""

import os
import shutil
import subprocess
import sys

FROZEN = getattr(sys, "frozen", False)
QUERY = (
    "import sys, thonny; "
    "sys.stdout.buffer.write(thonny.get_sys_path_directory_containg_plugins().encode('utf-8'))"
)


def source_file():
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    if not os.path.isfile(os.path.join(base, "thonnycontrib", "autopairs.py")):
        base = os.path.dirname(base)
    return os.path.join(base, "thonnycontrib", "autopairs.py")


def find_thonny_python():
    for var in ("LOCALAPPDATA", "ProgramFiles", "ProgramFiles(x86)"):
        root = os.environ.get(var)
        if root:
            subdir = ("Programs", "Thonny") if var == "LOCALAPPDATA" else ("Thonny",)
            candidate = os.path.join(root, *subdir, "python.exe")
            if os.path.isfile(candidate):
                return candidate

    print("Could not find the Thonny installation folder.")
    print("Paste the Thonny folder path and press Enter.")
    print("  (Find it by right-clicking the Thonny shortcut and selecting Open file location)")
    entered = input("Path: ").strip().strip('"')
    candidate = entered if os.path.isfile(entered) else os.path.join(entered, "python.exe")
    if not entered or not os.path.isfile(candidate):
        raise SystemExit("python.exe was not found in that folder. Installation cancelled.")
    return candidate


def plugins_dir():
    if not FROZEN:
        try:
            import thonny
            return thonny.get_sys_path_directory_containg_plugins()
        except ImportError:
            pass

    result = subprocess.run([find_thonny_python(), "-I", "-c", QUERY], capture_output=True)
    if result.returncode != 0 or not result.stdout:
        raise SystemExit("Could not determine Thonny's plugin folder.\n"
                         + result.stderr.decode("utf-8", "replace"))
    return result.stdout.decode("utf-8")


def main():
    target_dir = os.path.join(plugins_dir(), "thonnycontrib")
    os.makedirs(target_dir, exist_ok=True)
    shutil.copy2(source_file(), target_dir)
    print("Installation complete:", os.path.join(target_dir, "autopairs.py"))
    print("Close and reopen Thonny to activate the plugin.")


if __name__ == "__main__":
    if FROZEN:
        sys.stdout.reconfigure(errors="replace")
        sys.stderr.reconfigure(errors="replace")
    code = 0
    try:
        main()
    except SystemExit as e:
        if e.code not in (None, 0):
            print(e.code if isinstance(e.code, str) else "Installation failed.")
            code = 1
    except Exception as e:
        print("Installation failed:", e)
        code = 1
    if FROZEN:
        try:
            input("\nPress Enter to close the window.")
        except EOFError:
            pass
    sys.exit(code)
