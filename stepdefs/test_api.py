from cmath import e
from email import header
import imp
from importlib.resources import path
import json
from wsgiref import headers
import jsonpath
from pathlib2 import Path
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenarios, given, when, then,parsers
import requests
from requests.auth import HTTPBasicAuth
import pytest
# from pyseleniumbot.api_crud import crud
from pyallied.api_crud.crud import crud





def test_get_method():
    response=crud().crudCall(r"D:\Users\ssreeenivasreddy\Altimetrik_JCL\pythonseleniumframework\testdata\apiList.xlsx",'testcase_payment_5')
    # print(response.json())
    # print(response)
    code = 200
    # print(response.status_code)
    assert response.status_code == code
    '''
     #Dispaly Respose Content
    print(response.content)
     # Verify status code
    
     # Fetch Headers
     # print(response.headers)
     # Fetch specific respone header content
    print(response.headers.get('Date'))
    print(response.headers.get('Server'))
     # fetch cookies
    print(response.cookies)
     # fetch encoding
    print(response.encoding)
    print(response.elapsed)
    '''
    # parse response to json format
    json_response = json.loads(response.text)
    # print(json_response)
    # fetch vaule using json path
    a = jsonpath.jsonpath(json_response,'disclaimer')
    print(a)

    return response

def test_post_method():
    response=crud().crudCall(r"D:\Users\ssreeenivasreddy\Altimetrik_JCL\pythonseleniumframework\testdata\apiList.xlsx",'testcase_payment_6')
    #  print(responce.json())
    # print(response)
    # print(response.content)
    # print(response.headers.get('Content-Length'))
    # validation
    assert response.status_code == 201
    # fetch headers
    # print(response.headers)
    # parse respose to json format
    # response_json = json.loads(response.text)
    # id = jsonpath.jsonpath(response_json,'id')          # json path returns list
    # print(id[0])

def test_put_method():
    response=crud().crudCall(r"D:\Users\ssreeenivasreddy\Altimetrik_JCL\pythonseleniumframework\testdata\apiList.xlsx",'testcase_payment_7')
    # print(response)
    assert response.status_code == 200
    response_json = json.loads(response.text)
    # print(response_json)
    updated = jsonpath.jsonpath(response_json,'DOB')
    print(updated[0])

def test_delete_method():
    response=crud().crudCall(r"D:\Users\ssreeenivasreddy\Altimetrik_JCL\pythonseleniumframework\testdata\apiList.xlsx",'testcase_payment_8')
    # print(response)
    assert response.status_code == 204

# def test_basic_authentication():
#     response=requests.get('https://api.github.com/users', auth=HTTPBasicAuth('sreenivashs38@gmail.com', "Sree@2127"))
#     print(response.text)
#     print(response.status_code)

# def test_oauth():
#     uri = 'https://thetestingworldapi.com/api/StDetails/1104'
#     response=requests.get(uri)
#     print(response.text)




# def test_get_headers_method():
#     # Add Customised Headers
#     headerdata = {'Name_1':'Header_1', 'Name_2':'Header_2', 'Name_3':'Header_3'}
#     response = requests.get('https://httpbin.org/get',headers=headerdata)
#     print(response.text)
#     # Add Customised parameters
#     param = {'Name_1':'sreenivas', 'Name_2':'reddy', 'Name_3':'saddikuti'}
#     response = requests.get('https://httpbin.org/get',params=param)
#     print(response.text)

# def test_new_data():
#     response=crud().crudCall(r"D:\Users\ssreeenivasreddy\Altimetrik_JCL\pythonseleniumframework\testdata\apiList.xlsx",'testcase_data_10')
#     # print(response)
#     # print(response.content)
#     id = jsonpath.jsonpath(response.json(),"id")
#     print(id[0])

#     response=crud().crudCall(r"D:\Users\ssreeenivasreddy\Altimetrik_JCL\pythonseleniumframework\testdata\apiList.xlsx",'testcase_add_tech_11')
#     print(response.text)

#     response=crud().crudCall(r"D:\Users\ssreeenivasreddy\Altimetrik_JCL\pythonseleniumframework\testdata\apiList.xlsx",'testcase_address_12')
#     print(response.text)


#     response=crud().crudCall(r"D:\Users\ssreeenivasreddy\Altimetrik_JCL\pythonseleniumframework\testdata\apiList.xlsx",'testcase_final_13')
#     print(response.text)




