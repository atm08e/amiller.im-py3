import logging

import sys

from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

from app.main import create_app

logging.basicConfig(stream=sys.stdout, level=logging.debug)
logger = logging.getLogger(__name__)


class AmillerImTestCases(AioHTTPTestCase):

    def get_app(loop):
        return create_app(loop)

    def setUp(self):
        super(AmillerImTestCases, self).setUp()

    def tearDown(self):
        super(AmillerImTestCases, self).tearDown()

    @unittest_run_loop
    async def test_root(self):
        # Sanity Smoke Test
        req = await self.client.request('GET', '/')
