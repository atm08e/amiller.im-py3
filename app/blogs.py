import logging
import sys
import os
from pathlib import Path
#
from markdown import markdown

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


def blog_loader(path):
    logger.debug('Trying to open file and parse markdown: {}'.format(path))
    return markdown(Path(path).read_text(encoding='UTF-8'))


def setup_blogs(path_to_static):
    return {
        'movies':
            {
                'starwars': {
                    'header': 'Starwars series review',
                    'header3': 'The new Starwars series sucks, and it\'s Disney\'s and Jar Jar Abram\'s fault',
                    'date': '12/24/2017',
                    'content': blog_loader(os.path.join(path_to_static, *['blogs', 'movies', 'starwars.md']))
                }
            }
    }
