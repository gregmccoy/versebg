from setuptools import setup, find_packages

setup(
    name = 'versebg',
    author = "Greg McCoy",
    author_email = "gmccoy4242@gmail.com",
    url = "https://github.com/gmccoy42/versebg",
    version = '0.1.2',
    packages=['versebg'],
    scripts=['versebgd'],
    data_files=[('data', ['data/versebg.conf']),
	    ('data', ['data/default.png']), 
	    ('data', ['data/feh.sh']),
	    ('data', ['data/DejaVuSans.ttf']),
        ('/usr/lib/systemd/system', ['data/versebg.service'])],
    include_package_data=True,
    license='Open Source!',
    long_description=open('README.md').read(),

    install_requires = ['feedparser', 'pillow', 'schedule', 'python-systemd', 'configparser']
    )