import yaml

f = open('config\data.yml', encoding='utf-8')
data = yaml.safe_load(f)
print(data)