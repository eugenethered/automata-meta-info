import unittest

from metainfo.environment.DevEnvironmentMetaInfo import DevEnvironmentMetaInfo
from metainfo.exception.PackageFileNotFoundError import PackageFileNotFoundError


class DevEnvironmentMetaInfoTestCase(unittest.TestCase):

    def setUp(self):
        self.test_default_path = '../../'

    def test_should_have_setup_file(self):
        meta_info = DevEnvironmentMetaInfo(default_path=self.test_default_path)
        self.assertTrue(meta_info.setup_file_exists())

    def test_should_not_find_setup_file_using_default_path(self):
        with self.assertRaises(PackageFileNotFoundError):
            DevEnvironmentMetaInfo()

    def test_should_get_version_from_setup(self):
        meta_info = DevEnvironmentMetaInfo(default_path=self.test_default_path)
        result = meta_info.get_version()
        self.assertRegex(result, r'\d\.\d\.\d')

    def test_should_get_description_from_setup(self):
        meta_info = DevEnvironmentMetaInfo(default_path=self.test_default_path)
        result = meta_info.get_description()
        self.assertEqual(result, 'Automata Meta Info', 'Using actual description so check setup.cfg file')


if __name__ == '__main__':
    unittest.main()
