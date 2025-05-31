from setuptools import setup, find_packages 

setup(
        name="first_setup_tool",
        version="0.0.1",
        description="Reformats files to stout",
        install_requires=["click", "colorma"],
        entry_points="""
        [console scripts]
        jformat=jformat.main:main
        """,
        author="Umair Ahmed Imran",
        author_email="umairahmedimranbutt@gmail.com",
        packages=find_packages(),
        )
