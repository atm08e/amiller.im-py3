import json
# TODO async json
import logging
import os
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


def gallery_json_loader(path):
    logger.debug('Trying to open file: {}'.format(path))
    with open(path, 'r+') as f:
        # TODO async
        loaded_json = json.load(f)
        #logger.debug('Loaded Json: {}'.format(loaded_json))
        return loaded_json


def setup_galleries(path_to_static):
    # TODO this is shit, there is a better way to do this
    return {
        'snowboarding':
            {
                '2016':
                    {
                        '1': gallery_json_loader(
                                os.path.join(path_to_static,
                                             *['galleries', 'snowboarding', '2016', 'wreckbreck2016.json'])),
                        '2': gallery_json_loader(
                                os.path.join(path_to_static,
                                             *['galleries', 'snowboarding', '2016', 'familybreck2016.json']))
                    },
                '2017':
                    {
                        '1': gallery_json_loader(
                                os.path.join(path_to_static,
                                             *['galleries', 'snowboarding', '2017', 'wreckbreck2017.json'])),
                        '2': gallery_json_loader(
                                os.path.join(path_to_static,
                                             *['galleries', 'snowboarding', '2017', 'shredapalooza2017.json'])),
                        '3': gallery_json_loader(
                                os.path.join(path_to_static,
                                             *['galleries', 'snowboarding', '2017', 'ibelieveinspringbreak2017.json'])),
                    }
            },
        'boating':
            {
                '2016':
                    {
                        '1': gallery_json_loader(
                                os.path.join(path_to_static,
                                             *['galleries', 'boating', '2016', 'fishing-jan-2016.json'])),

                        '2': gallery_json_loader(
                                os.path.join(path_to_static,
                                             *['galleries', 'boating', '2016', 'airshow-2016.json'])),

                        '3': gallery_json_loader(
                                os.path.join(path_to_static,
                                             *['galleries', 'boating', '2016', 'fishing-dad-grandpa-july-2016.json'])),
                        '4': gallery_json_loader(
                                os.path.join(path_to_static,
                                             *['galleries', 'boating', '2016', 'miniseason-2016.json']))
                    }
            }
    }
