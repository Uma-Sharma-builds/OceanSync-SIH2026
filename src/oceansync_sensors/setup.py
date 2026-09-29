from setuptools import find_packages, setup

package_name = 'oceansync_sensors'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='krati',
    maintainer_email='krati@example.com',
    description='OceanSync simulated ocean sensors',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'ocean_sensors = oceansync_sensors.ocean_sensors:main',
        ],
    },
)
