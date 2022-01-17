from django.http import HttpResponse
import datetime
from django.template import Template, Context

from django.http.request import HttpRequest
from django.template import loader

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
html="se despidio"
#iniciamos primera vista saludo
def saludo(request):
    # nombre="Carlos"
    # apellido="Berro"
    #loader = cargador de plantillas
    p1=Persona("Profesor carlos","Berro")
    temas=["plantillas","modelos","Vista","despliegue"]
    ahora=datetime.datetime.now()


   # doc_externo=open("C:/Udemy/23.Djan/Miproject/plantillas/index.html")
  #  plt=Template(doc_externo.read())
    #doc_externo.close()
    doc_externo=loader.get_template('index.html')
    #ctx=Context({"nombre_persona ":p1.nombre,"apellido_persona":p1.apellido, "momento_actual":ahora,"temas":temas})
    #se almacena todo el rederizado de la pagina
    document=doc_externo.render({"nombre_persona ":p1.nombre,"apellido_persona":p1.apellido, "momento_actual":ahora,"temas":temas})
    return HttpResponse(document)


def despedida(request):         
    return HttpResponse(html)

def damefecha(request): 
    fecha_Actual=datetime.datetime.now()
    document="""
    <body>
    <h2>Fecha y hora %s</h2>
    </body>""" %fecha_Actual       
    return HttpResponse(document)

# def calculaEdad(request,edad,agno):
#     #_edadActual=18
#     periodo=agno-2022
#     edadFutura=edad+periodo
#     document="""
#     <body>
#     <h2>En el año %s tendras %s añosa</h2></body>"""%(agno, edadFutura) # => % marcador de posicion
#     return(document)

def plantilla(request):
    return HttpResponse("")