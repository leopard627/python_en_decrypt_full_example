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
    pass


if __name__ == "__main__":
    main()
