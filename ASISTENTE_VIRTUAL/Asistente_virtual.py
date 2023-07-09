import time
inicio = time.time()
import pyttsx3
import speech_recognition as sr
import yfinance as yf
tiempo_sin_librerias = time.time()
import pyjokes
import pywhatkit
import webbrowser
import datetime
import wikipedia

id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'


# escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print('ya puedes hablar')

        # guardar lo ue escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language='es-co')

            # prueba de que pudo ingresar
            print('digiste' + pedido)

            # devolver pedido
            return pedido

        # en caso de que no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendio el audio
            print('ups, no entendi')

            # devolver error
            return 'sigo esperando'

        # en caso de no resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print('ups, no hay servicio')

            # devolver error
            return 'sigo esperando'

        # en caso de no resolver el pedido
        except:

            # prueba de que no comprendio el audio
            print('ups, algo salio mal')

            # devolver error
            return 'sigo esperando'


#funcion para que el asistente pueda ser escuchado
def hablar(mensaje):

    # ensender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id3)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


#informar el dia de la semana
def pedir_dia():

    # crear variable con datos de hoy
    hoy = datetime.date.today()
    print(hoy)

    # crear variable con datos de la semana
    dia_semana = hoy.weekday()
    print(dia_semana)

    # diccionario con nombres de dias
    calendario = {0:'Lunes',
                  1:'Martes',
                  2:'miércoles',
                  3:'jueves',
                  4:'viernes',
                  5:'sábado',
                  6:'domingo'}

    # decir el dia de la semana
    hablar(f'hoy es {calendario[dia_semana]}')


# informar que hora es
def pedir_hora():

    # crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'en este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    # decir la hora
    hablar(hora)


# funcion saludo inicial
def saludo_inicial():

    # crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour >= 19 and hora.hour <= 5:
        momento = 'Buenas noches'
    elif 5 < hora.hour < 12:
        momento = 'buenos dias'
    else:
        momento = 'buenas tardes'

    # decir el saludo
    hablar(f'{momento} soy sabina, tu asistenete personal. Dime en que te puedo ayudar')


# funcion central del asistente
def pedir_cosas():

    # activar saludo inicial
    saludo_inicial()

    # variable de corte
    comenzar = True

    # loop central
    while comenzar:

        # activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('con gusto estoy habriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue

        elif 'abrir navegador' in pedido:
            hablar('claro estoy en eso')
            webbrowser.open('https://www.google.com')
            continue

        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue

        elif 'qué hora es' in pedido:
            pedir_hora()
            continue

        elif 'busca en wikipedia' in pedido:
            hablar('buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('wikipedia dice lo siguiente')
            hablar(resultado)
            continue

        elif 'busca en internet' in pedido:
            hablar('ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('esto es lo que he encontrado')
            continue

        elif 'reproducir' in pedido:
            hablar('buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue

        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue

        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}

            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'la encontre, el precio de {accion} es de {precio_actual}')

            except:
                hablar('perdon pero no la he encontrado')

            continue

        elif 'adiós' in pedido:
            hablar('Me voy a descanzar, cualquier cosa me avisas')
            break

pedir_cosas()

final = time.time()
print(final-inicio)
print(final-tiempo_sin_librerias)











