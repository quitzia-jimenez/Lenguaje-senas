import os
import cv2
import string  # para obtener el alfabeto A-Z automáticamente

# Ruta para guardar los datos
DATA_DIR = 'C:/Users/JAT/Documents/TraductorLS/data'

# Crear directorio raíz si no existe
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Letras del abecedario inglés (sin ñ, ll, etc.)
alphabet = list(string.ascii_uppercase)  # ['A', 'B', 'C', ..., 'Z']
dataset_size = 100  # Número de imágenes por letra

cap = cv2.VideoCapture(0)

for letter in alphabet:
    letter_dir = os.path.join(DATA_DIR, letter)
    if not os.path.exists(letter_dir):
        os.makedirs(letter_dir)

    print(f'\n➡️  Coleccionando datos para la letra: {letter.upper()}')
    print('Presiona "q" para comenzar la captura...')

    # Espera a que el usuario presione 'q' para empezar la captura
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, f'Letra: {letter.upper()} - Presiona "Q" para capturar', (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Comienza la captura
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            continue
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(letter_dir, f'{counter}.jpg'), frame)
        counter += 1

    print(f'✅ Capturadas {dataset_size} imágenes para la letra {letter}.')

cap.release()
cv2.destroyAllWindows()
