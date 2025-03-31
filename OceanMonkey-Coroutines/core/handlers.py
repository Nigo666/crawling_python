"""
@author: Nigo
@desc:
"""

import datetime


def generate_sh_futures_url(url_template, day):
    today = datetime.datetime.today()
    dt = today - datetime.timedelta(days=day)
    dt_str = dt.strftime("%Y%m%d")
    return url_template.format(dt_str)
