import keyboard
import pyperclip
# from Crypto.Cipher import AES
# import base64
import requests

#Este codigo se debe ejecutar en la ruta origen del proyecto

URL = "https://bpw09cbtfjlswpeq1hd1fgnxcffpuds6hiy0m0.onrender.com"

API_KEY_TOKENS = [
    "TU_API_TOKEN_AQUI", "TU_API_TOKEN_AQUI", "TU_API_TOKEN_AQUI_SE_PUEDEN_AÑADIR_MAS"
    ]
# AES_KEY = b"TfaHj4p1Xmpr8awVxtraOkRb5QU0x0fL"
# AES_IV = b"RopcdIcUQzZ6GE4q" # No se pudo utilizar esto

session = ""

# def encrypt( raw ): # No se pudo utilizar esto
#     bs = AES.block_size
#     pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
#     raw =  pad(raw)
#     cipher = AES.new( AES_KEY, AES.MODE_CBC, AES_IV )
#     return base64.b64encode(cipher.encrypt( raw.encode("utf-8") ))

# def decrypt( enc ): # No se pudo utilizar esto
#     unpad = lambda s : s[:-ord(s[len(s)-1:])]
#     enc = base64.b64decode(enc)
#     cipher = AES.new(AES_KEY, AES.MODE_CBC, AES_IV)
#     return unpad(cipher.decrypt(enc)).decode('utf-8')

def clean_payload(): #Limpia el payload
    with open("payload", "w") as file:
        file.write("")
        file.close()

def add_payload():
    with open("payload", "a") as file:
        file.write(pyperclip.paste())
        file.close()

def get_payload():
    with open("payload", "r") as file:
        text = ""
        for line in file.readlines():
            text += line + "\n"
        file.close()
        
        return text

def write_payload():
    keyboard.write(get_payload())

def send_payload():
    requests.post(url= URL + "/users", json={
        "session": session,
        "payload": get_payload(),
        "response": "",
        "tokens": API_KEY_TOKENS,
        "active": True
    })

def add_user_server():
    global session
    session = requests.post(url= URL + "/adduser", json={
        "session": session
    }).text
    
def copy_response():
    pyperclip.copy( requests.get(url= URL + f"/getresponse?session={session}").text)

def capture_command():
    keyboard.add_hotkey("'+¿", callback=clean_payload)
    keyboard.add_hotkey("{+}", callback=add_payload)
    keyboard.add_hotkey("inicio+fin", callback=write_payload)
    keyboard.add_hotkey(".+-", callback=send_payload)
    keyboard.add_hotkey("-+l", callback=copy_response)
    add_user_server() # Generar un nuevo id al usuario
    
    while True:
        keyboard.read_key()

def main():
    print("start")

    capture_command()

if __name__=="__main__":
    main()