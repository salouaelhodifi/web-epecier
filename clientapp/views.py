from django.shortcuts import render,redirect
from clientapp.models import Client
from clientapp.formulaire import ClientForm

def clients(request):
    if request.method=="POST":
        form= ClientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
            form=ClientForm()
    return render(request,'index.html',{'form': form})  

def show(request):
    clients= Client.objects.all()
    return render(request,'show.html',{'clients': clients })

def edit(request,id):
    client=Client.objects.get(id=id)
    return render(request,'edit.html',({'client':client}))

def update(request,id):
    client=Client.objects.get(id=id)
    form=ClientForm(request.POST,instance=client)
    if form .is_valid():
        form.save()
        return redirect("/show")
    return render(request,'edit.html',{'client':client})

def destroy(request,id):
    client=Client.objects.get(id=id)
    client.delete()
    return redirect("/show")

