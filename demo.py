import requests
get_token = requests.post('https://ipam.sic.net/api/snsg/user/',
                          auth=('py_api', 'TZ@T&Nq6Ar73'), verify=False).json()
print(get_token)
a = 1
b = 2
print(a+b)
c=a+b
