import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import pyAesCrypt
import base64
pss = "hey"

buffersize = 64*1024
message = input("enter your message: ")
message_h = message.encode('ascii')
base64_bytes = base64.b64encode(message_h)
base64_message = base64_bytes.decode('ascii')

password =  base64_message
path = "C:\\Users\Shivam Upadhyay\Desktop\hellp.txt"


class mygrid(GridLayout):
    def __init__(self,**kwargs):
        super(mygrid, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text = "your key is: "))
        self.add_widget(Label(text = password))



        self.encrypt = Button(text = "encrypt", font_size = 30)
        self.add_widget(self.encrypt)
        self.encrypt.bind(on_press = self.enc )
        self.decrypt = Button(text = "decrypt", font_size = 30)
        self.add_widget(self.decrypt)
        self.decrypt.bind(on_press = self.dec )
    def enc(self,event):
        return pyAesCrypt.encryptFile(path,"C:\\Users\Shivam Upadhyay\Desktop\hellp.txt.aes",password,buffersize)
    def dec(self, event):
        return pyAesCrypt.decryptFile("C:\\Users\Shivam Upadhyay\Desktop\hellp.txt.aes","C:\\Users\Shivam Upadhyay\Desktop\h.txt",password,buffersize)

class myapp(App):
    def build(self):
        return mygrid()

if __name__ == "__main__":
    myapp().run()
