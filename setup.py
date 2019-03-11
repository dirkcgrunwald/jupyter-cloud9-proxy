import setuptools

setuptools.setup(
    name="jupyter-c9-proxy",
    version='1.0b1',
    url="https://github.com/dirkcgrunwald/jupyter-cloud9-proxy.git",
    author="Dirk Grunwald based on Project Jupyter Contributors",
    description="grunwald@colorado.edu",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'c9 = jupyter_c9_proxy:setup_c9',
        ]
    },
    package_data={
        'jupyter_c9_proxy': ['icons/*'],
    },
)
