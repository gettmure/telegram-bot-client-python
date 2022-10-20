
import os

from setuptools import find_packages, setup

# Optional project description in README.md:
current_directory = os.path.dirname(os.path.abspath(__file__))

# try:
#     with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
#         long_description = f.read()
# except Exception:
#     long_description = ''
setup(

    # Project name:
    name='telegram-bot-client',

    # Packages to include in the distribution:
    packages=find_packages(','),

    # Project version number:
    version='1.0',

    # List a license for the project, eg. MIT License
    license='MIT License',

    # Short description of your library:
    description='Telegram bot client by gettmure',

    # Long description of your library:
    long_description='Telegram bot client by gettmure but veeeery long',
    long_description_content_type='text/markdown',

    # Your name:
    author='gettmure',

    # Your email address:
    author_email='gettmure.work@gmail.com',

    # Link to your github repository or website:
    url='https://github.com/gettmure',

    # Download Link from where the project can be downloaded from:
    download_url='https://github.com/gettmure/telegram-bot-client-python',

    # List of keywords:
    keywords=[
        'python',
        'telegram',
        'bot',
        'client',
        'telegram-bot',
        'telegram-client'
    ],

    # List project dependencies:
    install_requires=[
        "pycodestyle",
        "python-dotenv",
        "autopep8"
    ],

    # https://pypi.org/classifiers/
    classifiers=[
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.10',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Customer Service'
    ]
)
