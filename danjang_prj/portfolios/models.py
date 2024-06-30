from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

role_select = ( # 전문분야
    ('감독', '감독'),
    ('배우', '배우'),
    ('성우', '성우'),
    ('연출', '연출'),
    ('음향', '음향'),
    ('조명', '조명'),
    ('의상', '의상'),
    ('메이크업', '메이크업'),
    ('아역', '아역'),
    ('모델', '모델'),
    ('인플루언서', '인플루언서')
)

class Portfolio(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE) # 이름
    role = models.CharField(max_length=20, choices=role_select) # 전문분야
    profile_photo = models.ImageField(verbose_name="프로필사진", blank=True, upload_to='profile_photo') # 프로필 사진
    email = models.EmailField(max_length=128, verbose_name="이메일", blank=True)
    one_line = models.CharField(verbose_name="한줄소개", max_length=128, blank=True) # 한 줄 소개
    intro = models.TextField(verbose_name="소개글", blank=True) # 소개글

    def __str__(self):
        return self.name
    
class Career(models.Model): # 경력
    career_title = models.CharField(verbose_name="작품명", max_length=128)   
    career_role = models.CharField(verbose_name="역할", max_length=128)
    career_year = models.DateField(verbose_name="연도")
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

class Video(models.Model): # 포트폴리오 video
    title = models.CharField(verbose_name="제목", max_length=200)
    likes_user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='likes_user') # 찜
    cast = models.CharField(verbose_name="출연진", max_length=128) 
    staff = models.CharField(verbose_name="스탭", blank=True, max_length=128) 
    price = models.IntegerField(verbose_name="가격", default=0)
    keyword = models.TextField(verbose_name="키워드", blank=True)
    synopsis = models.TextField(verbose_name="시놉시스", blank=True)
    video = models.FileField(verbose_name="동영상", upload_to='media/')
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Photo(models.Model): # 포트폴리오 photo
    photo = models.ImageField(verbose_name="이미지", blank=True, null=True, upload_to='media/')
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def __str__(self):
        return self.photo
