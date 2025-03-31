"""
@author: 薯条老师
@desc:
"""

from configure import settings
from multiprocessing import Process
from threading import Thread
from core import worker


def build_processes():
    processes = []
    for name, config in settings.SEEDS.items():
        processes.append(Process(target=worker.worker,
                                 args=(config.get("url_template"),
                                       config.get("pages"),
                                       config.get("url_generator"),
                                       config.get("crawling_task"),
                                       config.get("parse_func"),
                                       config.get("save_func"),
                                       name,
                                       )))
    return processes


def build_threads(urls, threads_size, worker, container):
    threads = []
    urls_length = len(urls)
    step = urls_length // threads_size
    for index in range(0, urls_length, step):
        urls_ = urls[index:index+step]
        threads.append(Thread(target=worker, args=(urls_, container)))
    return threads


def generates_urls(url_template, pages, handler=None):
    urls = []
    for page in range(pages):
        if not handler:
            urls.append(url_template.format(page+1))
        else:
            urls.append(handler(url_template, page))
    return urls


def build_sql(fields, table):
    # insert into chips(id, name, sex) values (%s, %s, %s)
    sql = (f"insert into {table} ({','.join(fields)}) "
           f"values({','.join(['%s'] * len(fields))})")
    return sql





