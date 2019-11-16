from setuptools import setup, find_packages

setup(
    name="snowalert-runners",
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'aiohttp[speedups]',
        'fire==0.1.3',
        'jira==2.0.0',
        'PyYAML==4.2b1',
        'snowflake-connector-python==2.0.4',
        'snowflake-sqlalchemy==1.1.2',
        'pandas==0.24.1',
        'pybrake==0.4.0',
        'rpy2==3.2.0',
        'pytz==2018.9',
        'slackclient==1.3.1',
        'tzlocal==1.5.1',
        'snowflake-ingest==0.9.1',
        'azure-common==1.1.23',
        'azure-mgmt-compute==8.0.0',
        'azure-mgmt-network==5.0.0',
        'azure-mgmt-storage==4.1.0',
        'azure-mgmt-subscription==0.5.0',
        'azure-storage-blob==2.1.0',
        'azure-storage-common==2.1.0',
        'google-api-python-client==1.7.10',
        'pyTenable==0.3.22',
        'boto3==1.10.24',
        'twilio==6.29.4',
    ],
)
