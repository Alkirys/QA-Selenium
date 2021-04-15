import unittest
import sys
from tests.profile.check_auth import CheckAuth
from tests.film_popup.check_serial_popup import CheckSerialPopup
from tests.film_popup.check_film_popup import CheckFilmPopup
from tests.infoblock_film.check_infoblock import CheckInfoblock
from tests.my_list.check_my_list import CheckMyList

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(CheckAuth),
        unittest.makeSuite(CheckSerialPopup),
        unittest.makeSuite(CheckFilmPopup),
        unittest.makeSuite(CheckInfoblock),
        unittest.makeSuite(CheckMyList),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
