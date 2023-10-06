import setuptools

setuptools.setup(
    name="pkg1",
    version="0.0.1",
    packages=["pkg1"],
    package_dir={"": "src"},
    install_requires=["numpy", "tifffile"],
    include_package_data=True,
)
