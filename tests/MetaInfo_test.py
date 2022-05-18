import unittest

from metainfo.MetaInfo import MetaInfo
from metainfo.exception.MetaInfoMissingError import MetaInfoMissingError
from metainfo.exception.PackageFileNotFoundError import PackageFileNotFoundError


class MetaInfoTestCase(unittest.TestCase):

    def test_should_get_version_from_package_module_init_file(self):
        meta_info = MetaInfo(default_path='../metainfo')
        version = meta_info.get_version()
        self.assertEqual(version, '0.0.1')

    def test_should_get_description_from_package_module_init_file(self):
        meta_info = MetaInfo(default_path='../metainfo')
        description = meta_info.get_description()
        self.assertEqual(description, 'Automata Meta Info')

    def test_should_should_raise_exception_when_meta_info_file_not_present(self):
        with self.assertRaises(PackageFileNotFoundError):
            MetaInfo(meta_file='__non_existent__.py')

    def test_should_should_raise_exception_when_version_not_set(self):
        with self.assertRaises(MetaInfoMissingError):
            meta_info = MetaInfo()
            meta_info.get_version()


if __name__ == '__main__':
    unittest.main()
