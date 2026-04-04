from django.shortcuts import render, redirect
from .models import Event, Donation
from django.contrib.auth.decorators import login_required


# 🏠 HOME
def home(request):
    total_events = Event.objects.count()
    total_donations = Donation.objects.count()
    total_amount = sum([d.amount for d in Donation.objects.all()])

    return render(request, 'events/home.html', {
        'total_events': total_events,
        'total_donations': total_donations,
        'total_amount': total_amount
    })


# 📅 EVENTS LIST
def events_page(request):
    query = request.GET.get('q')
    events = Event.objects.all()

    if query:
        events = events.filter(title__icontains=query)

    return render(request, 'events/events.html', {'events': events})


# ➕ ADD EVENT
@login_required
def add_event(request):
    if request.method == 'POST':
        Event.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            date=request.POST.get('date'),
            location=request.POST.get('location'),
            image=request.FILES.get('image')
        )
        return redirect('/events/')

    return render(request, 'events/add_event.html')


# ✏️ EDIT EVENT
@login_required
def edit_event(request, id):
    event = Event.objects.get(id=id)

    if request.method == 'POST':
        event.title = request.POST.get('title')
        event.description = request.POST.get('description')
        event.date = request.POST.get('date')
        event.location = request.POST.get('location')

        if request.FILES.get('image'):
            event.image = request.FILES.get('image')

        event.save()
        return redirect('/events/')

    return render(request, 'events/edit_event.html', {'event': event})


# ❌ DELETE EVENT
@login_required
def delete_event(request, id):
    event = Event.objects.get(id=id)
    event.delete()
    return redirect('/events/')


# 👀 EVENT DETAIL
def event_detail(request, id):
    event = Event.objects.get(id=id)
    return render(request, 'events/event_detail.html', {'event': event})


# 💳 DONATE
@login_required
def donate(request):
    if request.method == 'POST':
        Donation.objects.create(
            name=request.POST.get('name'),
            amount=request.POST.get('amount'),
            message=request.POST.get('message')
        )
        return redirect('/')

    return render(request, 'events/donate.html')