try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'I decided to learn in order to finish binary search chalenge on Khan Academy.',
    'author': 'Mariana Souza',
    'url': 'https://www.khanacademy.org/computing/computer-programming/programming',
    'download_url': 'Where to download it.',
    'author_email': 'marianasouza.rj@gmail.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'Intro to Javascript'
}

setup(**config)