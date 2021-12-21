import sys
import os
import datetime
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
                    'Instances': [
                        {
                            'AmiLaunchIndex': 0, 
                            'ImageId': 'ami-0a8c5ad81884f3891', 
                            'InstanceId': 'i-00000000000000000', 
                            'InstanceType': 't3.micro', 
                            'KeyName': 'dummy-key', 
                            'LaunchTime': datetime.datetime(2021, 11, 28, 11, 32, 25, tzinfo=tzutc()), 
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
                            'State': {
                                'Code': 80, 'Name': 'stopped'
                            }, 
                            'StateTransitionReason': 'User initiated (2021-12-01 05:41:59 GMT)', 
                            'SubnetId': 'subnet-00000000000000000', 
                            'VpcId': 'vpc-00000000000000000', 
                            'Architecture': 'x86_64', 
                            'BlockDeviceMappings': [
                                {
                                    'DeviceName': '/dev/xvda', 
                                    'Ebs': {
                                        'AttachTime': datetime.datetime(2021, 11, 28, 11, 32, 26, tzinfo=tzutc()), 
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
                                        'AttachTime': datetime.datetime(2021, 11, 28, 11, 32, 25, tzinfo=tzutc()), 
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
                            'UsageOperationUpdateTime': datetime.datetime(2021, 11, 28, 11, 32, 25, tzinfo=tzutc()), 
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
                            'LaunchTime': datetime.datetime(2021, 11, 28, 11, 18, 46, tzinfo=tzutc()), 
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
                                        'AttachTime': datetime.datetime(2021, 11, 28, 11, 2, 12, tzinfo=tzutc()), 
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
                                        'AttachTime': datetime.datetime(2021, 11, 28, 11, 2, 11, tzinfo=tzutc()), 
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
                            'UsageOperationUpdateTime': datetime.datetime(2021, 11, 28, 11, 2, 11, tzinfo=tzutc()), 
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
                            'LaunchTime': datetime.datetime(2021, 11, 28, 10, 47, 27, tzinfo=tzutc()), 
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
                                        'AttachTime': datetime.datetime(2021, 11, 28, 10, 47, 28, tzinfo=tzutc()), 
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
                                        'AttachTime': datetime.datetime(2021, 11, 28, 10, 47, 27, tzinfo=tzutc()), 
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
                            'UsageOperationUpdateTime': datetime.datetime(2021, 11, 28, 10, 47, 27, tzinfo=tzutc()), 
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


class TestAwsEc2Scenario(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()

# EOF
