import numpy as np
import tkinter
from tkinter import *
import random

def calc(team1,am1,team2,am2,total,window,on1):
    dec1 = toDec(am1)
    dec2 = toDec(am2)
    opp=calcOp(dec1,dec2)
    t1=team1
    t2=team2
    TXT = Text(window)
    TXT.insert(INSERT,"Decimal Odds "+t1+": "+str(dec1))
    TXT.insert(INSERT,'\n'+"Decimal Odds "+t2+": "+str(dec2))
    TXT.insert(INSERT,'\n'+ "Arbitrage Opportunity: "+str(opp))
    if (opp):
        profit = 1-((1/dec1)+(1/dec2))
        TXT.insert(INSERT,'\n'+"Profit Margin: "+str(np.round(profit*100,2))+"%")
        brEv(dec1,dec2,total,profit,t1,t2,window,TXT,on1)
    else:
        TXT.place(relx=0.02,rely=0.25,relwidth=.96,relheight=.63)

def calcOp(d1,d2):
    if (d1+d2)<(d1*d2):
        return True
    return False

def toDec(a):
    if a > 0 :
        return 1 + (a/100)
    return 1-(100/a)

def brEv(a,b,c,d,e,f,w,TXT,on1):
    if on1!=0:
        betA=on1
        betB=on1*(a-1)
    else:
        betA=c/a
        betA=np.round(betA,2)
        betB=c-betA
    t1=e
    t2=f
    TXT.insert(INSERT,'\n'+"~~~~~~~~~~~~~~~~")
    TXT.insert(INSERT,'\n'+ "To Break Even On "+t1+": $"+str(np.round(betA,2))+"(Pays Out: $"+str(np.round(betA*a,2))+")")
    TXT.insert(INSERT,'\n'+ "To Profit On "+t2+": $"+str(np.round(betB,2))+"(Pays Out: $"+str(np.round(betB*b,2))+")")
    TXT.insert(INSERT,'\n'+ "Net $"+str(np.round(betB*b-(betA+betB),2))+" on "+t2+" Win.")
    if on1!=0:
        betB=on1/(b-1)
    else:
        betB=c/b
        betB=np.round(betB,2)
        betA=c-betB
    TXT.insert(INSERT,'\n'+"~~~~~~~~~~~~~~~~")
    TXT.insert(INSERT,'\n'+ "To Profit On "+t1+": $"+str(np.round(betA,2))+"(Pays Out: $"+str(np.round(betA*a,2))+")")
    TXT.insert(INSERT,'\n'+ "To Break Even On "+t2+": $"+str(np.round(betB,2))+"(Pays Out: $"+str(np.round(betB*b,2))+")")
    TXT.insert(INSERT,'\n'+ "Net $"+str(np.round(betA*a-(betA+betB),2))+" on "+t1+" Win.")
    if on1!=0:
        betB=(on1*a)/b
    else:
        percentA=100/a
        percentB=100/b
        betA=c*percentA/(percentA+percentB)
        betB=c-betA
    TXT.insert(INSERT,'\n'+"~~~~~~~~~~~~~~~~")
    TXT.insert(INSERT,'\n'+ "Optimal")
    TXT.insert(INSERT,'\n'+ "Winnings On "+t1+": $"+str(np.round(betA,2))+"(Pays Out: $"+str(np.round(betA*a,2))+")")
    TXT.insert(INSERT,'\n'+ "Winnings On "+t2+": $"+str(np.round(betB,2))+"(Pays Out: $"+str(np.round(betB*b,2))+")")
    TXT.insert(INSERT,'\n'+ "Net $"+str(np.round(betA*a-(betA+betB),2))+" on "+t1+" Win.")
    TXT.insert(INSERT,'\n'+ "Net $"+str(np.round(betB*b-(betA+betB),2))+" on "+t2+" Win.")
    TXT.place(relx=0.02,rely=0.25,relwidth=.96,relheight=.63)

def LEP(L,E,X,Y,H,W):
    L.place(relheight=H,relwidth=W*.25,relx=X,rely=Y)
    E.place(relheight=H,relwidth=W*.75,relx=X+(W/4),rely=Y)

window = Tk()
window.title("Smart Gambling TM")
aspect=50
window.configure(bg='green')

t1b= Entry(window, bd=3)
t1L = Label(window, font="size=1",text="Bet 1:")
LEP(t1L,t1b,0,0.01,.05,.49)

o1b = Spinbox(window, bd=3, from_=-1000000, to = 100000)
o1L = Label(window, font="size=1",text="Odds:")
LEP(o1L,o1b,0.51,0.01,.05,.49)

t2b= Entry(window, bd=3)
t2L = Label(window, font="size=1",text="Bet 2:")
LEP(t2L,t2b,0,0.07,.05,.49)

o2b = Spinbox(window, bd=3, from_=-1000000, to = 100000)
o2L = Label(window, font="size=1",text="Odds:")
LEP(o2L,o2b,0.51,0.07,.05,.49)

totmonb = Spinbox(window, bd=3, from_=-1, to = 100000)
monL = Label(window, font="size=1",text="Total $:")
LEP(monL, totmonb,.01,0.13,.05,.98)

maxMon = Spinbox(window, bd=3, from_=0, to = 100000)
maxL = Label(window, font="size=1",text="Bet On 1:")
LEP(maxL, maxMon,.01,0.19,.05,.98)

def send():
    calc(t1b.get(),int(o1b.get()),t2b.get(),int(o2b.get()),int(totmonb.get()),window,int(maxMon.get()))

goBut = tkinter.Button(window,font="size=94",text="Caclulate", command=send,padx=40,bg="lightgray")
goBut.place(relheight=.1,relwidth=1,rely=.9)

window.configure(width=aspect*9, height=aspect*14)
window.mainloop()