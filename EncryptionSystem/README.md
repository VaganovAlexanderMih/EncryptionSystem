Python encryption project.

'''
To run, go to the command line and type 
"git clone --branch dev git@github.com:VaganovAlexanderMih/PythonProjects.git PythonProjects"
"cd PythonProjects"
"cd EncryptionSystem"
"pip install -r requirements.txt".
Then type "python3 main.py --help" to see all use cases.
'''

There is an example what last command should print:
Write "--source" or "-s" to set source to the file that needed to be coded/decoded
Write "--cipher" or "-c" to set cipher/decoder (Caesar to set the "Caesar cipher" then offset (0 is default value), Vernam to set "Vernam cipher", Vigenere to set "Viegenere cipher")
Write "--output" or "-o" to set output file
Write "--decode" or "-d" to decode file (write nothing if you want to code it)

This encryption system can encrypt with the Caesar, Vigenere and Vernam ciphers,
as well as decrypt them, and the Caesar cipher can be decrypted both with the use of a key (offset)
and without it (using the method of frequency analysis)
When you use Vigenere and Vernam ciphers, the key is generating automatically
and randomly. You can find it in path that you left for the "key" option.

