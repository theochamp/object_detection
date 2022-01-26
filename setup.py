import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='object_detection',
    version='0.1',
    description='object detection with tf.io correction',
    license='MIT',
    url='https://github.com/theochamp/object_detection',
    author='Theo CHAMPIGNY',
    author_email='ai-tics@gmail.com',
    py_modules=['object_detection'],
    scripts=['object_detection'],
    install_requires=['Pillow', 'matplotlib', 'Cython']
)