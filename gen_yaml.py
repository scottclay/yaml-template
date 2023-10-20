import sys
import yaml

print(sys.argv)

values = sys.argv

d = [{'Owner': values[0],
      'Version':values[1],
      'Input':{'InputOption':values[2], 'InputOption':'InputSetting', 'InputOption':'InputSetting'},
      'Compute':{'ComputeType':values[3], 'ComputeOption':'ComputeSetting', 'ComputeOption':'ComputeSetting'},
      'Output':{'OutputType':values[4], 'OutputOption':'OutputSetting', 'OutputOption':'OutputSetting'},

      }]

with open('magic.yaml', 'w') as yaml_file:
    yaml.dump(d, yaml_file, default_flow_style=False, sort_keys=False)
