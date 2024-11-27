from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from main_app.models import Event
from main_app.forms import EventForm, EventModifyForm, EventDeleteForm, UserRegisterForm
from django.contrib.auth import get_user_model, authenticate, login, logout


def index(request):
    return render(request, template_name='index.html')


class EventListView(View):
    def get(self, request):
        events = Event.objects.all()
        return render(request, 'event_list.html', {'events': events})


class EventDetailView(View):
    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        return render(request, 'event_detail.html', {'event': event})


def EventCreateView(request):
    form = EventForm()

    if request.method == "POST":
        form = EventForm(request.POST or None)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('event-list')

    return render(request, 'event_form.html', {'form': form})


def EventModifyView(request, event_id):
    current_event = Event.objects.filter(id=event_id).first()
    form = EventModifyForm(instance=current_event)

    if request.method == "POST":
        form = EventModifyForm(request.POST, instance=current_event)
        if form.is_valid():
            form.save()
            return redirect('event-list')

    return render(request, 'event-modify-form.html', {'form': form,
                                                      'event': current_event})


def EventDeleteView(request, event_id):
    current_event = Event.objects.filter(id=event_id).first()
    form = EventDeleteForm(instance=current_event)

    if request.method == "POST":
        current_event.delete()
        return redirect('event-list')

    return render(request, 'event-delete-form.html', context={'form': form})


def ModifyProfileView(request):
    context = {}
    return render(request, template_name='modify-profile.html', context=context)


def ChangePasswordView(request):
    context = {}
    return render(request, template_name='change-password.html', context=context)


def DeleteProfileView(request):
    context = {}
    return render(request, template_name='delete-profile.html', context=context)


def user_profile(request):
    UserModel = get_user_model()
    current_user = UserModel.objects.get(username='pesho')
    return render(request, 'profile.html', {'profile': current_user})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('event-list')
        else:
            messages.success(request, "There was an error. Please try again later!")
            return redirect('login')

    context = {}
    return render(request, template_name='login.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('index')


def user_registration(request):
    form = UserRegisterForm()

    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('event-list')

    context = {'form': form}
    return render(request, template_name='registration.html', context=context)