from setuptools import setup
from bot.src.settings import bot_version


with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='Ikariam Helper',
    version=bot_version,
    author='Jakub S.',
    url='https://github.com/AnonymousX86/Ikariam-Helper',
    description='Ikariam assistant Discord bot',
    license='GPL-3.0',
    packages=['bot', 'bot.cogs', 'bot.src'],
    python_requires='>=3.8.1',
    install_requires=requirements
)
