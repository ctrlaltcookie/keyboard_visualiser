from pynput.keyboard import KeyCode, Key, Listener
from tkinter import *
from tkinter import ttk

tk_window = Tk()
tk_window.geometry("380x180")
tk_window.config(bg="yellow")
# tk_window.wm_attributes("-transparentcolor", "white")

left_img = PhotoImage(file="img/left.png")
left_img_low = PhotoImage(file="img/left-low.png")
left = ttk.Label(tk_window, image=left_img_low, borderwidth=0, background="yellow")
left.place(x=10, y=10)

down_img = PhotoImage(file="img/down.png")
down_img_low = PhotoImage(file="img/down-low.png")
down = ttk.Label(tk_window, image=down_img_low, borderwidth=0, background="yellow")
down.place(x=50, y=50)

right_img = PhotoImage(file="img/right.png")
right_img_low = PhotoImage(file="img/right-low.png")
right = ttk.Label(tk_window, image=right_img_low, borderwidth=0, background="yellow")
right.place(x=90, y=10)

jump_img = PhotoImage(file="img/up.png")
jump_img_low = PhotoImage(file="img/up-low.png")
jump = ttk.Label(tk_window, image=jump_img_low, borderwidth=0, background="yellow")
jump.place(x=120, y=70)

punch_img = PhotoImage(file="img/punch.png")
punch_img_low = PhotoImage(file="img/punch-low.png")
punch = ttk.Label(tk_window, image=punch_img_low, borderwidth=0, background="yellow")
punch.place(x=210, y=50)

kick_img = PhotoImage(file="img/kick.png")
kick_img_low = PhotoImage(file="img/kick-low.png")
kick = ttk.Label(tk_window, image=kick_img_low, borderwidth=0, background="yellow")
kick.place(x=200, y=10)

slash_img = PhotoImage(file="img/slash.png")
slash_img_low = PhotoImage(file="img/slash-low.png")
slash = ttk.Label(tk_window, image=slash_img_low, borderwidth=0, background="yellow")
slash.place(x=240, y=10)

heavy_img = PhotoImage(file="img/heavy.png")
heavy_img_low = PhotoImage(file="img/heavy-low.png")
heavy = ttk.Label(tk_window, image=heavy_img_low, borderwidth=0, background="yellow")
heavy.place(x=280, y=10)

dust_img = PhotoImage(file="img/dust.png")
dust_img_low = PhotoImage(file="img/dust-low.png")
dust = ttk.Label(tk_window, image=dust_img_low, borderwidth=0, background="yellow")
dust.place(x=290, y=50)

dash_img = PhotoImage(file="img/dash.png")
dash_img_low = PhotoImage(file="img/dash-low.png")
dash = ttk.Label(tk_window, image=dash_img_low, borderwidth=0, background="yellow")
dash.place(x=250, y=50)

fd_img = PhotoImage(file="img/fd.png")
fd_img_low = PhotoImage(file="img/fd-low.png")
fd = ttk.Label(tk_window, image=fd_img_low, borderwidth=0, background="yellow")
fd.place(x=160, y=30)

# on press event
def on_press(key):
  if key == KeyCode(char="a"):
    left.configure(image=left_img)
  if key == KeyCode(char="s"):
    down.configure(image=down_img)
  if key == KeyCode(char="d"):
    right.configure(image=right_img)
  if key == Key.space:
    jump.configure(image=jump_img)
  if key == KeyCode(char="u"):
    kick.configure(image=kick_img)
  if key == KeyCode(char="j"):
    punch.configure(image=punch_img)
  if key == KeyCode(char="i"):
    slash.configure(image=slash_img)
  if key == KeyCode(char="o"):
    heavy.configure(image=heavy_img)
  if key == KeyCode(char="l"):
    dust.configure(image=dust_img)
  if key == KeyCode(char="k"):
    dash.configure(image=dash_img)
  if key == KeyCode(char="y"):
    fd.configure(image=fd_img)

# on release event
def on_release(key):
  if key == KeyCode(char="a"):
    left.configure(image=left_img_low)
  if key == KeyCode(char="s"):
    down.configure(image=down_img_low)
  if key == KeyCode(char="d"):
    right.configure(image=right_img_low)
  if key == Key.space:
    jump.configure(image=jump_img_low)
  if key == KeyCode(char="u"):
    kick.configure(image=kick_img_low)
  if key == KeyCode(char="j"):
    punch.configure(image=punch_img_low)
  if key == KeyCode(char="i"):
    slash.configure(image=slash_img_low)
  if key == KeyCode(char="o"):
    heavy.configure(image=heavy_img_low)
  if key == KeyCode(char="l"):
    dust.configure(image=dust_img_low)
  if key == KeyCode(char="k"):
    dash.configure(image=dash_img_low)
  if key == KeyCode(char="y"):
    fd.configure(image=fd_img_low)

keyboard_listener = Listener(
      on_press=on_press,
      on_release=on_release)

keyboard_listener.start()

tk_window.mainloop()
