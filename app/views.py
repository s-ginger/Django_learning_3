from django.shortcuts import render, redirect
from .forms import NoteForm
from api.models import Note
from django.middleware.csrf import get_token

def main_page(request):
    csrf_token = get_token(request)
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")  # перенаправление после POST (защита от повторной отправки)
    else:
        form = NoteForm()

    notes = Note.objects.all().order_by('-id')  # выводим все заметки
    return render(request, "main.jinja", {"form": form, "notes": notes, "csrf_token": csrf_token})


def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect("home")


