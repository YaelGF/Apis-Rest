import web
import json

urls= (
  '/nacimiento?','Nacimiento',
)
app = web.application(urls, globals())

class Nacimiento:
  def GET(self):
    data = {}
    try:
      
      parametros = web.input()
      name = parametros.name
      datee = parametros["date"].split('/')
      year= int(datee[2])
      edad= 2021 - year

      if (int(datee[1]) > 2):
        edad -= 1

      data["Name"] = name
      data["Edad"] = edad
    except Exception as e:
      data["Error"]= type(e).__name__

    finally: 
      
      archivo = open("static/database.txt", "a")
      result = json.dumps(data)
      archivo.write(result+",")
      archivo.close
      archivo = open("static/database.txt", "r")
      contenedor = archivo.read()
      return contenedor

   
if __name__=="__main__":
  app.run()