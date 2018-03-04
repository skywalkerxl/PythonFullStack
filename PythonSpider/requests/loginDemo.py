import requests

form_data = {
    'option': 'CheckLogin',
    'USER': 'hhu005',
    'PSW': 'hhu005'
}

for i in range(10):
    response = requests.post(
        url='http://112.26.45.226:8000/login',
        data=form_data
    )
    print(response.text)
    print("第%s次请求"%(i+1))
