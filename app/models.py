from django.db import models
from adminsortable.models import SortableMixin

# Create your models here.
class Profile(models.Model):
    title = models.CharField('タイトル' , max_length=100, null=True , blank = True)
    subtitle = models.CharField('サブタイトル' , max_length=100, null=True , blank = True)
    name = models.CharField('名前' , max_length=100)
    job = models.TextField('仕事')
    introduction = models.TextField('自己紹介')
    github = models.CharField('github' , max_length=100, null=True , blank = True)
    twitter = models.CharField('twitter' , max_length=100, null=True , blank = True)
    linkedin = models.CharField('linkedin' , max_length=100, null=True , blank = True)
    facebook = models.CharField('facebook' , max_length=100, null=True , blank = True)
    instagram = models.CharField('instagram' , max_length=100, null=True , blank = True)
    topimage1 = models.ImageField(upload_to='images' , verbose_name='トップ画像',null=True , blank = True)
    topimage2 = models.ImageField(upload_to='images' , verbose_name='トップ画像',null=True , blank = True)
    topimage3 = models.ImageField(upload_to='images' , verbose_name='トップ画像',null=True , blank = True)
    subimage = models.ImageField(upload_to='images' , verbose_name='サブ画像')

    def __str__(self):
        return self.name
class Skill(models.Model):
    title = models.CharField('タイトル' , max_length=100)
    image = models.ImageField(upload_to='images' , verbose_name='イメージ画像')
    thumbnail = models.ImageField(upload_to='images' , verbose_name='サムネイル', null=True, blank=True)

    def __str__(self):
        return self.title

class Work(SortableMixin):
    title = models.CharField('タイトル' , max_length=100)
    image = models.ImageField(upload_to='images' , verbose_name='イメージ画像')
    thumbnail = models.ImageField(upload_to='images' , verbose_name='サムネイル', null=True, blank=True)
    skill = models.ForeignKey(Skill, verbose_name='スキル', on_delete=models.CASCADE)
    url = models.CharField('GithubURL' , max_length=100 , null=True, blank=True)
    created = models.DateField('作成日')
    worksTitle = models.CharField('作品タイトル' , max_length=100 ,null=True, blank=True)
    numberOfPeople = models.CharField('チーム開発か個人開発か' , max_length=100 ,null=True, blank=True)
    movieUrl = models.CharField('MovieURL' , max_length=100 , null=True, blank=True)
    worksDescription = models.TextField('その作品についての説明' ,null=True, blank=True)
    hardshipDescription = models.TextField('苦労した点について' ,null=True, blank=True)
    learning = models.TextField('そこから学んだこと' ,null=True, blank=True)
    thoughs = models.TextField('感想' ,null=True, blank=True)
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ["the_order"]

    def __str__(self):
        return self.title

class Dream(models.Model):
    title = models.CharField('タイトル' , max_length=100, null=True , blank = True)
    short_description = models.TextField('短い説明', null=True , blank = True)
    consciousness = models.TextField('意識していること', null=True , blank = True)
    description = models.TextField('説明', null=True , blank = True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    skill_name = models.CharField('技術名' , max_length=100 ,null=True , blank = True)
    skill = models.ForeignKey(Skill, verbose_name='スキル', on_delete=models.CASCADE)
    url = models.CharField('その技術を使った最高傑作のURL' , max_length=100 ,null=True , blank = True)
    description = models.TextField('その技術についての説明' ,null=True , blank = True)
    goodBad = models.TextField('その技術の苦手・得意' ,null=True , blank = True)
    aim = models.TextField('次の目標' ,null=True , blank = True)

    def __str__(self): 
        return self.skill_name

class Education(models.Model):
    course = models.CharField('コース' , max_length=100)
    school = models.CharField('学校' , max_length=100)
    place = models.CharField('場所' , max_length=100)
    period = models.CharField('期間' , max_length=100)

    def __str__(self):
        return self.course

class Software(models.Model):
    name = models.CharField('ソフトウェア' , max_length=100)
    level = models.CharField('レベル' , max_length=100)
    percentage = models.IntegerField('パーセンテージ')

    def __str__(self):
        return self.name

class Technical(models.Model):
    name = models.CharField('テクニカル' , max_length=100)
    level = models.CharField('レベル' , max_length=100)
    percentage = models.IntegerField('パーセンテージ')

    def __str__(self):
        return self.name