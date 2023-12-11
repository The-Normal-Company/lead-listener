from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='LeadListener',

    version='0.1.0',

    author='The Normal Company',

    author_email='info@normalcompany.co',

    description='Lead Listener is a state-of-the-art AI model accompanied by a training set, explicitly designed to locate existing lead pipes. This open-source initiative strives to make communities safer by aiding in the identification and eventual replacement of hazardous lead pipes across the globe.',

    long_description=open('README.md').read(),

    license='MIT',

    url='https://github.com/The-Normal-Company/lead-listener',

    packages=find_packages(),

    install_requires=required,

    python_requires='>=3.6',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],

    # Entry points can be used to provide executable scripts or plugins
    # entry_points={
    #     'console_scripts': [
    #         'mycommand=MyPackage.module1:main_function',
    #     ],
    # },
)
