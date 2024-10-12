from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import UploadedFile  

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            print(f'Uploaded file: {uploaded_file.file.name}')  # Check the uploaded file name
            return redirect('success')
        else:
            print(form.errors)  # Print out form errors if validation fails
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})



def success(request):
    return render(request, 'success.html')



def file_list(request):
    # Filter files using regex to match file extensions
    pdf_files = UploadedFile.objects.filter(file__regex=r'\.pdf$')
    image_files = UploadedFile.objects.filter(file__regex=r'\.(jpg|jpeg|png)$')
    other_files = UploadedFile.objects.exclude(file__regex=r'\.(pdf|jpg|jpeg|png)$')

    context = {
        'pdf_files': pdf_files,
        'image_files': image_files,
        'other_files': other_files,
    }

    return render(request, 'list_files.html', context)
