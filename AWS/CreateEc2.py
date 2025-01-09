from botocore.exceptions import ClientError
import boto3

def createEc2():
    # Set up Ec2 client
    ec2 = boto3.client('ec2', region_name='eu-north-1')  # Replace 'us-east-1' with your desired region


    # Specify instance parameters

    image_id = 'ami-0056da249ced43c7a'
    instance_type = 't3.micro'
    key_name = 'Sonar'
    security_group_ids = 'sg-0348878d694a5774f'
    subnet_id = 'subnet-02441165c86708a36'

    #Launch EC2 instance


    try:
        response = ec2.run_instances(
            ImageId=image_id,
            InstanceType=instance_type,  # Ensure this is available in your region
            MinCount=1,
            MaxCount=1,
            SubnetId=subnet_id,
            SecurityGroupIds=[security_group_ids]
        )
        print(response)

    # Get Instance ID from response
        instance_id = response['Instances'][0]['InstanceId']


    # Get for instance to be running
        ec2.get_waiter('instance_running').wait(InstanceIds=[instance_id])

    # Print instance information

        instance = ec2.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]
        print(f"Instance ID : {instance_id}")
        print(f"Public IP address : {instance.get('PublicIPAddress', 'N/A')}")
        print(f"Private address : {instance.get('PrivateIPAddress', 'N/A')}")
        print(f"Architecture : {instance.get('Architecture')}")

    except ClientError as e:
        print(f"Error: {e}")