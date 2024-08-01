import nltk
import os

# Configura NLTK para usar el directorio local
nltk_data_path = os.path.expanduser('~/nltk_data')
if not os.path.exists(nltk_data_path):
    os.makedirs(nltk_data_path)

nltk.data.path.append(nltk_data_path)

# Verifica que los datos de 'punkt' están disponibles
try:
    nltk.data.find('tokenizers/punkt')
    print("Los datos de 'punkt' ya están disponibles.")
except LookupError:
    print("No se encontraron los datos de 'punkt'. Asegúrate de que estén en el directorio correcto.")
