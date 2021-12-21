# Basic test setup

For the purposes of these examples, ensure you have a [named profile](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#shared-credentials-file) setup.

Once setup, the session is started by the following code, replacing `my-profile` with a profile name in your configuration:

```python
>>> import boto3
>>> session = boto3.Session(profile_name='my-profile')
>>> client = session.client('ec2')
```

_**Note**_: You can also [add a region](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#module-boto3.session) as parameter is required

# Getting all instances

For the purpose of security and privacy, in the examples the actual data values are masked.

```python
>>> response = client.describe_instances()
```

_**Note**_: If you have many instances, the above will only get a sub-set. You will know by the presence (or not) of the key `NextToken`. Below is an example check using the REPL, showing the result set we got contains ALL the instances:

```python
>>> 'NextToken' in response
False
```

How many instances did we get?

```python
>>> instances = list()
>>> for reservation in response['Reservations']:
...     for instance in reservation['Instances']:
...             instances.append(instance['InstanceId'])
... 
>>> len(instances)
3
```

The complete data structure is [explained well in the Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instances).


