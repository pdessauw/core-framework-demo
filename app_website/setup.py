from setuptools import setup, find_packages

setup(
    name="core_website",
    version="0.0.1-alpha1",

    description=("Lorem ipsum description",),

    author="no_author",
    author_email="contact@example.com",

    packages=find_packages(),
    include_package_data=True,
    # package_dir={
    #     '': 'src',
    # },
    #
    install_requires=[
        "Django==1.8.15",
        "core_main"
    ],
)
