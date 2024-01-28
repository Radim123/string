import tkinter as tk
import math
import time

#tkinter related stuff
window = tk.Canvas(height=600,width=1000,bg="#1B004B")
window.pack()

window.create_line(0,300,1000,300,width=3,fill="black")
window.create_line(500,0,500,600,width=3,fill="black")

def X(x: float) -> float:
    return 50*x + 500

def Y(y: float) -> float:
    return 300 - 50*y

window.create_oval(X(8)-5,Y(0)-5,X(8)+5,Y(0)+5,fill="red")
window.create_oval(X(-8)-5,Y(0)-5,X(-8)+5,Y(0)+5,fill="red")


#this part is kinda self explanatory
class GoniometricFunction():
    def __init__(self, a: float,b: float,c: float,d: float) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
    def f(self, x: float, t: float) -> float:
        return self.a*(math.cos(self.c*(x-t)) + math.cos(self.c*(x+t))) + self.b*(math.sin(self.d*(x-t)) + math.sin(self.d*(x+t)))
        

#GF stands for goniometric functions
def EvalGFSum(G: list[GoniometricFunction],x: float,t: float) -> float:
    y = 0
    for i in G:
        y += i.f(x,t)
    return y

#displays GF sum in window at time t
def Display(G: list[GoniometricFunction],t: float) -> None:
    x = -8 
    y = 0
    while x < 8:
        z = x + 0.1
        w = EvalGFSum(G,z,t)
        window.create_line(X(x),Y(y),X(z),Y(w),fill="yellow",tags="graf")
        x += 0.1
        y = w
        
#displays wave propagation in window
def Animation(G: list[GoniometricFunction]) -> None:
    t = 0
    while t < 100:
        Display(G,10*t)
        window.update()
        window.delete("graf")
        time.sleep(0.01)
        t += 0.01

#fins right coeffs for cosines
def OddIntegration(p: int) -> list[float]:
    w = []
    for i in range(0,p):
        c = 0
        x = -8
        deltaX = 0.05
        while x < 8:
            c += F(x)*(1/math.sqrt(8))*math.cos((math.pi*(2*i+1)/16)*x)*deltaX
            x += deltaX
        w.append(c)
    return w

#find right coeffs for sines
def EvenIntegration(p: int) -> list[float]:
    w = [0]
    for i in range(1,p):
        c = 0
        x = -8
        deltaX = 0.05
        while x < 8:
            c += F(x)*(1/math.sqrt(8))*math.sin((math.pi*(2*i)/16)*x)*deltaX
            x += deltaX
        w.append(c)
    return w     
    
#initial state of string
#must satisfy condition: F(8) = F(-8) is close to 0 & F(x) is continuus and twice differentiable on x in [-8,8]
def F(x: float) -> float:
    return math.exp(-(x)**2)

p = 20

o = OddIntegration(p)
e = EvenIntegration(p)
L = []
for i in range(0,p):
    x = GoniometricFunction(o[i]/(2*math.sqrt(8)),e[i]/(2*math.sqrt(8)),math.pi*(2*i+1)/16,math.pi*(2*i)/16)
    L.append(x)
Animation(L) 

#tkinter related stuff
window.mainloop()