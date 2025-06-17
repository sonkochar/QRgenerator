import qrcode
from tkinter import *
from tkinter import colorchooser
from PIL import ImageTk, Image


main = Tk()
main.geometry("500x800")
main.title("QR code generator")

def generate_qr():
    data = data_entry.get().strip()
    fill_color = fill_color_var.get()
    back_color = back_color_var.get()

    if not data:
        result_label.config(text="Please enter valid input for QR code!", fg = 'red')
        return

    qr = qrcode.QRCode(
        version=6,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=5,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save("qrcode.png")
    display_qr()

def display_qr():
    img = Image.open("qrcode.png")
    img = img.resize((300, 300), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    qr_image_label.config(image=img_tk)
    qr_image_label.image = img_tk

def choose_fill_color():
    color = colorchooser.askcolor(title="Choose Fill Color")
    if color[1]:
        fill_color_var.set(color[1])

def choose_back_color():
    color = colorchooser.askcolor(title="Choose Background Color")
    if color[1]:
        back_color_var.set(color[1])


fill_color_var = StringVar(value="black")
back_color_var = StringVar(value="white")

Label(main, text="Enter text or URL:").pack(pady=5)
data_entry = Entry(main, width=50)
data_entry.pack(pady=5)

Label(main, text="Choose fill color:").pack(pady=5)
Button(main, text="Select Fill Color", command=choose_fill_color,width=30).pack(pady=5)

Label(main, text="Choose background color:").pack(pady=5)
Button(main, text="Select Background Color", command=choose_back_color,width=30).pack(pady=5)

Button(main, text="Generate QR Code", command=generate_qr).pack(pady=20)
result_label = Label(main, text="")
result_label.pack(pady=5)


qr_image_label = Label(main)
qr_image_label.pack(pady=5)


main.mainloop()
