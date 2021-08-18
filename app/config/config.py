import confuse

source = confuse.YamlSource('app/config/config.yaml')
config = confuse.Configuration("MOTSI", __name__)

app_name = config['appName']