import boto3, json

session = boto3.Session(profile_name='development')
east = 'us-east-1'
west = 'us-west-2'

ec2East = session.client('ec2', region_name = east)
ec2Resource = session.resource('ec2', region_name=east)


ec2IDs = []

runningInstances = ec2East.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': [
                    'running',
                ]
            },
        ],
    )
a=runningInstances['Reservations']
for i in a:
    b=i['Instances']
    for j in b:
        ec2IDs.append(j['InstanceId'])

print('List of EC2 IDs: ',ec2IDs)

for instance in ec2IDs:
    response = ec2East.stop_instances(
        InstanceIds=[
            instance,
        ],
    )