from tkinter import *

import backend

def view_command():
    list1.delete(0,END)#delete everyth from zero to end
    for row in backend.view():
        list1.insert(END,row)#start at end then print

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def get_selected_row(event):
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    return (selected_tuple)
def delete_command():
    backend.delete(get_selected_row()[0])


window =Tk()

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l5=Label(window,text="ISBN")
l5.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=5,columnspan=3)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=7)

list1.config(yscrollcomman=sb1.set)#configures the boxes so that the scrollbar is adjusted as the box is scrolled
sb1.config(command=list1.yview)#configures the scroll bar to apply the scroll to the boxes

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="view all",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry",width=12,command=add_command)
b3.grid(row=4,column=3)


b5=Button(window,text="Update",width=12)
b5.grid(row=6,column=3)

b6=Button(window,text="Delete",width=12,command=delete_command)
b6.grid(row=67,column=3)




window.mainloop()