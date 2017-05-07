import json
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


# TODO async
def gallery_json_loader(path):
    logger.debug('Trying to open file: {}'.format(path))
    with open(path, 'r+') as f:
        # TODO async
        loaded_json = json.load(f)
        #logger.debug('Loaded Json: {}'.format(loaded_json))
        return loaded_json
