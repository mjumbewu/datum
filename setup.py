from setuptools import setup

setup(name='datum',
      version='0.1',
      description='Simple spatial data abstraction.',
      url='http://github.com/cityofphiladelphia/datum/',
      author='City of Philadelphia',
      author_email='maps@phila.gov',
      license='MIT',
      packages=['datum'],
      install_requires=[
        'pyproj==1.9.5.1',
        'Shapely==1.5.15',
        'six==1.10.0',
      ],
      extras_require={
        'oracle': ['cx_Oracle==5.2.1'],
        'postgres': ['psycopg2==2.6.1'],
      },
      # entry_points={'console_scripts': ['ais=ais:manager.run']},
      zip_safe=False)
