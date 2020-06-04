from django.shortcuts import render
from django.shortcuts import redirect

def blog_redirect(req):
    return redirect("/", permanent=True)