from django.shortcuts import render, redirect
from django.utils.translation import activate

def landing(request):
    LANGUAGE_CODE = request.session.get("django_language", "en")
    ctx = {'LANGUAGE_CODE':LANGUAGE_CODE}
    if LANGUAGE_CODE == 'en':
      return render(request, 'frontend/en/landing.html', ctx)
    elif LANGUAGE_CODE == 'ar':
      return render(request, 'frontend/ar/landing.html', ctx)

def set_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        if language in ['en', 'ar']:
            activate(language)
            request.session['django_language'] = language
    return redirect('landing')
