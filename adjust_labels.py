import os
from tempfile import mkstemp
from shutil import move, copymode


def replace(file_path):
    """
    Ta funkcja podmienia klase obiektu na '1' w kazdej linijce
    danego pliku tekstowego, zawierajacego etykiety dla pewnego zdjecia.
    Parametrem jest sciezka do pliku tekstowego.
    """
    fh, abs_path = mkstemp()  # tworzy tymczasowy plik
    with os.fdopen(fh, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_line = '1' + line[1:]
                new_file.write(new_line)
    copymode(file_path, abs_path)  # kopiuje uprawnienia pierwotnego pliku do nowego
    os.remove(file_path)
    move(abs_path, file_path)


path = '/mnt/d/actions_data2/'
dirs = os.listdir(path)
# folders to lista nazw wewnetrznych katalogow (w naszym wypadku 'train', 'test', 'valid')
folders = [file for file in os.listdir(path) if os.path.isdir(path + file)]

# Petla zewnetrzna uzyskuje sciezke folderu z etykietami biezacego podzbioru
for data_set in folders:
    txt_file_path = path + data_set + '/labels/'
    # Petla wewnetrzna podmienia klase obiektu w kazdym pliku z etykietami dla biezacego podzbioru
    for text_file in os.listdir(txt_file_path):
        replace(txt_file_path + text_file)