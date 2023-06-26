# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['sudoku_GUI.py'],
             pathex=['/Users/benjamin/Documents/python/PyQt/Sudoku'],
             binaries=[],
             datas=[('Sudoku.icns', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='sudoku_GUI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=True,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.datas,
               strip=True,
               upx=True,
               name='sudoku_GUI')

import sys
if sys.platform.startswith('darwin'):
   app = BUNDLE(coll,
                name='Sudoku.app', 
                #For Retina Display
                info_plist={'NSHighResolutionCapable': 'True'},
                icon='Sudoku.icns'
               )

# Note Run 'codesign --remove-signature Python' on Python file in App
