import boto3, json

session = boto3.Session(profile_name='development')
east = 'us-east-1'
west = 'us-west-2'
ec2East = session.client('ec2', region_name = east)


def getEC2withTags():
    ec2IDs = []
    response = ec2East.describe_instances(
        Filters=[
            {
                'Name': 'tag:TechnicalTeamdfsfs',
                'Values': [
                    'DevOpsdfsfds',
                ]
            },
        ],
    )
    print(response)

getEC2withTags()




    # runningInstances = ec2East.describe_instances(
    #     Filters = [
    #         {
    #             'Name' : 'tag:Day',
    #             'Values' : ['Saturday',]
    #         },
    #     ],
    # )
    # a=runningInstances['Reservations']
    # for i in a:
    #     b=i['Instances']
    #     for j in b:
    #         #print(j['InstanceId'])
    #         ec2IDs.append(j['InstanceId'])
    # #print('List of EC2 IDs: ',ec2IDs)
    # return ec2IDs

def main():
    # list of ec2s after filtering with existing tags 
    listOfEC2s=getEC2withTags()
    print(listOfEC2s)
    
    # list of ec2s with given tags in runnin state
    runningEC2s = ec2East.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': [
                    'running',
                ]
            },
        ],
    )
    b=runningEC2s['Reservations']
    runningEc2List = []
    for i in b:
        b=i['Instances']
        for j in b:
            runningEc2List.append(j['InstanceId'])
    print('List of running EC2 IDs: ',runningEc2List)

    # filter ec2s that are in running state and have the given tag
    runningWithTag = []
    for i in listOfEC2s:
        if i in runningEc2List:
            print(i)
            runningWithTag.append(i)
    
    for i in runningWithTag:
        response = ec2East.stop_instances(
            InstanceIds=[
                i,
            ],
        )
    
#main()