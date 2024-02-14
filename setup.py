from setuptools import setup


VERSION = "1.0"


setup(
    name="comments-rand",
    version=VERSION,
    description="Choose random winner from the comments to youtube video",
    author="Mikhail Campos Guadamuz",
    author_email="plageat90@gmail.com",
    classifiers=[
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: Other',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    include_package_data=True,
    install_requires=[
        "google-api-python-client",
        "pytube",
    ],
    packages=["comments_rand"],
    entry_points={
        'console_scripts': [
            'comments-rand = comments_rand.pickler:main',
        ],
    }
)
