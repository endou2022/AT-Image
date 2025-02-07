# -*- coding: utf-8 -*-

# wx.StaticBitmapにラバーバンドを表示するクラス
# ３つの関数が共通の変数を参照するのでクラスにした
# ---------------------------------------------------------------------------
#	ver.1.0		2022/03/25	初期バージョン
# ---------------------------------------------------------------------------
# https://www.programcreek.com/python/example/114457/wx.Overlay (2022/04/01)
# https://maku77.github.io/python/wxpython/drag-component.html (2022/04/01)
# -------------------------
import wx

class URubberBand():
	NoRubber  = 0
	Rectangle = 1
	Line      = 2
	NoFunc    = 0  # AT-Image独自
	HistArea  = 1
	DistHArea = 2
	DistVArea = 3
	DistLine  = 4
# -------------------------
	def __init__( self, static_bitmap ):
		self.wxoverlay = wx.Overlay()
		self.drag_flag = False                 # マウスをドラッグしているかどうか
		self.draw_type = URubberBand.NoRubber  # ラバーバンドの種類　クラス内からのアクセスでもクラス名をつけないといけないとは！
		self.static_bitmap = static_bitmap
		self.func_type = URubberBand.NoFunc    # AT-Image独自
# -------------------------
	def OnMLDown( self, event ):
		self.wxoverlay.Reset()  # 副作用なさそう
		self.drag_flag = True
		self.begin_pos = event.GetPosition()
		# CaptureMouse()を呼び出してキャプチャー開始, ReleaseMouse()を呼び出してキャプチャー終了です。
		self.static_bitmap.CaptureMouse()  # すべてのマウス入力をこのウィンドウに向ける
# -------------------------
	def OnMLUp( self, event ):
		# 位置の確定
		self.end_pos = event.GetPosition()
		if self.draw_type == URubberBand.Line:
			self.AjustLinePos()
		if self.draw_type == URubberBand.Rectangle:
			self.AjustRectanglePos()

		self.static_bitmap.Refresh()  # https://uyamae.hatenadiary.org/entry/20090319/1237437401 (2022/04/02) # 画面を元に戻す
		if self.static_bitmap.HasCapture():
			self.static_bitmap.ReleaseMouse()
		self.drag_flag = False
		self.draw_type = URubberBand.NoRubber
# -------------------------
	def OnMMotion( self, event ):
		# https://www.programcreek.com/python/example/114457/wx.Overlay (2022/04/01)
		# Use an Overlay to draw a rubberband-like bounding box.
		# if event.Dragging() and event.LeftIsDown() and self.drag_flag:
		begin_pos = self.begin_pos
		cur_pos   = event.GetPosition()

		dc = wx.ClientDC(self.static_bitmap)
		odc = wx.DCOverlay(self.wxoverlay, dc)
		odc.Clear() # オーバレークリア

		color = wx.Colour('cyan')  # cyan or yellow or gold
		dc.SetPen(wx.Pen(color, 2))
		dc.SetBrush(wx.Brush(color, style=wx.BRUSHSTYLE_CROSSDIAG_HATCH))

		if self.draw_type == URubberBand.Rectangle:
			rect = wx.Rect(begin_pos, cur_pos)
			dc.DrawRectangle(rect)
		
		if self.draw_type == URubberBand.Line:
			dc.DrawLine(begin_pos, cur_pos)
# -------------------------
	def AjustLinePos(self):
		"""線分の始点と終点の座標を調整する
		もう少し簡単にならないだろうか
		"""
		rect = self.static_bitmap.GetRect()
		if rect.Contains(self.end_pos) == False:  # マウスが枠外にある場合
			bitmap = self.static_bitmap.GetBitmap()
			w = bitmap.GetWidth()
			h = bitmap.GetHeight()
			if self.begin_pos.x == self.end_pos.x:  # 鉛直線の場合
				if self.end_pos.y  < 0:
					self.end_pos.y = 0
				if self.end_pos.y  > h:
					self.end_pos.y = h
			elif self.begin_pos.y == self.end_pos.y:  # 水平線の場合
				if self.end_pos.x  < 0:
					self.end_pos.x = 0
				if self.end_pos.x  > w:
					self.end_pos.x = w
			else:  # 傾きを持つ線分の場合
				x0 = float(self.begin_pos.x)
				y0 = float(self.begin_pos.y)
				x1 = float(self.end_pos.x)
				y1 = float(self.end_pos.y)
				a = (y1 - y0) / (x1 - x0)    # 傾き  直線の式 y = a * (x - x0) + y0

				x = int((0 - y0) / a + x0)   # y=0の時のx
				p1 = wx.Point(x, 0)

				y = int(a * (w - x0) + y0)   # x=wの時のy
				p2 = wx.Point(w, y)

				x = int((h - y0) / a + x0)   # y=hの時のx
				p3 = wx.Point(x, h)

				y = int(a * -1.0 * x0 + y0)  # x=0の時のy
				p4 = wx.Point(0, y)

				rect.Inflate(1,1)  # 境界判定のため
				if self.begin_pos.x < self.end_pos.x:  # 終点が始点の右側にある場合
					if rect.Contains(p1) == True and p1.x > self.begin_pos.x:
						self.end_pos = p1
					if rect.Contains(p2) == True and p2.x > self.begin_pos.x:
						self.end_pos = p2
					if rect.Contains(p3) == True and p3.x > self.begin_pos.x:
						self.end_pos = p3
				else:
					if rect.Contains(p3) == True and p3.x < self.begin_pos.x:
						self.end_pos = p3
					if rect.Contains(p4) == True and p4.x < self.begin_pos.x:
						self.end_pos = p4
					if rect.Contains(p1) == True and p1.x < self.begin_pos.x:
						self.end_pos = p1
		if self.begin_pos.x > self.end_pos.x:
			self.begin_pos , self.end_pos = self.end_pos , self.begin_pos  # python の値交換方法
# -------------------------
	def AjustRectanglePos(self):
		"""矩形の始点と終点の座標を調整する
		"""
		left   = min(self.begin_pos.x , self.end_pos.x)
		top    = min(self.begin_pos.y , self.end_pos.y)
		right  = max(self.begin_pos.x , self.end_pos.x)
		bottom = max(self.begin_pos.y , self.end_pos.y)
		self.begin_pos = wx.Point(left,  top)
		self.end_pos   = wx.Point(right, bottom)

		rect = self.static_bitmap.GetRect()
		if rect.Contains(self.end_pos) == False:  # 終点がマウスが枠外にある場合
			bitmap = self.static_bitmap.GetBitmap()
			w = bitmap.GetWidth()
			h = bitmap.GetHeight()
			if self.end_pos.y  > h:
				self.end_pos.y = h
			if self.end_pos.x  > w:
				self.end_pos.x = w
		if rect.Contains(self.begin_pos) == False:  # 始点がマウスが枠外にある場合
			if self.begin_pos.y  < 0:
				self.begin_pos.y = 0
			if self.begin_pos.x  < 0:
				self.begin_pos.x = 0
# -------------------------
