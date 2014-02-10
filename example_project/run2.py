import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example_project.settings")

    from scrapy.cmdline import execute

    execute("scrapy crawl article_spider2 -a id=1 -a do_action=yes".split())

    #from django.core.management import execute_from_command_line

    #execute_from_command_line(sys.argv)