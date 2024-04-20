import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.MAHousingTRO',
      version='2.2.5',
      description=('This form lets you ask the court for emergency help if your landlord is not fixing bad conditions in your apartment, your utilities are shut off, or your landlord is doing something else to breach your right to "quiet enjoyment" of your home.'),
      long_description='# docassemble.MAHousingTRO\r\n\r\nThis form lets you ask the court for emergency help if your landlord is not fixing bad conditions in your apartment, your utilities are shut off, or your landlord is doing something else to breach your right to "quiet enjoyment" of your home.\r\n\r\n\r\n## Author\r\n\r\n- Quinten Steenhuis\r\n- Caroline Robinson\r\n- Kate Barry\r\n- Plocket\r\n- Lily Yang\r\n- Matthew Brooks\r\n- Lance Godard\r\n- Maeve MacGlinchey\r\n- Kendall Garner\r\n- David Colarusso\r\n',
      long_description_content_type='text/markdown',
      author='Quinten Steenhuis',
      author_email='qsteenhuis@suffolk.edu',
      license='MIT',
      url='https://courtformsonline.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['docassemble.ALMassachusetts>=0.1.1', 'docassemble.AssemblyLine>=2.14.1', 'docassemble.MassAccess>=0.3.0'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/MAHousingTRO/', package='docassemble.MAHousingTRO'),
     )

