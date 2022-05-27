import unittest

from metainfo.MetaInfo import MetaInfo


class MetaInfoTestCase(unittest.TestCase):

    def test_should_obtain_version_and_description_from_dev_environment(self):
        meta_info = MetaInfo('persuader-technology-automata-meta-info')
        version = meta_info.get_version()
        description = meta_info.get_description()
        self.assertRegex(version, r'^\d+\.\d+\.\d+$')
        self.assertEqual(description, 'Automata Meta Info')

    def test_should_override_dev_path_location_of_setup_file(self):
        meta_info = MetaInfo('persuader-technology-automata-meta-info', '..')
        version = meta_info.get_version()
        description = meta_info.get_description()
        self.assertRegex(version, r'^\d+\.\d+\.\d+$')
        self.assertEqual(description, 'Automata Meta Info')


if __name__ == '__main__':
    unittest.main()
