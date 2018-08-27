import os
import re
import json
import sys

import oyaml as yaml

fnames = [x for x in os.listdir('images') if x.endswith('.svg')]

# Find list of kudos names, derived from the image file name.
names = []
for fname in fnames:
    name = ''.join([x.lower() for x in re.sub(r'\.svg$', '', fname)])
    names.append((name, fname))

# print(names)

with open('kudos.yaml', 'r') as f:
    existing_kudos = yaml.load(f)

existing_kudos_names = [kudos['name'] for kudos in existing_kudos]


objs = []
for name in names:
    if name[0] not in existing_kudos_names:
        print(name[0])
        obj = dict(name=name[0],
                   description='lorum',
                   rarity=20,
                   price=1,
                   numClonesAllowed=10,
                   tags='ipsum',
                   image=name[1]
                   )
        objs.append(obj)


with open('kudos2.yaml', 'w') as f:
    f.write(yaml.dump(objs, default_flow_style=False))
