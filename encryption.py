from os import urandom
import string


def substitution(pt):
    assert len(pt) == 4
    for i in pt:
        assert i in string.hexdigits
    # Lookup Dictionary
    lookup_dict = {'0': 'e', '1': '4', '2': 'd', '3': '1', '4': '2', '5': 'f', '6': 'b', '7': '8', '8': '3', '9': 'a', 'a': '6', 'b': 'c', 'c': '5', 'd': '9', 'e': '0', 'f': '7'}
    # Replacement using Lookup Dictionary
    for i in range(len(pt)):
        pt = pt[:i] + lookup_dict[pt[i]] + pt[i+1:]
    return pt


def permutation(pt):
    assert len(pt) == 4
    for i in pt:
        assert i in string.hexdigits
    pt = bin(int(pt, 16))
    flag_list = []
    # Permutation Lookup
    plookup_dict = {0: 0, 1: 4, 2: 8, 3: 12, 4: 1, 5: 5, 6: 9, 7: 13, 8: 2, 9: 6, 10: 10, 11: 14, 12: 3, 13: 7, 14: 11, 15: 15}
    # Transposition of bit indices
    for i in range(len(pt)):
        if i not in flag_list:
            temp = pt[i]
            pt = pt[:i] + pt[plookup_dict[i]] + pt[i+1:]
            pt = pt[:plookup_dict[i]] + temp + pt[plookup_dict[i]+1:]
            flag_list.append(temp)
            flag_list.append(plookup_dict[i])
        else:
            continue
    return pt


def xor(pt):
    assert len(pt) == 4
    pt = pt.decode("hex")
    key = urandom(2)
    ct = ""
    for i in range(len(pt)):
        ct += chr(ord(key[i]) ^ ord(pt[i]))
    return ct.encode("hex")


def encrypt(plaintext):
    plaintext = plaintext.encode("hex")
    for i in range(0, len(plaintext), 4):
        for j in range(4):
            plaintext = xor(plaintext)
            plaintext = substitution(plaintext[i:i+4]) + plaintext[i+5:]
            plaintext = permutation(plaintext[i:i+4]) + plaintext[i+5:]
        plaintext = xor(plaintext)


if __name__ == '__main__':
    text = raw_input("Enter the text you want to encrypt: ")