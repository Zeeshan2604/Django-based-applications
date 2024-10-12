import os
from django.db import models

def file_directory_path(instance, filename):
    # Get file extension
    ext = filename.split('.')[-1]
    
    # Define folder based on file extension
    if ext == 'pdf':
        folder = 'pdf'
    elif ext == 'docx':
        folder = 'doc'
    elif ext in ['jpg', 'png']:
        folder = 'images'
    else:
        folder = 'others'
    
    # Return the full path to the file
    return f'{folder}/{filename}'


def get_upload_path(instance, filename):
    # Get the file extension
    ext = filename.split('.')[-1].lower()
    
    # Determine the upload path based on the file type
    if ext in ['pdf']:
        return os.path.join('uploads', 'pdf', filename)  # Uploads to uploads/pdf/
    elif ext in ['jpg', 'jpeg', 'png']:
        return os.path.join('uploads', 'images', filename)  # Uploads to uploads/images/
    else:
        return os.path.join('uploads', 'others', filename)  # Uploads to uploads/others/


class Document(models.Model):
    file = models.FileField(upload_to=file_directory_path)

    def __str__(self):
        return self.file.name
    
class UploadedFile(models.Model):
    file = models.FileField(upload_to=get_upload_path) # Store files in uploads folder
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
