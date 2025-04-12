import os
from PIL import Image
from docx2pdf import convert as convert_docx
import uuid

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_DIR = os.path.join(BASE_DIR, '..', 'media')

def convert_to_pdf(uploaded_file):
    ext = uploaded_file.name.split('.')[-1].lower()
    base_name = uuid.uuid4().hex  # nome único

    input_path = os.path.join(MEDIA_DIR, f"{base_name}.{ext}")
    output_path = os.path.join(MEDIA_DIR, f"{base_name}.pdf")

    # Salvar o arquivo de upload
    with open(input_path, 'wb+') as f:
        for chunk in uploaded_file.chunks():
            f.write(chunk)

    # Converter para PDF
    if ext in ['jpg', 'jpeg', 'png']:
        image = Image.open(input_path).convert("RGB")
        image.save(output_path, "PDF")
    elif ext == 'docx':
        convert_docx(input_path, output_path)
    else:
        raise ValueError("Formato não suportado.")

    return output_path

# Garante que a pasta exista
if not os.path.exists(MEDIA_DIR):
    os.makedirs(MEDIA_DIR)
