def startEC2():    
    print("starting ec2s daily at 8am")
    # Get list of regions
    regions = [region['RegionName']
    for region in ec2_client.describe_regions()['Regions']]

    # Iterate over each region
    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)

        print("Region:", region)

        # Get only running instances
        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name',
                      'Values': ['stopped']}])

        # Stop the instances
        for instance in instances:
            instance.start()
            print('Started instance: ', instance.id)
  
startEC2()
