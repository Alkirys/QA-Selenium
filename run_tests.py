import unittest
import sys
from tests.profile.check_auth import CheckAuth
from tests.main.check_main import CheckMain
from tests.search.check_search import CheckSearch
from tests.content.check_content import CheckContent


if __name__ == '__main__':
    suite = unittest.TestSuite((
       unittest.makeSuite(CheckAuth),
       unittest.makeSuite(CheckMain),
       unittest.makeSuite(CheckSearch),
       unittest.makeSuite(CheckContent),
    ))
    result = unittest.TextTestRunner().run(suite)

    sys.exit(not result.wasSuccessful())