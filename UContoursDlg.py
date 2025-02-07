"""Subclass of ContoursDlg, which is generated by wxFormBuilder."""

import copy

import cv2
import numpy as np
import wx

import CL
import UCommon

# Implementing ContoursDlg
class UContoursDlg( CL.ContoursDlg ):
	def __init__( self, parent ):
		CL.ContoursDlg.__init__( self, parent )

	# Handlers for ContoursDlg events.
	def OnCancel( self, event ):
		# TODO: Implement OnCancel
		self.EndModal(0)

	def OnPreView( self, event ):
		# TODO: Implement OnPreView
		self.Execute(False)

	def OnExec( self, event ):
		# TODO: Implement OnExec
		ret = self.Execute(True)
		self.EndModal(ret + 1)  # 他のダイアローグと違って 1以外の数も返す

	def Execute(self, Flag):
		"""処理実行
		"""
		page = self.m_notebook8.GetSelection()
		if page   == 0:  # Canny  ２値画像を返す
			threshold1   = self.m_spinCtrl45.GetValue()
			threshold2   = self.m_spinCtrl46.GetValue()
			apertureSize = self.m_spinCtrl47.GetValue()
			if Flag:
				self.cv_image = self.cv_image.Canny(threshold1, threshold2, apertureSize)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
			else:
				ret_img = self.cv_image.Canny(threshold1, threshold2, apertureSize)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))
		elif page == 1:  # findContours  ２値画像しか処理しない
			if self.cv_image.kind != 'binary':
				wx.MessageBox('findContours は２値画像以外処理できません', 'エラー', wx.ICON_ERROR)
				return
			minsize      = self.m_spinCtrl49.GetValue()
			if Flag:
				self.cv_image = self.cv_image.findContours(minsize=minsize)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
			else:
				ret_img = self.cv_image.findContours(minsize=minsize)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))
		elif page == 2:  # モルフォロジー(GRADIENT)処理  同じ種類の画像を返す
			dilate_ksize = self.m_spinCtrl491.GetValue()
			dilate_it    = self.m_spinCtrl50.GetValue()
			erode_ksize  = self.m_spinCtrl51.GetValue()
			erode_it     = self.m_spinCtrl52.GetValue()

			if dilate_it == 0 and erode_it == 0:
				wx.MessageBox('膨張、縮小のどちらかは 1回以上にする必要があります', 'エラー', wx.ICON_ERROR)
				return

			if Flag:
				self.cv_image = self.cv_image.morphologyGradient(dilate_ksize, dilate_it, erode_ksize, erode_it)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
			else:
				ret_img = self.cv_image.morphologyGradient(dilate_ksize, dilate_it, erode_ksize, erode_it)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))
		return page  # ContoursDlgだけ特別
