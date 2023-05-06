# Kaveh Sabouri

import customtkinter
from tkinter import colorchooser
import pyperclip

customtkinter.set_appearance_mode("dark")
window = customtkinter.CTk()
window.title("Color Chooser")
window.geometry("500x500")
window.config(bg="#009FB7")
window.resizable(False,False)

def choose_color():
    def copy2():
        pyperclip.copy(colorHex)
    btn_copy = customtkinter.CTkButton(window , text="Copy",text_font=("Lalezar",35),command=copy2,fg_color="#FED766",text_color="#FE4A49",width=200,height=18)
    btn_copy.place(x=250,y=400)
    choose_color_btn.place(x=25,y=400)
    color=colorchooser.askcolor()
    colorHex=color[1]
    window.config(bg=colorHex)
    hex_color_label=customtkinter.CTkLabel(text="Your Hex color is:",text_font=("Lalezar",25),bg=colorHex)
    hex_color_label.place(x=60,y=100)
    hex_color_label2=customtkinter.CTkLabel(window,text=colorHex,text_font=("Lalezar",25),bg=colorHex)
    hex_color_label2.place(x=300,y=100)
    if colorHex=="#fffff":
      window.config(bg="#fc8803")

    

choose_color_btn = customtkinter.CTkButton(window , text="Choose color",text_font=("Lalezar",35),command=choose_color,fg_color="#FED766",text_color="#FE4A49")
def b11 ():
    pick_color_btn.destroy()
    list_of_colors.destroy()
    about_btn.destroy()
    choose_color_btn.place(x=150,y=250)


def b22():
    color_picker_label.destroy()
    pick_color_btn.destroy()
    list_of_colors.destroy()
    about_btn.destroy()

    list_colors_code=customtkinter.CTkLabel(window,text="List of Colors Code",text_font=("Lalezar",55),bg="#fc8803",text_color="#FED766")
    list_colors_code.pack()

    red_txt=customtkinter.CTkLabel(window,text="Red:",text_font=("Lalezar",35),text_color="red",bg="#fc8803")
    red_txt.place(x=60,y=100)

    red_code=customtkinter.CTkLabel(window,text="#ff3600",text_font=("Lalezar",35),text_color="red",bg="#fc8803")
    red_code.place(x=300,y=100)

    blue_txt=customtkinter.CTkLabel(window,text="Blue:",text_font=("Lalezar",35),text_color="blue",bg="#fc8803")
    blue_txt.place(x=60,y=160)

    blue_code=customtkinter.CTkLabel(window,text="#0432ff",text_font=("Lalezar",35),text_color="blue",bg="#fc8803")
    blue_code.place(x=300,y=160)

    green_txt=customtkinter.CTkLabel(window,text="Green:",text_font=("Lalezar",35),text_color="green",bg="#fc8803")
    green_txt.place(x=60,y=220)

    green_code=customtkinter.CTkLabel(window,text="#00f900",text_font=("Lalezar",35),text_color="green",bg="#fc8803")
    green_code.place(x=300,y=220)

    yellow_txt=customtkinter.CTkLabel(window,text="Yellow:",text_font=("Lalezar",35),text_color="yellow",bg="#fc8803")
    yellow_txt.place(x=60,y=280)

    yellow_code=customtkinter.CTkLabel(window,text="#fefb00",text_font=("Lalezar",35),text_color="yellow",bg="#fc8803")
    yellow_code.place(x=300,y=280)

    orange_txt=customtkinter.CTkLabel(window,text="Orange:",text_font=("Lalezar",35),text_color="orange",bg="#fc8803")
    orange_txt.place(x=60,y=340)

    orange_code=customtkinter.CTkLabel(window,text="#ff9200",text_font=("Lalezar",35),text_color="orange",bg="#fc8803")
    orange_code.place(x=300,y=340)

def b33():
    color_picker_label.destroy()
    pick_color_btn.destroy()
    list_of_colors.destroy()
    about_btn.destroy()



color_picker_label=customtkinter.CTkLabel(text="Color-Picker",text_font=("Lalezar",55),bg="#fc8803",text_color="#FED766")
color_picker_label.pack()

pick_color_btn= customtkinter.CTkButton(window,text="Pick a Color",text_font=("Lalezar",35),command=b11,width=250,height=25,fg_color="#FED766",text_color="#FE4A49")
pick_color_btn.place(x=130,y=160)

list_of_colors= customtkinter.CTkButton(window,text="List of Colors",text_font=("Lalezar",35),command=b22,width=250,height=25,fg_color="#FED766",text_color="#FE4A49")
list_of_colors.place(x=130,y=260)

about_btn = customtkinter.CTkButton(window,text="About",text_font=("Lalezar",35),command=b33,width=250,height=25,fg_color="#FED766",text_color="#FE4A49")
about_btn.place(x=130,y=360)


window.mainloop()