from setuptools import setup

setup(
    name='{{ cookiecutter.project_slug }}',
    version='1.0.0',
    description='Make any thing(y) an IoT thing(y)',
    author='Bugbird Co.',
    author_email='hey@cuoo.io',
    url='https://l.cuoo.io/thingy',
    install_requires=[
        'cuoo.thingwork @ git+ssh://git@gitlab.com:bugbirdco/cuoo/thingwork.git@main'
    ],
    packages=[
        'app',
        'app.controllers',
        'app.devices',
        'app.devices.dummy_device',
    ],
    package_dir={'app': '../'}
)
