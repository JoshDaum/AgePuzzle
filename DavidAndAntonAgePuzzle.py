# This is a tool I built to help me think through one of Matt Parker's Maths Puzzles. The puzzle is:
#
# David and Anton's ages combined equals 65. David is currently three times as old as Anton was when
# David was half as old as Anton will be when Anton is three times as old as David was when David was
# three times as old as Anton. How old is David?
#
# I was working with spreadsheets and graphs, and everything was just a little too chaotic to look at to be
# useful (to me) in finding an answer. This visualization allowed me to look at one specific pair of ages and see
# all of the ramifications of those ages for the rest of the puzzle.

# THIS IS NOT PRETTY CODE -- I fully acknowledge that!
# I just roughed this out quickly to help me think through the puzzle. :)

import tkinter as tk
from tkinter import *
master = tk.Tk()
master.title("Matt Parker's Maths Puzzles Age Puzzle")

def updateAnton(antonNew):
    anton = float(antonNew)
    david = 65 - anton
    d.set(david)
    updateLabels()

def updateDavid(davidNew):
    david = float(davidNew)
    anton = 65 - david
    a.set(anton)
    updateLabels()

def updateLabels():
    rLabelString.set("If Anton is " + str(a.get()) + " and David is " + str(d.get()) + ", then:")
    david = d.get()
    anton = a.get()

    # The variable names get crazy here -- I'm better at naming variables than this!  But this was my
    # "working out" of the problem by using variable names to think through the steps.
    oneThirdDavid = david / 3
    antonWasThatOldYrsAgo = anton - oneThirdDavid
    thenDavidWas = david - antonWasThatOldYrsAgo
    twiceThatAge = thenDavidWas * 2
    oneThirdThat = twiceThatAge / 3
    davidWasThatYearsAgo = david - oneThirdThat
    antonThatManyYearsAgo = anton - davidWasThatYearsAgo

    # Evaluate the truth condition in the final step of the problem: David was three times as old as Anton
    doesItWork = oneThirdThat / 3 == antonThatManyYearsAgo
    if doesItWork == True:
        ansString = "This is correct, because " + str(antonThatManyYearsAgo) + " is one third of " + str(oneThirdThat)
    else:
        ansString = "This is incorrect, because " + str(antonThatManyYearsAgo) + " is not one third of " + str(oneThirdThat)

    # Set the text for the problem explanation
    line1String.set("One third of David's age is " + str(oneThirdDavid))
    line2String.set("When Anton was that age, twice David's age was " + str(twiceThatAge))
    line3String.set("When Anton's age is " + str(twiceThatAge) + ", one third of that will be " + str(oneThirdThat))
    line4String.set("When David is that age, Anton will be " + str(antonThatManyYearsAgo) + ".")
    line5String.set(ansString)

# Define the GUI elements
aLabel = Label(master, text = "Anton")
a = tk.Scale(master, length = 1000, orient='horizontal', from_=0.01, to=64.99, resolution=0.01, command = updateAnton)

separator1 = Frame(height=10, bd=1, relief=SUNKEN)

dLabel = Label(master, text = "David")

d = tk.Scale(master, length = 1000, orient='horizontal', from_=0.01, to=64.99, resolution=0.01, command = updateDavid)
a.set(65 - d.get())

separator2 = Frame(height=10, bd=1, relief=SUNKEN)

# "rams" is short for "ramifications" -- the ramifications of the given ages on the conditions in the rest of the puzzle
rLabelString = StringVar()
ramsLabel = Label(master, textvariable=rLabelString)

line1String = StringVar()
line2String = StringVar()
line3String = StringVar()
line4String = StringVar()
line5String = StringVar()

ramsLine1 = Label(master, textvariable=line1String, anchor='w')
ramsLine2 = Label(master, textvariable=line2String)
ramsLine3 = Label(master, textvariable=line3String)
ramsLine4 = Label(master, textvariable=line4String)
ramsLine5 = Label(master, textvariable=line5String)


# Pack the GUI elements
aLabel.pack()
a.pack()
separator1.pack(fill=X, padx=5, pady=5)
dLabel.pack()
d.pack()
separator2.pack(fill=X, padx=5, pady=5)
ramsLabel.pack()
ramsLine1.pack()
ramsLine2.pack()
ramsLine3.pack()
ramsLine4.pack()
ramsLine5.pack()

# Do the thing
tk.mainloop()


