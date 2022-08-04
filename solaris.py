from __future__ import unicode_literals
from tkinter import *
from tkinter import messagebox

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import pi, sqrt



# ikona
# żeby czcz.get() zmienniał się podczas
# po co init

tlo = '#1C2429'  # taki ciemnoszaroniebieski

# definiowanie okna
okno = Tk()
okno.title('Układ Słoneczny')
okno['bg'] = tlo


# wykres

# fig to pole, a ax to konkretny wykres,
# w jednym polu może być kilka wykresów, w jedym wykresie wiele linii

fig, ax = plt.subplots(figsize=(7, 7))

# nx = int(fig.get_figwidth() * fig.dpi)
# ny = int(fig.get_figheight() * fig.dpi)

plt.tight_layout()

fig.patch.set_facecolor('black')
ax.set_xlim(-10, 10)  # wielkość wykresu
ax.set_ylim(-10, 10)
ax.axis('off')


# fig.patch.set_visible(False)
# ax.patch.set_visible(False)

# próby usunięcia ramki
# fig = figure(frameon=False)
# for item in [fig, ax]:
#    item.patch.set_visible(False)
# ax.axis('off')
# ax.set_axis_off()

'''
axes[0,1].clear()
axes[1,0].axis("off")
axes[1,1].set_visible(False)
axes[0,2].remove()

'''

cosmic = FigureCanvasTkAgg(fig, master=okno)  # pole do osadzenia matplotlib w tkinter
cosmic.get_tk_widget().grid(row=2, column=2)

d = np.linspace(0, 2*pi, 100)  # delta
# d = pd.Series(np.linspace(0, 2*pi, 100))


time_text = ax.text(0.02, 0.95, ' ', transform=ax.transAxes, color="white")

global animacja
# def init():
#   time_text.set_text('')
#  line1.set_data([],[])
# return line1, time_text
s = 4

slonce = plt.Circle((0, 0), s * 0.1, color='yellow')
ax.add_artist(slonce)
# slonce.set_radius(s*0.04)

line1, = ax.plot([], [])
line2, = ax.plot([], [])
line3, = ax.plot([], [])
line4, = ax.plot([], [])
line5, = ax.plot([], [])

    # initialization function
xdata1, ydata1 = [], []
xdata2, ydata2 = [], []
xdata3, ydata3 = [], []
xdata4, ydata4 = [], []
xdata5, ydata5 = [], []


def stop():
    if 'animacja' in globals():
        animacja.event_source.stop()


def run():
    global xdata1, ydata1, \
        xdata2, ydata2, \
        xdata3, ydata3, \
        xdata4, ydata4, \
        xdata5, ydata5
    global line1, line2, line3, line4, line5, animacja, slonce
    xdata1, ydata1 = [], []
    xdata2, ydata2 = [], []
    xdata3, ydata3 = [], []
    xdata4, ydata4 = [], []
    xdata5, ydata5 = [], []

    print('start')


    stop()
    #stap = Button(planety, text="Stop", command=stop).grid(row=1, column=0)

    s = ss.get()  # skala
    cz = czcz.get()
    slonce.set_radius(ss.get() * 0.1)


    def init():
        # creating an empty plot/frame
        line1.set_data([], [])
        line2.set_data([], [])
        line3.set_data([], [])
        line4.set_data([], [])
        line5.set_data([], [])
        return line1, line2, line2, line4, line5,

    # lists to store x and y axis points
    def animate(i):  # ziemia

        def orbita(e, a, T, g, col, i, line, ):
            b = sqrt(a ** 2 * (1 - e ** 2))  # mała półoś
            u = sqrt(a ** 2 - b ** 2)  # x przesunięty o ogniskową
            v = 0  # y
            plt.setp(line, animated=True, linestyle=':', linewidth=1.5 * g, color=col)
            t = (2 * pi) / T  # * d
            #print(t)
            return a, b, u, v, t

        if CheckMerk.get() == 1:

            a1, b1, u1, v1, t1 = orbita(0.206, s * 0.388, s * 0.24, s * 0.2, 'rosybrown', i, line1)

            ydata1.append(v1 + b1 * np.sin(i * t1 * cz / 10000))
            xdata1.append(u1 + a1 * np.cos(i * t1 * cz / 10000))
            line1.set_data(xdata1, ydata1)

        if CheckWenus.get() == 1:
            a2, b2, u2, v2, t2 = orbita(0.0068, s * 0.723, s * 0.62, s * 0.4, 'mediumvioletred', i, line2)

            ydata2.append(v2 + b2 * np.sin(i * t2 * cz / 10000))
            xdata2.append(u2 + a2 * np.cos(i * t2 * cz / 10000))
            line2.set_data(xdata2, ydata2)

        if CheckZiemia.get() == 1:
            a3, b3, u3, v3, t3 = orbita(0.0147, s, s, s * 0.4, 'springgreen', i, line3)

            ydata3.append(v3 + b3 * np.sin(i * t3 * cz / 10000))
            xdata3.append(u3 + a3 * np.cos(i * t3 * cz / 10000))
            line3.set_data(xdata3, ydata3)

        if CheckMars.get() == 1:

            a4, b4, u4, v4, t4 = orbita(0.0934, s * 1.524, s * 1.88, s * 0.3, 'coral', i, line4)

            ydata4.append(v4 + b4 * np.sin(i * t4 * cz / 10000))
            xdata4.append(u4 + a4 * np.cos(i * t4 * cz / 10000))
            line4.set_data(xdata4, ydata4)
            
        if CheckJow.get() == 1:			
            a5, b5, u5, v5, t5 = orbita(0.0485, s * 5.203, s * 11.86, s, 'tan', i, line5)

            ydata5.append(v5 + b5 * np.sin(i * t5 * cz / 10000))
            xdata5.append(u5 + a5 * np.cos(i * t5* cz / 10000))
            line5.set_data(xdata5, ydata5)

        return line1, line2, line3, line4, line5,

    animacja = animation.FuncAnimation(fig, animate, interval=0.01, init_func=init, blit=True)  # frames=int(80000 * s / cz),


def clean():
    global xdata1, ydata1, \
        xdata2, ydata2, \
        xdata3, ydata3, \
        xdata4, ydata4, \
        xdata5, ydata5

    xdata1, ydata1 = [], []
    xdata2, ydata2 = [], []
    xdata3, ydata3 = [], []
    xdata4, ydata4 = [], []
    xdata5, ydata5 = [], []

#clear = Button(planety, text="Wyczyść", command=clean).grid(row=2, column=0)

print('end')

    # 1.524 0.0934
    # 5.203 0.0485
    # 9.539 0.0556


# interfejs
tytul = Label(okno, text="\nSymulator ruchu planet w Układzie Słonecznym\n", bg=tlo, fg='white').grid(row=0, column=2)

# meni = Frame (okno, bg="black")
# meni.grid(row=0, column=0)

exit = Frame(okno)
exit.grid(row=3, column=3)
blackbutton = Button(exit, text="Wyjście", fg="black", bg="white", command=okno.quit).grid()

tcz = Label(okno, bg=tlo, fg='white', text="\n  upływ czasu  \n").grid(row=3, column=0)
czcz = IntVar()
sczas = Scale(okno, variable=czcz, bg=tlo, fg='gray',
              orient=HORIZONTAL, length=394, from_=1, to_=200).grid(row=3, column=2)
czcz.set(10)


sca = Frame(okno, bg=tlo)
sca.grid(row=2, column=3)
tss = Label(sca, bg=tlo, fg='white', text="       skala       \n").grid()
ss = IntVar()
sss = Scale(sca, variable=ss, bg=tlo, fg='gray',
            orient=VERTICAL, length=394, from_=1, to_=5).grid()
ss.set(4)


planety = Frame(okno, bg=tlo)
planety.grid(row=2, column=0)


CheckMerk = IntVar()
CheckWenus = IntVar()
CheckZiemia = IntVar()
CheckMars = IntVar()
CheckJow = IntVar()
CheckSat = IntVar()

tlop = tlo
start = Button(planety, text="Start", command=run).grid(row=0, column=0)
stap = Button(planety, text="Stop", command=stop).grid(row=1, column=0)
clear = Button(planety, text="Wyczyść", comman=clean).grid(row=2, column=0)


blank = Label(planety, text="\n\n", bg=tlo).grid()

merkury = Checkbutton(planety, text="Merkury", fg="peru", bg=tlop,
                      variable=CheckMerk, onvalue=1, offvalue=0).grid(sticky=W)

wenus = Checkbutton(planety, text="Wenus", fg='mediumvioletred', bg=tlop,
                    variable=CheckWenus, onvalue=1, offvalue=0).grid(sticky=W)

ziemia = Checkbutton(planety, text="Ziemia", fg="springgreen", bg=tlop,
                     variable=CheckZiemia, onvalue=1, offvalue=0).grid(sticky=W)

mars = Checkbutton(planety, text=" Mars", fg="coral", bg=tlop,
                   variable=CheckMars).grid(sticky=W)

jowisz = Checkbutton(planety, text="Jowisz", fg="tan", bg=tlop,
                     variable=CheckJow, onvalue=1, offvalue=0).grid(sticky=W)

saturn = Checkbutton(planety, text="Saturn", fg="lightsteelblue", bg=tlop,
                     variable=CheckSat, onvalue=1, offvalue=0).grid(sticky=W)


# funkcja to zmieniania labeli to mylabel.configure
def on_closing():
    if messagebox.askokcancel("Wyjście", "Chcesz zamknąć program?"):
        okno.destroy()


okno.protocol("WM_DELETE_WINDOW", on_closing)

okno.mainloop()
