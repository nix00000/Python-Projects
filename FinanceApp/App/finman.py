
class FinMan:
    def PP(self,inv,cfs):
        try:
            inv = float(inv)
            cfs = list(map(float, cfs))
        except:
            return -1
        n = len(cfs)
        count = 0
        yrs = 0
        inv = float(inv)
        cfs = list(map(float, cfs))

        if sum(cfs) >= inv:
            for i, j in enumerate(cfs):
                if count + j <= inv:
                    count += j
                    yrs += 1
            if count == inv:
                return("Years = " + str(round(yrs,2)))
            else:
                dif = round(inv - count,2)
                y = cfs[yrs]
                rez = ( "full years = " + str(yrs)+"\n"+ "difference = inves - full y val"+ "\n"+ "difference = " + str(dif) + "\n"+ "year " + str(yrs) + " cf = " + str(cfs[yrs]) +
                      "\n" + "years = " + str(dif) + " / " + str(cfs[yrs])  + "\n" + "Payback Period = " )
                yrs += dif / y
                return(rez + str(round(yrs,2)))
        else:
            return(-1)

    def ARR(self, inv, cfs, scrap):
        try:
            inv = float(inv)
            cfs = list(map(float, cfs))
            scrap = float(scrap)
        except:
            return -1
        tot = sum(cfs) - inv
        avgp = tot / len(cfs)
        prof = "Average Profit = Total Profit/years \n"
        prof_c = str(tot) + "/" + str(len(cfs)) + "\n"
        avgi = (inv + scrap)/2
        inves = "Average Investment = Total Profit/years \n"
        inves_c = str(inv)  + str(scrap)+ "/"+ str(2) + "\n"
        result = avgp/avgi * 100
        return(prof+"Average Profit = "+prof_c+inves+ "Average Investment ="+inves_c+"ARR = "+str(round(result,2)))

    def NPV(self,inv, cfs, rate):
        try:
            inv = float(inv)
            cfs = list(map(float, cfs))
            rate = float(rate)
        except:
            return -1
        total = 0
        r = rate/100 + 1

        for i in range(len(cfs)):
            total = total + cfs[i]/(r**(i+1))

        total = total - inv
        return round(total,2)

    def WaccVar(self,vs,vb,rs,rb,tax):
        try:
            tax=float(tax)
            vs=float(vs)
            vb=float(vb)
            rs=float(rs)
            rb=float(rb)
        except:
            return -1
        vf = vs + vb
        rs = rs / 100
        rb = rb / 100
        tax = tax / 100

        wacc = vs / vf * rs + vb / vf * rb * (1-tax)
        if round(wacc * 100,2).is_integer():
            return int(round(wacc * 100,2))
        else:
            return round(wacc * 100,2)

    def liquidity(self,ca,cl,inventory):
        try:
            ca =float(ca)
            cl = float(cl)
            inventory = float(inventory)
        except:
            return -1

        txt = ""
        liquid = dict(
            CurrentRatio = round(ca/cl,2),
            QuickRatio = round((ca - inventory) / ca,2),
            NetWorkingCap= round(ca - cl,2)
        )
        for l in liquid:
            if liquid[l].is_integer():
                txt += l + " : " + str(int(liquid[l])) + "\n"
            else:
                txt += l + " : " + str(liquid[l]) + "\n"
        return txt
    def leverage(self,debt,equity,assets):
        try:
            debt =float(debt)
            equity = float(equity)
            assets = float(assets)
        except:
            return -1
        txt = ""
        lev = dict(
            DebtRatio =round(debt/assets,2),
            Debt2Equity = round(debt/equity,2),
            EquityRatio = round(equity / assets,2)
        )
        for l in lev:
            txt += l + " : " + str(lev[l])+ "%" + "\n"
        return txt
    def profitability(self,profit,ebit,equity,interest,debt):
        try:
            profit =float(profit)
            ebit = float(ebit)
            equity = float(equity)
            interest = float(interest)
            debt = float(debt)
        except:
            return -1
        txt = ""

        prof = dict(
            ROE= round(profit/equity*10,2),
            ROD = round(interest/debt*10,2),
            ROI = round(ebit/(debt+equity)*10,2)
        )
        for l in prof:
            txt += l + " : " + str(prof[l])+ "%" + "\n"
        return txt





# fin = FinMan()
# fin.PP(1000, [100,200,200,100,200,500])
# fin.ARR(1000,100,[300,300,300,300,400])
# fin.NPV(1000,0.1,[300,300,300,300,400])
# fin.WaccVar(5000,2000,3000,0,5,8)
# rez = fin.liquidity(3000,1000,2000)
# print(rez['NetWorkingCap'])