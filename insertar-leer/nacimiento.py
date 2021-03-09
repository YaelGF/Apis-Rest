import web
import json

urls= (
  '/insert?','Nacimiento',
)
app = web.application(urls, globals())

class Nacimiento:
  def GET(self):
    data = {}
    try:
      parametros = web.input()
      action =str(parametros.action)
      if action == "put":
        name = parametros.name
        datee = parametros["date"].split('/')
        year= int(datee[2])
        age= 2021 - year
        if (int(datee[1]) > 2):
          age -= 1
        put(name,parametros["date"],age)
        data["resultado"] = "registro almacenado"
      elif action == "get":
        data = get()
      else:
        data["Error"] = "valor no aceptado"      
    except Exception as e:
      data["Error"]= type(e).__name__

    finally: 
      result = json.dumps(data)
      return result
def put (nombre,fecha,edad):
    dare = {}
    dare = get()
    dare['Usuarios'].append({
        'Nombre':nombre,
        'Fecha-Nacimiento': fecha,
        'Edad':edad
      })
    with open('static/datos.json', 'w') as file:
      json.dump(dare, file, indent=4)
def get():
    with open('static/datos.json') as file:
      data = json.load(file)
    return data
   
if __name__=="__main__":
  app.run()