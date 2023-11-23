# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 20:27:53 2023

@author: falconrex22
"""

from tkinter import*

root = Tk()
root.title("Serie Fibinacci")
root.geometry("400x400")
root.configure(background = "red")
label_series = Label(root, text="Serie Fibonacci:  ", bg="cyan" )
label_suma = Label(root, bg= "green")

enter_word = Entry(root)

label = Label(root, text="Serie Fibonacci", bg="cyan")

def Fibonacci(): #defino funcion
    entry = int(enter_word.get())
    first = 0 
    second = 1 
    sum = 0
    sum2 = 0
    counter = 1
    while (counter <= entry):
        #sum contiene la serie Fibonacci
        #str convierte el valor a cadena
        label_series["text"] += str(sum) + " "
        counter = counter + 1
        first = second
        second = sum
        sum = first + second
        sum2 = sum2 + sum
    #mostrar los textos en etiquetas    
    label_suma["text"] = "El total de espirales es  " + str(sum2)
        
btn = Button(root, text="Muestra la serie fibonacci", command= Fibonacci, bg="blue")
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
label_series.place(relx= 0.5, rely= 0.7, anchor=CENTER)
enter_word.place(relx= 0.5, rely= 0.3, anchor= CENTER)
label_suma.place(relx= 0.5, rely= 0.1, anchor= CENTER)

root.mainloop()