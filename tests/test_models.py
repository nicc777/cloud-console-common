import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
print('sys.path={}'.format(sys.path))

import unittest


from cloud_console_common.models import *


class TestDataObjectCacheModel(unittest.TestCase):

    def test_data_object_cache_basic_init_success(self):
        result = DataObjectCache(identifier='abc')
        self.assertIsNotNone(result)
        self.assertIsInstance(result, DataObjectCache)
        self.assertEqual(result.identifier, 'abc')
        self.assertEqual(result.last_called_timestamp_utc, 0)
        self.assertIsInstance(result.raw_result, dict)
        self.assertEqual(len(result.raw_result), 0)

    def test_data_object_cache_basic_init_with_null_identified_throws_exception(self):
        self.assertRaises(Exception, lambda:DataObjectCache(identifier=None))
        


if __name__ == '__main__':
    unittest.main()
