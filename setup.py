from setuptools import setup, find_packages

package_name = 'gym_robo_training'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    package_data={'': ['']},
    install_requires=['setuptools', 'gym', 'numpy', 'spinup', 'tensorflow'],
    zip_safe=True,
    author='Poh Zhi-Ee',
    author_email='zhiee.poh@httechnology.com',
    maintainer='Poh Zhi-Ee',
    maintainer_email='zhiee.poh@httechnology.com',
    keywords=['OpenAI', 'Gym', 'Ignition Gazebo'],
    description='OpenAI Gym environments for robotics training',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'script1 = gym_robo_training.script1:main',
        ],
    },
)
