import logging

import sys

from aiohttp.test_utils import  AioHTTPTestCase, unittest_run_loop

from amiller_im import AmillerIm

logging.basicConfig(stream=sys.stdout, level=logging.debug)
logger = logging.getLogger(__name__)

class AmillerImTestCases(AioHTTPTestCase):

    def get_app(self):
        return AmillerIm.get_app()

    def setUp(self):
        super(AmillerImTestCases, self).setUp()

    def tearDown(self):
        super(AmillerImTestCases, self).tearDown()

    @unittest_run_loop
    async def test_root(self):
        req = await self.client.request('GET', '/')