from Crypto.Cipher import AES
from base64 import b64decode as de

key = "pctf2016pctf2016pctf2016pctf2016"
cipher = "x/nzolo0TTIyrEISd4AP1spCzlhSWJXeNbY81SjPgmk="

aes = AES.new(key, AES.MODE_ECB)
print(aes.decrypt(de(cipher)))

# PCTF{Dot_Net_UnPack3r_yoo}