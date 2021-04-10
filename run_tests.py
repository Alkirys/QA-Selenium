import unittest
import sys
from tests.profile.check_auth import CheckAuth


if __name__ == '__main__':
    suite = unittest.TestSuite((
       unittest.makeSuite(CheckAuth),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
