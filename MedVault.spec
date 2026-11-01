# PyInstaller spec: same build for Windows and Linux
import os

a = Analysis(['main.py'], hiddenimports=['babel.numbers'])

# Linux: use the system's fontconfig/freetype instead of the bundled (older) ones,
# otherwise fonts are picked differently from running with Python directly.
a.binaries = [b for b in a.binaries if not b[0].startswith(('libfontconfig', 'libfreetype'))]

pyz = PYZ(a.pure)
exe = EXE(
    pyz, a.scripts, a.binaries, a.datas, [],
    name=os.environ.get('APP_NAME', 'MedVault'),
    console=True,
    upx=False,
)
