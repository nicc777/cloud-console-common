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


class TestDataPointBase(unittest.TestCase):

    def test_data_point_base_basic_init_success(self):
        result = DataPointBase(name='abc')
        self.assertIsNotNone(result)
        self.assertIsInstance(result, DataPointBase)
        self.assertEqual(result.name, 'abc')

    def test_data_point_base_basic_init_with_null_name_throws_exception(self):
        self.assertRaises(Exception, lambda:DataPointBase(name=None))

    def test_data_point_base_basic_init_with_invalid_type_name_throws_exception(self):
        self.assertRaises(Exception, lambda:DataPointBase(name=123))

    def test_data_point_base_basic_init_with_empty_string_name_throws_exception(self):
        self.assertRaises(Exception, lambda:DataPointBase(name=''))

    def test_data_point_base_with_label_success(self):
        result = DataPointBase(name='abc', label='xyz')
        self.assertIsNotNone(result)
        self.assertIsInstance(result, DataPointBase)
        self.assertEqual(result.name, 'abc')
        self.assertEqual(result.label, 'xyz')

    def test_data_point_base_basic_init_with_invalid_type_label_throws_exception(self):
        self.assertRaises(Exception, lambda:DataPointBase(name='abc', label=123))

    def test_data_point_base_basic_init_with_empty_string_label_throws_exception(self):
        self.assertRaises(Exception, lambda:DataPointBase(name='abc', label=''))

    def test_data_point_base_basic_init_with_to_long_string_label_throws_exception(self):
        self.assertRaises(Exception, lambda:DataPointBase(name='abc', label='x'*33))
        

class TestDataPoint(unittest.TestCase):

    def test_data_point_basic_init_success(self):
        result = DataPoint(name='abc')
        self.assertIsNotNone(result)
        self.assertIsInstance(result, DataPointBase)
        self.assertEqual(result.name, 'abc')

    def test_method_add_child_data_point_basic_success(self):
        result = DataPoint(name='parent')
        self.assertIsNotNone(result)
        self.assertIsInstance(result, DataPointBase)
        self.assertEqual(result.name, 'parent')
        child = DataPoint(name='child')
        self.assertIsNotNone(child)
        self.assertIsInstance(child, DataPointBase)
        self.assertEqual(child.name, 'child')
        result.add_child_data_point(data_point=child)
        children = result.children_data_points
        self.assertIsNotNone(children)
        self.assertIsInstance(children, dict)
        self.assertEqual(len(children), 1)
        self.assertTrue('child' in children)

    def test_method_add_child_data_point_none_val_do_nothing(self):
        result = DataPoint(name='parent')
        self.assertIsNotNone(result)
        self.assertIsInstance(result, DataPointBase)
        self.assertEqual(result.name, 'parent')
        result.add_child_data_point(data_point=None)
        children = result.children_data_points
        self.assertIsNotNone(children)
        self.assertIsInstance(children, dict)
        self.assertEqual(len(children), 0)

    def test_method_add_child_data_point_wrong_type_do_nothing(self):
        result = DataPoint(name='parent')
        self.assertIsNotNone(result)
        self.assertIsInstance(result, DataPointBase)
        self.assertEqual(result.name, 'parent')
        result.add_child_data_point(data_point=12345)
        children = result.children_data_points
        self.assertIsNotNone(children)
        self.assertIsInstance(children, dict)
        self.assertEqual(len(children), 0)


class MockExtractLogic01(ExtractLogic):

    def extract(self, raw_data)->dict:
        if 'test' in raw_data:
            return {'test_found': True}
        else:
            return {'test_found': False}


class MockRemoteCallLogic(RemoteCallLogic):

    def execute(self)->dict:
        fake_api_call_results = {'test': 123}
        return fake_api_call_results


class TestDataPointExtractLogic(unittest.TestCase):

    def test_data_point_extract_logic_basic_init_success(self):
        result = DataPointExtractLogic(
            name='get_aws_ec2_instances',
            data_point=DataPoint(name='ec2_instances', label='awc_ec2_instances'),
            extract_implementation=MockExtractLogic01(),
            remote_call_implementation=MockRemoteCallLogic()
        )
        self.assertIsNotNone(result)
        self.assertIsInstance(result, DataPointExtractLogic)
        self.assertEqual(result.name, 'get_aws_ec2_instances')
        data_point_value = result.get_data_point(return_only_value=True)
        self.assertIsNotNone(data_point_value)
        self.assertIsInstance(data_point_value, dict)
        self.assertTrue('test' in data_point_value)
        self.assertIsInstance(data_point_value['test_found'], bool)
        self.assertTrue(data_point_value['test_found'])



if __name__ == '__main__':
    unittest.main()

# EOF
