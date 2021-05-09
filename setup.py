from setuptools import setup, find_packages

setup(
    name='crypto_correlation_analysis',
    version='1.0',
    packages=find_packages(include=['tk', 'pandas-datareader', 'matplotlib', 'seaborn']),
    url='https://github.com/abdulalikhan/Cryptocurrency-Correlation-Analysis/',
    license='MIT',
    author='Abdul Ali Khan',
    author_email='abdulalikhan1337@gmail.com',
    description='Calculates and plots the correlations between various cryptocurrencies'
)
