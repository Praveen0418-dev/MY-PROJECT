import tkinter as tk 
#from tkinter import ttk
from tkinter import *
import ttkbootstrap as ttk

def convert():
    mile_input =entryInt.get()
    km_output = mile_input *1.61
    output_string.set(km_output)
   # print(km_output)
#window
# window = tk.Tk()
window =ttk.Window(themename = 'darkly')
window.title('Convert miles to km')
window.geometry('500x300')

#TITLE
titel_lable = ttk.Label(master= window, text ='miles to kilometres',font ='calibri 24 bold')
titel_lable.pack()


#input filed
input_fram =ttk.Frame(master=window )
entryInt=tk.IntVar()
entry =ttk.Entry(master=input_fram,textvariable=entryInt)
button=ttk.Button(master=input_fram,text='converter',command =convert)
entry.pack(side='left',padx=10)
button.pack(side='left')
input_fram.pack(pady=10)


#OUTPUT
output_string=tk.StringVar()
output_label=ttk.Label(
    master =window,
    text ='output',font='calibri 24',
    textvariable=output_string)
output_label.pack(pady=5)

#run
window.mainloop()