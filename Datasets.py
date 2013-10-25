import wx
import images
import wx.lib.scrolledpanel as scrolled
########################################################################

class SetPanel(scrolled.ScrolledPanel):
    """
    This will be the first notebook tab
    """
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """"""
        super(SetPanel, self).__init__(parent=parent, id=wx.ID_ANY)

        panel = self

        borderbox = wx.BoxSizer(wx.VERTICAL)

        #### PLOT SECTION
        sb = wx.StaticBox(panel, label="  Dataset  ")
        vbox = wx.StaticBoxSizer(sb,wx.VERTICAL)
        fgs = wx.FlexGridSizer(2, 5, 7, 15)
        plotB   =  wx.CheckBox(panel, label="plot?")
        x2B     =  wx.CheckBox(panel, label="X2?")
        y2B     =  wx.CheckBox(panel, label="Y2?")
        statsB  =  wx.CheckBox(panel, label="stats?")
        gridB   =  wx.CheckBox(panel, label="grid?")
        logxB   =  wx.CheckBox(panel, label="logx?")
        logyB   =  wx.CheckBox(panel, label="logy?")
        xticksB =  wx.CheckBox(panel, label="xticks?")
        yticksB =  wx.CheckBox(panel, label="yticks?")
        fgs.AddMany([(plotB), (x2B), (y2B), (statsB), (gridB),
                     (logxB), (logyB), (xticksB), (yticksB) ])

        #fgs.AddGrowableRow(2, 1)
        #fgs.AddGrowableCol(1, 1)
        vbox.Add(fgs, proportion=0, flag=wx.TOP|wx.LEFT|wx.RIGHT|wx.EXPAND, border=5)

        fgs2 = wx.FlexGridSizer(3, 2, 9, 15)
        datname = wx.StaticText(panel, label="Name")
        datdesc = wx.StaticText(panel, label="Description")
        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        fgs2.AddMany([(datname), (tc1, 1, wx.EXPAND), (datdesc), 
            (tc2, 1, wx.EXPAND)])
        fgs2.AddGrowableRow(1, 1)
        fgs2.AddGrowableCol(1, 1)
        vbox.Add(fgs2, proportion=1, flag=wx.TOP|wx.LEFT|wx.RIGHT|wx.EXPAND, border=5)

        borderbox.Add( vbox, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)


        #### DATA SECTION
        sb2 = wx.StaticBox(panel, label="  Data  ")
        vbox2 = wx.StaticBoxSizer(sb2,wx.VERTICAL)
        fgs3 = wx.FlexGridSizer(4, 2, 9, 15)
        datdir   = wx.StaticText(panel, label="DataDir")
        datrange = wx.StaticText(panel, label="Range")
        datxkey  = wx.StaticText(panel, label="X")
        datykey  = wx.StaticText(panel, label="Y")
        td1 = wx.TextCtrl(panel)
        td2 = wx.TextCtrl(panel)
        td3 = wx.TextCtrl(panel)
        td4 = wx.TextCtrl(panel)
        fgs3.AddMany([(datdir), (td1, 1, wx.EXPAND), 
                      (datrange), (td2, 1, wx.EXPAND),
                      (datxkey), (td3, 1, wx.EXPAND),
                      (datykey), (td4, 1, wx.EXPAND)
                     ])
        fgs3.AddGrowableCol(1, 1)
        vbox2.Add(fgs3, proportion=1, flag=wx.TOP|wx.LEFT|wx.RIGHT|wx.EXPAND, border=5)

        borderbox.Add( vbox2, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)


        #### optORATIONS
        sb3 = wx.StaticBox(panel, label="  Plot Options  ")
        vbox3 = wx.StaticBoxSizer(sb3,wx.VERTICAL) 
        
        fgs4 = wx.FlexGridSizer(2, 6, 9, 15)
        optxlab = wx.StaticText(panel, label="Xl")
        optxmin = wx.StaticText(panel, label="Xmin")
        optxmax = wx.StaticText(panel, label="Xmax")

        optylab = wx.StaticText(panel, label="Yl")
        optymin = wx.StaticText(panel, label="Ymin")
        optymax = wx.StaticText(panel, label="Ymax")

        topt1 = wx.TextCtrl(panel)
        topt2 = wx.TextCtrl(panel)
        topt3 = wx.TextCtrl(panel)
        topt4 = wx.TextCtrl(panel)
        topt5 = wx.TextCtrl(panel)
        topt6 = wx.TextCtrl(panel)

        fgs4.AddMany([
         (optxlab), (topt1, 2, wx.EXPAND), (optxmin), (topt2), (optxmax), (topt3),
         (optylab), (topt4, 2, wx.EXPAND), (optymin), (topt5), (optymax), (topt6)])
        fgs4.AddGrowableCol(1, 1)
        vbox3.Add(fgs4, proportion=1, flag=wx.TOP|wx.LEFT|wx.RIGHT|wx.EXPAND, border=5)

        fgs5 = wx.FlexGridSizer(1, 2, 9, 15)
        optleg = wx.StaticText(panel, label="Legend")
        topt7 = wx.TextCtrl(panel)
        fgs5.AddMany([(optleg), (topt7, 1, wx.EXPAND)])
        fgs5.AddGrowableCol(1, 1)
        vbox3.Add(fgs5, proportion=0, flag=wx.TOP|wx.LEFT|wx.RIGHT|wx.EXPAND, border=5)

        fgs6 = wx.FlexGridSizer(2,6, 9, 15)
        optec  = wx.StaticText(panel, label="ec")
        optfc  = wx.StaticText(panel, label="fc")
        optfmt = wx.StaticText(panel, label="fmt")
        optms  = wx.StaticText(panel, label="ms")
        optmew = wx.StaticText(panel, label="mew")
        dummy = wx.StaticText(panel, label="")

        topt8 = wx.TextCtrl(panel)
        topt9 = wx.TextCtrl(panel)
        topt10 = wx.TextCtrl(panel)
        topt11 = wx.TextCtrl(panel)
        topt12 = wx.TextCtrl(panel)
        matchB =  wx.CheckBox(panel, label="match?")
        fgs6.AddMany([(optec), (topt8, 1, wx.EXPAND),
                      (optfc), (topt9, 1, wx.EXPAND),
                      (matchB), (dummy),
                      (optfmt), (topt10, 1, wx.EXPAND),
                      (optms), (topt11, 1, wx.EXPAND),
                      (optmew), (topt12, 1, wx.EXPAND),
                      ])
        #fgs6.AddGrowableCol(1, 1)
        vbox3.Add(fgs6, proportion=0, flag=wx.TOP|wx.LEFT|wx.RIGHT|wx.EXPAND, border=5)

        borderbox.Add( vbox3, proportion=0, flag=wx.ALL|wx.EXPAND, border=5)

        panel.SetSizer(borderbox)
        panel.SetAutoLayout(1)
        panel.SetupScrolling()

        ##################3

        ###panel = self
        ###
        ###sizer = wx.GridBagSizer(5, 5)

        ###line = wx.StaticLine(panel)
        ###sizer.Add(line, pos=(1, 0), span=(1, 5), 
        ###    flag=wx.EXPAND|wx.BOTTOM, border=10)

        ###text2 = wx.StaticText(panel, label="Name")
        ###sizer.Add(text2, pos=(0, 0), flag=wx.LEFT|wx.TOP, border=10)

        ###tc1 = wx.TextCtrl(panel)
        ###sizer.Add(tc1, pos=(0, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND, border=10)

        ###text3 = wx.StaticText(panel, label="Package")
        ###sizer.Add(text3, pos=(3, 0), flag=wx.LEFT|wx.TOP, border=10)

        ###tc2 = wx.TextCtrl(panel)
        ###sizer.Add(tc2, pos=(3, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND, 
        ###    border=5)

        ###button1 = wx.Button(panel, label="Browse...")
        ###sizer.Add(button1, pos=(3, 4), flag=wx.TOP|wx.RIGHT, border=5)

        ###text4 = wx.StaticText(panel, label="Extends")
        ###sizer.Add(text4, pos=(4, 0), flag=wx.TOP|wx.LEFT, border=10)

        ###combo = wx.ComboBox(panel)
        ###sizer.Add(combo, pos=(4, 1), span=(1, 3), 
        ###    flag=wx.TOP|wx.EXPAND, border=5)

        ###button2 = wx.Button(panel, label="Browse...")
        ###sizer.Add(button2, pos=(4, 4), flag=wx.TOP|wx.RIGHT, border=5)

        ###sb = wx.StaticBox(panel, label="Optional Attributes")

        ###boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        ###boxsizer.Add(wx.CheckBox(panel, label="Public"), 
        ###    flag=wx.LEFT|wx.TOP, border=5)
        ###boxsizer.Add(wx.CheckBox(panel, label="Generate Default Constructor"),
        ###    flag=wx.LEFT, border=5)
        ###boxsizer.Add(wx.CheckBox(panel, label="Generate Main Method"), 
        ###    flag=wx.LEFT|wx.BOTTOM, border=5)
        ###sizer.Add(boxsizer, pos=(5, 0), span=(1, 5), 
        ###    flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)

        ###button3 = wx.Button(panel, label='Help')
        ###sizer.Add(button3, pos=(7, 0), flag=wx.LEFT, border=10)

        ###button4 = wx.Button(panel, label="Ok")
        ###sizer.Add(button4, pos=(7, 3))

        ###button5 = wx.Button(panel, label="Cancel")
        ###sizer.Add(button5, pos=(7, 4), span=(1, 1),  
        ###    flag=wx.BOTTOM|wx.RIGHT, border=5)

        ###sizer.AddGrowableCol(2)
        ###
        ###panel.SetSizer(sizer)

        #sizer = wx.BoxSizer(wx.VERTICAL)
        #txtOne = wx.TextCtrl(self, wx.ID_ANY, "")
        #txtTwo = wx.TextCtrl(self, wx.ID_ANY, "")
        #bPlot = wx.Button(self, wx.ID_ANY, "Plot", (50,50)) 
        #self.Bind(wx.EVT_BUTTON, self.OnButton, bPlot) 

        #sizer = wx.BoxSizer(wx.VERTICAL)
        #sizer.Add(txtOne, 0, wx.ALL, 5)
        #sizer.Add(txtTwo, 0, wx.ALL, 5)

        #self.SetSizer(sizer)
    def OnButton(self, evt):
        print "I want to plot something"

class RawDataPanel(wx.Panel):
    """
    This will hold the raw data text output
    """
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """"""
        super(RawDataPanel, self).__init__(parent=parent, id=wx.ID_ANY)
        panel = self

        borderbox = wx.BoxSizer(wx.VERTICAL)
        tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        borderbox.Add( tc2, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)

        sb2 = wx.StaticBox(panel, label="  Save Raw Data  ")
        borderbox.Add( sb2, proportion=0, flag=wx.ALL|wx.EXPAND, border=5)

class InfoPanel(wx.Panel):
    """
    This will hold the info text output
    """
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """"""
        super(InfoPanel, self).__init__(parent=parent, id=wx.ID_ANY)
        panel = self

        borderbox = wx.BoxSizer(wx.VERTICAL)
        tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        borderbox.Add( tc2, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)

        sb2 = wx.StaticBox(panel, label="  Hello  ")
        borderbox.Add( sb2, proportion=0, flag=wx.ALL|wx.EXPAND, border=5)

class DatasetPanel(wx.Notebook):
    """
    This will be the Dataset notebook
    """
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """"""
        super(DatasetPanel, self).__init__(parent=parent, id=wx.ID_ANY,
                                      style = wx.BK_DEFAULT )

        tabOne = SetPanel(self) 
        self.AddPage(tabOne,"Set")

        tabTwo = RawDataPanel(self)
        self.AddPage(tabTwo,"Raw Data") 

        tabThree = InfoPanel(self)
        self.AddPage(tabThree,"Info") 

       

