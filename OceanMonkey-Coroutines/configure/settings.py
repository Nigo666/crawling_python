"""
@author: Nigo
@desc:
"""
from pathlib import Path
import os
import logging
HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
}

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIRECTORY = os.path.join(ROOT_DIR, "data")
LOGGING_DIRECTORY = os.path.join(ROOT_DIR, "log")
LOGGING_LEVEL = logging.INFO

# 日志文件
LOGGING_FILE = os.path.join(LOGGING_DIRECTORY, "oceanmonkey.log")

from bll import crawler
from bll import parser
from bll import loader
from core import handlers
names_xpath = '//div[@class="price-list"]//td//a/text()'
prices_xpath = '//div[@class="price-list"]//td/text()'
SEEDS = {
    "east_money_US_share": {
        "url_template": 'https://push2.eastmoney.com/api/qt/clist/get?np=1&fltt=1&invt=2&cb=jQuery3710938326761399431_1741244459681&fs=b%3AMK0001&fields=f12%2Cf13%2Cf14%2Cf1%2Cf2%2Cf4%2Cf3%2Cf152%2Cf17%2Cf18%2Cf15%2Cf16%2Cf20%2Cf115&fid=f3&pn={}&pz=20&po=1&dect=1&ut=fa5fd1943c7b386f172d6893dbfba10b&wbp2u=%7C0%7C0%7C0%7Cweb&_=1741244459683',
        "pages": 100,
        "crawling_task": crawler.crawling_east_money_share,
        "parse_func": parser.parse_east_money_share,
        "save_func": loader.load_shares_2_db
    },
    "east_money_A_share": {
        "url_template": "https://push2.eastmoney.com/api/qt/clist/get?np=1&fltt=1&invt=2&cb=jQuery37103964269611528126_1741242954086&fs=m%3A1%2Bt%3A2%2Cm%3A1%2Bt%3A23&fields=f12%2Cf13%2Cf14%2Cf1%2Cf2%2Cf4%2Cf3%2Cf152%2Cf5%2Cf6%2Cf7%2Cf15%2Cf18%2Cf16%2Cf17%2Cf10%2Cf8%2Cf9%2Cf23&fid=f3&pn={}&pz=20&po=1&dect=1&ut=fa5fd1943c7b386f172d6893dbfba10b&wbp2u=%7C0%7C0%7C0%7Cweb&_=1741242954096",
        "pages": 100,
        "crawling_task": crawler.crawling_east_money_share,
        "parse_func": parser.parse_east_money_share,
        "save_func": loader.load_shares_2_db
    },
    "sh_futures": {
        "url_template": "https://www.shfe.com.cn/data/busiparamdata"
                        "/future/ContractBaseInfo{}.dat?params=1741143191046",
        "pages": 100,
        "url_generator": handlers.generate_sh_futures_url,
        "crawling_task": crawler.crawling_sh_future,
        "parse_func": parser.parse_sh_future,
        "save_func": loader.load_sh_futures_2_db
    },
    "drugs": {
        "url_template": "https://www.zyctd.com/jiage/1-0-0-{}.html",
        "pages": 100,
        "threads": 100,
        "crawling_task": crawler.crawling_drugs,
        "parse_func": parser.parse_drugs,
        "save_func":loader.load_drugs_2_db
    },
}

