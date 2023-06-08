from flet import Page, app, Column, TextField, dropdown, Dropdown, ElevatedButton, Row, LabelPosition 
from flet import ThemeMode, Switch,DataTable, DataColumn, DataRow, DataCell, Text, border, FontWeight
from time import sleep

mesclados = { 
#la pocicion 0 es morse la 1 es siete cruces
'a':['.-/','1v ','1-1/',], 
'b':['-.../','<1 ','1-2/'],
'c':['-.-./','1ʌ ','1-3/'],
'd':['-../','1> ','1-4/'],
'e':['./','2v ','1-5/'],
'f':['..-./','<2 ','2-1/'],
'g':['--../','2ʌ ','2-2/'],
'h':['..../','2ʌ ','2-3/'],
'i':['../','3v ','2-4/'],
'j':['.---/','<3 ','2-4/'],
'k':['-.-/','3ʌ ','2-5/'],
'l':['.-../','3> ','3-1/'],
'm':['--/','4v ','3-2/'],
'n':['-./','<4 ','3-3/'],
'ñ':['--.--/','4ʌ ','ñ/'],
'o':['---/','4> ','3-4/'],
'p':['.--./','5v ','3-5/'],
'q':['--.-/','<5 ','4-1/'],
'r':['.-./','5ʌ ','4-2/'],
's':['.../','5> ','4-3/'],
't':['-/','6v ','4-4/'],
'u':['..-/','<6 ','4-5/'],
'v':['...-/','6ʌ ','5-1/'],
'w':['.--/','6> ','5-2/'],
'x':['-..-/','7v ','5-3/'],
'y':['-.--/','<7 ','5-4/'],
'z':['--../','7ʌ ','5-5/'],
' ':['/','7> ', ' '],
'1': ['.----', '(1)',], 
'2': ['..---', '(2)',], 
'3': ['...--', '(3)',], 
'4': ['....-', '(4)',], 
'5': ['.....', '(5)',], 
'6': ['-....', '(6)',], 
'7': ['--...', '(7)',], 
'8': ['---..', '(8)',], 
'9': ['----.', '(9)',], 
'0': ['-----', '(0)',], 
}

murcielago_cod = {
        'm': '0',
        'u': '1',
        'r': '2',
        'c': '3',
        'i': '4',
        'é': '5',
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
    terminado = []
    espacio =0
    for x in traducir:
        letr = traducir [espacio]
        traducido = mesclados.get (letr,f"{traducir[espacio]}")
        terminado += traducido [p]
        espacio += 1
        listo = ''.join(terminado)
    return listo
        
class codigos():
    
    @staticmethod
    def morse(lista:str=""):
        traducir = list (lista.lower())
        traducido = codigos_complejos(0,traducir)
        return traducido
        
    
    @staticmethod
    def siete_cruses(lista:str=""):
        traducir = list (lista.lower())
        traducido = codigos_complejos(1,traducir)
        return traducido
    
    @staticmethod
    def murcielago(lista:str=""):
        frase_codificada = ''
        for letra in lista:
            if letra.lower() in murcielago_cod:
                frase_codificada += murcielago_cod[letra.lower()]
            else:
                frase_codificada += letra

        return frase_codificada
    
    @staticmethod
    def Cenit_polar(lista:str=""):
        frase_codificada = ''
        for letra in lista:
            if letra.lower() in cenit_polar:
                frase_codificada += cenit_polar[letra.lower()]
            else:
                frase_codificada += letra

        return frase_codificada
    
    @staticmethod
    def rot_trece(lista:str=""):
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
        traducir = list (lista.lower())
        traducido = codigos_complejos(2,traducir)
        return traducido
    

 
def main(page: Page):
    page.title = "Scoutsito"
    
    def theme_changed(e):
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
    c = Switch(label="Light Mode", on_change=theme_changed, label_position=LabelPosition.LEFT)
    
    mensajes = Text(value= "", size= 30, weight=FontWeight.BOLD)
    
    def  mens_momentaneo (texto :str = 'mensajito plis'):
        """se usa para mensajes de errores o cuando queres explicar algo"""
        mensajes.value = f"{texto}"
        page.update()
        sleep(2)
        mensajes.value= ""
        page.update()
        pass
    
    
    swi_men = Row([c, mensajes, ])
    
    sin_cod = TextField(label= "Entrada texto", width=500,)
    
    dd = Dropdown(
        label= "Codigo",
        options=[
            dropdown.Option("Morse"),
            dropdown.Option("Cenit Polar"),
            dropdown.Option("5x5"),
            dropdown.Option("7 Cruces"),
            dropdown.Option("Rot 13"),
            dropdown.Option("Murcielago"),
            
        ],
        width=200,
    )
    
    codificado = TextField(label= "Salida de texto",hint_text="", width=500,)
    
    
    
    cod = codigos()
    def traducir_text(event):
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
            elif dd.value == "5x5":
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
                mens_momentaneo("Eleji en que queres traducir")
        else :
            mens_momentaneo("Escribi algo para traducir")
        page.update() 
        
    
    bot_trad = ElevatedButton("traducir", on_click=traducir_text)
    col_trad = Row([dd, bot_trad,], )
    
        
    colu_principal = Column ([swi_men, sin_cod, col_trad, codificado,])
    
    
    page.add(colu_principal)

app(target=main)
