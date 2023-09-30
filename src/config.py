import urllib
import tomli

config = {}
with open('configuration.toml', mode='rb') as f:
    config = tomli.load(f)

config['mongodb']['host'] = config['mongodb']['server'] + urllib.parse.quote(config['mongodb']['password']) + config['mongodb']['cluster']
