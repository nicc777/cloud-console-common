import sys
import os
import time
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
        self.assertIsNone(result.data_point)

    def test_data_object_cache_basic_init_with_null_identified_throws_exception(self):
        self.assertRaises(Exception, lambda:DataObjectCache(identifier=None))

    def test_data_object_cache_basic_init_update_results_throws_exception(self):
        result = DataObjectCache(identifier='abc')
        self.assertRaises(Exception, lambda:result.update_results(results={'test': 123}))

    def test_data_object_cache_basic_init_and_data_point_update(self):
        result = DataObjectCache(identifier='abc', data_point=DataPoint(name='xys'))
        result.update_results(results={'test': 123})
        self.assertIsNotNone(result.data_point)
        self.assertIsInstance(result.data_point, DataPoint)
        self.assertIsNotNone(result.data_point.value)
        self.assertIsInstance(result.data_point.value, dict)
        self.assertTrue('test' in result.data_point.value)
        self.assertEqual(result.data_point.value['test'], 123)

    def test_data_object_cache_update_results_with_none_does_nothing(self):
        data_point = DataPoint(name='xyz')
        data_point.value = {'test': 999}
        result = DataObjectCache(identifier='abc', data_point=data_point)
        result.update_results(results=None)
        self.assertIsNotNone(result.data_point)
        self.assertIsInstance(result.data_point, DataPoint)
        self.assertIsNotNone(result.data_point.value)
        self.assertIsInstance(result.data_point.value, dict)
        self.assertTrue('test' in result.data_point.value)
        self.assertEqual(result.data_point.value['test'], 999)

    def test_data_object_cache_update_results_with_incorrect_type_does_nothing(self):
        data_point = DataPoint(name='xyz')
        data_point.value = {'test': 999}
        result = DataObjectCache(identifier='abc', data_point=data_point)
        result.update_results(results=123)
        self.assertIsNotNone(result.data_point)
        self.assertIsInstance(result.data_point, DataPoint)
        self.assertIsNotNone(result.data_point.value)
        self.assertIsInstance(result.data_point.value, dict)
        self.assertTrue('test' in result.data_point.value)
        self.assertEqual(result.data_point.value['test'], 999)


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


class MockExtractLogicForMockRemoteCall(ExtractLogic):

    def extract(self, raw_data)->dict:
        if 'test' in raw_data:
            return raw_data
        raise Exception('Invalid Test Data')            


class MockMetaDataExtractLogic01(ExtractLogic):
    
    def extract(self, raw_data) -> dict:
        result = dict()
        if 'meta_data' in raw_data:
            result['isUnitTest'] = raw_data['meta_data']['isUnitTest']
        return result


class MockRemoteCallLogic(RemoteCallLogic):

    def execute(self)->dict:
        fake_api_call_results = {'test': 123, 'meta_data': { 'name': 'testName', 'isUnitTest': True, 'value': 123}}
        extract_results = self.extract_logic.extract(raw_data=fake_api_call_results)
        self.base_data = copy.deepcopy(extract_results)
        return fake_api_call_results


class MetaDataRemoteCallLogic(RemoteCallLogic):

    def execute(self)->dict:
        meta_data = self.extract_logic.extract(raw_data=copy.deepcopy(self.base_data))
        return meta_data


class TestDataObjectCache(unittest.TestCase):

    def setUp(self):
        self.remote_data_point = DataPoint(
            name='remote_mock',
            label='remote_mock',
            remote_call_logic=MockRemoteCallLogic(extract_logic=MockExtractLogicForMockRemoteCall())
        )
        md_data_point = DataPoint(
            name='meta_data',
            label='meta_data',
            remote_call_logic=MetaDataRemoteCallLogic(extract_logic=MockMetaDataExtractLogic01())
        )
        self.remote_data_point.add_child_data_point(data_point=md_data_point)

    def test_data_object_cache_basic(self):
        cache = DataObjectCache(identifier='mock_remote_test', data_point=self.remote_data_point)
        cache.refresh_cache(force=True)
        remote_data_point = None
        md_data_point = None
        self.assertIsNotNone(cache)
        remote_data_point = cache.data_point
        self.assertIsNotNone(remote_data_point)
        self.assertIsInstance(remote_data_point, DataPointBase)
        self.assertTrue('test' in remote_data_point.value)
        self.assertIsNotNone(remote_data_point.value['test'])
        self.assertIsInstance(remote_data_point.value['test'], int)
        self.assertEqual(remote_data_point.value['test'], 123)
        md_data_point = remote_data_point.get_child_by_name(name='meta_data')
        self.assertIsNotNone(md_data_point)
        self.assertIsInstance(md_data_point, DataPointBase)
        self.assertIsNotNone(md_data_point.value)
        self.assertIsInstance(md_data_point.value, dict)
        self.assertTrue('isUnitTest' in md_data_point.value)
        self.assertIsInstance(md_data_point.value['isUnitTest'], bool)
        self.assertTrue(md_data_point.value['isUnitTest'])

    def test_data_object_cache_second_refresh_no_remote_call(self):
        cache = DataObjectCache(identifier='mock_remote_test', data_point=self.remote_data_point)
        run_cache_01 = cache.refresh_cache()
        self.assertTrue(run_cache_01)
        self.assertEqual(cache.max_cache_lifetime, 300)
        run_cache_02 = cache.refresh_cache()
        self.assertFalse(run_cache_02)

        remote_data_point = cache.data_point
        self.assertIsNotNone(remote_data_point)
        self.assertIsInstance(remote_data_point, DataPointBase)
        self.assertTrue('test' in remote_data_point.value)
        self.assertIsNotNone(remote_data_point.value['test'])
        self.assertIsInstance(remote_data_point.value['test'], int)
        self.assertEqual(remote_data_point.value['test'], 123)
        md_data_point = remote_data_point.get_child_by_name(name='meta_data')
        self.assertIsNotNone(md_data_point)
        self.assertIsInstance(md_data_point, DataPointBase)
        self.assertIsNotNone(md_data_point.value)
        self.assertIsInstance(md_data_point.value, dict)
        self.assertTrue('isUnitTest' in md_data_point.value)
        self.assertIsInstance(md_data_point.value['isUnitTest'], bool)
        self.assertTrue(md_data_point.value['isUnitTest'])



if __name__ == '__main__':
    unittest.main()

# EOF
