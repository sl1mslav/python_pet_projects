from tkinter import *
from shape_calculator.classes import *

win = Tk()
win.title("Shape Calculator")
win.geometry("840x600")

canvas = Canvas(win, bg='#C2D2FF')
canvas.pack(anchor='nw', fill='both', expand=1)
# canvas.create_line(200, 3, 200, 400)
canvas.create_polygon(200, 3, 208, 9, 192, 9)
canvas.create_line(200, 3, 200, 400)
canvas.create_line(3, 199, 400, 199)
canvas.create_line(225, 191, 225, 208)
canvas.create_line(191, 175, 209, 175)

canvas.create_polygon(400, 199, 392, 193, 392, 205)
Label(canvas, text="y", bg="#C2D2FF").place(x=210, y=3)
Label(canvas, text="x", bg="#C2D2FF").place(x=400, y=199)
Label(canvas, text="Choose dimension: ", bg="#C2D2FF").place(x=600, y=15)
dimension_var = IntVar()
dimension_var.set(1)
Radiobutton(canvas, text="2D", variable=dimension_var, value=1).place(x=610, y=40)
Radiobutton(canvas, text="3D", variable=dimension_var, value=2).place(x=660, y=40)
Label(canvas, text="Choose shape: ", bg="#C2D2FF").place(x=600, y=80)
shape_var = StringVar()
shape_var.set("Circle")
OptionMenu(canvas, shape_var, "Circle", "Square", "Rectangle", "Triangle", "Trapeze", "Rhombus").place(x=615, y=110)

shape_menu = Label(canvas, text="Enter the values below: ", bg="#C2D2FF")
shape_menu.place(x=600, y=160)

radius = Label(canvas, text="Radius: ", bg="#C2D2FF")
radius.place(x=590, y=190)
radius_value = Entry(canvas)
radius_value.place(height=16, x=700, y=190)

side1 = Label(canvas, text="Side: ", bg="#C2D2FF")
side1.place(x=590, y=210)
side1_value = Entry(canvas)
side1_value.place(height=16, x=700, y=210)

side2 = Label(canvas, text="Second side: ", bg="#C2D2FF")
side2.place(x=590, y=230)
side2_value = Entry(canvas)
side2_value.place(height=16, x=700, y=230)

side3 = Label(canvas, text="Third side: ", bg="#C2D2FF")
side3.place(x=590, y=250)
side3_value = Entry(canvas)
side3_value.place(height=16, x=700, y=250)

side4 = Label(canvas, text="Fourth side: ", bg="#C2D2FF")
side4.place(x=590, y=270)
side4_value = Entry(canvas)
side4_value.place(height=16, x=700, y=270)

diag1 = Label(canvas, text="First diagonal: ", bg="#C2D2FF")
diag1.place(x=590, y=290)
diag1_value = Entry(canvas)
diag1_value.place(height=16, x=700, y=290)

diag2 = Label(canvas, text="Second diagonal: ", bg="#C2D2FF")
diag2.place(x=590, y=310)
diag2_value = Entry(canvas)
diag2_value.place(height=16, x=700, y=310)

area = Label(canvas, text="Area: ", bg="#C2D2FF", font="Montserrat, 17")
area.place(x=40, y=500)
area_value = Label(canvas, text="", bg="#C2D2FF", font="Montserrat, 17")
area_value.place(x=110, y=500)

perimeter = Label(canvas, text="Perimeter: ", bg="#C2D2FF", font="Montserrat, 17")
perimeter.place(x=40, y=540)
perimeter_value = Label(canvas, text="", bg="#C2D2FF", font="Montserrat, 17")
perimeter_value.place(x=155, y=540)

# diag3_value.place_forget()
# diag3_value.place(height=16, x=700, y=310)

def showOrHide(*args):
    to_forget = (
        radius, radius_value,
        side1, side1_value,
        side2, side2_value,
        side3, side3_value,
        side4, side4_value,
        diag1, diag1_value,
        diag2, diag2_value
    )
    for i in to_forget:
        i.place_forget()
    if "radius" in args:
        radius.place(x=590, y=190)
        radius_value.place(height=16, x=700, y=190)
    if "side1" in args:
        side1.place(x=590, y=210)
        side1_value.place(height=16, x=700, y=210)
    if "side2" in args:
        side2.place(x=590, y=230)
        side2_value.place(height=16, x=700, y=230)
    if "side3" in args:
        side3.place(x=590, y=250)
        side3_value.place(height=16, x=700, y=250)
    if "side4" in args:
        side4.place(x=590, y=270)
        side4_value.place(height=16, x=700, y=270)
    if "diag" in args:
        diag1.place(x=590, y=290)
        diag1_value.place(height=16, x=700, y=290)
        diag2.place(x=590, y=310)
        diag2_value.place(height=16, x=700, y=310)


# 125, 260 STARTPOINT
# 199, 200 ZEROCOORD
def create_triangle(r0, r1, c):
    coord_list = sorted([r0, r1, c])
    coord_list = list(map(lambda x: x * (200 / (max(r0, r1, c))), coord_list))
    r0 = coord_list[0]
    r1 = coord_list[1]
    c = coord_list[2]
    a = (r0 ** 2 - r1 ** 2 + c ** 2) / (2 * c)
    h = (r0 ** 2 - a ** 2) ** 0.5
    print(a, h)
    canvas.create_line(125, 260, 125 + c, 260, fill="red")
    canvas.create_line(125, 260, 125 + a, 260 - h, fill="red")
    canvas.create_line(125 + a, 260 - h, 125 + c, 260, fill="red")

def create_circle(x, y, r): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    canvas.create_oval(x0, y0, x1, y1, outline="red")


def display_fields(*args):
    to_check = shape_var.get()
    if to_check == "Circle":
        showOrHide("radius")
    elif to_check == "Square":
        showOrHide("side1")
    elif to_check == "Rectangle":
        showOrHide("side1", "side2")
    elif to_check == "Triangle":
        showOrHide("side1", "side2", "side3")
    elif to_check == "Trapeze":
        showOrHide("side1", "side2", "side3", "side4")
    elif to_check == "Rhombus":
        showOrHide("diag")

def calculate(*args):
    shape = shape_var.get()
    shape_menu.config(text="Enter the values below: ", fg="black")
    if shape == "Circle":
        circle = Circle(int(radius_value.get()))
        create_circle(200, 199, circle.radius)
        area_value.config(text=f"{circle.area()}")
        perimeter_value.config(text=f"{circle.perimeter(circle)}")
    elif shape == "Triangle":
        try:
            triangle = Triangle(
                int(side1_value.get()),
                int(side2_value.get()),
                int(side3_value.get())
            )
        except ValueError:
            shape_menu.config(text="Incorrect values!", fg="red")
            return
        create_triangle(triangle.side1, triangle.side2, triangle.side3)
        area_value.config(text=f"{triangle.area()}")
        perimeter_value.config(text=f"{triangle.perimeter()}")



calculate_button = Button(canvas, text="Calculate", command=calculate)
calculate_button.place(x=615, y=400)
display_fields()
shape_var.trace("w", callback=display_fields)
win.mainloop()
