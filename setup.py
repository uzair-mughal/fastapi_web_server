from setuptools import find_packages, setup

setup(
    name='fastapi_web_server',
    packages=find_packages(),
    version='0.0.1',
    license='MIT',
    description='',
    author='Uzair Ahmed Mughal',
    author_email='uzam.dev@gmail.com',
    url='',
    download_url='',
    keywords=[
        'AsyncIO',
        'Web Server',
        'FastAPI'
    ],
    install_requires=[
        'fastapi==0.68.2',
        'httptools==0.6.0',
        'gunicorn==20.1.0',
        'python-multipart==0.0.5',
        'uvicorn==0.15.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10'
    ]
)
