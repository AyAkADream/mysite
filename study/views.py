from django.shortcuts import render , redirect
from django.views.generic import View
from .models import study_Post
from .forms import study_PostForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class StudyIndexView(View):
    def get(self , request , *args, **kwargs):
        study_post_data = study_Post.objects.order_by('-id')
        return render(request , 'study/study_index.html' , {
            'study_post_data' : study_post_data
        })

class StudyPostDetailView(View):
    def get(self , request , *args, **kwargs):
        study_post_data = study_Post.objects.get(id=self.kwargs['pk'])
        return render(request , 'study/study_post_detail.html',{
            'study_post_data' : study_post_data
        })

class StudyCreatePostView(LoginRequiredMixin , View):
    def get(self , request , *args, **kwargs):
        study_form = study_PostForm(request.POST or None)
        return render(request , 'study/study_post_form.html' , {
            'study_form' : study_form
        })

    def post(self, request, *args, **kwargs):
        study_form = study_PostForm(request.POST or None)

        if study_form.is_valid():
            study_post_data = study_Post()
            #study_post_data.author = request.user
            study_post_data.title = study_form.cleaned_data['title']
            study_post_data.author = study_form.cleaned_data['author']
            study_post_data.content = study_form.cleaned_data['content']
            study_post_data.url1_title = study_form.cleaned_data['url1_title']
            study_post_data.url1 = study_form.cleaned_data['url1']
            study_post_data.url2_title = study_form.cleaned_data['url2_title']
            study_post_data.url2 = study_form.cleaned_data['url2']
            study_post_data.url3_title = study_form.cleaned_data['url3_title']
            study_post_data.url3 = study_form.cleaned_data['url3']
            study_post_data.url4_title = study_form.cleaned_data['url4_title']
            study_post_data.url4 = study_form.cleaned_data['url4']
            study_post_data.image1 = study_form.cleaned_data['image1']
            study_post_data.image2 = study_form.cleaned_data['image2']
            study_post_data.image3 = study_form.cleaned_data['image3']
            study_post_data.image4 = study_form.cleaned_data['image4']
            study_post_data.comparison = study_form.cleaned_data['comparison']
            study_post_data.key = study_form.cleaned_data['key']
            study_post_data.experiment = study_form.cleaned_data['experiment']
            study_post_data.discussion = study_form.cleaned_data['discussion']
            study_post_data.next_paper = study_form.cleaned_data['next_paper']
            study_post_data.thoughts = study_form.cleaned_data['thoughts']
            study_post_data.memo = study_form.cleaned_data['memo']
            study_post_data.save()
            return redirect('study_post_detail',study_post_data.id)

        return render(request , 'study/study_post_form.html' , {
            'study_form' : study_form
        })

class StudyPostEditView(LoginRequiredMixin , View):
    def get(self , request , *args, **kwargs):
        study_post_data = study_Post.objects.get(id=self.kwargs['pk'])
        study_form = study_PostForm(
            request.POST or None,
            initial={
                'title' : study_post_data.title,
                'author' : study_post_data.author,
                'content' : study_post_data.content,
                'url1_title' : study_post_data.url1_title,
                'url1' : study_post_data.url1,
                'url2_title' : study_post_data.url2_title,
                'url2' : study_post_data.url2,
                'url3_title' : study_post_data.url3_title,
                'url3' : study_post_data.url3,
                'url4_title' : study_post_data.url4_title,
                'url4' : study_post_data.url4,
                'image1' : study_post_data.image1,
                'image2' : study_post_data.image2,
                'image3' : study_post_data.image3,
                'image4' : study_post_data.image4,
                'comparison' : study_post_data.comparison,
                'key' : study_post_data.key,
                'experiment' : study_post_data.experiment,
                'discussion' : study_post_data.discussion,
                'next_paper' : study_post_data.next_paper,
                'thoughts' : study_post_data.thoughts,
                'memo' : study_post_data.memo,
            }
        )

        return render(request , 'study/study_post_form.html' , {
            'study_form' : study_form
        })

    def post(self , request , *args, **kwargs):
        study_form = study_PostForm(request.POST or None)

        if study_form.is_valid():
            study_post_data = study_Post.objects.get(id=self.kwargs['pk'])
            study_post_data.title = study_form.cleaned_data['title']
            study_post_data.author = study_form.cleaned_data['author']
            study_post_data.content = study_form.cleaned_data['content']
            study_post_data.url1_title = study_form.cleaned_data['url1_title']
            study_post_data.url1 = study_form.cleaned_data['url1']
            study_post_data.url2_title = study_form.cleaned_data['url2_title']
            study_post_data.url2 = study_form.cleaned_data['url2']
            study_post_data.url3_title = study_form.cleaned_data['url3_title']
            study_post_data.url3 = study_form.cleaned_data['url3']
            study_post_data.url4_title = study_form.cleaned_data['url4_title']
            study_post_data.url4 = study_form.cleaned_data['url4']
            study_post_data.image1 = study_form.cleaned_data['image1']
            study_post_data.image2 = study_form.cleaned_data['image2']
            study_post_data.image3 = study_form.cleaned_data['image3']
            study_post_data.image4 = study_form.cleaned_data['image4']
            study_post_data.comparison = study_form.cleaned_data['comparison']
            study_post_data.key = study_form.cleaned_data['key']
            study_post_data.experiment = study_form.cleaned_data['experiment']
            study_post_data.discussion = study_form.cleaned_data['discussion']
            study_post_data.next_paper = study_form.cleaned_data['next_paper']
            study_post_data.thoughts = study_form.cleaned_data['thoughts']
            study_post_data.memo = study_form.cleaned_data['memo']
            study_post_data.save()
            return redirect('study_post_detail' , self.kwargs['pk'])

        return render(request , 'study_/study_post_form.html' , {
            'study_form' : study_form
        })

class StudyPostDeleteView(LoginRequiredMixin , View):
    def get(self , request , *args, **kwargs):
        study_post_data = study_Post.objects.get(id=self.kwargs['pk'])

        return render(request , 'study/study_post_delete.html' , {
            'study_post_data' : study_post_data
        })

    def post(self , request , *args, **kwargs):
        study_post_data = study_Post.objects.get(id=self.kwargs['pk'])
        study_post_data.delete()
        return redirect('study_index')





