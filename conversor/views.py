from django.shortcuts import render
from django.http import FileResponse
from .forms import UploadFileForm
from .utils import convert_to_pdf

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            try:
                pdf_path = convert_to_pdf(uploaded_file)
                return FileResponse(open(pdf_path, 'rb'), as_attachment=True, filename="convertido.pdf")
            except Exception as e:
                return render(request, 'upload.html', {'form': form, 'error': str(e)})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

# Create your views here.
