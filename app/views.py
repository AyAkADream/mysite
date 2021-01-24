from django.shortcuts import render , redirect, get_object_or_404
from django.views.generic import View
from .forms import ContactForm
from .models import Profile , Work , Skill ,Experience , Education, Software , Technical , Dream
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
import textwrap

# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by('-id')[0]
        skill_data = Skill.objects.all()
        return render(request, 'app/index.html' , {
            'profile_data':profile_data,
            'skill_data':skill_data,
        })

class SkillView(View):
    def get(self, request, *args, **kwargs):
        #skill_data = Skill.objects.get(id=self.kwargs['pk'])
        skill_data = get_object_or_404(Skill, id=self.kwargs['pk'])
        experience_data = Experience.objects.filter(skill=skill_data)
        work_data =  Work.objects.filter(skill=skill_data)
        return render(request, 'app/skill.html' , {
            'skill_data':skill_data,
            'experience_data':experience_data,
            'work_data':work_data,
        })

class DetailView(View):
    def get(self, request, *args, **kwargs):
        work_data = Work.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/detail.html' , {
            'work_data':work_data,
        })

class AboutView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by('-id')[0]
        #experience_data = Experience.objects.order_by('-id')
        education_data = Education.objects.order_by('-id')
        software_data = Software.objects.order_by('-id')
        technical_data = Technical.objects.order_by('-id')
        return render(request , 'app/about.html' , {
            'profile_data': profile_data,
            #'experience_data' : experience_data,
            'education_data' : education_data,
            'software_data' : software_data,
            'technical_data' : technical_data,
        })

class DreamView(View):
    def get(self, request, *args, **kwargs):
        dream_data = Dream.objects.all()
        if dream_data.exists():
            dream_data = dream_data.order_by('-id')[0]
        print(dream_data)
        print(dream_data)
        return render(request, 'app/dream.html' , {
            'dream_data': dream_data
        })

class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)
        return render(request , 'app/contact.html' , {
            'form':form
        })
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'お問い合わせありがとうございます。'
            contact = textwrap.dedent('''
                ※このメールはシステムからの自動返信です。

                {name}様

                お問い合わせありがとうございました。
                以下の内容でお問い合わせを受け付けいたしました。
                内容を確認させていただき、ご返信させていただきますので、少々お待ちください。

                -------------------
                ■お名前
                {name}

                ■メールアドレス
                {email}

                ■メッセージ
                {message}
                -------------------
                ''').format(
                    name=name,
                    email=email,
                    message=message
                )
            to_list = [email]
            bcc_list = [settings.EMAIL_HOST_USER]

            try:
                message = EmailMessage(subject=subject, body=contact, to=to_list, bcc=bcc_list)
                message.send()
            except BadHeaderError:
                return HttpResponse('無効なヘッダが検出されました。')

            return redirect('thanks')

        return render(request , 'app/contact.html' , {
            'form':form
        })

class ThanksView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/thanks.html')