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

    print('+'*50)
    quotes = "hack me up"
    print('quotes --> {}'.format(quotes))
    encrypted_quotes = new_key.encrypt(quotes, 32)
    print('after encrypt --> {}'.format(encrypted_quotes))
    print('+'*50)

    # return tuple (private_key, public_key)
    return private_key, public_key, encrypted_quotes

def todo_rsa_example():
    # let's get_RSA key_pairs
    key_pairs = generate_RSA()
    # [0]  private_key
    # [1]  public_key
    # [2]  encryped_quotes 

    # use private_key 
    rsakey = RSA.importKey(key_pairs[0])

    # export it again LOL
    print(rsakey.exportKey('PEM'))

    print('+'*50)
    print('before decrypt --> {}'.format(key_pairs[2]))
    print('after decrypt --> {}'.format(rsakey.decrypt(key_pairs[2])))
    print('+'*50)

if __name__ == "__main__":
    main()
    use_specific_key()
    todo_rsa_example()
