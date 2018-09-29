from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Entry
from .forms import EntryForm
from django.views.generic import ListView, DetailView, TemplateView


class IndexTemplateView(TemplateView):
    template_name = 'calendarNote/index.html'


class CalendarListView(ListView):
    template_name = 'calendarNote/calendar.html'
    model = Entry
    context_object_name = 'entries'

    def get_queryset(self, *args, **kwargs):
        return Entry.objects.filter(author=self.request.user)


class EntryDetailView(DetailView):
    template_name = 'calendarNote/details.html'
    model = Entry
    context_object_name = 'entry'

# CreateView

# DeleteView


def add(request):

    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']

            Entry.objects.create(
                name=name,
                author=request.user,
                date=date,
                description=description,
                start_time=start_time,
                end_time=end_time,
            )

            return HttpResponseRedirect('/todo')

    else:
        form = EntryForm()

    return render(request, 'calendarNote/form.html', {'form': form})


def delete(request, pk):

    if request.method == 'DELETE':
        entry = get_object_or_404(Entry, pk=pk)
        entry.delete()

    return HttpResponseRedirect('/')

