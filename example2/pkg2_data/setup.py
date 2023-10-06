import setuptools

setuptools.setup(
    name="pkg2_data",
    version="0.0.1",
    packages=["pkg2_data"],
    package_dir={"": "src"},
    include_package_data=True,
)
