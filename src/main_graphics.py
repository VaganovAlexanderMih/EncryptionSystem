import PySimpleGUI
import os
from enum import Enum
import Cryptographer
import Decoder


class Layouts(Enum):
  DEFAULT = 0
  CHOOSING_CIPHER = 1
  CAESAR = 2
  VERNAM = 3
  VIGENERE = 4
  COLUMNAR = 5
  IMAGE = 6
  FILE_CHOICE = 10
  KEY_CHOICE = 11


decoding = False
current_window = 0


def DefaultWindow():
  layout = [  # Default window ()
    [PySimpleGUI.Text("Do you want to encrypt text or decode?")],
    [PySimpleGUI.Button("Encrypt"), PySimpleGUI.Button("Decode")],
  ]
  decoding = False
  window = PySimpleGUI.Window("EncryptingSystem", layout)
  event, values = window.Read()  # type: ignore
  if event == PySimpleGUI.WIN_CLOSED:
    global current_window
    current_window = -1
    window.Close()
  if (event == "Decode"):
    decoding = True
  window.Close()
  return decoding


def ChoosingCipher(parent_windows):
  layout = [  # Choosing the way to encrypt / decode
    [PySimpleGUI.Text("Choose the method to cipher the text")],
    [PySimpleGUI.Button("Caesar"), PySimpleGUI.Button("Vernam"),
      PySimpleGUI.Button("Vigenere"), PySimpleGUI.Button("Columnar"),
      PySimpleGUI.Button("Image"),],
    [PySimpleGUI.Button("Back"), PySimpleGUI.Button("Exit")]
  ]
  current_window = 1
  window = PySimpleGUI.Window("EncryptingSystem", layout)
  event, values = window.Read()  # type: ignore
  if event == "Back":
    parent_windows.pop()
    current_window = parent_windows[-1]
    window.Close()
  if event == "Exit" or event == PySimpleGUI.WIN_CLOSED:
    window.Close()
    current_window = -1
  if event == "Caesar":
    current_window = Layouts.CAESAR.value
  if event == "Vernam":
    current_window = Layouts.VERNAM.value
  if event == "Vigenere":
    current_window = Layouts.VIGENERE.value
  if event == "Columnar":
    current_window = Layouts.COLUMNAR.value
  if event == "Image":
    current_window = Layouts.IMAGE.value
  window.Close()
  return current_window


def GettingFilePath(parent_windows, string):
  source = ""
  layout = [
    [
      PySimpleGUI.Text(string)
    ],
    [
      PySimpleGUI.Text("Source Folder"),
      PySimpleGUI.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
      PySimpleGUI.FolderBrowse(),
    ],
    [
      PySimpleGUI.Listbox(
          values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
      ), PySimpleGUI.Button("Back"), PySimpleGUI.Button("Exit")
    ],
  ]
  window = PySimpleGUI.Window("Choose the path to the file", layout)
  current_window = 10
  while True:
    event, values = window.Read()  # type: ignore
    if event == "-FOLDER-":
      folder = values["-FOLDER-"]
      file_list = os.listdir(folder)
      file_names = [
          f for f in file_list if os.path.isfile(os.path.join(folder, f))
          and f.lower().endswith((".txt", ".doc"))
      ]
      window["-FILE LIST-"].update(file_names)  # type: ignore
    if event == "-FILE LIST-":
      source = os.path.join(
          values["-FOLDER-"], values["-FILE LIST-"][0]
      )
      window.Close()
      break
    if event == "Back":
      current_window = parent_windows[-1]
      parent_windows.pop()
      window.Close()
      break
    if event == "Exit" or event == PySimpleGUI.WIN_CLOSED:
      current_window = -1
      window.Close()
      break
  return (source, current_window)


def GettingInput(parent_windows, string):
  layout = [
    [
      PySimpleGUI.Text(string)
    ],
    [
      PySimpleGUI.Input("", size=(25, 1), enable_events=True,
                        expand_x=True, key="-OFFSET-"),
    ],
    [
      PySimpleGUI.Button("Enter"), PySimpleGUI.Button("Back"),
      PySimpleGUI.Button("Exit")
    ]
  ]

  window = PySimpleGUI.Window("Encryption System", layout)
  offset = 0
  current_window = 11
  while True:
    event, values = window.Read()  # type: ignore
    if event == "-OFFSET-":
      offset = values["-OFFSET-"]
      window["-OFFSET-"].update(offset)
    if event == "Enter":
      offset = values["-OFFSET-"]
      window.Close()
      break
    if event == "Back":
      current_window = parent_windows[-1]
      parent_windows.pop()
      window.Close()
      break
    if event == "Exit":
      current_window = -1
      window.Close()
      break
  return (offset, current_window)


def RewriteOutputFile(output):
  layout = [
    [
      PySimpleGUI.Text("Do you want to rewrite the output file?")
    ],
    [
      PySimpleGUI.Button("No"), PySimpleGUI.Button("Yes")
    ]
  ]

  window = PySimpleGUI.Window(
    "Do you want to rewrite the output file?", layout)
  event, values = window.Read()  # type: ignore

  if event == "Yes":
    f = open(output, "w")
    f.write("")
    f.close()
  window.Close()


parent_windows = []
source = ""
offset = 0
output = ""
key = ""


def GettingImage(parent_windows):
  source = ""
  layout = [
    [
      PySimpleGUI.Text("Choose the image, please")
    ],
    [
      PySimpleGUI.Text("Source Folder"),
      PySimpleGUI.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
      PySimpleGUI.FolderBrowse(),
    ],
    [
      PySimpleGUI.Listbox(
          values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
      ), PySimpleGUI.Button("Back"), PySimpleGUI.Button("Exit")
    ],
  ]
  window = PySimpleGUI.Window("Encryption System", layout)
  current_window = 10
  while True:
    event, values = window.Read()  # type: ignore
    if event == "-FOLDER-":
      folder = values["-FOLDER-"]
      file_list = os.listdir(folder)
      file_names = [
        f for f in file_list if os.path.isfile(os.path.join(folder, f))
        and f.lower().endswith(("png", "jpg", "bmp"))
      ]
      window["-FILE LIST-"].update(file_names)  # type: ignore
    if event == "-FILE LIST-":
      source = os.path.join(
        values["-FOLDER-"], values["-FILE LIST-"][0]
      )
      window.Close()
      break
    if event == "Back":
      current_window = parent_windows[-1]
      parent_windows.pop()
      window.Close()
      break
    if event == "Exit" or event == PySimpleGUI.WIN_CLOSED:
      current_window = -1
      window.Close()
      break
  return (source, current_window)


def SimilarCiphers(version):
  source = ""
  key = ""
  current_window = 10
  while (current_window >= 10):
    if current_window == 10:
      source = ""
      while source == "" and current_window == 10:
        if (version == Layouts.IMAGE.value):
          source, current_window = GettingImage(parent_windows)
        else:
          string_source = "Choose the source file, please"
          source, current_window = GettingFilePath(
              parent_windows, string_source)
      if current_window == 10:
        if (not (current_window in parent_windows)):
            parent_windows.append(current_window)
        current_window = 11
    if current_window == 11:
      if (version == Layouts.IMAGE.value and decoding == True):
        current_window = 12
      else:
        key = ""
        string_key = ""
        if (version == Layouts.IMAGE.value):
          string_key = "Choose the file to be encrypted, please"
        else:
          string_key = "Choose the key for encryption, please"
        while key == "":
          key, current_window = GettingFilePath(
              parent_windows, string_key)
          if current_window != 10:
              break
        if current_window == 10:
          if (not (Layouts.KEY_CHOICE.value in parent_windows)):
              parent_windows.append(Layouts.KEY_CHOICE.value)
          current_window = 12
    if current_window == 12:
      output = ""
      string_output = ""
      while output == "":
        if (version == Layouts.IMAGE.value and decoding == False):
          string_output = "Write the path to the output file(with ext)"
          output, current_window = GettingInput(
            parent_windows, string_output)
        else:
          string_output = "Choose the output file, please"
          output, current_window = GettingFilePath(
            parent_windows, string_output)
      if current_window != 10:
        if (current_window != 11):
          break
      RewriteOutputFile(output)
      if (decoding == False):
        if (version == Layouts.IMAGE.value):
          Cryptographer.ImageCiphers(source, key, output)
        else:
          with open(source) as inp:
            for string in inp:
              if (version == Layouts.VERNAM.value):
                Cryptographer.VernamCipher(string, key, output)
              elif (version == Layouts.VIGENERE.value):
                Cryptographer.VigenereCipher(string, key, output)
              elif (version == Layouts.COLUMNAR.value):
                Cryptographer.ColumnarCipher(string, key, output)
      else:
        if (version == Layouts.IMAGE.value):
          Decoder.DecoderImage(source, output)
        else:
          with open(source) as inp:
            for string in inp:
              if (version == Layouts.VERNAM.value):
                Decoder.DecoderVernamCipher(string, key, output)
              elif (version == Layouts.VIGENERE.value):
                Decoder.DecoderVigenereCipher(string, key, output)
              elif (version == Layouts.COLUMNAR.value):
                Decoder.DecoderColumnarCipher(string, key, output)
      current_window = -1
      break
  return current_window


def CaesarCipher():
  current_window = 10
  source = ""
  offset = 0
  while (current_window >= 10):
    if current_window == 10:
        source = ""
        string_source = "Choose the file to be encrypted"
        while source == "" and current_window == 10:
            source, current_window = GettingFilePath(
                parent_windows, string_source)
        if current_window == 10:
            if (not (current_window in parent_windows)):
                parent_windows.append(current_window)
            current_window = 11
    if current_window == 11:
        offset = 0
        if (not(decoding)):
          string_offset = "Write the offset, please"
        else:
          string_offset = "Do you have the offset? (If no - set 200)"
        offset, current_window = GettingInput(
            parent_windows, string_offset)
        if offset == "":
            offset = 0
        if current_window == 11:
            parent_windows.append(current_window)
            current_window = 12
    if current_window == 12:
        output = ""
        string_output = "Choose the output file, please"
        while output == "":
            output, current_window = GettingFilePath(
                parent_windows, string_output)
            if current_window != 10:
                break
        if (current_window != 10):
            break
        RewriteOutputFile(output)
        offset = int(offset)
        if (not(decoding)):
          with open(source) as inp:
              for string in inp:
                  Cryptographer.CaesarCipher(
                      string, int(offset), output)
        else:
          if (offset == 200):
            Decoder.DecoderCaesarCipherWithoutKey(source, output)
          else:
            Decoder.DecoderCaesarCipherWithKey(source, offset, output)
        current_window = -1
        break
  return current_window


while True:
  if (not (Layouts.DEFAULT.value in parent_windows)):
    parent_windows.append(Layouts.DEFAULT.value)
  if current_window == -1:
    break
  if current_window == 0:
    decoding = DefaultWindow()
    if current_window != -1:
      current_window = Layouts.CHOOSING_CIPHER.value
  if current_window == 1:
    parent_windows.append(current_window)
    current_window = ChoosingCipher(parent_windows)
  if decoding == False:
    if current_window == 2:
      current_window = CaesarCipher()
    if current_window == 3:
      current_window = SimilarCiphers(Layouts.VERNAM.value)
    if current_window == 4:
      current_window = SimilarCiphers(Layouts.VIGENERE.value)
    if current_window == 5:
      current_window = SimilarCiphers(Layouts.COLUMNAR.value)
    if current_window == 6:
      current_window = SimilarCiphers(Layouts.IMAGE.value)

  if decoding == True:
    if current_window == 2:
      current_window = CaesarCipher()
    if current_window == 3:
      current_window = SimilarCiphers(Layouts.VERNAM.value)
    if current_window == 4:
      current_window = SimilarCiphers(Layouts.VIGENERE.value)
    if current_window == 5:
      current_window = SimilarCiphers(Layouts.COLUMNAR.value)
    if current_window == 6:
      current_window = SimilarCiphers(Layouts.IMAGE.value)

layout_final = [
    [
        PySimpleGUI.Text("Done!")
    ],
    [
        PySimpleGUI.Button("Exit")
    ]
]

window = PySimpleGUI.Window("Encrypter System", layout_final)

event, values = window.Read()  # type: ignore

if event == "Exit" or event == PySimpleGUI.WIN_CLOSED:
    window.Close()
