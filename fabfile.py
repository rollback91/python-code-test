import os
from fabric.api import local


def run_manage(command, capture=False):
    return local('/home/ubuntu/.virtualenvs/code-test/bin/python /vagrant/testsite/manage.py %s' % command, capture=capture)


def web():
    run_manage('runserver 0.0.0.0:8888')


def migrate():
    run_manage('migrate')


def make_migrations():
    run_manage('makemigrations')


def requirements():
    local('/home/ubuntu/.virtualenvs/code-test/bin/pip install -r requirements.txt ')


def _save_fixture(app, fixture):
    directory = './testsite/{}/fixtures/'.format(app)

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open('{}initial_data.json'.format(directory), 'w') as f:
        f.writelines(fixture)


def _make_fixture(app):
    fixtures = run_manage('dumpdata {} --indent=4'.format(app), capture=True)
    _save_fixture(app, fixtures)


def create_fixtures():
    _make_fixture('reactions')
    _make_fixture('episodes')


def load_fixtures():
    run_manage('loaddata ./testsite/reactions/fixtures/initial_data.json')
    run_manage('loaddata ./testsite/episodes/fixtures/initial_data.json')
