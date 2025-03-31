"""
@author: Nigo
@desc:
"""


from utils import utils


def run():
    processes = utils.build_processes()
    [process.start() for process in processes]
    [process.join() for process in processes]
