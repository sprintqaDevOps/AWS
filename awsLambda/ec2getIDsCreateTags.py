import boto3, json

session = boto3.Session(profile_name='development')
#global variables for region_name
east = 'us-east-1'
west = 'us-west-2'

# declaring ec2East variable to use ec2 session.client
ec2East = session.client('ec2', region_name = east)
ec2West = session.client('ec2', region_name = west)

def helloWorld():
    ec2IDs = []
    ec2AMIs = []
    hello = ec2East.describe_instances()
    a = hello['Reservations']

    for i in a:
        #print(i['Instances'])
        for j in i['Instances']:
            # print(j['ImageId'])
            # print(j['InstanceId'])
            ec2IDs.append(j['InstanceId'])
            ec2AMIs.append(j['ImageId'])

    print('existing instance ids:',ec2IDs)
    print('existing ami ids:', ec2AMIs)
    return (ec2IDs,ec2AMIs)

def updateTags(listOfEC2s):
    for i in listOfEC2s:
        response = ec2East.create_tags(
            Resources=[
                i,
            ],
            Tags=[
                {
                    'Key': 'Day',
                    'Value': 'Sunday',
                },
                {
                    'Key': 'TechnicalTeam',
                    'Value': 'DevOps',
                },
            ],
        )

def main():
    listOfEC2s,listOfAMIs = helloWorld()
    updateTags(listOfEC2s)

main()

