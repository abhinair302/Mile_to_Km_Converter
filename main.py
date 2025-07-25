from tkinter import *

window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=200,height=100)

#Label

my_label=Label(text="Miles",font=("Calibri",11))
my_label.grid(column=2,row=0)

statement_label=Label(text="is equal to",font=("Calibri",11))
statement_label.grid(column=0,row=1)

ans_label=Label(text=0,font=("Calibri",11))
ans_label.grid(column=1,row=1)

unit_label=Label(text="Km",font=("Calibri",11))
unit_label.grid(column=2,row=1)


def button_clicked():
    new_text=input.get()
    data=int(new_text)
    final_ans=data*1.60934
    ans_label.config(text=final_ans)

button=Button(text="Calculate",command=button_clicked)
button.grid(column=1,row=2)

input=Entry(width=5)
input.grid(column=1,row=0)
print(input.get())

window.mainloop()