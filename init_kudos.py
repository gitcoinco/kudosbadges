import os
import re
import json
import sys

import oyaml as yaml

fnames = [x for x in os.listdir('images') if x.endswith('.svg')]

names = []
for fname in fnames:
    name = ' '.join([x.capitalize() for x in re.sub(r'\.svg$', '', fname).split('_')])
    names.append((name, fname))


if os.path.exists('kudos.yaml'):
    print('kudos.yaml file already exists.')
    ans = input('Do you want to re-initialize it. (y/N)?  ')
    if ans.lower() != 'y':
        sys.exit(1)

objs = []
for name in names:
    obj = dict(name=name[0],
               description='lorum',
               rarity=20,
               price=1,
               numClonesAllowed=10,
               tags='ipsum',
               image=name[1]
               )
    objs.append(obj)

with open('kudos.yaml', 'w') as f:
    f.write(yaml.dump(objs, default_flow_style=False))
