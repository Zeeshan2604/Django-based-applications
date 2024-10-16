from django.shortcuts import render
from django.http import HttpResponse
from weasyprint import HTML
from .forms import HTMLFileForm

def html_to_pdf(request):
    if request.method == 'POST':
        form = HTMLFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Read the HTML content from the uploaded file
            html_file = request.FILES['file']
            html_content = html_file.read().decode('utf-8')

            # Convert the HTML content to PDF using WeasyPrint
            pdf = HTML(string=html_content).write_pdf()

            # Return the PDF as a downloadable response
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="output.pdf"'
            return response
    else:
        form = HTMLFileForm()

    return render(request, 'converter/upload.html', {'form': form})

