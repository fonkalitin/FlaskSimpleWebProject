
# coding=windows-1251

from ast import Str
from os import write
from subprocess import CREATE_NEW_CONSOLE
from flask import Flask
#from flask import flask_restful
#from flask import Api, Resource, request
from flask import request
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it. 
wsgi_app = app.wsgi_app


@app.route('/convertTank', methods=['GET'])
def getVal():
    try:
        getValues =  request.args.get('value', 0) # ��������� �������� �� �������
        getValuesList = getValues.split(',')
        D = getValuesList[0]
        h_otb = getValuesList[1] 
        L = getValuesList[2] 
        h_dn = getValuesList[3] 
        h_ur =getValuesList[4] 

        returnedValue = tank_h(D, h_otb, L, h_dn, h_ur) #','.join(tank_h(D, h_otb, L, h_dn, h_ur))  # ��� ����� ������ �������-����������� � ��������� �� ��� �������� value

        return returnedValue, 200, {'Content-Type': 'text/plain'} # ����� ���������� HTTP-������ 200 � ������ ��������� �������.
    except ValueError:
        return "Error.", 400 # ����� ���������� HTTP-������ 404 � ������ ���� ������ �� �������.
 


def tank_h(D, h_otb, L, h_dn, h_ur):  #h_otb,L,h_dn,h_ur
    #D = 1;
    print(D)
    return("������� ������� ��������� ����� ��������: ", D, h_otb, L, h_dn, h_ur)

def getList():

    try:
        #listOfValues = myCalculateFunction.getList() # ����� ������ �������-����������� � ��������������� ������� ��� ��������� ������ ��������
                # [ '���������', '����', '�������-�������' ]  - ����� getList ������ ������� ������ ��������
 
        #stringOfValues = ','.join(listOfValues) # ����������� ������ � ������, ����������� ��������
        # �������������� ����� ������� � � �������� ������� � ����� �� ������� ���� ������� ������**

        return 0, 200, {'Content-Type': 'text/plain'} # ����� ���������� HTTP-������ 200 � ������ ��������� �������, � �������� ������� ��� ���������������� ����� (������� �����)
    except ValueError:
        return "Error.", 400 # ����� ���������� HTTP-������ 404 � ������ ���� ������ �� �������.


def getFunc():  
    try:
        getValues =  request.args.get('value', 0) # ��������� �������� �� �������
        #getValuesList = getValues.split(',')
        returnedValue = tank_h(getValues) # ��� ����� ������ �������-����������� � ��������� �� ��� �������� value

        return returnedValue, 200 # ����� ���������� HTTP-������ 200 � ������ ��������� �������.
    except ValueError:
        return "Error.", 400 # ����� ���������� HTTP-������ 404 � ������ ���� ������ �� �������.
 

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)


    # /convertTank/?value=1,2,3,4,5

