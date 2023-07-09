from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ''

precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''

def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_bebidas:
        if variables_bebida[x].get() == 1:
            cuadros_bebidas[x].config(state=NORMAL)
            if cuadros_bebidas[x].get() == '0':
                cuadros_bebidas[x].delete(0, END)
            cuadros_bebidas[x].focus()
        else:
            cuadros_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set('0')
        x += 1

    x = 0
    for c in cuadros_postres:
        if variables_postre[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1

def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebidas = 0
    p = 0
    for cantidad in texto_bebidas:
        sub_total_bebidas = sub_total_bebidas + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1

    sub_total = sub_total_comida + sub_total_postres + sub_total_bebidas
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
    var_costo_bebidas.set(f'$ {round(sub_total_bebidas, 2)}')
    var_costo_postres.set(f'$ {round(sub_total_postres, 2)}')
    var_costo_subtotal.set(f'$ {round(sub_total, 2)}')
    var_costo_impustos.set(f'$ {round(impuestos, 2)}')
    var_costo_total.set(f'$ {round(total, 2)}')

def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'DATOS:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 63 + '\n')
    texto_recibo.insert(END, f'Items\t\t Cant.\tCosto Items\n ')
    texto_recibo.insert(END, f'_' * 41 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comida[x]}\t\t'
                                     f'{comida.get()}\t{int(comida.get()) * precios_comida[x]}\n')
        x += 1

    x = 0
    for bebida in texto_bebidas:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebida[x]}\t\t'
                                     f'{bebida.get()}\t{int(bebida.get()) * precios_bebida[x]}\n')
        x += 1

    x = 0
    for postres in texto_postres:
        if postres.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t'
                                     f'{postres.get()}\t{int(postres.get()) * precios_postres[x]}\n')
        x += 1

    texto_recibo.insert(END, f'_' * 41 + '\n')
    texto_recibo.insert(END, f'Costo de la comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de la bebida: \t\t\t{var_costo_bebidas.get()}\n')
    texto_recibo.insert(END, f'Costo del postre: \t\t\t{var_costo_postres.get()}\n')
    texto_recibo.insert(END, f'_' * 41 + '\n')
    texto_recibo.insert(END, f'Sub-Total: \t\t\t{var_costo_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t{var_costo_impustos.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t{var_costo_total.get()}\n')
    texto_recibo.insert(END, f'*' * 63 + '\n')
    texto_recibo.insert(END, f'Lo esperamos pronto')

def guardar():
    info_recivo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recivo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')

def resetear():
    texto_recibo.delete(1.0, END)

    for texto in texto_comida:
        texto.set('0')

    for texto in texto_bebidas:
        texto.set('0')

    for texto in texto_postres:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)

    for cuadro in cuadros_bebidas:
        cuadro.config(state=DISABLED)

    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set(0)

    for v in variables_bebida:
        v.set(0)

    for v in variables_postre:
        v.set(0)

    var_costo_comida.set('')
    var_costo_bebidas.set('')
    var_costo_postres.set('')
    var_costo_subtotal.set('')
    var_costo_impustos.set('')
    var_costo_total.set('')

#iniciar tkinter
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry('1320x630+0+0')

# evitar maximizar
aplicacion.resizable(0, 0)

# titulo de la ventana
aplicacion.title('RESTAURANTE - SISTEMA DE FACTURACION')

# color de fondo de la pantalla
aplicacion.config(bg='CadetBlue')

# panel superior
panel_superio = Frame(aplicacion, bd=1, relief=FLAT)
panel_superio.pack(side=TOP)

# etiqueta de titulo
etiqueta_titulo = Label(panel_superio, text='Sistema de Facturacion',
                        fg='DarkSlateGrey', font=('Dosis', 58),bg='CadetBlue',
                        width=20)

etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=130)
panel_costos.pack(side=BOTTOM)

# panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida',
                           font=('dosis', 19, 'bold'), bd=1,
                           relief=FLAT, fg='DarkSlateGrey')
panel_comidas.pack(side=LEFT)

# panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas',
                           font=('dosis', 19, 'bold'), bd=1,
                           relief=FLAT, fg='DarkSlateGrey')
panel_bebidas.pack(side=LEFT)

# panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres',
                           font=('dosis', 19, 'bold'), bd=1,
                           relief=FLAT, fg='DarkSlateGrey')
panel_postres.pack(side=LEFT)

# panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(aplicacion, bd=1, relief=FLAT,
                          bg='CadetBlue')
panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(aplicacion, bd=1, relief=FLAT,
                          bg='CadetBlue')
panel_recibo.pack()

# panel botones
panel_botones = Frame(aplicacion, bd=1, relief=FLAT,
                          bg='CadetBlue')
panel_botones.pack()

#listas_productos
lista_comida = ['Papa','Empanada','Arepa rellena','Aborrajado',
         'Marranita','Dedo','Panzeroti']

lista_bebida = ['Jugos naturales','Gaseosas','Lacteos','Cafe','Milo',
          'Aromatica','chocolate']

lista_postres = ['helado','fruta','brownes','flan','mouse','pastel1','pastel2']

# generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comida:

    # crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis',19,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis',18,'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=1)

    contador += 1


# generar items bebida
variables_bebida = []
cuadros_bebidas = []
texto_bebidas = []
contador = 0
for bebida in lista_bebida:

    # crear checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis',19,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadros_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set('0')
    cuadros_bebidas[contador] = Entry(panel_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebidas[contador])
    cuadros_bebidas[contador].grid(row=contador, column=1)

    contador += 1

# generar items postre
variables_postre = []
cuadros_postres = []
texto_postres = []
contador = 0
for postre in lista_postres:

    # crear checkbutton
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis',19,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postre[contador],
                         command=revisar_check)

    postre.grid(row=contador,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador, column=1)

    contador += 1

# variables
var_costo_comida = StringVar()
var_costo_bebidas = StringVar()
var_costo_postres = StringVar()
var_costo_subtotal = StringVar()
var_costo_impustos = StringVar()
var_costo_total = StringVar()

# etiqueta de costos y campos de entrada

etiqueta_costos_comida = Label(panel_costos,
                               text='Costo Comida',
                               font=('Dosis',12,'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_costos_comida.grid(row=0,column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)

texto_costo_comida.grid(row=0, column=1, padx=41)

etiqueta_costos_bebidas = Label(panel_costos,
                               text='Costo Bebidas',
                               font=('Dosis',12,'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_costos_bebidas.grid(row=1,column=0)

texto_costo_bebidas = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebidas)

texto_costo_bebidas.grid(row=1, column=1, padx=41)

etiqueta_costos_postres = Label(panel_costos,
                               text='Costo Postres',
                               font=('Dosis',12,'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_costos_postres.grid(row=2,column=0)

texto_costo_postres = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postres)

texto_costo_postres.grid(row=2, column=1, padx=41)

etiqueta_subtotal = Label(panel_costos,
                               text='SubTotal',
                               font=('Dosis',12,'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_subtotal.grid(row=0,column=2)

texto_subtotal = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_subtotal)

texto_subtotal.grid(row=0, column=3, padx=41)

etiqueta_impuestos = Label(panel_costos,
                               text='Impuestos',
                               font=('Dosis',12,'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_impuestos.grid(row=1,column=2)

texto_impuestos = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_impustos)

texto_impuestos.grid(row=1, column=3, padx=41)

etiqueta_total = Label(panel_costos,
                               text='Total',
                               font=('Dosis',12,'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_total.grid(row=2,column=2)

texto_total = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_total)

texto_total.grid(row=2, column=3, padx=41)

# botones
botones = ['total','recibo','guardar','recetear']
botones_creados = []
columna = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Disis',14,'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)

    botones_creados.append(boton)

    boton.grid(row=0,
               column=columna)
    columna +=1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis',12,'bold'),
                    bd=1,
                    width=42,
                    height=10)

texto_recibo.grid(row=0,
                  column=0)

# calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis',16,'bold'),
                          width=32,
                          bd=1)

visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

lista_calculadora = ['7','8','9','+','4','5','6','-','1','2','3'
                     ,'x','CE','BORRAR','0','/']

botones_guardados = []

fila = 1
columna = 0

for boton in lista_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis',16,'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)
    boton.grid(row=fila,
               column=columna)

    botones_guardados.append(boton)

    if columna ==3:
        fila +=1

    columna +=1

    if columna ==4:
        columna = 0

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))




#evitar que la pantalla se cierre
aplicacion.mainloop()



