import rumps
import pyperclip


x = 300
letters = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890,.' ="
char_set_2 = "≤≥O¸IO∏±—·°¨A„EO~`!@#$oiuytrewqMNBVUYTR√^&≈Ω-=πCXZLKJHGFDSAPOI{«*;:? xzlkjhgfdsapEW'.,0987654321mnbvcQ"

shift = ""
for i in range(x + 1):
    for w in range(i + 1):
        shift += str(w * i)


def encrypt(code_to_encrypt):
    encrypted_array = []
    for letter in range(len(code_to_encrypt)):
        encrypted_array.append(letters.find(code_to_encrypt[letter]) + int(shift[letter]))

    encrypted_code = ""
    for encrypted_number in encrypted_array:
        encrypted_code += char_set_2[encrypted_number]

    return encrypted_code


def decrypt(code_to_decrypt):
    decrypted_array = []
    for dletter in code_to_decrypt:
        decrypted_array.append(char_set_2.find(dletter))

    decrypted_code = ""
    for number in range(len(decrypted_array)):
        decrypted_code += letters[(int(decrypted_array[number])) - int(shift[number])]
    return decrypted_code


# APP FUNCTIONALITY
class App(rumps.App):
    def __init__(self):
        super(App, self).__init__("ClipEncrypt")
        self.menu = ["Encrypt", "Decrypt"]

    @rumps.clicked("Encrypt")
    def app_encrypt(self, sender):
        user_input = pyperclip.paste()
        encrypted_code = encrypt(user_input)
        pyperclip.copy(encrypted_code)
        rumps.alert("Encrypted text copied to clipboard")

    @rumps.clicked("Decrypt")
    def app_decrypt(self, sender):
        user_input_d = pyperclip.paste()
        decrypted_code = decrypt(user_input_d)
        pyperclip.copy(decrypted_code)
        rumps.alert("Decrypted text copied to clipboard")


if __name__ == '__main__':
    App().run()
