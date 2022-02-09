from tkinter import *
import requests

def mostrar_respuesta(clima):
	try:
		nombre_ciudad = clima['name']
		desc = clima['weather'][0]['description']
		temp = clima['main']['temp']

		ciudad['text'] = nombre_ciudad
		descripcion['text'] = desc
		temperatura['text'] = str(int(temp)) + "°C"
	except:
		ciudad['text'] = 'Intente nuevamente'

def clima_JSON(ciudad):
	try:
		API_key = '5a8644a22a77468a14ee1d89c1f0cb92'
		URL = 'https://api.openweathermap.org/data/2.5/weather?'
		parametros = {'APPID': API_key, 'q': ciudad, 'units': 'metric', 'lang':'es'}
		response = requests.get(URL, params = parametros)
		clima = response.json()
		mostrar_respuesta(clima)

		print(clima['name'])
		print(clima['weather'][0]['description'])
		print(clima['main']['temp'])
	except:
		print('ERROR')


ventana = Tk()
ventana.title("MoonSky")
ventana.attributes('-toolwindow', 'True')
ventana.geometry('350x400')
ventana.resizable(False,False)
ventana.config(bg='#779ECB')

texto_ciudad = Entry(ventana, font=('Courier', 20, 'normal'), justify='center', bg='#dde6f2', borderwidth=0)
texto_ciudad.pack(pady=15)

obtener_clima = Button(ventana, text='Obtener Clima', font=('Courier', 20, 'normal'), bg='#2d3b4c', fg='#dde6f2', borderwidth=0, command=lambda: clima_JSON(texto_ciudad.get()))
obtener_clima.pack(pady=20)

ciudad = Label(font=('Courier', 20, 'normal'), bg='#779ECB', fg='#dde6f2', borderwidth=0)
ciudad.pack(pady=5)

temperatura = Label(font=('Courier', 50, 'normal'), bg='#779ECB', fg='#dde6f2', borderwidth=0)
temperatura.pack(pady=5)

descripcion = Label(font=('Courier', 20, 'normal'), bg='#779ECB', fg='#dde6f2', borderwidth=0)
descripcion.pack(pady=10)

ventana.mainloop()