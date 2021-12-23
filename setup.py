import setuptools
import io

setuptools.setup(
    name="tkfontawesome",
    version="0.1.0",
    author="Israel Dryer",
    author_email="israel.dryer@gmail.com",
    description="Use any of the 1k+ free FontAwesome icons in your tkinter application.",
    keywords="svg fontawesome icons tkinter ttk",
    long_description=io.open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/israel-dryer/tkfontawesome",
    packages=setuptools.find_packages(),
    package_data={"": ["svgs/brands/*", "svgs/regular/*", "svgs/solid/*"]},
    include_package_data=True,
    install_requires=["lxml==4.7.1", "tksvg==0.7.4"],
    python_requires=">=3.7",
)
