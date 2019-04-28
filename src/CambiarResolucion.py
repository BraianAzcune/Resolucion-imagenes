import PIL 
from PIL import Image
import Sistema
class CambiarResolucion:

    dondeGuardar=1280

    #rutaImagen tiene la ruta completa de la imagen para poder abrirla
    #dondeGuardar posee la ruta completa de donde guardar, incluido el nombre y extension de la imagen.
    @staticmethod
    def cambiarResolucion(rutaImagen,dondeGuardar):
        
        img = Image.open(rutaImagen)

        


        ancho= float(img.size[0])
        alto= float(img.size[1])

        if ancho>CambiarResolucion.dondeGuardar or alto>CambiarResolucion.dondeGuardar:
    
            if ancho > alto:
                wpercent = (CambiarResolucion.dondeGuardar / ancho)
                hsize = int(alto * float(wpercent))
                img = img.resize((CambiarResolucion.dondeGuardar, hsize), PIL.Image.ANTIALIAS)
                #img = img.resize((CambiarResolucion.dondeGuardar, hsize))
                img.save(dondeGuardar)
            else:
                hpercent=(CambiarResolucion.dondeGuardar/alto)
                wsize=int(ancho*float(hpercent))
                img= img.resize((wsize,CambiarResolucion.dondeGuardar),PIL.Image.ANTIALIAS)
                #img= img.resize((wsize,CambiarResolucion.dondeGuardar))
                img.save(dondeGuardar)


        else:
                img.save(dondeGuardar)
