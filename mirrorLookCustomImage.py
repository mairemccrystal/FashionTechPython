########## Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
'Ocp-Apim-Subscription-Key': 'ba10a036532d4c438ded719c0f797a4e',
'Content-Type': 'multipart/form-data',
#'Content-Type': 'application/json',
'Ocp-Apim-Subscription-Key': 'ba10a036532d4c438ded719c0f797a4e',
}

#file =open('C:/Users/User/Desktop/python component/data/test.jpeg'),
#file = 'http://localhost:4555/image'

params = urllib.parse.urlencode({

#'image': open('C:/Users/User/Desktop/python component/data/test.jpeg'),
#'image': '/data/test.jpeg'
#'type:' : 'file',
#'image': 'http://localhost:4555/image',
#'type': 'file',
#'description' : 'http://localhost:4555/image'
#'upload_image' : open('file:///C:/Users/User/Desktop/python%20component/data/test.jpeg')
})

conn = http.client.HTTPSConnection('api.mirrorthatlook.com')


#conn.request("POST", "/v2/upload_image?%s" % params, "{body}", headers)


conn.request("POST", "/v2/upload_image?%s'http://localhost:4555/image'", "{body}", headers)
#something about this kind of works idk ^^

#conn.request("POST", "/v2/upload_image?%s'http://localhost:4555/image'", params, "{body}", headers)
# get a diff error

#conn.request("POST", "/v2/upload_image?%s" % params, "{body}", headers)
# get a diff error
print(conn.request)

response = conn.getresponse()
data = response.read()
print(data)
conn.close()


####################################