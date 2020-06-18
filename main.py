from jinja2 import Environment, FileSystemLoader
from git import Repo
from os import path, listdir


def render_file(output, filename='Dockerfile'):
  with open(filename, 'w') as rendered:
    rendered.write(output)


def jinja2_generator(template_name, **kwargs):
  return Environment(loader=FileSystemLoader('templates')).get_template(template_name).render(kwargs)


def force_create_tag(git, tag):
  git.add('Dockerfile')
  git.commit(m='Update {} :whale:'.format(tag))
  git.tag(a=tag, m='Update {} :fire:'.format(tag), f=True)


if __name__ == '__main__':
  php_versions = [5.6, 7.1, 7.2, 7.3, 7.4]  # render php versions
  templates = listdir(path.join('templates'))
  repo = Repo(path.curdir)
  git = repo.git

  for template in templates:
    for version in php_versions:
      tag = '{}-{}'.format(version, template.split('.')[-2])
      dockerfile = jinja2_generator(template, php_version=version)
      render_file(dockerfile)
      force_create_tag(git, tag)

  git.rm('Dockerfile')  # delete Dockerfile on remote repository
  git.push('origin', f=True, tags=True)  # push all tags
