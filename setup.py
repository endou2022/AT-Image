# -*- coding: utf-8 -*-


# https://genchan.net/it/programming/python/10325/  (2022/05/18)
# https://tomomai.com/python_cx_freeze/  (2022/05/18)
# cx_Freeze 用セットアップファイル

# 仮想環境で必要なライブラリ
# pip install cx_Freeze
# pip install opencv-python
# pip install opencv-contrib-python
# pip install wxPython==4.1.1    wxPythonはver.4.1.1でないとMDIのときウインドウメニューが英語になる
# pip install matplotlib

# python setup.py build

import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'
# Winデスクトップ出ない場合「CUI」の場合はif文をコメントアウト

exe = Executable(script = "ATImage.py",       # exe化したいPythonファイル名をscript = ' ' の中に記載します。
                 base= base, icon='icons/sakura.ico')  # アイコンを付けたい場合は、icon = ' ' の中に記載します。

setup(name = 'ATImage',               # name = ' ' の中にexe化した際のソフト名を記載します。
    version = '6.1',                  # version を設定したい場合は、version = ' ' の中に数字を記載します。
    description = '画像処理ソフト',   # description = ' ' の中にソフトの説明を記載します。
    executables = [exe])
