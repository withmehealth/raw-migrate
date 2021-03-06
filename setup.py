from setuptools import setup


VERSION = open('__version__').read()

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='alembic-migrate',
    version=VERSION,
    url='https://github.com/withmehealth/alembic-migrate',
    license='MIT',
    author='Filip Dimitrovski',
    author_email='filipdimitrovski22@gmail.com',
    description=('A framework-independent fork of flask-migrate.'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['alembic_migrate'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'alembic>=0.7',
        'click'
    ],
    entry_points={
        'console_scripts': [
            'alembic-db = alembic_migrate.cli:db'
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
