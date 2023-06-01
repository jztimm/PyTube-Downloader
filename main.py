import tkinter
import customtkinter                        # Makes UI nicer on top of tkinter
from pytube import YouTube


def startDowload():
  try:
    ytLink = link.get()
    ytObject = YouTube(ytLink)
    video = ytObject.streams.get_highest_resolution()
    
    title.configure(text=ytObject.title, text_color="white")
    finishLabel.configure(text="")
    video.download()
    finishLabel.configure(text="Downloaded!", text_color="white")
  except:
    finishLabel.configure(text="YouTube link is invalid", text_color="red")


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDowload)
download.pack(padx=10, pady=10)



# Run app
app.mainloop()