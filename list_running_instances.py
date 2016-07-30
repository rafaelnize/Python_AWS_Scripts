import boto
import boto.ec2
from pprint import pprint


def print_running_instances(running_instances):
    print 'The following running instances were found'
    for account_name in running_instances:
        print '\tAccount: %s' % account_name
        d = running_instances[account_name]
        for region_name in d:
            print '\t\tRegion: %s' % region_name
            for instance in d[region_name]:
                print "\n"
                print '\t\t --> %s instance2: %s' % (instance.instance_type, instance.id)
                print '\t\t\t --> Tags=%s' % instance.tags


def find_all_running_instances(accounts=None, quiet=False):
    global running_instances
    if not accounts:
        creds = (boto.config.get('Credentials', 'aws_access_key_id'),
                 boto.config.get('Credentials', 'aws_secret_access_key'))
        accounts = {'main': creds}
        print "no credentials"
    running_instances = {}
    for account_name in accounts:
        running_instances[account_name] = {}
        ak, sk = accounts[account_name]
        try:
            for region in boto.ec2.regions():
                print "connection to " + region.name + "\n"
                conn = region.connect(aws_access_key_id=ak, aws_secret_access_key=sk)
                filters = {'instance-state-name': 'running'}
                instances = []
                reservations = conn.get_all_instances(filters=filters)
                for r in reservations:
                    instances += r.instances
                    if instances:
                        running_instances[account_name][region.name] = instances
        except Exception, e:
            print "can't connect to region " + e.message
            pass
    if not quiet:
        print_running_instances(running_instances)
    return running_instances


if __name__ == '__main__':
    find_all_running_instances()
