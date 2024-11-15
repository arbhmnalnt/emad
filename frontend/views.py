from django.shortcuts import render, redirect
from django.utils.translation import activate

def landing(request):
    print(f'{request.session["django_language"]}')
    LANGUAGE_CODE = request.session["django_language"]
    ctx = {'LANGUAGE_CODE':LANGUAGE_CODE}
    return render(request, 'frontend/landing.html', ctx)

def set_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        if language in ['en', 'ar']:
            activate(language)
            request.session['django_language'] = language
    return redirect('landing')
