import setuptools

setuptools.setup(
    name="jupyter-cloud9-proxy",
    version='1.0',
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
            'cloud9 = jupyter_cloud9_proxy:setup_cloud9',
        ]
    },
    package_data={
        'jupyter_cloud9_proxy': ['icons/*'],
    },
)
