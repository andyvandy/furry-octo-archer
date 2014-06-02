# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 26 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1167,616 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL, name = u"The Amazing Grapher" )
		
		self.SetSizeHintsSz( wx.Size( 1100,600 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 77, 167, 183 ) )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_file = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_file, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_file.AppendItem( self.m_menuItem2 )
		
		self.m_menuItem3 = wx.MenuItem( self.m_file, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_file.AppendItem( self.m_menuItem3 )
		
		self.m_file.AppendSeparator()
		
		self.m_file_quit = wx.MenuItem( self.m_file, wx.ID_EXIT, u"Quit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_file.AppendItem( self.m_file_quit )
		
		self.m_menubar1.Append( self.m_file, u"File" ) 
		
		self.m_edit = wx.Menu()
		self.m_edit_piss = wx.MenuItem( self.m_edit, wx.ID_ANY, u"I ain't ready yet", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_edit.AppendItem( self.m_edit_piss )
		
		self.m_menubar1.Append( self.m_edit, u"Edit" ) 
		
		self.m_about = wx.Menu()
		self.m_about_about = wx.MenuItem( self.m_about, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_about.AppendItem( self.m_about_about )
		
		self.m_menubar1.Append( self.m_about, u"About" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Parameters" ), wx.VERTICAL )
		
		gbSizer6 = wx.GridBagSizer( 0, 0 )
		gbSizer6.SetFlexibleDirection( wx.BOTH )
		gbSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		m_functionscomboChoices = []
		self.m_functionscombo = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_functionscomboChoices, 0 )
		gbSizer6.Add( self.m_functionscombo, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_savecheck = wx.CheckBox( self, wx.ID_ANY, u"save?", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.m_savecheck, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Img name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gbSizer6.Add( self.m_staticText2, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_textCtrl_filename = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.m_textCtrl_filename, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		sbSizer1.Add( gbSizer6, 1, wx.EXPAND, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText_field1 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_field1.Wrap( -1 )
		fgSizer1.Add( self.m_staticText_field1, 0, wx.ALL, 5 )
		
		self.m_textCtrl_field1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl_field1, 0, wx.ALL, 5 )
		
		self.m_staticText_field2 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_field2.Wrap( -1 )
		fgSizer1.Add( self.m_staticText_field2, 0, wx.ALL, 5 )
		
		self.m_textCtrl_field2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl_field2, 0, wx.ALL, 5 )
		
		self.m_staticText_field3 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_field3.Wrap( -1 )
		fgSizer1.Add( self.m_staticText_field3, 0, wx.ALL, 5 )
		
		self.m_textCtrl_field3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl_field3, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( fgSizer1, 1, wx.ALIGN_LEFT, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_checkBox4 = wx.CheckBox( self, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_checkBox4, 0, wx.ALL, 5 )
		
		self.m_checkBox5 = wx.CheckBox( self, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_checkBox5, 0, wx.ALL, 5 )
		
		self.m_checkBox6 = wx.CheckBox( self, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_checkBox6, 0, wx.ALL, 5 )
		
		self.m_checkBox7 = wx.CheckBox( self, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_checkBox7, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( fgSizer2, 1, wx.ALIGN_RIGHT, 5 )
		
		
		sbSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		gbSizer3.SetMinSize( wx.Size( 200,-1 ) ) 
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.m_button3, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.m_button2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		sbSizer1.Add( gbSizer3, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( sbSizer1, 1, wx.ALL, 5 )
		
		
		gbSizer1.Add( bSizer1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.m_canvas = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_canvas.SetMinSize( wx.Size( 200,200 ) )
		
		gbSizer1.Add( self.m_canvas, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		
		gbSizer1.AddGrowableCol( 1 )
		gbSizer1.AddGrowableRow( 0 )
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		self.m_statusBar2 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
	
	def __del__( self ):
		pass
	

