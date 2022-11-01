#designing the Screen
import tkinter as tk
window = tk.Tk()
window.geometry("780x540")
window.config(bg="yellow")
window.resizable(width=False,height=False)
window.title('||Simple Email Slicer||')
 
def result():
    try:
        email=entry.get()
        inp_email = email.strip()
        username = inp_email[0:inp_email.index('@')]
        domain = inp_email[inp_email.index('@') + 1:]
        text_box.delete('1.0', tk.END)
        msg = 'Email entered was: {}\n Your email username is : {}\n And your email domain server is : {}'
        msg_formatted = msg.format(email,username,domain.upper())
        text_box.insert(tk.END,msg_formatted)
        entry.delete(0, 'end')
    except:
        text_box.delete('1.0', tk.END)
        text_box.insert(tk.END,"ERROR! Its not the correct format. ")
 
def reset_all():
    text_box.delete('1.0', tk.END)
    entry.delete(0, 'end')
 
# Labels
greeting = tk.Label(text="Welcome to A Simple Email Slicer!",font=("Times",16),foreground="white",background="black")
Info = tk. Label(foreground= "white",background="#BE361A",font=("Comic Sans MS",16),text="Enter your Email ID and then click the done button!\n The application will extract your username and domain name.")
entry_label = tk.Label(foreground= "white",font=("Times",14),background="black",text="Enter Your Email ID: ")
result_label = tk.Label(font=("Comic Sans MS",14),foreground= "white",background="#BE361A",text="The results are as follows:")
empty_label0=tk.Label(background="yellow")
empty_label1=tk.Label(background="yellow")
empty_label2=tk.Label(background="yellow")
empty_label3=tk.Label(background="yellow")
empty_label4=tk.Label(background="yellow")
empty_label5=tk.Label(background="yellow")
 
#Entry
e1=tk.StringVar()
entry = tk.Entry(font=(11),width=50,justify='center',textvariable=e1)
 
#Buttons
button = tk.Button(text="Done!",command=result,font=(11))
reset=tk.Button(text="Reset!",command=reset_all,font=(11))
 
#Result
text_box = tk.Text(height=5,width=50)
 
#Packing Everything Together
empty_label0.pack()
greeting.pack()
Info.pack()
empty_label1.pack()
entry_label.pack()
empty_label4.pack()
entry.pack()
empty_label2.pack()
button.pack()
empty_label5.pack()
reset.pack()
empty_label3.pack()
result_label.pack()
text_box.pack()
 
window.mainloop()
