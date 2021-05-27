from django.shortcuts import redirect, render
from .models import modelForm
from .forms import mainForm
# Create your views here.



def testKt(request):
    return render(request, 'test.html')

# Add and show data to the home page
def index(request):
    form = mainForm()
    if request.method == 'POST' :
        form = mainForm(request.POST)
        if form.is_valid():
            print('Form validation successfull')
            ktName = form.cleaned_data['name']
            ktEmail = form.cleaned_data['email']
            ktPass = form.cleaned_data['password']

            regForm = modelForm(name = ktName, email = ktEmail, password = ktPass)
            regForm.save()
            return redirect('/submit')

        else :
            print('Form is not valid')
            params = {'form' : form}

    else :
        params = {'form' : form}

    dbData = modelForm.objects.all() 
    print(dbData)
    dataParam = {'data' : dbData}

    params = {'form' : form ,'data' : dbData}
    return render(request, 'index.html', params)


# delete data
def delData(request, id):
    if request.method == 'POST' :
        pid = modelForm.objects.get(pk = id )
        pid.delete()

    return redirect('/')


# Update Data
def upData(request, pid):
    if request.method == "POST" :
        data = modelForm.objects.get(pk = pid)
        formData = mainForm(request.POST)
        if formData.is_valid():
            fName = formData.cleaned_data['name']
            fEmail = formData.cleaned_data['email']
            fPass = formData.cleaned_data['password']
            regData = modelForm(id = pid, name = fName, email = fEmail, password = fPass)
            regData.save()

        else :
            pass
        # data.delete()

    data = modelForm.objects.get(pk = pid)
    ktName = data.name
    ktEmail = data.email
    ktPass = data.password
    form = mainForm()
    form.initial = {'name' : ktName, 'email' : ktEmail, 'password' : ktPass}
    params = {'data' : data, 'id' : pid , 'form' : form}
    return render(request, 'edit.html', params)

# Help in submitting the form
def subForm(request):
    return redirect('/')

