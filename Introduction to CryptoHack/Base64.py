import base64

data = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
data = bytes.fromhex(data)
data = base64.b64encode(data)

print(data)
