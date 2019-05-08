import json
# TODO async json
import logging
import os
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


def gallery_json_loader(path):
    logger.debug('Trying to open file: {}'.format(path))
    with open(path, 'r+', encoding='utf-8') as f:
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
                    },
                '2018':
                    {
                        '1': gallery_json_loader(
                            os.path.join(path_to_static,
                                         *['galleries', 'snowboarding', '2018', 'alpinemeadows2018.json'])),
                        '2': gallery_json_loader(
                            os.path.join(path_to_static,
                                         *['galleries', 'snowboarding', '2018', 'senditinvitational2018.json'])),
                        '3': gallery_json_loader(
                            os.path.join(path_to_static,
                                         *['galleries', 'snowboarding', '2018', 'sierraattahoe2018.json'])),
                        '4': gallery_json_loader(
                            os.path.join(path_to_static,
                                         *['galleries', 'snowboarding', '2018', 'whistlerblackcomb2018.json'])),
                        '5': gallery_json_loader(
                            os.path.join(path_to_static,
                                         *['galleries', 'snowboarding', '2018', 'wreckbreck2018.json']))
                    },
                '2019':
                    {
                        '1': gallery_json_loader(
                            os.path.join(path_to_static,
                                         *['galleries', 'snowboarding', '2019', 'whistler-dec-2019.json'])),
                        '2': gallery_json_loader(
                            os.path.join(path_to_static,
                                         *['galleries', 'snowboarding', '2019', 'colorado-solo-2019.json'])),
                        '3': gallery_json_loader(
                            os.path.join(path_to_static,
                                         *['galleries', 'snowboarding', '2019', 'wreck-breck-2019.json'])),
                        '4': gallery_json_loader(
                            os.path.join(path_to_static,
                                         *['galleries', 'snowboarding', '2019', 'shred-a-palooza-2019.json'])),
                        '5': gallery_json_loader(
                            os.path.join(path_to_static,
                                         *['galleries', 'snowboarding', '2019', 'heavenly-spring-2019.json'])),
                        '6': gallery_json_loader(
                            os.path.join(path_to_static,
                                         *['galleries', 'snowboarding', '2019', 'kirkwood-spring-2019.json']))
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
                    },
                '2017':
                    {

                        '1': gallery_json_loader(
                                os.path.join(path_to_static,
                                             *['galleries', 'boating', '2017', 'fishing-june-2017.json'])),
                        '2': gallery_json_loader(
                                os.path.join(path_to_static,
                                             *['galleries', 'boating', '2017', 'keys-july-2017.json'])),
                    }
            }
    }
