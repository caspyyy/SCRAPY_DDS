from celery.task import task

from dynamic_scraper.utils.task_utils import TaskUtils
from open_news.models import NewsWebsite, Article, Article2, NewsWebsite2

@task()
def run_spiders():
    t = TaskUtils()
    t.run_spiders(NewsWebsite, 'scraper', 'scraper_runtime', 'article_spider')
    t.run_spiders(NewsWebsite2, 'scraper', 'scraper_runtime', 'article_spider')
    
@task()
def run_checkers():
    t = TaskUtils()
    t.run_checkers(Article, 'news_website__scraper', 'checker_runtime', 'article_checker')
    t.run_checkers(Article2, 'news_website__scraper', 'checker_runtime', 'article_checker')