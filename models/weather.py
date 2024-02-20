import requests
import os
from dotenv import load_dotenv

class Clima:

    @staticmethod
    def buscar_o_clima(cidade):
        load_dotenv('.env')
        key = os.getenv('WEATHER_API_KEY')
        uri = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key}&lang=pt_br"
        requisicao = requests.get(uri)
        if requisicao.status_code == 200:
            os.system('cls')
            r = requisicao.json()
            descricao = r['weather'][0]['description']
            temperatura = r['main']['temp'] - 273.15
            print(f'A previsão em {cidade} é de: {temperatura:.2f}ºC com o seguinte clima: {descricao}')