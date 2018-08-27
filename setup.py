from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('README.md') as f:
    readme = f.read()

setup(
    name='aiotwitch',
    version='0.1dev',
    author='Kelwing',
    packages=['aiotwitch',],
    license='GPLv3',
    description='A python wrapper for the Twitch Helix API',
    url='https://github.com/kelwing/aiotwitch',
    python_requires='>=3.6.6',
    install_requires=requirements,
    long_description=readme,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: AsyncIO',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
