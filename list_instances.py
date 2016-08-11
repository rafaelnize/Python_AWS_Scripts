import boto.ec2
from boto import *
from pprint import pprint
from aws import EC2Instances

def main():
    """docstring"""
    conn = boto.connect_ec2()
    instances = EC2Instances()
    instances.list_instance_names(conn)
    # instances.list_instances(conn)



if __name__ == "__main__":
    main()

