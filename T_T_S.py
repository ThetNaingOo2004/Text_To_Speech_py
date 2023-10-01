import pyttsx3
import customtkinter as ctk

def text_to_say():
    ttx = pyttsx3.init()
    ttx.say(text_input.get())
    ttx.runAndWait()

window = ctk.CTk()

window.geometry("500x200")
window.title("Text to Speech")
title_label = ctk.CTkLabel(window, text="Text to Speech", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10,pady=(30,20))

Input_Frame = ctk.CTkFrame(window)
Input_Frame.pack(fill="x", padx=50)

text_input = ctk.CTkEntry(Input_Frame, width=300, height=50, placeholder_text="enter a text...")
text_input.pack(side="left", padx=(20,0), pady=20)

speak_button = ctk.CTkButton(Input_Frame, text="Say", command=text_to_say)
speak_button.pack(side="left", padx=10, pady=20)


window.mainloop()
