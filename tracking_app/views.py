import datetime
from django.core.files.utils import FileProxyMixin
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .forms import LoginForm, ParticipantForm, EntryForm, QrcodeEditForm
from .models import Participant, QrCodeId, Entry
import uuid

# Util
def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False

# Create your views here.
def index_view(request):
    if not request.user.is_authenticated:       
        return redirect('login')

    participants = Participant.objects.all().filter(date_entered__date=datetime.datetime.today())
    total = participants.count

    return render(request, 'tracking_app/index.html', {
        'totalNr': total,
    })
    

def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"],
                password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, "Invalid username or password")

    return render(request, 'tracking_app/login.html', {
        'form': form
        })

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(redirect_field_name='login', login_url='/login')
def new_participant_view(request):
    form = ParticipantForm(request.POST or None)
    
    context = {'form': form}

    if request.method == "POST":
        if form.is_valid():
            copil = form.save()
            copil.inside = True
            copil.save()
            name = form.cleaned_data['name']
            #first_name = form.cleaned_data['first_name']
            context['name'] = "%d %s" % (copil.id, name)
            form = ParticipantForm()
    
    return render(request, 'tracking_app/new_participant.html', context)

@login_required(redirect_field_name='login', login_url='/login')
def participants_view(request):
    participants = Participant.objects.all().order_by('name')

    return render(request, 'tracking_app/participants.html', { 'participants': participants })

@login_required(redirect_field_name='login', login_url='/login')
def edit_participant_view(request, id):
    try:
        participant = Participant.objects.get(pk=id)
    except Participant.DoesNotExist:
        return HttpResponse("404 Particpant with id '%s' does not exist"%id)
    
    form = QrcodeEditForm(request.POST or None)

    context = {}

    if request.method == 'POST':
        if form.is_valid():
            qrcodeid = form.cleaned_data['qrcode_uuid']
            try:
                participant = Participant.objects.get(qrcode_id=qrcodeid)
            except:
                entry_set = Entry.objects.all().filter(participant=participant).order_by('time')
                entries = {}
                for entry in entry_set:
                    date = entry.time.strftime("%d %b %Y")
                    if date not in entries:
                        entries[date] = []
                    entries[date].append(entry)
                return render(request, 'tracking_app/edit_participant.html', {
                    'participant': participant,
                    'entries': entries.items(),
                    'form': form,
                    'message': "Invalid qrcode"
                })
            participant.qrcode_id = qrcodeid
            participant.save()
            context['message'] = "Qrcode changed"
        else:
            context['message'] = "Invalid qrcode"
    entry_set = Entry.objects.all().filter(participant=participant).order_by('time')
    entries = {}
    for entry in entry_set:
        date = entry.time.strftime("%d %b %Y")
        if date not in entries:
            entries[date] = []
        entries[date].append(entry)
    print(entries)

    context['participant'] = participant
    context['entries'] = entries.items()
    context['form'] = form
    return render(request, 'tracking_app/edit_participant.html', context)

@login_required(redirect_field_name='login', login_url='/login')
def participant_entry_view(request):
    form = EntryForm(request.POST or None)
    context = {'form': form}

    if request.method == "POST":
        if form.is_valid():
            try:
                participant = Participant.objects.get(qrcode_id=form.cleaned_data['qrcode_uuid'])
                stand=form.cleaned_data['stand']
            except Participant.DoesNotExist:
                form.add_error(None, "Invalid code")
                return render(request, 'tracking_app/entry.html', context)
            if stand == '1':
                if participant.stand1 ==False:
                    participant.scans = participant.scans+1
                    participant.stand1 = True 
            elif stand == '2':
                if participant.stand2 ==False:
                    participant.scans = participant.scans+1
                    participant.stand2 = True
            elif stand == '3':
                if participant.stand3 ==False:
                    participant.scans = participant.scans+1
                    participant.stand3 = True
            elif stand == '4':
                if participant.stand4 ==False:
                    participant.scans = participant.scans+1
                    participant.stand4 = True
            elif stand == '5':
                if participant.stand5 ==False:
                    participant.scans = participant.scans+1
                    participant.stand5 = True
            elif stand == '6':
                if participant.stand6 ==False:
                    participant.scans = participant.scans+1
                    participant.stand6 = True
            elif stand == '7':
                if participant.stand7 ==False:
                    participant.scans = participant.scans+1
                    participant.stand7 = True
            elif stand == '8':
                if participant.stand8 ==False:
                    participant.scans = participant.scans+1
                    participant.stand8 = True
            elif stand == '9':
                if participant.stand9 ==False:
                    participant.scans = participant.scans+1
                    participant.stand9 = True
            elif stand == '10':
                if participant.stand10 ==False:
                    participant.scans = participant.scans+1
                    participant.stand10 = True
            elif stand == '11':
                if participant.stand1 ==False:
                    participant.scans = participant.scans+1
                    participant.stand11 = True
            elif stand == '12':
                if participant.stand12 ==False:
                    participant.scans = participant.scans+1
                    participant.stand12 = True
            elif stand == '13':
                if participant.stand13 ==False:
                    participant.scans = participant.scans+1
                    participant.stand13 = True
            elif stand == '14':
                if participant.stand14 ==False:
                    participant.scans = participant.scans+1
                    participant.stand14 = True
            elif stand == '15':
                if participant.stand15 ==False:
                    participant.scans = participant.scans+1
                    participant.stand15 = True
            elif stand == '16':
                if participant.stand16 ==False:
                    participant.scans = participant.scans+1
                    participant.stand16 = True
            elif stand == '17':
                if participant.stand17 ==False:
                    participant.scans = participant.scans+1
                    participant.stand17 = True
            elif stand == '18':
                if participant.stand18 ==False:
                    participant.scans = participant.scans+1
                    participant.stand18 = True
            elif stand == '19':
                if participant.stand19 ==False:
                    participant.scans = participant.scans+1
                    participant.stand19 = True
            elif stand == '20':
                if participant.stand20 ==False:
                    participant.scans = participant.scans+1
                    participant.stand20 = True
            elif stand == '21':
                if participant.stand21 ==False:
                    participant.scans = participant.scans+1
                    participant.stand21 = True
            elif stand == '22':
                if participant.stand22 ==False:
                    participant.scans = participant.scans+1
                    participant.stand22 = True
            elif stand == '23':
                if participant.stand23 ==False:
                    participant.scans = participant.scans+1
                    participant.stand23 = True
            elif stand == '24':
                if participant.stand24 ==False:
                    participant.scans = participant.scans+1
                    participant.stand24 = True
            elif stand == '25':
                if participant.stand25 ==False:
                    participant.scans = participant.scans+1
                    participant.stand25 = True
            elif stand == '26':
                if participant.stand26 ==False:
                    participant.scans = participant.scans+1
                    participant.stand26 = True
            elif stand == '27':
                if participant.stand27 ==False:
                    participant.scans = participant.scans+1
                    participant.stand27 = True
            elif stand == '28':
                if participant.stand28 ==False:
                    participant.scans = participant.scans+1
                    participant.stand28 = True
            elif stand == '29':
                if participant.stand29 ==False:
                    participant.scans = participant.scans+1
                    participant.stand29 = True
            elif stand=='30':
                if participant.stand30 ==False:
                    participant.scans = participant.scans+1
                    participant.stand30 = True
            elif stand=='31':
                if participant.stand31 ==False:
                    participant.scans = participant.scans+1
                    participant.stand31 = True
            elif stand=='32':
                if participant.stand32 ==False:
                    participant.scans = participant.scans+1
                    participant.stand32 = True
            participant.date_entered = datetime.datetime.today()
            participant.save()
            Entry.objects.create(participant=participant)
            context['succes'] = '%d %s %s has %s' % (
                participant.id,
                participant.name,
                participant.first_name,
                'finished task')
            context['succes'] = '<div style="color:green;">' + context['succes'] + '</div>'
            
    return render(request, 'tracking_app/entry.html', context)

@login_required(redirect_field_name='login', login_url='/login')
def delete_participant_view(request, id):
    copil = get_object_or_404(Participant, pk=id)
    qrcodeid = QrCodeId.objects.get(pk = copil.qrcode_id)
    qrcodeid.is_used = False
    qrcodeid.save()
    copil.delete()
    return redirect('participants')