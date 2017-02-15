from django import forms
from .models import Calc



#не настроено!!!
def upload_file(request):
    # Если метод POST
    if request.method == 'POST':
        # Заполняем форму полученными данными
        form = UploadFileForm(request.POST, request.FILES)
        # Если данные валидны
        if form.is_valid():
            # обрабатываем файл
            handle_uploaded_file(request.FILES['file'])
            # перенаправляем на другую страницу
            return HttpResponseRedirect('/success/url/')
    # Если другой метод (обычно GET)
    else:
        form = UploadFileForm()
    # Выводим форму загрузки
    return render_to_response('upload.html', {'form': form})
