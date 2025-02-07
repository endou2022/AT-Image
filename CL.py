# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MWin
###########################################################################

class MWin ( wx.MDIParentFrame ):

    def __init__( self, parent ):
        wx.MDIParentFrame.__init__ ( self, parent, id = wx.ID_ANY, title = u"AT-Image", pos = wx.DefaultPosition, size = wx.Size( 650,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"開く(&O)"+ u"\t" + u"CTRL+O", u"画像ファイルを開く", wx.ITEM_NORMAL )
        self.m_menuItem1.SetBitmap( wx.Bitmap( u"icons/01on_open.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu1.Append( self.m_menuItem1 )

        self.m_menu1.AppendSeparator()

        self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"終了(&X)"+ u"\t" + u"CRTL+Q", u"ソフトウエアを終了する", wx.ITEM_NORMAL )
        self.m_menuItem2.SetBitmap( wx.Bitmap( u"icons/15on_exit.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu1.Append( self.m_menuItem2 )

        self.m_menubar1.Append( self.m_menu1, u"ファイル(&F)" )

        self.m_menu2 = wx.Menu()
        self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"コピー(&C)"+ u"\t" + u"CTRL+C", u"画像をクリップボードに送る", wx.ITEM_NORMAL )
        self.m_menuItem3.SetBitmap( wx.Bitmap( u"icons/04on_copy.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu2.Append( self.m_menuItem3 )
        self.m_menuItem3.Enable( False )

        self.m_menuItem4 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"ペースト(&P)"+ u"\t" + u"CTRL+V", u"クリップボードから画像を得る", wx.ITEM_NORMAL )
        self.m_menuItem4.SetBitmap( wx.Bitmap( u"icons/on_paste.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu2.Append( self.m_menuItem4 )

        self.m_menubar1.Append( self.m_menu2, u"編集(&E)" )

        self.m_menu3 = wx.Menu()
        self.m_menuItem5 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"このソフトについて(&A)", u"ソフトウエアの説明を表示する", wx.ITEM_NORMAL )
        self.m_menuItem5.SetBitmap( wx.Bitmap( u"icons/14on_about.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu3.Append( self.m_menuItem5 )

        self.m_menubar1.Append( self.m_menu3, u"ヘルプ(&H)" )

        self.SetMenuBar( self.m_menubar1 )

        self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
        self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
        self.m_tool1 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/01on_open.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"開く", u"画像ファイルを開く", None )

        self.m_tool2 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/02on_save.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"保存", u"画像をファイルに保存する", None )

        self.m_toolBar1.AddSeparator()

        self.m_tool3 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/03on_fclose.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"閉じる", u"画像ウインドウを閉じる", None )

        self.m_toolBar1.AddSeparator()

        self.m_tool4 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/04on_copy.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"コピー", u"画像をクリップボードに送る", None )

        self.m_tool21 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/on_paste.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"ペースト", u"クリップボードから画像を得る", None )

        self.m_toolBar1.AddSeparator()

        self.m_tool6 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/06on_magnify.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"拡大", u"画像を10%ずつ拡大する", None )

        self.m_tool5 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/05on_reduse.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"縮小", u"画像を10%ずつ縮小する", None )

        self.m_tool19 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/on_viewlog.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"履歴", u"処理履歴を表示する", None )

        self.m_toolBar1.AddSeparator()

        self.m_tool7 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/07on_gray.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"グレースケール化", u"カラー画像をグレースケール画像に変換する", None )

        self.m_tool18 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/07_2on_bin.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"２値化", u"グレースケール画像を２値画像に変換する", None )

        self.m_tool20 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/on_bitwise.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"反転", u"色を反転する", None )

        self.m_toolBar1.AddSeparator()

        self.m_tool181 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/on_calc.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"画像間演算", u"画像同士で演算を行う", None )

        self.m_toolBar1.AddSeparator()

        self.m_tool8 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/08on_hist.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"ヒストグラム", u"ヒストグラムを求めて表示する", None )

        self.m_tool9 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/09on_dist_h.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"水平方向周辺分布", u"水平方向の周辺分布を求めて表示する", None )

        self.m_tool10 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/10on_dist_v.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"垂直方向周辺分布", u"垂直方向の周辺分布を求めて表示する", None )

        self.m_tool11 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/11on_area.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"領域指定ヒストグラム", u"矩形領域を指定して、ヒストグラムを求めて表示する", None )

        self.m_tool12 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/12on_line.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"線上の分布", u"線分を指定して輝度分布を求め表示する", None )

        self.m_tool13 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/13on_get.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"データ表示", u"座標を指定して、近傍のピクセルの値を表示する", None )

        self.m_toolBar1.AddSeparator()

        self.m_tool14 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/14on_about.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"このソフト", u"ソフトウエアの情報を表示する", None )

        self.m_toolBar1.AddSeparator()

        self.m_tool15 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/15on_exit.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"終了", u"ソフトウエアを終了する", None )

        self.m_toolBar1.Realize()


        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnExit )
        self.Bind( wx.EVT_MENU, self.OnOpen, id = self.m_menuItem1.GetId() )
        self.Bind( wx.EVT_MENU, self.OnExit, id = self.m_menuItem2.GetId() )
        self.Bind( wx.EVT_MENU, self.OnCopy, id = self.m_menuItem3.GetId() )
        self.Bind( wx.EVT_MENU, self.OnPaste, id = self.m_menuItem4.GetId() )
        self.Bind( wx.EVT_MENU, self.OnAbout, id = self.m_menuItem5.GetId() )
        self.Bind( wx.EVT_TOOL, self.OnOpen, id = self.m_tool1.GetId() )
        self.Bind( wx.EVT_TOOL, self.OnSaveAs, id = self.m_tool2.GetId() )
        self.Bind( wx.EVT_TOOL, self.OnWClose, id = self.m_tool3.GetId() )
        self.Bind( wx.EVT_TOOL, self.OnCopy, id = self.m_tool4.GetId() )
        self.Bind( wx.EVT_TOOL, self.OnPaste, id = self.m_tool21.GetId() )
        self.Bind( wx.EVT_TOOL, self.OnZoomIn, id = self.m_tool6.GetId() )
        self.Bind( wx.EVT_TOOL, self.OnZoomOut, id = self.m_tool5.GetId() )
        self.Bind( wx.EVT_TOOL, self.OnViewLog, id = self.m_tool19.GetId() )
        self.Bind( wx.EVT_TOOL, self.OnGray, id = self.m_tool7.GetId() )
        self.Bind( wx.EVT_TOOL, self.OnBinary, id = self.m_tool18.GetId() )
        self.Bind( wx.EVT_TOOL, self.OnBitwise, id = self.m_tool20.GetId() )
        self.Bind( wx.EVT_TOOL, self.OnOp, id = self.m_tool181.GetId() )
        self.Bind( wx.EVT_TOOL, self.OnHist, id = self.m_tool8.GetId() )
        self.Bind( wx.EVT_TOOL, self.OnDistH, id = self.m_tool9.GetId() )
        self.Bind( wx.EVT_TOOL, self.OnDistV, id = self.m_tool10.GetId() )
        self.Bind( wx.EVT_TOOL, self.OnHistArea, id = self.m_tool11.GetId() )
        self.Bind( wx.EVT_TOOL, self.OnLine, id = self.m_tool12.GetId() )
        self.Bind( wx.EVT_TOOL, self.OnPixcel, id = self.m_tool13.GetId() )
        self.Bind( wx.EVT_TOOL, self.OnAbout, id = self.m_tool14.GetId() )
        self.Bind( wx.EVT_TOOL, self.OnExit, id = self.m_tool15.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnExit( self, event ):
        event.Skip()

    def OnOpen( self, event ):
        event.Skip()


    def OnCopy( self, event ):
        event.Skip()

    def OnPaste( self, event ):
        event.Skip()

    def OnAbout( self, event ):
        event.Skip()


    def OnSaveAs( self, event ):
        event.Skip()

    def OnWClose( self, event ):
        event.Skip()



    def OnZoomIn( self, event ):
        event.Skip()

    def OnZoomOut( self, event ):
        event.Skip()

    def OnViewLog( self, event ):
        event.Skip()

    def OnGray( self, event ):
        event.Skip()

    def OnBinary( self, event ):
        event.Skip()

    def OnBitwise( self, event ):
        event.Skip()

    def OnOp( self, event ):
        event.Skip()

    def OnHist( self, event ):
        event.Skip()

    def OnDistH( self, event ):
        event.Skip()

    def OnDistV( self, event ):
        event.Skip()

    def OnHistArea( self, event ):
        event.Skip()

    def OnLine( self, event ):
        event.Skip()

    def OnPixcel( self, event ):
        event.Skip()




###########################################################################
## Class CWin
###########################################################################

class CWin ( wx.MDIChildFrame ):

    def __init__( self, parent ):
        wx.MDIChildFrame.__init__ ( self, parent, id = wx.ID_ANY, title = u"カラー画像", pos = wx.DefaultPosition, size = wx.Size( 600,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar2 = wx.MenuBar( 0 )
        self.m_menu4 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"開く(&O)"+ u"\t" + u"CTRL+O", u"画像ファイルを開く", wx.ITEM_NORMAL )
        self.m_menuItem1.SetBitmap( wx.Bitmap( u"icons/01on_open.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu4.Append( self.m_menuItem1 )

        self.m_menu4.AppendSeparator()

        self.m_menuItem8 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"別名保存(&S)"+ u"\t" + u"CTRL+S", u"名前をつけて画像をファイルに保存する", wx.ITEM_NORMAL )
        self.m_menuItem8.SetBitmap( wx.Bitmap( u"icons/02on_save.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu4.Append( self.m_menuItem8 )

        self.m_menu4.AppendSeparator()

        self.m_menuItem9 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"閉じる(&W)"+ u"\t" + u"CTRL+W", u"画像を閉じる", wx.ITEM_NORMAL )
        self.m_menuItem9.SetBitmap( wx.Bitmap( u"icons/03on_fclose.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu4.Append( self.m_menuItem9 )

        self.m_menu4.AppendSeparator()

        self.m_menuItem10 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"終了(&X)", u"ソフトウエアを終了する", wx.ITEM_NORMAL )
        self.m_menuItem10.SetBitmap( wx.Bitmap( u"icons/15on_exit.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu4.Append( self.m_menuItem10 )

        self.m_menubar2.Append( self.m_menu4, u"ファイル(&F)" )

        self.m_menu5 = wx.Menu()
        self.m_menuItem3 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"コピー(&C)"+ u"\t" + u"CTRL+C", u"画像をクリップボードに送る", wx.ITEM_NORMAL )
        self.m_menuItem3.SetBitmap( wx.Bitmap( u"icons/04on_copy.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu5.Append( self.m_menuItem3 )

        self.m_menuItem4 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"ペースト(&P)"+ u"\t" + u"CTRL+V", u"クリップボードから画像を得る", wx.ITEM_NORMAL )
        self.m_menuItem4.SetBitmap( wx.Bitmap( u"icons/on_paste.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu5.Append( self.m_menuItem4 )

        self.m_menubar2.Append( self.m_menu5, u"編集(&E)" )

        self.m_menu6 = wx.Menu()
        self.m_menuItem17 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"拡大(&I)"+ u"\t" + u"CTRL++", u"10%拡大表示する", wx.ITEM_NORMAL )
        self.m_menuItem17.SetBitmap( wx.Bitmap( u"icons/06on_magnify.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu6.Append( self.m_menuItem17 )

        self.m_menuItem18 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"縮小(&O)"+ u"\t" + u"CTRL+-", u"10%縮小表示する", wx.ITEM_NORMAL )
        self.m_menuItem18.SetBitmap( wx.Bitmap( u"icons/05on_reduse.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu6.Append( self.m_menuItem18 )

        self.m_menuItem19 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"表示倍率リセット(&R)", u"100%の大きさで表示する", wx.ITEM_NORMAL )
        self.m_menu6.Append( self.m_menuItem19 )

        self.m_menu6.AppendSeparator()

        self.m_menuItem20 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"処理履歴(&L)", u"画像処理の履歴を表示する", wx.ITEM_NORMAL )
        self.m_menuItem20.SetBitmap( wx.Bitmap( u"icons/on_viewlog.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu6.Append( self.m_menuItem20 )

        self.m_menubar2.Append( self.m_menu6, u"表示(&V)" )

        self.m_menu7 = wx.Menu()
        self.m_menuItem171 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"グレースケール変換(&R)", u"グレースケールの画像に変換する", wx.ITEM_NORMAL )
        self.m_menuItem171.SetBitmap( wx.Bitmap( u"icons/07on_gray.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu7.Append( self.m_menuItem171 )

        self.m_menuItem181 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"モノトーン変換(&M)", u"モノトーンの画像に変換する", wx.ITEM_NORMAL )
        self.m_menuItem181.SetBitmap( wx.Bitmap( u"icons/18OnMono.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu7.Append( self.m_menuItem181 )

        self.m_menuItem191 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"疑似カラー表示(&P)", u"疑似カラーで色づけする", wx.ITEM_NORMAL )
        self.m_menu7.Append( self.m_menuItem191 )

        self.m_menuItem201 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"色画像分離(&E)", u"R,G,B、H,S,V画像などに分離する", wx.ITEM_NORMAL )
        self.m_menuItem201.SetBitmap( wx.Bitmap( u"icons/on_extract.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu7.Append( self.m_menuItem201 )

        self.m_menubar2.Append( self.m_menu7, u"画像変換(&T)" )

        self.m_menu8 = wx.Menu()
        self.m_menuItem21 = wx.MenuItem( self.m_menu8, wx.ID_ANY, u"シェーディング補正(&S)", u"照明むらの補正をする", wx.ITEM_NORMAL )
        self.m_menuItem21.SetBitmap( wx.Bitmap( u"icons/on_shading.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu8.Append( self.m_menuItem21 )

        self.m_menuItem22 = wx.MenuItem( self.m_menu8, wx.ID_ANY, u"輝度ヒストグラム変換(&V)", u"輝度のみヒストグラムを操作する", wx.ITEM_NORMAL )
        self.m_menu8.Append( self.m_menuItem22 )

        self.m_menuItem23 = wx.MenuItem( self.m_menu8, wx.ID_ANY, u"画像フィルタ(&F)", u"平滑化、先鋭化等画像フィルタ処理を行う", wx.ITEM_NORMAL )
        self.m_menuItem23.SetBitmap( wx.Bitmap( u"icons/on_filter.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu8.Append( self.m_menuItem23 )

        self.m_menuItem24 = wx.MenuItem( self.m_menu8, wx.ID_ANY, u"輝度ルックアップテーブル(&L)", u"ルックアップテーブルによる輝度変換を行う", wx.ITEM_NORMAL )
        self.m_menuItem24.SetBitmap( wx.Bitmap( u"icons/on_lookup.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu8.Append( self.m_menuItem24 )

        self.m_menuItem26 = wx.MenuItem( self.m_menu8, wx.ID_ANY, u"モルフォロジー処理(&M)", u"画像形状を変化させる", wx.ITEM_NORMAL )
        self.m_menu8.Append( self.m_menuItem26 )

        self.m_menuItem121 = wx.MenuItem( self.m_menu8, wx.ID_ANY, u"輪郭化(&C)", u"Canny法で境界を作る", wx.ITEM_NORMAL )
        self.m_menu8.Append( self.m_menuItem121 )

        self.m_menuItem27 = wx.MenuItem( self.m_menu8, wx.ID_ANY, u"円・線分検出(&D)", u"画像にある白い部分の円、線分を検出する", wx.ITEM_NORMAL )
        self.m_menu8.Append( self.m_menuItem27 )

        self.m_menuItem28 = wx.MenuItem( self.m_menu8, wx.ID_ANY, u"アート効果(&A)", u"絵画調に変換する", wx.ITEM_NORMAL )
        self.m_menuItem28.SetBitmap( wx.Bitmap( u"icons/19OnArt.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu8.Append( self.m_menuItem28 )

        self.m_menubar2.Append( self.m_menu8, u"画像処理(&G)" )

        self.m_menu9 = wx.Menu()
        self.m_menuItem29 = wx.MenuItem( self.m_menu9, wx.ID_ANY, u"画像間演算(&M)", u"２つの画像で、算術、論理演算などを行う", wx.ITEM_NORMAL )
        self.m_menuItem29.SetBitmap( wx.Bitmap( u"icons/on_calc.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu9.Append( self.m_menuItem29 )

        self.m_menubar2.Append( self.m_menu9, u"画像間演算(&B)" )

        self.m_menu10 = wx.Menu()
        self.m_menuItem30 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"ヒストグラム(&H)", u"画像全体のヒストグラムを表示する", wx.ITEM_NORMAL )
        self.m_menuItem30.SetBitmap( wx.Bitmap( u"icons/08on_hist.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem30 )

        self.m_menuItem31 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"水平方向周辺分布", u"水平方向に周辺分布を集計する", wx.ITEM_NORMAL )
        self.m_menuItem31.SetBitmap( wx.Bitmap( u"icons/09on_dist_h.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem31 )

        self.m_menuItem32 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"垂直方向周辺分布", u"垂直方向に周辺分布を集計する", wx.ITEM_NORMAL )
        self.m_menuItem32.SetBitmap( wx.Bitmap( u"icons/10on_dist_v.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem32 )

        self.m_menu10.AppendSeparator()

        self.m_menuItem33 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"ヒストグラム（領域指定）", u"矩形領域を指定してヒストグラムを求め表示する", wx.ITEM_NORMAL )
        self.m_menuItem33.SetBitmap( wx.Bitmap( u"icons/11on_area.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem33 )

        self.m_menuItem34 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"水平方向周辺分布（領域指定）", u"矩形領域を指定して水平方向に周辺分布を集計する", wx.ITEM_NORMAL )
        self.m_menu10.Append( self.m_menuItem34 )

        self.m_menuItem35 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"垂直方向周辺分布（領域指定）", u"矩形領域を指定して垂直方向に周辺分布を集計する", wx.ITEM_NORMAL )
        self.m_menu10.Append( self.m_menuItem35 )

        self.m_menu10.AppendSeparator()

        self.m_menuItem36 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"線上の分布(&L)", u"線分を指定して輝度分布を求め表示する", wx.ITEM_NORMAL )
        self.m_menuItem36.SetBitmap( wx.Bitmap( u"icons/12on_line.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem36 )

        self.m_menuItem37 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"ピクセル値(&P)", u"座標を指定して、近傍のピクセルの値を表示する", wx.ITEM_NORMAL )
        self.m_menuItem37.SetBitmap( wx.Bitmap( u"icons/13on_get.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem37 )

        self.m_menubar2.Append( self.m_menu10, u"画像計測(&M)" )

        self.m_menu11 = wx.Menu()
        self.m_menuItem5 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"このソフトについて(&A)", u"ソフトウエアの説明を表示する", wx.ITEM_NORMAL )
        self.m_menuItem5.SetBitmap( wx.Bitmap( u"icons/14on_about.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu11.Append( self.m_menuItem5 )

        self.m_menubar2.Append( self.m_menu11, u"ヘルプ(&H)" )

        self.SetMenuBar( self.m_menubar2 )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow1.SetScrollRate( 5, 5 )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_bitmap1 = wx.StaticBitmap( self.m_scrolledWindow1, wx.ID_ANY, wx.NullBitmap, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        bSizer2.Add( self.m_bitmap1, 0, wx.ALL, 0 )


        self.m_scrolledWindow1.SetSizer( bSizer2 )
        self.m_scrolledWindow1.Layout()
        bSizer2.Fit( self.m_scrolledWindow1 )
        bSizer1.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 0 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MOVE_END, self.OnMvEnd )
        self.Bind( wx.EVT_MENU, self.OnOpen, id = self.m_menuItem1.GetId() )
        self.Bind( wx.EVT_MENU, self.OnSaveAs, id = self.m_menuItem8.GetId() )
        self.Bind( wx.EVT_MENU, self.OnWClose, id = self.m_menuItem9.GetId() )
        self.Bind( wx.EVT_MENU, self.OnExit, id = self.m_menuItem10.GetId() )
        self.Bind( wx.EVT_MENU, self.OnCopy, id = self.m_menuItem3.GetId() )
        self.Bind( wx.EVT_MENU, self.OnPaste, id = self.m_menuItem4.GetId() )
        self.Bind( wx.EVT_MENU, self.OnZoomIn, id = self.m_menuItem17.GetId() )
        self.Bind( wx.EVT_MENU, self.OnZoomOut, id = self.m_menuItem18.GetId() )
        self.Bind( wx.EVT_MENU, self.OnZoomRst, id = self.m_menuItem19.GetId() )
        self.Bind( wx.EVT_MENU, self.OnViewLog, id = self.m_menuItem20.GetId() )
        self.Bind( wx.EVT_MENU, self.OnGray, id = self.m_menuItem171.GetId() )
        self.Bind( wx.EVT_MENU, self.OnMono, id = self.m_menuItem181.GetId() )
        self.Bind( wx.EVT_MENU, self.OnPseud, id = self.m_menuItem191.GetId() )
        self.Bind( wx.EVT_MENU, self.OnCvtColor, id = self.m_menuItem201.GetId() )
        self.Bind( wx.EVT_MENU, self.OnShading, id = self.m_menuItem21.GetId() )
        self.Bind( wx.EVT_MENU, self.OnChHist, id = self.m_menuItem22.GetId() )
        self.Bind( wx.EVT_MENU, self.OnFilter, id = self.m_menuItem23.GetId() )
        self.Bind( wx.EVT_MENU, self.OnLookup, id = self.m_menuItem24.GetId() )
        self.Bind( wx.EVT_MENU, self.OnMorphology, id = self.m_menuItem26.GetId() )
        self.Bind( wx.EVT_MENU, self.OnContours, id = self.m_menuItem121.GetId() )
        self.Bind( wx.EVT_MENU, self.OnEdge, id = self.m_menuItem27.GetId() )
        self.Bind( wx.EVT_MENU, self.OnArt, id = self.m_menuItem28.GetId() )
        self.Bind( wx.EVT_MENU, self.OnOp, id = self.m_menuItem29.GetId() )
        self.Bind( wx.EVT_MENU, self.OnHist, id = self.m_menuItem30.GetId() )
        self.Bind( wx.EVT_MENU, self.OnDistH, id = self.m_menuItem31.GetId() )
        self.Bind( wx.EVT_MENU, self.OnDistV, id = self.m_menuItem32.GetId() )
        self.Bind( wx.EVT_MENU, self.OnHistArea, id = self.m_menuItem33.GetId() )
        self.Bind( wx.EVT_MENU, self.OnDistHArea, id = self.m_menuItem34.GetId() )
        self.Bind( wx.EVT_MENU, self.OnDistVArea, id = self.m_menuItem35.GetId() )
        self.Bind( wx.EVT_MENU, self.OnLine, id = self.m_menuItem36.GetId() )
        self.Bind( wx.EVT_MENU, self.OnPixcel, id = self.m_menuItem37.GetId() )
        self.Bind( wx.EVT_MENU, self.OnAbout, id = self.m_menuItem5.GetId() )
        self.m_bitmap1.Bind( wx.EVT_LEFT_DOWN, self.OnLDwn )
        self.m_bitmap1.Bind( wx.EVT_LEFT_UP, self.OnLUp )
        self.m_bitmap1.Bind( wx.EVT_MOTION, self.OnMove )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnMvEnd( self, event ):
        event.Skip()

    def OnOpen( self, event ):
        event.Skip()

    def OnSaveAs( self, event ):
        event.Skip()

    def OnWClose( self, event ):
        event.Skip()

    def OnExit( self, event ):
        event.Skip()

    def OnCopy( self, event ):
        event.Skip()

    def OnPaste( self, event ):
        event.Skip()

    def OnZoomIn( self, event ):
        event.Skip()

    def OnZoomOut( self, event ):
        event.Skip()

    def OnZoomRst( self, event ):
        event.Skip()

    def OnViewLog( self, event ):
        event.Skip()

    def OnGray( self, event ):
        event.Skip()

    def OnMono( self, event ):
        event.Skip()

    def OnPseud( self, event ):
        event.Skip()

    def OnCvtColor( self, event ):
        event.Skip()

    def OnShading( self, event ):
        event.Skip()

    def OnChHist( self, event ):
        event.Skip()

    def OnFilter( self, event ):
        event.Skip()

    def OnLookup( self, event ):
        event.Skip()

    def OnMorphology( self, event ):
        event.Skip()

    def OnContours( self, event ):
        event.Skip()

    def OnEdge( self, event ):
        event.Skip()

    def OnArt( self, event ):
        event.Skip()

    def OnOp( self, event ):
        event.Skip()

    def OnHist( self, event ):
        event.Skip()

    def OnDistH( self, event ):
        event.Skip()

    def OnDistV( self, event ):
        event.Skip()

    def OnHistArea( self, event ):
        event.Skip()

    def OnDistHArea( self, event ):
        event.Skip()

    def OnDistVArea( self, event ):
        event.Skip()

    def OnLine( self, event ):
        event.Skip()

    def OnPixcel( self, event ):
        event.Skip()

    def OnAbout( self, event ):
        event.Skip()

    def OnLDwn( self, event ):
        event.Skip()

    def OnLUp( self, event ):
        event.Skip()

    def OnMove( self, event ):
        event.Skip()


###########################################################################
## Class GWin
###########################################################################

class GWin ( wx.MDIChildFrame ):

    def __init__( self, parent ):
        wx.MDIChildFrame.__init__ ( self, parent, id = wx.ID_ANY, title = u"グレースケール画像", pos = wx.DefaultPosition, size = wx.Size( 600,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar2 = wx.MenuBar( 0 )
        self.m_menu4 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"開く(&O)"+ u"\t" + u"CTRL+O", u"画像ファイルを開く", wx.ITEM_NORMAL )
        self.m_menuItem1.SetBitmap( wx.Bitmap( u"icons/01on_open.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu4.Append( self.m_menuItem1 )

        self.m_menu4.AppendSeparator()

        self.m_menuItem8 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"別名保存(&S)"+ u"\t" + u"CTRL+S", u"名前をつけて画像をファイルに保存する", wx.ITEM_NORMAL )
        self.m_menuItem8.SetBitmap( wx.Bitmap( u"icons/02on_save.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu4.Append( self.m_menuItem8 )

        self.m_menu4.AppendSeparator()

        self.m_menuItem9 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"閉じる(&W)"+ u"\t" + u"CTRL+W", u"画像を閉じる", wx.ITEM_NORMAL )
        self.m_menuItem9.SetBitmap( wx.Bitmap( u"icons/03on_fclose.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu4.Append( self.m_menuItem9 )

        self.m_menu4.AppendSeparator()

        self.m_menuItem10 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"終了(&X)", u"ソフトウエアを終了する", wx.ITEM_NORMAL )
        self.m_menuItem10.SetBitmap( wx.Bitmap( u"icons/15on_exit.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu4.Append( self.m_menuItem10 )

        self.m_menubar2.Append( self.m_menu4, u"ファイル(&F)" )

        self.m_menu5 = wx.Menu()
        self.m_menuItem3 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"コピー(&C)"+ u"\t" + u"CTRL+C", u"画像をクリップボードに送る", wx.ITEM_NORMAL )
        self.m_menuItem3.SetBitmap( wx.Bitmap( u"icons/04on_copy.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu5.Append( self.m_menuItem3 )

        self.m_menuItem4 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"ペースト(&P)"+ u"\t" + u"CTRL+V", u"クリップボードから画像を得る", wx.ITEM_NORMAL )
        self.m_menuItem4.SetBitmap( wx.Bitmap( u"icons/on_paste.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu5.Append( self.m_menuItem4 )

        self.m_menubar2.Append( self.m_menu5, u"編集(&E)" )

        self.m_menu6 = wx.Menu()
        self.m_menuItem17 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"拡大(&I)"+ u"\t" + u"CTRL++", u"10%拡大表示する", wx.ITEM_NORMAL )
        self.m_menuItem17.SetBitmap( wx.Bitmap( u"icons/06on_magnify.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu6.Append( self.m_menuItem17 )

        self.m_menuItem18 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"縮小(&O)"+ u"\t" + u"CTRL+-", u"10%縮小表示する", wx.ITEM_NORMAL )
        self.m_menuItem18.SetBitmap( wx.Bitmap( u"icons/05on_reduse.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu6.Append( self.m_menuItem18 )

        self.m_menuItem19 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"表示倍率リセット(&R)", u"100%の大きさで表示する", wx.ITEM_NORMAL )
        self.m_menu6.Append( self.m_menuItem19 )

        self.m_menu6.AppendSeparator()

        self.m_menuItem20 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"処理履歴(&L)", u"画像処理の履歴を表示する", wx.ITEM_NORMAL )
        self.m_menuItem20.SetBitmap( wx.Bitmap( u"icons/on_viewlog.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu6.Append( self.m_menuItem20 )

        self.m_menubar2.Append( self.m_menu6, u"表示(&V)" )

        self.m_menu7 = wx.Menu()
        self.m_menuItem181 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"モノトーン変換(&M)", u"モノトーンの画像に変換する", wx.ITEM_NORMAL )
        self.m_menu7.Append( self.m_menuItem181 )

        self.m_menuItem191 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"疑似カラー表示(&P)", u"疑似カラーで色づけする", wx.ITEM_NORMAL )
        self.m_menu7.Append( self.m_menuItem191 )

        self.m_menu7.AppendSeparator()

        self.m_menuItem105 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"２値化(&B)", u"２値画像に変換する", wx.ITEM_NORMAL )
        self.m_menuItem105.SetBitmap( wx.Bitmap( u"icons/07_2on_bin.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu7.Append( self.m_menuItem105 )

        self.m_menu7.AppendSeparator()

        self.m_menuItem106 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"FFT処理(&F)", u"FFT変換する", wx.ITEM_NORMAL )
        self.m_menu7.Append( self.m_menuItem106 )

        self.m_menubar2.Append( self.m_menu7, u"画像変換(&T)" )

        self.m_menu8 = wx.Menu()
        self.m_menuItem22 = wx.MenuItem( self.m_menu8, wx.ID_ANY, u"ヒストグラム変換(&V)", u"ヒストグラムを操作する", wx.ITEM_NORMAL )
        self.m_menu8.Append( self.m_menuItem22 )

        self.m_menuItem23 = wx.MenuItem( self.m_menu8, wx.ID_ANY, u"画像フィルタ(&F)", u"平滑化、先鋭化等画像フィルタ処理を行う", wx.ITEM_NORMAL )
        self.m_menuItem23.SetBitmap( wx.Bitmap( u"icons/on_filter.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu8.Append( self.m_menuItem23 )

        self.m_menuItem24 = wx.MenuItem( self.m_menu8, wx.ID_ANY, u"ルックアップテーブル(&L)", u"ルックアップテーブルによる輝度変換を行う", wx.ITEM_NORMAL )
        self.m_menuItem24.SetBitmap( wx.Bitmap( u"icons/on_lookup.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu8.Append( self.m_menuItem24 )

        self.m_menuItem26 = wx.MenuItem( self.m_menu8, wx.ID_ANY, u"モルフォロジー処理(&M)", u"画像形状を変化させる", wx.ITEM_NORMAL )
        self.m_menu8.Append( self.m_menuItem26 )

        self.m_menuItem122 = wx.MenuItem( self.m_menu8, wx.ID_ANY, u"輪郭化(&C)", u"Canny法で境界を作る", wx.ITEM_NORMAL )
        self.m_menu8.Append( self.m_menuItem122 )

        self.m_menuItem27 = wx.MenuItem( self.m_menu8, wx.ID_ANY, u"円・線分検出(&D)", u"画像にある白い部分の円、線分を検出する", wx.ITEM_NORMAL )
        self.m_menu8.Append( self.m_menuItem27 )

        self.m_menuItem28 = wx.MenuItem( self.m_menu8, wx.ID_ANY, u"アート効果(&A)", u"絵画調に変換する", wx.ITEM_NORMAL )
        self.m_menuItem28.SetBitmap( wx.Bitmap( u"icons/19OnArt.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu8.Append( self.m_menuItem28 )

        self.m_menubar2.Append( self.m_menu8, u"画像処理(&G)" )

        self.m_menu9 = wx.Menu()
        self.m_menuItem29 = wx.MenuItem( self.m_menu9, wx.ID_ANY, u"画像間演算(&M)", u"２つの画像で、算術、論理演算などを行う", wx.ITEM_NORMAL )
        self.m_menuItem29.SetBitmap( wx.Bitmap( u"icons/on_calc.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu9.Append( self.m_menuItem29 )

        self.m_menubar2.Append( self.m_menu9, u"画像間演算(&B)" )

        self.m_menu10 = wx.Menu()
        self.m_menuItem30 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"ヒストグラム(&H)", u"画像全体のヒストグラムを表示する", wx.ITEM_NORMAL )
        self.m_menuItem30.SetBitmap( wx.Bitmap( u"icons/08on_hist.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem30 )

        self.m_menuItem31 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"水平方向周辺分布", u"水平方向に周辺分布を集計する", wx.ITEM_NORMAL )
        self.m_menuItem31.SetBitmap( wx.Bitmap( u"icons/09on_dist_h.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem31 )

        self.m_menuItem32 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"垂直方向周辺分布", u"垂直方向に周辺分布を集計する", wx.ITEM_NORMAL )
        self.m_menuItem32.SetBitmap( wx.Bitmap( u"icons/10on_dist_v.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem32 )

        self.m_menu10.AppendSeparator()

        self.m_menuItem33 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"ヒストグラム（領域指定）", u"矩形領域を指定してヒストグラムを求め表示する", wx.ITEM_NORMAL )
        self.m_menuItem33.SetBitmap( wx.Bitmap( u"icons/11on_area.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem33 )

        self.m_menuItem34 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"水平方向周辺分布（領域指定）", u"矩形領域を指定して水平方向に周辺分布を集計する", wx.ITEM_NORMAL )
        self.m_menu10.Append( self.m_menuItem34 )

        self.m_menuItem35 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"垂直方向周辺分布（領域指定）", u"矩形領域を指定して垂直方向に周辺分布を集計する", wx.ITEM_NORMAL )
        self.m_menu10.Append( self.m_menuItem35 )

        self.m_menu10.AppendSeparator()

        self.m_menuItem36 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"線上の分布(&L)", u"線分を指定して輝度分布を求め表示する", wx.ITEM_NORMAL )
        self.m_menuItem36.SetBitmap( wx.Bitmap( u"icons/12on_line.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem36 )

        self.m_menuItem37 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"ピクセル値(&P)", u"座標を指定して、近傍のピクセルの値を表示する", wx.ITEM_NORMAL )
        self.m_menuItem37.SetBitmap( wx.Bitmap( u"icons/13on_get.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem37 )

        self.m_menubar2.Append( self.m_menu10, u"画像計測(&M)" )

        self.m_menu11 = wx.Menu()
        self.m_menuItem5 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"このソフトについて(&A)", u"ソフトウエアの説明を表示する", wx.ITEM_NORMAL )
        self.m_menuItem5.SetBitmap( wx.Bitmap( u"icons/14on_about.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu11.Append( self.m_menuItem5 )

        self.m_menubar2.Append( self.m_menu11, u"ヘルプ(&H)" )

        self.SetMenuBar( self.m_menubar2 )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow1.SetScrollRate( 5, 5 )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_bitmap1 = wx.StaticBitmap( self.m_scrolledWindow1, wx.ID_ANY, wx.NullBitmap, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        bSizer2.Add( self.m_bitmap1, 0, wx.ALL, 0 )


        self.m_scrolledWindow1.SetSizer( bSizer2 )
        self.m_scrolledWindow1.Layout()
        bSizer2.Fit( self.m_scrolledWindow1 )
        bSizer1.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 0 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MOVE_END, self.OnMvEnd )
        self.Bind( wx.EVT_MENU, self.OnOpen, id = self.m_menuItem1.GetId() )
        self.Bind( wx.EVT_MENU, self.OnSaveAs, id = self.m_menuItem8.GetId() )
        self.Bind( wx.EVT_MENU, self.OnWClose, id = self.m_menuItem9.GetId() )
        self.Bind( wx.EVT_MENU, self.OnExit, id = self.m_menuItem10.GetId() )
        self.Bind( wx.EVT_MENU, self.OnCopy, id = self.m_menuItem3.GetId() )
        self.Bind( wx.EVT_MENU, self.OnPaste, id = self.m_menuItem4.GetId() )
        self.Bind( wx.EVT_MENU, self.OnZoomIn, id = self.m_menuItem17.GetId() )
        self.Bind( wx.EVT_MENU, self.OnZoomOut, id = self.m_menuItem18.GetId() )
        self.Bind( wx.EVT_MENU, self.OnZoomRst, id = self.m_menuItem19.GetId() )
        self.Bind( wx.EVT_MENU, self.OnViewLog, id = self.m_menuItem20.GetId() )
        self.Bind( wx.EVT_MENU, self.OnMono, id = self.m_menuItem181.GetId() )
        self.Bind( wx.EVT_MENU, self.OnPseud, id = self.m_menuItem191.GetId() )
        self.Bind( wx.EVT_MENU, self.OnBinary, id = self.m_menuItem105.GetId() )
        self.Bind( wx.EVT_MENU, self.OnFFT, id = self.m_menuItem106.GetId() )
        self.Bind( wx.EVT_MENU, self.OnChHist, id = self.m_menuItem22.GetId() )
        self.Bind( wx.EVT_MENU, self.OnFilter, id = self.m_menuItem23.GetId() )
        self.Bind( wx.EVT_MENU, self.OnLookup, id = self.m_menuItem24.GetId() )
        self.Bind( wx.EVT_MENU, self.OnMorphology, id = self.m_menuItem26.GetId() )
        self.Bind( wx.EVT_MENU, self.OnContours, id = self.m_menuItem122.GetId() )
        self.Bind( wx.EVT_MENU, self.OnEdge, id = self.m_menuItem27.GetId() )
        self.Bind( wx.EVT_MENU, self.OnArt, id = self.m_menuItem28.GetId() )
        self.Bind( wx.EVT_MENU, self.OnOp, id = self.m_menuItem29.GetId() )
        self.Bind( wx.EVT_MENU, self.OnHist, id = self.m_menuItem30.GetId() )
        self.Bind( wx.EVT_MENU, self.OnDistH, id = self.m_menuItem31.GetId() )
        self.Bind( wx.EVT_MENU, self.OnDistV, id = self.m_menuItem32.GetId() )
        self.Bind( wx.EVT_MENU, self.OnHistArea, id = self.m_menuItem33.GetId() )
        self.Bind( wx.EVT_MENU, self.OnDistHArea, id = self.m_menuItem34.GetId() )
        self.Bind( wx.EVT_MENU, self.OnDistVArea, id = self.m_menuItem35.GetId() )
        self.Bind( wx.EVT_MENU, self.OnLine, id = self.m_menuItem36.GetId() )
        self.Bind( wx.EVT_MENU, self.OnPixcel, id = self.m_menuItem37.GetId() )
        self.Bind( wx.EVT_MENU, self.OnAbout, id = self.m_menuItem5.GetId() )
        self.m_bitmap1.Bind( wx.EVT_LEFT_DOWN, self.OnLDwn )
        self.m_bitmap1.Bind( wx.EVT_LEFT_UP, self.OnLUp )
        self.m_bitmap1.Bind( wx.EVT_MOTION, self.OnMove )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnMvEnd( self, event ):
        event.Skip()

    def OnOpen( self, event ):
        event.Skip()

    def OnSaveAs( self, event ):
        event.Skip()

    def OnWClose( self, event ):
        event.Skip()

    def OnExit( self, event ):
        event.Skip()

    def OnCopy( self, event ):
        event.Skip()

    def OnPaste( self, event ):
        event.Skip()

    def OnZoomIn( self, event ):
        event.Skip()

    def OnZoomOut( self, event ):
        event.Skip()

    def OnZoomRst( self, event ):
        event.Skip()

    def OnViewLog( self, event ):
        event.Skip()

    def OnMono( self, event ):
        event.Skip()

    def OnPseud( self, event ):
        event.Skip()

    def OnBinary( self, event ):
        event.Skip()

    def OnFFT( self, event ):
        event.Skip()

    def OnChHist( self, event ):
        event.Skip()

    def OnFilter( self, event ):
        event.Skip()

    def OnLookup( self, event ):
        event.Skip()

    def OnMorphology( self, event ):
        event.Skip()

    def OnContours( self, event ):
        event.Skip()

    def OnEdge( self, event ):
        event.Skip()

    def OnArt( self, event ):
        event.Skip()

    def OnOp( self, event ):
        event.Skip()

    def OnHist( self, event ):
        event.Skip()

    def OnDistH( self, event ):
        event.Skip()

    def OnDistV( self, event ):
        event.Skip()

    def OnHistArea( self, event ):
        event.Skip()

    def OnDistHArea( self, event ):
        event.Skip()

    def OnDistVArea( self, event ):
        event.Skip()

    def OnLine( self, event ):
        event.Skip()

    def OnPixcel( self, event ):
        event.Skip()

    def OnAbout( self, event ):
        event.Skip()

    def OnLDwn( self, event ):
        event.Skip()

    def OnLUp( self, event ):
        event.Skip()

    def OnMove( self, event ):
        event.Skip()


###########################################################################
## Class BWin
###########################################################################

class BWin ( wx.MDIChildFrame ):

    def __init__( self, parent ):
        wx.MDIChildFrame.__init__ ( self, parent, id = wx.ID_ANY, title = u"２値画像", pos = wx.DefaultPosition, size = wx.Size( 600,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar2 = wx.MenuBar( 0 )
        self.m_menu4 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"開く(&O)"+ u"\t" + u"CTRL+O", u"画像ファイルを開く", wx.ITEM_NORMAL )
        self.m_menuItem1.SetBitmap( wx.Bitmap( u"icons/01on_open.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu4.Append( self.m_menuItem1 )

        self.m_menu4.AppendSeparator()

        self.m_menuItem8 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"別名保存(&S)"+ u"\t" + u"CTRL+S", u"名前をつけて画像をファイルに保存する", wx.ITEM_NORMAL )
        self.m_menuItem8.SetBitmap( wx.Bitmap( u"icons/02on_save.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu4.Append( self.m_menuItem8 )

        self.m_menu4.AppendSeparator()

        self.m_menuItem9 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"閉じる(&W)"+ u"\t" + u"CTRL+W", u"画像を閉じる", wx.ITEM_NORMAL )
        self.m_menuItem9.SetBitmap( wx.Bitmap( u"icons/03on_fclose.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu4.Append( self.m_menuItem9 )

        self.m_menu4.AppendSeparator()

        self.m_menuItem10 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"終了(&X)", u"ソフトウエアを終了する", wx.ITEM_NORMAL )
        self.m_menuItem10.SetBitmap( wx.Bitmap( u"icons/15on_exit.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu4.Append( self.m_menuItem10 )

        self.m_menubar2.Append( self.m_menu4, u"ファイル(&F)" )

        self.m_menu5 = wx.Menu()
        self.m_menuItem3 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"コピー(&C)"+ u"\t" + u"CTRL+C", u"画像をクリップボードに送る", wx.ITEM_NORMAL )
        self.m_menuItem3.SetBitmap( wx.Bitmap( u"icons/04on_copy.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu5.Append( self.m_menuItem3 )

        self.m_menuItem4 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"ペースト(&P)"+ u"\t" + u"CTRL+V", u"クリップボードから画像を得る", wx.ITEM_NORMAL )
        self.m_menuItem4.SetBitmap( wx.Bitmap( u"icons/on_paste.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu5.Append( self.m_menuItem4 )

        self.m_menubar2.Append( self.m_menu5, u"編集(&E)" )

        self.m_menu6 = wx.Menu()
        self.m_menuItem17 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"拡大(&I)"+ u"\t" + u"CTRL++", u"10%拡大表示する", wx.ITEM_NORMAL )
        self.m_menuItem17.SetBitmap( wx.Bitmap( u"icons/06on_magnify.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu6.Append( self.m_menuItem17 )

        self.m_menuItem18 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"縮小(&O)"+ u"\t" + u"CTRL+-", u"10%縮小表示する", wx.ITEM_NORMAL )
        self.m_menuItem18.SetBitmap( wx.Bitmap( u"icons/05on_reduse.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu6.Append( self.m_menuItem18 )

        self.m_menuItem19 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"表示倍率リセット(&R)", u"100%の大きさで表示する", wx.ITEM_NORMAL )
        self.m_menu6.Append( self.m_menuItem19 )

        self.m_menu6.AppendSeparator()

        self.m_menuItem20 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"処理履歴(&L)", u"画像処理の履歴を表示する", wx.ITEM_NORMAL )
        self.m_menuItem20.SetBitmap( wx.Bitmap( u"icons/on_viewlog.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu6.Append( self.m_menuItem20 )

        self.m_menubar2.Append( self.m_menu6, u"表示(&V)" )

        self.m_menu34 = wx.Menu()
        self.m_menuItem109 = wx.MenuItem( self.m_menu34, wx.ID_ANY, u"グレースケール変換(&R)", u"グレースケールの画像に変換する", wx.ITEM_NORMAL )
        self.m_menuItem109.SetBitmap( wx.Bitmap( u"icons/07on_gray.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu34.Append( self.m_menuItem109 )

        self.m_menubar2.Append( self.m_menu34, u"画像変換(&T)" )

        self.m_menu8 = wx.Menu()
        self.m_menuItem121 = wx.MenuItem( self.m_menu8, wx.ID_ANY, u"白黒反転", u"白黒反転する", wx.ITEM_NORMAL )
        self.m_menuItem121.SetBitmap( wx.Bitmap( u"icons/on_bitwise.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu8.Append( self.m_menuItem121 )

        self.m_menuItem1211 = wx.MenuItem( self.m_menu8, wx.ID_ANY, u"輪郭化(&C)", u"Canny法で境界を作る", wx.ITEM_NORMAL )
        self.m_menu8.Append( self.m_menuItem1211 )

        self.m_menuItem27 = wx.MenuItem( self.m_menu8, wx.ID_ANY, u"円・線分検出(&D)", u"画像にある白い部分の円、線分を検出する", wx.ITEM_NORMAL )
        self.m_menu8.Append( self.m_menuItem27 )

        self.m_menuItem174 = wx.MenuItem( self.m_menu8, wx.ID_ANY, u"２値画像処理", u"２値画像を操作する", wx.ITEM_NORMAL )
        self.m_menuItem174.SetBitmap( wx.Bitmap( u"icons/17OnBinOp.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu8.Append( self.m_menuItem174 )

        self.m_menubar2.Append( self.m_menu8, u"画像処理(&G)" )

        self.m_menu9 = wx.Menu()
        self.m_menuItem29 = wx.MenuItem( self.m_menu9, wx.ID_ANY, u"画像間演算(&M)", u"２つの画像で、算術、論理演算などを行う", wx.ITEM_NORMAL )
        self.m_menuItem29.SetBitmap( wx.Bitmap( u"icons/on_calc.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu9.Append( self.m_menuItem29 )

        self.m_menubar2.Append( self.m_menu9, u"画像間演算(&B)" )

        self.m_menu10 = wx.Menu()
        self.m_menuItem31 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"水平方向周辺分布", u"水平方向に周辺分布を集計する", wx.ITEM_NORMAL )
        self.m_menuItem31.SetBitmap( wx.Bitmap( u"icons/09on_dist_h.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem31 )

        self.m_menuItem32 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"垂直方向周辺分布", u"垂直方向に周辺分布を集計する", wx.ITEM_NORMAL )
        self.m_menuItem32.SetBitmap( wx.Bitmap( u"icons/10on_dist_v.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem32 )

        self.m_menu10.AppendSeparator()

        self.m_menuItem34 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"水平方向周辺分布（領域指定）", u"矩形領域を指定して水平方向に周辺分布を集計する", wx.ITEM_NORMAL )
        self.m_menu10.Append( self.m_menuItem34 )

        self.m_menuItem35 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"垂直方向周辺分布（領域指定）", u"矩形領域を指定して垂直方向に周辺分布を集計する", wx.ITEM_NORMAL )
        self.m_menu10.Append( self.m_menuItem35 )

        self.m_menu10.AppendSeparator()

        self.m_menuItem36 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"線上の分布(&L)", u"線分を指定して輝度分布を求め表示する", wx.ITEM_NORMAL )
        self.m_menuItem36.SetBitmap( wx.Bitmap( u"icons/12on_line.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem36 )

        self.m_menuItem37 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"ピクセル値(&P)", u"座標を指定して、近傍のピクセルの値を表示する", wx.ITEM_NORMAL )
        self.m_menuItem37.SetBitmap( wx.Bitmap( u"icons/13on_get.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem37 )

        self.m_menu10.AppendSeparator()

        self.m_menuItem173 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"ラベリング処理", u"黒い物体を抽出する", wx.ITEM_NORMAL )
        self.m_menu10.Append( self.m_menuItem173 )

        self.m_menubar2.Append( self.m_menu10, u"画像計測(&M)" )

        self.m_menu11 = wx.Menu()
        self.m_menuItem5 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"このソフトについて(&A)", u"ソフトウエアの説明を表示する", wx.ITEM_NORMAL )
        self.m_menuItem5.SetBitmap( wx.Bitmap( u"icons/14on_about.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu11.Append( self.m_menuItem5 )

        self.m_menubar2.Append( self.m_menu11, u"ヘルプ(&H)" )

        self.SetMenuBar( self.m_menubar2 )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow1.SetScrollRate( 5, 5 )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_bitmap1 = wx.StaticBitmap( self.m_scrolledWindow1, wx.ID_ANY, wx.NullBitmap, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        bSizer2.Add( self.m_bitmap1, 0, wx.ALL, 0 )


        self.m_scrolledWindow1.SetSizer( bSizer2 )
        self.m_scrolledWindow1.Layout()
        bSizer2.Fit( self.m_scrolledWindow1 )
        bSizer1.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 0 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MOVE_END, self.OnMvEnd )
        self.Bind( wx.EVT_MENU, self.OnOpen, id = self.m_menuItem1.GetId() )
        self.Bind( wx.EVT_MENU, self.OnSaveAs, id = self.m_menuItem8.GetId() )
        self.Bind( wx.EVT_MENU, self.OnWClose, id = self.m_menuItem9.GetId() )
        self.Bind( wx.EVT_MENU, self.OnExit, id = self.m_menuItem10.GetId() )
        self.Bind( wx.EVT_MENU, self.OnCopy, id = self.m_menuItem3.GetId() )
        self.Bind( wx.EVT_MENU, self.OnPaste, id = self.m_menuItem4.GetId() )
        self.Bind( wx.EVT_MENU, self.OnZoomIn, id = self.m_menuItem17.GetId() )
        self.Bind( wx.EVT_MENU, self.OnZoomOut, id = self.m_menuItem18.GetId() )
        self.Bind( wx.EVT_MENU, self.OnZoomRst, id = self.m_menuItem19.GetId() )
        self.Bind( wx.EVT_MENU, self.OnViewLog, id = self.m_menuItem20.GetId() )
        self.Bind( wx.EVT_MENU, self.OnGray, id = self.m_menuItem109.GetId() )
        self.Bind( wx.EVT_MENU, self.OnBitwise, id = self.m_menuItem121.GetId() )
        self.Bind( wx.EVT_MENU, self.OnContours, id = self.m_menuItem1211.GetId() )
        self.Bind( wx.EVT_MENU, self.OnEdge, id = self.m_menuItem27.GetId() )
        self.Bind( wx.EVT_MENU, self.OnBinOp, id = self.m_menuItem174.GetId() )
        self.Bind( wx.EVT_MENU, self.OnOp, id = self.m_menuItem29.GetId() )
        self.Bind( wx.EVT_MENU, self.OnDistH, id = self.m_menuItem31.GetId() )
        self.Bind( wx.EVT_MENU, self.OnDistV, id = self.m_menuItem32.GetId() )
        self.Bind( wx.EVT_MENU, self.OnDistHArea, id = self.m_menuItem34.GetId() )
        self.Bind( wx.EVT_MENU, self.OnDistVArea, id = self.m_menuItem35.GetId() )
        self.Bind( wx.EVT_MENU, self.OnLine, id = self.m_menuItem36.GetId() )
        self.Bind( wx.EVT_MENU, self.OnPixcel, id = self.m_menuItem37.GetId() )
        self.Bind( wx.EVT_MENU, self.OnLabel, id = self.m_menuItem173.GetId() )
        self.Bind( wx.EVT_MENU, self.OnAbout, id = self.m_menuItem5.GetId() )
        self.m_bitmap1.Bind( wx.EVT_LEFT_DOWN, self.OnLDwn )
        self.m_bitmap1.Bind( wx.EVT_LEFT_UP, self.OnLUp )
        self.m_bitmap1.Bind( wx.EVT_MOTION, self.OnMove )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnMvEnd( self, event ):
        event.Skip()

    def OnOpen( self, event ):
        event.Skip()

    def OnSaveAs( self, event ):
        event.Skip()

    def OnWClose( self, event ):
        event.Skip()

    def OnExit( self, event ):
        event.Skip()

    def OnCopy( self, event ):
        event.Skip()

    def OnPaste( self, event ):
        event.Skip()

    def OnZoomIn( self, event ):
        event.Skip()

    def OnZoomOut( self, event ):
        event.Skip()

    def OnZoomRst( self, event ):
        event.Skip()

    def OnViewLog( self, event ):
        event.Skip()

    def OnGray( self, event ):
        event.Skip()

    def OnBitwise( self, event ):
        event.Skip()

    def OnContours( self, event ):
        event.Skip()

    def OnEdge( self, event ):
        event.Skip()

    def OnBinOp( self, event ):
        event.Skip()

    def OnOp( self, event ):
        event.Skip()

    def OnDistH( self, event ):
        event.Skip()

    def OnDistV( self, event ):
        event.Skip()

    def OnDistHArea( self, event ):
        event.Skip()

    def OnDistVArea( self, event ):
        event.Skip()

    def OnLine( self, event ):
        event.Skip()

    def OnPixcel( self, event ):
        event.Skip()

    def OnLabel( self, event ):
        event.Skip()

    def OnAbout( self, event ):
        event.Skip()

    def OnLDwn( self, event ):
        event.Skip()

    def OnLUp( self, event ):
        event.Skip()

    def OnMove( self, event ):
        event.Skip()


###########################################################################
## Class EWin
###########################################################################

class EWin ( wx.MDIChildFrame ):

    def __init__( self, parent ):
        wx.MDIChildFrame.__init__ ( self, parent, id = wx.ID_ANY, title = u"その他の画像", pos = wx.DefaultPosition, size = wx.Size( 600,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar2 = wx.MenuBar( 0 )
        self.m_menu4 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"開く(&O)"+ u"\t" + u"CTRL+O", u"画像ファイルを開く", wx.ITEM_NORMAL )
        self.m_menuItem1.SetBitmap( wx.Bitmap( u"icons/01on_open.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu4.Append( self.m_menuItem1 )

        self.m_menu4.AppendSeparator()

        self.m_menuItem8 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"別名保存(&S)"+ u"\t" + u"CTRL+S", u"名前をつけて画像をファイルに保存する", wx.ITEM_NORMAL )
        self.m_menuItem8.SetBitmap( wx.Bitmap( u"icons/02on_save.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu4.Append( self.m_menuItem8 )

        self.m_menu4.AppendSeparator()

        self.m_menuItem9 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"閉じる(&W)"+ u"\t" + u"CTRL+W", u"画像を閉じる", wx.ITEM_NORMAL )
        self.m_menuItem9.SetBitmap( wx.Bitmap( u"icons/03on_fclose.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu4.Append( self.m_menuItem9 )

        self.m_menu4.AppendSeparator()

        self.m_menuItem10 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"終了(&X)", u"ソフトウエアを終了する", wx.ITEM_NORMAL )
        self.m_menuItem10.SetBitmap( wx.Bitmap( u"icons/15on_exit.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu4.Append( self.m_menuItem10 )

        self.m_menubar2.Append( self.m_menu4, u"ファイル(&F)" )

        self.m_menu5 = wx.Menu()
        self.m_menuItem3 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"コピー(&C)"+ u"\t" + u"CTRL+C", u"画像をクリップボードに送る", wx.ITEM_NORMAL )
        self.m_menuItem3.SetBitmap( wx.Bitmap( u"icons/04on_copy.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu5.Append( self.m_menuItem3 )

        self.m_menuItem4 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"ペースト(&P)"+ u"\t" + u"CTRL+V", u"クリップボードから画像を得る", wx.ITEM_NORMAL )
        self.m_menuItem4.SetBitmap( wx.Bitmap( u"icons/on_paste.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu5.Append( self.m_menuItem4 )

        self.m_menubar2.Append( self.m_menu5, u"編集(&E)" )

        self.m_menu6 = wx.Menu()
        self.m_menuItem17 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"拡大(&I)"+ u"\t" + u"CTRL++", u"10%拡大表示する", wx.ITEM_NORMAL )
        self.m_menuItem17.SetBitmap( wx.Bitmap( u"icons/06on_magnify.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu6.Append( self.m_menuItem17 )

        self.m_menuItem18 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"縮小(&O)"+ u"\t" + u"CTRL+-", u"10%縮小表示する", wx.ITEM_NORMAL )
        self.m_menuItem18.SetBitmap( wx.Bitmap( u"icons/05on_reduse.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu6.Append( self.m_menuItem18 )

        self.m_menuItem19 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"表示倍率リセット(&R)", u"100%の大きさで表示する", wx.ITEM_NORMAL )
        self.m_menu6.Append( self.m_menuItem19 )

        self.m_menu6.AppendSeparator()

        self.m_menuItem20 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"処理履歴(&L)", u"画像処理の履歴を表示する", wx.ITEM_NORMAL )
        self.m_menuItem20.SetBitmap( wx.Bitmap( u"icons/on_viewlog.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu6.Append( self.m_menuItem20 )

        self.m_menubar2.Append( self.m_menu6, u"表示(&V)" )

        self.m_menu7 = wx.Menu()
        self.m_menuItem171 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"グレースケール変換(&R)", u"グレースケールの画像に変換する", wx.ITEM_NORMAL )
        self.m_menuItem171.SetBitmap( wx.Bitmap( u"icons/07on_gray.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu7.Append( self.m_menuItem171 )

        self.m_menubar2.Append( self.m_menu7, u"画像変換(&T)" )

        self.m_menu8 = wx.Menu()
        self.m_menuItem159 = wx.MenuItem( self.m_menu8, wx.ID_ANY, u"逆FFT変換(マスク指定)", u"マスクを指定して逆FFT変換する", wx.ITEM_NORMAL )
        self.m_menu8.Append( self.m_menuItem159 )

        self.m_menubar2.Append( self.m_menu8, u"画像処理(&G)" )

        self.m_menu10 = wx.Menu()
        self.m_menuItem30 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"ヒストグラム(&H)", u"画像全体のヒストグラムを表示する", wx.ITEM_NORMAL )
        self.m_menuItem30.SetBitmap( wx.Bitmap( u"icons/08on_hist.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem30 )

        self.m_menuItem31 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"水平方向周辺分布", u"水平方向に周辺分布を集計する", wx.ITEM_NORMAL )
        self.m_menuItem31.SetBitmap( wx.Bitmap( u"icons/09on_dist_h.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem31 )

        self.m_menuItem32 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"垂直方向周辺分布", u"垂直方向に周辺分布を集計する", wx.ITEM_NORMAL )
        self.m_menuItem32.SetBitmap( wx.Bitmap( u"icons/10on_dist_v.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem32 )

        self.m_menu10.AppendSeparator()

        self.m_menuItem33 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"ヒストグラム（領域指定）", u"矩形領域を指定してヒストグラムを求め表示する", wx.ITEM_NORMAL )
        self.m_menuItem33.SetBitmap( wx.Bitmap( u"icons/11on_area.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem33 )

        self.m_menuItem34 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"水平方向周辺分布（領域指定）", u"矩形領域を指定して水平方向に周辺分布を集計する", wx.ITEM_NORMAL )
        self.m_menu10.Append( self.m_menuItem34 )

        self.m_menuItem35 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"垂直方向周辺分布（領域指定）", u"矩形領域を指定して垂直方向に周辺分布を集計する", wx.ITEM_NORMAL )
        self.m_menu10.Append( self.m_menuItem35 )

        self.m_menu10.AppendSeparator()

        self.m_menuItem36 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"線上の分布(&L)", u"線分を指定して輝度分布を求め表示する", wx.ITEM_NORMAL )
        self.m_menuItem36.SetBitmap( wx.Bitmap( u"icons/12on_line.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem36 )

        self.m_menuItem37 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"ピクセル値(&P)", u"座標を指定して、近傍のピクセルの値を表示する", wx.ITEM_NORMAL )
        self.m_menuItem37.SetBitmap( wx.Bitmap( u"icons/13on_get.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu10.Append( self.m_menuItem37 )

        self.m_menubar2.Append( self.m_menu10, u"画像計測(&M)" )

        self.m_menu11 = wx.Menu()
        self.m_menuItem5 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"このソフトについて(&A)", u"ソフトウエアの説明を表示する", wx.ITEM_NORMAL )
        self.m_menuItem5.SetBitmap( wx.Bitmap( u"icons/14on_about.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu11.Append( self.m_menuItem5 )

        self.m_menubar2.Append( self.m_menu11, u"ヘルプ(&H)" )

        self.SetMenuBar( self.m_menubar2 )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow1.SetScrollRate( 5, 5 )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_bitmap1 = wx.StaticBitmap( self.m_scrolledWindow1, wx.ID_ANY, wx.NullBitmap, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        bSizer2.Add( self.m_bitmap1, 0, wx.ALL, 0 )


        self.m_scrolledWindow1.SetSizer( bSizer2 )
        self.m_scrolledWindow1.Layout()
        bSizer2.Fit( self.m_scrolledWindow1 )
        bSizer1.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 0 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MOVE_END, self.OnMvEnd )
        self.Bind( wx.EVT_MENU, self.OnOpen, id = self.m_menuItem1.GetId() )
        self.Bind( wx.EVT_MENU, self.OnSaveAs, id = self.m_menuItem8.GetId() )
        self.Bind( wx.EVT_MENU, self.OnWClose, id = self.m_menuItem9.GetId() )
        self.Bind( wx.EVT_MENU, self.OnExit, id = self.m_menuItem10.GetId() )
        self.Bind( wx.EVT_MENU, self.OnCopy, id = self.m_menuItem3.GetId() )
        self.Bind( wx.EVT_MENU, self.OnPaste, id = self.m_menuItem4.GetId() )
        self.Bind( wx.EVT_MENU, self.OnZoomIn, id = self.m_menuItem17.GetId() )
        self.Bind( wx.EVT_MENU, self.OnZoomOut, id = self.m_menuItem18.GetId() )
        self.Bind( wx.EVT_MENU, self.OnZoomRst, id = self.m_menuItem19.GetId() )
        self.Bind( wx.EVT_MENU, self.OnViewLog, id = self.m_menuItem20.GetId() )
        self.Bind( wx.EVT_MENU, self.OnGray, id = self.m_menuItem171.GetId() )
        self.Bind( wx.EVT_MENU, self.OnIFFT, id = self.m_menuItem159.GetId() )
        self.Bind( wx.EVT_MENU, self.OnHist, id = self.m_menuItem30.GetId() )
        self.Bind( wx.EVT_MENU, self.OnDistH, id = self.m_menuItem31.GetId() )
        self.Bind( wx.EVT_MENU, self.OnDistV, id = self.m_menuItem32.GetId() )
        self.Bind( wx.EVT_MENU, self.OnHistArea, id = self.m_menuItem33.GetId() )
        self.Bind( wx.EVT_MENU, self.OnDistHArea, id = self.m_menuItem34.GetId() )
        self.Bind( wx.EVT_MENU, self.OnDistVArea, id = self.m_menuItem35.GetId() )
        self.Bind( wx.EVT_MENU, self.OnLine, id = self.m_menuItem36.GetId() )
        self.Bind( wx.EVT_MENU, self.OnPixcel, id = self.m_menuItem37.GetId() )
        self.Bind( wx.EVT_MENU, self.OnAbout, id = self.m_menuItem5.GetId() )
        self.m_bitmap1.Bind( wx.EVT_LEFT_DOWN, self.OnLDwn )
        self.m_bitmap1.Bind( wx.EVT_LEFT_UP, self.OnLUp )
        self.m_bitmap1.Bind( wx.EVT_MOTION, self.OnMove )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnMvEnd( self, event ):
        event.Skip()

    def OnOpen( self, event ):
        event.Skip()

    def OnSaveAs( self, event ):
        event.Skip()

    def OnWClose( self, event ):
        event.Skip()

    def OnExit( self, event ):
        event.Skip()

    def OnCopy( self, event ):
        event.Skip()

    def OnPaste( self, event ):
        event.Skip()

    def OnZoomIn( self, event ):
        event.Skip()

    def OnZoomOut( self, event ):
        event.Skip()

    def OnZoomRst( self, event ):
        event.Skip()

    def OnViewLog( self, event ):
        event.Skip()

    def OnGray( self, event ):
        event.Skip()

    def OnIFFT( self, event ):
        event.Skip()

    def OnHist( self, event ):
        event.Skip()

    def OnDistH( self, event ):
        event.Skip()

    def OnDistV( self, event ):
        event.Skip()

    def OnHistArea( self, event ):
        event.Skip()

    def OnDistHArea( self, event ):
        event.Skip()

    def OnDistVArea( self, event ):
        event.Skip()

    def OnLine( self, event ):
        event.Skip()

    def OnPixcel( self, event ):
        event.Skip()

    def OnAbout( self, event ):
        event.Skip()

    def OnLDwn( self, event ):
        event.Skip()

    def OnLUp( self, event ):
        event.Skip()

    def OnMove( self, event ):
        event.Skip()


###########################################################################
## Class LWin
###########################################################################

class LWin ( wx.MDIChildFrame ):

    def __init__( self, parent ):
        wx.MDIChildFrame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ラベリング結果", pos = wx.DefaultPosition, size = wx.Size( 600,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar2 = wx.MenuBar( 0 )
        self.m_menu4 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"開く(&O)"+ u"\t" + u"CTRL+O", u"画像ファイルを開く", wx.ITEM_NORMAL )
        self.m_menuItem1.SetBitmap( wx.Bitmap( u"icons/01on_open.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu4.Append( self.m_menuItem1 )

        self.m_menu4.AppendSeparator()

        self.m_menuItem8 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"別名保存(&S)"+ u"\t" + u"CTRL+S", u"名前をつけて画像をファイルに保存する", wx.ITEM_NORMAL )
        self.m_menuItem8.SetBitmap( wx.Bitmap( u"icons/02on_save.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu4.Append( self.m_menuItem8 )

        self.m_menu4.AppendSeparator()

        self.m_menuItem9 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"閉じる(&W)"+ u"\t" + u"CTRL+W", u"画像を閉じる", wx.ITEM_NORMAL )
        self.m_menuItem9.SetBitmap( wx.Bitmap( u"icons/03on_fclose.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu4.Append( self.m_menuItem9 )

        self.m_menu4.AppendSeparator()

        self.m_menuItem10 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"終了(&X)", u"ソフトウエアを終了する", wx.ITEM_NORMAL )
        self.m_menuItem10.SetBitmap( wx.Bitmap( u"icons/15on_exit.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu4.Append( self.m_menuItem10 )

        self.m_menubar2.Append( self.m_menu4, u"ファイル(&F)" )

        self.m_menu5 = wx.Menu()
        self.m_menuItem3 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"コピー(&C)"+ u"\t" + u"CTRL+C", u"画像をクリップボードに送る", wx.ITEM_NORMAL )
        self.m_menuItem3.SetBitmap( wx.Bitmap( u"icons/04on_copy.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu5.Append( self.m_menuItem3 )

        self.m_menuItem4 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"ペースト(&P)"+ u"\t" + u"CTRL+V", u"クリップボードから画像を得る", wx.ITEM_NORMAL )
        self.m_menuItem4.SetBitmap( wx.Bitmap( u"icons/on_paste.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu5.Append( self.m_menuItem4 )

        self.m_menubar2.Append( self.m_menu5, u"編集(&E)" )

        self.m_menu6 = wx.Menu()
        self.m_menuItem17 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"拡大(&I)"+ u"\t" + u"CTRL++", u"10%拡大表示する", wx.ITEM_NORMAL )
        self.m_menuItem17.SetBitmap( wx.Bitmap( u"icons/06on_magnify.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu6.Append( self.m_menuItem17 )

        self.m_menuItem18 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"縮小(&O)"+ u"\t" + u"CTRL+-", u"10%縮小表示する", wx.ITEM_NORMAL )
        self.m_menuItem18.SetBitmap( wx.Bitmap( u"icons/05on_reduse.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu6.Append( self.m_menuItem18 )

        self.m_menuItem19 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"表示倍率リセット(&R)", u"100%の大きさで表示する", wx.ITEM_NORMAL )
        self.m_menu6.Append( self.m_menuItem19 )

        self.m_menu6.AppendSeparator()

        self.m_menuItem20 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"処理履歴(&L)", u"画像処理の履歴を表示する", wx.ITEM_NORMAL )
        self.m_menuItem20.SetBitmap( wx.Bitmap( u"icons/on_viewlog.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu6.Append( self.m_menuItem20 )

        self.m_menubar2.Append( self.m_menu6, u"表示(&V)" )

        self.m_menu11 = wx.Menu()
        self.m_menuItem5 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"このソフトについて(&A)", u"ソフトウエアの説明を表示する", wx.ITEM_NORMAL )
        self.m_menuItem5.SetBitmap( wx.Bitmap( u"icons/14on_about.png", wx.BITMAP_TYPE_ANY ) )
        self.m_menu11.Append( self.m_menuItem5 )

        self.m_menubar2.Append( self.m_menu11, u"ヘルプ(&H)" )

        self.SetMenuBar( self.m_menubar2 )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow1.SetScrollRate( 5, 5 )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_bitmap1 = wx.StaticBitmap( self.m_scrolledWindow1, wx.ID_ANY, wx.NullBitmap, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        bSizer2.Add( self.m_bitmap1, 0, wx.ALL, 0 )


        self.m_scrolledWindow1.SetSizer( bSizer2 )
        self.m_scrolledWindow1.Layout()
        bSizer2.Fit( self.m_scrolledWindow1 )
        bSizer1.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 0 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MOVE_END, self.OnMvEnd )
        self.Bind( wx.EVT_MENU, self.OnOpen, id = self.m_menuItem1.GetId() )
        self.Bind( wx.EVT_MENU, self.OnSaveAs, id = self.m_menuItem8.GetId() )
        self.Bind( wx.EVT_MENU, self.OnWClose, id = self.m_menuItem9.GetId() )
        self.Bind( wx.EVT_MENU, self.OnExit, id = self.m_menuItem10.GetId() )
        self.Bind( wx.EVT_MENU, self.OnCopy, id = self.m_menuItem3.GetId() )
        self.Bind( wx.EVT_MENU, self.OnPaste, id = self.m_menuItem4.GetId() )
        self.Bind( wx.EVT_MENU, self.OnZoomIn, id = self.m_menuItem17.GetId() )
        self.Bind( wx.EVT_MENU, self.OnZoomOut, id = self.m_menuItem18.GetId() )
        self.Bind( wx.EVT_MENU, self.OnZoomRst, id = self.m_menuItem19.GetId() )
        self.Bind( wx.EVT_MENU, self.OnViewLog, id = self.m_menuItem20.GetId() )
        self.Bind( wx.EVT_MENU, self.OnAbout, id = self.m_menuItem5.GetId() )
        self.m_bitmap1.Bind( wx.EVT_LEFT_DOWN, self.OnLDwn )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnMvEnd( self, event ):
        event.Skip()

    def OnOpen( self, event ):
        event.Skip()

    def OnSaveAs( self, event ):
        event.Skip()

    def OnWClose( self, event ):
        event.Skip()

    def OnExit( self, event ):
        event.Skip()

    def OnCopy( self, event ):
        event.Skip()

    def OnPaste( self, event ):
        event.Skip()

    def OnZoomIn( self, event ):
        event.Skip()

    def OnZoomOut( self, event ):
        event.Skip()

    def OnZoomRst( self, event ):
        event.Skip()

    def OnViewLog( self, event ):
        event.Skip()

    def OnAbout( self, event ):
        event.Skip()

    def OnLDwn( self, event ):
        event.Skip()


###########################################################################
## Class LogDlg
###########################################################################

class LogDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"処理履歴", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        bSizer149 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText116 = wx.StaticText( self, wx.ID_ANY, u"内容を選択し、右クリックでクリップボードにコピーできる", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText116.Wrap( -1 )

        bSizer149.Add( self.m_staticText116, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer149.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button59 = wx.Button( self, wx.ID_ANY, u"ファイル保存", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer149.Add( self.m_button59, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer9.Add( bSizer149, 1, wx.EXPAND, 5 )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,325 ), wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
        bSizer9.Add( self.m_textCtrl1, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer9 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button59.Bind( wx.EVT_BUTTON, self.OnSaveLog )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnSaveLog( self, event ):
        event.Skip()


###########################################################################
## Class PixDlg
###########################################################################

class PixDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"ピクセルの値", pos = wx.DefaultPosition, size = wx.Size( 610,230 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer10 = wx.BoxSizer( wx.VERTICAL )

        self.m_toolBar2 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL )
        self.m_staticText1 = wx.StaticText( self.m_toolBar2, wx.ID_ANY, u"中心座標 (x , y)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        self.m_toolBar2.AddControl( self.m_staticText1 )
        self.m_toolBar2.AddSeparator()

        self.m_spinCtrl1 = wx.SpinCtrl( self.m_toolBar2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 5000, 0 )
        self.m_toolBar2.AddControl( self.m_spinCtrl1 )
        self.m_toolBar2.AddSeparator()

        self.m_spinCtrl2 = wx.SpinCtrl( self.m_toolBar2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 5000, 0 )
        self.m_toolBar2.AddControl( self.m_spinCtrl2 )
        self.m_toolBar2.AddSeparator()

        self.m_tool17 = self.m_toolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/16on_view.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"ピクセルの値を表示する", wx.EmptyString, None )

        self.m_staticText3 = wx.StaticText( self.m_toolBar2, wx.ID_ANY, u"表示される値は カラー画像なら[R , G , B] の順", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        self.m_toolBar2.AddControl( self.m_staticText3 )
        self.m_toolBar2.Realize()

        bSizer10.Add( self.m_toolBar2, 0, wx.EXPAND, 5 )

        self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid1.CreateGrid( 7, 7 )
        self.m_grid1.EnableEditing( False )
        self.m_grid1.EnableGridLines( True )
        self.m_grid1.EnableDragGridSize( False )
        self.m_grid1.SetMargins( 0, 0 )

        # Columns
        self.m_grid1.SetColSize( 0, 70 )
        self.m_grid1.EnableDragColMove( False )
        self.m_grid1.EnableDragColSize( False )
        self.m_grid1.SetColLabelValue( 0, u"-3" )
        self.m_grid1.SetColLabelValue( 1, u"-2" )
        self.m_grid1.SetColLabelValue( 2, u"-1" )
        self.m_grid1.SetColLabelValue( 3, u"0" )
        self.m_grid1.SetColLabelValue( 4, u"1" )
        self.m_grid1.SetColLabelValue( 5, u"2" )
        self.m_grid1.SetColLabelValue( 6, u"3" )
        self.m_grid1.SetColLabelSize( wx.grid.GRID_AUTOSIZE )
        self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid1.EnableDragRowSize( False )
        self.m_grid1.SetRowLabelValue( 0, u"-3" )
        self.m_grid1.SetRowLabelValue( 1, u"-2" )
        self.m_grid1.SetRowLabelValue( 2, u"-1" )
        self.m_grid1.SetRowLabelValue( 3, u"0" )
        self.m_grid1.SetRowLabelValue( 4, u"1" )
        self.m_grid1.SetRowLabelValue( 5, u"2" )
        self.m_grid1.SetRowLabelValue( 6, u"3" )
        self.m_grid1.SetRowLabelSize( wx.grid.GRID_AUTOSIZE )
        self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
        bSizer10.Add( self.m_grid1, 0, wx.ALL, 5 )


        self.SetSizer( bSizer10 )
        self.Layout()

        # Connect Events
        self.Bind( wx.EVT_TOOL, self.OnView, id = self.m_tool17.GetId() )
        self.m_staticText3.Bind( wx.EVT_LEFT_DOWN, self.OnView )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnView( self, event ):
        event.Skip()



###########################################################################
## Class Dlg
###########################################################################

class Dlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"ダイアローグ", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"プレビュー", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"キャンセル", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnCancel )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnPreView )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnExec )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnCancel( self, event ):
        event.Skip()

    def OnPreView( self, event ):
        event.Skip()

    def OnExec( self, event ):
        event.Skip()



###########################################################################
## Class MonoDlg
###########################################################################

class MonoDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"モノトーン変換", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,270 ), wx.TAB_TRAVERSAL )
        bSizer11.Add( self.m_panel1, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"色の選択", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer17.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_colourPicker1 = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 225, 202, 181 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
        bSizer17.Add( self.m_colourPicker1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText143 = wx.StaticText( self, wx.ID_ANY, u"(数値入力、または、マウスで選択)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText143.Wrap( -1 )

        bSizer17.Add( self.m_staticText143, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer11.Add( bSizer17, 1, wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"プレビュー", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"キャンセル", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnCancel )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnPreView )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnExec )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnCancel( self, event ):
        event.Skip()

    def OnPreView( self, event ):
        event.Skip()

    def OnExec( self, event ):
        event.Skip()



###########################################################################
## Class PseudDlg
###########################################################################

class PseudDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"疑似カラー表示", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        bSizer22 = wx.BoxSizer( wx.VERTICAL )

        bSizer232 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bitmap52 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"colorscale/colorscale_jet.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer232.Add( self.m_bitmap52, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_radioBtn12 = wx.RadioButton( self, wx.ID_ANY, u"jet", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.m_radioBtn12.SetValue( True )
        bSizer232.Add( self.m_radioBtn12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer22.Add( bSizer232, 1, wx.EXPAND, 5 )

        bSizer234 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bitmap54 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"colorscale/colorscale_rainbow.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer234.Add( self.m_bitmap54, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_radioBtn14 = wx.RadioButton( self, wx.ID_ANY, u"rainbow", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer234.Add( self.m_radioBtn14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer22.Add( bSizer234, 1, wx.EXPAND, 5 )

        bSizer231 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bitmap51 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"colorscale/colorscale_bone.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer231.Add( self.m_bitmap51, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_radioBtn11 = wx.RadioButton( self, wx.ID_ANY, u"bone", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer231.Add( self.m_radioBtn11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer22.Add( bSizer231, 1, wx.EXPAND, 5 )

        bSizer235 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bitmap55 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"colorscale/colorscale_plasma.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer235.Add( self.m_bitmap55, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_radioBtn15 = wx.RadioButton( self, wx.ID_ANY, u"plasma", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer235.Add( self.m_radioBtn15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer22.Add( bSizer235, 1, wx.EXPAND, 5 )

        bSizer237 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bitmap57 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"colorscale/colorscale_spring.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer237.Add( self.m_bitmap57, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_radioBtn17 = wx.RadioButton( self, wx.ID_ANY, u"spring", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer237.Add( self.m_radioBtn17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer22.Add( bSizer237, 1, wx.EXPAND, 5 )

        bSizer236 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bitmap56 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"colorscale/colorscale_summer.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer236.Add( self.m_bitmap56, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_radioBtn16 = wx.RadioButton( self, wx.ID_ANY, u"summer", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer236.Add( self.m_radioBtn16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer22.Add( bSizer236, 1, wx.EXPAND, 5 )

        bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bitmap5 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"colorscale/colorscale_autumn.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer23.Add( self.m_bitmap5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_radioBtn1 = wx.RadioButton( self, wx.ID_ANY, u"autumn", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer23.Add( self.m_radioBtn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer22.Add( bSizer23, 1, wx.EXPAND, 5 )

        bSizer233 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bitmap53 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"colorscale/colorscale_winter.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer233.Add( self.m_bitmap53, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_radioBtn13 = wx.RadioButton( self, wx.ID_ANY, u"winter", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer233.Add( self.m_radioBtn13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer22.Add( bSizer233, 1, wx.EXPAND, 5 )


        bSizer11.Add( bSizer22, 1, wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"プレビュー", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"キャンセル", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnCancel )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnPreView )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnExec )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnCancel( self, event ):
        event.Skip()

    def OnPreView( self, event ):
        event.Skip()

    def OnExec( self, event ):
        event.Skip()



###########################################################################
## Class CvtColorDlg
###########################################################################

class CvtColorDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"色画像分離", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,150 ), wx.TAB_TRAVERSAL )
        bSizer11.Add( self.m_panel1, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer135 = wx.BoxSizer( wx.VERTICAL )

        m_radioBox5Choices = [ u"X(XYZ)", u"Y(XYZ)", u"Z(XYZ)", u"Y(輝度)(YCrCb)", u"Cr(YCrCb)", u"Cb(YCrCb)", u"H(色相)(HSV)", u"S(彩度)(HSV)", u"V(明度)(HSV)", u"H(色相)(HLS)", u"L(輝度)(HLS)", u"S(彩度)(HLS)", u"L(Lab)", u"a(Lab)", u"b(Lab)", u"L(Luv)", u"u(Luv)", u"v(Luv)", u"Y(輝度)(YUV)", u"U(YUV)", u"V(YUV)", u"B(BGR)", u"G(BGR)", u"R(BGR)" ]
        self.m_radioBox5 = wx.RadioBox( self, wx.ID_ANY, u"色画像分離", wx.DefaultPosition, wx.Size( -1,150 ), m_radioBox5Choices, 5, wx.RA_SPECIFY_COLS )
        self.m_radioBox5.SetSelection( 0 )
        bSizer135.Add( self.m_radioBox5, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer11.Add( bSizer135, 1, wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"プレビュー", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"キャンセル", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnCancel )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnPreView )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnExec )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnCancel( self, event ):
        event.Skip()

    def OnPreView( self, event ):
        event.Skip()

    def OnExec( self, event ):
        event.Skip()



###########################################################################
## Class ShadingDlg
###########################################################################

class ShadingDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"シェーディング補正", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,320 ), 0 )
        self.m_panel3 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer34 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel8 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,170 ), wx.TAB_TRAVERSAL )
        bSizer34.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"処理後画像 = 補正前画像 - 黒基準画像 + オフセット値の計算を行う", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        bSizer34.Add( self.m_staticText8, 0, wx.ALL, 5 )

        bSizer49 = wx.BoxSizer( wx.VERTICAL )

        bSizer35 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText6 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"黒基準画像", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        self.m_staticText6.Wrap( -1 )

        bSizer35.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_filePicker3 = wx.FilePickerCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, u"黒基準画像を選択", u"画像ファイル(png,jpg,bmp)|*.png;*.jpg;*.bmp", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer35.Add( self.m_filePicker3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer49.Add( bSizer35, 1, wx.EXPAND, 5 )

        bSizer50 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText7 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"オフセット値", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        self.m_staticText7.Wrap( -1 )

        bSizer50.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble1 = wx.SpinCtrlDouble( self.m_panel3, wx.ID_ANY, u"128.0", wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, -255, 255, 0, 1 )
        self.m_spinCtrlDouble1.SetDigits( 1 )
        bSizer50.Add( self.m_spinCtrlDouble1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer49.Add( bSizer50, 1, wx.EXPAND, 5 )


        bSizer34.Add( bSizer49, 1, wx.EXPAND, 5 )


        self.m_panel3.SetSizer( bSizer34 )
        self.m_panel3.Layout()
        bSizer34.Fit( self.m_panel3 )
        self.m_notebook1.AddPage( self.m_panel3, u"黒基準画像", True )
        self.m_panel4 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer341 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel81 = wx.Panel( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,130 ), wx.TAB_TRAVERSAL )
        bSizer341.Add( self.m_panel81, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText81 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"処理後画像 = (補正前画像 - 黒基準画像) / (白基準画像 - 黒基準画像) * 乗算値の計算を行う", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText81.Wrap( -1 )

        bSizer341.Add( self.m_staticText81, 0, wx.ALL, 5 )

        bSizer3511 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText611 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"白基準画像", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText611.Wrap( -1 )

        bSizer3511.Add( self.m_staticText611, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_filePicker311 = wx.FilePickerCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, u"黒基準画像を選択", u"画像ファイル(png,jpg,bmp)|*.png;*.jpg;*.bmp", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer3511.Add( self.m_filePicker311, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer341.Add( bSizer3511, 1, wx.EXPAND, 5 )

        bSizer351 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText61 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"黒基準画像", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText61.Wrap( -1 )

        bSizer351.Add( self.m_staticText61, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_filePicker31 = wx.FilePickerCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, u"黒基準画像を選択", u"画像ファイル(png,jpg,bmp)|*.png;*.jpg;*.bmp", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer351.Add( self.m_filePicker31, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer341.Add( bSizer351, 1, wx.EXPAND, 5 )

        bSizer3512 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText711 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"乗算値", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.m_staticText711.Wrap( -1 )

        bSizer3512.Add( self.m_staticText711, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble2 = wx.SpinCtrlDouble( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 500, 255, 1 )
        self.m_spinCtrlDouble2.SetDigits( 1 )
        bSizer3512.Add( self.m_spinCtrlDouble2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer341.Add( bSizer3512, 1, wx.EXPAND, 5 )


        self.m_panel4.SetSizer( bSizer341 )
        self.m_panel4.Layout()
        bSizer341.Fit( self.m_panel4 )
        self.m_notebook1.AddPage( self.m_panel4, u"白・黒基準画像", False )
        self.m_panel5 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer342 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel82 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,210 ), wx.TAB_TRAVERSAL )
        bSizer342.Add( self.m_panel82, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText31 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"処理後画像 = 原画像 / 単純平滑化画像 の計算を行う", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )

        bSizer342.Add( self.m_staticText31, 0, wx.ALL, 5 )

        bSizer491 = wx.BoxSizer( wx.VERTICAL )

        bSizer501 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText71 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"単純平滑化のカーネルサイズ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText71.Wrap( -1 )

        bSizer501.Add( self.m_staticText71, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl41 = wx.SpinCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 101, 31 )
        bSizer501.Add( self.m_spinCtrl41, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer491.Add( bSizer501, 1, wx.EXPAND, 5 )


        bSizer342.Add( bSizer491, 1, wx.EXPAND, 5 )


        self.m_panel5.SetSizer( bSizer342 )
        self.m_panel5.Layout()
        bSizer342.Fit( self.m_panel5 )
        self.m_notebook1.AddPage( self.m_panel5, u"凸凹係数", False )
        self.m_panel6 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3421 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel821 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,210 ), wx.TAB_TRAVERSAL )
        bSizer3421.Add( self.m_panel821, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText311 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"モルフォロジー演算MORPH_BLACKHAT(入力画像とクロージングした画像の差)を行い、輝度反転する", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText311.Wrap( -1 )

        bSizer3421.Add( self.m_staticText311, 0, wx.ALL, 5 )

        bSizer4911 = wx.BoxSizer( wx.VERTICAL )

        bSizer5011 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText712 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"モルフォロジー演算のカーネルサイズ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText712.Wrap( -1 )

        bSizer5011.Add( self.m_staticText712, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl412 = wx.SpinCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 101, 15 )
        bSizer5011.Add( self.m_spinCtrl412, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer4911.Add( bSizer5011, 1, wx.EXPAND, 5 )


        bSizer3421.Add( bSizer4911, 1, wx.EXPAND, 5 )


        self.m_panel6.SetSizer( bSizer3421 )
        self.m_panel6.Layout()
        bSizer3421.Fit( self.m_panel6 )
        self.m_notebook1.AddPage( self.m_panel6, u"モルフォロジー演算", False )

        bSizer11.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"プレビュー", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"キャンセル", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnCancel )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnPreView )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnExec )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnCancel( self, event ):
        event.Skip()

    def OnPreView( self, event ):
        event.Skip()

    def OnExec( self, event ):
        event.Skip()



###########################################################################
## Class ChHistDlg
###########################################################################

class ChHistDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"ヒストグラム変更（カラー画像の場合は輝度のみ変更）", pos = wx.DefaultPosition, size = wx.Size( 600,600 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 450,380 ), wx.TAB_TRAVERSAL )
        bSizer11.Add( self.m_panel11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,120 ), wx.NB_MULTILINE )
        self.m_panel12 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer50 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText19 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"clipLimit 大きくすればコントラストが強くなる\ntile 大きいと大局的に平坦化、小さいと部分的に平坦化", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )

        bSizer50.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText20 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"ClipLimit", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )

        bSizer50.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble3 = wx.SpinCtrlDouble( self.m_panel12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 200, 40, 5 )
        self.m_spinCtrlDouble3.SetDigits( 1 )
        bSizer50.Add( self.m_spinCtrlDouble3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText21 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"tile", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )

        bSizer50.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble4 = wx.SpinCtrlDouble( self.m_panel12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 100, 8, 1 )
        self.m_spinCtrlDouble4.SetDigits( 0 )
        bSizer50.Add( self.m_spinCtrlDouble4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.m_panel12.SetSizer( bSizer50 )
        self.m_panel12.Layout()
        bSizer50.Fit( self.m_panel12 )
        self.m_notebook2.AddPage( self.m_panel12, u"コントラスト制限適応ヒストグラム平坦化", True )
        self.m_panel13 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer51 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText22 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"（パラメータなし）", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )

        bSizer51.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.m_panel13.SetSizer( bSizer51 )
        self.m_panel13.Layout()
        bSizer51.Fit( self.m_panel13 )
        self.m_notebook2.AddPage( self.m_panel13, u"平坦化", False )
        self.m_panel79 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer149 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText130 = wx.StaticText( self.m_panel79, wx.ID_ANY, u"ヒストグラムを範囲内に収める", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText130.Wrap( -1 )

        bSizer149.Add( self.m_staticText130, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText131 = wx.StaticText( self.m_panel79, wx.ID_ANY, u"最小", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText131.Wrap( -1 )

        bSizer149.Add( self.m_staticText131, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble44 = wx.SpinCtrlDouble( self.m_panel79, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 255, 0, 5 )
        self.m_spinCtrlDouble44.SetDigits( 0 )
        bSizer149.Add( self.m_spinCtrlDouble44, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText132 = wx.StaticText( self.m_panel79, wx.ID_ANY, u"最大", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText132.Wrap( -1 )

        bSizer149.Add( self.m_staticText132, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble45 = wx.SpinCtrlDouble( self.m_panel79, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 255, 255, 5 )
        self.m_spinCtrlDouble45.SetDigits( 0 )
        bSizer149.Add( self.m_spinCtrlDouble45, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.m_panel79.SetSizer( bSizer149 )
        self.m_panel79.Layout()
        bSizer149.Fit( self.m_panel79 )
        self.m_notebook2.AddPage( self.m_panel79, u"正規化", False )
        self.m_panel16 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer55 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText29 = wx.StaticText( self.m_panel16, wx.ID_ANY, u"輝度の分布を min から maxに拡張する\ny' = max(y) * (y - min) / (max - min) の計算を行う", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText29.Wrap( -1 )

        bSizer55.Add( self.m_staticText29, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText30 = wx.StaticText( self.m_panel16, wx.ID_ANY, u"min", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText30.Wrap( -1 )

        bSizer55.Add( self.m_staticText30, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble8 = wx.SpinCtrlDouble( self.m_panel16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 255, 0, 5 )
        self.m_spinCtrlDouble8.SetDigits( 0 )
        bSizer55.Add( self.m_spinCtrlDouble8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText31 = wx.StaticText( self.m_panel16, wx.ID_ANY, u"max", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )

        bSizer55.Add( self.m_staticText31, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble9 = wx.SpinCtrlDouble( self.m_panel16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 255, 255, 5 )
        self.m_spinCtrlDouble9.SetDigits( 0 )
        bSizer55.Add( self.m_spinCtrlDouble9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.m_panel16.SetSizer( bSizer55 )
        self.m_panel16.Layout()
        bSizer55.Fit( self.m_panel16 )
        self.m_notebook2.AddPage( self.m_panel16, u"拡張", False )
        self.m_panel17 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer54 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText32 = wx.StaticText( self.m_panel17, wx.ID_ANY, u"grad = (max2 - min2) / (max1 - min1)\ny' = grad * (y - min1) + min2 の計算を行う", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText32.Wrap( -1 )

        bSizer54.Add( self.m_staticText32, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        bSizer58 = wx.BoxSizer( wx.VERTICAL )

        bSizer59 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText33 = wx.StaticText( self.m_panel17, wx.ID_ANY, u"伸張する前の輝度(min1 , max1)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText33.Wrap( -1 )

        bSizer59.Add( self.m_staticText33, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble10 = wx.SpinCtrlDouble( self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 255, 0, 1 )
        self.m_spinCtrlDouble10.SetDigits( 0 )
        bSizer59.Add( self.m_spinCtrlDouble10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble11 = wx.SpinCtrlDouble( self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 255, 255, 1 )
        self.m_spinCtrlDouble11.SetDigits( 0 )
        bSizer59.Add( self.m_spinCtrlDouble11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer58.Add( bSizer59, 1, wx.EXPAND, 5 )

        bSizer60 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText34 = wx.StaticText( self.m_panel17, wx.ID_ANY, u"伸張した後の輝度(min2 , max2)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText34.Wrap( -1 )

        bSizer60.Add( self.m_staticText34, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble12 = wx.SpinCtrlDouble( self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 255, 0, 1 )
        self.m_spinCtrlDouble12.SetDigits( 0 )
        bSizer60.Add( self.m_spinCtrlDouble12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble13 = wx.SpinCtrlDouble( self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 255, 255, 1 )
        self.m_spinCtrlDouble13.SetDigits( 0 )
        bSizer60.Add( self.m_spinCtrlDouble13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer58.Add( bSizer60, 1, wx.EXPAND, 5 )


        bSizer54.Add( bSizer58, 1, wx.EXPAND, 5 )


        self.m_panel17.SetSizer( bSizer54 )
        self.m_panel17.Layout()
        bSizer54.Fit( self.m_panel17 )
        self.m_notebook2.AddPage( self.m_panel17, u"伸張", False )
        self.m_panel18 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer53 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText35 = wx.StaticText( self.m_panel18, wx.ID_ANY, u"（パラメータなし）", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText35.Wrap( -1 )

        bSizer53.Add( self.m_staticText35, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.m_panel18.SetSizer( bSizer53 )
        self.m_panel18.Layout()
        bSizer53.Fit( self.m_panel18 )
        self.m_notebook2.AddPage( self.m_panel18, u"反転", False )
        self.m_panel19 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer52 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText36 = wx.StaticText( self.m_panel19, wx.ID_ANY, u"３チャンネルの輝度を反転する（パラメータなし）(グレースケール画像の場合は「反転」と同じ)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText36.Wrap( -1 )

        bSizer52.Add( self.m_staticText36, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.m_panel19.SetSizer( bSizer52 )
        self.m_panel19.Layout()
        bSizer52.Fit( self.m_panel19 )
        self.m_notebook2.AddPage( self.m_panel19, u"ネガポジ変換", False )
        self.m_panel15 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer56 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText26 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"y' = (y - mean(y)) * std / std(y) + avg の計算をする", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText26.Wrap( -1 )

        bSizer56.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText27 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"標準偏差", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText27.Wrap( -1 )

        bSizer56.Add( self.m_staticText27, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble6 = wx.SpinCtrlDouble( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 128, 32, 4 )
        self.m_spinCtrlDouble6.SetDigits( 0 )
        bSizer56.Add( self.m_spinCtrlDouble6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText28 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"平均", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText28.Wrap( -1 )

        bSizer56.Add( self.m_staticText28, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble7 = wx.SpinCtrlDouble( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 255, 128, 5 )
        self.m_spinCtrlDouble7.SetDigits( 0 )
        bSizer56.Add( self.m_spinCtrlDouble7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.m_panel15.SetSizer( bSizer56 )
        self.m_panel15.Layout()
        bSizer56.Fit( self.m_panel15 )
        self.m_notebook2.AddPage( self.m_panel15, u"平均と標準偏差を指定して変換", False )
        self.m_panel14 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer57 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText23 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"y' = (alpha * (y - 127) + 127 ) + beta の計算を行う", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText23.Wrap( -1 )

        bSizer57.Add( self.m_staticText23, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText24 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"alpha", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText24.Wrap( -1 )

        bSizer57.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble5 = wx.SpinCtrlDouble( self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 10, 1.000000, 0.5 )
        self.m_spinCtrlDouble5.SetDigits( 1 )
        bSizer57.Add( self.m_spinCtrlDouble5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText25 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"beta", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText25.Wrap( -1 )

        bSizer57.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble48 = wx.SpinCtrlDouble( self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, -255, 255, 0, 1 )
        self.m_spinCtrlDouble48.SetDigits( 1 )
        bSizer57.Add( self.m_spinCtrlDouble48, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.m_panel14.SetSizer( bSizer57 )
        self.m_panel14.Layout()
        bSizer57.Fit( self.m_panel14 )
        self.m_notebook2.AddPage( self.m_panel14, u"コントラスト、明るさ変換Ａ", False )
        self.m_panel80 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer150 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText135 = wx.StaticText( self.m_panel80, wx.ID_ANY, u"dst = (src ∗ alpha + beta) の計算を行う", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText135.Wrap( -1 )

        bSizer150.Add( self.m_staticText135, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText133 = wx.StaticText( self.m_panel80, wx.ID_ANY, u"alpha", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText133.Wrap( -1 )

        bSizer150.Add( self.m_staticText133, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble46 = wx.SpinCtrlDouble( self.m_panel80, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 100, 1, 1 )
        self.m_spinCtrlDouble46.SetDigits( 1 )
        bSizer150.Add( self.m_spinCtrlDouble46, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText134 = wx.StaticText( self.m_panel80, wx.ID_ANY, u"beta", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText134.Wrap( -1 )

        bSizer150.Add( self.m_staticText134, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble47 = wx.SpinCtrlDouble( self.m_panel80, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, -255, 255, 0, 1 )
        self.m_spinCtrlDouble47.SetDigits( 1 )
        bSizer150.Add( self.m_spinCtrlDouble47, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.m_panel80.SetSizer( bSizer150 )
        self.m_panel80.Layout()
        bSizer150.Fit( self.m_panel80 )
        self.m_notebook2.AddPage( self.m_panel80, u"コントラスト、明るさ変換Ｂ", False )

        bSizer11.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"プレビュー", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"キャンセル", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnCancel )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnPreView )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnExec )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnCancel( self, event ):
        event.Skip()

    def OnPreView( self, event ):
        event.Skip()

    def OnExec( self, event ):
        event.Skip()



###########################################################################
## Class FilterDlg
###########################################################################

class FilterDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"画像フィルタ", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook3 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,310 ), wx.NB_MULTILINE )
        self.m_panel20 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer63 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel29 = wx.Panel( self.m_panel20, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,210 ), wx.TAB_TRAVERSAL )
        bSizer63.Add( self.m_panel29, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer64 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText36 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"カーネルサイズ(3以上の奇数)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText36.Wrap( -1 )

        bSizer64.Add( self.m_staticText36, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl7 = wx.SpinCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 3, 201, 3 )
        bSizer64.Add( self.m_spinCtrl7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer63.Add( bSizer64, 1, wx.EXPAND, 5 )


        self.m_panel20.SetSizer( bSizer63 )
        self.m_panel20.Layout()
        bSizer63.Fit( self.m_panel20 )
        self.m_notebook3.AddPage( self.m_panel20, u"単純平滑化", True )
        self.m_panel21 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer631 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel291 = wx.Panel( self.m_panel21, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,210 ), wx.TAB_TRAVERSAL )
        bSizer631.Add( self.m_panel291, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer641 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText361 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"カーネルサイズ(3以上の奇数)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText361.Wrap( -1 )

        bSizer641.Add( self.m_staticText361, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl71 = wx.SpinCtrl( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 3, 201, 3 )
        bSizer641.Add( self.m_spinCtrl71, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer631.Add( bSizer641, 1, wx.EXPAND, 5 )


        self.m_panel21.SetSizer( bSizer631 )
        self.m_panel21.Layout()
        bSizer631.Fit( self.m_panel21 )
        self.m_notebook3.AddPage( self.m_panel21, u"メディアンフィルタ", False )
        self.m_panel22 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer632 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel292 = wx.Panel( self.m_panel22, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,210 ), wx.TAB_TRAVERSAL )
        bSizer632.Add( self.m_panel292, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer642 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText362 = wx.StaticText( self.m_panel22, wx.ID_ANY, u"カーネルサイズ(3以上の奇数)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText362.Wrap( -1 )

        bSizer642.Add( self.m_staticText362, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl72 = wx.SpinCtrl( self.m_panel22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 3, 101, 5 )
        bSizer642.Add( self.m_spinCtrl72, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText40 = wx.StaticText( self.m_panel22, wx.ID_ANY, u"標準偏差", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText40.Wrap( -1 )

        bSizer642.Add( self.m_staticText40, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble14 = wx.SpinCtrlDouble( self.m_panel22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 100, 3, 1 )
        self.m_spinCtrlDouble14.SetDigits( 0 )
        bSizer642.Add( self.m_spinCtrlDouble14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer632.Add( bSizer642, 1, wx.EXPAND, 5 )


        self.m_panel22.SetSizer( bSizer632 )
        self.m_panel22.Layout()
        bSizer632.Fit( self.m_panel22 )
        self.m_notebook3.AddPage( self.m_panel22, u"ガウシアンフィルタ", False )
        self.m_panel23 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6321 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel2921 = wx.Panel( self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,190 ), wx.TAB_TRAVERSAL )
        bSizer6321.Add( self.m_panel2921, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText46 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"処理後画像 = 原画像 + (原画像 - ガウシアン平滑化画像) * 乗数 の計算を行い画像を鮮明にする", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText46.Wrap( -1 )

        bSizer6321.Add( self.m_staticText46, 0, wx.ALL, 5 )

        bSizer6421 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText3621 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"カーネルサイズ(3以上の奇数)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3621.Wrap( -1 )

        bSizer6421.Add( self.m_staticText3621, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl721 = wx.SpinCtrl( self.m_panel23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 3, 101, 5 )
        bSizer6421.Add( self.m_spinCtrl721, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText401 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"標準偏差", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText401.Wrap( -1 )

        bSizer6421.Add( self.m_staticText401, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble141 = wx.SpinCtrlDouble( self.m_panel23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 100, 3, 1 )
        self.m_spinCtrlDouble141.SetDigits( 0 )
        bSizer6421.Add( self.m_spinCtrlDouble141, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText45 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"乗数", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText45.Wrap( -1 )

        bSizer6421.Add( self.m_staticText45, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble17 = wx.SpinCtrlDouble( self.m_panel23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 100, 1, 1 )
        self.m_spinCtrlDouble17.SetDigits( 1 )
        bSizer6421.Add( self.m_spinCtrlDouble17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer6321.Add( bSizer6421, 1, wx.EXPAND, 5 )


        self.m_panel23.SetSizer( bSizer6321 )
        self.m_panel23.Layout()
        bSizer6321.Fit( self.m_panel23 )
        self.m_notebook3.AddPage( self.m_panel23, u"アンシャープフィルタ", False )
        self.m_panel24 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6322 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel2922 = wx.Panel( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,180 ), wx.TAB_TRAVERSAL )
        bSizer6322.Add( self.m_panel2922, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText149 = wx.StaticText( self.m_panel24, wx.ID_ANY, u"エッジを残した平滑化", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText149.Wrap( -1 )

        bSizer6322.Add( self.m_staticText149, 0, wx.ALL, 5 )

        bSizer6422 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText3622 = wx.StaticText( self.m_panel24, wx.ID_ANY, u"処理する隣接ピクセル", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3622.Wrap( -1 )

        bSizer6422.Add( self.m_staticText3622, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl722 = wx.SpinCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 100, 15 )
        bSizer6422.Add( self.m_spinCtrl722, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText402 = wx.StaticText( self.m_panel24, wx.ID_ANY, u"色空間標準偏差", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText402.Wrap( -1 )

        bSizer6422.Add( self.m_staticText402, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble142 = wx.SpinCtrlDouble( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 100, 25, 1 )
        self.m_spinCtrlDouble142.SetDigits( 1 )
        bSizer6422.Add( self.m_spinCtrlDouble142, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText48 = wx.StaticText( self.m_panel24, wx.ID_ANY, u"距離空間標準偏差", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText48.Wrap( -1 )

        bSizer6422.Add( self.m_staticText48, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble19 = wx.SpinCtrlDouble( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 100, 25, 1 )
        self.m_spinCtrlDouble19.SetDigits( 1 )
        bSizer6422.Add( self.m_spinCtrlDouble19, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer6322.Add( bSizer6422, 1, wx.EXPAND, 5 )


        self.m_panel24.SetSizer( bSizer6322 )
        self.m_panel24.Layout()
        bSizer6322.Fit( self.m_panel24 )
        self.m_notebook3.AddPage( self.m_panel24, u"バイラテラルフィルタ", False )
        self.m_panel25 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer63221 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel29221 = wx.Panel( self.m_panel25, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,130 ), wx.TAB_TRAVERSAL )
        bSizer63221.Add( self.m_panel29221, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText144 = wx.StaticText( self.m_panel25, wx.ID_ANY, u"エッジを残した平滑化\nsigma_s : sigma spatial 近接領域のサイズ\nsigma_r : sigma range   近接領域の異なる色を平均化する。\n                 sigma_rを大きくすると、特定の色の領域が広くなる。", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText144.Wrap( -1 )

        bSizer63221.Add( self.m_staticText144, 0, wx.ALL, 5 )

        bSizer64221 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText4021 = wx.StaticText( self.m_panel25, wx.ID_ANY, u"sigma_s", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4021.Wrap( -1 )

        bSizer64221.Add( self.m_staticText4021, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble1421 = wx.SpinCtrlDouble( self.m_panel25, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 200, 3, 1 )
        self.m_spinCtrlDouble1421.SetDigits( 1 )
        bSizer64221.Add( self.m_spinCtrlDouble1421, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText481 = wx.StaticText( self.m_panel25, wx.ID_ANY, u"sigma_r", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText481.Wrap( -1 )

        bSizer64221.Add( self.m_staticText481, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble191 = wx.SpinCtrlDouble( self.m_panel25, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 1, 0.1, 0.05 )
        self.m_spinCtrlDouble191.SetDigits( 2 )
        bSizer64221.Add( self.m_spinCtrlDouble191, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer63221.Add( bSizer64221, 1, wx.EXPAND, 5 )


        self.m_panel25.SetSizer( bSizer63221 )
        self.m_panel25.Layout()
        bSizer63221.Fit( self.m_panel25 )
        self.m_notebook3.AddPage( self.m_panel25, u"エッジプレザービング", False )
        self.m_panel26 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer632211 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel292211 = wx.Panel( self.m_panel26, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,145 ), wx.TAB_TRAVERSAL )
        bSizer632211.Add( self.m_panel292211, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText1441 = wx.StaticText( self.m_panel26, wx.ID_ANY, u"sigma_s : sigma spatial 近接領域のサイズ\nsigma_r : sigma range   近接領域の異なる色を平均化する。\n                 sigma_rを大きくすると、特定の色の領域が広くなる。", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1441.Wrap( -1 )

        bSizer632211.Add( self.m_staticText1441, 0, wx.ALL, 5 )

        bSizer642211 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText40211 = wx.StaticText( self.m_panel26, wx.ID_ANY, u"sigma_s", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText40211.Wrap( -1 )

        bSizer642211.Add( self.m_staticText40211, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble14211 = wx.SpinCtrlDouble( self.m_panel26, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 200, 10, 1 )
        self.m_spinCtrlDouble14211.SetDigits( 1 )
        bSizer642211.Add( self.m_spinCtrlDouble14211, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText4811 = wx.StaticText( self.m_panel26, wx.ID_ANY, u"sigma_r", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4811.Wrap( -1 )

        bSizer642211.Add( self.m_staticText4811, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble1911 = wx.SpinCtrlDouble( self.m_panel26, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 1, 0.15, 0.05 )
        self.m_spinCtrlDouble1911.SetDigits( 2 )
        bSizer642211.Add( self.m_spinCtrlDouble1911, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer632211.Add( bSizer642211, 1, wx.EXPAND, 5 )


        self.m_panel26.SetSizer( bSizer632211 )
        self.m_panel26.Layout()
        bSizer632211.Fit( self.m_panel26 )
        self.m_notebook3.AddPage( self.m_panel26, u"細部強調フィルタ", False )
        self.m_panel27 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer633 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel293 = wx.Panel( self.m_panel27, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,145 ), wx.TAB_TRAVERSAL )
        bSizer633.Add( self.m_panel293, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText54 = wx.StaticText( self.m_panel27, wx.ID_ANY, u"dx , dy 微分の次数と方向を決定する\n(dx, dy)=(1, 0) 縦方向の輪郭検出\n(dx, dy)=(0, 1) 横方向の輪郭検出\n(dx, dy)=(1, 1) 斜め右上方向の輪郭検出", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText54.Wrap( -1 )

        bSizer633.Add( self.m_staticText54, 0, wx.ALL, 5 )

        bSizer643 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText61 = wx.StaticText( self.m_panel27, wx.ID_ANY, u"方向(dx , dy)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText61.Wrap( -1 )

        bSizer643.Add( self.m_staticText61, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl17 = wx.SpinCtrl( self.m_panel27, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 2, 1 )
        bSizer643.Add( self.m_spinCtrl17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl18 = wx.SpinCtrl( self.m_panel27, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 2, 1 )
        bSizer643.Add( self.m_spinCtrl18, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText363 = wx.StaticText( self.m_panel27, wx.ID_ANY, u"カーネルサイズ(奇数)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText363.Wrap( -1 )

        bSizer643.Add( self.m_staticText363, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl73 = wx.SpinCtrl( self.m_panel27, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 7, 3 )
        bSizer643.Add( self.m_spinCtrl73, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText153 = wx.StaticText( self.m_panel27, wx.ID_ANY, u"オフセット", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText153.Wrap( -1 )

        bSizer643.Add( self.m_staticText153, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble49 = wx.SpinCtrlDouble( self.m_panel27, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 255, 128, 1 )
        self.m_spinCtrlDouble49.SetDigits( 0 )
        bSizer643.Add( self.m_spinCtrlDouble49, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer633.Add( bSizer643, 1, wx.EXPAND, 5 )


        self.m_panel27.SetSizer( bSizer633 )
        self.m_panel27.Layout()
        bSizer633.Fit( self.m_panel27 )
        self.m_notebook3.AddPage( self.m_panel27, u"ゾーベル(１次微分)フィルタ", False )
        self.m_panel28 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer634 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel294 = wx.Panel( self.m_panel28, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,210 ), wx.TAB_TRAVERSAL )
        bSizer634.Add( self.m_panel294, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer644 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText364 = wx.StaticText( self.m_panel28, wx.ID_ANY, u"カーネルサイズ(奇数)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText364.Wrap( -1 )

        bSizer644.Add( self.m_staticText364, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl74 = wx.SpinCtrl( self.m_panel28, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 101, 3 )
        bSizer644.Add( self.m_spinCtrl74, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText154 = wx.StaticText( self.m_panel28, wx.ID_ANY, u"オフセット", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText154.Wrap( -1 )

        bSizer644.Add( self.m_staticText154, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble50 = wx.SpinCtrlDouble( self.m_panel28, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 255, 128, 1 )
        self.m_spinCtrlDouble50.SetDigits( 0 )
        bSizer644.Add( self.m_spinCtrlDouble50, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer634.Add( bSizer644, 1, wx.EXPAND, 5 )


        self.m_panel28.SetSizer( bSizer634 )
        self.m_panel28.Layout()
        bSizer634.Fit( self.m_panel28 )
        self.m_notebook3.AddPage( self.m_panel28, u"ラプラシアン(２次微分)フィルタ", False )
        self.m_panel76 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer146 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel77 = wx.Panel( self.m_panel76, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        bSizer136 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText117 = wx.StaticText( self.m_panel77, wx.ID_ANY, u"7x7のカーネルとして処理している。不要な要素は0にしておく\nカーネルの妥当性はチェックしていない\n乗数と除数でコントラスト、加算値で明るさを調整できる", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText117.Wrap( -1 )

        bSizer136.Add( self.m_staticText117, 1, wx.ALL|wx.EXPAND, 5 )


        self.m_panel77.SetSizer( bSizer136 )
        self.m_panel77.Layout()
        bSizer136.Fit( self.m_panel77 )
        bSizer146.Add( self.m_panel77, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer82 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer82.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer83 = wx.BoxSizer( wx.VERTICAL )


        bSizer83.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_spinCtrl16 = wx.SpinCtrl( self.m_panel76, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, -255, 255, 1 )
        bSizer83.Add( self.m_spinCtrl16, 0, wx.ALL, 5 )

        self.m_staticline1 = wx.StaticLine( self.m_panel76, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer83.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_spinCtrl171 = wx.SpinCtrl( self.m_panel76, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 255, 1 )
        bSizer83.Add( self.m_spinCtrl171, 0, wx.ALL, 5 )


        bSizer83.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer82.Add( bSizer83, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText56 = wx.StaticText( self.m_panel76, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText56.Wrap( -1 )

        bSizer82.Add( self.m_staticText56, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_grid2 = wx.grid.Grid( self.m_panel76, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE )

        # Grid
        self.m_grid2.CreateGrid( 7, 7 )
        self.m_grid2.EnableEditing( True )
        self.m_grid2.EnableGridLines( True )
        self.m_grid2.EnableDragGridSize( False )
        self.m_grid2.SetMargins( 0, 0 )

        # Columns
        self.m_grid2.SetColSize( 0, 30 )
        self.m_grid2.SetColSize( 1, 30 )
        self.m_grid2.SetColSize( 2, 30 )
        self.m_grid2.SetColSize( 3, 30 )
        self.m_grid2.SetColSize( 4, 30 )
        self.m_grid2.SetColSize( 5, 30 )
        self.m_grid2.SetColSize( 6, 30 )
        self.m_grid2.EnableDragColMove( False )
        self.m_grid2.EnableDragColSize( False )
        self.m_grid2.SetColLabelSize( 0 )
        self.m_grid2.SetColLabelAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTER )

        # Rows
        self.m_grid2.EnableDragRowSize( True )
        self.m_grid2.SetRowLabelSize( 0 )
        self.m_grid2.SetRowLabelAlignment( wx.ALIGN_RIGHT, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_RIGHT, wx.ALIGN_CENTER )
        bSizer82.Add( self.m_grid2, 0, wx.ALL, 0 )

        self.m_staticText57 = wx.StaticText( self.m_panel76, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText57.Wrap( -1 )

        bSizer82.Add( self.m_staticText57, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl181 = wx.SpinCtrl( self.m_panel76, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, -255, 255, 0 )
        bSizer82.Add( self.m_spinCtrl181, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer82.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer146.Add( bSizer82, 1, wx.EXPAND, 5 )

        bSizer84 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText58 = wx.StaticText( self.m_panel76, wx.ID_ANY, u"フィルタファイルの読み込み", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText58.Wrap( -1 )

        bSizer84.Add( self.m_staticText58, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_filePicker4 = wx.FilePickerCtrl( self.m_panel76, wx.ID_ANY, wx.EmptyString, u"フィルタファイルの選択", u"フィルタファイル(*.xml)|*.xml", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_OPEN )
        bSizer84.Add( self.m_filePicker4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer146.Add( bSizer84, 1, wx.EXPAND, 5 )


        self.m_panel76.SetSizer( bSizer146 )
        self.m_panel76.Layout()
        bSizer146.Fit( self.m_panel76 )
        self.m_notebook3.AddPage( self.m_panel76, u"空間フィルタ", False )

        bSizer11.Add( self.m_notebook3, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"プレビュー", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"キャンセル", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnCancel )
        self.m_filePicker4.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFOpen )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnPreView )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnExec )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnCancel( self, event ):
        event.Skip()

    def OnFOpen( self, event ):
        event.Skip()

    def OnPreView( self, event ):
        event.Skip()

    def OnExec( self, event ):
        event.Skip()



###########################################################################
## Class LookUpDlg
###########################################################################

class LookUpDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"ルックアップテーブル変換（カラー画像の場合は輝度のみ変換）", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel39 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 270,270 ), wx.TAB_TRAVERSAL )
        bSizer11.Add( self.m_panel39, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer90 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText59 = wx.StaticText( self, wx.ID_ANY, u"ファイル選択", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText59.Wrap( -1 )

        bSizer90.Add( self.m_staticText59, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_filePicker5 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"ルックアップテーブルを選択", u"ルックアップテーブルファイル(*.xml)|*.xml", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer90.Add( self.m_filePicker5, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer11.Add( bSizer90, 1, wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"プレビュー", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"キャンセル", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnCancel )
        self.m_filePicker5.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFOpen )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnPreView )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnExec )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnCancel( self, event ):
        event.Skip()

    def OnFOpen( self, event ):
        event.Skip()

    def OnPreView( self, event ):
        event.Skip()

    def OnExec( self, event ):
        event.Skip()



###########################################################################
## Class SamplingDlg
###########################################################################

class SamplingDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"画像抽出", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,270 ), wx.TAB_TRAVERSAL )
        bSizer11.Add( self.m_panel1, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"色の上限", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer17.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_colourPicker1 = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 255, 255, 255 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL )
        bSizer17.Add( self.m_colourPicker1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText62 = wx.StaticText( self, wx.ID_ANY, u"色の下限", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText62.Wrap( -1 )

        bSizer17.Add( self.m_staticText62, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_colourPicker5 = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 0, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL )
        bSizer17.Add( self.m_colourPicker5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer11.Add( bSizer17, 1, wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"プレビュー", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"キャンセル", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnCancel )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnPreView )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnExec )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnCancel( self, event ):
        event.Skip()

    def OnPreView( self, event ):
        event.Skip()

    def OnExec( self, event ):
        event.Skip()



###########################################################################
## Class MorphologyDlg
###########################################################################

class MorphologyDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"モルフォロジー処理", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel42 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,160 ), wx.TAB_TRAVERSAL )
        bSizer11.Add( self.m_panel42, 1, wx.EXPAND |wx.ALL, 5 )

        m_radioBox2Choices = [ u"収縮(erosion)", u"膨張(dilate)", u"収縮→膨張(open)", u"膨張→収縮(close)", u"膨張した画像と収縮した画像の差を取る(gradient)", u"入力画像とオープニングした画像の差を取る(tophat)", u"入力画像とクロージングした画像の差を取る(blackhat)" ]
        self.m_radioBox2 = wx.RadioBox( self, wx.ID_ANY, u"処理の種類（グレースケール、２値画像は「白い部分」に注目した処理を行う）", wx.DefaultPosition, wx.DefaultSize, m_radioBox2Choices, 2, wx.RA_SPECIFY_COLS )
        self.m_radioBox2.SetSelection( 0 )
        bSizer11.Add( self.m_radioBox2, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer149 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText151 = wx.StaticText( self, wx.ID_ANY, u"カーネルサイズ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText151.Wrap( -1 )

        bSizer149.Add( self.m_staticText151, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl44 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 3, 100, 3 )
        bSizer149.Add( self.m_spinCtrl44, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText118 = wx.StaticText( self, wx.ID_ANY, u"繰返し回数", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText118.Wrap( -1 )

        bSizer149.Add( self.m_staticText118, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl37 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 30, 1 )
        bSizer149.Add( self.m_spinCtrl37, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer11.Add( bSizer149, 1, wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"プレビュー", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"キャンセル", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnCancel )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnPreView )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnExec )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnCancel( self, event ):
        event.Skip()

    def OnPreView( self, event ):
        event.Skip()

    def OnExec( self, event ):
        event.Skip()



###########################################################################
## Class EdgeDlg
###########################################################################

class EdgeDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"エッジ検出", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook3 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,310 ), wx.NB_MULTILINE )
        self.m_panel21 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer631 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel291 = wx.Panel( self.m_panel21, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        bSizer631.Add( self.m_panel291, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText142 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"事前にガウシアンフィルタでぼかしておく必要がある。ぼかしの程度で検出感度が変わる", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText142.Wrap( -1 )

        self.m_staticText142.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

        bSizer631.Add( self.m_staticText142, 0, wx.ALL, 5 )

        gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText102 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"投票器の解像度 0.8 ～ 1.2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText102.Wrap( -1 )

        gSizer1.Add( self.m_staticText102, 0, wx.ALL, 5 )

        self.m_spinCtrlDouble42 = wx.SpinCtrlDouble( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 10, 0.800000, 0.1 )
        self.m_spinCtrlDouble42.SetDigits( 1 )
        gSizer1.Add( self.m_spinCtrlDouble42, 0, wx.ALL, 5 )

        self.m_staticText103 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"円同士が最低限離れていなければならない距離", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText103.Wrap( -1 )

        gSizer1.Add( self.m_staticText103, 0, wx.ALL, 5 )

        self.m_spinCtrlDouble43 = wx.SpinCtrlDouble( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 500, 50, 10 )
        self.m_spinCtrlDouble43.SetDigits( 1 )
        gSizer1.Add( self.m_spinCtrlDouble43, 0, wx.ALL, 5 )

        self.m_staticText104 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"Canny法のHysteresis処理の閾値", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText104.Wrap( -1 )

        gSizer1.Add( self.m_staticText104, 0, wx.ALL, 5 )

        self.m_spinCtrlDouble44 = wx.SpinCtrlDouble( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 500, 100, 1 )
        self.m_spinCtrlDouble44.SetDigits( 1 )
        gSizer1.Add( self.m_spinCtrlDouble44, 0, wx.ALL, 5 )

        self.m_staticText105 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"円の中心を検出する際の閾値", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText105.Wrap( -1 )

        gSizer1.Add( self.m_staticText105, 0, wx.ALL, 5 )

        self.m_spinCtrlDouble45 = wx.SpinCtrlDouble( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 500, 100, 1 )
        self.m_spinCtrlDouble45.SetDigits( 1 )
        gSizer1.Add( self.m_spinCtrlDouble45, 0, wx.ALL, 5 )

        self.m_staticText106 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"検出する円の半径の下限", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText106.Wrap( -1 )

        gSizer1.Add( self.m_staticText106, 0, wx.ALL, 5 )

        self.m_spinCtrl40 = wx.SpinCtrl( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 1000, 10 )
        gSizer1.Add( self.m_spinCtrl40, 0, wx.ALL, 5 )

        self.m_staticText107 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"検出する円の半径の上限", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText107.Wrap( -1 )

        gSizer1.Add( self.m_staticText107, 0, wx.ALL, 5 )

        self.m_spinCtrl41 = wx.SpinCtrl( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, -1, 1000, 1000 )
        gSizer1.Add( self.m_spinCtrl41, 0, wx.ALL, 5 )


        bSizer631.Add( gSizer1, 1, wx.EXPAND, 5 )


        self.m_panel21.SetSizer( bSizer631 )
        self.m_panel21.Layout()
        bSizer631.Fit( self.m_panel21 )
        self.m_notebook3.AddPage( self.m_panel21, u"ハフ変換（円）", True )
        self.m_panel22 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer632 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel292 = wx.Panel( self.m_panel22, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        bSizer632.Add( self.m_panel292, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText141 = wx.StaticText( self.m_panel22, wx.ID_ANY, u"事前にCanny法で輪郭検出をしておくと良い", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText141.Wrap( -1 )

        self.m_staticText141.SetForegroundColour( wx.Colour( 0, 0, 255 ) )

        bSizer632.Add( self.m_staticText141, 0, wx.ALL, 5 )

        gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText108 = wx.StaticText( self.m_panel22, wx.ID_ANY, u"直角座標点と直線の距離", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText108.Wrap( -1 )

        gSizer3.Add( self.m_staticText108, 0, wx.ALL, 5 )

        self.m_spinCtrlDouble47 = wx.SpinCtrlDouble( self.m_panel22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 100, 1, 1 )
        self.m_spinCtrlDouble47.SetDigits( 1 )
        gSizer3.Add( self.m_spinCtrlDouble47, 0, wx.ALL, 5 )

        self.m_staticText110 = wx.StaticText( self.m_panel22, wx.ID_ANY, u"直線とみなすための閾値(100前後)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText110.Wrap( -1 )

        gSizer3.Add( self.m_staticText110, 0, wx.ALL, 5 )

        self.m_spinCtrl42 = wx.SpinCtrl( self.m_panel22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 500, 100 )
        gSizer3.Add( self.m_spinCtrl42, 0, wx.ALL, 5 )

        self.m_staticText111 = wx.StaticText( self.m_panel22, wx.ID_ANY, u"直線とみなす最小の長さ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText111.Wrap( -1 )

        gSizer3.Add( self.m_staticText111, 0, wx.ALL, 5 )

        self.m_spinCtrl441 = wx.SpinCtrl( self.m_panel22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 1000, 400 )
        gSizer3.Add( self.m_spinCtrl441, 0, wx.ALL, 5 )

        self.m_staticText112 = wx.StaticText( self.m_panel22, wx.ID_ANY, u"同一直線とみなす点間隔の長さ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText112.Wrap( -1 )

        gSizer3.Add( self.m_staticText112, 0, wx.ALL, 5 )

        self.m_spinCtrl451 = wx.SpinCtrl( self.m_panel22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 1000, 5 )
        gSizer3.Add( self.m_spinCtrl451, 0, wx.ALL, 5 )


        bSizer632.Add( gSizer3, 1, wx.EXPAND, 5 )


        self.m_panel22.SetSizer( bSizer632 )
        self.m_panel22.Layout()
        bSizer632.Fit( self.m_panel22 )
        self.m_notebook3.AddPage( self.m_panel22, u"ハフ変換（線分）", False )
        self.m_panel23 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6321 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel2921 = wx.Panel( self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        bSizer6321.Add( self.m_panel2921, 1, wx.EXPAND |wx.ALL, 5 )

        gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText113 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"長さ閾値(これより短いセグメントは破棄)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText113.Wrap( -1 )

        gSizer5.Add( self.m_staticText113, 0, wx.ALL, 5 )

        self.m_spinCtrl43 = wx.SpinCtrl( self.m_panel23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 1000, 10 )
        gSizer5.Add( self.m_spinCtrl43, 0, wx.ALL, 5 )

        self.m_staticText114 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"距離閾値(これより遠いポイントは外れ値)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText114.Wrap( -1 )

        gSizer5.Add( self.m_staticText114, 0, wx.ALL, 5 )

        self.m_spinCtrlDouble51 = wx.SpinCtrlDouble( self.m_panel23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 100, 1.414, 0.1 )
        self.m_spinCtrlDouble51.SetDigits( 3 )
        gSizer5.Add( self.m_spinCtrlDouble51, 0, wx.ALL, 5 )

        self.m_staticText115 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"Canny最初の閾値", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText115.Wrap( -1 )

        gSizer5.Add( self.m_staticText115, 0, wx.ALL, 5 )

        self.m_spinCtrl44 = wx.SpinCtrl( self.m_panel23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 255, 50 )
        gSizer5.Add( self.m_spinCtrl44, 0, wx.ALL, 5 )

        self.m_staticText116 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"Canny次の閾値", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText116.Wrap( -1 )

        gSizer5.Add( self.m_staticText116, 0, wx.ALL, 5 )

        self.m_spinCtrl45 = wx.SpinCtrl( self.m_panel23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 255, 150 )
        gSizer5.Add( self.m_spinCtrl45, 0, wx.ALL, 5 )

        self.m_staticText117 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"Canny法のアパチャーサイズ(3 , 5 , 7のいずれか)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText117.Wrap( -1 )

        gSizer5.Add( self.m_staticText117, 0, wx.ALL, 5 )

        self.m_spinCtrl46 = wx.SpinCtrl( self.m_panel23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 3, 7, 3 )
        gSizer5.Add( self.m_spinCtrl46, 0, wx.ALL, 5 )

        self.m_staticText118 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"増分マージオプション", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText118.Wrap( -1 )

        gSizer5.Add( self.m_staticText118, 0, wx.ALL, 5 )

        m_choice1Choices = [ u"True", u"False" ]
        self.m_choice1 = wx.Choice( self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.Size( 70,-1 ), m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        gSizer5.Add( self.m_choice1, 0, wx.ALL, 5 )


        bSizer6321.Add( gSizer5, 1, wx.EXPAND, 5 )


        self.m_panel23.SetSizer( bSizer6321 )
        self.m_panel23.Layout()
        bSizer6321.Fit( self.m_panel23 )
        self.m_notebook3.AddPage( self.m_panel23, u"Fast Line Detector", False )
        self.m_panel24 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6322 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel2922 = wx.Panel( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        bSizer6322.Add( self.m_panel2922, 1, wx.EXPAND |wx.ALL, 5 )

        gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText119 = wx.StaticText( self.m_panel24, wx.ID_ANY, u"scale", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText119.Wrap( -1 )

        gSizer6.Add( self.m_staticText119, 0, wx.ALL, 5 )

        self.m_spinCtrlDouble52 = wx.SpinCtrlDouble( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 100, 0.8, 1 )
        self.m_spinCtrlDouble52.SetDigits( 1 )
        gSizer6.Add( self.m_spinCtrlDouble52, 0, wx.ALL, 5 )

        self.m_staticText120 = wx.StaticText( self.m_panel24, wx.ID_ANY, u"sigma_scale", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText120.Wrap( -1 )

        gSizer6.Add( self.m_staticText120, 0, wx.ALL, 5 )

        self.m_spinCtrlDouble58 = wx.SpinCtrlDouble( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 100, 0.6, 0.1 )
        self.m_spinCtrlDouble58.SetDigits( 1 )
        gSizer6.Add( self.m_spinCtrlDouble58, 0, wx.ALL, 5 )

        self.m_staticText121 = wx.StaticText( self.m_panel24, wx.ID_ANY, u"quant", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText121.Wrap( -1 )

        gSizer6.Add( self.m_staticText121, 0, wx.ALL, 5 )

        self.m_spinCtrlDouble57 = wx.SpinCtrlDouble( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 100, 2, 0.1 )
        self.m_spinCtrlDouble57.SetDigits( 1 )
        gSizer6.Add( self.m_spinCtrlDouble57, 0, wx.ALL, 5 )

        self.m_staticText122 = wx.StaticText( self.m_panel24, wx.ID_ANY, u"ang_th", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText122.Wrap( -1 )

        gSizer6.Add( self.m_staticText122, 0, wx.ALL, 5 )

        self.m_spinCtrlDouble56 = wx.SpinCtrlDouble( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 100, 22.5, 0.1 )
        self.m_spinCtrlDouble56.SetDigits( 1 )
        gSizer6.Add( self.m_spinCtrlDouble56, 0, wx.ALL, 5 )

        self.m_staticText123 = wx.StaticText( self.m_panel24, wx.ID_ANY, u"log_eps", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText123.Wrap( -1 )

        gSizer6.Add( self.m_staticText123, 0, wx.ALL, 5 )

        self.m_spinCtrlDouble55 = wx.SpinCtrlDouble( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 100, 0, 0.1 )
        self.m_spinCtrlDouble55.SetDigits( 1 )
        gSizer6.Add( self.m_spinCtrlDouble55, 0, wx.ALL, 5 )

        self.m_staticText124 = wx.StaticText( self.m_panel24, wx.ID_ANY, u"density_th", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText124.Wrap( -1 )

        gSizer6.Add( self.m_staticText124, 0, wx.ALL, 5 )

        self.m_spinCtrlDouble54 = wx.SpinCtrlDouble( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 100, 0.7, 0.1 )
        self.m_spinCtrlDouble54.SetDigits( 1 )
        gSizer6.Add( self.m_spinCtrlDouble54, 0, wx.ALL, 5 )

        self.m_staticText125 = wx.StaticText( self.m_panel24, wx.ID_ANY, u"n_bins", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText125.Wrap( -1 )

        gSizer6.Add( self.m_staticText125, 0, wx.ALL, 5 )

        self.m_spinCtrl461 = wx.SpinCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 20000, 1024 )
        gSizer6.Add( self.m_spinCtrl461, 0, wx.ALL, 5 )


        bSizer6322.Add( gSizer6, 1, wx.EXPAND, 5 )


        self.m_panel24.SetSizer( bSizer6322 )
        self.m_panel24.Layout()
        bSizer6322.Fit( self.m_panel24 )
        self.m_notebook3.AddPage( self.m_panel24, u"Line Segment Detector", False )

        bSizer11.Add( self.m_notebook3, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"プレビュー", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"キャンセル", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnCancel )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnPreView )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnExec )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnCancel( self, event ):
        event.Skip()

    def OnPreView( self, event ):
        event.Skip()

    def OnExec( self, event ):
        event.Skip()



###########################################################################
## Class CannyDlg
###########################################################################

class CannyDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"境界検出(Canny法)", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        bSizer63 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel29 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,185 ), wx.TAB_TRAVERSAL )
        bSizer63.Add( self.m_panel29, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText137 = wx.StaticText( self, wx.ID_ANY, u"処理結果は２値画像になる", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText137.Wrap( -1 )

        bSizer63.Add( self.m_staticText137, 0, wx.ALL, 5 )

        gSizer15 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText36 = wx.StaticText( self, wx.ID_ANY, u"最小しきい値(連続性の大きさ)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText36.Wrap( -1 )

        gSizer15.Add( self.m_staticText36, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl7 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 255, 50 )
        gSizer15.Add( self.m_spinCtrl7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText99 = wx.StaticText( self, wx.ID_ANY, u"最大しきい値(この輝度ならばエッジである)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText99.Wrap( -1 )

        gSizer15.Add( self.m_staticText99, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl37 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 255, 150 )
        gSizer15.Add( self.m_spinCtrl37, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText100 = wx.StaticText( self, wx.ID_ANY, u"ゾーベルフィルタのサイズ(3 , 5 , 7のいずれか)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText100.Wrap( -1 )

        gSizer15.Add( self.m_staticText100, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl38 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 3, 7, 3 )
        gSizer15.Add( self.m_spinCtrl38, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer63.Add( gSizer15, 0, wx.EXPAND, 5 )


        bSizer11.Add( bSizer63, 1, wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"プレビュー", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"キャンセル", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnCancel )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnPreView )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnExec )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnCancel( self, event ):
        event.Skip()

    def OnPreView( self, event ):
        event.Skip()

    def OnExec( self, event ):
        event.Skip()



###########################################################################
## Class ArtDlg
###########################################################################

class ArtDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"絵画効果", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook3 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,320 ), wx.NB_MULTILINE )
        self.m_panel20 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer63 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel29 = wx.Panel( self.m_panel20, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,200 ), wx.TAB_TRAVERSAL )
        bSizer63.Add( self.m_panel29, 1, wx.EXPAND |wx.ALL, 5 )

        gSizer17 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText36 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"近接領域のサイズ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText36.Wrap( -1 )

        gSizer17.Add( self.m_staticText36, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl7 = wx.SpinCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 500, 3 )
        gSizer17.Add( self.m_spinCtrl7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText99 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"最大しきい値", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText99.Wrap( -1 )

        gSizer17.Add( self.m_staticText99, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl37 = wx.SpinCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 500, 5 )
        gSizer17.Add( self.m_spinCtrl37, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer63.Add( gSizer17, 1, wx.EXPAND, 5 )


        self.m_panel20.SetSizer( bSizer63 )
        self.m_panel20.Layout()
        bSizer63.Fit( self.m_panel20 )
        self.m_notebook3.AddPage( self.m_panel20, u"油絵調変換", True )
        self.m_panel21 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer631 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel291 = wx.Panel( self.m_panel21, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,145 ), wx.TAB_TRAVERSAL )
        bSizer631.Add( self.m_panel291, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText147 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"sigma_s : sigma spatial 近接領域のサイズ\nsigma_r : sigma range   近接領域の異なる色を平均化する。\n                 sigma_rを大きくすると、特定の色の領域が広くなる。", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText147.Wrap( -1 )

        bSizer631.Add( self.m_staticText147, 0, wx.ALL, 5 )

        gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText102 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"sigma_s", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText102.Wrap( -1 )

        gSizer1.Add( self.m_staticText102, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble42 = wx.SpinCtrlDouble( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 200, 60, 5 )
        self.m_spinCtrlDouble42.SetDigits( 1 )
        gSizer1.Add( self.m_spinCtrlDouble42, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText103 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"sigma_r", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText103.Wrap( -1 )

        gSizer1.Add( self.m_staticText103, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble43 = wx.SpinCtrlDouble( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 1, 0.45, 0.1 )
        self.m_spinCtrlDouble43.SetDigits( 2 )
        gSizer1.Add( self.m_spinCtrlDouble43, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer631.Add( gSizer1, 1, wx.EXPAND, 5 )


        self.m_panel21.SetSizer( bSizer631 )
        self.m_panel21.Layout()
        bSizer631.Fit( self.m_panel21 )
        self.m_notebook3.AddPage( self.m_panel21, u"水彩画調変換", False )
        self.m_panel22 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer632 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel292 = wx.Panel( self.m_panel22, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,110 ), wx.TAB_TRAVERSAL )
        bSizer632.Add( self.m_panel292, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText148 = wx.StaticText( self.m_panel22, wx.ID_ANY, u"sigma_s : sigma spatial 近接領域のサイズ\nsigma_r : sigma range   近接領域の異なる色を平均化する。\n                 sigma_rを大きくすると、特定の色の領域が広くなる。\nshade_factor 明るさを調整するパラメータ。", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText148.Wrap( -1 )

        bSizer632.Add( self.m_staticText148, 0, wx.ALL, 5 )

        gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText108 = wx.StaticText( self.m_panel22, wx.ID_ANY, u"sigma_s", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText108.Wrap( -1 )

        gSizer3.Add( self.m_staticText108, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble47 = wx.SpinCtrlDouble( self.m_panel22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 200, 60, 5 )
        self.m_spinCtrlDouble47.SetDigits( 1 )
        gSizer3.Add( self.m_spinCtrlDouble47, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText109 = wx.StaticText( self.m_panel22, wx.ID_ANY, u"sigma_r", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText109.Wrap( -1 )

        gSizer3.Add( self.m_staticText109, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble48 = wx.SpinCtrlDouble( self.m_panel22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 1, 0.07, 0.05 )
        self.m_spinCtrlDouble48.SetDigits( 2 )
        gSizer3.Add( self.m_spinCtrlDouble48, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText110 = wx.StaticText( self.m_panel22, wx.ID_ANY, u"shade_factor", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText110.Wrap( -1 )

        gSizer3.Add( self.m_staticText110, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble49 = wx.SpinCtrlDouble( self.m_panel22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 0.1, 0.05, 0.01 )
        self.m_spinCtrlDouble49.SetDigits( 2 )
        gSizer3.Add( self.m_spinCtrlDouble49, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer632.Add( gSizer3, 1, wx.EXPAND, 5 )


        self.m_panel22.SetSizer( bSizer632 )
        self.m_panel22.Layout()
        bSizer632.Fit( self.m_panel22 )
        self.m_notebook3.AddPage( self.m_panel22, u"鉛筆画調変換", False )
        self.m_panel23 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6321 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel2921 = wx.Panel( self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,240 ), wx.TAB_TRAVERSAL )
        bSizer6321.Add( self.m_panel2921, 1, wx.EXPAND |wx.ALL, 5 )

        gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText113 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"階調数(減色して n 階調にする)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText113.Wrap( -1 )

        gSizer5.Add( self.m_staticText113, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl43 = wx.SpinCtrl( self.m_panel23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 255, 4 )
        gSizer5.Add( self.m_spinCtrl43, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer6321.Add( gSizer5, 1, wx.EXPAND, 5 )


        self.m_panel23.SetSizer( bSizer6321 )
        self.m_panel23.Layout()
        bSizer6321.Fit( self.m_panel23 )
        self.m_notebook3.AddPage( self.m_panel23, u"ポスタリゼーション", False )

        bSizer11.Add( self.m_notebook3, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"プレビュー", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"キャンセル", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnCancel )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnPreView )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnExec )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnCancel( self, event ):
        event.Skip()

    def OnPreView( self, event ):
        event.Skip()

    def OnExec( self, event ):
        event.Skip()



###########################################################################
## Class OpDlg
###########################################################################

class OpDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"画像間演算", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        bSizer109 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText96 = wx.StaticText( self, wx.ID_ANY, u"画像１", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.m_staticText96.Wrap( -1 )

        bSizer109.Add( self.m_staticText96, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        m_choice2Choices = []
        self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
        self.m_choice2.SetSelection( 0 )
        bSizer109.Add( self.m_choice2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText97 = wx.StaticText( self, wx.ID_ANY, u"係数１", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText97.Wrap( -1 )

        bSizer109.Add( self.m_staticText97, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble44 = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, -10, 10, 1, 0.1 )
        self.m_spinCtrlDouble44.SetDigits( 1 )
        bSizer109.Add( self.m_spinCtrlDouble44, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer11.Add( bSizer109, 1, wx.EXPAND, 5 )

        bSizer110 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText98 = wx.StaticText( self, wx.ID_ANY, u"画像２", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.m_staticText98.Wrap( -1 )

        bSizer110.Add( self.m_staticText98, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        m_choice3Choices = []
        self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
        self.m_choice3.SetSelection( 0 )
        bSizer110.Add( self.m_choice3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText99 = wx.StaticText( self, wx.ID_ANY, u"係数２", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText99.Wrap( -1 )

        bSizer110.Add( self.m_staticText99, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble45 = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, -10, 10, 1, 0.1 )
        self.m_spinCtrlDouble45.SetDigits( 1 )
        bSizer110.Add( self.m_spinCtrlDouble45, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer11.Add( bSizer110, 1, wx.EXPAND, 5 )

        bSizer111 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText100 = wx.StaticText( self, wx.ID_ANY, u"オフセット", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.m_staticText100.Wrap( -1 )

        bSizer111.Add( self.m_staticText100, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl32 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, -255, 255, 0 )
        bSizer111.Add( self.m_spinCtrl32, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer11.Add( bSizer111, 1, wx.EXPAND, 5 )

        m_radioBox3Choices = [ u"係数付き加算", u"加算", u"減算", u"差の絶対値", u"大きい方", u"小さい方", u"AND", u"OR", u"XOR", u"透過" ]
        self.m_radioBox3 = wx.RadioBox( self, wx.ID_ANY, u"演算の種類", wx.DefaultPosition, wx.DefaultSize, m_radioBox3Choices, 6, wx.RA_SPECIFY_COLS )
        self.m_radioBox3.SetSelection( 0 )
        bSizer11.Add( self.m_radioBox3, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"係数付き加算\n　新画像　＝　画像１＊係数１＋画像２＊係数２＋オフセット\n　係数の範囲　-10 <= x <= 10　オフセットの範囲  -255 <= x <= 255　係数の和を1.0にする必要はない\n算術演算、論理演算\n　新画像　＝　画像１　(演算)　画像２（係数は無視される）\n透過演算\n　新画像　＝　画像１＊係数１＋画像２＊（１－係数１）＋オフセット", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText101.Wrap( -1 )

        bSizer11.Add( self.m_staticText101, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"プレビュー", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"キャンセル", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnCancel )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnPreView )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnExec )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnCancel( self, event ):
        event.Skip()

    def OnPreView( self, event ):
        event.Skip()

    def OnExec( self, event ):
        event.Skip()



###########################################################################
## Class BinaryDlg
###########################################################################

class BinaryDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"２値化", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 370,230 ), wx.TAB_TRAVERSAL )
        bSizer11.Add( self.m_panel11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,80 ), wx.NB_MULTILINE )
        self.m_panel12 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer50 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText20 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"閾値", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.m_staticText20.Wrap( -1 )

        bSizer50.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl35 = wx.SpinCtrl( self.m_panel12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 255, 128 )
        bSizer50.Add( self.m_spinCtrl35, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.m_panel12.SetSizer( bSizer50 )
        self.m_panel12.Layout()
        bSizer50.Fit( self.m_panel12 )
        self.m_notebook2.AddPage( self.m_panel12, u"固定閾値", True )
        self.m_panel13 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer51 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText22 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"（パラメータなし）", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )

        bSizer51.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText119 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"計算された閾値 = ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText119.Wrap( -1 )

        bSizer51.Add( self.m_staticText119, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.m_panel13.SetSizer( bSizer51 )
        self.m_panel13.Layout()
        bSizer51.Fit( self.m_panel13 )
        self.m_notebook2.AddPage( self.m_panel13, u"自動閾値(大津の手法)", False )
        self.m_panel14 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer57 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText23 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"（パラメータなし）", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText23.Wrap( -1 )

        bSizer57.Add( self.m_staticText23, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText120 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"計算された閾値 = ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText120.Wrap( -1 )

        bSizer57.Add( self.m_staticText120, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.m_panel14.SetSizer( bSizer57 )
        self.m_panel14.Layout()
        bSizer57.Fit( self.m_panel14 )
        self.m_notebook2.AddPage( self.m_panel14, u"自動閾値(トライアングルアルゴリズム)", False )
        self.m_panel15 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer56 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText26 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"アルゴリズム", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText26.Wrap( -1 )

        bSizer56.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        m_choice4Choices = [ u"平均", u"ガウシアン" ]
        self.m_choice4 = wx.Choice( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0 )
        self.m_choice4.SetSelection( 0 )
        bSizer56.Add( self.m_choice4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText27 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"近傍サイズ(1より大きい奇数)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText27.Wrap( -1 )

        bSizer56.Add( self.m_staticText27, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl36 = wx.SpinCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 200, 51 )
        bSizer56.Add( self.m_spinCtrl36, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText28 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"計算した閾値から引く値", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText28.Wrap( -1 )

        bSizer56.Add( self.m_staticText28, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl37 = wx.SpinCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, -255, 255, 0 )
        bSizer56.Add( self.m_spinCtrl37, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.m_panel15.SetSizer( bSizer56 )
        self.m_panel15.Layout()
        bSizer56.Fit( self.m_panel15 )
        self.m_notebook2.AddPage( self.m_panel15, u"適応的２値化", False )

        bSizer11.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"プレビュー", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"キャンセル", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnCancel )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnPreView )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnExec )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnCancel( self, event ):
        event.Skip()

    def OnPreView( self, event ):
        event.Skip()

    def OnExec( self, event ):
        event.Skip()



###########################################################################
## Class BinOpDlg
###########################################################################

class BinOpDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"２値画像処理", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,320 ), wx.NB_MULTILINE )
        self.m_panel12 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer150 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel92 = wx.Panel( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,240 ), wx.TAB_TRAVERSAL )
        bSizer150.Add( self.m_panel92, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer50 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText20 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"（パラメータなし）", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.m_staticText20.Wrap( -1 )

        bSizer50.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer150.Add( bSizer50, 1, wx.EXPAND, 5 )


        self.m_panel12.SetSizer( bSizer150 )
        self.m_panel12.Layout()
        bSizer150.Fit( self.m_panel12 )
        self.m_notebook2.AddPage( self.m_panel12, u"白黒反転", True )
        self.m_panel13 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer131 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel74 = wx.Panel( self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,240 ), wx.TAB_TRAVERSAL )
        bSizer131.Add( self.m_panel74, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer51 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText22 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"（パラメータなし）", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )

        bSizer51.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer131.Add( bSizer51, 1, wx.EXPAND, 5 )


        self.m_panel13.SetSizer( bSizer131 )
        self.m_panel13.Layout()
        bSizer131.Fit( self.m_panel13 )
        self.m_notebook2.AddPage( self.m_panel13, u"白孤立点除去", False )
        self.m_panel14 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer129 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel73 = wx.Panel( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,240 ), wx.TAB_TRAVERSAL )
        bSizer129.Add( self.m_panel73, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer57 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText23 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"（パラメータなし）", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText23.Wrap( -1 )

        bSizer57.Add( self.m_staticText23, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer129.Add( bSizer57, 1, wx.EXPAND, 5 )


        self.m_panel14.SetSizer( bSizer129 )
        self.m_panel14.Layout()
        bSizer129.Fit( self.m_panel14 )
        self.m_notebook2.AddPage( self.m_panel14, u"黒孤立点除去", False )
        self.m_panel15 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer127 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel72 = wx.Panel( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,205 ), wx.TAB_TRAVERSAL )
        bSizer127.Add( self.m_panel72, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText137 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"白い部分を細線化する。  ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText137.Wrap( -1 )

        self.m_staticText137.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

        bSizer127.Add( self.m_staticText137, 0, wx.ALL, 5 )

        bSizer56 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText128 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"アルゴリズム", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText128.Wrap( -1 )

        bSizer56.Add( self.m_staticText128, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        m_choice4Choices = [ u"ZHANGSUEN", u"GUOHALL" ]
        self.m_choice4 = wx.Choice( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0 )
        self.m_choice4.SetSelection( 0 )
        bSizer56.Add( self.m_choice4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer127.Add( bSizer56, 1, wx.EXPAND, 5 )


        self.m_panel15.SetSizer( bSizer127 )
        self.m_panel15.Layout()
        bSizer127.Fit( self.m_panel15 )
        self.m_notebook2.AddPage( self.m_panel15, u"細線化(スケルトン化)", False )
        self.m_panel77 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer137 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel81 = wx.Panel( self.m_panel77, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,110 ), wx.TAB_TRAVERSAL )
        bSizer137.Add( self.m_panel81, 1, wx.EXPAND |wx.ALL, 5 )

        m_radioBox2Choices = [ u"収縮(erosion)", u"膨張(dilate)", u"収縮→膨張(open)", u"膨張→収縮(close)", u"膨張した画像と収縮した画像の差を取る(gradient)", u"入力画像とオープニングした画像の差を取る(tophat)", u"入力画像とクロージングした画像の差を取る(blackhat)" ]
        self.m_radioBox2 = wx.RadioBox( self.m_panel77, wx.ID_ANY, u"処理の種類(白い部分の縮小、膨張処理)", wx.DefaultPosition, wx.Size( -1,-1 ), m_radioBox2Choices, 2, wx.RA_SPECIFY_COLS )
        self.m_radioBox2.SetSelection( 0 )
        self.m_radioBox2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer137.Add( self.m_radioBox2, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer149 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText1511 = wx.StaticText( self.m_panel77, wx.ID_ANY, u"カーネルサイズ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1511.Wrap( -1 )

        bSizer149.Add( self.m_staticText1511, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl441 = wx.SpinCtrl( self.m_panel77, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 100, 5 )
        bSizer149.Add( self.m_spinCtrl441, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText1181 = wx.StaticText( self.m_panel77, wx.ID_ANY, u"繰返し回数", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1181.Wrap( -1 )

        bSizer149.Add( self.m_staticText1181, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl371 = wx.SpinCtrl( self.m_panel77, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 30, 1 )
        bSizer149.Add( self.m_spinCtrl371, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer137.Add( bSizer149, 1, wx.EXPAND, 5 )


        self.m_panel77.SetSizer( bSizer137 )
        self.m_panel77.Layout()
        bSizer137.Fit( self.m_panel77 )
        self.m_notebook2.AddPage( self.m_panel77, u"モルフォロジー処理", False )

        bSizer11.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"プレビュー", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"キャンセル", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnCancel )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnPreView )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnExec )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnCancel( self, event ):
        event.Skip()

    def OnPreView( self, event ):
        event.Skip()

    def OnExec( self, event ):
        event.Skip()



###########################################################################
## Class BinHoughDlg
###########################################################################

class BinHoughDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"２値画像ハフ変換(線分)", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel75 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,240 ), wx.TAB_TRAVERSAL )
        bSizer11.Add( self.m_panel75, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText136 = wx.StaticText( self, wx.ID_ANY, u"白い部分から線を抽出する。白い部分を細線化してから実行する必要がある", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText136.Wrap( -1 )

        self.m_staticText136.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

        bSizer11.Add( self.m_staticText136, 0, wx.ALL, 5 )

        bSizer133 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText113 = wx.StaticText( self, wx.ID_ANY, u"距離分解能", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText113.Wrap( -1 )

        bSizer133.Add( self.m_staticText113, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble46 = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 1000, 1, 1 )
        self.m_spinCtrlDouble46.SetDigits( 1 )
        bSizer133.Add( self.m_spinCtrlDouble46, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText114 = wx.StaticText( self, wx.ID_ANY, u"角度分解能", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText114.Wrap( -1 )

        bSizer133.Add( self.m_staticText114, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble47 = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 360, 180, 1 )
        self.m_spinCtrlDouble47.SetDigits( 0 )
        bSizer133.Add( self.m_spinCtrlDouble47, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText115 = wx.StaticText( self, wx.ID_ANY, u"投票の閾値", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText115.Wrap( -1 )

        bSizer133.Add( self.m_staticText115, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl37 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 2000, 200 )
        bSizer133.Add( self.m_spinCtrl37, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer11.Add( bSizer133, 1, wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"プレビュー", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"キャンセル", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnCancel )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnPreView )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnExec )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnCancel( self, event ):
        event.Skip()

    def OnPreView( self, event ):
        event.Skip()

    def OnExec( self, event ):
        event.Skip()



###########################################################################
## Class IFFTDlg
###########################################################################

class IFFTDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"逆FFT変換", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        bSizer140 = wx.BoxSizer( wx.VERTICAL )

        self.m_bitmap14 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 300,270 ), 0 )
        bSizer140.Add( self.m_bitmap14, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer11.Add( bSizer140, 1, wx.EXPAND, 5 )

        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"マスク画像を使う", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.m_checkBox1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_filePicker6 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"マスク画像を選択", u"画像ファイル(png,jpg,bmp)|*.png;*.jpg;*.bmp", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer17.Add( self.m_filePicker6, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer11.Add( bSizer17, 1, wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"プレビュー", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"キャンセル", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnCancel )
        self.m_filePicker6.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFOpen )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnPreView )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnExec )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnCancel( self, event ):
        event.Skip()

    def OnFOpen( self, event ):
        event.Skip()

    def OnPreView( self, event ):
        event.Skip()

    def OnExec( self, event ):
        event.Skip()



###########################################################################
## Class RetDlg
###########################################################################

class RetDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"結果表示", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        bSizer148 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText115 = wx.StaticText( self, wx.ID_ANY, u"内容を選択し、右クリックでクリップボードにコピーできる", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText115.Wrap( -1 )

        bSizer148.Add( self.m_staticText115, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer148.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button58 = wx.Button( self, wx.ID_ANY, u"ファイル保存", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer148.Add( self.m_button58, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer9.Add( bSizer148, 1, wx.EXPAND, 5 )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,325 ), wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
        self.m_textCtrl1.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "ＭＳ ゴシック" ) )

        bSizer9.Add( self.m_textCtrl1, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer9 )
        self.Layout()

        # Connect Events
        self.m_button58.Bind( wx.EVT_BUTTON, self.OnSaveResult )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnSaveResult( self, event ):
        event.Skip()


###########################################################################
## Class LabelDlg
###########################################################################

class LabelDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"ラベリング", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel79 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,250 ), wx.TAB_TRAVERSAL )
        bSizer11.Add( self.m_panel79, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText125 = wx.StaticText( self, wx.ID_ANY, u"白い部分をラベリング処理する", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText125.Wrap( -1 )

        self.m_staticText125.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

        bSizer11.Add( self.m_staticText125, 0, wx.ALL, 5 )

        bSizer144 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText124 = wx.StaticText( self, wx.ID_ANY, u"ラベリング最小サイズ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText124.Wrap( -1 )

        bSizer144.Add( self.m_staticText124, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl47 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 20000, 50 )
        bSizer144.Add( self.m_spinCtrl47, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer11.Add( bSizer144, 1, wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"プレビュー", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"キャンセル", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnCancel )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnPreView )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnExec )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnCancel( self, event ):
        event.Skip()

    def OnPreView( self, event ):
        event.Skip()

    def OnExec( self, event ):
        event.Skip()



###########################################################################
## Class ContoursDlg
###########################################################################

class ContoursDlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"輪郭化", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook8 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,320 ), 0 )
        self.m_panel81 = wx.Panel( self.m_notebook8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer154 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel84 = wx.Panel( self.m_panel81, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,100 ), wx.TAB_TRAVERSAL )
        bSizer154.Add( self.m_panel84, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText141 = wx.StaticText( self.m_panel81, wx.ID_ANY, u"処理結果は２値画像になる", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText141.Wrap( -1 )

        self.m_staticText141.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

        bSizer154.Add( self.m_staticText141, 0, wx.ALL, 5 )

        gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText138 = wx.StaticText( self.m_panel81, wx.ID_ANY, u"最小しきい値(連続性の大きさ)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText138.Wrap( -1 )

        gSizer10.Add( self.m_staticText138, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl45 = wx.SpinCtrl( self.m_panel81, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 255, 50 )
        gSizer10.Add( self.m_spinCtrl45, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText139 = wx.StaticText( self.m_panel81, wx.ID_ANY, u"最大しきい値(この輝度ならばエッジである)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText139.Wrap( -1 )

        gSizer10.Add( self.m_staticText139, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl46 = wx.SpinCtrl( self.m_panel81, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 255, 150 )
        gSizer10.Add( self.m_spinCtrl46, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText140 = wx.StaticText( self.m_panel81, wx.ID_ANY, u"ゾーベルフィルタのサイズ(3 , 5 , 7のいずれか)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText140.Wrap( -1 )

        gSizer10.Add( self.m_staticText140, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl47 = wx.SpinCtrl( self.m_panel81, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 3, 7, 3 )
        gSizer10.Add( self.m_spinCtrl47, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer154.Add( gSizer10, 1, wx.EXPAND, 5 )


        self.m_panel81.SetSizer( bSizer154 )
        self.m_panel81.Layout()
        bSizer154.Fit( self.m_panel81 )
        self.m_notebook8.AddPage( self.m_panel81, u"Canny", True )
        self.m_panel82 = wx.Panel( self.m_notebook8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer155 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel85 = wx.Panel( self.m_panel82, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,220 ), wx.TAB_TRAVERSAL )
        bSizer155.Add( self.m_panel85, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer153 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText142 = wx.StaticText( self.m_panel82, wx.ID_ANY, u"２値画像しか処理できません", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText142.Wrap( -1 )

        self.m_staticText142.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

        bSizer153.Add( self.m_staticText142, 0, wx.ALL, 5 )

        self.m_staticText1521 = wx.StaticText( self.m_panel82, wx.ID_ANY, u"（findContours関数は、輪郭のベクトルデータを作る関数です）", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1521.Wrap( -1 )

        bSizer153.Add( self.m_staticText1521, 0, wx.ALL, 5 )


        bSizer155.Add( bSizer153, 1, wx.EXPAND, 5 )

        gSizer12 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText144 = wx.StaticText( self.m_panel82, wx.ID_ANY, u"最小面積", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText144.Wrap( -1 )

        gSizer12.Add( self.m_staticText144, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl49 = wx.SpinCtrl( self.m_panel82, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 5000, 50 )
        gSizer12.Add( self.m_spinCtrl49, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer155.Add( gSizer12, 1, wx.EXPAND, 5 )


        self.m_panel82.SetSizer( bSizer155 )
        self.m_panel82.Layout()
        bSizer155.Fit( self.m_panel82 )
        self.m_notebook8.AddPage( self.m_panel82, u"findContours", False )
        self.m_panel851 = wx.Panel( self.m_notebook8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer154 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel87 = wx.Panel( self.m_panel851, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,165 ), wx.TAB_TRAVERSAL )
        bSizer154.Add( self.m_panel87, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText154 = wx.StaticText( self.m_panel851, wx.ID_ANY, u"n回膨張した画像から、n回縮小した画像を引いて輪郭を作る\n繰り返し回数 = 0 の場合は、元画像を用いる", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText154.Wrap( -1 )

        bSizer154.Add( self.m_staticText154, 0, wx.ALL, 5 )

        gSizer121 = wx.GridSizer( 0, 5, 0, 0 )

        self.m_staticText148 = wx.StaticText( self.m_panel851, wx.ID_ANY, u"膨張", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText148.Wrap( -1 )

        gSizer121.Add( self.m_staticText148, 0, wx.ALL, 5 )

        self.m_staticText149 = wx.StaticText( self.m_panel851, wx.ID_ANY, u"カーネルサイズ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText149.Wrap( -1 )

        gSizer121.Add( self.m_staticText149, 0, wx.ALL, 5 )

        self.m_spinCtrl491 = wx.SpinCtrl( self.m_panel851, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 3, 100, 3 )
        gSizer121.Add( self.m_spinCtrl491, 0, wx.ALL, 5 )

        self.m_staticText150 = wx.StaticText( self.m_panel851, wx.ID_ANY, u"繰り返し回数", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText150.Wrap( -1 )

        gSizer121.Add( self.m_staticText150, 0, wx.ALL, 5 )

        self.m_spinCtrl50 = wx.SpinCtrl( self.m_panel851, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 30, 1 )
        gSizer121.Add( self.m_spinCtrl50, 0, wx.ALL, 5 )

        self.m_staticText151 = wx.StaticText( self.m_panel851, wx.ID_ANY, u"縮小", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText151.Wrap( -1 )

        gSizer121.Add( self.m_staticText151, 0, wx.ALL, 5 )

        self.m_staticText152 = wx.StaticText( self.m_panel851, wx.ID_ANY, u"カーネルサイズ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText152.Wrap( -1 )

        gSizer121.Add( self.m_staticText152, 0, wx.ALL, 5 )

        self.m_spinCtrl51 = wx.SpinCtrl( self.m_panel851, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 3, 100, 3 )
        gSizer121.Add( self.m_spinCtrl51, 0, wx.ALL, 5 )

        self.m_staticText153 = wx.StaticText( self.m_panel851, wx.ID_ANY, u"繰り返し回数", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText153.Wrap( -1 )

        gSizer121.Add( self.m_staticText153, 0, wx.ALL, 5 )

        self.m_spinCtrl52 = wx.SpinCtrl( self.m_panel851, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 0, 30, 0 )
        gSizer121.Add( self.m_spinCtrl52, 0, wx.ALL, 5 )


        bSizer154.Add( gSizer121, 1, wx.EXPAND, 5 )


        self.m_panel851.SetSizer( bSizer154 )
        self.m_panel851.Layout()
        bSizer154.Fit( self.m_panel851 )
        self.m_notebook8.AddPage( self.m_panel851, u"モルフォロジー", False )

        bSizer11.Add( self.m_notebook8, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"プレビュー", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"実行", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"キャンセル", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnCancel )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnPreView )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnExec )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnCancel( self, event ):
        event.Skip()

    def OnPreView( self, event ):
        event.Skip()

    def OnExec( self, event ):
        event.Skip()



