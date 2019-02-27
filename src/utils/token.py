import jwt
from datetime import datetime, timedelta


def encode(data):
    payload = {
        "data": data,
        "exp": datetime.utcnow() + timedelta(seconds=3),
        "iat": datetime.utcnow()
    }

    encoded = jwt.encode(payload, "kucing-merah", algorithm="HS256").decode('utf-8')
    return encoded


def decode():
    decoded = jwt.decode(data, "kucing-merah", algorithms=["HS256"])
    return decoded