from django.contrib import admin
from cms.models import GetRSS,priRSS

# admin.site.register(Book)
# admin.site.register(Impression)


class rssAdmin(admin.ModelAdmin):
    list_display = ('id',"title","link","time","category","flag",)  # 一覧に出したい項目
    list_display_links = ('id', 'title',)  # 修正リンクでクリックできる項目


admin.site.register(GetRSS, rssAdmin)


class priRSSAdmin(admin.ModelAdmin):
    list_display = ('id',"url","siteName","siteDetail",)  # 一覧に出したい項目
    list_display_links = ('id', 'url',)  # 修正リンクでクリックできる項目


admin.site.register(priRSS, priRSSAdmin)
