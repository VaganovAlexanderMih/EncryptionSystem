#Python encryption project.


##About

This [Encryption System](https://github.com/VaganovAlexanderMih/EncryptionSystem) can encrypt with the Caesar, Vigenere and Vernam ciphers,
as well as decrypt them, and the Caesar cipher can be decrypted both with the use of a key (offset)
and without it (using the method of frequency analysis)
When you use Vigenere and Vernam ciphers, the key is generating automatically
and randomly. You can find it in path that you left for the "key" option.


##Installation

1. To run, go to the command line and type 
2. "git clone --branch dev git@github.com:VaganovAlexanderMih/PythonProjects.git PythonProjects"
3. "cd PythonProjects"
4. "cd EncryptionSystem"
5. "pip install -r requirements.txt".
6. Then type "python3 main.py --help" to see all use cases.


###How to use the program:

- Write "--source" or "-s" to set source to the file that needed to be coded/decoded
- Write "--cipher" or "-c" to set cipher/decoder (Caesar to set the "Caesar cipher" then offset, Vernam to set "Vernam cipher", Vigenere to set "Viegenere cipher")
- Write "--output" or "-o" to set output file
- Write "--decode" or "-d" to decode file (write nothing if you want to code it)

![Printing help](src/images/printing_help.png)


##Examples of using

Let's see how to work with Vernam cipher:

Source file:
![Source](src/images/source.png)

Command sequence to launch the program:
![Vernam cipher command](src/images/vernam_cipher_command.png)

Key file:
![Key](src/images/key.png)

Output file:
![Output](src/images/output.png)
