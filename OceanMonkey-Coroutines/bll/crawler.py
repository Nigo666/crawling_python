"""
@author: Nigo
@desc:
"""
from utils.logger import logger
from configure import settings
import aiohttp


async def crawling_east_money_share(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=settings.HEADERS) as response:
            return await response.text()


async def crawling_sh_future(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=settings.HEADERS) as response:
            try:
                return await response.json()
            except (Exception, ):
                return None

async def crawling_drugs(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=settings.HEADERS) as response:
            try:
                return await response.text()
            except(Exception, ):
                return None



