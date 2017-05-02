#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.PublicKey import RSA
from Crypto import Random


def main():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)
    print(key)
    print(key.can_encrypt())
    print(key.has_private())
    print('*'*50)

    public_key = key.publickey()
    enc_data = key.encrypt('Whhhattt\'s Up Danielllll?', 32)

    print(enc_data)
    print('*'*50)

    print(key.decrypt(enc_data))


def use_specific_key():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)
    public_key = key.publickey().exportKey("PEM") 
    private_key = key.exportKey("PEM") 
    print('*'*50)
    print(public_key)
    print('*'*50)
    print(private_key)

    print('*'*50)

def generate_RSA(bits=2048):
    # Generate an RSA keypair with an exponent of 65537 in PEM format; @bits is length of key in bits; returns private and public keys 
    from Crypto.PublicKey import RSA 
    new_key = RSA.generate(bits, e=65537) 
    public_key = new_key.publickey().exportKey("PEM") 
    private_key = new_key.exportKey("PEM") 

    # return tuple (private_key, public_key)
    return private_key, public_key


if __name__ == "__main__":
    main()
    use_specific_key()
    print (generate_RSA())

