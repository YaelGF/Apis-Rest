import web
import json
import random

urls= (
  '/zodiaco/(.*)','Zodiaco',
)
app = web.application(urls, globals())


class Zodiaco:
  def GET(self, fecha):
    predicion = [" tiene un problema contigo", " es tu amor platonico", " compatibilidad del 50%", " dijo que chingas a tu madre", " esta enamorado de ti en secreto"]
    data={}
    zodi=[]
    try:
      zodi=fecha.split(',')
      if(int(zodi[0]) <32):
        dia= int(zodi[0])
      messusti = zodi[1]
      meses = {"enero" : 1, "febrero" : 2, "marzo" : 3, "abril" : 4, "mayo" : 5, "junio" : 6, "julio" : 7, "agosto" : 8, "septiembre" : 9, "octubre" : 10, "noviembre" : 11, "diciembre" : 12}
      signo = ("Capricornio", "Acuario", "Piscis", "Aries", "Tauro","Geminis", "Cancer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario")
      fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)
      mes = meses[messusti]
      mes -= 1
      if (dia > fechas[mes]):
        mes += 1
      if (mes == 12):
        mes = 0
      buscar = signo[mes]
      data ["status"] = 200
      signoinfo={
        signo[0]: {"signo" : signo[0],"elemento" : "Tierra", "Color" : "Negro", "Numero Suerte" : random.randrange(100) , "Horoscopo" : "Los capricornio son personas fuertes y resistentes ante cualquier situacion, por eso tienen este color de aura, pues son los que mas resaltan entre los signos del zodiaco por su valentia y persistencia. Se entienden perfecto con auras rosas o amarillas.","Predicion" : random.choice(signo)+random.choice(predicion), "img" : "https://python-curso.yaelgf.repl.co/static/img/capricornio.jpg"},
        signo[1]: {"signo" : signo[1],"elemento" : "Aire", "Color" : "Verde", "Numero Suerte" : random.randrange(100) , "Horoscopo" : "Los acuario buscan siempre ayudar a los demas, dar paz y tranquilidad a la vida de los otros y sobre todo ayudarles a superarse personalmente, por eso el color de la naturaleza es el que los rige. Son compatibles con las personas de auras azules y verdes.","Predicion" : random.choice(signo)+random.choice(predicion), "img" : "https://python-curso.yaelgf.repl.co/static/img/acuario.jpg"},
        signo[2]: {"signo" : signo[2],"elemento" : "Agua", "Color" : "Violeta", "Numero Suerte" : random.randrange(100) , "Horoscopo" : "Estas personas son independientes, soñadoras y creativas, por eso el color de su aura es el violeta pues representa la imaginacion y los sueños. Los piscis nunca dejan que los manipulen o les digan que hacer, por eso se entienden perfecto con auras de color indigo. ","Predicion" : random.choice(signo)+random.choice(predicion), "img" : "https://python-curso.yaelgf.repl.co/static/img/piscis.jpg"},
        signo[3]: {"signo" : signo[3],"elemento" : "Fuego", "Color" : "Rojo", "Numero Suerte" : random.randrange(100) , "Horoscopo" : "El rojo es el color de la pasion y los Aries son pasionales en todos los aspectos de la vida, son entregados y muy competitivos en todo lo que hacen. Suelen ser compatibles con personas de aura amarillo o naranja.","Predicion" : random.choice(signo)+random.choice(predicion),"img" : "https://python-curso.yaelgf.repl.co/static/img/aries.jpg"},
        signo[4]: {"signo" : signo[4],"elemento" : "Tierra", "Color" : "Marron", "Numero Suerte" : random.randrange(100) , "Horoscopo" : "Su tonalidad concuerda perfectamente con su personalidad, son fuertes, audaces y un poco misteriosos, amantes de la perfeccion y muy objetivos. Tienden a entenderse perfecto con auras verdes, azules y blancas.","Predicion" : random.choice(signo)+random.choice(predicion),"img" : "https://python-curso.yaelgf.repl.co/static/img/tauro.jpg"},
        signo[5]: {"signo" : signo[5],"elemento" : "Aire", "Color" : "Amarillo", "Numero Suerte" : random.randrange(100) , "Horoscopo" : "Los geminis se caracterizan por transmitir su energia y pensamientos y sobre todo por llamar la atencion de todos, por eso el amarillo es su color, pues son vibrantes y contagiosos, como la personalidad de las personas de este signo. Ellos son compatibles con auras naranjas y rojos.","Predicion" : random.choice(signo)+random.choice(predicion),"img" : "https://python-curso.yaelgf.repl.co/static/img/geminis.jpg"},
        signo[6]: {"signo" : signo[6],"elemento" : "Agua", "Color" : "Rosa", "Numero Suerte" : random.randrange(100) , "Horoscopo" : "El rosa es un color claro que transmite ternura, amor, serenidad y romanticismo, las personas de este signo suelen ser muy romanticas y enamoradizas, tanto de las personas como de la vida, por eso todo el tiempo transmiten buena vibra. Son compatibles con auras rojos, pues se complementan a la perfeccion.","Predicion" : random.choice(signo)+random.choice(predicion), "img" : "https://python-curso.yaelgf.repl.co/static/img/cancer.jpg"},
        signo[7]: {"signo" : signo[7],"elemento" : "Fuego", "Color" : "Naranja", "Numero Suerte" : random.randrange(100) , "Horoscopo" : "Las personas de leo son creativas, alegres y cuentan con mucha energia, por eso su color es el del sol y del atardecer. Son compatibles con auras rojas, amarillas y rosas; tener algun tipo de relacion con estos colores sera muy benefico para los leo. ","Predicion" : random.choice(signo)+random.choice(predicion), "img" : "https://python-curso.yaelgf.repl.co/static/img/leo.jpg"},
        signo[8]: {"signo" : signo[8],"elemento" : "Tierra", "Color" : "Turquesa", "Numero Suerte" : random.randrange(100) , "Horoscopo" : "Son personas inteligentes y racionales, aunque son un poco timidos siempre buscan conocer nuevas personas y tener nuevas experiencias. Son inteligentes y siempre tratan de rodearse de personas que aporte algo positivo a usted vida, por eso se entienden perfecto con personas de auras amarillas y verdes.","Predicion" : random.choice(signo)+random.choice(predicion),"img" : "https://python-curso.yaelgf.repl.co/static/img/virgo.jpg"},
        signo[9]: {"signo" : signo[9],"elemento" : "Aire", "Color" : "Blanco", "Numero Suerte" : random.randrange(100) , "Horoscopo" : "El color de aura de los libra es el rosa, pues son personas tranquilas, muy cariñosas y sinceras, caracteristicas del color. Son compatibles con auras rosas, verdes y azules, con ellos pueden crear conexiones increibles.","Predicion" : random.choice(signo)+random.choice(predicion), "img" : "https://python-curso.yaelgf.repl.co/static/img/libra.jpg"},
        signo[10]: {"signo" : signo[10],"elemento" : "Agua", "Color" : "Indigo", "Numero Suerte" : random.randrange(100) , "Horoscopo" : "Aunque son personas de sentimientos muy fuerte y emociones extremas, son a la vez muy misteriosos, pues no suelen demostrarlo. Por eso su color es el indigo que refleja la sensibilidad y la intuicion. Son compatibles con auras rojas y violetas.","Predicion" : random.choice(signo)+random.choice(predicion), "img" : "https://python-curso.yaelgf.repl.co/static/img/escorpion.jpg"},
        signo[11]: {"signo" : signo[11],"elemento" : "Fuego", "Color" : "Azul", "Numero Suerte" : random.randrange(100) , "Horoscopo" : "Los sagitarianos se caracterizan por ser personas responsables, honestas, creativas y respetables a las que les encanta divertirse, son comprensibles con los demas y muy empaticos, por eso conectan sus emociones a la perfeccion con auras de color rojo o amarillo.","Predicion" : random.choice(signo)+random.choice(predicion),"img" : "https://python-curso.yaelgf.repl.co/static/img/sagitario.jpg"}
    }
      data ["info"] = signoinfo[buscar]
    
    except UnboundLocalError:
      data["status"] = 400
      data["mesagge"] = "No hay dia mayor a 31"
      data["error"] = "UnboundLocalError"
    except Exception as e:
      data["status"] = 400
      data["mesagge"] = "Separa el dia y la fecha con coma"
      data["error"] = type(e).__name__
    finally:
      result = json.dumps(data)
      return result
  
        
if __name__=="__main__":
  app.run()