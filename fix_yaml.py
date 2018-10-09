
import oyaml as yaml


with open('kudos.yaml', 'r') as f:
    kudos = yaml.load(f)


for kudo in kudos:
    kudo.pop('rarity')
    kudo['tags'] = [x.strip() for x in kudo['tags'].split(',')]


with open('kudos2.yaml', 'w') as f:
    f.write(yaml.dump(kudos, default_flow_style=False))
