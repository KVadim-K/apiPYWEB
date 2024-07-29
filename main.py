from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
   weather = None
   news = None
   if request.method == 'POST':
       city = request.form['city']
       #прописываем переменную, куда будет сохраняться результат и функцию weather с указанием города, который берем из формы
       weather = get_weather(city)
       #передаем информацию о погоде в index.html
       news = get_news()
   return render_template("index.html", weather=weather, news=news)

def get_weather(city):
   api_key = '656ff4407a5225762cbbb0487b7b630a'
   #адрес, по которомы мы будем отправлять запрос. Не забываем указывать f строку.
   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
   #для получения результата нам понадобится модуль requests
   response = requests.get(url)
   #прописываем формат возврата результата
   return response.json()

def get_news():
   api_key = "0a540c8fcaae42b49aff912ae81c088a"
   url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
   response = requests.get(url)
   return response.json().get('articles', [])



if __name__ == '__main__':
   app.run(debug=True)