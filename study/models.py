from django.db import models
from django.conf import settings
from django.utils import timezone

class study_Post(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField("タイトル" , max_length=200)
    author = models.TextField("著者と所属のリスト" , null=True, blank=True)
    content = models.TextField("どんなもの？", null=True, blank=True)
    url1_title = models.CharField('URL1のタイトル' , max_length=100 , null=True, blank=True)
    url1 = models.CharField('URL1' , max_length=100 , null=True, blank=True)
    url2_title = models.CharField('URL2のタイトル' , max_length=100 , null=True, blank=True)
    url2 = models.CharField('URL2' , max_length=100 , null=True, blank=True)
    url3_title = models.CharField('URL3のタイトル' , max_length=100 , null=True, blank=True)
    url3 = models.CharField('URL3' , max_length=100 , null=True, blank=True)
    url4_title = models.CharField('URL4のタイトル' , max_length=100 , null=True, blank=True)
    url4 = models.CharField('URL4' , max_length=100 , null=True, blank=True)
    image1 = models.ImageField(upload_to='images' , verbose_name='イメージ画像1', null=True, blank=True)
    image2 = models.ImageField(upload_to='images' , verbose_name='イメージ画像2', null=True, blank=True)
    image3 = models.ImageField(upload_to='images' , verbose_name='イメージ画像3', null=True, blank=True)
    image4 = models.ImageField(upload_to='images' , verbose_name='イメージ画像4', null=True, blank=True)
    comparison = models.TextField("先行研究と比べてどこがすごい？", null=True, blank=True)
    key = models.TextField("技術や手法のキモはどこ？", null=True, blank=True)
    experiment = models.TextField("どうやって有効だと検証した？", null=True, blank=True)
    discussion = models.TextField("議論はある？", null=True, blank=True)
    next_paper = models.TextField("次に読むべき論文は？", null=True, blank=True)
    thoughts = models.TextField("この論文について、どう思う？", null=True, blank=True)
    memo = models.TextField("その他・メモ", null=True, blank=True)
    created = models.DateTimeField("作成日" , default=timezone.now)

    def __str__(self):
        return self.title

