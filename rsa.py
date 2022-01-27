"""
    RSA Algorithm 
        Implemented by Gavrilo Palalic
        Class: I-2
"""
import os ,io ,sys
from threading import * 
import random
import math
#find e , d , find f(fi) 
#p * q = N 
#find p and q 
#fi = (p - 1)*(q - 1)
#x^fi mod n  =1 
class RSA(object):
    def __init__(self):
        print("RSA object started.")
        #self.coprime(14,6)
        pairs = self.createPair()
        pub = pairs[0]
        priv = pairs[1]
        if(len(sys.argv) < 2 ):
            print("Specify a string.")
            sys.exit(1)
        string = sys.argv[1]
        
            

       
        en= self.encrypt(pub,string )
        self.decrypt(priv,en)
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
        

        num = random.randint(900000000,999999999999999999)
            
        maxPrime =-1
        while num%2==0:
            maxPrime=2
            num>>=1
        for i in range(3,int(math.sqrt(num))+1,2):
            while num%i==0:
                maxPrime=i
                num = num/i

        if(num>2):
            maxPrime=num


        return maxPrime
        
   
    def createPair(self):
        p = 47 #test num1
        q =61 #test num2
        N = p*q
        
        f_n = (p-1)*(q-1)
        #Choose E 
        #co_primes = self.coprime(N,f_n)
        #e = co_primes[0]
        e1=self.coprime(f_n)
        e = e1[0]
        #Choose d
        #Shit me ovo je tesko lol
        #part1 =e-(f_n-(p*e))
        #part2 = 1-(f_n-(p*1))%f_n
        d1 =  1183
        d = d1
       
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
        print("******************* ENCRYPTED ********************")
        print(f"Public pair: {e} : {n}")
        print("---------------------------------------------------")
        print(self.arrToStr(encr))
        return encr


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
            
            
        print("******************* DECRYPTED ********************")
        print(f"Private pair: {d} : {n}")
        print("---------------------------------------------------")
        print(self.arrToStr(decr))
        return decr
      
        
        


app = RSA()