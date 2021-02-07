#Minimal Effort
#Friendly Timetable


# Importar librerías
from tkinter import *
from tkcalendar import *
import datetime
from tkinter import messagebox




#Funciones

#Funciones de los colores de los temas
def color_tema1():
    archivo_color = open("acolor.txt", "w")
    archivo_color.write("LightCyan4\n")
    archivo_color.write("DarkSlateGray3\n")
    archivo_color.write("PaleTurquoise1")
    archivo_color.close()



def color_tema2():
    archivo_color = open("acolor.txt", "w")
    archivo_color.write("gray25\n")
    archivo_color.write("MistyRose2\n")
    archivo_color.write("SteelBlue3")
    archivo_color.close()



def color_tema3():
    archivo_color = open("acolor.txt", "w")
    archivo_color.write("gray80\n")
    archivo_color.write("CadetBlue1\n")
    archivo_color.write("DarkOrchid3")
    archivo_color.close()



def color_tema4():
    archivo_color = open("acolor.txt", "w")
    archivo_color.write("VioletRed4\n")
    archivo_color.write("DeepPink3\n")
    archivo_color.write("HotPink1")
    archivo_color.close()



def color_tema5():
    archivo_color = open("acolor.txt", "w")
    archivo_color.write("wheat4\n")
    archivo_color.write("coral1\n")
    archivo_color.write("burlywood1")
    archivo_color.close()



#Valores de color (van antes de mostrar pantalla)
def valores_de_color():
    global color1, color2, color3, Icono
    archivo_color=open("acolor.txt","r")
    color1_en_archivo = str(archivo_color.readlines(1))
    color1 = color1_en_archivo[2:len(color1_en_archivo)-4]

    color2_en_archivo = str(archivo_color.readlines(2))
    color2 = color2_en_archivo[2:len(color2_en_archivo)-4]

    color3_en_archivo = str(archivo_color.readlines(3))
    color3=color3_en_archivo[2:len(color3_en_archivo)-2]
    archivo_color.close()

    #Iconos
    archivo_icono=open("icon.txt","r")
    Icono_en_archivo= str(archivo_icono.readlines(1))
    Icono= Icono_en_archivo[2:len(Icono_en_archivo)-2]

    archivo_icono.close()



def click1(event):
    archivo_icono=open("icon.txt","w")
    archivo_icono.write("icono1.ppm")
    archivo_icono.close()



def click2(event):
    archivo_icono=open("icon.txt","w")
    archivo_icono.write("icono2.ppm")
    archivo_icono.close()



def click3(event):
    archivo_icono=open("icon.txt","w")
    archivo_icono.write("icono3.ppm")
    archivo_icono.close()



def click4(event):
    archivo_icono=open("icon.txt","w")
    archivo_icono.write("icono4.ppm")
    archivo_icono.close()



def click5(event):
    archivo_icono=open("icon.txt","w")
    archivo_icono.write("icono5.ppm")
    archivo_icono.close()



def perfil():
    #Perfil
    archivo_perfil = open("icon.txt", "r")
    archivo_perfil.close()



#Errores
def mostrar_error(descripcion_del_error):
    messagebox.showwarning("Error", str(descripcion_del_error))



def mostrar_exito(descripcion_exito):
    messagebox.showinfo("Exito", str(descripcion_exito))



# Pasar de número a nombre de mes
def pasar_mes_de_num_a_letra():
    global nombre_mes
    if mes_numero == 1:
        nombre_mes = "Enero"
    elif mes_numero == 2:
        nombre_mes = "Febrero"
    elif mes_numero == 3:
        nombre_mes = "Marzo"
    elif mes_numero == 4:
        nombre_mes = "Abril"
    elif mes_numero == 5:
        nombre_mes = "Mayo"
    elif mes_numero == 6:
        nombre_mes = "Junio"
    elif mes_numero == 7:
        nombre_mes = "Julio"
    elif mes_numero == 8:
        nombre_mes = "Agosto"
    elif mes_numero == 9:
        nombre_mes = "Septiembre"
    elif mes_numero == 10:
        nombre_mes = "Octubre"
    elif mes_numero == 11:
        nombre_mes = "Noviembre"
    elif mes_numero == 12:
        nombre_mes = "Diciembre"



def borrar_linea_archivo_hoy(archivo):
    global cont1, band, a_elim

    band=True
    with open(archivo, "a+") as arch:
        arch.seek(0)
        contenido = arch.readlines()
        if band == True:
            a_elim = len(contenido)-1
            band = False
        contenido.pop(a_elim)

    with open(archivo, "w") as arch2:
        arch2.writelines("")
        arch2.writelines(contenido)
    a_elim -=1

    mostrar_acts()

    for i in range(a_elim+1,cont1+1):
        Label(f_tablaHoy, text="                             ", font=10, bg=color1).grid(row=i, column=0)
        Label(f_tablaHoy, text="                             ", font=10, bg=color1).grid(row=i, column=1)
        Label(f_tablaHoy, text="                             ", font=10, bg=color1).grid(row=i, column=2)
        Label(f_tablaHoy, text="                             ", font=10, bg=color1).grid(row=i, column=3)
        Label(f_tablaHoy, text="                             ", font=10, bg=color1, height=2).grid(row=i, column=4)



def borrar_linea_archivo_diario(archivo):
    global cont1, band, a_elim

    band=True
    with open(archivo, "a+") as arch:
        arch.seek(0)
        contenido = arch.readlines()
        if band == True:
            a_elim = len(contenido)-1
            band = False
        contenido.pop(a_elim)

    with open(archivo, "w") as arch2:
        arch2.writelines("")
        arch2.writelines(contenido)
    a_elim -=1

    mostrar_acts()

    for i in range(a_elim+2,cont2+1):
        Label(f_tablaDiaria, text="                             ", font=10, bg=color1).grid(row=i, column=0)
        Label(f_tablaDiaria, text="                             ", font=10, bg=color1).grid(row=i, column=1)
        Label(f_tablaDiaria, text="                             ", font=10, bg=color1).grid(row=i, column=2)
        Label(f_tablaDiaria, text="                             ", font=10, bg=color1).grid(row=i, column=3)
        Label(f_tablaDiaria, text="                             ", font=10, bg=color1, height=2).grid(row=i, column=4)



# Funcion para mostrar un frame del menú
def mostrar_frame(frame):
    frame.tkraise()



# Función para mostrar el calendario
def hacer_calendario(ano, mes):
    # año y mes del calendario
    calendario = Calendar(frame_opciones_calendario, selectmode="day", year=ano_numero, month=mes_numero, day=dia_numero, width= width_screen-100)
    calendario.pack(pady=32)



# Funcion botón de + (agregar actividad)
def agregarAct():
    global dicc_Actividades, lista_acts, fechaEntry, horaEntry


    # Función para preguntar por fecha y hora específica si así lo indica el usuario
    def especifico():
        global fechaEntry
        fechaLabel = Label(ventana_agregar, text="Fecha (formato dd/mm/aaaa)")
        fechaLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

        fechaEntry = Entry(ventana_agregar)
        fechaEntry.grid(row=3, column=1, padx=10, pady=0)


    def guardar_actividades_y_cerrar():
        global dicc_Actividades, lista_acts, fechaEntry, horaEntry
        try:
            if (str(horaEntry.get()))[2] == ":" and len(str(horaEntry.get())) == 5 and (str(horaEntry.get())[0:2]).isdigit() and (str(horaEntry.get())[3:6]).isdigit() and (int(str(horaEntry.get())[0:2])) <= 23 and (int(str(horaEntry.get())[3:6])) <= 59:
                lista_acts = []

                #se va a agregar a actividades de hoy
                if varDiaOpc.get() == 1 and len(fechaEntry.get()) == 10 and (fechaEntry.get())[2] == "/" and (fechaEntry.get())[5] == "/" and (int(str(fechaEntry.get())[0:2])) <= 31 and (int(str(fechaEntry.get())[3:5])) <= 12 and (int(str(fechaEntry.get())[6:10])) >= 1:
                    dicc_Actividades = {"Actividad_de_hoy":nombreEntry.get(), "Hora": horaEntry.get(), "Importancia": varImpOpc.get(),
                            "Fecha": fechaEntry.get(), "Descripcion":descripcionEntry.get("1.0",END)}


                    lista_acts = ["Actividad_de_hoy", dicc_Actividades["Actividad_de_hoy"] + ";",
                                  dicc_Actividades["Hora"] + "!",
                                  str(dicc_Actividades["Importancia"]) + "#", str(dicc_Actividades["Descripcion"])[0:-1] + "$",
                                  dicc_Actividades["Fecha"]]


                    #Pasar la información al archico
                    with open("Actividades_de_hoy.txt", "a") as archivo_acts_hoy:
                        archivo_acts_hoy.writelines("\n")
                        archivo_acts_hoy.writelines(lista_acts)


                    #Cerrar y mensaje de guardado
                    ventana_agregar.destroy()

                    mostrar_exito("Se ha guardado la actividad exitosamente")


                #se va a agregar a actividades diarias
                elif varDiaOpc.get() == 2:
                    dicc_Actividades = {"Actividad_diaria":nombreEntry.get(), "Hora": horaEntry.get(), "Importancia": varImpOpc.get(),
                            "Descripcion":descripcionEntry.get("1.0",END)}


                    lista_acts = ["Actividad_diaria",dicc_Actividades["Actividad_diaria"] + ";", dicc_Actividades["Hora"] + "!",
                                  str(dicc_Actividades["Importancia"]) + "#",dicc_Actividades["Descripcion"], 1]

                    #Pasar la información al archivo
                    with open("ActividadesDiarias.txt", "a") as archivo_acts_diarias:
                        archivo_acts_diarias.writelines(lista_acts)

                    #Cerrar y mensaje de guardado
                    ventana_agregar.destroy()
                    mostrar_exito("Se ha guardado la actividad exitosamente")


            #Errores en la fecha, mostrar mensaje apropiado y cerrar
                elif len(fechaEntry.get()) != 10:
                    mostrar_error("Error: la fecha no esta escrita en el formato correcto.")
                    ventana_agregar.destroy()

                elif (fechaEntry.get())[2] != "/" or (fechaEntry.get())[5] != "/":
                    mostrar_error("Error: la fecha debe tener un '/' entre el día, el mes y el año.")
                    ventana_agregar.destroy()

                elif (int(str(fechaEntry.get())[0:2])) >= 31 or (int(str(fechaEntry.get())[3:5])) >= 12 or (int(str(fechaEntry.get())[6:10])) <= 1:
                    mostrar_error("Error: los valores de la fecha son imposibles.")
                    ventana_agregar.destroy()

                else:
                    mostrar_error("Error: la sintaxis o valor de la fecha es incorrecto.")
                    ventana_agregar.destroy()


            #Errores en la hora, mostrar mensaje apropiado y cerrar
            elif str(horaEntry.get())[2] != ":":
                    mostrar_error("Error: la hora debe tener un ':' entre las horas y los minutos.")
                    ventana_agregar.destroy()

            elif len(str(horaEntry.get())) != 5:
                    mostrar_error("Error: la hora no esta escrita en el formato correcto.")
                    ventana_agregar.destroy()

            elif (str(horaEntry.get())[0:2]).isalpha() or (str(horaEntry.get())[3:6]).isalpha():
                    mostrar_error("Error: los valores de la hora deben ser numericos.")
                    ventana_agregar.destroy()

            elif (int(str(horaEntry.get())[0:2])) >= 23 or (int(str(horaEntry.get())[3:6])) >= 59:
                    mostrar_error("Error: los valores de la hora son imposibles.")
                    ventana_agregar.destroy()

            else:
                mostrar_error("Error: la sintaxis o valor de la hora es incorrecto.")
                ventana_agregar.destroy()

        #Errores mayores, mostrar mensaje apropiado y cerrar
        except:
            if varDiaOpc.get() == 1:
                if (str(fechaEntry.get())[0:2]).isalpha() or (str(fechaEntry.get())[3:5]).isalpha() or (str(fechaEntry.get())[6:10]).isalpha():
                    mostrar_error("Error: los valores de la fecha deben ser numéricos.")
                    ventana_agregar.destroy()

                else:
                    mostrar_error("Error: Se deben llenar los campos requeridos.")
                    ventana_agregar.destroy()
            else:
                mostrar_exito("Se ha guardado la actividad exitosamente")
                ventana_agregar.destroy()

        mostrar_acts()


    dicc_Actividades = {}


    # Variables para opciones de importancia y si es día es especiífico o diario
    varDiaOpc = IntVar()
    varImpOpc = IntVar()

    # Información del root de la nueva pestaña de agragar actividad (ventana_agregar)
    ventana_agregar = Toplevel(width=1200, height=1000)
    ventana_agregar.title("Agregar una actividad")

    # Pide nombre
    nombreLabel = Label(ventana_agregar, text="Nombre de la actividad")
    nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

    # Espacio para escribir nombre
    nombreEntry = Entry(ventana_agregar)
    nombreEntry.grid(row=0, column=1, padx=10, pady=0)

    # Pide hora
    horaLabel = Label(ventana_agregar, text="Hora (formato hh:mm)")
    horaLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

    horaEntry = Entry(ventana_agregar)
    horaEntry.grid(row=4, column=1, padx=10, pady=0)

    # Pregunta si la actividad se va a agregar a un día específico o va a ser diaria
    varDiaOpc = IntVar()
    varDiaOpc.set(2)

    # Opción de día específico, (corre la función de específico)
    diaOpc1 = Radiobutton(ventana_agregar, text="Dia específico", variable=varDiaOpc, value=1, command=especifico)
    diaOpc1.grid(row=2, column=0, padx=10, pady=10)

    # Opción de diario
    diaOpc2 = Radiobutton(ventana_agregar, text="Diario", variable=varDiaOpc, value=2)
    diaOpc2.grid(row=2, column=1, padx=10, pady=10)

    # Pide importancia de la actividad
    varImpOpc = StringVar()
    varImpOpc.set(1)
    importanciaLabel = Label(ventana_agregar, text="Importancia")
    importanciaLabel.grid(row=5, column=0, sticky="e")

    # Opciones de los diferentes tipos de importancia
    impOpc1 = Radiobutton(ventana_agregar, text="Verde", variable=varImpOpc, value="Verde")
    impOpc1.grid(row=5, column=1, padx=10, sticky="w")

    impOpc2 = Radiobutton(ventana_agregar, text="Amarillo", variable=varImpOpc, value="Amarillo")
    impOpc2.grid(row=6, column=1, padx=10, sticky="w")

    impOpc3 = Radiobutton(ventana_agregar, text="Rojo", variable=varImpOpc, value="Rojo")
    impOpc3.grid(row=7, column=1, padx=10, sticky="w")

    # Pide la descripción
    descripcionLabel = Label(ventana_agregar, text="Descripción: ")
    descripcionLabel.grid(row=8, column=0, sticky="e", padx=10, pady=10)

    descripcionEntry = Text(ventana_agregar, width=16, height=5)
    descripcionEntry.grid(row=8, column=1, padx=0, pady=10)

    # Le pone un scrollbar al cuadro de texto de descripción
    scrollVert_descripcion = Scrollbar(ventana_agregar, command=descripcionEntry.yview)
    scrollVert_descripcion.grid(row=8, column=2, sticky="nsew")
    descripcionEntry.config(yscrollcommand=scrollVert_descripcion.set)

    # Botón para guardar y cerrar ventana ventana_agregar
    botonEnviar = Button(ventana_agregar, text="Guardar", command=guardar_actividades_y_cerrar)
    botonEnviar.grid(row=9, column=0, sticky="e", pady="10")



def hacer_frame_tabla_hoy():
    global f_tablaHoy
    f_tablaHoy = Frame(f_agenda, bg=color1)
    f_tablaHoy.pack(side="top", fill="x")
    f_tablaHoy.config(heigh=height_screen / 2 - 80)

    for column in range(13):
        Grid.columnconfigure(f_tablaHoy, column, weight=1)

    columna_Act_hoy = Label(f_tablaHoy, bg=color3, text="      Actividad de Hoy      ", font=10).grid(row=0, column=0)
    columna_Hora_hoy = Label(f_tablaHoy, bg=color3, text="       Hora       ", font=10).grid(row=0, column=1)
    columna_Importancia_hoy = Label(f_tablaHoy, bg=color3, text="       Importancia       ", font=10).grid(row=0,
                                                                                                           column=2)
    columna_Descripcion_hoy = Label(f_tablaHoy, bg=color3, text="       Descripción       ", font=10).grid(row=0,
                                                                                                           column=3)
    columna_Realizada_hoy = Label(f_tablaHoy, bg=color3, text="       Realizada       ", font=10).grid(row=0, column=4)



# Función para (cambiar la fecha)
def cambiar_fecha():
    global dia_numero, ano_numero, mes_numero, nombre_mes, f_tablaHoy


    #Cuando se le da al boton de guardado
    def guardar_fecha():
        global dia_numero, ano_numero, nombre_mes, mes_numero

        dia_ingresado = fechaEntry1.get()

        try:

            #Checar que todos los datos esten bien
            if len(dia_ingresado) == 10 and dia_ingresado[2] == "/" and dia_ingresado[5] == "/" and (int(dia_ingresado[0:2])) <= 31 and (int(dia_ingresado[3:5])) <= 12 and (str(dia_ingresado[6:10])).isdigit() and (str(dia_ingresado[0:2])).isdigit() and (str(dia_ingresado[3:5])).isdigit() and (str(dia_ingresado[6:10])).isdigit():
                #cambiar dia
                dia_numero = 0
                str_dia_numero = ""
                for i in str(dia_ingresado)[0:2]:
                    if len(str_dia_numero) < 2:
                        str_dia_numero += i
                        dia_numero = int(str_dia_numero)

                #cambiar mes
                mes_numero = 0
                str_mes_numero = ""
                for i in str(dia_ingresado)[3:5]:
                    if len(str_mes_numero) < 2:
                        str_mes_numero += i
                        mes_numero = int(str_mes_numero)

                #cambiar año
                ano_numero = 0
                str_ano_numero = ""
                for i in str(dia_ingresado)[6:10]:
                    if len(str_ano_numero) < 4:
                        str_ano_numero += i
                        ano_numero = int(str_ano_numero)


                #agregar datos y cerrar
                pasar_mes_de_num_a_letra()
                ventana_cambiar.destroy()

                #Mensaje confirmar exito
                mostrar_exito("Se ha cambiado la fecha exitosamente.")

            #Errores en la fecha, mostrar mensaje apropiado y cerrar
            elif not dia_ingresado:
                mostrar_error("Error: se debe ingresar una fecha.")
                ventana_cambiar.destroy()

            elif len(dia_ingresado) != 10:
                mostrar_error("Error: el formato de la fecha es incorrecto.")
                ventana_cambiar.destroy()

            elif dia_ingresado[2] != "/" or dia_ingresado[5] != "/":
                mostrar_error("Error: la fecha debe tener un '/' entre el día, el mes y el año.")
                ventana_cambiar.destroy()

            elif (int(dia_ingresado[0:2])) >= 31 or (int(dia_ingresado[3:5])) >= 12 or (int(dia_ingresado[6:10])) <= 1:
                mostrar_error("Error: los valores de la fecha son imposibles.")
                ventana_cambiar.destroy()

            elif (str(dia_ingresado[6:10])).isalpha() or (str(dia_ingresado[0:2])).isalpha() or (str(dia_ingresado[3:5])).isalpha() or (str(dia_ingresado[6:10])).isalpha():
                mostrar_error("Error: los valores de la fecha deben ser numéricos.")
                ventana_cambiar.destroy()

            else:
                mostrar_error("Error: la sintaxis o valor de la fecha es incorrecto.")
                ventana_cambiar.destroy()


        #Errores mayores, mostrar mensaje apropiado y cerrar
        except:
            if not dia_ingresado:
                mostrar_error("Error: se debe ingresar una fecha.")
                ventana_cambiar.destroy()

            elif (str(dia_ingresado[6:10])).isalpha() or (str(dia_ingresado[0:2])).isalpha() or (str(dia_ingresado[3:5])).isalpha() or (str(dia_ingresado[6:10])).isalpha():
                mostrar_error("Error: los valores de la fecha deben ser numéricos.")
                ventana_cambiar.destroy()

            else:
                mostrar_error("Error: la sintaxis o valor de la fecha es incorrecto.")
                ventana_cambiar.destroy()


        #Mostrar nueva fecha
        textoFecha.set(str(dia_numero) + " de " + nombre_mes + " del " + str(ano_numero))


        #f_tablaHoy.destroy()
        for i in range(1, cont1 + 1):
            Label(f_tablaHoy, text="                             ", font=10, bg=color1).grid(row=i, column=0)
            Label(f_tablaHoy, text="                             ", font=10, bg=color1).grid(row=i, column=1)
            Label(f_tablaHoy, text="                             ", font=10, bg=color1).grid(row=i, column=2)
            Label(f_tablaHoy, text="                             ", font=10, bg=color1).grid(row=i, column=3)
            Label(f_tablaHoy, text="                             ", font=10, bg=color1, height=2).grid(row=i, column=4)
        #hacer_frame_tabla_hoy()
        mostrar_acts()


    # Crea una nueva ventana (camb)
    ventana_cambiar = Toplevel(width=1200, height=1000)
    ventana_cambiar.title("Cambiar de día")

    # Pide nueva fecha
    fechaLabel1 = Label(ventana_cambiar, text="Fecha (formato dd/mm/aaaa)")
    fechaLabel1.grid(row=0, column=0, sticky="e", padx=10, pady=10)
    fechaEntry1 = Entry(ventana_cambiar)
    fechaEntry1.grid(row=0, column=1, padx=10, pady=0)

    # Guardar nueva fecha y cerrar ventana
    Button(ventana_cambiar, text="Guardar", command=guardar_fecha).grid(row=1, column=0, padx=10, pady=0)

    #mostrar_acts() (en proceso, si no se comenta, se repiten)
    frame_opciones_calendario.pack()



def actualizar_etiqueta(root, texto, fila, column):
    Label(root, text=texto, font=10, bg=color3).grid(row=fila, column=column)



#Mostrar las actividades en frame agenda (en proceso)
def mostrar_acts():
    global cont1, cont2, f_tablaHoy
    cont1 = 1
    cont2 = 1

    #Si ya existe el archivo de acts de hoy
    try:
        #Leer archivo de actividades de hoy
        with open("Actividades_de_hoy.txt", "r") as archivo_acts_hoy:
            archivo_acts_hoy.seek(0)
            lista_acts_hoy = archivo_acts_hoy.readlines()


        #Agregar actividades
            for elem in lista_acts_hoy:
                inicio_hora_hoy = str(elem).find(";")
                inicio_importancia_hoy = str(elem).find("!")
                inicio_descripcion_hoy = str(elem).find("#")
                inicio_fecha = str(elem).find("$")

                if dia_numero<10:
                    str_dia_numero = "0" + str(dia_numero)
                else:
                    str_dia_numero = str(dia_numero)

                if mes_numero<10:
                    str_mes_numero = "0" + str(mes_numero)
                else:
                    str_mes_numero = str(mes_numero)

                str_ano_numero = str(ano_numero)


                if (str(elem)[inicio_fecha+1:-1] == str(str_dia_numero) + "/" + str(str_mes_numero) + "/" + str(str_ano_numero)) or (str(elem)[inicio_fecha+1:] == str(str_dia_numero) + "/" + str(str_mes_numero) + "/" + str(str_ano_numero)):

                    if str(elem)[0:16] == "Actividad_de_hoy":
                        #Label(f_tablaHoy, text=str(elem)[16:inicio_hora_hoy], font=10).grid(row=cont1, column=0)
                        actualizar_etiqueta(f_tablaHoy, (str(elem))[16:inicio_hora_hoy], cont1, 0)

                    if str(elem)[inicio_hora_hoy] == ";":
                        #Label(f_tablaHoy, text=str(elem)[inicio_hora_hoy + 1:inicio_importancia_hoy],

                        #font=10).grid(row=cont1, column=1)
                        actualizar_etiqueta(f_tablaHoy, str(elem)[inicio_hora_hoy + 1:inicio_importancia_hoy], cont1, 1)


                    if str(elem)[inicio_importancia_hoy] == "!":
                        actualizar_etiqueta(f_tablaHoy, str(elem)[inicio_importancia_hoy + 1:inicio_descripcion_hoy], cont1, 2)


                    if str(elem)[inicio_descripcion_hoy] == "#":

                        actualizar_etiqueta(f_tablaHoy, str(elem)[inicio_descripcion_hoy + 1:inicio_fecha], cont1, 3)


                    Button(f_tablaHoy, text="Realizado", font=10, command=lambda: borrar_linea_archivo_hoy("Actividades_de_hoy.txt"), height=1).grid(row=cont1, column=4)

                    cont1 += 1


    #Si no existe el archivo hacer uno nuevo
    except:
        with open("Actividades_de_hoy.txt", "a") as archivo_acts_hoy:
            archivo_acts_hoy.write("")


    #si ya existe el archivo de acts diarias
    try:
        #Leer archivo de acts diarias
        with open("ActividadesDiarias.txt", "r") as archivo_acts_diarias:
            lista_acts_diarias = archivo_acts_diarias.readlines()

        #Agregar actividades

            for elem in lista_acts_diarias:

                inicio_hora_diaria = str(elem).find(";")
                inicio_importancia_diaria = str(elem).find("!")
                inicio_descripcion_diaria = str(elem).find("#")


                if str(elem)[0:16] == "Actividad_diaria":

                    actualizar_etiqueta(f_tablaDiaria, str(elem)[16:inicio_hora_diaria], cont2, 0)

                if str(elem)[inicio_hora_diaria] == ";":
                    Label(f_tablaDiaria,bg=color3, text=str(elem)[inicio_hora_diaria+1:inicio_importancia_diaria], font=10).grid(row=cont2, column=1)

                if str(elem)[inicio_importancia_diaria] == "!":
                    Label(f_tablaDiaria,bg=color3, text=str(elem)[inicio_importancia_diaria+1:inicio_descripcion_diaria], font=10).grid(row=cont2, column=2)

                if str(elem)[inicio_descripcion_diaria] == "#":
                    actualizar_etiqueta(f_tablaDiaria, str(elem)[inicio_descripcion_diaria + 1:-1], cont2, 3)
                    #Label(f_tablaDiaria,bg=color3, text=str(elem)[inicio_descripcion_diaria+1:], font=10).grid(row=cont2, column=3)


                Button(f_tablaDiaria, text="Realizado", font=10,
                       command=lambda: borrar_linea_archivo_diario("ActividadesDiarias.txt")).grid(row=cont2, column=4)

                cont2 += 1

    #Si no existe el archivo hacer uno nuevo
    except:
        with open("ActividadesDiarias.txt", "a") as archivo_acts_diarias:
            archivo_acts_diarias.write("")



def inicio():
    global f_agenda, mes_numero, height_screen, frame_opciones_calendario, ano_numero, dia_numero, width_screen, textoFecha, f_tablaDiaria, f_tablaHoy, cont1, cont2
    # obtener datos del día de hoy
    #locale.setlocale(locale.LC_ALL, 'es-ES')
    ano_numero = datetime.date.today().year
    mes_numero = datetime.date.today().month
    dia_numero = datetime.date.today().day

    #Ejecucion de funciones para iniciar
    pasar_mes_de_num_a_letra()


    # Se inicia el main loop (raiz)
    raiz = Tk()


    # Configuración del raiz principal
    raiz.title("Friendly Timetable")

    # w y h son el temaño de la pantalla del usuario
    width_screen, height_screen = raiz.winfo_screenwidth(), raiz.winfo_screenheight()
    raiz.geometry("%dx%d+0+0" % (width_screen, height_screen - 60))

    # No se puede cambiar el tamaño de la ventana
    raiz.resizable(False, False)



    # Frame para el menú de opciones de página
    frameMenu = Frame(raiz,bg=color1)

    # Tamaño y posicion del frame
    frameMenu.pack(side="left", anchor="w", fill="y", expand="True")
    frameMenu.config(width="300", heigh="350")



    # FramePrincipal
    f_princ = Frame(raiz, height=height_screen - 50, width=width_screen, bg=color1)
    f_princ.pack(side="left")


    # Frames por modulo que se muestran cuando apretamos los botones de frame menu
    f_agenda = Frame(f_princ, height=height_screen - 70, width=width_screen - 200, bg=color1)
    f_agenda.grid(row=0, column=0, sticky='news')

    f_calendario = Frame(f_princ, height=height_screen - 50, width=width_screen, bg=color1)
    f_calendario.grid(row=0, column=0, sticky='news')


    f_personalizar = Frame(f_princ, height=height_screen - 50, width=width_screen, bg=color1)
    f_personalizar.grid(row=0, column=0, sticky='news')

    f_configuracion = Frame(f_princ, height=height_screen - 50, width=width_screen, bg=color1)
    f_configuracion.grid(row=0, column=0, sticky='news')


    # Botones FrameMenu
    # Boton que muestra el frame de agenda
    boton_agenda = Button(frameMenu,bg=color2, text="Agenda", heigh="8", width="20", font="50",
                        command=lambda: mostrar_frame(f_agenda))
    boton_agenda.grid(row="0", column="0", sticky="we")

    # Boton que muestra el frame de calendario
    boton_Calendario = Button(frameMenu,bg=color2, text="Calendario", heigh="8", width="20", font="50",
                        command=lambda: mostrar_frame(f_calendario))
    boton_Calendario.grid(row="1", column="0", sticky="we")

    # Boton que muestra el frame de personalizar
    boton_Personalizar = Button(frameMenu,bg=color2, text="Personalizar", heigh="8", width="20", font="50",
                      command=lambda: mostrar_frame(f_personalizar))
    boton_Personalizar.grid(row="2", column="0", sticky="we")

    # Boton que muestra el frame de configuración
    boton_Configuracion = Button(frameMenu,bg=color2, text="Configuración", heigh="8", width="20", font="50",
                       command=lambda: mostrar_frame(f_configuracion))
    boton_Configuracion.grid(row="3", column="0", sticky="we")


    # Iniciar mostrando el frame de agenda
    mostrar_frame(f_agenda)


    # Frame Agenda

    # labels superiores, muestran titulo (agenda), y fecha que se muestra
    textoFecha = StringVar()
    textoFecha.set(str(dia_numero) + " de " + nombre_mes + " del " + str(ano_numero))

    label_titulo = Label(f_agenda,bg=color3, text="Agenda", font="10").pack(fill="x")
    label_mostrar_fecha = Label(f_agenda,bg=color3, textvariable=(textoFecha), font="10").pack(fill="x")


    # boton para cambiar de día y para agregar actividad, corren sus funciones respectivas
    frameBotones = Frame(f_agenda,bg=color1)
    frameBotones.pack(anchor="n")
    frameBotones.config(heigh=2)

    botonCambio = Button(frameBotones,bg=color2, text="Cambiar de día", font="10", command=cambiar_fecha)
    botonCambio.pack(side="left")

    ventana_agregar_Boton = Button(frameBotones,bg=color2, text="+", font="500", heigh="3", width="5", command=agregarAct)
    ventana_agregar_Boton.pack(side="top")

    hacer_frame_tabla_hoy()


    # frame table diaria
    f_tablaDiaria = Frame(f_agenda, bg=color1)
    f_tablaDiaria.pack(anchor="n", fill="x", expand="True")
    f_tablaDiaria.config(heigh=height_screen / 2 - 60)
    f_tablaDiaria.grid_propagate(False)


    #Que las columnas tengan ancho
    for column in range(13):
        Grid.columnconfigure(f_tablaDiaria, column, weight=1)

    # Columnas de la tabla diaria
    columna_Act_diaria = Label(f_tablaDiaria,bg=color3, text="       Actividad Diaria       ", font=10).grid(row=0, column=0)
    columna_Hora_diaria = Label(f_tablaDiaria,bg=color3, text="       Hora       ", font=10).grid(row=0, column=1)
    columna_Importancia_diaria = Label(f_tablaDiaria,bg=color3, text="       Importancia       ", font=10).grid(row=0, column=2)
    columna_Descripcion_diaria = Label(f_tablaDiaria,bg=color3, text="       Descripción       ", font=10).grid(row=0, column=3)
    columna_Realizada_diaria = Label(f_tablaDiaria,bg=color3, text="       Realizada       ", font=10).grid(row=0, column=4)


    #Ya cuando se creó el frame, se muestran las actividades

    mostrar_acts()


    # Frame Calendario

    #Frames de la pantalla calendario
    frame_opciones_calendario = Frame(f_calendario, bd=5)

    f_calendario_mes = Frame(frame_opciones_calendario, height=height_screen*0.1, width=width_screen, bg=color3)
    f_calendario_mes.grid(row=0, column=0, sticky='news')

    #Iniciar mostrando mes
    mostrar_frame(f_calendario_mes)

    # Hacer calendario
    frame_opciones_calendario = Frame(f_calendario, bg=color3, height=100, width=100)
    frame_opciones_calendario.pack(side=TOP)


    #funcion para crear el calendario
    hacer_calendario(ano_numero, mes_numero)


    #Boton Mostrar
    lista_actividades=Label(frame_opciones_calendario, bg=color3, text="",width=4)
    lista_actividades.pack(side=BOTTOM)
    boton_seleccionar_calendario_mes= Button(frame_opciones_calendario,bg=color2, text="Mostrar actividades", width = 30)
    boton_seleccionar_calendario_mes.pack(side=TOP)


    #frame personalizar
    #Iconos
    icono1=PhotoImage(file="icono1.ppm")
    icono2=PhotoImage(file="icono2.ppm")
    icono3=PhotoImage(file="icono3.ppm")
    icono4=PhotoImage(file="icono4.ppm")
    icono5=PhotoImage(file="icono5.ppm")

    f_seleccionar_Icono_personalizado = Frame(f_personalizar, bg=color1, heigh=100, width= width_screen*.6)
    f_seleccionar_Icono_personalizado.pack(side=TOP, expand= FALSE)

    label_seleccionar_icono = Label(f_seleccionar_Icono_personalizado, bg=color3, font= ('Consolas', 14), text= "Selección de Icono")
    label_seleccionar_icono.pack(fill=X, expand=FALSE)

    seleccion_Icono_Scroll= Scrollbar(f_seleccionar_Icono_personalizado, orient=HORIZONTAL)
    lista_iconos= Listbox(f_seleccionar_Icono_personalizado, bg=color3, xscrollcommand=seleccion_Icono_Scroll.set)

    seleccion_Icono_Scroll.config(command=lista_iconos.xview)
    seleccion_Icono_Scroll.pack(side=BOTTOM, fill=X)
    lista_iconos.pack(padx= 15)

    boton_icono1= Canvas(lista_iconos, width= 184, bg=color2)
    boton_icono1.pack(side=LEFT, expand=FALSE)
    boton_icono1.create_image(1,1, anchor=NW, image=icono1)
    boton_icono1.bind("<Button-1>", click1)

    boton_icono2= Canvas(lista_iconos, width= 184, bg=color2)
    boton_icono2.pack(side=LEFT, expand=FALSE)
    boton_icono2.create_image(1,1, anchor=NW, image=icono2)
    boton_icono2.bind("<Button-1>", click2)

    boton_icono3= Canvas(lista_iconos, width= 184, bg=color2)
    boton_icono3.pack(side=LEFT, expand=FALSE)
    boton_icono3.create_image(1,1, anchor=NW, image=icono3)
    boton_icono3.bind("<Button-1>", click3)

    boton_icono4= Canvas(lista_iconos, width= 184, bg=color2)
    boton_icono4.pack(side=LEFT, expand=FALSE)
    boton_icono4.create_image(1,1, anchor=NW, image=icono4)
    boton_icono4.bind("<Button-1>", click4)

    boton_icono5= Canvas(lista_iconos, width= 184,bg=color2)
    boton_icono5.pack(side=LEFT, expand=FALSE)
    boton_icono5.create_image(1,1, anchor=NW, image=icono5)
    boton_icono5.bind("<Button-1>", click5)

    f_vacio=Frame(f_personalizar, bg=color1, heigh=20,  width= width_screen*.6)
    f_vacio.pack()

    f_seleccionar_tema_personalizado = Frame(f_personalizar, bg=color3, heigh=100,  width= width_screen*.6)
    f_seleccionar_tema_personalizado.pack(expand=FALSE)

    label_seleccionar_tema = Label(f_seleccionar_tema_personalizado, bg=color3, font= ('Consolas', 14), text= "Selección de Tema")
    label_seleccionar_tema.pack(fill=X, expand=FALSE)

    seleccionar_tema_scrollbar=Scrollbar(f_seleccionar_tema_personalizado, orient=HORIZONTAL)
    listatemas=Listbox(f_seleccionar_tema_personalizado, xscrollcommand=seleccionar_tema_scrollbar.set)

    seleccionar_tema_scrollbar.config(command=listatemas.xview)
    seleccionar_tema_scrollbar.pack(side=BOTTOM, fill=X)
    listatemas.pack(padx=15)

    Tema1= Button(listatemas, text= "Devs2",height=2, width= 32, command=lambda: color_tema1(), bg="DarkSlateGray3")
    Tema1.pack(side=LEFT, expand=FALSE)

    Tema2= Button(listatemas, text= "Staid",height=2, width= 32, command=lambda: color_tema2(), bg="MistyRose2")
    Tema2.pack(side=LEFT, expand=FALSE)

    Tema3= Button(listatemas, text= "Joy",height=2, width= 32, command=lambda: color_tema3(), bg="CadetBlue1")
    Tema3.pack(side=LEFT, expand=FALSE)

    Tema4= Button(listatemas, text= "Deadly",height=2, width= 32, command=lambda: color_tema4(), bg="DeepPink3")
    Tema4.pack(side=LEFT, expand=FALSE)

    Tema5= Button(listatemas, text= "West",height=2, width= 32, command=lambda: color_tema5(), bg="coral1")
    Tema5.pack(side=LEFT, expand=FALSE)

    # Frame Configuración
    foto_perfil=PhotoImage(file=str(Icono))
    nombre=""
    cumpleanos=""

    f_acomodo_config=Frame(f_configuracion,bg=color3)
    f_acomodo_config.pack(side=TOP)

    #Este frame es para arreglar un problema de distribución de causa desconocida

    f_arreglo=Frame(f_configuracion,height=1000,width=2000,bg=color1)
    f_arreglo.pack(side=RIGHT)

    Nombre="Naim Towfighian"
    Cumple="22/06/2002"

    f_perfil=Frame(f_acomodo_config, bg=color3, heigh=200,  width=184)
    f_perfil.grid(row=0, column=0)

    Etiqueta_perfil=Label(f_perfil,bg=color3,text="Perfil", font=('Consolas',14))
    Etiqueta_perfil.pack(side=TOP, fill=X)

    Icono_Perfil=Canvas(f_perfil,height=184, width=184,bg=color3)
    Icono_Perfil.pack()
    Icono_Perfil.create_image(1,1, anchor=NW, image=foto_perfil)

    l_nombre=Label(f_perfil, bg=color3, text="Nombre: " + str(Nombre))
    l_nombre.pack()

    l_cumpleanos=Label(f_perfil, bg=color3, text="Cumpleaños: " + str(Cumple))
    l_cumpleanos.pack()


    f_config=Frame(f_acomodo_config, bg=color3,height=258, width= width_screen*.6)
    f_config.grid(row=0, column=1)

    Cambiar_nombre=Button(f_config,bg=color2,height=2,text="Cambiar nombre")
    Cambiar_nombre.grid(row=0, column=0)

    Cambiar_cumple=Button(f_config,bg=color2,height=2,text="Cambiar cumpleaños")
    Cambiar_cumple.grid(row=0, column=1)

    # Se cierra el mainloop
    raiz.mainloop()

try:
    valores_de_color()
except:
    color_tema1()
    click1("event")
    valores_de_color()


perfil()
inicio()

#Fin :)