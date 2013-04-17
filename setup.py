import os
import platform

from setuptools import setup, find_packages


class Setup(object):
    @staticmethod
    def read(fname, fail_silently=False):
        """
        Utility function to read the content of the given file.
        """
        try:
            return open(os.path.join(os.path.dirname(__file__), fname)).read()
        except:
            if not fail_silently:
                raise
            return ''


    @staticmethod
    def requirements(fname):
        """
        Utility function to create a list of requirements from the output of the
        pip freeze command saved in a text file.
        """
        packages = Setup.read(fname).split('\n')
        packages = (p.strip() for p in packages)
        packages = (p for p in packages if p and not p.startswith('#'))
        return list(packages)


    @staticmethod
    def get_files(*bases):
        """
        Utility function to list all files in a data directory.
        """
        for base in bases:
            basedir, _ = base.split('.', 1)
            base = os.path.join(os.path.dirname(__file__), *base.split('.'))

            rem = len(os.path.dirname(base))  + len(basedir) + 2

            for root, dirs, files in os.walk(base):
                for name in files:
                    yield os.path.join(basedir, root, name)[rem:]


setup(
    name='subcommands',
    version='0.1a',
    description='Small framework to create command line utilities',
    author='Jonathan Stoppani',
    author_email='jonathan@stoppani.name',
    url='https://github.com/garetjax/subcommands',
    license='MIT',
    packages=find_packages(),
    package_dir = {'subcommands': 'subcommands'},
    package_data = {
    },
    install_requires=Setup.requirements('requirements.txt'),
    entry_points=Setup.read('entry-points.ini', True),
)
