from setuptools import setup, find_packages

setup(
    name="quant_sdn_platform",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Plateforme d'arbitrage quantitatif haute fréquence optimisée par réseau SDN et agent IA",
    long_description=open("README.md").read() if open("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "numpy>=1.22.0",
        "matplotlib>=3.5.0",
        "ipywidgets>=7.7.0",
    ],
)
