from tkinter import *
root=Tk()
root.geometry("600x400")
root.configure(background='orange')
root.title("Definations")

label_of_lists = Label(root)
label_of_tuples = Label(root)
label_of_functions = Label(root)

categories = {'Lists' : 'Are used for storing specific elements, which can be printed',
              'Tuples' : 'Are same as list, just it used small bracked to store the elements',
              'Functions' : 'Are used to perform a specific purpose or a function'}

def lists():
    label_of_lists["text"] = categories['Lists']
    
def tuples():
    label_of_tuples["text"] = categories['Tuples']
    
def functions():
    label_of_functions["text"] = categories['Functions']
    
button_lists= Button(root, text = "Meaning of Lists", command = lists())
button_lists.place(relx = 0.5, rely = 0.2, anchor = CENTER)

label_of_lists.place(relx = 0.5, rely = 0.3, anchor = CENTER)

button_tuples= Button(root, text = "Meaning of Tuples", command = tuples())
button_tuples.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label_of_tuples.place(relx = 0.5, rely = 0.5, anchor = CENTER)

button_functions= Button(root, text = "Meaning of Functions", command = functions())
button_functions.place(relx = 0.5, rely = 0.6, anchor = CENTER)

label_of_functions.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()