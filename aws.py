import boto.ec2
from boto import *
from pprint import pprint


class EC2Instances:
    def __init__(self):
        ''' EC2Instance Constructor '''

    def get_instances(self,conn):
        ''' List Ec2 Instances'''
        reservations = conn.get_all_reservations()
        l_instances = []
        for r in reservations:
            for instance in r.instances:
                    l_instances.append(instance)


        return l_instances

    def get_instance_by_name(self, conn, name):

        filter = {'tag:Name': name}
        ''' List Ec2 Instances'''
        reservations = conn.get_all_reservations(filters=filter)
        l_instances = []
        for r in reservations:
            for instance in r.instances:
                l_instances.append(instance)

        return l_instances

    def list_instance_names(self, conn):

        instances = self.get_instances(conn)
        l_instances = []
        sorted_instances = []
        for instance in instances:
            tags = instance.tags if (hasattr(instance, 'tags')) else {''}

            if 'Name' in tags:
                instancename = tags['Name']
                l_instances.append(instancename)


        sorted_instances = sorted(l_instances)
        print "Found instances with the tag 'Name' are below: \n"

        for instance_name in sorted_instances:
            print instance_name

        print "\n"
        print "Total of instances found: " + str(len(sorted_instances))


    def list_all_instances(self, conn):

        instances = self.get_instances(conn)

        for instance in instances:

            tags = instance.tags if (hasattr(instance, 'tags')) else {''}
            instancename = 'Default EC2 Instance Name'

            if 'Name' in tags:
                instancename = tags['Name']
            #print instance.__dict__
            print "Instance Name:", instancename, ' Instance Id:'\
                , instance.id, " State:", instance.state, " IP: ", instance.private_ip_address


def main():
    """docstring"""
    conn = boto.connect_ec2()
    instances = EC2Instances()
    #instances.list_instance_names(conn)
    instances.list_all_instances(conn)
    # instances.list_instances(conn)



if __name__ == "__main__":
    main()




