from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm, TicketForm, TicketFilter
from .models import Ticket


def create_ticket(request):
    if not request.user.is_authenticated():
        return render(request, 'dashboard/login.html')
    else:
        # (request.POST or None, request.FILES or None)
        form = TicketForm(request.POST or None)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return render(request, 'dashboard/detail.html', {'ticket': ticket})
        context = {
            'form': form
        }
    return render(request, 'dashboard/create_ticket.html', context)


def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, ticket_id)
    if not request.user.is_authenticated():
        return render(request, 'dashboard/login.html')
    else:
        # (request.POST or None, request.FILES or None)
        form = TicketForm(request.POST or None)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return render(request, 'dashboard/detail.html', {'ticket': ticket})
        context = {
            'form': form,
            'title': ticket.title
        }
    return render(request, 'dashboard/create_ticket.html', context)


def delete_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    ticket.delete()
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'dashboard/index.html', {'tickets': tickets})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'dashboard/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                tickets = Ticket.objects.filter(user=request.user)
                return render(request, 'dashboard/index.html', {'tickets': tickets})
            else:
                return render(request, 'dashboard/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'dashboard/login.html', {'error_message': 'Invalid login'})
    return render(request, 'dashboard/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                tickets = Ticket.objects.filter(user=request.user)
                return render(request, 'dashboard/index.html', {'tickets': tickets})
    context = {
        "form": form,
    }
    return render(request, 'dashboard/register.html', context)


def detail(request, ticket_id):
    if not request.user.is_authenticated():
        return render(request, 'dashboard/login.html')
    else:
        user = request.user
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        return render(request, 'dashboard/detail.html', {'ticket': ticket, 'user': user})


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'dashboard/login.html')
    else:
        tickets = Ticket.objects.filter(user=request.user)
        '''query = request.GET.get("q")
        if query:
            tickets = tickets.filter(
                Q(ticket_title__icontains=query)
            ).distinct()
            return render(request, 'dashboard/index.html', {
                'tickets': tickets,
            })
        else:'''
        return render(request, 'dashboard/index.html', {'tickets': tickets})


def ticket_list(request):
    filter = TicketFilter(request.GET, queryset=Ticket.objects.all())
    return render(request, 'dashboard/index.html', {'filter': filter})
