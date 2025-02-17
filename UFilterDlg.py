"""Subclass of FilterDlg, which is generated by wxFormBuilder."""

import numpy as np
import wx

import CL
import UCommon
from UOpenCV import UOpenCV

# Implementing FilterDlg
class UFilterDlg( CL.FilterDlg ):
	def __init__( self, parent ):
		CL.FilterDlg.__init__( self, parent )
		for i in range(0, 7):      # i行(yの値)
			for j in range(0, 7):  # j列(xの値)
				self.m_grid2.SetCellValue(i, j, '0')

	# Handlers for FilterDlg events.
	def OnCancel( self, event ):
		# TODO: Implement OnCancel
		self.EndModal(0)

	def OnFOpen( self, event ):
		# TODO: Implement OnFOpen
		fname = self.m_filePicker4.GetPath()
		if fname == '':
			wx.MessageBox('ファイルが指定されていません', 'エラー', wx.ICON_ERROR)
			return
		try:
			multiplier, divisor, k_mat, offset, name, description = UOpenCV.read_2Dfilter(fname)
		except Exception as e:
			wx.MessageBox(str(e), 'エラー', wx.ICON_ERROR)
			return
		if k_mat.shape[0] == 3:  # 7x7に拡張する
			k2    = np.insert(k_mat, 0, 0, axis=0)
			k2    = np.insert(k2   , 0, 0, axis=0)
			k2    = np.insert(k2   , 5, 0, axis=0)
			k2    = np.insert(k2   , 6, 0, axis=0)
			k2    = np.insert(k2   , 0, 0, axis=1)
			k2    = np.insert(k2   , 0, 0, axis=1)
			k2    = np.insert(k2   , 5, 0, axis=1)
			k_mat = np.insert(k2   , 6, 0, axis=1)
		elif k_mat.shape[0] == 5:
			k2    = np.insert(k_mat, 0, 0, axis=0)
			k2    = np.insert(k2   , 6, 0, axis=0)
			k2    = np.insert(k2   , 0, 0, axis=1)
			k_mat = np.insert(k2   , 6, 0, axis=1)
		for i in range(0, 7):      # i行(yの値)
			for j in range(0, 7):  # j列(xの値)
				self.m_grid2.SetCellValue(i, j, str(int(k_mat[i][j])))
		self.m_spinCtrl16.SetValue(multiplier)
		self.m_spinCtrl171.SetValue(divisor)
		self.m_spinCtrl181.SetValue(offset)

	def OnPreView( self, event ):
		# TODO: Implement OnPreView
		self.Execute(False)

	def OnExec( self, event ):
		# TODO: Implement OnExec
		self.Execute(True)
		self.EndModal(1)

	def Execute(self, Flag):
		"""処理実行
		"""
		page = self.m_notebook3.GetSelection()
		if page == 0:  # 単純平滑化
			ksize = self.m_spinCtrl7.GetValue()
			if Flag:
				self.cv_image = self.cv_image.blur(ksize)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
			else:
				ret_img = self.cv_image.blur(ksize)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))

		if page == 1:  # メディアンフィルタ
			ksize = self.m_spinCtrl71.GetValue()
			if Flag:
				self.cv_image = self.cv_image.medianBlur(ksize)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
			else:
				ret_img = self.cv_image.medianBlur(ksize)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))

		if page == 2:  # ガウシアンフィルタ
			ksize = self.m_spinCtrl72.GetValue()
			std   = self.m_spinCtrlDouble14.GetValue()
			if Flag:
				self.cv_image = self.cv_image.GaussianBlur(ksize, std)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
			else:
				ret_img = self.cv_image.GaussianBlur(ksize, std)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))

		if page == 3:  # アンシャープフィルタ
			ksize = self.m_spinCtrl721.GetValue()
			std   = self.m_spinCtrlDouble141.GetValue()
			mul   = self.m_spinCtrlDouble17.GetValue()
			if Flag:
				self.cv_image = self.cv_image.unsharp(ksize, std, mul)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
			else:
				ret_img = self.cv_image.unsharp(ksize, std, mul)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))

		if page == 4:  # バイラテラルフィルタ
			d = self.m_spinCtrl722.GetValue()
			sigmaColor = self.m_spinCtrlDouble142.GetValue()
			sigmaSpace = self.m_spinCtrlDouble19.GetValue()
			if Flag:
				self.cv_image = self.cv_image.bilateralFilter(d, sigmaColor, sigmaSpace)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
			else:
				ret_img = self.cv_image.bilateralFilter(d, sigmaColor, sigmaSpace)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))

		if page == 5:  # エッジプレザービング
			sigma_s = self.m_spinCtrlDouble1421.GetValue()
			sigma_r = self.m_spinCtrlDouble191.GetValue()
			if Flag:
				self.cv_image = self.cv_image.edgePreservingFilter(sigma_s=sigma_s, sigma_r=sigma_r)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
			else:
				ret_img = self.cv_image.edgePreservingFilter(sigma_s=sigma_s, sigma_r=sigma_r)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))

		if page == 6:  # 細部強調フィルタ
			sigma_s = self.m_spinCtrlDouble14211.GetValue()
			sigma_r = self.m_spinCtrlDouble1911.GetValue()
			if Flag:
				self.cv_image = self.cv_image.detailEnhance(sigma_s=sigma_s, sigma_r=sigma_r)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
			else:
				ret_img = self.cv_image.detailEnhance(sigma_s=sigma_s, sigma_r=sigma_r)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))

		if page == 7:  # ゾーベル
			dx = self.m_spinCtrl17.GetValue()
			dy = self.m_spinCtrl18.GetValue()
			if dx == 0 and dy == 0:
				wx.MessageBox('dx , dy の両方が 0 です', 'エラー', wx.ICON_ERROR)
				return
			ksize = self.m_spinCtrl73.GetValue()
			offset = self.m_spinCtrlDouble49.GetValue()
			if Flag:
				self.cv_image = self.cv_image.Sobel(dx, dy, ksize, offset)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
			else:
				ret_img = self.cv_image.Sobel(dx, dy, ksize, offset)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))

		if page == 8:  # ラプラシアン
			ksize  = self.m_spinCtrl74.GetValue()
			offset = self.m_spinCtrlDouble50.GetValue()
			if Flag:
				self.cv_image = self.cv_image.Laplacian(ksize, offset)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
			else:
				ret_img = self.cv_image.Laplacian(ksize, offset)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))

		if page == 9:  # 空間フィルタ
			mul = self.m_spinCtrl16.GetValue()
			div = self.m_spinCtrl171.GetValue()
			add = self.m_spinCtrl181.GetValue()
			mat = np.zeros((7, 7))
			for i in range(0, 7):      # i行(yの値)
				for j in range(0, 7):  # j列(xの値)
					mat[i][j] = float(self.m_grid2.GetCellValue(i, j))
			kernel = mul * mat / div
			if Flag:
				self.cv_image = self.cv_image.filter2D(kernel, add, '2Dfilter')
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
			else:
				ret_img = self.cv_image.filter2D(kernel, add, '2Dfilter')
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))
