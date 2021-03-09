import web
import json

urls= (
  '/par/(.*)','Par',
)
app = web.application(urls, globals())

class Par:
  def GET(self, numero):
    try:
      data={}
      if int(numero) % 2 ==0:
        data["result"]="par"
      else:
        data["result"]="impar"
      data["status"]= 200
      result = json.dumps(data)
      return result
    except:
      data= {}
      data["status"]= 400
      data["error"] = "El valor debe ser entero"
      result = json.dumps(data)
      return result
if __name__=="__main__":
  app.run()