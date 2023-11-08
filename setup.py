from setuptools import setup, find_packages

setup(
    name='StudentDatabase',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'student-database=student_database:main',
        ],
    },
    author='Franklin Ajisogun',
    author_email='franklin.ajisogun03@gmail.com',
    description='A simple student database management system',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Franklin0603/StudentDatabase_sqlite3',
    project_urls={
        'Bug Tracker': 'http://github.com/yourusername/studentDatabase/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
