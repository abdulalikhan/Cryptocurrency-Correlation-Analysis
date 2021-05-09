from tkinter import *
from tkinter import messagebox
from correlation import calc_correlation
from correlation import crypto
from correlation import selected_crypto


def make_ui():
    root = Tk()
    root.geometry('600x650')
    root.resizable(False, False)
    root.configure(background='#202a38')
    root.title("Cryptocurrency Correlation Analysis")
    heading = Label(root, text="Cryptocurrency Correlation Analysis", font=("Arial Bold", 22), fg='#ce3f3f', bg='#202a38').grid(row=0, sticky=W, padx=(50, 10), pady=(5, 5))
    lbl = Label(root, text=".:: Select Cryptocurrencies (Total: {0}) ::.".format(len(crypto)), font=("Arial Bold", 13), fg='#ce3f3f', bg='#202a38')
    listbox = Listbox(root, height=17, selectmode='multiple', font=("Arial Bold", 13), fg='#ffffff', bg='#363f4b', selectbackground="#d25252")
    scrollbar = Scrollbar(root, orient=VERTICAL)
    listbox.config(yscrollcommand=scrollbar.set)
    listbox.configure(justify=CENTER)
    scrollbar.config(command=listbox.yview)
    for elem in crypto:
        listbox.insert(END, elem)
    s_date_lbl = Label(root, text="Start date:", font=("Arial Bold", 13), fg='#ce3f3f', bg='#202a38')
    start_date = Entry(root, font=("Arial Bold", 13), fg='#ffffff', bg='#202a38', bd=5)
    start_date.insert(0, "YYYY-MM-DD")
    e_date_lbl = Label(root, text="End date:", font=("Arial Bold", 13), fg='#ce3f3f', bg='#202a38')
    end_date = Entry(root, font=("Arial Bold", 13), fg='#ffffff', bg='#202a38', bd=5)
    end_date.insert(0, "YYYY-MM-DD")

    def update_selected_list():
        conf_msg = "Are you sure you would like to perform a correlation analysis on the selected cryptos?"
        choice = messagebox.askyesno("Confirmation", conf_msg)
        if not choice:
            return
        selected_crypto.clear()
        for i in listbox.curselection():
            selected_crypto.append(listbox.get(i))
        start_str = start_date.get()
        end_str = end_date.get()
        try:
            print("OK")
            calc_correlation(start_str, end_str)
        except:
            messagebox.showerror("Error", "An unexpected error occurred.")
    btn = Button(root, text='Analyze', font=("Arial Bold", 18), fg='#ffffff', bg='#ce3f3f', command=update_selected_list)
    s_date_lbl.grid()
    start_date.grid(pady=(5, 5))
    e_date_lbl.grid()
    end_date.grid(pady=(5, 10))
    lbl.grid()
    listbox.grid(pady=(5, 10), row=6, sticky=E+W+N)
    scrollbar.grid(row=6, column=1, sticky=NS)
    btn.grid(pady=(10, 0))
    root.mainloop()


if __name__ == '__main__':
    make_ui()
