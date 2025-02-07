# -*- coding: utf-8 -*-

# ドラッグ＆ドロップクラス
# https://python-minutes.blogspot.com/2017/01/pythongui_89.html (2022/04/12)

import wx

# -------------------------
class UFileDropTarget(wx.FileDropTarget):
	def __init__(self, window):
		wx.FileDropTarget.__init__(self)
		self.window = window

	def OnDropFiles(self, x, y, filenames):
		for file in filenames:
			self.window.OnDrop(file)
		return True
# -------------------------
