# -*- coding: utf-8 -*-

#		AT-Image ver. 6 画像処理プログラム
#		(C)Copyright 1998-99,2003-08,10,11,2022,23 Y.Endou All rights reserved

#---------------------------------------------------------------------------
import wx
import wx.adv
from UMWin import UMWin

__soft_name__   = 'AT-Image'
__version__     = '6.1' # バージョン番号
__description__ = '画像処理クラス(UOpenCV)を試すために作成'
__copyright__   = '(C)Copyright 1998-99,2003-08,10,11,2022,23 Y.Endou All rights reserved'

if __name__ == '__main__':
    app = wx.App(False)
    frame = UMWin(None)
    frame.SetTitle(__soft_name__ + ' ' + __version__)

    bitmap = wx.Bitmap('splash.jpg')
    splash = wx.adv.SplashScreen(bitmap, wx.adv.SPLASH_CENTER_ON_SCREEN | wx.adv.SPLASH_TIMEOUT, 1500, None)
    splash.Show()

    frame.Show(True)
    app.MainLoop()
#---------------------------------------------------------------------------
