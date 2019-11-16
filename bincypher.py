#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from sys import argv as sys_argv
from re import findall as re_findall


def encrypt(data):
    def utf8_byte(symb_ord):
        symb_binary = str(bin(symb_ord))[2:]
        while len(symb_binary) % 8 != 0:
            symb_binary = '0' + symb_binary
        return symb_binary
    data = data.split('  ')
    data = [[x for x in dat.encode('utf-8')] for dat in data]
    encrypt = [''.join([utf8_byte(x) for x in dat]) for dat in data]
    return encrypt


def decrypt(data):
    def check_bin(binstr):
        p = set(binstr)
        s = {'0', '1'}
        return s == p or p == {'0'} or p == {'1'}
    data = data.split()
    for i in data:
        if not check_bin(i):
            print('Error: Given cypher contained not binary number')
            exit()
    words_data = [[int(x, 2) for x in re_findall(r'.{8}', i)] for i in data]
    decrypts = [bytearray(i).decode('utf-8') for i in words_data]
    return decrypts


if len(sys_argv) == 2 and sys_argv[1] in ['-e', '-d', '--encrypt', '--decrypt']:
    if sys_argv[1].lower() in ['-e', '--encrypt']:
        data = input("Input message here: ")
        print(' '.join(encrypt(data)))
    else:
        data = input("Input binary encoded message here: ")
        print('\n'.join(decrypt(data)))
elif len(sys_argv) == 3 and sys_argv[1] in ['-e', '-d', '--encrypt', '--decrypt'] and sys_argv[2] in ['-H', '--hex']:
    if sys_argv[1] in ['-e', '--encrypt']:
        data = input("Input message here to get in hex: ")
        print(' '.join([hex(int(i, 2)) for i in encrypt(data)]))
    else:
        data = [int(x, 16) for x in input("Input here hex encoded message: ").split()]
        data = [bin(x)[2:] for x in data]
        print('\n'.join(decrypt(' '.join(data))))

else:
    print("Usage: bin_cypher.py [-d --decrypt | -e --encrypt] [-H --hex] [-h --help]")
    print("Notice: If you want to encrypt line break add double space instead of ENTER -> '  '", end="\n\n")
    print("Options:")
    print("-d, --decrypt\tDecode mode")
    print("-e, --encrypt\tEncode mode")
    print("-H, --hex\tClarifying that output will be in hex")
