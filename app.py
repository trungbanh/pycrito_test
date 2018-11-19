from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto import Random
import copy
import ast
from Crypto.Cipher import DES, AES

import tkinter as tk 

class Application (tk.Frame) :
    def __init__(self,master=None) :
        super().__init__(master)
        self.master=master
        self.pack()
        self.create_widgets()
        self.KeyDes = '12345678'
        self.KeyAes = '0123456789123456'
        self.encodeWith = 0
        self.RSA_key()
        self.des = DES.new(self.KeyDes, DES.MODE_ECB)
        self.aes = AES.new(self.KeyAes, AES.MODE_ECB)
    def create_widgets(self):
        self.lb_1 = tk.Label(self,text='input =>')
        self.lb_1.grid(row=0, column=0)

        self.lb_2 = tk.Label(self,text='output =>')
        self.lb_2.grid(row=1, column=0)

        self.lb_3 = tk.Label(self,text='decode =>')
        self.lb_3.grid(row=2, column=0)

        self.et_in = tk.Entry(self,width=20)
        self.et_in.grid(row=0,column=1)

        self.et_out = tk.Entry(self,width=20)
        self.et_out.grid(row=1,column=1)

        self.et_decode = tk.Entry(self,width=20)
        self.et_decode.grid(row=2,column=1)

        self.et_hash = tk.Entry(self,width=55)
        self.et_hash.grid(row=3,column=0,columnspan=5,rowspan=3)

        self.bt_Des = tk.Button(self, width=10, text="DES",command=self.Des)
        self.bt_Aes = tk.Button(self, width=10, text="AES",command=self.Aes)
        self.bt_Rsa = tk.Button(self, width=10, text="RSA",command=self.Rsa)

        
        self.bt_Des.grid(row=0,column=3)
        self.bt_Aes.grid(row=0,column=4)
        self.bt_Rsa.grid(row=0,column=5)

        self.bt_giaima = tk.Button(self,text='__Decode__',command=self.Decode)
        self.bt_giaima.grid(row=1,column=3,columnspan=3)

        self.bt_Hash = tk.Button(self, width=10, text="hash",command=self.Hash)
        self.bt_Hash.grid(row=3, column=5)
        

    def Des(self) :
        self.code = self.des.encrypt(self.et_in.get())
        cipher_text = copy.copy(self.code)
        self.et_out.delete(0)
        self.et_out.insert(0,str(cipher_text))  
        self.encodeWith=1
    def Aes(self) :
        
        self.code = self.aes.encrypt(self.et_in.get())
        cipher_text = copy.copy(self.code)
        self.et_out.delete(0)
        self.et_out.insert(0,str(cipher_text))
        self.encodeWith=2
    def Rsa(self) :
        encrypted = self.rsa.publickey().encrypt(str(self.et_in.get()).encode('utf-8'),int(32))
        self.code = copy.copy(encrypted)
        self.et_out.delete(0)
        self.et_out.insert(0, str(encrypted))
        self.encodeWith = 3
    def Decode(self) :
        if self.encodeWith ==1 :
            giaima = self.des.decrypt(self.code)
            self.et_decode.delete(0)
            self.et_decode.insert(0,str(giaima))
        if self.encodeWith ==2 :
            giaima = self.aes.decrypt(self.code)
            self.et_decode.delete(0)
            self.et_decode.insert(0,str(giaima))
        if self.encodeWith ==3 :
            encrypted = copy.copy(self.code)
            decrypted = self.rsa.decrypt(encrypted)
            self.et_decode.delete(0)
            self.et_decode.insert(0, str(decrypted))

    def RSA_key(self):
        random_generator = Random.new().read
        self.rsa = RSA.generate(1024, random_generator)
        key = copy.copy(self.rsa)
        # print(type(key))
        #public key
        self.Plkey=key.publickey().exportKey()
        #private key
        self.Prkey=key.exportKey()
    def Hash (self):
        h = SHA256.new()
        h.update(self.et_in.get().encode('utf-8'))
        self.et_hash.insert(0,str(h.hexdigest()))
        

root = tk.Tk()
app = Application(master=root)
app.mainloop()
