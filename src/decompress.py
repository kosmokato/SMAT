import shutil, os, magic
from zipfile import ZipFile


localpath = os.getcwd()
filepath = localpath + "/tmp/"

def zipfile(filename):
    print('[i] Compressed .zip file found')
    try:
        ZipFile(filename, 'r').extractall('./tmp')  # extracts the file into a temporal folder
    except:
        print("[!] There was a problem extracting the compressed file.")
        pswd = input("[?] May it has a password? (empty for \'infected\'):")
        if pswd is "": pswd = 'infected'
        ZipFile(filename, 'r').extractall(path=filepath, pwd = bytes(pswd, 'utf-8'))
    filename = compressedMenu()
    return [magic.from_file(filename, mime=True), filename]  # [filetype, filename]


def genericCompressedFile(filename):
    print('[i] Unknown file format. Trying to decompress...')
    try:
        shutil.unpack_archive(filename,filepath)

        filename = compressedMenu()
        return [magic.from_file(filename, mime=True), filename]  # [filetype, filename]

    except Exception as e:
        print("[-] There was an error: " + str(e) + "\nThe program will exit now.")
        exit()


def compressedMenu():
    if len(os.listdir(filepath)) == 0:
        print("[-] The compressed file is empty\n[i] The program will exit")
        exit()
    elif len(os.listdir(filepath)) < 2:
        print("[i] There was a file inside:")
        print("\t[x] " + os.listdir(filepath)[0])
        return filepath + os.listdir(filepath)[0]
    else:
        print("[i] There was several files inside: (" + str(len(os.listdir(filepath))) + ")")
        i = 0
        for compressed_file in os.listdir(filepath):
            print("\t[" + str(i) + "] " + compressed_file)
            i += 1
        filename = input("[?] Wich one do you want to analyze? > ")
        if filename == "": filename = os.listdir(filepath)[0]
        try:
            return filepath + os.listdir(filepath)[int(filename)]
        except:
            return filepath + filename