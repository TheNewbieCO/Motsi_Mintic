import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'Motsi-Mintic-Backend-Airbnb2008'

def create_access_token(user,days=3):

    data={
        "user_id":user.id_user,
        "username":user.email,
        "exp":datetime.utcnow() + timedelta(days=days)
    }
    return jwt.encode(data, SECRET_KEY, algorithm="HS256")