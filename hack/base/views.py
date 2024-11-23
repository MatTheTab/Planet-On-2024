from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        uploaded_files = request.FILES.getlist('uploaded_file')
        if not uploaded_files:
            messages.error(request, "No file uploaded!")
            # Przekierowanie tylko, jeśli jest konieczne
            return redirect('/upload-error/')  # Inny URL, który obsługuje błąd

    # Renderowanie strony głównej w przypadku GET lub poprawnego przetwarzania
    return render(request, 'base/home.html')
