#!/usr/bin/env python

import json
from swiftclient.service import SwiftService

client_opts = {'insecure': True}

with SwiftService(options=client_opts) as swift:
    stat_output = swift.stat()
    print json.dumps(stat_output, indent=2)

