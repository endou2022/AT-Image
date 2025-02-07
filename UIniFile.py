# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
SOFTNAME  = "UIniFile ver.1.0 : 初期設定クラス"
COPYRIGHT = "(C)Copyright 2022 Y.ENDOU All right reserved."
VER       = "1.0"
# ---------------------------------------------------------------------------
#	ver.1.0		2022/03/25	初期バージョン
# ---------------------------------------------------------------------------
# https://docs.python.org/ja/3/library/configparser.html (2022/04/13)
# https://rainbow-engine.com/python-configparser-howtouse/ (2022/04/13)
# -------------------------
import configparser

import wx

class UIniFile():
    """ini初期設定ファイル操作クラス
    """
# -------------------------
    def __init__(self, fname: str = None):
        """コンストラクタ
        @param string fname iniファイル名
        """
        self.config_ini = configparser.ConfigParser()
        self.config_ini.read(fname, encoding='utf-8')
        self.fname = fname
# -------------------------
    def read_integer(self, section:str, key:str) -> int:
        """値の読み込み
        @param string section セクション名
        @param string key キー
        @return セクション -> キー で指定された値
        """
        return(int(self.config_ini[section][key]))
# -------------------------
    def read_float(self, section, key) -> float:
        return(float(self.config_ini[section][key]))
# -------------------------
    def read_string(self, section, key) -> str:
        return(self.config_ini[section][key])
# -------------------------
    def SetPos(self, frame, section):
        """wx.Frameの位置を初期設定ファイルで設定する
        """
        y  = int(self.config_ini[section]['Top'])
        x = int(self.config_ini[section]['Left'])
        frame.SetPosition(wx.Point(x, y))
# -------------------------
    def SetPosSize(self, frame, section):
        """wx.Frameの位置と大きさを初期設定ファイルで設定する
        """
        y  = int(self.config_ini[section]['Top'])
        x = int(self.config_ini[section]['Left'])
        w  = int(self.config_ini[section]['Width'])
        h = int(self.config_ini[section]['Height'])
        frame.SetPosition(wx.Point(x, y))
        frame.SetSize(wx.Size(w, h))
# -------------------------
    def WritePos(self, frame, section):
        """wx.Frameの位置を記憶する
        """
        x, y = frame.GetPosition()
        self.write_val(section, 'Top'   , y)
        self.write_val(section, 'Left'  , x)
# -------------------------
    def WritePosSize(self, frame, section):
        """wx.Frameの位置と大きさを記憶する
        """
        x, y = frame.GetPosition()
        w, h = frame.GetSize()
        self.write_val(section, 'Top'   , y)
        self.write_val(section, 'Left'  , x)
        self.write_val(section, 'Width' , w)
        self.write_val(section, 'Height', h)
# -------------------------
    def write_val(self, section, key, val):
        """値の書き込み
        @param string section セクション名
        @param string key キー
        @param valiable val 書き込む値
        """
        if not self.config_ini.has_section(section):
            self.config_ini.add_section(section)
        self.config_ini[section][key] = str(val)
# -------------------------
    def write_ini_file(self):
        """ini出力
        """
        with open(self.fname, "w", encoding="utf-8") as configfile:
            self.config_ini.write(configfile)
# -------------------------
