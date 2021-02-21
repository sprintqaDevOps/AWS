import boto3
import botocore
#import cfnresponse
session = boto3.Session(profile_name='development')
east = 'us-east-1'
west = 'us-west-2'
route53 = session.client('route53')

response = route53.list_hosted_zones()

f=response['HostedZones']
hostedZoneName='' 
hostedZoneId=''
for zone in f:
    config=zone["Config"]
    name=zone["Name"]
    e=config["PrivateZone"]
    
    if ('devops.corporate' in name) and e:
        hostedZoneName=zone["Name"]
        hostedZoneId=zone["Id"]
    print(hostedZoneName, hostedZoneId)

responseData = {}
responseData['hostedzonename'] = hostedZoneName
responseData['hostedZonebla'] = hostedZoneId
print(responseData)
    # cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData)