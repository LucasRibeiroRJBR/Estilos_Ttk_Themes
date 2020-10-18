from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle


def alt():
    root_alt = Tk()

    style_alt = ThemedStyle(root_alt)
    style_alt.set_theme('alt')

    botao = ttk.Button(root_alt, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_alt, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_alt)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_alt)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_alt, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_alt, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_alt, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_alt.mainloop()


def aquativo():
    root_aquativo = Tk()

    style_aquativo = ThemedStyle(root_aquativo)
    style_aquativo.set_theme('aquativo')

    botao = ttk.Button(root_aquativo, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_aquativo, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_aquativo)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_aquativo)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_aquativo, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_aquativo, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_aquativo, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_aquativo.mainloop()


def arc():
    root_arc = Tk()

    style_arc = ThemedStyle(root_arc)
    style_arc.set_theme('arc')

    botao = ttk.Button(root_arc, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_arc, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_arc)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_arc)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_arc, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_arc, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_arc, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_arc.mainloop()


def black():
    root_black = Tk()

    style_black = ThemedStyle(root_black)
    style_black.set_theme('black')

    botao = ttk.Button(root_black, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_black, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_black)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_black)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_black, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_black, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_black, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_black.mainloop()


def blue():
    root_blue = Tk()

    style_blue = ThemedStyle(root_blue)
    style_blue.set_theme('blue')

    botao = ttk.Button(root_blue, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_blue, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_blue)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_blue)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_blue, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_blue, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_blue, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_blue.mainloop()


def breeze():
    root_breeze = Tk()

    style_breeze = ThemedStyle(root_breeze)
    style_breeze.set_theme('breeze')

    botao = ttk.Button(root_breeze, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_breeze, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_breeze)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_breeze)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_breeze, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_breeze, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_breeze, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_breeze.mainloop()


def clam():
    root_clam = Tk()

    style_clam = ThemedStyle(root_clam)
    style_clam.set_theme('clam')

    botao = ttk.Button(root_clam, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_clam, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_clam)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_clam)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_clam, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_clam, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_clam, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_clam.mainloop()


def classic():
    root_classic = Tk()

    style_classic = ThemedStyle(root_classic)
    style_classic.set_theme('classic')

    botao = ttk.Button(root_classic, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_classic, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_classic)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_classic)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_classic, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_classic, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_classic, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_classic.mainloop()


def clearlooks():
    root_clearlooks = Tk()

    style_clearlooks = ThemedStyle(root_clearlooks)
    style_clearlooks.set_theme('clearlooks')

    botao = ttk.Button(root_clearlooks, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_clearlooks, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_clearlooks)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_clearlooks)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_clearlooks, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_clearlooks, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_clearlooks, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_clearlooks.mainloop()


def default():
    root_default = Tk()

    style_default = ThemedStyle(root_default)
    style_default.set_theme('default')

    botao = ttk.Button(root_default, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_default, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_default)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_default)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_default, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_default, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_default, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_default.mainloop()


def elegance():
    root_elegance = Tk()

    style_elegance = ThemedStyle(root_elegance)
    style_elegance.set_theme('elegance')

    botao = ttk.Button(root_elegance, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_elegance, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_elegance)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_elegance)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_elegance, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_elegance, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_elegance, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_elegance.mainloop()


def equilux():
    root_equilux = Tk()

    style_equilux = ThemedStyle(root_equilux)
    style_equilux.set_theme('equilux')

    botao = ttk.Button(root_equilux, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_equilux, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_equilux)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_equilux)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_equilux, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_equilux, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_equilux, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_equilux.mainloop()


def itft1():
    root_itft1 = Tk()

    style_itft1 = ThemedStyle(root_itft1)
    style_itft1.set_theme('itft1')

    botao = ttk.Button(root_itft1, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_itft1, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_itft1)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_itft1)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_itft1, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_itft1, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_itft1, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_itft1.mainloop()


def keramik():
    root_keramik = Tk()

    style_keramik = ThemedStyle(root_keramik)
    style_keramik.set_theme('keramik')

    botao = ttk.Button(root_keramik, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_keramik, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_keramik)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_keramik)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_keramik, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_keramik, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_keramik, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_keramik.mainloop()


def kroc():
    root_kroc = Tk()

    style_kroc = ThemedStyle(root_kroc)
    style_kroc.set_theme('kroc')

    botao = ttk.Button(root_kroc, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_kroc, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_kroc)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_kroc)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_kroc, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_kroc, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_kroc, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_kroc.mainloop()


def plastik():
    root_plastik = Tk()

    style_plastik = ThemedStyle(root_plastik)
    style_plastik.set_theme('plastik')

    botao = ttk.Button(root_plastik, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_plastik, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_plastik)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_plastik)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_plastik, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_plastik, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_plastik, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_plastik.mainloop()


def radiance():
    root_radiance = Tk()

    style_radiance = ThemedStyle(root_radiance)
    style_radiance.set_theme('radiance')

    botao = ttk.Button(root_radiance, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_radiance, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_radiance)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_radiance)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_radiance, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_radiance, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_radiance, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_radiance.mainloop()


def scidblue():
    root_scidblue = Tk()

    style_scidblue = ThemedStyle(root_scidblue)
    style_scidblue.set_theme('scidblue')

    botao = ttk.Button(root_scidblue, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_scidblue, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_scidblue)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_scidblue)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_scidblue, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_scidblue, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_scidblue, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_scidblue.mainloop()


def scidgreen():
    root_scidgreen = Tk()

    style_scidgreen = ThemedStyle(root_scidgreen)
    style_scidgreen.set_theme('scidgreen')

    botao = ttk.Button(root_scidgreen, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_scidgreen, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_scidgreen)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_scidgreen)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_scidgreen, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_scidgreen, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_scidgreen, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_scidgreen.mainloop()


def scidgrey():
    root_scidgrey = Tk()

    style_scidgrey = ThemedStyle(root_scidgrey)
    style_scidgrey.set_theme('scidgrey')

    botao = ttk.Button(root_scidgrey, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_scidgrey, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_scidgrey)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_scidgrey)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_scidgrey, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_scidgrey, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_scidgrey, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_scidgrey.mainloop()


def scidmint():
    root_scidmint = Tk()

    style_scidmint = ThemedStyle(root_scidmint)
    style_scidmint.set_theme('scidmint')

    botao = ttk.Button(root_scidmint, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_scidmint, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_scidmint)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_scidmint)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_scidmint, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_scidmint, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_scidmint, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_scidmint.mainloop()


def scidpink():
    root_scidpink = Tk()

    style_scidpink = ThemedStyle(root_scidpink)
    style_scidpink.set_theme('scidpink')

    botao = ttk.Button(root_scidpink, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_scidpink, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_scidpink)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_scidpink)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_scidpink, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_scidpink, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_scidpink, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_scidpink.mainloop()


def scidpurple():
    root_scidpurple = Tk()

    style_scidpurple = ThemedStyle(root_scidpurple)
    style_scidpurple.set_theme('scidpurple')

    botao = ttk.Button(root_scidpurple, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_scidpurple, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_scidpurple)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_scidpurple)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_scidpurple, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_scidpurple, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_scidpurple, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_scidpurple.mainloop()


def scidsand():
    root_scidsand = Tk()

    style_scidsand = ThemedStyle(root_scidsand)
    style_scidsand.set_theme('scidsand')

    botao = ttk.Button(root_scidsand, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_scidsand, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_scidsand)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_scidsand)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_scidsand, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_scidsand, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_scidsand, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_scidsand.mainloop()


def smog():
    root_smog = Tk()

    style_smog = ThemedStyle(root_smog)
    style_smog.set_theme('smog')

    botao = ttk.Button(root_smog, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_smog, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_smog)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_smog)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_smog, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_smog, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_smog, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_smog.mainloop()


def ubuntu():
    root_ubuntu = Tk()

    style_ubuntu = ThemedStyle(root_ubuntu)
    style_ubuntu.set_theme('ubuntu')

    botao = ttk.Button(root_ubuntu, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_ubuntu, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_ubuntu)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_ubuntu)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_ubuntu, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_ubuntu, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_ubuntu, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_ubuntu.mainloop()


def vista():
    root_vista = Tk()

    style_vista = ThemedStyle(root_vista)
    style_vista.set_theme('vista')

    botao = ttk.Button(root_vista, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_vista, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_vista)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_vista)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_vista, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_vista, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_vista, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_vista.mainloop()


def winnative():
    root_winnative = Tk()

    style_winnative = ThemedStyle(root_winnative)
    style_winnative.set_theme('winnative')

    botao = ttk.Button(root_winnative, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_winnative, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_winnative)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_winnative)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_winnative, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_winnative, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_winnative, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_winnative.mainloop()


def winxpblue():
    root_winxpblue = Tk()

    style_winxpblue = ThemedStyle(root_winxpblue)
    style_winxpblue.set_theme('winxpblue')

    botao = ttk.Button(root_winxpblue, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_winxpblue, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_winxpblue)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_winxpblue)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_winxpblue, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_winxpblue, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_winxpblue, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_winxpblue.mainloop()


def xpnative():
    root_xpnative = Tk()

    style_xpnative = ThemedStyle(root_xpnative)
    style_xpnative.set_theme('xpnative')

    botao = ttk.Button(root_xpnative, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_xpnative, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_xpnative)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_xpnative)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_xpnative, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_xpnative, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_xpnative, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_xpnative.mainloop()


def yaru():
    root_yaru = Tk()

    style_yaru = ThemedStyle(root_yaru)
    style_yaru.set_theme('yaru')

    botao = ttk.Button(root_yaru, text='Botão')
    botao.grid(row=0, column=0, padx=10, pady=10)

    check_button = ttk.Checkbutton(root_yaru, text='Check Button')
    check_button.grid(row=1, column=0, padx=10, pady=10)

    combo_box = ttk.Combobox(root_yaru)
    combo_box['values'] = [1, 2, 3, 4, 5]
    combo_box.set("Combo Box")
    combo_box.grid(row=2, column=0, padx=10, pady=10)

    entry = ttk.Entry(root_yaru)
    entry.grid(row=3, column=0, padx=10, pady=10)

    frame = ttk.LabelFrame(root_yaru, text='Frame')
    frame.grid(row=4, column=0, padx=10, pady=10)
    label_para_frame = Label(frame, text='                                  ')
    label_para_frame.grid(row=0, column=0)

    label = Label(root_yaru, text='Label')
    label.grid(row=5, column=0, padx=10, pady=10)

    labeledscale = ttk.LabeledScale(root_yaru, from_=9, to=90)
    labeledscale.grid(row=6, column=0, padx=10, pady=10)

    root_yaru.mainloop()


root = Tk()
root.title('Validador de CPF')

style = ThemedStyle(root)
style.set_theme('equilux')

bt_alt = ttk.Button(root, text='alt', command=alt)
bt_alt.grid(row=0, column=0)

bt_aquativo = ttk.Button(root, text='aquativo', command=aquativo)
bt_aquativo.grid(row=1, column=0)

bt_arc = ttk.Button(root, text='arc', command=arc)
bt_arc.grid(row=2, column=0)

bt_black = ttk.Button(root, text='black', command=black)
bt_black.grid(row=3, column=0)

bt_blue = ttk.Button(root, text='blue', command=blue)
bt_blue.grid(row=4, column=0)

bt_breeze = ttk.Button(root, text='breeze', command=breeze)
bt_breeze.grid(row=5, column=0)

bt_clam = ttk.Button(root, text='clam', command=clam)
bt_clam.grid(row=6, column=0)

bt_classic = ttk.Button(root, text='classic', command=classic)
bt_classic.grid(row=7, column=0)

bt_clearlooks = ttk.Button(root, text='clearlooks', command=clearlooks)
bt_clearlooks.grid(row=8, column=0)

bt_default = ttk.Button(root, text='default', command=default)
bt_default.grid(row=9, column=0)

bt_elegance = ttk.Button(root, text='elegance', command=elegance)
bt_elegance.grid(row=0, column=1)

bt_equilux = ttk.Button(root, text='equilux', command=equilux)
bt_equilux.grid(row=1, column=1)

bt_itft1 = ttk.Button(root, text='itft1', command=itft1)
bt_itft1.grid(row=2, column=1)

bt_keramik = ttk.Button(root, text='keramik', command=keramik)
bt_keramik.grid(row=3, column=1)

bt_kroc = ttk.Button(root, text='kroc', command=kroc)
bt_kroc.grid(row=4, column=1)

bt_plastik = ttk.Button(root, text='plastik', command=plastik)
bt_plastik.grid(row=5, column=1)

bt_radiance = ttk.Button(root, text='radiance', command=radiance)
bt_radiance.grid(row=6, column=1)

bt_scidblue = ttk.Button(root, text='scidblue', command=scidblue)
bt_scidblue.grid(row=7, column=1)

bt_scidgreen = ttk.Button(root, text='scidgreen', command=scidgreen)
bt_scidgreen.grid(row=8, column=1)

bt_scidgrey = ttk.Button(root, text='scidgrey', command=scidgrey)
bt_scidgrey.grid(row=9, column=1)

bt_scidmint = ttk.Button(root, text='scidmint', command=scidmint)
bt_scidmint.grid(row=0, column=2)

bt_scidpink = ttk.Button(root, text='scidpink', command=scidpink)
bt_scidpink.grid(row=1, column=2)

bt_scidpurple = ttk.Button(root, text='scidpurple', command=scidpurple)
bt_scidpurple.grid(row=2, column=2)

bt_scidsand = ttk.Button(root, text='scidsand', command=scidsand)
bt_scidsand.grid(row=3, column=2)

bt_smog = ttk.Button(root, text='smog', command=smog)
bt_smog.grid(row=4, column=2)

bt_ubuntu = ttk.Button(root, text='ubuntu', command=ubuntu)
bt_ubuntu.grid(row=5, column=2)

bt_vista = ttk.Button(root, text='vista', command=vista)
bt_vista.grid(row=6, column=2)

bt_winnative = ttk.Button(root, text='winnative', command=winnative)
bt_winnative.grid(row=7, column=2)

bt_winxpblue = ttk.Button(root, text='winxpblue', command=winxpblue)
bt_winxpblue.grid(row=8, column=2)

bt_xpnative = ttk.Button(root, text='xpnative', command=xpnative)
bt_xpnative.grid(row=9, column=2)

bt_yaru = ttk.Button(root, text='yaru', command=yaru)
bt_yaru.grid(row=10, column=1)


root.mainloop()