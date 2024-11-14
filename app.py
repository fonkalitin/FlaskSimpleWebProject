"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from os import write
from subprocess import CREATE_NEW_CONSOLE
from flask import Flask
from flask import flask_restful
from flask import Api, Resource, request
app = Flask(__name__)
 

# Make the WSGI interface available at the top level so wfastcgi can get it. 
wsgi_app = app.wsgi_app


@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"


def tank_h(D,h_otb,L,h_dn,h_ur):
    D = 1;
    print(D,h_otb,L,h_dn,h_ur)
    return("Функция вернула ответ")

def getList():

    try:
        listOfValues = myCalculateFunction.getList() # вызов нужной функции-обработчика с соответствующим методом для получение списка значений
                # [ 'Сантипуаз', 'Пуаз', 'Паскаль-секунда' ]  - метод getList должен вернуть список значений
 
        stringOfValues = ','.join(listOfValues) # Преобразуем список в строку, разделяемую запятыми
         # преобразование можно вынести и в исходную функцию и сразу же вернуть сюда готовую строку**
 
        return stringOfValues, 200, {'Content-Type': 'text/plain'} # метод возвращает HTTP-статус 200 в случае успешного запроса, и сообщает клиенту как интерпретировать ответ (простой текст)
    except ValueError:
        return "Ошибка. Запрос не верный.", 400 # метод возвращает HTTP-статус 404 в случае если запись не найдена.


def getFunc():  
    try:
        getValues =  request.args.get(value, 0) # получение значения из запроса

        getValuesList = getValues.split(',')
        #convertedValue = myCalculateFunction(getValue) # тут вызов нужной функции-обработчика и получение из нее значения value
        tank_h(getValuesList)
        
        return convertedValue, 200 # метод возвращает HTTP-статус 200 в случае успешного запроса.
    except ValueError:
        return "Ошибка. Запрос не верный.", 400 # метод возвращает HTTP-статус 404 в случае если запись не найдена.
 



if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
