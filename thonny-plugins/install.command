#!/bin/bash
# Install the Thonny plugin: bracket/quote auto-pairing (autopairs)
# Double-click in Finder or run `bash install.command` in Terminal.

cd "$(dirname "$0")" || exit 1

# Find Thonny.app
THONNY_APP=""
for candidate in "/Applications/Thonny.app" "$HOME/Applications/Thonny.app"; do
    if [ -d "$candidate" ]; then
        THONNY_APP="$candidate"
        break
    fi
done
if [ -z "$THONNY_APP" ]; then
    THONNY_APP="$(mdfind "kMDItemCFBundleIdentifier == 'org.thonny.Thonny'" 2>/dev/null | head -n 1)"
fi

# Ask Thonny for the plugin folder it uses
DEST=""
THONNY_PY="$THONNY_APP/Contents/Frameworks/Python.framework/Versions/Current/bin/python3"
if [ -n "$THONNY_APP" ] && [ -x "$THONNY_PY" ]; then
    DEST="$("$THONNY_PY" -I -c 'import thonny; print(thonny.get_sys_path_directory_containg_plugins())' 2>/dev/null)"
fi
if [ -z "$DEST" ]; then
    DEST="$HOME/Library/Thonny/plugins/lib/python/site-packages"
    echo "Thonny.app was not found; installing in the default location."
fi

mkdir -p "$DEST/thonnycontrib" || exit 1
cp ../thonnycontrib/autopairs.py "$DEST/thonnycontrib/" || exit 1

echo ""
echo "Installation complete: $DEST/thonnycontrib"
if pgrep -f "Thonny.app/Contents/Resources/thonnymain.py" > /dev/null; then
    echo "Thonny is running. Quit it with Cmd+Q, then reopen it to activate the plugin."
else
    echo "Open Thonny to activate the plugin."
fi
