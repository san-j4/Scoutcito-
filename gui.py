from flet import Page, app, Column, TextField, dropdown, Dropdown, ElevatedButton, Row, LabelPosition, border, ResponsiveRow, MainAxisAlignment
from flet import ThemeMode, Switch, Text, FontWeight, Banner, colors, TextButton, icons, Icon, DataCell, DataColumn, DataRow, DataTable
from time import sleep

mesclados = { 
#la pocicion 0 es morse la 1 es siete cruces
'a':['.-','1v ','1-1/',], 
'b':['-...','<1 ','1-2/'],
'c':['-.-.','1ʌ ','1-3/'],
'd':['-..','1> ','1-4/'],
'e':['.','2v ','1-5/'],
'f':['..-.','<2 ','2-1/'],
'g':['--..','2ʌ ','2-2/'],
'h':['....','2ʌ ','2-3/'],
'i':['..','3v ','2-4/'],
'j':['.---','<3 ','2-4/'],
'k':['-.-','3ʌ ','2-5/'],
'l':['.-..','3> ','3-1/'],
'm':['--','4v ','3-2/'],
'n':['-.','<4 ','3-3/'],
'ñ':['--.--','4ʌ ','ñ/'],
'o':['---','4> ','3-4/'],
'p':['.--.','5v ','3-5/'],
'q':['--.-','<5 ','4-1/'],
'r':['.-.','5ʌ ','4-2/'],
's':['...','5> ','4-3/'],
't':['-','6v ','4-4/'],
'u':['..-','<6 ','4-5/'],
'v':['...-','6ʌ ','5-1/'],
'w':['.--','6> ','5-2/'],
'x':['-..-','7v ','5-3/'],
'y':['-.--','<7 ','5-4/'],
'z':['--..','7ʌ ','5-5/'],
' ':['/','7> ', ' '],
'1': ['.----', '1',], 
'2': ['..---', '2',], 
'3': ['...--', '3',], 
'4': ['....-', '4',], 
'5': ['.....', '5',], 
'6': ['-....', '6',], 
'7': ['--...', '7',], 
'8': ['---..', '8',], 
'9': ['----.', '9',], 
'0': ['-----', '0',], 
}

murcielago_cod = {
        'm': '0',
        'u': '1',
        'r': '2',
        'c': '3',
        'i': '4',
        'e': '5',
        'l': '6',
        'a': '7',
        'g': '8',
        'o': '9'
}

cenit_polar = {
        'c': 'p',
        'e': 'o',
        'n': 'l',
        'i': 'a',
        't': 'r',
        'p': 'c',
        'o': 'e',
        'l': 'n',
        'a': 'i',
        'r': 't',
        }


def codigos_complejos (p,traducir):
    """#* es una funcion global para traducir una sola vez"""
    terminado = []
    espacio =0
    for x in traducir:
        letr = traducir [espacio]
        traducido = mesclados.get (letr,f"{traducir[espacio]}")
        terminado += traducido [p]
        espacio += 1
    return terminado
        

        
class codigos():
    
    @staticmethod
    def morse(lista:str="", ret: int = 0):
        """#* traduce al codigo Morse"""
        traducir = list (lista.lower())
        traducido = codigos_complejos(0,traducir)
        if ret !=0 :
            listo =f"{''.join(traducido)}"
        if ret == 0:
            listo = f"{''.join(traducido)}/"
        return listo

        
    
    @staticmethod
    def siete_cruses(lista:str=""):
        """#* traduce al codigo Siete Cruces"""
        traducir = list (lista.lower())
        traducido = codigos_complejos(1,traducir)
        listo = ''.join(traducido)
        return listo
    
    @staticmethod
    def murcielago(lista:str=""):
        """#* traduce al codigo Murcielago"""
        frase_codificada = ''
        for letra in lista:
            if letra.lower() in murcielago_cod:
                frase_codificada += murcielago_cod[letra.lower()]
            else:
                frase_codificada += letra

        return frase_codificada
    
    @staticmethod
    def Cenit_polar(lista:str=""):
        """#* traduce al codigo Cenit Polar"""
        frase_codificada = ''
        for letra in lista:
            if letra.lower() in cenit_polar:
                frase_codificada += cenit_polar[letra.lower()]
            else:
                frase_codificada += letra
        return frase_codificada
    
    @staticmethod
    def rot_trece(lista:str=""):
        """#* traduce al codigo rot 13"""
        resultado = ''
        for caracter in lista:
            if 'a' <= caracter <= 'z':
                nuevo_caracter = chr((ord(caracter) - ord('a') + 13) % 26 + ord('a'))
            elif 'A' <= caracter <= 'Z':
                nuevo_caracter = chr((ord(caracter) - ord('A') + 13) % 26 + ord('A'))
            else:
                nuevo_caracter = caracter
            resultado += nuevo_caracter
        return resultado
    
    @staticmethod
    def cincoxcinco(lista:str=""):
        """#* traduce al codigo 5X5"""
        traducir = list (lista.lower())
        traducido = codigos_complejos(2,traducir)
        listo = ''.join(traducido)
        return listo

#* aca estan las listas de las letras para las tablas
letr_cinxcin = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i,j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letr_morse = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]
 
def main(page: Page):
    # * esto sirve para actualizar la app rapido
    def actualizar():
        page.update()
        
    #* esta es la tabla de morse o 7 cruces que se muestra al elejir el lenguaje
    tab_morse_2 = DataTable(
        border=border.all(2,"blue"),border_radius=10,
        columns =[
        DataColumn(Text(" ",size=20,)),
        DataColumn(Text(" ",size=20,)),
        DataColumn(Text(" ",size=20,)),
        DataColumn(Text(" ",size=20,)),
        DataColumn(Text(" ",size=20,)),
        DataColumn(Text(" ",size=20,))],
        rows =  [],)
    
    #* esta funcion rellena los tableros de morce y 7 cruces 
    def tab_morse(event: str= ""):
        for element in range(0,len(letr_morse),6):
            f= codigos()
            if dd.value== "Morse":
                t_0 =f.morse(letr_morse[element], ret=1)
                t_1 =f.morse(letr_morse[element+1],ret=1)
                t_2 =f.morse(letr_morse[element+2],ret=1)
                t_3 =f.morse(letr_morse[element+3],ret=1)
                t_4 =f.morse(letr_morse[element+4],ret=1)
                t_5 =f.morse(letr_morse[element+5],ret=1)
            if dd.value =="7 Cruces":
                t_0 =f.siete_cruses(letr_morse[element])
                t_1 =f.siete_cruses(letr_morse[element+1])
                t_2 =f.siete_cruses(letr_morse[element+2])
                t_3 =f.siete_cruses(letr_morse[element+3])
                t_4 =f.siete_cruses(letr_morse[element+4])
                t_5 =f.siete_cruses(letr_morse[element+5])
                pass
            
            tab_morse_2.rows.append(DataRow(cells=[
                    DataCell(Text(value=f"{letr_morse[element]}= {t_0}",size=20,)),
                    DataCell(Text(value=f"{letr_morse[element+1]}= {t_1}",size=20,)),
                    DataCell(Text(value=f"{letr_morse[element+2]}= {t_2}",size=20,)),
                    DataCell(Text(value=f"{letr_morse[element+3]}= {t_3}",size=20,)),
                    DataCell(Text(value=f"{letr_morse[element+4]}= {t_4}",size=20,)),
                    DataCell(Text(value=f"{letr_morse[element+5]}= {t_5}",size=20,)),]))
        actualizar()
    
    #* esta tabla es la de murcielago que se muestra cuando la elegis
    tab_murcielago= DataTable(
        border=border.all(2,"blue"),border_radius=10,
            columns=[
                DataColumn(Text("m",size=15,),),
                DataColumn(Text("u",size=15,),),
                DataColumn(Text("r",size=15,),),
                DataColumn(Text("c",size=15,),),
                DataColumn(Text("i",size=15,),),
                DataColumn(Text("e",size=15,),),
                DataColumn(Text("l",size=15,),),
                DataColumn(Text("a",size=15,),),
                DataColumn(Text("g",size=15,),),
                DataColumn(Text("o",size=15,),),
            ],
            rows=[
                DataRow(
                    cells=[
                        DataCell(Text("0",size=15,)),
                        DataCell(Text("1",size=15,)),
                        DataCell(Text("2",size=15,)),
                        DataCell(Text("3",size=15,)),
                        DataCell(Text("4",size=15,)),
                        DataCell(Text("5",size=15,)),
                        DataCell(Text("6",size=15,)),
                        DataCell(Text("7",size=15,)),
                        DataCell(Text("8",size=15,)),
                        DataCell(Text("9",size=15,)),
                    ],
                ),
            ],
        )
    #* esta es la tabla de cenit polar 
    tab_cen_pol= DataTable(
        border=border.all(2,"blue"),border_radius=10,
            columns=[
                DataColumn(Text("c",size=20,),),
                DataColumn(Text("e",size=20,),),
                DataColumn(Text("n",size=20,),),
                DataColumn(Text("i",size=20,),),
                DataColumn(Text("t",size=20,),),
            ],
            rows=[
                DataRow(
                    cells=[
                        DataCell(Text("p",size=20,)),
                        DataCell(Text("o",size=20,)),
                        DataCell(Text("l",size=20,)),
                        DataCell(Text("a",size=20,)),
                        DataCell(Text("r",size=20,)),
                    ],
                ),
            ],
        )
    
    tabla_rot13 = DataTable(
        border=border.all(2,"blue"),border_radius=10,
            columns=[
                DataColumn(Text("a",size=20,),),
                DataColumn(Text("b",size=20,),),
                DataColumn(Text("c",size=20,),),
                DataColumn(Text("d",size=20,),),
                DataColumn(Text("e",size=20,),),
                DataColumn(Text("f",size=20,),),
                DataColumn(Text("g",size=20,),),
                DataColumn(Text("h",size=20,),),
                DataColumn(Text("i",size=20,),),
                DataColumn(Text("j",size=20,),),
                DataColumn(Text("k",size=20,),),
                DataColumn(Text("l",size=20,),),
                DataColumn(Text("m",size=20,),),
            ],
            rows=[
                DataRow(
                    cells=[
                        DataCell(Text("n",size=20,)),
                        DataCell(Text("o",size=20,)),
                        DataCell(Text("p",size=20,)),
                        DataCell(Text("q",size=20,)),
                        DataCell(Text("r",size=20,)),
                        DataCell(Text("s",size=20,)),
                        DataCell(Text("t",size=20,)),
                        DataCell(Text("u",size=20,)),
                        DataCell(Text("v",size=20,)),
                        DataCell(Text("w",size=20,)),
                        DataCell(Text("x",size=20,)),
                        DataCell(Text("y",size=20,)),
                        DataCell(Text("z",size=20,)),
                    ],
                ),
            ],
        )
    
    
    #* esta es la tabla de 5x5
    sin_cod = TextField(label= "Entrada texto", width=500,)
    tab_cincoxcinco = DataTable(
        border=border.all(2,"blue"),border_radius=10,
        columns =[
        DataColumn(Text(" ",size=20,)),
        DataColumn(Text("1",size=20,)),
        DataColumn(Text("2",size=20,)),
        DataColumn(Text("3",size=20,)),
        DataColumn(Text("4",size=20,)),
        DataColumn(Text("5",size=20,))],
        rows =  [],)
    
    def tab_cinc(event: str= ""):
        "esta funcion agrega todos las letras y agrega una columna numerica"
        vueltas = 1
        for element in range(0,len(letr_cinxcin),5):
            tab_cincoxcinco.rows.append(DataRow(cells=[
                    DataCell(Text(value=f"{vueltas}",size=20,)),
                    DataCell(Text(value=f"{letr_cinxcin[element]}",size=20,)),
                    DataCell(Text(value=f"{letr_cinxcin[element+1]}",size=20,)),
                    DataCell(Text(value=f"{letr_cinxcin[element+2]}",size=20,)),
                    DataCell(Text(value=f"{letr_cinxcin[element+3]}",size=20,)),
                    DataCell(Text(value=f"{letr_cinxcin[element+4]}",size=20,)),]))
            vueltas +=1
        actualizar()
        
    
    #* aca comienza el codigo de a pantalla
    page.title = "Scoutsito"
    page.window_width = 550 
    page.window_height = 500
    
    def close_banner(event):
        "este hace desaparecer el cartel de error"
        page.banner.open = False
        page.update()

    page.banner = Banner(
        bgcolor=colors.WHITE,
        leading=Icon(icons.WARNING_AMBER_ROUNDED, color=colors.BLACK, size=40),
        content=Text(
            "o no esta poniendo algo para traducir, o no estas eligiendo con que traducir", 
            color= colors.BLACK
        ),
        actions=[
            TextButton("okay", on_click=close_banner),
        ],
    )

    def mostrar_cartel(event):
        "hace aparecer el cartel de error"
        page.banner.open = True
        page.update()

    
    def camb_color(e):
        "esta parte cambia el color de la app a modo black"
        page.theme_mode = (
            ThemeMode.DARK
            if page.theme_mode == ThemeMode.LIGHT
            else ThemeMode.LIGHT
        )
        c.label = (
            "Light Mode" if page.theme_mode == ThemeMode.LIGHT else "Dark Mode"
        )
        page.update()

    page.theme_mode = ThemeMode.LIGHT
    c = Switch(label="Light Mode", on_change=camb_color, label_position=LabelPosition.LEFT)
    
    tablas = Row(alignment=MainAxisAlignment.CENTER)
    
    def boton (event):
        tablas.controls.clear()
        if dd.value == "Cenit Polar":
            tablas.controls.append(tab_cen_pol)
        if dd.value == "Murcielago":
            tablas.controls.append(tab_murcielago)
        if dd.value == "Morse":
            tablas.controls.append(tab_morse_2)
            tab_morse()
        if dd.value == "5X5":
            tablas.controls.append(tab_cincoxcinco)
            tab_cinc()
        if dd.value == "7 Cruces":
            tablas.controls.append(tab_morse_2)
            tab_morse()
        if dd.value == "Rot 13":
            tablas.controls.append(tabla_rot13)
        actualizar()
    #* ↓ esto es la dropbox donde guardan los codigos
    dd = Dropdown(
        label= "Codigo",
        on_change= boton,
        options=[
            dropdown.Option("Morse"),
            dropdown.Option("Cenit Polar"),
            dropdown.Option("5X5"),
            dropdown.Option("7 Cruces"),
            dropdown.Option("Rot 13"),
            dropdown.Option("Murcielago"),
            
        ],
        width=200,
    )
    
    codificado = TextField(label= "Salida de texto",hint_text="", width=500,)

    cod = codigos()
    def traducir_text(event):
        """ #* sirve para traducir el texto a el codigo deceado """
        if sin_cod.value != "":
            codificado.clean
            if dd.value == "Morse":
                trad = sin_cod.value
                resolucion = cod.morse(trad)
                codificado.value = resolucion
            elif dd.value == "Cenit Polar":
                trad = sin_cod.value
                resolucion = cod.Cenit_polar(trad)
                codificado.value = resolucion
            elif dd.value == "5X5":
                trad = sin_cod.value
                resolucion = cod.cincoxcinco(trad)
                codificado.value = resolucion
            elif dd.value == "7 Cruces":
                trad = sin_cod.value
                resolucion = cod.siete_cruses(trad)
                codificado.value = resolucion
            elif dd.value == "Rot 13":
                trad = sin_cod.value
                resolucion = cod.rot_trece(trad)
                codificado.value = resolucion
            elif dd.value == "Murcielago":
                trad = sin_cod.value
                resolucion = cod.murcielago(trad)
                codificado.value = resolucion
            else:
                mostrar_cartel("")
        else :
            mostrar_cartel("")
        page.update() 
        
    #* este es el boton de traducir
    bot_trad = ElevatedButton("traducir", on_click=traducir_text)
    
    #* ↓ contiene el boton de traducir y el dropbox de los codigos
    col_trad = Row([dd, bot_trad,], alignment=MainAxisAlignment.CENTER)
    
    nuevo_sin_cod = ResponsiveRow([sin_cod, col_trad, codificado,])
    colu_principal = Column ([c, nuevo_sin_cod])
    
    page.add(colu_principal, tablas)

if __name__ == "__main__":
    app(target=main)
