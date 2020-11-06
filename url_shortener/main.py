import pyperclip
import pyshorteners
from tkinter import *


# getting the large url, and making it short
def urlShortener():
    url_address_2 = url.get()  # getting the url
    url_short = pyshorteners.Shortener().tinyurl.short(url_address_2)  # shorting the url
    url_address.set(url_short)


# copying the link to the clipboard
def copy_url():
    url_short = url_address.get()  # getting the short url
    pyperclip.copy(url_short)  # clipping


# graphical user interface for the application
root = Tk()  # calling the tk object
root.geometry("400x200")  # dimensions
root.title("URL SHORTENER")  # a title
root.configure(bg="#49A")  # background color
url = StringVar()
url_address = StringVar()



# to install the libraries
# pip install pyshorteners
# pip install pyperclip
