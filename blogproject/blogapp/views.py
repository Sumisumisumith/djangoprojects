from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import BlogPost
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage

def index_view(request):
    records = BlogPost.objects.order_by('-posted_at')
    paginator = Paginator(records, 4)
    page_number = request.GET.get('page', 1)
    pages = paginator.page(page_number)
    return render(request, 'index.html', {'orderby_records': pages})

def blog_detail(request, pk):
    record = BlogPost.objects.get(id=pk)
    return render(request, 'post.html', {'object': record})


def fashion_view(request):
    records = BlogPost.objects.filter(category='fashion').order_by('-posted_at')
    paginator = Paginator(records, 2)
    page_number = request.GET.get('page', 1)
    pages = paginator.page(page_number)
    return render(request, 'fashion_list.html', {'orderby_records': pages})

def dailylife_view(request):
    records = BlogPost.objects.filter(category='dailylife').order_by('-posted_at')
    paginator = Paginator(records, 2)
    page_number = request.GET.get('page', 1)
    pages = paginator.page(page_number)
    return render(request, 'dailylife_list.html', {'orderby_records': pages})

def sports_view(request):
    records = BlogPost.objects.filter(category='sports').order_by('-posted_at')
    paginator = Paginator(records, 2)
    page_number = request.GET.get('page', 1)
    pages = paginator.page(page_number)
    return render(request, 'sports_list.html', {'orderby_records': pages})


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, "contact.html", {'form': form})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['name']
            title = form.cleaned_data['title']
            message = form.cleaned_data['message']
            subject = 'お問い合わせ:{}'.format(title)
            message = '送信者名:{0}\nメールアドレス:{1}\nタイトル:{2}\n{3}'.format(name, email, title, message)
            from_email = 'sumiya.soccer.0806@gmail.com'
            to_list = ['sumiya.soccer.0806@gmail.com']
            message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list)
            message.send()
            messages.success(request, 'お問い合わせは正常に送信されました．')
            return redirect('blogapp:contact')
