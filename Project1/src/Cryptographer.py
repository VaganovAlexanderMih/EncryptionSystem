import random
import string

special_symbols = {255: ".", 200: " ", 210: ",", 240: ":", 260: "!", 230: "?", 300: "-",
                   320: "(", 340: ")", 360: "0", 361: "1", 362: "2", 363: "3", 364: "4", 365: "5", 366: "6", 367: "7", 368: "8", 369: "9"}


def VernamCipher(string_, key_path):
    # helpers
    def xor_char(char1_bin, char2_bin):
        final_str = ""
        final_arr = []
        first_arr = []
        second_arr = []
        for i in char1_bin:
            first_arr.append(i)
        for i in char2_bin:
            second_arr.append(i)
        first_arr.reverse()
        second_arr.reverse()
        for i in range(min(len(char1_bin), len(char2_bin))):
            final_arr.append((int(first_arr[i]) + int(second_arr[i])) % 2)
        final_arr.reverse()
        for i in final_arr:
            final_str += str(i)
        return final_str

    # if first bits are nulls - delete
    def DeleteFirstNulls(cur_string):
        while cur_string[0] == "0" and not (int(cur_string) == 0):
            cur_string = cur_string[1:]
        return cur_string

    # getting random key
    result_key = ""
    for i in range(len(string_)):
        letter = random.choice(string.ascii_letters)
        while (
            DeleteFirstNulls(xor_char(bin(ord(string_[i]))[
                             2:], bin(ord(letter))[2:]))
            == "1011100"
            or DeleteFirstNulls(
                xor_char(bin(ord(string_[i]))[2:], bin(ord(letter))[2:])
            )
            == "1010"
            or DeleteFirstNulls(
                xor_char(bin(ord(string_[i]))[2:], bin(ord(letter))[2:])
            )
            == "1101"
        ):
            letter = random.choice(string.ascii_letters)
        result_key += letter
    key = open(key_path, "a+")
    key.write(result_key)
    key.write("\n")
    key.close()

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
        xored_char = xor_char(cur_char_bin, bin(ord(result_key[i]))[2:])
        final_string += chr(int(xored_char, 2))
    # writing the line to output file
    crypted = open("Crypted_Text.txt", "a+")
    crypted.write(final_string)
    crypted.write("\n")
    crypted.close()


def CaesarCipher(string_, offset):
    final_string = ""
    for letter in string_:
        # if the symbol is in syntactic signs, then we set a fixed value
        if (letter in special_symbols.values()):
            final_string += chr(ord(letter) + offset)
            continue

        # else we set chars with offset
        if (letter.lower() == letter):
            letter_ind = ord(letter) - ord('a')
            letter_ind += offset
            letter_ind %= (ord('z') - ord('a'))
            letter_ind += ord('a')
        else:
            letter_ind = ord(letter) - ord('A')
            letter_ind += offset
            letter_ind %= (ord('Z') - ord('A'))
            letter_ind += ord('A')
        final_string += chr(letter_ind)
    # writing the line to output file
    crypted = open("Crypted_Text.txt", "a+")
    crypted.write(final_string)
    crypted.write('\n')
    crypted.close()


def VigenereCipher(string_, key_path):

    # getting random key
    result_key = ""
    key = open("key.txt", "w")
    key.write('')
    key.close()
    for i in range(len(string_)):
        letter = random.choice(string.ascii_letters)
        result_key += letter
    key = open(key_path, "a+")
    key.write(result_key)
    key.write("\n")
    key.close()

    # cipher
    final_string = ""
    for i in range(len(string_)):
        # if the symbol is in syntactic signs, then we set a fixed value
        if (string_[i] in special_symbols):
            final_string += chr(special_symbols[string_[i]])
            continue

        # else we using cipher algorithm on it
        if (string_[i].lower() == string_[i]):
            letter_ind = ord(string_[i]) - ord('a')
            letter_ind += (ord(result_key[i]) - ord('a'))
            letter_ind %= (ord('z') - ord('a'))
            letter_ind += ord('a')
        else:
            letter_ind = ord(string_[i]) - ord('A')
            letter_ind += (ord(result_key[i]) - ord('A'))
            letter_ind %= (ord('Z') - ord('A'))
            letter_ind += ord('A')
        final_string += chr(letter_ind)
    # writing the line in output file
    crypted = open("Crypted_Text.txt", "a+")
    crypted.write(final_string)
    crypted.write('\n')
    crypted.close()