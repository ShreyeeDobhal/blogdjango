from django.shortcuts import render,get_object_or_404,redirect
from .models import post
from django.shortcuts import HttpResponse,HttpResponseRedirect,Http404
from .forms import postform
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
def post_create(request):
    if request.user.is_staff or not request.user.is_superuser:#remove when required
        raise Http404
    form=postform(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        #message of success
        messages.success(request,"Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
        }
    return render(request, 'post_form.html',context)

def post_detail(request,id=None):
    instance=get_object_or_404(post,id=id)
    context={
        "title":instance.title,
        "instance": instance,
    }
    return render(request,"post_detail.html",context)

def post_list(request):
    today= timezone.now().date()
    queryset_list=post.objects.order_by("-timestamp")
    if request.user.is_staff or not request.user.is_superuser:
        queryset_list=post.objects.all()
    query=request.GET.get("q")
    if query:
        queryset_list=queryset_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(user__first_name__icontains=query)|
            Q(user__last_name__icontains=query)).distinct()
    paginator = Paginator(queryset_list, 25)  # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        queryset=paginator.page(page)
    except PageNotAnInteger:
        #if page isnt an integer deliver first page
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context={
        "object_list" : queryset,
        "title" : "List "
    }
    return render(request,"post_list.html",context)







def post_update(request,id=None):
    if request.user.is_staff or not request.user.is_superuser:
        raise Http404#remove when required
    instance = get_object_or_404(post, id=id)
    form = postform(request.POST or None,request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #message saying success
        messages.success(request, "Successfully updated")
        messages.success(request, "Item saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        'form':form,
    }
    return render(request,"post_form.html",context)

def post_delete(request,id=None):
    if request.user.is_staff or not request.user.is_superuser:#remove when required
        raise Http404
    instance = get_object_or_404(post, id=id)
    instance.delete()
    messages.success(request, "Deleted Succesfully")
    return redirect("blog1:list")
   # return HttpResponse("<h1>DELETE</h1>")


def post_contact(request):
    return render(request, "contact.html")