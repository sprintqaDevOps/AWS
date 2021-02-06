import boto3, json

session = boto3.Session(profile_name='development')
east = 'us-east-1'
west = 'us-west-2'
ec2East = session.client('ec2', region_name = east)

def getEC2IDs():
    response = ec2East.describe_instances()
    a=response['Reservations']
    ec2IDs = []
    for i in a:
        b=i['Instances']
        for j in b:
            #print(j['InstanceId'])
            ec2IDs.append(j['InstanceId'])
    #print('List of EC2 IDs: ',ec2IDs)
    return ec2IDs

def main():
    listOfEC2s=getEC2IDs()
    print(listOfEC2s)
    for i in listOfEC2s:
        ec2East.create_tags(
            Resources = [
                i
            ],
            Tags = [
                {
                    'Key' : 'Day',
                    'Value' : 'Saturday'

                }
            ]
        )

main()