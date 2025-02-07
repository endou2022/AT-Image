# -*- coding: UTF-8 -*-

# 共通ルーチン
#

import math

import cv2
import wx

# showHistルーチンでmatplotlibを使うが、matplotlibのバックエンドを標準のTkAggからWXAggに変えておかないとハングアップする
import matplotlib
matplotlib.use('WXAgg')  # https://code-examples.net/ja/q/3220c9 (2022/05/18)
from matplotlib import pyplot as plt

from UOpenCV import UOpenCV
# -------------------------
def uopencv2wxbitmap(cv_image: UOpenCV, mag: float) -> wx.Bitmap:
    """UOpenCVをwxStaticBitmapの形式に変換する
    @param UOpenCV : cv_image 表示するデータ
	@param float : mag 表示倍率
    @return wx.Bitmap
    @link https://amdkkj.blogspot.com/2017/06/converting-opencv-python-images-into-wxpython-images_17.html (2022/01/14)
    """
    if(mag != 1.0):
        cv_image2 = cv_image.resize(mag, mag)
        height = cv_image2.height
        width  = cv_image2.width
        rgb = cv2.cvtColor(cv_image2.bitmap, cv2.COLOR_BGR2RGB)
    else:
        height = cv_image.height
        width  = cv_image.width
        rgb = cv2.cvtColor(cv_image.bitmap, cv2.COLOR_BGR2RGB)
    return wx.Bitmap.FromBuffer(width, height, rgb)
# -------------------------
def CopyToClipboard(cv_image: UOpenCV):
    """選択されている画像をクリップボードにコピーする
    @param UOpenCV : cv_image コピーする画像データ
    @link https://pashango-p.hatenadiary.org/entry/20110609/1307630616 (2022/01/25)
    """
    clip = wx.Clipboard()
    clip.Open()
    img = uopencv2wxbitmap(cv_image, 1.0)
    do = wx.BitmapDataObject()
    do.SetBitmap(img)
    clip.SetData(do)
    clip.Flush()
    clip.Close()
# -------------------------
def EnumChildWindow(parent):
    """子ウインドウを列挙する
    wxWidgetsにはない？
    @return list WindowID : ウインドウのIDリスト
    @return list WindowTitle :  ウインドウのタイトルリスト
    """
    children = parent.GetChildren()
    WindowID = list()
    WindowTitle = list()
    for child in children:
        if isinstance(child,wx.MDIChildFrame):    # GetChildren()は、子ウインドウでないものも検出する
            WindowID.append(child.GetId())        # wx.FindWindowById(id, parent=None) で利用
            WindowTitle.append(child.GetTitle())
    return WindowID , WindowTitle
# -------------------------
def SaveAs(win):
    """名前をつけて保存
    AT-Imageは処理前の画像を残すので、必ず別名で保存する
    """
    dialog = wx.FileDialog(None, "ファイルを選択", wildcard="画像ファイル(png)|*.png|画像ファイル,jpg)|*.jpg|画像ファイル(bmp)|*.bmp", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
        win.cv_image.imwrite(path)
    dialog.Destroy()
# -------------------------
def ZoomOut(win):
    """縮小表示
    @param win : 操作するウインドウ
    """
    win.magnification = win.magnification - 0.1
    if win.magnification < 0.1:
        win.magnification = 0.1
    wx_bitmap = uopencv2wxbitmap(win.cv_image,  win.magnification)
    win.m_bitmap1.SetBitmap(wx_bitmap)
# -------------------------
def ZoomIn(win):
    """拡大表示
    @param win : 操作するウインドウ
    """
    win.magnification = win.magnification + 0.1
    if win.magnification > 2.5:
        win.magnification = 2.5
    wx_bitmap = uopencv2wxbitmap(win.cv_image,  win.magnification)
    win.m_bitmap1.SetBitmap(wx_bitmap)
# -------------------------
def ZoomRst(win):
    """100%表示
    @param win : 操作するウインドウ
    """
    win.magnification = 1.0
    wx_bitmap = uopencv2wxbitmap(win.cv_image,  win.magnification)
    win.m_bitmap1.SetBitmap(wx_bitmap)
# -------------------------
def About():
    """このソフトについて
    """
    bitmap = wx.Bitmap('splash.jpg')
    splash = wx.adv.SplashScreen(bitmap, wx.adv.SPLASH_CENTER_ON_SCREEN | wx.adv.SPLASH_NO_TIMEOUT, 0, None, style=wx.DEFAULT_FRAME_STYLE)
    splash.SetTitle('このソフトについて')
    splash.Show()
# -------------------------
def showHist(cv_image):
    """ヒストグラムを描画する
    wxPythonを使っているので、UOpenCVのshowHist()とは別に用意した
    このファイルの先頭で matplotlib.use('WXAgg') とし、matplotlib のバックエンドを指定している
    """
    plt.figure('ヒストグラム')
    plt.clf()  # 描画域クリア
    plt.grid()
    if cv_image.kind == 'color':
        plt.plot(cv_image.dist_array[0], color='b')
        plt.plot(cv_image.dist_array[1], color='g')
        plt.plot(cv_image.dist_array[2], color='r')
    else:
        plt.plot(cv_image.dist_array[0], color='k')

    plt.show(block=False)  # このプログラムでは、matplotlib.use('WXAgg')でないとエラーが出る。
# -------------------------
def showDist(cv_image):
    """水平・垂直方向周辺分布を描画する
    """
    plt.figure('周辺分布')
    plt.clf()
    plt.grid()
    if cv_image.kind == 'color':
        plt.plot(cv_image.dist_array[3], cv_image.dist_array[0], color='b')
        plt.plot(cv_image.dist_array[3], cv_image.dist_array[1], color='g')
        plt.plot(cv_image.dist_array[3], cv_image.dist_array[2], color='r')
    else:
        plt.plot(cv_image.dist_array[1], cv_image.dist_array[0], color='k')

    plt.show(block=False)
# -------------------------
def showLine(cv_image):
    """線上のデータを描画する
    """
    plt.figure('線上のデータ')
    plt.clf()
    plt.grid()
    if cv_image.kind == 'color':
        plt.plot(cv_image.x_axis, cv_image.value_b, color='b')
        plt.plot(cv_image.x_axis, cv_image.value_g, color='g')
        plt.plot(cv_image.x_axis, cv_image.value_r, color='r')
    elif cv_image.kind == 'fft':
        fft = list()
        for i in range(len(cv_image.x_axis)):
            fft.append(math.sqrt(cv_image.value_b[i] * cv_image.value_b[i] + cv_image.value_g[i] * cv_image.value_g[i]))
        plt.plot(cv_image.x_axis, fft, color='k')
    else:
        plt.plot(cv_image.x_axis, cv_image.value_b, color='k')

    plt.show(block=False)
# -------------------------
