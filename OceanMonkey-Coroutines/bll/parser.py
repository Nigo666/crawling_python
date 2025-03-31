"""
@author: Nigo
@desc:
"""
import json
from  lxml import  etree
from  configure import  settings


def parse_east_money_share(text):
    try:
        data = json.loads(text[text.find("{"):-2])
        diff = data.get("data", {}).get("diff", [])
    except (Exception,):
        diff = []
    return diff


def parse_sh_future(json_data):
    try:
        contract_base_info = json_data.get("ContractBaseInfo", [])
    except (Exception,):
        contract_base_info = []
    return contract_base_info
def parse_drugs(text):
    drugs = []
    etree_parser = etree.HTML(text)
    names_specs = [name for name in etree_parser.xpath(settings.names_xpath) if name.strip() != '']
    prices = etree_parser.xpath(settings.prices_xpath)[7:]
    prices = [price for price in prices if price.strip() != '']

    for index in range(0, len(names_specs), 2):
        drug = names_specs[index:index + 2]
        index = index * 3
        drug.extend(prices[index:index + 6])
        drugs.append(drug)
    return drugs