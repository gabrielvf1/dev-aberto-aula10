# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['hello.py'],
<<<<<<< HEAD
             pathex=['/home/gabrielvf/Documents/Semestre7/Dev-Aberto/aula10Git/LALAL/dev-aberto-aula10/scripts'],
=======
             pathex=['/home/gabrielvf/Documents/Semestre7/Dev-Aberto/aula10Git/dev-aberto-aula10/scripts'],
>>>>>>> 65a3e6743e6a52d3fcf4d201b72c776d30091d40
             binaries=[],
             datas=[],
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
          name='hello',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='hello')
