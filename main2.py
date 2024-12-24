from tkinter import *



BACKGROUND_COLOR = "#B1DDC6"



# creating the GUI_____________________
window = Tk()
window.title("Flash-Cards")
window.config( padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas( width=800, height=526)
card_front_image =PhotoImage(file="card_front.png")
canvas.create_image(400,263, image=card_front_image)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400,263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan =2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

cross_image = PhotoImage(file="wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="right.png")
known_button = Button(image=check_image,highlightthickness=0)
known_button.grid(row=1, column=1)





window.mainloop()