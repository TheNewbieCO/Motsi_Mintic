import jwt, time
def func():
    secret = '123456' #pasar a variables de entorno
    time_unit = int(time.time())

    token = jwt.encode(
        {'id':'1', 'nombre':'gianpier', 'time':time_unit},
        secret,
        algorithm='HS256'        
    )
    return token    
print(func())