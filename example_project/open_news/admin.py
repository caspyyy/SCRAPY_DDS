from django.contrib import admin
from open_news.models import NewsWebsite, NewsWebsite2, Article, Article2

class NewsWebsiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url_', 'scraper')
    list_display_links = ('name',)
    
    def url_(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (instance.url, instance.url)
    url_.allow_tags = True

class NewsWebsite2Admin(admin.ModelAdmin):
    list_display = ('id', 'name2', 'url_', 'scraper')
    list_display_links = ('name2',)
    
    def url_(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (instance.url, instance.url)
    url_.allow_tags = True
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'index', 'news_website', 'value', 'change', 'percentage', 'url_',)
    list_display_links = ('index',)
    raw_id_fields = ('checker_runtime',)
    
    def url_(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (instance.url, instance.url)
    url_.allow_tags = True

class Article2Admin(admin.ModelAdmin):
    list_display = ('id', 'index', 'news_website', 'value', 'change', 'percentage', 'date', 'url_',)
    list_display_links = ('index',)
    raw_id_fields = ('checker_runtime',)

    def url_(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (instance.url, instance.url)
    url_.allow_tags = True

admin.site.register(NewsWebsite, NewsWebsiteAdmin)
admin.site.register(NewsWebsite2, NewsWebsite2Admin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Article2, Article2Admin)