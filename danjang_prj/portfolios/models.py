from django.db import models
from django.contrib.auth.models import User

class Role(models.Model): # 전문분야 모델
    role_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

class Portfolio(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE) # 이름
    role = models.ForeignKey(Role, null=True, blank=True,on_delete=models.SET_NULL)
    profile_photo = models.ImageField(verbose_name="프로필사진", blank=True, upload_to='profile_photo') # 프로필 사진
    email = models.EmailField(max_length=128, verbose_name="이메일")
    one_line = models.CharField(verbose_name="한줄소개", max_length=128) # 한 줄 소개
    intro = models.TextField(verbose_name="소개글") # 소개글
    
class Career(models.Model): # 경력
    career_title = models.CharField(verbose_name="작품명", max_length=128)   
    career_role = models.CharField(verbose_name="역할", max_length=128)
    career_year = models.DateField(verbose_name="연도")

