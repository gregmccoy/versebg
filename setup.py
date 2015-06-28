from setuptools import setup, find_packages

setup(
    name = 'versebg',
    author = "Greg McCoy",
    author_email = "gmccoy4242@gmail.com",
    url = "https://github.com/gmccoy42/versebg",
    version = '0.1dev',
    packages=['versebg'],
    scripts=['run_versebg'],
    data_files=[('/etc/versebg/', ['data/versebg.conf']),
	    ('bitmaps', ['data/default.png']), 
	    ('scripts', ['data/feh']),
	    ('font', ['data/DejaVuSans.ttf'])],
    include_package_data=True,
    license='Open Source!',
    long_description=open('README.md').read(),

    install_requires = ['feedparser', 'pillow', 'schedule']
    )