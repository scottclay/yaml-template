import sys
import yaml
import os
import random

#print(sys.argv)
#values = sys.argv

# d = [{'Owner': values[0],
#       'Version':values[1],
#       'Input':{'InputOption':values[2], 'InputOption':'InputSetting', 'InputOption':'InputSetting'},
#       'Compute':{'ComputeType':values[3], 'ComputeOption':'ComputeSetting', 'ComputeOption':'ComputeSetting'},
#       'Output':{'OutputType':values[4], 'OutputOption':'OutputSetting', 'OutputOption':'OutputSetting'},
#
#       }]

GHA_NAME = os.environ['GHA_NAME']
GHA_OWNER = os.environ['GHA_OWNER']
GHA_TYPE = os.environ['GHA_TYPE']
GHA_VERSION = os.environ['GHA_VERSION']
GHA_BOOLEAN = os.environ['GHA_BOOLEAN']

print(GHA_NAME, GHA_OWNER, GHA_TYPE, GHA_VERSION, GHA_BOOLEAN)

rand_number = random.randint(0, 99999)

d = [{'Owner': GHA_NAME,
      'Version':GHA_NAME,
      'Input':{'InputOption':GHA_OWNER, 'InputOption':'InputSetting', 'InputOption':'InputSetting'},
      'Compute':{'ComputeType':GHA_OWNER, 'ComputeOption':'ComputeSetting', 'ComputeOption':'ComputeSetting'},
      'Output':{'OutputType':GHA_TYPE, 'OutputOption':'OutputSetting', 'OutputOption':'OutputSetting'},
      }]

with open('magic.yaml', 'w') as yaml_file:
    yaml.dump(d, yaml_file, default_flow_style=False, sort_keys=False)
