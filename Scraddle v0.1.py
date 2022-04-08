# Import module
from tkinter import *
from tkinter import messagebox
from random import randint
import numpy
import pandas

corpus = pandas.read_csv(r'C:/Users/Adam/Documents/Python Scripts/Scraddle Project/wordle2.csv')
corpus = corpus['x']

# initialize word list
word_list = corpus
  
# initial word length
word_length = 5

# initialize secret word as empty
secret_word = 'dummy'

# an empty list to hold and track user guesses
guess_history = numpy.empty(0, dtype = str)

# create tkinter object
root = Tk()
  
# adjust window size
root.geometry( "450x350" )

# begin layout
lbl_start = Label(text = "Word length:")
lbl_start.grid(row = 0, column = 0)

# datatype of menu text
clicked = IntVar()
clicked.set( 5 )

# create dropdown menu options
options = [
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15
]
  
# create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.grid(row = 0, column = 1)

label_spacer1 = Label( root , text = " " )
label_spacer1.grid(row = 0, column = 2)
  
def start():

    global corpus
    global word_list
    global secret_word

    # filter corpus to include words of a certain letter length
    word_list = corpus.loc[corpus.str.len() == clicked.get()]
    word_list = word_list.reset_index()['x']

    secret_word = word_list[randint(0, len(word_list))]

    # change button args
    btn_start['state'] = 'disabled'
    btn_start['bg'] = "gray"
    btn_reset['state'] = 'normal'
    btn_reset['bg'] = "red"
    drop['state'] = 'disabled'
    btn_submit['state'] = 'normal'
    btn_submit['bg'] = "green"
    enter_guess['state'] = 'normal'

# create start button defaults and map to start function
btn_start = Button( root , text = "Start Game", fg = "white", bg = "green", command = start, state = 'normal' )
btn_start.grid(row = 0, column = 3)

label_guess1 = Label( root, text = "Guess 1:", justify = 'right').grid(row = 3, column = 0)
guess1 = Label( root, text = " ", font = 6, justify = 'right')
guess1.grid(row = 3, column = 1)

label_guess2 = Label( root, text = "Guess 2:", justify = 'right').grid(row = 4, column = 0)
guess2 = Label( root, text = " ", font = 6, justify = 'right')
guess2.grid(row = 4, column = 1)

label_guess3 = Label( root, text = "Guess 3:", justify = 'right').grid(row = 5, column = 0)
guess3 = Label( root, text = " ", font = 6, justify = 'right')
guess3.grid(row = 5, column = 1)

label_guess4 = Label( root, text = "Guess 4:", justify = 'right').grid(row = 6, column = 0)
guess4 = Label( root, text = " ", font = 6, justify = 'right')
guess4.grid(row = 6, column = 1)

label_guess5 = Label( root, text = "Guess 5:", justify = 'right').grid(row = 7, column = 0)
guess5 = Label( root, text = " ", font = 6, justify = 'right')
guess5.grid(row = 7, column = 1)

label_guess6 = Label( root, text = "Guess 6:", justify = 'right').grid(row = 8, column = 0)
guess6 = Label( root, text = " ", font = 6, justify = 'right')
guess6.grid(row = 8, column = 1)

label_spacer2 = Label( root , text = " " )
label_spacer2.grid(row = 9, column = 0)

enter_guess = Entry( root , show = "", font = 6, state = 'disabled')
enter_guess.grid(row = 10, column = 1)

def eval_letters(guess):

    result = ' '
    global secret_word

    for i in range(len(guess)):
        if guess[i] == secret_word[i] :
            result = result + " " + guess[i].capitalize()
            next
        elif guess[i] in secret_word:
            result = result + " " + '*'
            next
        else:
            result = result + " " + '_'

    guess = guess + result
    return(guess)

def eval_guess():

    global guess_history
    global secret_word
    global enter_guess

    wd = enter_guess.get()

    if len(wd) != clicked.get():
        messagebox.showerror('Invalid Guess', wd.capitalize() + ' is not ' + str(clicked.get()) + ' letters long.')
    elif not wd.isalpha():
        messagebox.showerror('Invalid Guess', 'Remove spaces and characters.')
    elif len(word_list.loc[word_list == wd.lower()])==0:
        messagebox.showerror('Invalid Guess', wd.capitalize() + ' is not in the word list.')
    elif len(guess_history[guess_history == wd.lower()])==1:
        messagebox.showerror('Invalid Guess', wd.capitalize() + ' was already guessed.')
    elif len(word_list.loc[word_list == wd.lower()]) == 1:

        guess_history = numpy.append(guess_history, wd.lower())
        enter_guess.delete(0,END)

        # update guess texts
        if len(guess_history) == 1:
            guess1['text'] = eval_letters(wd.lower())
    
        if len(guess_history) == 2:
            guess2['text'] = eval_letters(wd.lower())

        if len(guess_history) == 3:
            guess3['text'] = eval_letters(wd.lower())

        if len(guess_history) == 4:
            guess4['text'] = eval_letters(wd.lower())

        if len(guess_history) == 5:
            guess5['text'] = eval_letters(wd.lower())

        if len(guess_history) == 6:
            guess6['text'] = eval_letters(wd.lower())

        # update letters remaining
        eval_unused(wd.upper())

        # define game outcomes
        if wd.lower() == secret_word:
            messagebox.showerror(title = 'You won!', message = secret_word.capitalize() + ' was the secret word.', icon = 'info')

            btn_submit['state'] = 'disabled'
            btn_submit['bg'] = "gray"
            enter_guess['state'] = 'disabled'

        elif len(guess_history) == 6:
            messagebox.showerror(title = 'You lost!', message = secret_word.capitalize() + ' was the secret word.', icon = 'error')

            btn_submit['state'] = 'disabled'
            btn_submit['bg'] = "gray"
            enter_guess['state'] = 'disabled'

label_spacer3 = Label( root , text = " " )
label_spacer3.grid(row = 10, column = 2)

btn_submit = Button( root, text = "Submit", fg = "white", bg = "gray", state = 'disabled', command = eval_guess)
btn_submit.grid(row = 10, column = 3)

label_spacer4 = Label( root , text = " " )
label_spacer4.grid(row = 10, column = 4)

def reset():

    global guess_history

    guess_history = numpy.empty(0, dtype = str) 

    # change button args
    btn_start['state'] = 'normal'
    btn_start['bg'] = "green"
    btn_reset['state'] = 'disabled'
    btn_reset['bg'] = "gray"
    drop['state'] = 'normal'
    btn_submit['state'] = 'disabled'
    btn_submit['bg'] = "gray"
    enter_guess.delete(0,END)
    enter_guess['state'] = 'disabled'
    guess1['text'] = ' '
    guess2['text'] = ' '
    guess3['text'] = ' '
    guess4['text'] = ' '
    guess5['text'] = ' '
    guess6['text'] = ' '
    unused1['text'] = "QWERT YUIOP"
    unused2['text'] = "ASDFG HJKL"
    unused3['text'] = "ZXCV BNM"

btn_reset = Button( root, text = "Reset", fg = "white", bg = "gray", command = reset, state = 'disabled')
btn_reset.grid(row = 10, column = 5)

unused1 = Label( root, text = "QWERT YUIOP", font = 5)
unused1.grid(row = 11, column = 1)
unused2 = Label( root, text = "ASDFG HJKL", font = 5)
unused2.grid(row = 12, column = 1)
unused3 = Label( root, text = "ZXCV BNM", font = 5)
unused3.grid(row = 13, column = 1)

def eval_unused(guess):

    for i in range(len(guess)):
        if guess[i] in unused1['text']:
            unused1['text'] = unused1['text'].replace(guess[i],'_')
        if guess[i] in unused2['text']:
            unused2['text'] = unused2['text'].replace(guess[i],'_')
        if guess[i] in unused3['text']:
            unused3['text'] = unused3['text'].replace(guess[i],'_')


# Execute tkinter
root.mainloop()