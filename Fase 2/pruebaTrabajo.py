from hashlib import sha256

data = "informacion"
cadenaEvaluada = ""
nonce = 0
prefijo = "0000"

while True:
    nonce = nonce + 1
    cadenaEvaluada = data + "" + str(nonce)
    if str(sha256(cadenaEvaluada.encode('utf-8')).hexdigest().find(prefijo)) == 0:
        break
