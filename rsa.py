"""
    RSA Algorithm 
        Implemented by Gavrilo Palalic
        Class: I-2
"""
import os ,io ,sys
from threading import * 
import random
import math

class RSA(object):
    def __init__(self):
        print("RSA object started.")
        
        
        arg = sys.argv[1]
        if(len(sys.argv) < 2 ):
            print("Specify a string.")
            sys.exit(1)
       

        if arg == "-e":
            pairs = self.createPair()
            pub = pairs[0]
            priv = pairs[1]

            string = sys.argv[2]
            en= self.encrypt(pub,string )
            encrypted = en[0]
            print("\r\n\t")
            print(encrypted)
            z = open("data.dat","wb")
            z.write(encrypted.encode())
            z.close()

            e = en[1]
            n = en[2]



            #create public key and save it to key.pub
            pubkey = self.createFile(e,n)
            print("\r\n\t")
            combi = "-----BEGIN RSA PUBLIC KEY-----\n"+pubkey+"\n-----END RSA PUBLIC KEY-----"
            print(combi)
            oz = open("key.pub","w")
            oz.write(combi)
            oz.close()

            res = self.decrypt(priv,encrypted)
            decrypted = res[0]
            d = res[1]
            pubkey = self.createFile(d,n)

            print("\r\n\t")
            print(decrypted)
            print("\r\n\t")
            combi = "-----BEGIN RSA PRIVATE KEY-----\n"+pubkey+"\n-----END RSA PRIVATE KEY-----"
            print(combi)
            oz = open("key.private","w")
            oz.write(combi)
            oz.close()

        if(arg =="-d"):
            keyfile = sys.argv[3]
            
            string1 = sys.argv[2]
            
            

            pair = self.reCreate(keyfile)
            res = self.decrypt(pair,string1)
            
            print("\n---- DECRYPTED ----\n")
            print(res[0])

        #create private key and save it to key.private

    def createFile(self,de,n):
        num1 = str(de)
        num2 = str(n)
        sofi=""
      
        jni1 = str(hex(int(num1)))
        sofi+=jni1

        sofi+=":"
        
        jni = str(hex(int(num2)))
        sofi+=jni



        return sofi 

    def reCreate(self,keyfile):
        z = open(keyfile,"r")
        data= z.read()
        d = 0
        n = 0
        slom = data.split("\n")
        cont = slom[1].split(":")
        d = int(cont[0],16)
        n = int(cont[1],16)
        

        

        arr=[d,n]
        
        return arr 

    def coprime(self,N):
        hcf =1 
        coprime=[]
        N = int(N)
        for j in range(2,N):
            
            for i in range(1,N+1):
                if(N%i==0 and j%i==0):
                    hcf = i
                
                
            if hcf == 1:
                if(j != 1 and j not in coprime):
                    
                    coprime.append(j)

        if(len(coprime) >0):
            return coprime

    def findPrime(self):
        x = 20
        y = 100
        prime=[]
        for n in range(x,y):
            iz=True
            for num in range(2,n):
                if n%num==0:
                    iz=False

            if iz:
                prime.append(n)
        return prime

        
    def findD(self,e,fn):
        d = 0
        k = 0 
        while True:
            res = 1+(k*fn) 
            fin =res/e
            if(fin > 0 and fin.is_integer()):

                d+=fin
                break

            k+=1
        return d


    def createPair(self):
        p1 = self.findPrime()
        p = p1[random.randint(0,len(p1))]
        q1 =self.findPrime() 
        q = q1[random.randint(0,len(q1))]
       
        N = p*q
        f_n = (p-1)*(q-1)
        
        
        e1=self.coprime(f_n)

        e=e1[random.randint(0,len(e1))]
        
       
        d1 =  self.findD(e,f_n)
       
        d = int(d1)
       
        #      PUBLIC  PRIVATE
        pair = [[e,N], [d,N]]
        return pair

    def encrypt(self,pair,string):
        brk = list(string)
        encr=[]
        for i in range(len(brk)):
            num = ord(brk[i])
            e = pair[0]
            n = pair[1]    
            powd= num**e%n 
            char = chr(powd)
            encr.append(char)
        
        finisharr = [self.arrToStr(encr),e,n]
        return finisharr


    def arrToStr(self,arr):
        str1=""
        for i in range(len(arr)):
            str1+=arr[i]

        return str1
    def decrypt(self,pair,str1):
        brk = list(str1)
        decr=[]
        for i in range(len(brk)):
            num = ord(brk[i])
            d = pair[0]
            n = pair[1]
            powd = (pow(num,d))%n
            cha = chr(powd)
            decr.append(cha)
            
            
        finisharr = [self.arrToStr(decr),d,n]
        return finisharr
      
        
    
app = RSA()