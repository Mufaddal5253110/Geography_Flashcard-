import tkinter.messagebox as msg
from tkinter import *
from PIL import ImageTk,Image
from random import randint

root = Tk()
root.title("Geography Flashcard App")
root.geometry('200x50')
Label(root,text=u'\u00A9'+'Mufaddal Shakir').pack(side=BOTTOM,anchor='se')
root.iconbitmap('geography3.ico')

def ramdom_selection():
    # List of states
    global state_list
    state_list = ['andhra pradesh','andhrapradesh', 'arunachal pradesh','arunachalpradesh', 'assam', 'bihar',
                  'chhattisgarh', 'goa', 'gujarat','haryana', 'himachal pradesh', 'himachalpradesh', 'jharkhand',
                  'karnataka', 'kerala', 'madhya pradesh','madhyapradesh','maharashtra', 'manipur', 'meghalaya',
                  'mizoram', 'nagaland', 'odisha', 'punjab', 'rajasthan','sikkim', 'tamil nadu','tamilnadu',
                  'telangana', 'tripura', 'uttar pradesh', 'uttarpradesh', 'uttarakhand', 'west bengal', 'westbengal']

    # Random selection
    global rndm
    rndm = randint(0,len(state_list)-1)
    return rndm

def labling_img_state():
    img ="statemap\\"+state_list[rndm]+'.jpg'

    # Labeling image on screen
    global stateimg
    image = Image.open(img)
    image = image.resize((500, 500), Image.ANTIALIAS)
    stateimg=ImageTk.PhotoImage(image)
    state_label.config(image=stateimg)

def labling_img_capital_state():
    img ="statemap\\"+state_list[rndm]+'.jpg'

    # Labeling image on screen
    global state_capital_img
    image = Image.open(img)
    image = image.resize((500, 500), Image.ANTIALIAS)
    state_capital_img=ImageTk.PhotoImage(image)
    capital_label.config(image=state_capital_img)

def state_():

    # Clearing Screen
    dlt_prvs_opretion()

    state_frame.pack(fill=BOTH,expand=1)

    global state_label
    state_label=Label(state_frame)
    state_label.pack()

    # Calling function
    ramdom_selection()
    labling_img_state()
    # Creating button for random selection
    Button(state_frame, text='Next State', command=state_).pack()

    #Creating state entry
    global state_entry
    state_entry = Entry(state_frame,font=15,borderwidth=3)
    state_entry.pack(pady=10)

    # Button for search state
    search_button=Button(state_frame, text='Search',command=state_search)
    search_button.pack()


def state_search():
    global rndm
    if state_entry.get().lower() in state_list:
        rndm = state_list.index(state_entry.get().lower())
        labling_img_state()
        state_entry.delete(0,END)


    else:
        msg.showerror("Error","Invalid input please try again")

def check_capital():

    state_capital={

     'andhrapradesh':'amaravati','arunachalpradesh':'itanagar','assam':'guwahati','bihar':'patna','chhattisgarh':'raipur',
        'goa':'panaji','gujarat':'gandhinagar','haryana':'chandigarh','himachalpradesh':'shimla','jharkhand':'ranchi',
        'karnataka':'bengaluru','kerala':'thiruvananthapuram','madhyapradesh':'bhopal','maharashtra':'mumbai',
        'manipur':'imphal','meghalaya':'shillong','mizoram':'aizawl','nagaland':'kohima','odisha':'bhubaneswar',
        'punjab':'chandigarh','rajasthan':'jaipur','sikkim':'gangtok','tamilnadu':'chennai','telangana':'hyderabad',
        'tripura':'agartala','uttarpradesh':'lucknow','uttarakhand':'dehradun','westbengal':'kolkata'
    }

    if capital_entry.get().lower() == state_capital[state_list[rndm].replace(' ','')] :
        Label(capital_state_frame,text=f"Correct!\n{state_capital[state_list[rndm].replace(' ','')].title()} is the capital of {state_list[rndm].title()}").pack()
    else:
        Label(capital_state_frame, text=f"Incorrect!\n{state_capital[state_list[rndm].replace(' ','')].title()} is the capital of {state_list[rndm].title()}").pack()
    capital_entry.delete(0,END)
def state_capital_():

    # Clearing frame
    dlt_prvs_opretion()

    capital_state_frame.pack(fill=BOTH,expand=1)

    # Initally labling something into frame for further configuration
    global capital_label
    capital_label=Label(capital_state_frame)
    capital_label.pack()

    # Calling Function
    ramdom_selection()
    labling_img_capital_state()

    # Labeling Question
    Label(capital_state_frame,text="What is Capital of "+state_list[rndm].title()).pack()

    # Labeling answer entry
    global capital_entry
    capital_entry=Entry(capital_state_frame,font=15,borderwidth=3)
    capital_entry.pack(pady=10)

    # Button for check capital
    search_button=Button(capital_state_frame, text='Check',command=check_capital)
    search_button.pack()

    # Button for next map
    Button(capital_state_frame, text='Next', command=state_capital_).pack(pady=5)





def dlt_prvs_opretion():
    for widget in state_frame.winfo_children():
        widget.destroy()
    for widget in capital_state_frame.winfo_children():
        widget.destroy()
    state_frame.pack_forget()
    capital_state_frame.pack_forget()




# Main Menu

main_menu=Menu(root)

geography = Menu(main_menu,tearoff=0)

geography.add_command(label='State',command=state_)
geography.add_separator()
geography.add_command(label='State Capital',command=state_capital_)
geography.add_separator()
geography.add_command(label='Exit',command=exit)

main_menu.add_cascade(label='Geography',menu = geography)
root.config(menu=main_menu)

# Frames

state_frame = Frame(root,width=700,height=700)
capital_state_frame = Frame(root,width=700,height=700)



root.mainloop()