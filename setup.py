import setuptools


def setup() -> None:
    setuptools.setup(
        packages=setuptools.find_packages(),
        name='matrix-life',
        author='biantsh',
        version=0.2,
    )


if __name__ == '__main__':
    setup()
