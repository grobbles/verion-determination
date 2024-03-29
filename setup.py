from setuptools import find_packages, setup

setup(
    name='version-determination',
    packages=find_packages(exclude=("VersionDeterminationTests",)),
    version='1.0.0',
    license='MIT',
    description='version determination.',
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    author='Uwe Roder',
    author_email='uweroder@gmail.com',
    include_package_data=True,
    install_requires=['GitPython>=3.0.3'],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Development Status :: 3 - Alpha',
        # Again, pick a license    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Topic :: Software Development :: Build Tools', 'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)
