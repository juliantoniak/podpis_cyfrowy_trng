import hashlib

def hash_file(filename):
    # Inicjalizuj obiekt SHA-3
    sha3 = hashlib.sha3_256()

    with open(filename, 'rb') as file:
        # Odczytaj zawartość pliku partiami, aby uniknąć zbyt dużego obciążenia pamięciowego
        for chunk in iter(lambda: file.read(4096), b''):
            # Uaktualnij skrót SHA-3
            sha3.update(chunk)

    # Zwróć zakodowany skrót jako heksadecymalny ciąg znaków
    return sha3.hexdigest()

# Przykładowe użycie
filename = 'sciezka/do/pliku.txt'
hash_value = hash_file(filename)
print(f"Skrót SHA-3 pliku '{filename}': {hash_value}")

##########################################################################
from Cryptodome.Hash import SHA3_256

def hash_file(filename):
    # Inicjalizuj obiekt SHA-3
    sha3 = SHA3_256.new()

    with open(filename, 'rb') as file:
        # Odczytaj zawartość pliku partiami, aby uniknąć zbyt dużego obciążenia pamięciowego
        for chunk in iter(lambda: file.read(4096), b''):
            # Uaktualnij skrót SHA-3
            sha3.update(chunk)

    # Zwróć zakodowany skrót jako heksadecymalny ciąg znaków
    return sha3.hexdigest()

# Przykładowe użycie
filename = 'sciezka/do/pliku.txt'
hash_value = hash_file(filename)
print(f"Skrót SHA-3 pliku '{filename}': {hash_value}")
