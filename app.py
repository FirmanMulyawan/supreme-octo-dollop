from flask import Flask, request, jsonify
import jwt
from src.routes import router


app = Flask(__name__)
app.register_blueprint(router)

# @app.errorhandler(404)
#     def errorhandler404(e):

@app.route('/jwt/encode')
def jwtEncode():
    encoded = jwt.encode({"data": "makers"}, "kucing-merah", algorithm="HS256")
    return encoded

@app.route('/jwt/decode', methods=["POST"])
def jwtDecode():
    decoded = jwt.decode(request.json["token"], "kucing-merah", algorithms=["HS256"])
    return str(decoded)

@app.route('/penjumlahan/<firstNumber>/<secondNumber>')
def penjumlahan(firstName, secondName):
    return jsonify({
        "hasil_jumlah": firstName+secondName,
        "mancing_mania": "mantap"
    })


if __name__ == "__main__":
    app.run(debug=True, port=1989)