import boto
import boto.ec2
import argparse
from aws import EC2Instances
from aws import EC2Instances


parser = argparse.ArgumentParser(description='Get instance details')
parser.add_argument('-n', '--instance_name', metavar='pattern')
parser.add_argument('-i', "--instance_id", metavar='pattern')


def main():
    """docstring"""
    #conn = boto.connect_ec2()
    #instances = EC2Instances()
    #instances.list_instance_names(conn)
    # instances.list_instances(conn)
    args = parser.parse_args()
    print args

if __name__ == "__main__":
    main()