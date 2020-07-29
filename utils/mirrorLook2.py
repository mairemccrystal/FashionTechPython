########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json2

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'ba10a036532d4c438ded719c0f797a4e',
    'Ocp-Apim-Subscription-Key': 'ba10a036532d4c438ded719c0f797a4e',
}

params = urllib.parse.urlencode({
    # Request parameters
    'image': 'https://contestimg.wish.com/api/webimage/5c394bfbe3e6604287a573da-large.jpg?cache_buster=276746c000af54b686498893ade2baea',
    # 'gender': '{string}',
    'limit': '1',
})

conn = http.client.HTTPSConnection('api.mirrorthatlook.com')
conn.request("GET", "/v2/mirrorthatlook?%s" % params, "{body}", headers)
response = conn.getresponse()
data = response.read()
    # print(data)

my_json = data.decode('utf8')
python_obj = json2.loads(my_json)


#data = json.loads('{"lat":444, "lon":555}')
#data = json.dumps(my_json)
#wut = data['status']
#print(wut)

print(type(my_json))
print(type(python_obj))

print(my_json)
loaded_json = json2.dumps(my_json)
loaded_json = json2.loads(my_json)
new_json = (loaded_json["result"])


print(type(new_json))
#new_json = str(new_json).strip('[]')
print(new_json)
print(type(new_json))







#print(python_obj.items())
#for i in python_obj:
 #   print(i, python_obj[i])
#for key,value in python_obj.items():
#    print(key + " => " + value)

conn.close()