import Decoder
import Cryptographer
import sys
import os

cur_path = os.getcwd()
cur_path += "/src"
sys.path.insert(1, cur_path)

source = ""
cipher = ""
offset = 0
output = ""
decoder = False
skip_to = 0

# Parsing command line arguments
if __name__ == "__main__":
    for i in range(len(sys.argv)):
        if skip_to >= i:
            continue
        if sys.argv[i] == "--help":
            print('Write "man ./EncryptionSystem" to get manual about function')
        elif sys.argv[i] == "--source" or sys.argv[i] == "-s":
            source = sys.argv[i + 1]
            skip_to = i + 1
        elif sys.argv[i] == "--cipher" or sys.argv[i] == "-c":
            cipher = sys.argv[i + 1]
            skip_to = i + 1
        elif sys.argv[i] == "--output" or sys.argv[i] == "-o":
            output = sys.argv[i + 1]
            skip_to = i + 1
        elif sys.argv[i] == "--decoder" or sys.argv[i] == "-d":
            decoder = True
        else:
            print("Invalid argument. Write --help to get args list")

if source == "" or cipher == "" or output == "":
    print("Not enough arguments, please write --help to get args list")
    sys.exit()

# Rewrite output file?
rewrite_output_file = ""
print("Do you want to rewrite the output file?")
rewrite_output_file = str(input())
if rewrite_output_file == "y":
    f = open(output, "w")
    f.write("")
    f.close()
elif rewrite_output_file != "y" and rewrite_output_file != "n":
    print("Invalid argument. Aborting.")
    sys.exit()

# Crypting/Decoding input text
if decoder:
    if cipher == "Vernam":
        print("Insert the KeyPath, please")
        key_path = str(input())
        Decoder.DecoderVernamCipher(source, key_path, output)
    elif cipher == "Vigenere":
        print("Insert the KeyPath, please")
        key_path = str(input())
        Decoder.DecoderVigenereCipher(source, key_path, output)
    elif cipher == "Caesar":
        print("Do you have the OffsetKey? [y/n]")
        decoder_version = str(input())
        if decoder_version == "y":
            print("Then print it)))")
            offset = int(input())
            Decoder.DecoderCaesarCipherWithKey(source, offset, output)
        elif decoder_version == "n":
            Decoder.DecoderCaesarCipherWithoutKey(source, output)
        else:
            print("Invalid argument. Aborting")
            sys.exit()
else:
    if cipher == "Vernam":
        print("Insert KeyPath, please")
        key_path = str(input())
        f = open(key_path, "w")
        f.write("")
        f.close()
        with open(source) as inp:
            for string in inp:
                Cryptographer.VernamCipher(string, key_path, output)
    elif cipher == "Vigenere":
        print("Insert KeyPath, please")
        key_path = str(input())
        f = open(key_path, "w")
        f.write("")
        f.close()
        with open(source) as inp:
            for string in inp:
                Cryptographer.VigenereCipher(string, key_path, output)
    elif cipher == "Caesar":
        print("Input the offset, please")
        offset = int(input())
        with open(source) as inp:
            for string in inp:
                Cryptographer.CaesarCipher(string, offset, output)

print("Done!")
