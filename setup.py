import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-site-tag",
    version="0.0.1",
    author="Richard Oyudo",
    author_email="ebube.rc@gmail.com",
    description="Tag each page on your website with an indicator text or image",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yudori/django-site-tag",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)