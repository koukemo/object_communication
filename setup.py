from setuptools import setup

package_name = 'object_communication'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='koukemo',
    maintainer_email='java.sparrow22.surface@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            '3dobject_publish = object_communication.object_publisher:main',
            '3dobject_subscribe = object_communication.object_subscriber:main',
        ],
    },
)
