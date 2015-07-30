from django.shortcuts import render

# Create your views here.
def view_site(request):
	return render(request,'website.html',{})