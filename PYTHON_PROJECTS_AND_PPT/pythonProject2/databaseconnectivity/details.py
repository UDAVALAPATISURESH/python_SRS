# # import tkinter
# from tkinter import *
# # import random module
# import random
# # Creating GUI window
# root = Tk()
# # Defining the container size, width=400, height=240
# root.geometry('400x240')
# root.title('Love Calculator????') # Title of the container
#
# # Function to calculate love percentage between the user ans partner
# def calculate_love():
#     st = '0123456789'  # value will contain digits between 0-9
#     digit = 2  # result will be in double digits
#     temp = "".join(random.sample(st, digit))  # result
#     result.config(text=temp)
#
#
# # Heading on Top
# heading = Label(root, text='Love Calculator????')
# heading.pack()
#
# # Slot/input for the first name
# slot1 = Label(root, text="Enter Your Name:")
# slot1.pack()
# name1 = Entry(root, border=5)
# name1.pack()
#
# # Slot/input for the partner name
# slot2 = Label(root, text="Enter Your Partner Name:")
# slot2.pack()
# name2 = Entry(root, border=5)
# name2.pack()
#
# # create a Button and place at a particular
# # location inside the root window .
# # when user press the button, calculate_love function
# # affiliated to that button is executed .
# # 'text' used to define text on button and
# # height and width defines those properties of button
# bt = Button(root, text="Calculate", height=1,
#             width=7, command=calculate_love)
# bt.pack()
#
# # Text on result slot
# result = Label(root, text='Love Percentage between both of You:')
# result.pack()
#
# # Starting the GUI
# root.mainloop()
