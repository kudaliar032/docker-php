import docker
from jinja2 import Environment, FileSystemLoader
from os import path, listdir, makedirs
from shutil import rmtree

client = docker.from_env()
images = client.images

php_versions = listdir(path.join('output'))
for version in php_versions:
  variants = listdir(path.join('output/{}'.format(version)))
  for variant in variants:
    dockerfile_path = path.join('output/{}/{}'.format(version, variant))
    tag = 'kudaliar032/php:{}-{}'.format(version, variant)
    client.containers.run('gcr.io/kaniko-project/executor:latest')
