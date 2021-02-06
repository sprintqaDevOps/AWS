import boto3, json

session = boto3.Session(profile_name='development')
east = 'us-east-1'
west = 'us-west-2'
ec2East = session.client('ec2', region_name = east)

def getEC2withTags():
    ec2IDs = []
    runningInstances = ec2East.describe_instances(
        Filters = [
            {
                'Name' : 'tag:Day',
                'Values' : ['Saturday',]
            },
        ],
    )
    a=runningInstances['Reservations']
    for i in a:
        b=i['Instances']
        for j in b:
            #print(j['InstanceId'])
            ec2IDs.append(j['InstanceId'])
    #print('List of EC2 IDs: ',ec2IDs)
    return ec2IDs

def main():
    listOfEC2s=getEC2withTags()
    print(listOfEC2s)
main()