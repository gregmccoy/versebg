from setuptools import setup, find_packages
import os
from os.path import expanduser
home = expanduser("~")
if not os.path.exists(home + "/.versebg"):
    os.mkdir(home + "/.versebg")
    os.mkdir(home + "/.versebg/scripts")
    os.mkdir(home + "/.versebg/font")

setup(
    name = 'versebg',
    author = "Greg McCoy",
    author_email = "gmccoy4242@gmail.com",
    url = "https://github.com/gmccoy42/versebg",
    version = '0.1.3',
    packages=['versebg'],
    scripts=['versebgd'],
    data_files=[(home + "/.versebg", ['data/versebg.conf']),
	    (home + "/.versebg", ['data/default.png']), 
	    (home + "/.versebg/scripts", ['data/feh.sh']),
	    (home + "/.versebg/font", ['data/DejaVuSans.ttf']),
        ('/usr/lib/systemd/system', ['data/versebg.service'])],
    include_package_data=True,
    license='Open Source!',
    long_description=open('README.md').read(),

    install_requires = ['feedparser', 'pillow', 'apscheduler >=2.1.2, <=2.1.2', 'python-systemd', 'configparser']
    )