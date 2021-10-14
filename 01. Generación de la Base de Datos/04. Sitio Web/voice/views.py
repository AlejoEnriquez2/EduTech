from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
import datetime

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def prueba(request):
    fecha_actual=datetime.datetime.now()
    return render(request, "Prueba.html", {"dameFecha":fecha_actual})
        
def saludo(request):
    nombre = "Juan"
    apellido = "Lopez"
    habilidades = ["Programacion", "Lider", "Deportista"]
    p1 = Persona(nombre, apellido)
    ahora = datetime.datetime.now()
    #doc_externo = open("/home/alejo/Documents/EduTech/Fase1/codigo/voice/voice/plantillas/plantilla1.html")
    #plt = Template(doc_externo.read())
    #doc_externo.close()
    #doc_externo = loader.get_template("plantilla1.html")
    #ctx = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "ahora":ahora, "habilidades":habilidades})
    #documento = doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "ahora":ahora, "habilidades":habilidades})
    #return HttpResponse(documento)
    return render(request, "plantilla1.html", {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "ahora":ahora, "habilidades":habilidades})

def despedida(request):
    return HttpResponse("Adios django")

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""
    <html>
        <body>
            <h1>La hora actual es: %s</h1>
        </body>
    </html>
    """ % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, anio, edadActual):    
    periodo = anio-2021
    edadFutura = edadActual+periodo
    documento="""
    <html>
        <body>
            <h1>En el anio: %s tendras %s anios</h1>
        </body>
    </html>
    """ %(anio, edadFutura)

    return HttpResponse(documento)
