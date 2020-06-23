from jinja2 import Environment, FileSystemLoader
from os import path, listdir, makedirs
from shutil import rmtree


def render_file(output_path, body):
  makedirs('output/{}'.format(output_path), exist_ok=True)
  with open('output/{}/Dockerfile'.format(output_path), 'w') as rendered:
    rendered.write(body)


def jinja2_generator(template_name, **kwargs):
  return Environment(loader=FileSystemLoader('templates')).get_template(template_name).render(kwargs)


if __name__ == '__main__':
  php_versions = [7.1, 7.2, 7.3, 7.4]  # render php versions
  templates = listdir(path.join('templates'))
  for template in templates:
    rmtree('output') if path.exists('output') else print('output path created')
    for version in php_versions:
      template_name = template.split('.')[-2]
      dockerfile = jinja2_generator(template, php_version=version)
      render_file('{}/{}'.format(version, template_name), dockerfile)
