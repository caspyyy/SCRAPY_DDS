import os
import sys
import shlex
import subprocess

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example_project.settings")

    #from scrapy.cmdline import execute

    #execute("scrapy crawl article_spider -a id=1 -a do_action=yes".split())

    cmdl = "scrapy crawl article_spider -a id=1 -a do_action=yes"
    args = shlex.split(cmdl)
    p = subprocess = Popen(args)
    #from django.core.management import execute_from_command_line

    #execute_from_command_line(sys.argv)
