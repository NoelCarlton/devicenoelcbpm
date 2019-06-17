import setuptools

with open("README.md", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'device-noel-cbpm',
    version = '0.0.1',
    author= 'noel@cbpm.com',
    author_email = 'noelcarlton@foxmail.com',
    description = 'crrc train or subway use for inspire drivers gesture',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = "",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ]
)