import pyperclip
import pyshorteners
from tkinter import *


# getting the large url, and making it short
def urlShortener():
    url_address_2 = link.get()  # getting the link from the input
    print(url_address_2)
    short_url = pyshorteners.Shortener().tinyurl.short(url_address_2)  # making it short
    url_address.set(short_url)


# copying the link to the clipboard
def copy_url():
    url_short = url_address.get()  # getting the short url
    pyperclip.copy(url_short)  # clipping


if __name__ == '__main__':
    # graphical user interface for the application
    root = Tk()  # calling the tk object
    root.geometry("400x200")  # dimensions
    root.title("URL SHORTENER")  # a title
    root.configure(bg="#49A")  # background color
    link = StringVar()
    url_address = StringVar()

    # adding elements ot the interface
    Label(root, text="My URL Shortener", font="poppins").pack(pady=10)  # adding a title
    Entry(root, textvariable="link").pack(pady=5)  # adding an input
    Button(root, text="Generate Short URL", command=urlShortener).pack(pady=7)  # button that calls the urlShortener
    Entry(root, textvariable=url_address).pack(pady=5)  # the short url output
    Button(root, text="Copy URL", command=copy_url).pack(pady=5)  # button that copies the url

    root.mainloop()

# to install the libraries
# pip install pyshorteners
# pip install pyperclip
