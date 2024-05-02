import requests
# endpoint="http://httpbin.org/status/200/"
# endpoint="http://www.httpbin.org/anything"
endpoint="http://localhost:800/"  #http://127.0.0.1:8000/


get_response= requests.get(endpoint,query={"json":"Hello World"})  # http request
print(get_response.text)  # print row response text code
print(get_response.status_code)

# http request--> html
# Rest Api http request --> json
# javascript object nototion -->python dict
# print(get_response.json())
# print(get_response.status_code)
