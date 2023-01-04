from tkinter import *  # impordime kõik

from Circle import Circle


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def calculate(event):
    # print('Button clicked')  # Testimine
    radius = user_input.get()
    # print(radius)  # Test
    if is_float(radius):
        user_input.delete(0, END)  # CLEAR INPUT
        radius = float(radius)  # nüüd on radius float
        circle = Circle(radius)
        txt_field['state'] = 'normal'  # can change field , saan teksti välja muuta
        txt_field.delete('1.0', END)  # Kustutab enne uut sisestust esimesest reast kuni lõpuni
        txt_field.insert(END, 'Radius: ' + str(circle.radius) + '\n')  # end paneb kõife lõppu
        txt_field.insert(END, 'Diameter: ' + str(circle.diameter()) + '\n')
        txt_field.insert(END, 'Perimeter: ' + str(circle.perimeter()) + '\n')
        txt_field.insert(END, 'Area: ' + str(circle.area()) + '\n')
        txt_field['state'] = 'disabled'  # nüüd ei saa kasutaja muuta

       # print('Number')  # Test
   # else: # Test
        # print('Error')  # Test


# main window properties
window = Tk()  # see loob graafilise akna  (tk aken tiitel riba)
window.title('Geometry - Circle')  # Tekst mida soovin aknal näha
window.geometry('400x500')  # akna suurus w=100 h=500
window.resizable(False, True)  # selliselt ei saa kõrgust muuta aga laiust
# saab muuta, võid ka kõik True panna saad kõike muuta laius ja kõrgus

# Frames
frame_top = Frame(window, bg='#89CFF0', height=50)  # sellega lõime freimi, see läks põhiakna peale laius 50 pix ja värv sinine
frame_top.pack(fill='both')  # both on igatpidi. saab panna ka x ja y

frame_bottom = Frame(window, bg='#90EE90', height=50)
frame_bottom.pack(fill=BOTH)  # both võib kirjutada suure v väikeste tähtedega

# First line inf frame top
lbl = Label(frame_top, text='Circle radius', bg='#89CFF0')  # kuhu pannakse (frame top) milline tekst text= circle radius
lbl.pack(side='left')  # see toob välja

user_input = Entry(frame_top)  # sisestamis väli
user_input.pack(side=LEFT)
user_input.focus()

btn_calc = Button(frame_top, text='Calculate', command=lambda: calculate(0)) # null peab olema, nüüd saime et enter ja aruvta nupp töötavad
btn_calc.pack(side=LEFT, padx=5, pady=5)  # vahe calculate nuppu äärest vasakult ja alt


# Second line, one big textfield

txt_field = Text(frame_bottom, state=DISABLED)  # teksti kast
txt_field.pack(side='left', padx=2, pady=2, expand=True)

# Bind Entry key
window.bind('<Return>', lambda event: calculate(event))  # enter klahv teeb ka arvutuse


window.mainloop()  # aken
