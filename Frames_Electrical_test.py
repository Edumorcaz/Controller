import tkinter as tk
import json

window = tk.Tk()
window.geometry('1000x700')
window.title('Trafficware - Cabinets')
window.iconbitmap('semaphore.ico')

#Es la informacion de los gabinetes que se tienen en produccion
def cabinets_in_floor():
    with open('Tracking_Cabinets.json','r+') as file_tracking_cabinets:
        Cabinets_data=json.load(file_tracking_cabinets)
        return(Cabinets_data)
    
#Es la configuracion de pruebas asignadas a los modelos de gabinetes
def setup():
    with open('Setup_cabinet.json','r+') as file_setup_cabinet:
        Cabinets_setup=json.load(file_setup_cabinet)
        return(Cabinets_setup)

#Es el repertorio de pruebas que se pueden implementar
def settings():
    with open('settings.json','r+') as file_settings:
        Cabinets_settings=json.load(file_settings)
        return(Cabinets_settings)

#Revisar modelo para cargar la configuracion correspondiente
#Model = "70006-3044E"
#List_settings=settings()

#index=List_settings.index("")


window.mainloop

