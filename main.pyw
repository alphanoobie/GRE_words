import pandas as pd
from datetime import date
from plyer import notification
import tkinter

#GUI
window = tkinter.Tk()
window.geometry('500x100',)
window.title("GRE Words")
window.config(bg='#fc3c49')
label1 = tkinter.Label(window, text="----------Today's Word And Its Meaning----------")
label1.config(font=("Comic Sans MS", 12, "bold"), bg="black", fg="White", relief="ridge", padx=5, pady=5)
label1.pack(fill='x')

#Reading CSV data
words_df = pd.read_csv("./data.csv", index_col="Index", parse_dates=True)

#Checking if a word for today already exist
todays_word_row = words_df[words_df['Displayed'] == str(date.today())]

def word_and_meaning():
    todays_word = todays_word_row['Word'].values[0]
    todays_meaning = todays_word_row['Meaning'].values[0]
    notification.notify(title="Today's word is: "+todays_word, message="and its meaning is: "+todays_meaning)
    label2 = tkinter.Label(window, text=todays_word+"\n"+"\n"+todays_meaning)
    label2.config(font=("Monospace" , 11, "bold"),bg="#fc3c49", fg="White",relief="sunken", padx=5, pady=2)
    label2.pack(fill="x")

#If today's word does not exist, fetching a new word and displaying it
if todays_word_row.empty:
    todays_word_row = words_df[words_df['Displayed'].isna()].sample()
    word_and_meaning()
    words_df.loc[words_df['Word'] == todays_word_row['Word'].values[0],'Displayed'] = date.today()
    words_df.to_csv('data.csv')

#Else display already existing today's word
else:
    word_and_meaning()

window.mainloop()

