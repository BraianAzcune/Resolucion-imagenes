import os
import CambiarResolucion
import progress
from progress.bar import Bar

#NOTA= Cosas que pueden ser editadas
#Nombre de la carpeta que se crea

class Sistema:
    """Se encarga de llamar a cambiarResolucion, le pasa los parametros y crea carpetas, todo lo relacionado
    a comunicarse con el Sistema Operativo"""

    #ruta de la carpeta por defecto
    rutaCarpetaAGuardar=""
    nombreNuevaCarpeta="Fotos_Subir"

    def __init__(self, rutasImagenes):
        
        #definimos la ruta de la carpeta
        Sistema.rutaCarpetaAGuardar= self.rutaDeImagen(rutasImagenes[0])+"\\"+Sistema.nombreNuevaCarpeta
        
        #creamos la carpeta
        self.crearCarpeta()

        #para cada imagen, tomamos la ruta donde se guardara, y llamamos a CambiarResolucion, que cambiara y guardara la img.
        bar = Bar('Procesando',max=len(rutasImagenes))
        
        for imagen in rutasImagenes:
            dondeGuardar= self.nuevaRuta(imagen)
            CambiarResolucion.CambiarResolucion.cambiarResolucion(imagen,dondeGuardar)
            bar.next()
        bar.finish()


    #Entrega la ruta de la imagen
    def rutaDeImagen(self,imagen):
        return os.path.dirname(imagen)

    #devuelve la ruta del nuevo archivo, junto con su nombre y extension.
    def nuevaRuta(self, rutaOriginal):

        nuevaRuta=Sistema.rutaCarpetaAGuardar+"\\"+os.path.basename(os.path.normpath(rutaOriginal))
        
        return nuevaRuta

    #crea una carpeta con el nombre rutaCarpetaAGuardar, si ya exite le agrega un numero al final.
    def crearCarpeta(self):
        
        ruta=Sistema.rutaCarpetaAGuardar
        number= 1
        flag=True

        while(flag):

            if not os.path.exists(ruta):
                try:

                    os.mkdir(ruta)
                    #Si salio bien actualizamos la ruta
                    Sistema.rutaCarpetaAGuardar=ruta
                except OSError:
                    raise ValueError('Fallo al crear la carpeta')

                flag=False
            else:
                ruta=Sistema.rutaCarpetaAGuardar
                ruta+=str(number)
                number+=1


