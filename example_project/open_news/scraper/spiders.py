from dynamic_scraper.spiders.django_spider import DjangoSpider
from open_news.models import NewsWebsite, NewsWebsite2, Article, Article2, ArticleItem, ArticleItem2


class ArticleSpider(DjangoSpider):
    
    name = 'article_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(NewsWebsite, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = Article
        self.scraped_obj_item_class = ArticleItem
        super(ArticleSpider, self).__init__(self, *args, **kwargs)

class ArticleSpider2(DjangoSpider):

	name = 'article_spider2'

	def __init__(self, *args, **kwargs):
		self._set_ref_object(NewsWebsite2, **kwargs)
		self.scraper = self.ref_object.scraper
		self.scrape_url = self.ref_object.url
		self.scheduler_runtime = self.ref_object.scraper_runtime
		self.scraped_obj_class = Article2
		self.scraped_obj_item_class = ArticleItem2
		super(ArticleSpider2, self).__init__(self, *args, **kwargs)