from django.db import models


class GetRSS(models.Model):
    """取得したRSS情報"""
    title = models.CharField('タイトル', max_length=255)
    link = models.CharField('URL', max_length=5124)
    time = models.DateTimeField('時間', blank=True, default=0)
    category = models.IntegerField('カテゴリ', blank=True, default=0)
    flag =  models.IntegerField('カテゴリ', blank=True, default=0)

    def __str__(self):
        return self.title


class priRSS(models.Model):
    """RSSを取得するための情報"""
    url=models.CharField("URL",max_length=5124,blank=True)
    siteName=models.CharField("サイト名",max_length=255,blank=True)
    siteDetail=models.CharField("詳細",max_length=255,blank=True)
    def __str__(self):
        return self.url
