from tkinter import *
from tkinter import ttk
from views import *
from tkinter import messagebox

co0="#ffffff"
co1="#000000"
co2="#4456F0"

window=Tk()
window.title("")
window.geometry("485x450")
window.configure(background=co0)
window.resizable(width=FALSE,height=FALSE)

frame_up=Frame(window,width=500,height=50,bg=co2)
frame_up.grid(row=0,column=0,padx=0,pady=1)

frame_down=Frame(window,width=500,height=150,bg=co0)
frame_down.grid(row=1,column=0,padx=0,pady=1)

frame_table=Frame(window,width=500,height=100,bg=co0,relief='flat')
frame_table.grid(row=2,column=0,columnspan=2,padx=10,pady=1,sticky=NW)


def show():
    global tree

    listheader = ['Name', 'Telephone', 'Email', 'Address']

    demo_list=view()

    tree = ttk.Treeview(frame_table, selectmode="extended", columns=listheader,show="headings")

    vsb = ttk.Scrollbar(frame_table, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(frame_table, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0,row=0,sticky='nsew')
    vsb.grid(column=1,row=0,sticky='ns')
    hsb.grid(column=0,row=1,sticky='ew')

    tree.heading(0,text="Name",anchor=NW)
    tree.heading(1,text="Telephone",anchor=NW)
    tree.heading(2,text="Email id",anchor=NW)
    tree.heading(3,text="Address",anchor=NW)

    tree.column(0,width=120,anchor='nw')
    tree.column(1,width=100,anchor='nw')
    tree.column(2,width=140,anchor='nw')
    tree.column(3,width=190,anchor='nw')

    for item in demo_list:
        tree.insert('','end',values=item)

show()

def insert():
    Name= e_name.get()
    Telephone=e_telephone.get()
    Email=e_email.get()
    Address=e_address.get()

    data=[Name, Telephone, Email, Address]

    if Name==''or Telephone==''or Email=='' or Address=='':
        messagebox.showwarning('data','Please fill in all the details')
    else:
        add(data)
        messagebox.showinfo('data','Data added successfully')

        e_name.delete(0,'end')
        e_telephone.delete(0,'end')
        e_email.delete(0,'end')
        e_address.delete(0,'end')

        show()

def to_update():
    try:
        tree_data=tree.focus()
        tree_dictionary=tree.item(tree_data)
        tree_list=tree_dictionary['values']

        Name=str(tree_list[0])
        Telephone = str(tree_list[1])
        Email = str(tree_list[2])
        Address = str(tree_list[3])

        e_name.insert(0,Name)
        e_telephone.insert(0, Telephone)
        e_email.insert(0, Email)
        e_address.insert(0, Address)

        def confirm():
            new_name=e_name.get()
            new_telephone=e_telephone.get()
            new_email=e_email.get()
            new_address=e_address.get()

            data=[new_telephone,new_name,new_telephone,new_email,new_address]

            update(data)

            messagebox.showinfo('success','data updated successfully')

            e_name.delete(0,'end')
            e_telephone.delete(0,'end')
            e_email.delete(0,'end')
            e_address.delete(0,'end')

            for widget in frame_table.winfo_children():
                widget.destroy()

            b_confirm.destroy()

            show()

        b_confirm=Button(frame_down,text='Confirm',width=10,height=1,bg=co2,fg=co0,font=('Ivy 8 bold'),command=confirm)
        b_confirm.place(x=290,y=110)

    except IndexError:
        messagebox.showerror('Error','Select one of them from the table')

def to_remove():
    try:
        tree_data=tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']
        tree_telephone= str(tree_list[2])

        remove(tree_telephone)

        messagebox.showinfo('success','Data has been deleted successfully')

        for widget in frame_table.winfo_children():
            widget.destroy()
        show()

    except IndexError:
        messagebox.showerror('Error','Select one of them from the table')

def to_search():
    telephone=e_search.get()
    data=search(telephone)

    def delete_command():
        tree.delete(*tree.get_children())

    delete_command()

    for item in data:
        tree.insert('', 'end', values = item)

    e_search.delete(0, 'end')


app_name=Label(frame_up,text="Contactbook",height=1,font=('verdana 17 bold'),bg=co2,fg=co0)
app_name.place(x=5,y=5)

l_name=Label(frame_down,text="Name ",width=20,height=1,font=('Ivy 10'),bg=co0,anchor=NW)
l_name.place(x=10,y=20)
e_name=Entry(frame_down,width=25,justify='left',highlightthickness=1,relief='solid')
e_name.place(x=100,y=20)

l_telephone=Label(frame_down,text="Telephone",height=1,font=('Ivy 10'),bg=co0,anchor=NW)
l_telephone.place(x=10,y=50)
e_telephone=Entry(frame_down,width=25,justify='left',highlightthickness=1,relief='solid')
e_telephone.place(x=100,y=50)

l_email=Label(frame_down,text="Email-id  ",height=1,font=('Ivy 10'),bg=co0,anchor=NW)
l_email.place(x=10,y=80)
e_email=Entry(frame_down,width=25,justify='left',highlightthickness=1,relief='solid')
e_email.place(x=100,y=80)

l_address=Label(frame_down,text="Address  ",height=5,font=('Ivy 10'),bg=co0,anchor=NW)
l_address.place(x=10,y=110)
e_address=Entry(frame_down,width=25,justify='left',highlightthickness=1,relief='solid')
e_address.place(x=100,y=110)

b_search=Button(frame_down,text='Search',height=1,bg=co2,fg=co0,font=('Ivy 8 bold'),command=to_search)
b_search.place(x=290,y=20)
e_search=Entry(frame_down,width=16,justify='left',font=('Ivy',11),highlightthickness=1,relief='solid')
e_search.place(x=347,y=20)

b_view=Button(frame_down,text='View',width=10,height=1,bg=co2,fg=co0,font=('Ivy 8 bold'),command=show)
b_view.place(x=290,y=50)

b_add=Button(frame_down,text='Add',width=10,height=1,bg=co2,fg=co0,font=('Ivy 8 bold'),command=insert)
b_add.place(x=400,y=50)

b_update=Button(frame_down,text='Update',width=10,height=1,bg=co2,fg=co0,font=('Ivy 8 bold'),command=to_update)
b_update.place(x=290,y=80)

b_delete=Button(frame_down,text='Delete',width=10,height=1,bg=co2,fg=co0,font=('Ivy 8 bold'),command=to_remove)
b_delete.place(x=400,y=80)

window.mainloop()