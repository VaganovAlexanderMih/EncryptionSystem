import random
import string
import helpers

special_symbols = {255: ".", 200: " ", 210: ",", 240: ":", 260: "!", 230: "?", 300: "-",
                   320: "(", 340: ")", 360: "0", 361: "1", 362: "2", 363: "3", 364: "4", 365: "5", 366: "6", 367: "7", 368: "8", 369: "9"}


def VernamCipher(string_, key_path, output):
    # if first bits are nulls - delete
    helpers.delete_first_nulls()

    # getting random key
    result_key = helpers.getting_random_key(string_, key_path)

    # formatting string
    final_string = ""
    if string_.endswith("\n"):
        string_ = string_[:-1]
    for i in range(len(string_)):
        # if the symbol is in syntactic signs, then we set a fixed value
        if string_[i] in special_symbols.keys():
            final_string += chr(special_symbols[string_[i]])
            continue
        # else xoring symbol's bits with key's bits
        cur_char_bin = bin(ord(string_[i]))[2:]
        xored_char = helpers.xor_char(cur_char_bin, bin(ord(result_key[i]))[2:])
        final_string += chr(int(xored_char, 2))
    # writing the line to output file
    crypted = open(output, "a+")
    crypted.write(final_string)
    crypted.write("\n")
    crypted.close()


def CaesarCipher(string_, offset, output):
    final_string = helpers.caesar_cipher_coder(special_symbols, string_, offset)
    # writing the line to output file
    crypted = open(output, "a+")
    crypted.write(final_string)
    crypted.write('\n')
    crypted.close()


def VigenereCipher(string_, key_path, output):

    # getting random key
    result_key = helpers.getting_random_key(string_, key_path)

    # cipher
    final_string = helpers.vigenere_cipher_coder(special_symbols, string_, result_key)
    # writing the line in output file
    crypted = open(output, "a+")
    crypted.write(final_string)
    crypted.write('\n')
    crypted.close()