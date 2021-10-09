#Dependancies
import pandas as pd
from datetime import date
from plyer import notification
import tkinter

#Reading CSV data
words_df = pd.read_csv("./data.csv", index_col = "Index", parse_dates = True)

#Function to get today's word and its meaning
def get_word_and_meaning():
    """
    Fetches todays word from data.csv. If it doesn't exist, samples a random
    word.

    Input:
        -None
    Returns:
        -A tuple containing today's word and meaning
    """

    today = date.today()
    todays_word_row = words_df[words_df['Displayed'] == str(today)]
    #Checking if a word for today doesn't exist
    if todays_word_row.empty:
        #Fetching random word
        todays_word_row = words_df[words_df['Displayed'].isna()].sample()
        #Marking the word as today's word
        words_df.loc[words_df['Word'] == todays_word_row['Word'].values[0], 'Displayed'] = str(today)
        #Updating the csv file
        words_df.to_csv('data.csv')
    todays_word = todays_word_row['Word'].values[0]
    todays_meaning = todays_word_row['Meaning'].values[0]
    return (todays_word, todays_meaning)

def set_gui(word, meaning):
    """
    Creates the main GUI of the application.

    Input:
        -None
    Returns:
        -None
    """
    window = tkinter.Tk()
    window.geometry('500x100')
    window.title("GRE Words")
    window.config(bg = '#fc3c49')
    header_text = "----------Today's Word And Its Meaning----------"
    title_label = tkinter.Label(window, text = header_text)
    title_font = ("Comic Sans MS", 12, "bold")
    title_label.config(font = title_font, bg = "black",
                       fg = "White", relief = "ridge",
                       padx = 5, pady = 5)
    title_label.pack(fill = 'x')
    title = "Today's word is: " + word
    msg = "and its meaning is: " + meaning

    txt = word + "\n" + "\n" + meaning
    body_label = tkinter.Label(window, text = txt)
    body_font = ("Monospace" , 11, "bold")
    body_label.config(font = body_font, bg = "#fc3c49",
                      fg = "White", relief = "sunken",
                      padx = 5, pady = 2)
    body_label.pack(fill = "x")
    window.mainloop()

#Main entry point of the application
if __name__ == "__main__":
    word, meaning = get_word_and_meaning()
    notification.notify(title = word, message = meaning)
    set_gui(word, meaning)
