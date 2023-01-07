from django.shortcuts import render,redirect

# Create your views here.
def home_view(request):
    context = {'web_url':'api/'}

    return render(request,'home.html',context=context)
    # return redirect('serialI')