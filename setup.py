from setuptools import setup

setup(name='PyBot',
      version='1.0',
      description='OpenShift App',
      author='Danh Tran',
      author_email='12520054@gm.uit.edu.vn',
      url='https://www.python.org/community/sigs/current/distutils-sig',
      install_requires=['chatterbot>=0.4.14',
                        'Flask>=0.7.2',
                        'MarkupSafe',
                        'jsonpickle',
                        'requests>=2.11.0',
                        'jsondatabase>=0.1.1',
                        'nltk<4.0.0',
                        'pymongo>=3.3.0,<4.0.0',
                        'python-twitter>=3.0',
                        'textblob>=0.11.0,<0.12.0']
      )
