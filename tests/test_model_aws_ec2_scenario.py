import sys
import os
from datetime import datetime
from dateutil.tz import tzutc
import copy
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
print('sys.path={}'.format(sys.path))

import unittest


from cloud_console_common.models import *


class MockBoto3Ec2Client:
    
    def describe_instances(self)->dict:
        return {
            'Reservations': [
                {
                    'Groups': [], 
                    'Instances': [  # Reservations[].Instances[]
                        {
                            'AmiLaunchIndex': 0, 
                            'ImageId': 'ami-0a8c5ad81884f3891', 
                            'InstanceId': 'i-00000000000000000', 
                            'InstanceType': 't3.micro', 
                            'KeyName': 'dummy-key', 
                            'LaunchTime': datetime(2021, 11, 28, 11, 32, 25, tzinfo=tzutc()), 
                            'Monitoring': {
                                'State': 'disabled'
                            }, 
                            'Placement': {
                                'AvailabilityZone': 'eu-central-1a', 
                                'GroupName': '', 
                                'Tenancy': 'default'
                            }, 
                            'PrivateDnsName': 'ip-192-168-5-209.eu-central-1.compute.internal', 
                            'PrivateIpAddress': '192.168.5.209', 
                            'ProductCodes': [], 
                            'PublicDnsName': '', 
                            'State': {  # Reservations[].Instances[].State
                                'Code': 80,         # Reservations[].Instances[].State.Code
                                'Name': 'stopped'   # Reservations[].Instances[].State.Name
                            }, 
                            'StateTransitionReason': 'User initiated (2021-12-01 05:41:59 GMT)', 
                            'SubnetId': 'subnet-00000000000000000', 
                            'VpcId': 'vpc-00000000000000000', 
                            'Architecture': 'x86_64', 
                            'BlockDeviceMappings': [
                                {
                                    'DeviceName': '/dev/xvda', 
                                    'Ebs': {
                                        'AttachTime': datetime(2021, 11, 28, 11, 32, 26, tzinfo=tzutc()), 
                                        'DeleteOnTermination': True, 
                                        'Status': 'attached', 
                                        'VolumeId': 'vol-00000000000000000'
                                    }
                                }
                            ], 
                            'ClientToken': '', 
                            'EbsOptimized': True, 
                            'EnaSupport': True, 
                            'Hypervisor': 'xen', 
                            'IamInstanceProfile': {
                                'Arn': 'arn:aws:iam::000000000000:instance-profile/eksworkshop-admin', 
                                'Id': 'AAAAAAAAAAAAAAAAAAAAA'
                            }, 
                            'NetworkInterfaces': [
                                {
                                    'Attachment': {
                                        'AttachTime': datetime(2021, 11, 28, 11, 32, 25, tzinfo=tzutc()), 
                                        'AttachmentId': 'eni-attach-00000000000000000', 
                                        'DeleteOnTermination': True, 
                                        'DeviceIndex': 0, 
                                        'Status': 'attached', 
                                        'NetworkCardIndex': 0
                                    }, 
                                    'Description': 'Primary network interface', 
                                    'Groups': [
                                        {
                                            'GroupName': 'default', 
                                            'GroupId': 'sg-00000000000000000'
                                        }
                                    ], 
                                    'Ipv6Addresses': [], 
                                    'MacAddress': '02:c8:fc:ea:87:f0', 
                                    'NetworkInterfaceId': 'eni-00000000000000000', 
                                    'OwnerId': '000000000000', 
                                    'PrivateDnsName': 'ip-192-168-5-209.eu-central-1.compute.internal', 
                                    'PrivateIpAddress': '192.168.5.209', 
                                    'PrivateIpAddresses': [
                                        {
                                            'Primary': True, 
                                            'PrivateDnsName': 'ip-192-168-5-209.eu-central-1.compute.internal', 
                                            'PrivateIpAddress': '192.168.5.209'
                                        }
                                    ], 
                                    'SourceDestCheck': True, 
                                    'Status': 'in-use', 
                                    'SubnetId': 'subnet-00000000000000000', 
                                    'VpcId': 'vpc-00000000000000000', 
                                    'InterfaceType': 'interface'
                                }
                            ], 
                            'RootDeviceName': '/dev/xvda', 
                            'RootDeviceType': 'ebs', 
                            'SecurityGroups': [
                                {
                                    'GroupName': 'default', 
                                    'GroupId': 'sg-00000000000000000'
                                }
                            ], 
                            'SourceDestCheck': True, 
                            'StateReason': {
                                'Code': 'Client.UserInitiatedShutdown', 
                                'Message': 'Client.UserInitiatedShutdown: User initiated shutdown'
                            }, 
                            'Tags': [
                                {
                                    'Key': 'Name', 
                                    'Value': 'machine-01'
                                }
                            ], 
                            'VirtualizationType': 'hvm', 
                            'CpuOptions': {
                                'CoreCount': 1, 
                                'ThreadsPerCore': 2
                            }, 
                            'CapacityReservationSpecification': {
                                'CapacityReservationPreference': 'open'
                            }, 
                            'HibernationOptions': {
                                'Configured': False
                            }, 
                            'MetadataOptions': {
                                'State': 'applied', 
                                'HttpTokens': 'optional', 
                                'HttpPutResponseHopLimit': 1, 
                                'HttpEndpoint': 'enabled', 
                                'HttpProtocolIpv6': 'disabled'
                            }, 
                            'EnclaveOptions': {
                                'Enabled': False
                            }, 
                            'PlatformDetails': 'Linux/UNIX', 
                            'UsageOperation': 'RunInstances', 
                            'UsageOperationUpdateTime': datetime(2021, 11, 28, 11, 32, 25, tzinfo=tzutc()), 
                            'PrivateDnsNameOptions': {
                                'HostnameType': 'ip-name', 
                                'EnableResourceNameDnsARecord': True, 
                                'EnableResourceNameDnsAAAARecord': False
                            }
                        }
                    ], 
                    'OwnerId': '000000000000', 
                    'ReservationId': 'r-00000000000000000'
                }, 
                {
                    'Groups': [], 
                    'Instances': [
                        {
                            'AmiLaunchIndex': 0, 
                            'ImageId': 'ami-0bd99ef9eccfee250', 
                            'InstanceId': 'i-11111111111111111', 
                            'InstanceType': 
                            't2.micro', 
                            'KeyName': 'dummy-key', 
                            'LaunchTime': datetime(2021, 11, 28, 11, 18, 46, tzinfo=tzutc()), 
                            'Monitoring': {
                                'State': 'disabled'
                            }, 
                            'Placement': {
                                'AvailabilityZone': 'eu-central-1c', 
                                'GroupName': '', 
                                'Tenancy': 'default'
                            }, 
                            'PrivateDnsName': 'ip-172-31-1-186.eu-central-1.compute.internal', 
                            'PrivateIpAddress': '172.31.1.186', 
                            'ProductCodes': [], 
                            'PublicDnsName': '', 
                            'State': {
                                'Code': 80, 
                                'Name': 'stopped'
                            }, 
                            'StateTransitionReason': 'User initiated (2021-11-28 11:26:46 GMT)', 
                            'SubnetId': 'subnet-11111111', 
                            'VpcId': 'vpc-11111111', 
                            'Architecture': 'x86_64', 
                            'BlockDeviceMappings': [
                                {
                                    'DeviceName': '/dev/xvda', 
                                    'Ebs': {
                                        'AttachTime': datetime(2021, 11, 28, 11, 2, 12, tzinfo=tzutc()), 
                                        'DeleteOnTermination': True, 
                                        'Status': 'attached', 
                                        'VolumeId': 'vol-11111111111111111'
                                    }
                                }
                            ], 
                            'ClientToken': '', 
                            'EbsOptimized': False, 
                            'EnaSupport': True, 
                            'Hypervisor': 
                            'xen', 'IamInstanceProfile': {
                                'Arn': 'arn:aws:iam::000000000000:instance-profile/eksworkshop-admin', 
                                'Id': 'AAAAAAAAAAAAAAAAAAAAA'
                            }, 
                            'NetworkInterfaces': [
                                {
                                    'Attachment': {
                                        'AttachTime': datetime(2021, 11, 28, 11, 2, 11, tzinfo=tzutc()), 
                                        'AttachmentId': 'eni-attach-11111111111111111', 
                                        'DeleteOnTermination': True, 
                                        'DeviceIndex': 0, 
                                        'Status': 'attached', 
                                        'NetworkCardIndex': 0
                                    }, 
                                    'Description': '', 
                                    'Groups': [
                                        {
                                            'GroupName': 'test1-sg', 
                                            'GroupId': 'sg-11111111111111111'
                                        }
                                    ], 
                                    'Ipv6Addresses': [], 
                                    'MacAddress': '0a:54:53:6c:d2:5e', 
                                    'NetworkInterfaceId': 'eni-11111111111111111', 
                                    'OwnerId': '000000000000', 
                                    'PrivateDnsName': 'ip-172-31-1-186.eu-central-1.compute.internal', 
                                    'PrivateIpAddress': '172.31.1.186', 
                                    'PrivateIpAddresses': [
                                        {
                                            'Primary': True, 
                                            'PrivateDnsName': 'ip-172-31-1-186.eu-central-1.compute.internal', 
                                            'PrivateIpAddress': '172.31.1.186'
                                        }
                                    ], 
                                    'SourceDestCheck': True, 
                                    'Status': 'in-use', 
                                    'SubnetId': 'subnet-11111111', 
                                    'VpcId': 'vpc-11111111', 
                                    'InterfaceType': 'interface'
                                }
                            ], 
                            'RootDeviceName': '/dev/xvda', 
                            'RootDeviceType': 'ebs', 
                            'SecurityGroups': [
                                {
                                    'GroupName': 'test1-sg', 
                                    'GroupId': 'sg-11111111111111111'
                                }
                            ], 
                            'SourceDestCheck': True, 
                            'StateReason': {
                                'Code': 'Client.UserInitiatedShutdown', 
                                'Message': 'Client.UserInitiatedShutdown: User initiated shutdown'
                            }, 
                            'Tags': [
                                {
                                    'Key': 'Name', 
                                    'Value': 'machine-02'
                                }
                            ], 
                            'VirtualizationType': 'hvm', 
                            'CpuOptions': {
                                'CoreCount': 1, 
                                'ThreadsPerCore': 1
                            }, 
                            'CapacityReservationSpecification': {
                                'CapacityReservationPreference': 'open'
                            }, 
                            'HibernationOptions': {
                                'Configured': False
                            }, 
                            'MetadataOptions': {
                                'State': 'applied', 
                                'HttpTokens': 'optional', 
                                'HttpPutResponseHopLimit': 1, 
                                'HttpEndpoint': 'enabled', 
                                'HttpProtocolIpv6': 'disabled'
                            }, 
                            'EnclaveOptions': {
                                'Enabled': False
                            }, 
                            'PlatformDetails': 'Linux/UNIX', 
                            'UsageOperation': 'RunInstances', 
                            'UsageOperationUpdateTime': datetime(2021, 11, 28, 11, 2, 11, tzinfo=tzutc()), 
                            'PrivateDnsNameOptions': {
                                'HostnameType': 'ip-name', 
                                'EnableResourceNameDnsARecord': True, 
                                'EnableResourceNameDnsAAAARecord': False
                            }
                        }
                    ], 
                    'OwnerId': '000000000000', 
                    'ReservationId': 'r-11111111111111111'
                }, 
                {
                    'Groups': [], 
                    'Instances': [
                        {
                            'AmiLaunchIndex': 0, 
                            'ImageId': 'ami-06c7e3ecba3661a89', 
                            'InstanceId': 'i-22222222222222222', 
                            'InstanceType': 't4g.micro', 
                            'KeyName': 'dummy-key', 
                            'LaunchTime': datetime(2021, 11, 28, 10, 47, 27, tzinfo=tzutc()), 
                            'Monitoring': {
                                'State': 'disabled'
                            }, 
                            'Placement': {
                                'AvailabilityZone': 'eu-central-1c', 
                                'GroupName': '', 
                                'Tenancy': 'default'
                            }, 
                            'PrivateDnsName': 'ip-172-31-10-249.eu-central-1.compute.internal', 
                            'PrivateIpAddress': '172.31.10.249', 
                            'ProductCodes': [], 
                            'PublicDnsName': '', 
                            'State': {
                                'Code': 80, 
                                'Name': 'stopped'
                            }, 
                            'StateTransitionReason': 'User initiated (2021-12-01 05:41:59 GMT)', 
                            'SubnetId': 'subnet-11111111', 
                            'VpcId': 'vpc-11111111', 
                            'Architecture': 'arm64', 
                            'BlockDeviceMappings': [
                                {
                                    'DeviceName': '/dev/xvda', 
                                    'Ebs': {
                                        'AttachTime': datetime(2021, 11, 28, 10, 47, 28, tzinfo=tzutc()), 
                                        'DeleteOnTermination': True, 
                                        'Status': 'attached', 
                                        'VolumeId': 'vol-22222222222222222'
                                    }
                                }
                            ], 
                            'ClientToken': '', 
                            'EbsOptimized': True, 
                            'EnaSupport': True, 
                            'Hypervisor': 'xen', 
                            'NetworkInterfaces': [
                                {
                                    'Attachment': {
                                        'AttachTime': datetime(2021, 11, 28, 10, 47, 27, tzinfo=tzutc()), 
                                        'AttachmentId': 'eni-attach-22222222222222222', 
                                        'DeleteOnTermination': True, 
                                        'DeviceIndex': 0, 
                                        'Status': 'attached', 
                                        'NetworkCardIndex': 0
                                    }, 
                                    'Description': '', 
                                    'Groups': [
                                        {
                                            'GroupName': 'default', 
                                            'GroupId': 'sg-22222222'
                                        }
                                    ], 
                                    'Ipv6Addresses': [], 
                                    'MacAddress': '0a:89:b0:33:55:9a', 
                                    'NetworkInterfaceId': 'eni-22222222222222222', 
                                    'OwnerId': '000000000000', 
                                    'PrivateDnsName': 'ip-172-31-10-249.eu-central-1.compute.internal', 
                                    'PrivateIpAddress': '172.31.10.249', 
                                    'PrivateIpAddresses': [
                                        {
                                            'Primary': True, 
                                            'PrivateDnsName': 'ip-172-31-10-249.eu-central-1.compute.internal', 
                                            'PrivateIpAddress': '172.31.10.249'
                                        }
                                    ], 
                                    'SourceDestCheck': True, 
                                    'Status': 'in-use', 
                                    'SubnetId': 'subnet-11111111', 
                                    'VpcId': 'vpc-11111111', 
                                    'InterfaceType': 'interface'
                                }
                            ], 
                            'RootDeviceName': '/dev/xvda', 
                            'RootDeviceType': 'ebs', 
                            'SecurityGroups': [
                                {
                                    'GroupName': 'default', 
                                    'GroupId': 'sg-22222222'
                                }
                            ], 
                            'SourceDestCheck': True, 
                            'StateReason': {
                                'Code': 'Client.UserInitiatedShutdown', 
                                'Message': 'Client.UserInitiatedShutdown: User initiated shutdown'
                            }, 
                            'Tags': [
                                {
                                    'Key': 'Name', 
                                    'Value': 'machine-03'
                                }
                            ], 
                            'VirtualizationType': 'hvm', 
                            'CpuOptions': {
                                'CoreCount': 2, 
                                'ThreadsPerCore': 1
                            }, 
                            'CapacityReservationSpecification': {
                                'CapacityReservationPreference': 'open'
                            }, 
                            'HibernationOptions': {
                                'Configured': False
                            }, 
                            'MetadataOptions': {
                                'State': 'applied', 
                                'HttpTokens': 'optional', 
                                'HttpPutResponseHopLimit': 1, 
                                'HttpEndpoint': 'enabled', 
                                'HttpProtocolIpv6': 'disabled'
                            }, 
                            'EnclaveOptions': {
                                'Enabled': False
                            }, 
                            'BootMode': 'uefi', 
                            'PlatformDetails': 'Linux/UNIX', 
                            'UsageOperation': 'RunInstances', 
                            'UsageOperationUpdateTime': datetime(2021, 11, 28, 10, 47, 27, tzinfo=tzutc()), 
                            'PrivateDnsNameOptions': {
                                'HostnameType': 'ip-name', 
                                'EnableResourceNameDnsARecord': True, 
                                'EnableResourceNameDnsAAAARecord': False
                            }
                        }
                    ], 
                    'OwnerId': '000000000000', 
                    'ReservationId': 'r-22222222222222222'
                }
            ], 
            'ResponseMetadata': {
                'RequestId': '00000000-0000-0000-0000-000000000000', 
                'HTTPStatusCode': 200, 
                'HTTPHeaders': {
                    'x-amzn-requestid': '00000000-0000-0000-0000-000000000000', 
                    'cache-control': 'no-cache, no-store', 
                    'strict-transport-security': 'max-age=31536000; includeSubDomains', 
                    'vary': 'accept-encoding', 
                    'content-type': 'text/xml;charset=UTF-8', 
                    'transfer-encoding': 'chunked', 
                    'date': 'Mon, 20 Dec 2021 07:42:29 GMT', 
                    'server': 'AmazonEC2'
                }, 
                'RetryAttempts': 0
            }
        }


class InstanceStateExtractLogic(ExtractLogic):

    def extract(self, raw_data)->dict:
        """
            Expecting a dict with the Instance data - # Reservations[].Instances[].raw_data with the following in raw_data:

            'State': {
                'Code': 80,
                'Name': 'stopped'
            }, 
        """
        state = dict()
        state['Code'] = None
        state['Name'] = 'unknown'
        if 'State' in raw_data:
            state = raw_data['State']
        return state


class InstanceNameExtractLogic(ExtractLogic):

    def extract(self, raw_data)->dict:
        """
            Expecting a dict with the Instance data - # Reservations[].Instances[].raw_data with the following in raw_data:

            'Tags': [
                {
                    'Key': 'Name', 
                    'Value': 'machine-01'
                }
            ], 
        """
        name_data = dict()
        name_value = '-'
        for tag_data in raw_data['Tags']:
            if tag_data['Key'] == 'Name':
                name_value = tag_data['Value']
        name_data['Name'] = name_value
        return name_data


class InstanceExtractLogic(ExtractLogic):

    def extract(self, raw_data)->dict:
        # Expecting the raw response from the AWS EC2 API call "describe-instances"  - Reservations[].Instances[].raw_data
        instances = dict()
        for reservation in raw_data['Reservations']:
            for instance in reservation['Instances']:
                instances[instance['InstanceId']] = copy.deepcopy(instance)
        return instances


class TestExtractLogicClasses(unittest.TestCase):

    def setUp(self):
        self.client = MockBoto3Ec2Client()
        self.root_raw_data = self.client.describe_instances()
        self.instance_1 = self.root_raw_data['Reservations'][0]['Instances'][0]

    def test_instance_extract_logic(self):
        c = InstanceExtractLogic()
        data = c.extract(self.root_raw_data)
        self.assertIsNotNone(data)
        self.assertIsInstance(data, dict)
        self.assertEqual(len(data), 3)
        self.assertTrue('i-00000000000000000' in data)
        self.assertTrue('i-11111111111111111' in data)
        self.assertTrue('i-22222222222222222' in data)

    def test_instance_name_extract_logic(self):
        c = InstanceNameExtractLogic()
        data = c.extract(raw_data=self.instance_1)
        self.assertIsNotNone(data)
        self.assertIsInstance(data, dict)
        self.assertEqual(len(data), 1)
        self.assertTrue('Name' in data)
        self.assertIsInstance(data['Name'], str)
        self.assertFalse(data['Name'] == '-')
        self.assertTrue(len(data['Name']) > 1)
    
    def test_instance_state_extract_logic(self):
        c = InstanceStateExtractLogic()
        data = c.extract(raw_data=self.instance_1)
        self.assertIsNotNone(data)
        self.assertIsInstance(data, dict)
        self.assertEqual(len(data), 2)
        self.assertEqual(data['Code'], 80)
        self.assertEqual(data['Name'], 'stopped')


class TestAwsEc2Scenario(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()

# EOF
