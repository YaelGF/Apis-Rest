import json
data = {}
def get ():
      
  with open('datos.json') as file:
    data = json.load(file)

    dare = data
    return dare
def put (nombre,fecha,edad):
  dare = get()
  dare['Usuarios'].append({
      'Nombre':nombre,
      'Fecha-Nacimiento': fecha,
      'Edad':edad
    })
  with open('datos.json', 'w') as file:
    json.dump(dare, file, indent=4)


put("Juan","22/07/1998","22")
print(get())