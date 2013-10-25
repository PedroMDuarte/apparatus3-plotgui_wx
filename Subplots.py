import wx
import images
import wx.lib.agw.flatnotebook as fnb
import Datasets
########################################################################
class DataTabs(fnb.FlatNotebook):
    """
    Notebook class
    """

    #----------------------------------------------------------------------
    def __init__(self, parent):
        fnb.FlatNotebook.__init__(self, parent, id=wx.ID_ANY, style=
                             wx.BK_DEFAULT
                             #wx.BK_TOP 
                             #wx.BK_BOTTOM
                             #wx.BK_LEFT
                             #wx.BK_RIGHT
                             )

        # Create the first tab and add it to the notebook
        tabOne = Datasets.DatasetPanel(self)
        tabOne.SetBackgroundColour("Gray")
        self.AddPage(tabOne, "TabOne")

        # Show how to put an image on one of the notebook tabs,
        # first make the image list:
        il = wx.ImageList(16, 16)
        idx1 = il.Add(images.Smiles.GetBitmap())
        self.AssignImageList(il)

        # now put an image on the first tab we just created:
        self.SetPageImage(0, idx1)

        # Create and add the second tab
        tabTwo = Datasets.DatasetPanel(self)
        self.AddPage(tabTwo, "TabTwo")

        # Create and add the third tab
        self.AddPage(Datasets.DatasetPanel(self), "TabThree")

        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging)


    def OnPageChanged(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        print 'OnPageChanged,  old:%d, new:%d, sel:%d\n' % (old, new, sel)
        event.Skip()

    def OnPageChanging(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        print 'OnPageChanging, old:%d, new:%d, sel:%d\n' % (old, new, sel)
        event.Skip()
########################################################################
class DataPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, style=wx.CLIP_CHILDREN)
 
        tb = self.BuildToolbar() 

        datatabs = DataTabs( self  ) 
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(tb, 0, wx.ALL | wx.ALIGN_LEFT | wx.EXPAND, 4)
        self.sizer.Add(datatabs, 1, wx.LEFT | wx.BOTTOM | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

    def BuildToolbar( self ) :
        tb = wx.ToolBar( self, -1 )
        self.ToolBar = tb
        tsize=(24,24)
        tb.SetToolBitmapSize( tsize )# this required for non-standard size buttons on MSW

        self.wxId_PLOTME = 25
        plotme = wx.CheckBox(label="plotme?", parent=tb, id=self.wxId_PLOTME,
                             size=wx.Size(80,28))#, (65, 40), (150, 20), wx.NO_BORDER)
        tb.AddControl( control = plotme ) 
        tb.AddSeparator()   # Invisible spacer

        self.wxId_NXDATAS = 50
        self.wxId_NYDATAS = 51

        cbNX = wx.ComboBox(choices=['1', '2', '3'], id=self.wxId_NXDATAS,
              name='cbNX', parent=tb, pos=wx.Point(72, 8), size=wx.Size(50,
              28), style=0, validator=wx.DefaultValidator, value='')
        cbNX.Refresh()
        tb.AddControl(control = cbNX) 

        cbNY = wx.ComboBox(choices=['1', '2', '3'], id=self.wxId_NYDATAS,
              name='cbNY', parent=tb, pos=wx.Point(72, 8), size=wx.Size(50,
              28), style=0, validator=wx.DefaultValidator, value='')
        cbNY.Refresh()
        tb.AddControl(control = cbNY)
 
        subplotName = wx.TextCtrl(value="", parent=tb, id=wx.ID_ANY, size=wx.Size(160,28))
        tb.AddControl(control = subplotName)

        bmp = wx.ArtProvider.GetBitmap( wx.ART_ADD_BOOKMARK, wx.ART_TOOLBAR, tsize)
        tb.AddSimpleTool( 30+1, bmp, "New subplot tab", "New subplot tab" )

        tb.Realize()
        return tb


class SubplotTabs(fnb.FlatNotebook):
    def __init__(self, parent):
        fnb.FlatNotebook.__init__(self, parent, id=wx.ID_ANY, style=
                             wx.BK_DEFAULT
                             #wx.BK_TOP 
                             #wx.BK_BOTTOM
                             #wx.BK_LEFT
                             #wx.BK_RIGHT
                             )

        # Create the first tab and add it to the notebook
        tabOne = DataPanel(self)
        tabOne.SetBackgroundColour("Gray")
        self.AddPage(tabOne, "TabOne")


        # Create and add the second tab
        tabTwo = Datasets.DatasetPanel(self)
        self.AddPage(tabTwo, "TabTwo")

        # Create and add the third tab
        self.AddPage(Datasets.DatasetPanel(self), "TabThree")

        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging)

    def OnPageChanged(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        print 'OnPageChanged,  old:%d, new:%d, sel:%d\n' % (old, new, sel)
        event.Skip()

    def OnPageChanging(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        print 'OnPageChanging, old:%d, new:%d, sel:%d\n' % (old, new, sel)
        event.Skip()

########################################################################
ID_REPLOT_BUTTON     = wx.NewId()

class SubplotPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, style=wx.CLIP_CHILDREN)
 
        tb = self.BuildToolbar() 
        

        subplottabs = SubplotTabs( self  ) 
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(tb, 0, wx.ALL | wx.ALIGN_LEFT | wx.EXPAND, 4)
        self.sizer.Add(subplottabs, 1, wx.LEFT | wx.BOTTOM | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()
    
    def BuildToolbar( self ) :
        tb = wx.ToolBar( self, -1 )
        self.ToolBar = tb
        tsize=(24,24)
        tb.SetToolBitmapSize( tsize )# this required for non-standard size buttons on MSW

        new_bmp =  wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR, tsize)
        open_bmp = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, tsize)
        copy_bmp = wx.ArtProvider.GetBitmap(wx.ART_COPY, wx.ART_TOOLBAR, tsize)

   
        bmp = wx.ArtProvider.GetBitmap( wx.ART_EXECUTABLE_FILE, wx.ART_TOOLBAR, tsize)
        tb.AddSimpleTool( 30+1, bmp, "Replot", "Replot" )
        tb.AddSeparator()   # Invisible spacer

        self.wxId_NXSUBPLOTS = 50
        self.wxId_NYSUBPLOTS = 51

        cbNX = wx.ComboBox(choices=['1', '2', '3'], id=self.wxId_NXSUBPLOTS,
              name='cbNX', parent=tb, pos=wx.Point(72, 8), size=wx.Size(50,
              28), style=0, validator=wx.DefaultValidator, value='')
        cbNX.Refresh()
        tb.AddControl(control = cbNX) 

        cbNY = wx.ComboBox(choices=['1', '2', '3'], id=self.wxId_NYSUBPLOTS,
              name='cbNY', parent=tb, pos=wx.Point(72, 8), size=wx.Size(50,
              28), style=0, validator=wx.DefaultValidator, value='')
        cbNY.Refresh()
        tb.AddControl(control = cbNY) 

        bmp = wx.ArtProvider.GetBitmap( wx.ART_ADD_BOOKMARK, wx.ART_TOOLBAR, tsize)
        tb.AddSimpleTool( 30+1, bmp, "New subplot tab", "New subplot tab" )

        bmp = wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_TOOLBAR, tsize)
        tb.AddSimpleTool( 30+1, bmp, "Save subplot tab", "Save subplot tab" )

        bmp = wx.ArtProvider.GetBitmap( wx.ART_FILE_OPEN, wx.ART_TOOLBAR, tsize)
        tb.AddSimpleTool( 30+1, bmp, "Load subplot tab", "Load subplot tab" )
        tb.Realize()
        return tb
