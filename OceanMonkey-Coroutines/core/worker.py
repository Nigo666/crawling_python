"""
@author: Nigo
@desc:
"""

from utils.logger import logger
from utils import utils
import os
import pandas as pd
from configure import settings
from dal import database
import asyncio


async def main(urls, file_name, fetch_callback, parse_callback, save_callback=None):

    tasks = [fetch_callback(url) for url in urls]
    results = await asyncio.gather(*tasks)
    data = []
    for result in results:
        item = parse_callback(result)
        data.extend(item)

    if save_callback:
        save_file_path = os.path.join(settings.DATA_DIRECTORY, f"{file_name}.xlsx")
        db_conn = database.build_db_conn()
        save_callback(db_conn, data, save_file_path)


def worker(*args):
    pid = os.getpid()
    (url_template, pages, url_generator, crawling_func,
     parse_func, save_func, name) = args
    logger.info(f"pid:{pid}"
                f"url template:{url_template}, "
                f"pages:{pages}")
    urls = utils.generates_urls(url_template, pages, handler=url_generator)
    asyncio.run(main(urls, name, crawling_func, parse_func, save_func))


