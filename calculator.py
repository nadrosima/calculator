import os
try:
    dirs = os.path.dirname(os.__file__).lower()
    if "python2" in dirs:
        from Tkinter import *
    elif "python3" in dirs:
        from tkinter import *
except Exception,e : print e

class _hesap:
    def __init__(self):
        self.ana = Tk()
        self.sonuc = Entry(self.ana)
        self.sonuc.place(x=0,y=0,width=100)
        self.btn = "1","2","3","+","4","5","6","-","7","8","9","x",".","0","DEL","/","CLR","ENTER"
        self.conte = {}
        for i in range(len(self.btn)):
            tx = self.btn[i]
            ndx = self.btn.index(tx)
            satir = divmod(ndx,4)            
            fr = Button(self.ana,text=tx)
            fr.place(x=(25*satir[1]),y=(25*satir[0])+25,width=25)
            self.conte[tx] = fr
            del fr
            if tx == self.btn[-1]:
                self.conte[self.btn[-1]].place(x=25,y=125,width=75)                
            self.conte[tx].bind('<Button-1>', self.ne)
        self.ana.config(width=80,height=150)
        
    def ne(self,event):
        f = self.sonuc.get()
        pres = event.widget.config("text")[-1]
        ndx = self.btn.index(pres)        
        if ndx in (14,16,17) :
            self.sonuc.delete(0,END)
            if ndx in (14,):
                self.sonuc.insert(0, f[:-1])
            elif ndx in (17,):
                self.sonuc.insert(0,eval(("1.0x" + f).replace("x","*")))            
        else:
            ekle = f + pres
            self.sonuc.delete(0,END)
            self.sonuc.insert(0, ekle )

if __name__ == "__main__":
    hesap = _hesap()
    hesap.ana.mainloop()
