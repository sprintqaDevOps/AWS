import boto3, json

session = boto3.Session(profile_name='development')
east = 'us-east-1'
west = 'us-west-2'

ec2East = session.client('ec2', region_name = east)
ec2Resource = session.resource('ec2', region_name=east)

response = ec2East.describe_volumes(
        Filters=[
            {
                'Name': 'tag:TechnicalTeam',
                'Values': [
                    'DevOps',
                ]
            }, #get both matching tag and in-use volumes in that region
            {
                'Name': 'status',
                'Values': [
                    'in-use',
                ]
            },
        ],
    )
volumeIDs=[]
vol=response['Volumes']
for i in vol:
    # print(i['VolumeId'])
    # print('///////////////////////////////////////')
    volumeIDs.append(i['VolumeId'])

print(volumeIDs)

retention = 3

for i in volumeIDs:
        response = ec2East.create_snapshot(
            Description='DevOps Team Snapshots',
            VolumeId=i,
            TagSpecifications=[
                {
                    'ResourceType': 'snapshot',
                    'Tags': [
                        {
                            'Key': 'Retention',
                            'Value': str(retention)
                        },
                        {
                            'Key': 'TechnicalTeam',
                            'Value': 'DevOps'
                        },
                    ]
                },
            ],
        )