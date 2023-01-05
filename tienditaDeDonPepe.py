
from tkinter import *  
# Top level window
frame = Tk()
frame.title("La tiendita de don Pepe")
frame.geometry("1000x400")
info = ["DNI", "Apellido", "Nombres", "direccion", "telefono", "Productos"]
info2 = ["Cod_Prod", "Descipcion","Unidad", "Cantidad","Precio", "Subtotal"]
rw = 1
myEntries= []
#titulo 
titulo = Label (frame , text = "La tiendita de Don Pepe",font=5).grid(column = 3, row = 0)
"""parte del boton"""
#creacion de valores
for x in info:
    lbl = Label(frame,text = x, font=5)
    lbl.grid(column =0,row=rw)
    inputTxt= Entry(frame)
    inputTxt.grid(column = 1, row =rw)
    
    if (x == "Nombres"):
        lbl = Label(frame, text = x, font = 5).grid (column = 3, row =2 ) 
        # TextBox Creation
        inputTxt = Entry(frame)
        inputTxt.grid(column = 4, row =2 )
        rw = rw -1 
    rw= rw+1
    myEntries.append(inputTxt)
    
#crear una caja para poner las respuestas 
respuesta = Label (frame, text = " ")
respuesta.grid(column = 4, row =4 )

# accion para el boton 
def defineValues():
    entryList =" "
    for entries in myEntries:
        entryList = entryList + str(entries.get()) + " "
        respuesta.config(text =entryList)
    print (entryList)


# creacion para el boton
printButton = Button(text = "Submit",command= defineValues,activebackground = "pink", activeforeground = "blue")
printButton.grid(column =3 , row =3)


frame.mainloop()