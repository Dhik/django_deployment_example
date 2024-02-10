from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord, User
from . import forms
from first_app.forms import NewUserForm
# Create your views here.

def index_rel_url(request):
    context_dict = {'text': 'hello world', 'number': 100}
    return render(request, 'basic_app/index.html', context_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_template.html')

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    # my_dict = {'insert_me': "Now I coming from first app index.html !"}
    return render(request, 'first_app/index.html', context=date_dict)

def another(request):
    my_dict = {'insert_me': "Another Page"}
    return render(request, 'first_app/index.html', context=my_dict)

def register(request):
    return render(request, 'first_app/register.html')

def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return register(request)
        else:
            print('ERROR FORM INVALID')
    return render(request, 'first_app/users.html', {'form': form})

def form_name_view(request):
	form = forms.FormName()
	
	if request.method == 'POST':
		form = forms.FormName(request.POST)
		if form.is_valid():
			print("VALIDATION SUCCESS!")
			print("NAME: "+form.cleaned_data['name'])
			print("EMAIL: "+form.cleaned_data['email'])
			print("TEXT: "+form.cleaned_data['text'])

	return render(request, 'first_app/form_page.html', {'form':form})
