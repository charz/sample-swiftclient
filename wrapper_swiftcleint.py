#!/usr/bin/env python

import socket
from os import environ
from optparse import OptionParser
from swiftclient import shell
from swiftclient import RequestException
from swiftclient.exceptions import ClientException
from swiftclient.multithreading import OutputManager

def options():
    parser = OptionParser()
    parser.add_option('-A', '--auth', dest='auth',
                    default=environ.get('ST_AUTH'))
    parser.add_option('-V', '--auth-version',
                    default=environ.get('ST_AUTH_VERSION',
                                        (environ.get('OS_AUTH_VERSION',
                                                    '1.0'))))
    parser.add_option('-U', '--user', dest='user',
                    default=environ.get('ST_USER'))
    parser.add_option('-K', '--key', dest='key',
                    default=environ.get('ST_KEY'))

    parser.add_option('--os_user_id')
    parser.add_option('--os_user_domain_id')
    parser.add_option('--os_user_domain_name')
    parser.add_option('--os_tenant_id')
    parser.add_option('--os_tenant_name')
    parser.add_option('--os_project_id')
    parser.add_option('--os_project_domain_id')
    parser.add_option('--os_project_name')
    parser.add_option('--os_project_domain_name')
    parser.add_option('--os_service_type')
    parser.add_option('--os_endpoint_type')
    parser.add_option('--os_auth_token')
    parser.add_option('--os_storage_url')
    parser.add_option('--os_region_name')
    parser.add_option('--verbose')
    parser.add_option('--insecure', default='True')
    return parser

def stat(*args):
    args = ('',) + args
    with OutputManager() as output:
        parser = options()
        try:
            shell.st_stat(parser, list(args), output)
        except (ClientException, RequestException, socket.error) as err:
            output.error(str(err))

print 'show swift cluster stat'
stat()

