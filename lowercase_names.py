import os
import re
import json
import sys

import oyaml as yaml

with open('kudos.yaml', 'r') as f:
    items = yaml.load(f)
    for i in items:
        i['name'] = i['name'].lower().replace(' ', '_')

with open('kudos.yaml', 'w') as f:
    f.write(yaml.dump(items, default_flow_style=False))