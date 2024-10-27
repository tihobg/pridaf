
# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegisterForm, NameForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from . models import Patients
from . forms import ScoreForm
from . forms import PreeclampsiaForm
import base64
import io
import urllib
import numpy as np
#import os os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"

import matplotlib.pyplot as plt
import matplotlib


def home1(request):
    return render(request, 'home1.html')

def index(request):
   return render(request, 'web/index.html')

def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about_us.html')

def services(request):
    return render(request, 'services.html')

def news(request):
    return render(request, 'news.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def logout_view(request):
    # handle logout logic here
    return render(request, 'home.html')


def preeclampsia(request):

    form_pre = PreeclampsiaForm()
    patients = Patients.objects.all()
    s = request.POST.getlist('ss')

    # Visualization of Correlation
    matplotlib.use('agg')
    # plt.style.use('ggplot')
    nx = np.arange(10, 20)
    ny = np.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])
    xyz = np.array([[10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                    [2, 1, 4, 5, 8, 12, 18, 25, 96, 48],
                    [5, 3, 2, 1, 0, -2, -8, -11, -15, -16]])

    corr_matrix = np.corrcoef(xyz).round(decimals=2)
    # print(corr_matrix)

    fig, ax = plt.subplots()
    im = ax.imshow(corr_matrix)
    im.set_clim(-1, 1)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1, 2), ticklabels=('x', 'y', 'z'))
    ax.yaxis.set(ticks=(0, 1, 2), ticklabels=('x', 'y', 'z'))
    ax.set_ylim(2.5, -0.5)
    for i in range(3):
        for j in range(3):
            ax.text(j, i, corr_matrix[i, j], ha='center', va='center',
                    color='r')
    cbar = ax.figure.colorbar(im, ax=ax, format='% .2f')

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    url = urllib.parse.quote(string)

    # ax.plot(nx, ny, linewidth=0, marker='s', label='Data Points')
    # plt.savefig("mygraph.png")
    # plt.show()
    form = ScoreForm()
    form_pre = PreeclampsiaForm()
    if request.method == "POST":
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form_pre = PreeclampsiaForm(request.POST)
            else:
                patient = Patients.objects.get(patient_id=pk)
                form_pre = PreeclampsiaForm(request.POST, instance=patient)
            form_pre.save()
            form_pre = PreeclampsiaForm()

        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            patient = Patients.objects.get(patient_id=pk)
            patient.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            patient = Patients.objects.get(patient_id=pk)
            form_pre = PreeclampsiaForm(instance=patient)
            print('Hello')
    context1 = {
        'patients': patients,
        'key': s,
        'key6': url,
        'key7': form,
        'key8': form_pre,

    }

    return render(request, 'preeclampsia.html', context1)

def pregnant_controls(request):
    return render(request, 'pregnant_controls.html')

def spontaneous_abortions(request):
    return render(request, 'spontaneous_abortions.html')
def database(request):
    return render(request, 'database.html')


def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('/about_us')
    else:
        # form = UserCreationForm()
        form = RegisterForm()
        # form = NameForm()
    return render(request, 'users/register.html', { 'form': form})
    # if request.method == 'POST':
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.username = user.username.lower()
    #         user.save()
    #         messages.success(request, 'You have singed up successfully.')
    #         login(request, user)
    #         return redirect('posts')
    #     else:
    #         return render(request, 'users/register.html', {'form': form})


# def login(request):
#     return render(request, 'login.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/preeclampsia')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', { 'form' : form})


def correlation(request):
    # if request.method == 'POST':
    #     form = AuthenticationForm(data=request.POST)
    #     if form.is_valid():
    #         login(request, form.get_user())
    #         return redirect('/')
    # else:
    #     form = AuthenticationForm()
    return render(request, 'users/correlation.html')


def add_edit_patient(request):
    return render(request, 'add_edit_patient.html')


def base(request):
    return render(request, 'base.html')

# def correlation(request):
#     return render(request, 'correlation.html')




