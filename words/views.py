from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Word
from .forms import WordForm

# List all words
def word_list(request):
    # Get filter parameters from GET request
    language = request.GET.get('language', '')
    level = request.GET.get('level', '')

    # Start with all words
    words = Word.objects.all()

    # Apply filters based on GET parameters
    if language:
        words = words.filter(language=language)

    if level:
        words = words.filter(level=level)

    return render(request, 'words/word_list.html', {'words': words})

# Create a new word
def word_create(request):
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('word_list')
    else:
        form = WordForm()
    return render(request, 'words/word_form.html', {'form': form})

# Update an existing word
def word_update(request, pk):
    word = get_object_or_404(Word, pk=pk)
    if request.method == "POST":
        form = WordForm(request.POST, instance=word)
        if form.is_valid():
            form.save()
            return redirect('word_list')
    else:
        form = WordForm(instance=word)
    return render(request, 'words/word_form.html', {'form': form})

# Delete a word
def word_delete(request, pk):
    word = get_object_or_404(Word, pk=pk)
    if request.method == "POST":
        word.delete()
        return redirect('word_list')
    return render(request, 'words/word_confirm_delete.html', {'word': word})
