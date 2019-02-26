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
    decoded = jwt.decode(eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRhIjoibWFrZXJzIn0.a6VqF1oQpUOZjU5U7diD9FvcStirR2A08STBsTBNvcY, "kucing-merah", algorithms=["HS256"])
    return str(decoded)