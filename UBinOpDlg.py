"""Subclass of BinOpDlg, which is generated by wxFormBuilder."""

import copy

import cv2
import wx

import CL
import UCommon

# Implementing BinOpDlg
class UBinOpDlg( CL.BinOpDlg ):
	def __init__( self, parent ):
		CL.BinOpDlg.__init__( self, parent )

	# Handlers for BinOpDlg events.
	def OnCancel( self, event ):
		# TODO: Implement OnCancel
		self.EndModal(0)

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
		page = self.m_notebook2.GetSelection()
		if page == 0:  # 白黒反転
			if Flag:
				self.cv_image = self.cv_image.bitwise_not()
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
			else:
				ret_img = self.cv_image.bitwise_not()
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))

		elif page == 1:  # 白孤立点除去
			if Flag:
				self.cv_image = self.cv_image.solation_point_elimination_white()
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
			else:
				ret_img = self.cv_image.solation_point_elimination_white()
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))

		elif page == 2:  # 黒孤立点除去
			if Flag:
				self.cv_image = self.cv_image.solation_point_elimination_black()
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
			else:
				ret_img = self.cv_image.solation_point_elimination_black()
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))

		elif page == 3:  # 細線化
			mt = self.m_choice4.GetSelection()
			if mt == 0:
				type = cv2.ximgproc.THINNING_ZHANGSUEN
			else:
				type = cv2.ximgproc.THINNING_GUOHALL
			if Flag:
				self.cv_image = self.cv_image.thinning(type)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
			else:
				ret_img = self.cv_image.thinning(type)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))

		elif page == 4:  # モルフォロジー演算
			op_code = self.m_radioBox2.GetSelection()
			ksize   = self.m_spinCtrl441.GetValue()
			it      = self.m_spinCtrl371.GetValue()
			if op_code == 0:
				op = cv2.MORPH_ERODE
			elif op_code == 1:
				op = cv2.MORPH_DILATE
			elif op_code == 2:
				op = cv2.MORPH_OPEN
			elif op_code == 3:
				op = cv2.MORPH_CLOSE
			elif op_code == 4:
				op = cv2.MORPH_GRADIENT
			elif op_code == 5:
				op = cv2.MORPH_TOPHAT
			elif op_code == 6:
				op = cv2.MORPH_BLACKHAT
			if Flag:
				self.cv_image = self.cv_image.morphologyEx(op, ksize, it)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
			else:
				ret_img = self.cv_image.morphologyEx(op, ksize, it)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))
