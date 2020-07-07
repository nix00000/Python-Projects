import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from data_comp import Data
from finman import FinMan as Fin
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

LARGE_FONT = ("Verdana", 14)
print("testing")

class Business(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.iconbitmap(self,'finance_icon.ico')
        tk.Tk.title(self, "OOP GUI")
        tk.Tk.geometry(self,"1360x720")
        minh = 800
        minw = 600
        tk.Tk.minsize(self,minh,minw)
        container = tk.Frame(self)

        container.pack(side="top",fill = "both", expand = True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for f in (StartPage, PageOne,PageTwo):
            frame = f(container,self)
            self.frames[f] = frame
            frame.grid(row=0, column = 0, sticky="nsew")

        self.show_frame(StartPage)
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text = """
        This is a Beta application. The infomration presented here may be faulty.
        Use the application at your own risk. This project is for practice purposes only.
        I am not responsible for any financial losses resulting from the use of this app""",font=LARGE_FONT)
        label.pack(pady = 10, padx=10)
        butt1 = ttk.Button(self, text = "Agree",command = lambda: controller.show_frame(PageOne))
        butt1.pack()
        butt1 = ttk.Button(self, text="Exit", command=self.quit)
        butt1.pack()

class PageOne(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        newframe1 = tk.Frame(self)

        label = tk.Label(newframe1, text="Stocks", font=LARGE_FONT)
        label.grid(row=0,column = 0)

        butt1 = ttk.Button(newframe1, text="Financial Management",width = 20, command=lambda: controller.show_frame(PageTwo))
        butt1.grid(row = 0,column = 1) #row = 0, column =

        newframe1.grid(row = 0,column = 0)

        newframe2= tk.Frame(self)
        # Stocks
        src_lbl = tk.Label(newframe2, text = "Search a Company:")
        src_lbl.grid(row = 2,column = 0)
        src_lbl.config(font=("Verdana", 18))
        src = tk.Entry(newframe2,width = 20,borderwidth = 5,font=("Verdana", 16))
        src.grid(row = 2,column = 1,pady = 20)
        btn_sub = tk.Button(newframe2, text="Submit", width=20,bg = "blue",fg="white", command=lambda:self.info(src))
        btn_sub.grid(row = 3,column = 1)

        newframe2.grid(row=1, column=0)
        newframe2.columnconfigure(0, weight=3)


    def info(self,s):

        global stats
        global graph
        global toolbar
        global cmp_lbl
        global tbtn1
        global tbtn2
        global tbtn3
        global tbtn4


        self.forget()
        self.forgetData()
        rez = Data()
        ands = rez.company(s.get())
        if ands == -1:
            err = mb.showerror("No results","There are no companies found under that name")
        elif len(ands) == 1:
            company = rez.companyFinal(ands[0][0])
            cmp_lbl = tk.Label(self, text=company, font=("Verdana", 18))
            cmp_lbl.grid(row=3, column=0,pady = 30)
            res = rez.getData(ands[0][0])

            try:
                stats = tk.Label(self, text="Last Open \n" + res["Open"].tail(1).to_string(index = False,header = 0) + "\n\n"+
                             "Last Close \n" +res["Close"].tail(1).to_string(index = False,header = 0) + "\n\n"+
                             "High \n" +res["High"].tail(1).to_string(index = False,header = 0) + "\n\n"+
                             "Low \n" +res["Low"].tail(1).to_string(index = False,header = 0) + "\n\n"+
                             "Volume \n" +res["Volume"].tail(1).to_string(index = False,header = 0), font=("Verdana", 16))
                stats.grid(row=4,column = 0)

                f = Figure(figsize=(7, 4), dpi=100)
                a = f.add_subplot(111)

                a.plot(res["High"], "g", label="High")
                a.plot(res["Low"], "r", label="Low")

                a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)
                title = "Stock prices"
                a.set_title(title)

                newfeame3 = tk.Frame(self)
                canvas = FigureCanvasTkAgg(f, newfeame3)
                canvas.draw()

                try:
                    graph = canvas.get_tk_widget()
                    canvas._tkcanvas.pack()
                    toolbar = NavigationToolbar2Tk(canvas,newfeame3)
                    toolbar.update()
                    newfeame3.grid(row = 4, column = 2)

                except:
                    graph = canvas.get_tk_widget()
                    graph.grid(row = 4, column = 2)
            except:
                mb.showerror("Fatal Error","Something went wrong... \n Check internet connection")

        else:

            if len(ands) == 2:
                tbtn1 = tk.Button(self, text=ands[0][0] + " - " + ands[0][1], command=lambda s=ands[0][0]: self.finalinfo(s))
                tbtn1.grid(column=0, pady=10)

                tbtn2 = tk.Button(self, text=ands[1][0] + " - " + ands[1][1], command=lambda s=ands[1][0]: self.finalinfo(s))
                tbtn2.grid(column=0, pady=10)
            if len(ands) == 3:
                tbtn1 = tk.Button(self, text=ands[0][0] + " - " + ands[0][1], command=lambda s=ands[0][0]: self.finalinfo(s))
                tbtn1.grid(column=0, pady=10)

                tbtn2 = tk.Button(self, text=ands[1][0] + " - " + ands[1][1], command=lambda s=ands[1][0]: self.finalinfo(s))
                tbtn2.grid(column=0, pady=10)

                tbtn3 = tk.Button(self, text=ands[2][0] + " - " + ands[2][1],command=lambda s=ands[2][0]: self.finalinfo(s))
                tbtn3.grid(column=0, pady=10)
            if len(ands) == 4:
                tbtn1 = tk.Button(self, text=ands[0][0] + " - " + ands[0][1], command=lambda s=ands[0][0]: self.finalinfo(s))
                tbtn1.grid(column=0, pady=10)

                tbtn2 = tk.Button(self, text=ands[1][0] + " - " + ands[1][1], command=lambda s=ands[1][0]: self.finalinfo(s))
                tbtn2.grid(column=0, pady=10)

                tbtn3 = tk.Button(self, text=ands[2][0] + " - " + ands[2][1],command=lambda s=ands[2][0]: self.finalinfo(s))
                tbtn3.grid(column=0, pady=10)

                tbtn4 = tk.Button(self, text=ands[3][0] + " - " + ands[3][1],command=lambda s=ands[3][0]: self.finalinfo(s))
                tbtn4.grid(column=0, pady=10)


    def finalinfo(self,s):
        global stats
        global graph
        global cmp_lbl
        global toolbar
        self.forget()
        self.forgetData()
        res = Data()
        ret = res.getData(s)
        try:
            company = res.companyFinal(s)
            cmp_lbl = tk.Label(self, text=company, font=("Verdana", 18))
            cmp_lbl.grid(row=3, column=0,pady= 20)

            stats = tk.Label(self, text="Last Open \n" + ret["Open"].tail(1).to_string(index = False,header = 0) + "\n\n"+
                             "Last Close \n" +ret["Close"].tail(1).to_string(index = False,header = 0) + "\n\n"+
                             "High \n" +ret["High"].tail(1).to_string(index = False,header = 0) + "\n\n"+
                             "Low \n" +ret["Low"].tail(1).to_string(index = False,header = 0) + "\n\n"+
                             "Volume \n" +ret["Volume"].tail(1).to_string(index = False,header = 0), font=("Verdana", 16))
            stats.grid(row=4, column=0)

            f = Figure(figsize=(7, 4), dpi=100)
            a = f.add_subplot(111)
            a.plot(ret["High"], "g", label="High")
            a.plot(ret["Low"], "r", label="Low")

            a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)
            title = "Stock prices"
            a.set_title(title)

            newfeame3 = tk.Frame(self)
            canvas = FigureCanvasTkAgg(f, newfeame3)
            canvas.draw()

            try:
                graph = canvas.get_tk_widget()
                canvas._tkcanvas.pack()
                toolbar = NavigationToolbar2Tk(canvas, newfeame3)
                toolbar.update()
                newfeame3.grid(row=4, column=2)

            except:
                graph = canvas.get_tk_widget()
                graph.grid(row=4, column=2)
        except:
            mb.showerror("Fatal Error", "Something went frong... \n check wifi connection")


    def forget(self):
        global tbtn1
        global tbtn2
        global tbtn3
        global tbtn4

        try:
            tbtn1.grid_forget()
        except:
            pass
        try:
            tbtn2.grid_forget()
        except:
            pass
        try:
            tbtn3.grid_forget()
        except:
            pass
        try:
            tbtn4.grid_forget()
        except:
            pass

    def forgetData(self):
        global stats
        global graph
        global cmp_lbl
        global toolbar
        try:
            stats.destroy()
        except:
            pass
        try:
            cmp_lbl.destroy()
        except:
            pass
        try:
            graph.destroy()
            toolbar.destroy()
        except:
            pass



class PageTwo(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        global manframe2
        global manframe3
        global subcalc1
        global resultFrame
        global wccresprint
        global rtresFrame

        # Main frame
        manframe1 = tk.Frame(self)
        label = tk.Label(manframe1, text="Finanical Management", font=LARGE_FONT,bd = 1)
        label.grid(row=0, column=1, columnspan=2)
        butt1 = ttk.Button(manframe1, text="Stocks",width = 20, command=lambda: controller.show_frame(PageOne))
        butt1.grid(row = 0, column = 3,sticky="nsew",padx = 20)
        manframe1.grid(row = 0, column = 0)

        # Investments
        investFrame = tk.Frame(self,height = 300,width = 400)

        btnframe = tk.Frame(investFrame)
        lbl1 = tk.Label(btnframe, text="Investments",font = ("Verdana", 18))
        lbl1.grid(row=0, column=1)

        r = tk.IntVar()
        r.set(0)
        btn_pp = tk.Radiobutton(btnframe,text = "PP",variable = r , value = 0, command = lambda:self.options(r.get()),font = ("Verdana", 12)) #variable = r , value = 1, command = lambda:clicked(r.get())
        btn_arr = tk.Radiobutton(btnframe,text = "ARR",variable = r , value = 1, command = lambda:self.options(r.get()),font = ("Verdana", 12))
        btn_npv = tk.Radiobutton(btnframe,text = "NPV",variable = r , value = 2, command = lambda:self.options(r.get()),font = ("Verdana", 12))
        btn_pp.grid(row= 1, column = 0)
        btn_arr.grid(row = 1, column = 1, padx = 5)
        btn_npv.grid(row = 1, column = 2)
        btnframe.grid(row = 1, column = 0,pady = 10)

        manframe2 = tk.Frame(investFrame)
        lblnm = tk.Label(manframe2, text="Payback Period", font=("Verdana", 12,"bold"))
        lblnm.grid(row=1, column=0)

        lblentpp1 = tk.Label(manframe2, text="Enter Investment Amount: ", font=("Verdana", 12))
        entpp1 = tk.Entry(manframe2, width=10, font=("Verdana", 12))
        lblentpp1.grid(row=2, column=0)
        entpp1.grid(row=2, column=1)

        lblentpp2 = tk.Label(manframe2, text="Enter Cash Flows" + '\n' + "(comma separated)", font=("Verdana", 12))
        entpp2 = tk.Entry(manframe2, font=("Verdana", 12))
        lblentpp2.grid(row=3, column=0)
        entpp2.grid(row=3, column=1)

        ratelbl = tk.Label(manframe2)
        ratelbl.grid(row=4, column=0)

        subcalc1 = tk.Button(manframe2, text="Submit", bg="lightgreen",command=lambda: self.hadlepp(entpp1.get(), entpp2.get()))
        subcalc1.grid(row=5, column=0, columnspan=2, ipadx=50, pady=6)

        # Manframe, Invest frame end
        manframe2.grid(row = 2, column = 0,fill=None)
        investFrame.grid(row = 1, column = 0,pady = 10,padx = 10)
        investFrame.grid_propagate(0)

        resultFrame = tk.Frame(self, height=200, width=470, bg="white", border=5, relief="sunken")
        resultFrame.grid(row = 2, column = 0,padx = 30)
        resultFrame.grid_rowconfigure(0, minsize=200, weight=1)
        resultFrame.grid_columnconfigure(0, minsize=470, weight=1)
        resultFrame.grid_propagate(0)

        #WACC
        waccframe = tk.Frame(self)
        # vf,vs,vb,rs,rb,wacc
        wacclbl1 = tk.Label(waccframe, text="WACC calculations", font=("Verdana", 18))
        wacclbl1.grid(row=0, column=0, columnspan = 2,pady=10)

        vslbl = tk.Label(waccframe, text="Total Equity:", font=("Verdana", 12))
        vs = tk.Entry(waccframe,width = 10, font=("Verdana", 12))
        vslbl.grid(row=2, column=0, pady=7)
        vs.grid(row=2, column=1, pady=7)

        vblbl = tk.Label(waccframe, text="Total Debt:", font=("Verdana", 12))
        vb = tk.Entry(waccframe,width = 10, font=("Verdana", 12))
        vblbl.grid(row=3, column=0, pady=7)
        vb.grid(row=3, column=1, pady=7)

        rslbl = tk.Label(waccframe, text="Rate of Equity(%):", font=("Verdana", 12))
        rs = tk.Entry(waccframe,width = 10, font=("Verdana", 12))
        rslbl.grid(row=4, column=0, pady=7)
        rs.grid(row=4, column=1, pady=7)

        rblbl = tk.Label(waccframe, text="Rate of Debt(%):", font=("Verdana", 12))
        rb = tk.Entry(waccframe,width = 10, font=("Verdana", 12))
        rblbl.grid(row=5, column=0, pady=3)
        rb.grid(row=5, column=1, pady=3)

        txlbl = tk.Label(waccframe, text="Tax rate (%):", font=("Verdana", 12))
        tax = tk.Entry(waccframe,width = 10, font=("Verdana", 12))
        txlbl.grid(row=6, column=0, pady=3)
        tax.grid(row=6, column=1, pady=3)


        waccbtn = tk.Button(waccframe, text="Submit", bg="lightgreen",command=lambda: self.handlewacc( vs.get(),vb.get(),rs.get(),rb.get(),tax.get()))                                                                          # vf,vs,vb,rs,rb,wacc
        waccbtn.grid(row=7, column=0, columnspan = 2, pady=7,ipadx = 50)

        waccframe.grid(row = 1, column = 1, padx=80)
        #WACC RESULTS
        wccresprint = tk.Frame(self,height = 200, width = 250, bg ="white",border = 5, relief = "sunken")
        wccresprint.grid(row = 2, column = 1)
        wccresprint.grid_rowconfigure(0, minsize=200, weight=1)
        wccresprint.grid_columnconfigure(0, minsize=250, weight=1)
        wccresprint.grid_propagate(0)

        # Ratios
        ratioFrame = tk.Frame(self)

        # Option Buttons

        btnframe2 = tk.Frame(ratioFrame)
        lbl1 = tk.Label(btnframe2, text="Ratios", font=("Verdana", 18))
        lbl1.grid(row=0, column=1)

        p = tk.IntVar()
        p.set(0)
        btn_liq = tk.Radiobutton(btnframe2, text="Liquidity", variable=p, value=0, command=lambda: self.optrat(p.get()),
                                font=("Verdana", 12))  # variable = r , value = 1, command = lambda:clicked(r.get())
        btn_prof = tk.Radiobutton(btnframe2, text="Leverage", variable=p, value=1, command=lambda: self.optrat(p.get()),
                                 font=("Verdana", 12))
        btn_leve = tk.Radiobutton(btnframe2, text="Profitability", variable=p, value=2, command=lambda: self.optrat(p.get()),
                                 font=("Verdana", 12))

        btn_liq.grid(row=1, column=0)
        btn_prof.grid(row=1, column=1, padx=5)
        btn_leve.grid(row=1, column=2)
        btnframe2.grid(row=1, column=0, pady=5)

        # Main Frame 3

        global rtlbl, rtlbl1, rtlbl2, rtlbl3, rtlbl4,rtlbl5
        global rtent1, rtent2, rtent3, rtent4, rtent5, ratsub1
        manframe3 = tk.Frame(ratioFrame,height = 200, width = 300)
        rtlbl = tk.Label(manframe3, text="Liquidity", font=("Verdana", 12, "bold"))
        rtlbl.grid(row=1, column=0, pady=3)

        rtlbl1 = tk.Label(manframe3, text="Current Assets: ", font=("Verdana", 12))
        rtent1 = tk.Entry(manframe3, width=10, font=("Verdana", 12))
        rtlbl1.grid(row=2, column=0, pady=3)
        rtent1.grid(row=2, column=1, pady=3)

        rtlbl2 = tk.Label(manframe3, text="Current Liabilities: ", font=("Verdana", 12))
        rtent2 = tk.Entry(manframe3, width=10, font=("Verdana", 12))
        rtlbl2.grid(row=3, column=0, pady=3)
        rtent2.grid(row=3, column=1, pady=3)

        rtlbl3 = tk.Label(manframe3, text="Inventory: ", font=("Verdana", 12))
        rtent3 = tk.Entry(manframe3, width=10, font=("Verdana", 12))
        rtlbl3.grid(row=4, column=0, pady=3)
        rtent3.grid(row=4, column=1, pady=3)

        rtlbl4 = tk.Label(manframe3)
        rtlbl4.grid(row=5, column=0, pady=3)

        rtlbl5 = tk.Label(manframe3)
        rtlbl5.grid(row=6, column=0, pady=3)

        ratsub1 = tk.Button(manframe3, text="Submit", bg="lightgreen",
                            command=lambda: self.liquid(rtent1.get(), rtent2.get(), rtent3.get()))
        ratsub1.grid(row=7, column=0, columnspan=2, ipadx=50, pady=6)
        manframe3.grid(row=2, column=0)


        ratioFrame.grid(row=1, column=2,padx = 40)
        rtresFrame = tk.Frame(self,height = 200, width = 300, bg = "white",border = 5, relief = "sunken")
        rtresFrame.grid(row=2, column=2)
        rtresFrame.grid_rowconfigure(0, minsize=200, weight=1)
        rtresFrame.grid_columnconfigure(0, minsize=300, weight=1)
        rtresFrame.grid_propagate(0)

    def optrat(self,n):
        self.forgetting2()
        self.forgetrezs()

        global rtlbl, rtlbl1, rtlbl2, rtlbl3, rtlbl4,rtlbl5
        global rtent1, rtent2, rtent3, rtent4,rtent5, ratsub1
        # rtlbl rtlbl1 rtlbl2 rtlbl3 rtent1 rtent1 rtent2 rtent3 ratsub1 ratsub1

        if n == 0:
            rtlbl = tk.Label(manframe3, text="Liquidity",font = ("Verdana", 12, "bold"))
            rtlbl.grid(row=1, column=0, pady=3)

            rtlbl1 = tk.Label(manframe3, text="Current Assets: ",font = ("Verdana", 12))
            rtent1 = tk.Entry(manframe3, width = 10,font = ("Verdana", 12))
            rtlbl1.grid(row=2, column=0, pady=3)
            rtent1.grid(row=2, column=1, pady=3)

            rtlbl2 = tk.Label(manframe3, text="Current Liabilities: ",font = ("Verdana", 12))
            rtent2 = tk.Entry(manframe3, width=10,font = ("Verdana", 12))
            rtlbl2.grid(row=3, column=0, pady=3)
            rtent2.grid(row=3, column=1, pady=3)

            rtlbl3 = tk.Label(manframe3, text="Inventory: ", font=("Verdana", 12))
            rtent3 = tk.Entry(manframe3, width=10, font=("Verdana", 12))
            rtlbl3.grid(row=4, column=0, pady=3)
            rtent3.grid(row=4, column=1, pady=3)

            rtlbl4 = tk.Label(manframe3)
            rtlbl4.grid(row=5, column=0, pady=3)
            rtlbl5 = tk.Label(manframe3)
            rtlbl5.grid(row=6, column=0, pady=3)

            ratsub1 = tk.Button(manframe3,text ="Submit",bg = "lightgreen", command = lambda: self.liquid(rtent1.get(),rtent2.get(),rtent3.get()))
            ratsub1.grid(row=7, column=0,columnspan = 2,ipadx = 50,pady = 6)
        elif n == 1:
            rtlbl = tk.Label(manframe3, text="Leverage", font=("Verdana", 12, "bold"))
            rtlbl.grid(row=1, column=0, pady=3)

            rtlbl1 = tk.Label(manframe3, text="Total Debt: ", font=("Verdana", 12))
            rtent1 = tk.Entry(manframe3, width=10, font=("Verdana", 12))
            rtlbl1.grid(row=2, column=0, pady=3)
            rtent1.grid(row=2, column=1, pady=3)

            rtlbl2 = tk.Label(manframe3, text="Total Equity: ", font=("Verdana", 12))
            rtent2 = tk.Entry(manframe3, width=10, font=("Verdana", 12))
            rtlbl2.grid(row=3, column=0, pady=3)
            rtent2.grid(row=3, column=1, pady=3)

            rtlbl3 = tk.Label(manframe3, text="Total Assets: ", font=("Verdana", 12))
            rtent3 = tk.Entry(manframe3, width=10, font=("Verdana", 12))
            rtlbl3.grid(row=4, column=0, pady=3)
            rtent3.grid(row=4, column=1, pady=3)

            rtlbl4 = tk.Label(manframe3)
            rtlbl4.grid(row=5, column=0, pady=3)
            rtlbl5 = tk.Label(manframe3)
            rtlbl5.grid(row=6, column=0, pady=3)

            ratsub1 = tk.Button(manframe3, text="Submit", bg="lightgreen",
                                command=lambda: self.leve(rtent1.get(),rtent2.get(),rtent3.get()))
            ratsub1.grid(row=7, column=0, columnspan=2, ipadx=50, pady=6)
        elif n == 2:
            # profit,ebit,equity,interest,debt
            rtlbl = tk.Label(manframe3, text="Profitability",font = ("Verdana", 12, "bold"))
            rtlbl.grid(row=1, column=0, pady=3)

            rtlbl1 = tk.Label(manframe3, text="Total Profit: ",font = ("Verdana", 12))
            rtent1 = tk.Entry(manframe3, width=10,font = ("Verdana", 12))
            rtlbl1.grid(row=2, column=0, pady=3)
            rtent1.grid(row=2, column=1, pady=3)

            rtlbl2 = tk.Label(manframe3, text="EBIT: ",font = ("Verdana", 12))
            rtent2 = tk.Entry(manframe3, width=10,font = ("Verdana", 12))
            rtlbl2.grid(row=3, column=0, pady=3)
            rtent2.grid(row=3, column=1, pady=3)

            rtlbl3 = tk.Label(manframe3, text="Interest(charge): ",font = ("Verdana", 12))
            rtent3 = tk.Entry(manframe3, width=10,font = ("Verdana", 12))
            rtlbl3.grid(row=4, column=0, pady=3)
            rtent3.grid(row=4, column=1, pady=3)

            rtlbl4 = tk.Label(manframe3, text="Equity: ", font=("Verdana", 12))
            rtent4 = tk.Entry(manframe3, width=10, font=("Verdana", 12))
            rtlbl4.grid(row=5, column=0, pady=3)
            rtent4.grid(row=5, column=1, pady=3) #debt

            rtlbl5 = tk.Label(manframe3, text="Total Debt: ", font=("Verdana", 12))
            rtent5 = tk.Entry(manframe3, width=10, font=("Verdana", 12))
            rtlbl5.grid(row=6, column=0, pady=3)
            rtent5.grid(row=6, column=1, pady=3)

            ratsub1 = tk.Button(manframe3, text="Submit", bg="lightgreen",command=lambda: self.prof(rtent1.get(),rtent2.get(),rtent3.get(),rtent5.get(),rtent5.get()))
            ratsub1.grid(row=7, column=0, columnspan=2, ipadx=50,pady = 6)




    def options(self,n):
        self.forgetting()
        self.forgetrezs()
        global lblnm,lblentpp1,lblentpp2,entpp1,entpp2,subcalc1
        global scrap,scraplbl
        global rate,ratelbl
        global manframe2

        if n == 0:
            lblnm = tk.Label(manframe2, text="Payback Period",font = ("Verdana", 12, "bold"))
            lblnm.grid(row=1, column=0)

            lblentpp1 = tk.Label(manframe2, text="Enter Investment Amount: ",font = ("Verdana", 12))
            entpp1 = tk.Entry(manframe2, width = 10,font = ("Verdana", 12))
            lblentpp1.grid(row=2, column=0)
            entpp1.grid(row=2, column=1)

            lblentpp2 = tk.Label(manframe2, text="Enter Cash Flows"+ '\n' +"(comma separated)",font = ("Verdana", 12))
            entpp2 = tk.Entry(manframe2,font = ("Verdana", 12))
            lblentpp2.grid(row=3, column=0)
            entpp2.grid(row=3, column=1)

            ratelbl = tk.Label(manframe2)
            ratelbl.grid(row = 4, column = 0)

            subcalc1 = tk.Button(manframe2,text ="Submit",bg = "lightgreen", command = lambda: self.hadlepp(entpp1.get(),entpp2.get()))
            subcalc1.grid(row=5, column=0,columnspan = 2,ipadx = 50,pady = 6)
        elif n == 1:
            lblnm = tk.Label(manframe2, text="Accounting Rate of Return",font = ("Verdana", 12, "bold"))
            lblnm.grid(row=1, column=0)

            lblentpp1 = tk.Label(manframe2, text="Enter Investment Amount: ",font = ("Verdana", 12))
            entpp1 = tk.Entry(manframe2, width=10,font = ("Verdana", 12))
            lblentpp1.grid(row=2, column=0)
            entpp1.grid(row=2, column=1)

            lblentpp2 = tk.Label(manframe2, text="Enter Cash Flows "+ '\n' +" (comma separated)",font = ("Verdana", 12))
            entpp2 = tk.Entry(manframe2,font = ("Verdana", 12))
            lblentpp2.grid(row=3, column=0)
            entpp2.grid(row=3, column=1)

            scraplbl = tk.Label(manframe2, text="Scrap Value",font = ("Verdana", 12))
            scrap = tk.Entry(manframe2,width = 10,font = ("Verdana", 12))
            scraplbl.grid(row=4, column=0)
            scrap.grid(row=4, column=1)

            subcalc1 = tk.Button(manframe2, text="Submit", bg="lightgreen",command=lambda: self.hadlearr(entpp1.get(), entpp2.get(),scrap.get()))
            subcalc1.grid(row=5, column=0, columnspan=2, ipadx=50,pady = 6)
        elif n == 2:
            lblnm = tk.Label(manframe2, text="Net Present Value",font = ("Verdana", 12, "bold"))
            lblnm.grid(row=1, column=0)

            lblentpp1 = tk.Label(manframe2, text="Enter Investment Amount: ",font = ("Verdana", 12))
            entpp1 = tk.Entry(manframe2, width=10,font = ("Verdana", 12))
            lblentpp1.grid(row=2, column=0)
            entpp1.grid(row=2, column=1)

            lblentpp2 = tk.Label(manframe2, text="Enter Cash Flows: " + '\n' + " (comma separated)",font = ("Verdana", 12))
            entpp2 = tk.Entry(manframe2,font = ("Verdana", 12))
            lblentpp2.grid(row=3, column=0)
            entpp2.grid(row=3, column=1)

            ratelbl = tk.Label(manframe2, text="Rate(%): ",font = ("Verdana", 12))
            rate = tk.Entry(manframe2, width=10,font = ("Verdana", 12))
            ratelbl.grid(row=4, column=0)
            rate.grid(row=4, column=1)


            subcalc1 = tk.Button(manframe2, text="Submit", bg="lightgreen",command=lambda: self.hadlenpv(entpp1.get(), entpp2.get(),rate.get()))
            subcalc1.grid(row=5, column=0, columnspan=2, ipadx=50,pady = 6)

    # Investments handlers
    def hadlepp(self,inv,cfs):
        global result
        self.forgetrezs()
        if inv != "" or cfs != "":
            a = Fin()
            cfs = cfs.split(",")
            rez =  a.PP(inv,cfs)
            if rez == -1:
                mb.showerror("Wrong input or Bad Investment", "Payments do not cover the investment")
            else:
                result = tk.Label(resultFrame,bg = "white",text = rez,font = ("Verdana", 16))
                result.grid(row=0, column=0)
        else:
            mb.showwarning("Blank Spaces", "Incomplete input \n Please make sure that no fields are blank")

    def hadlearr(self, inv, cfs, scrap):
        global result
        self.forgetrezs()
        if inv != "" or cfs != "" or scrap != "" :
            a = Fin()
            cfs = cfs.split(",")
            rez = a.ARR(inv, cfs, scrap)
            if rez == -1:
                mb.showerror("Error", "Invalid input")
            else:
                result = tk.Label(resultFrame,bg = "white", text=rez + "%", font=("Verdana", 16))
                result.grid(row=0, column=0, columnspan=2)
        else:
            mb.showwarning("Blank Spaces", "Incomplete input \n Please make sure that no fields are blank")
    def hadlenpv(self,inv, cfs, rate):
        global result
        self.forgetrezs()
        if inv != "" or cfs != "" :
            a = Fin()
            cfs = cfs.split(",")
            rez = a.NPV(inv, cfs, rate)
            if rez == -1:
                mb.showerror("Error", "Invalid input")
            elif rez >= 0:
                result = tk.Label(resultFrame, text="NPV =" +  str(rez),bg = "white",fg = 'green', font=("Verdana", 16))
                result.grid(row=0, column=0, columnspan=2)
            elif rez < 0 :
                result = tk.Label(resultFrame, text="NPV =" + str(rez),bg = "white", fg='red', font=("Verdana", 16))
                result.grid(row=0, column=0, columnspan=2)
        else:
            mb.showwarning("Blank Spaces", "Incomplete input \n Please make sure that no fields are blank")
    # WACC handle
    def handlewacc(self,vs,vb,rs,rb,tax):
        self.forgetrezs()
        global result2
        a = Fin()
        if vs != ""and vb != ""and rs != ""and rb != ""and tax != "":
            rez = a.WaccVar(vs,vb,rs,rb,tax)

            if rez == -1:
                mb.showerror("Invalid Characters!", "Please check your input")
            else:
                result2 = tk.Label(wccresprint, text="WACC =" + str(rez) + "%", fg='red', font=("Verdana", 16))
                result2.grid(row=0, column=0)
        else:
            mb.showwarning("Blank Spaces", "Incomplete input \n Please make sure no fields are blank")

    # Ratio Handles
    def liquid(self,ca,cl,inventory):
        global result3
        self.forgetrezs()
        if ca != "" and cl != "" and inventory != "":
            a = Fin()
            rez = a.liquidity(ca,cl,inventory)
            if rez == -1:
                mb.showerror("Invalid Characters!", "Please check your input")
            else:
                result3 = tk.Label(rtresFrame, text=rez, bg = "white", font=("Verdana", 16))
                result3.grid(row=0, column=0)
        else:
            mb.showwarning("Blank Spaces", "Incomplete input \n Please make sure no fields are blank")

    def leve(self,debt,equity,assets):
        global result3
        self.forgetrezs()
        if debt != "" and equity != "" and assets != "":
            a = Fin()
            rez = a.leverage(debt,equity,assets)

            if rez == -1:
                mb.showerror("Invalid Characters!", "Please check your input")
            else:
                result3 = tk.Label(rtresFrame, bg = "white", text=rez, font=("Verdana", 16))
                result3.grid(row=0, column=0)

        else:
            mb.showwarning("Blank Spaces", "Incomplete input \n Please make sure no fields are blank")

    def prof(self,profit,ebit,equity,interest,debt):
        global result3
        self.forgetrezs()
        if profit != "" and ebit != "" and equity != "" and interest != "" and debt != "":
            a = Fin()
            rez = a.profitability(profit,ebit,equity,interest,debt)

            if rez == -1:
                mb.showerror("Invalid Characters!", "Please check your input")
            else:
                result3 = tk.Label(rtresFrame, text=rez, bg = "white", font=("Verdana", 16))
                result3.grid(row=0, column=0)
        else:
            mb.showwarning("Blank Spaces", "Incomplete input \n Please make sure no fields are blank")

    def forgetting(self):
        global lblnm, lblentpp1, lblentpp2, entpp1, entpp2
        global scrap, scraplbl
        global rate,ratelbl
        global result,subcalc1
        try:
            subcalc1.grid_forget()
        except:
            pass
        try:
            lblnm.grid_forget()
            lblentpp1.grid_forget()
            lblentpp2.grid_forget()
            entpp1.grid_forget()
            entpp2.grid_forget()

        except:
            pass
        try:
            scrap.grid_forget()
            scraplbl.grid_forget()
        except:
            pass
        try:
            rate.grid_forget()
            ratelbl.grid_forget()
        except:
            pass
    def forgetting2(self):
        global rtlbl, rtlbl1, rtlbl2, rtlbl3, rtlbl4, rtlbl5
        global rtent1, rtent2, rtent3, rtent4, rtent5, ratsub1

        try:

            rtlbl.grid_forget()
            rtlbl1.grid_forget()
            rtlbl2.grid_forget()
            rtlbl3.grid_forget()

            rtent1.grid_forget()
            rtent2.grid_forget()
            rtent3.grid_forget()

            ratsub1.grid_forget()
        except:
            pass

        try:
            rtlbl4.grid_forget()
            rtent4.grid_forget()
        except:
            pass

        try:
            rtlbl5.grid_forget()
            rtent5.grid_forget()
        except:
            pass


    def forgetrezs(self):
        try:
            result.grid_forget()
        except:
            pass
        try:
            result2.grid_forget()
        except:
            pass

        try:
            result3.grid_forget()
        except:
            pass


if __name__ == '__main__':
    app = Business()
    app.mainloop()
