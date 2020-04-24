# Python 2.7.x: AttributeError: 'module' object has no attribute '__version__'

## Steps to reproduce

```bash
virtualenv -p python2.7 test

. ./test/bin/activate

pip install setuptools==39.2.0

python setup.py install
```

### Packages
```
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. A future version of pip will drop support for Python 2.7. More details about Python 2 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
Package       Version
------------- ----------
appdirs       1.4.3
boto3         1.9.113
certifi       2020.4.5.1
chardet       3.0.4
decorator     4.4.2
dpath         1.4.2
GitPython     3.1.1
idna          2.7
Jinja2        2.10
jsonpath-rw   1.4.0
paramiko      2.7.1
pip           20.0.2
ply           3.11
python-consul 1.1.0
requests      2.20.1
semver        2.8.1
setuptools    39.2.0
six           1.14.0
sshtunnel     0.1.4
test          0.0.1rc0
urllib3       1.24.3
wheel         0.34.2
```

### Outcome
```
/private/tmp/test/lib/python2.7/site-packages/setuptools/dist.py:398: UserWarning: Normalizing '0.0.1-preview' to '0.0.1rc0'
  normalized_version,
running install
running bdist_egg
running egg_info
creating test.egg-info
writing requirements to test.egg-info/requires.txt
writing test.egg-info/PKG-INFO
writing top-level names to test.egg-info/top_level.txt
writing dependency_links to test.egg-info/dependency_links.txt
writing manifest file 'test.egg-info/SOURCES.txt'
reading manifest file 'test.egg-info/SOURCES.txt'
writing manifest file 'test.egg-info/SOURCES.txt'
installing library code to build/bdist.macosx-10.13-x86_64/egg
running install_lib
warning: install_lib: 'build/lib' does not exist -- no Python modules to install

creating build
creating build/bdist.macosx-10.13-x86_64
creating build/bdist.macosx-10.13-x86_64/egg
creating build/bdist.macosx-10.13-x86_64/egg/EGG-INFO
copying test.egg-info/PKG-INFO -> build/bdist.macosx-10.13-x86_64/egg/EGG-INFO
copying test.egg-info/SOURCES.txt -> build/bdist.macosx-10.13-x86_64/egg/EGG-INFO
copying test.egg-info/dependency_links.txt -> build/bdist.macosx-10.13-x86_64/egg/EGG-INFO
copying test.egg-info/requires.txt -> build/bdist.macosx-10.13-x86_64/egg/EGG-INFO
copying test.egg-info/top_level.txt -> build/bdist.macosx-10.13-x86_64/egg/EGG-INFO
zip_safe flag not set; analyzing archive contents...
creating dist
creating 'dist/test-0.0.1rc0-py2.7.egg' and adding 'build/bdist.macosx-10.13-x86_64/egg' to it
removing 'build/bdist.macosx-10.13-x86_64/egg' (and everything under it)
Processing test-0.0.1rc0-py2.7.egg
Copying test-0.0.1rc0-py2.7.egg to /private/tmp/test/lib/python2.7/site-packages
Adding test 0.0.1rc0 to easy-install.pth file

Installed /private/tmp/test/lib/python2.7/site-packages/test-0.0.1rc0-py2.7.egg
Processing dependencies for test==0.0.1rc0
Searching for appdirs==1.4.3
Reading https://pypi.org/simple/appdirs/
Downloading https://files.pythonhosted.org/packages/56/eb/810e700ed1349edde4cbdc1b2a21e28cdf115f9faf263f6bbf8447c1abf3/appdirs-1.4.3-py2.py3-none-any.whl#sha256=d8b24664561d0d34ddfaec54636d502d7cea6e29c3eaf68f3df6180863e2166e
Best match: appdirs 1.4.3
Processing appdirs-1.4.3-py2.py3-none-any.whl
Installing appdirs-1.4.3-py2.py3-none-any.whl to /private/tmp/test/lib/python2.7/site-packages
Adding appdirs 1.4.3 to easy-install.pth file

Installed /private/tmp/test/lib/python2.7/site-packages/appdirs-1.4.3-py2.7.egg
Searching for jsonpath_rw==1.4.0
Reading https://pypi.org/simple/jsonpath_rw/
Downloading https://files.pythonhosted.org/packages/71/7c/45001b1f19af8c4478489fbae4fc657b21c4c669d7a5a036a86882581d85/jsonpath-rw-1.4.0.tar.gz#sha256=05c471281c45ae113f6103d1268ec7a4831a2e96aa80de45edc89b11fac4fbec
Best match: jsonpath-rw 1.4.0
Processing jsonpath-rw-1.4.0.tar.gz
Writing /var/folders/jm/nszzwsfd7tb76tv9b58rx6980000gn/T/easy_install-6rqIxu/jsonpath-rw-1.4.0/setup.cfg
Running jsonpath-rw-1.4.0/setup.py -q bdist_egg --dist-dir /var/folders/jm/nszzwsfd7tb76tv9b58rx6980000gn/T/easy_install-6rqIxu/jsonpath-rw-1.4.0/egg-dist-tmp-Gq0iN1
zip_safe flag not set; analyzing archive contents...
jsonpath_rw.parser: module references __file__
creating /private/tmp/test/lib/python2.7/site-packages/jsonpath_rw-1.4.0-py2.7.egg
Extracting jsonpath_rw-1.4.0-py2.7.egg to /private/tmp/test/lib/python2.7/site-packages
Adding jsonpath-rw 1.4.0 to easy-install.pth file
Installing jsonpath.py script to /private/tmp/test/bin

Installed /private/tmp/test/lib/python2.7/site-packages/jsonpath_rw-1.4.0-py2.7.egg
Searching for python-consul==1.1.0
Reading https://pypi.org/simple/python-consul/
Downloading https://files.pythonhosted.org/packages/3f/d0/59bc5f1c6c4d4b498c41d8ce7052ee9e9d68be19e16038a55252018a6c4d/python_consul-1.1.0-py2.py3-none-any.whl#sha256=eeaaeeae87807ad1bc0d476ca3a9c53823ed5d514832951acebeca671eb54b20
Best match: python-consul 1.1.0
Processing python_consul-1.1.0-py2.py3-none-any.whl
Installing python_consul-1.1.0-py2.py3-none-any.whl to /private/tmp/test/lib/python2.7/site-packages
writing requirements to /private/tmp/test/lib/python2.7/site-packages/python_consul-1.1.0-py2.7.egg/EGG-INFO/requires.txt
Adding python-consul 1.1.0 to easy-install.pth file

Installed /private/tmp/test/lib/python2.7/site-packages/python_consul-1.1.0-py2.7.egg
Searching for semver==2.8.1
Reading https://pypi.org/simple/semver/
Downloading https://files.pythonhosted.org/packages/21/18/a0de8cda637ba3efee1b3617ded00601507ce15bd70a39399740e0fd415f/semver-2.8.1-py2.py3-none-any.whl#sha256=41c9aa26c67dc16c54be13074c352ab666bce1fa219c7110e8f03374cd4206b0
Best match: semver 2.8.1
Processing semver-2.8.1-py2.py3-none-any.whl
Installing semver-2.8.1-py2.py3-none-any.whl to /private/tmp/test/lib/python2.7/site-packages
Adding semver 2.8.1 to easy-install.pth file

Installed /private/tmp/test/lib/python2.7/site-packages/semver-2.8.1-py2.7.egg
Searching for sshtunnel==0.1.4
Reading https://pypi.org/simple/sshtunnel/
Downloading https://files.pythonhosted.org/packages/bf/8d/385c7e7c90e17934b3102ad2902e224c27a7173a6a57ef4805dcef8043b1/sshtunnel-0.1.4.tar.gz#sha256=f29ae41a1bd3afa64e9a31029bece2966e4be9a9641e8262372741e691c40d76
Best match: sshtunnel 0.1.4
Processing sshtunnel-0.1.4.tar.gz
Writing /var/folders/jm/nszzwsfd7tb76tv9b58rx6980000gn/T/easy_install-t_hz0s/sshtunnel-0.1.4/setup.cfg
Running sshtunnel-0.1.4/setup.py -q bdist_egg --dist-dir /var/folders/jm/nszzwsfd7tb76tv9b58rx6980000gn/T/easy_install-t_hz0s/sshtunnel-0.1.4/egg-dist-tmp-adhCxl
zip_safe flag not set; analyzing archive contents...
Copying sshtunnel-0.1.4-py2.7.egg to /private/tmp/test/lib/python2.7/site-packages
Adding sshtunnel 0.1.4 to easy-install.pth file
Installing sshtunnel script to /private/tmp/test/bin

Installed /private/tmp/test/lib/python2.7/site-packages/sshtunnel-0.1.4-py2.7.egg
Searching for requests==2.20.1
Reading https://pypi.org/simple/requests/
Downloading https://files.pythonhosted.org/packages/ff/17/5cbb026005115301a8fb2f9b0e3e8d32313142fe8b617070e7baad20554f/requests-2.20.1-py2.py3-none-any.whl#sha256=65b3a120e4329e33c9889db89c80976c5272f56ea92d3e74da8a463992e3ff54
Best match: requests 2.20.1
Processing requests-2.20.1-py2.py3-none-any.whl
Installing requests-2.20.1-py2.py3-none-any.whl to /private/tmp/test/lib/python2.7/site-packages
writing requirements to /private/tmp/test/lib/python2.7/site-packages/requests-2.20.1-py2.7.egg/EGG-INFO/requires.txt
Adding requests 2.20.1 to easy-install.pth file

Installed /private/tmp/test/lib/python2.7/site-packages/requests-2.20.1-py2.7.egg
Searching for Jinja2==2.10
Reading https://pypi.org/simple/Jinja2/
Downloading https://files.pythonhosted.org/packages/7f/ff/ae64bacdfc95f27a016a7bed8e8686763ba4d277a78ca76f32659220a731/Jinja2-2.10-py2.py3-none-any.whl#sha256=74c935a1b8bb9a3947c50a54766a969d4846290e1e788ea44c1392163723c3bd
Best match: Jinja2 2.10
Processing Jinja2-2.10-py2.py3-none-any.whl
Installing Jinja2-2.10-py2.py3-none-any.whl to /private/tmp/test/lib/python2.7/site-packages
writing requirements to /private/tmp/test/lib/python2.7/site-packages/Jinja2-2.10-py2.7.egg/EGG-INFO/requires.txt
Adding Jinja2 2.10 to easy-install.pth file

Installed /private/tmp/test/lib/python2.7/site-packages/Jinja2-2.10-py2.7.egg
Searching for GitPython
Reading https://pypi.org/simple/GitPython/
Downloading https://files.pythonhosted.org/packages/ac/3d/9fe11d9cf14b49553e8e35a4dce360e18f25f964638b631dc5b9ca23a88f/GitPython-3.1.1.tar.gz#sha256=6d4f10e2aaad1864bb0f17ec06a2c2831534140e5883c350d58b4e85189dab74
Best match: GitPython 3.1.1
Processing GitPython-3.1.1.tar.gz
Writing /var/folders/jm/nszzwsfd7tb76tv9b58rx6980000gn/T/easy_install-ZzPKK4/GitPython-3.1.1/setup.cfg
Running GitPython-3.1.1/setup.py -q bdist_egg --dist-dir /var/folders/jm/nszzwsfd7tb76tv9b58rx6980000gn/T/easy_install-ZzPKK4/GitPython-3.1.1/egg-dist-tmp-lrBtbc
warning: no previously-included files matching '__pycache__' found anywhere in distribution
warning: no previously-included files matching '*.pyc' found anywhere in distribution
creating /private/tmp/test/lib/python2.7/site-packages/GitPython-3.1.1-py2.7.egg
Extracting GitPython-3.1.1-py2.7.egg to /private/tmp/test/lib/python2.7/site-packages
Adding GitPython 3.1.1 to easy-install.pth file

Installed /private/tmp/test/lib/python2.7/site-packages/GitPython-3.1.1-py2.7.egg
Searching for dpath==1.4.2
Reading https://pypi.org/simple/dpath/
Downloading https://files.pythonhosted.org/packages/23/0d/c48b7caa127d0f4987fd9538eddda1314a8df7f22740f51e2dc0e0383c59/dpath-1.4.2.tar.gz#sha256=0f635f49e88843a4a519aca1c599faee271730f818a81860827e7d7b4d40273f
Best match: dpath 1.4.2
Processing dpath-1.4.2.tar.gz
Writing /var/folders/jm/nszzwsfd7tb76tv9b58rx6980000gn/T/easy_install-gxIeyQ/dpath-1.4.2/setup.cfg
Running dpath-1.4.2/setup.py -q bdist_egg --dist-dir /var/folders/jm/nszzwsfd7tb76tv9b58rx6980000gn/T/easy_install-gxIeyQ/dpath-1.4.2/egg-dist-tmp-hBnQQa
zip_safe flag not set; analyzing archive contents...
Copying dpath-1.4.2-py2.7.egg to /private/tmp/test/lib/python2.7/site-packages
Adding dpath 1.4.2 to easy-install.pth file

Installed /private/tmp/test/lib/python2.7/site-packages/dpath-1.4.2-py2.7.egg
Searching for boto3==1.9.113
Reading https://pypi.org/simple/boto3/
Downloading https://files.pythonhosted.org/packages/b6/99/4736997c6b993591dc433123235f6d9a4a1d5384f145c54af279a151e4c5/boto3-1.9.113-py2.py3-none-any.whl#sha256=e270308792f4bb6ab52a2b70e9fc5947a1f9819653b5431e51eedae2fb897e96
Best match: boto3 1.9.113
Processing boto3-1.9.113-py2.py3-none-any.whl
Installing boto3-1.9.113-py2.py3-none-any.whl to /private/tmp/test/lib/python2.7/site-packages
writing requirements to /private/tmp/test/lib/python2.7/site-packages/boto3-1.9.113-py2.7.egg/EGG-INFO/requires.txt
Adding boto3 1.9.113 to easy-install.pth file

Installed /private/tmp/test/lib/python2.7/site-packages/boto3-1.9.113-py2.7.egg
Searching for six
Reading https://pypi.org/simple/six/
Downloading https://files.pythonhosted.org/packages/65/eb/1f97cb97bfc2390a276969c6fae16075da282f5058082d4cb10c6c5c1dba/six-1.14.0-py2.py3-none-any.whl#sha256=8f3cd2e254d8f793e7f3d6d9df77b92252b52637291d0f0da013c76ea2724b6c
Best match: six 1.14.0
Processing six-1.14.0-py2.py3-none-any.whl
Installing six-1.14.0-py2.py3-none-any.whl to /private/tmp/test/lib/python2.7/site-packages
Adding six 1.14.0 to easy-install.pth file

Installed /private/tmp/test/lib/python2.7/site-packages/six-1.14.0-py2.7.egg
Searching for decorator
Reading https://pypi.org/simple/decorator/
Downloading https://files.pythonhosted.org/packages/ed/1b/72a1821152d07cf1d8b6fce298aeb06a7eb90f4d6d41acec9861e7cc6df0/decorator-4.4.2-py2.py3-none-any.whl#sha256=41fa54c2a0cc4ba648be4fd43cff00aedf5b9465c9bf18d64325bc225f08f760
Best match: decorator 4.4.2
Processing decorator-4.4.2-py2.py3-none-any.whl
Installing decorator-4.4.2-py2.py3-none-any.whl to /private/tmp/test/lib/python2.7/site-packages
Adding decorator 4.4.2 to easy-install.pth file

Installed /private/tmp/test/lib/python2.7/site-packages/decorator-4.4.2-py2.7.egg
Searching for ply
Reading https://pypi.org/simple/ply/
Downloading https://files.pythonhosted.org/packages/a3/58/35da89ee790598a0700ea49b2a66594140f44dec458c07e8e3d4979137fc/ply-3.11-py2.py3-none-any.whl#sha256=096f9b8350b65ebd2fd1346b12452efe5b9607f7482813ffca50c22722a807ce
Best match: ply 3.11
Processing ply-3.11-py2.py3-none-any.whl
Installing ply-3.11-py2.py3-none-any.whl to /private/tmp/test/lib/python2.7/site-packages
Adding ply 3.11 to easy-install.pth file

Installed /private/tmp/test/lib/python2.7/site-packages/ply-3.11-py2.7.egg
Searching for paramiko>=1.15.2
Reading https://pypi.org/simple/paramiko/
Downloading https://files.pythonhosted.org/packages/06/1e/1e08baaaf6c3d3df1459fd85f0e7d2d6aa916f33958f151ee1ecc9800971/paramiko-2.7.1-py2.py3-none-any.whl#sha256=9c980875fa4d2cb751604664e9a2d0f69096643f5be4db1b99599fe114a97b2f
Best match: paramiko 2.7.1
Processing paramiko-2.7.1-py2.py3-none-any.whl
Installing paramiko-2.7.1-py2.py3-none-any.whl to /private/tmp/test/lib/python2.7/site-packages
writing requirements to /private/tmp/test/lib/python2.7/site-packages/paramiko-2.7.1-py2.7.egg/EGG-INFO/requires.txt
Adding paramiko 2.7.1 to easy-install.pth file

Installed /private/tmp/test/lib/python2.7/site-packages/paramiko-2.7.1-py2.7.egg
Searching for urllib3<1.25,>=1.21.1
Reading https://pypi.org/simple/urllib3/
Downloading https://files.pythonhosted.org/packages/01/11/525b02e4acc0c747de8b6ccdab376331597c569c42ea66ab0a1dbd36eca2/urllib3-1.24.3-py2.py3-none-any.whl#sha256=a637e5fae88995b256e3409dc4d52c2e2e0ba32c42a6365fee8bbd2238de3cfb
Best match: urllib3 1.24.3
Processing urllib3-1.24.3-py2.py3-none-any.whl
Installing urllib3-1.24.3-py2.py3-none-any.whl to /private/tmp/test/lib/python2.7/site-packages
writing requirements to /private/tmp/test/lib/python2.7/site-packages/urllib3-1.24.3-py2.7.egg/EGG-INFO/requires.txt
Adding urllib3 1.24.3 to easy-install.pth file

Installed /private/tmp/test/lib/python2.7/site-packages/urllib3-1.24.3-py2.7.egg
Searching for idna<2.8,>=2.5
Reading https://pypi.org/simple/idna/
Downloading https://files.pythonhosted.org/packages/4b/2a/0276479a4b3caeb8a8c1af2f8e4355746a97fab05a372e4a2c6a6b876165/idna-2.7-py2.py3-none-any.whl#sha256=156a6814fb5ac1fc6850fb002e0852d56c0c8d2531923a51032d1b70760e186e
Best match: idna 2.7
Processing idna-2.7-py2.py3-none-any.whl
Installing idna-2.7-py2.py3-none-any.whl to /private/tmp/test/lib/python2.7/site-packages
Adding idna 2.7 to easy-install.pth file

Installed /private/tmp/test/lib/python2.7/site-packages/idna-2.7-py2.7.egg
Searching for chardet<3.1.0,>=3.0.2
Reading https://pypi.org/simple/chardet/
Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl#sha256=fc323ffcaeaed0e0a02bf4d117757b98aed530d9ed4531e3e15460124c106691
Best match: chardet 3.0.4
Processing chardet-3.0.4-py2.py3-none-any.whl
Installing chardet-3.0.4-py2.py3-none-any.whl to /private/tmp/test/lib/python2.7/site-packages
Adding chardet 3.0.4 to easy-install.pth file
Installing chardetect script to /private/tmp/test/bin

Installed /private/tmp/test/lib/python2.7/site-packages/chardet-3.0.4-py2.7.egg
Searching for certifi>=2017.4.17
Reading https://pypi.org/simple/certifi/
Downloading https://files.pythonhosted.org/packages/57/2b/26e37a4b034800c960a00c4e1b3d9ca5d7014e983e6e729e33ea2f36426c/certifi-2020.4.5.1-py2.py3-none-any.whl#sha256=1d987a998c75633c40847cc966fcf5904906c920a7f17ef374f5aa4282abd304
Best match: certifi 2020.4.5.1
Processing certifi-2020.4.5.1-py2.py3-none-any.whl
Installing certifi-2020.4.5.1-py2.py3-none-any.whl to /private/tmp/test/lib/python2.7/site-packages
Adding certifi 2020.4.5.1 to easy-install.pth file

Installed /private/tmp/test/lib/python2.7/site-packages/certifi-2020.4.5.1-py2.7.egg
Searching for MarkupSafe>=0.23
Reading https://pypi.org/simple/MarkupSafe/
Downloading https://files.pythonhosted.org/packages/e0/bf/acc45baeb2d7333ed724c30af188640d9cb0be4b28533edfc3e2ae5aad72/MarkupSafe-2.0.0a1.tar.gz#sha256=beac28ed60c8e838301226a7a85841d0af2068eba2dcb1a58c2d32d6c05e440e
Best match: MarkupSafe 2.0.0a1
Processing MarkupSafe-2.0.0a1.tar.gz
Writing /var/folders/jm/nszzwsfd7tb76tv9b58rx6980000gn/T/easy_install-o23Mtd/MarkupSafe-2.0.0a1/setup.cfg
Running MarkupSafe-2.0.0a1/setup.py -q bdist_egg --dist-dir /var/folders/jm/nszzwsfd7tb76tv9b58rx6980000gn/T/easy_install-o23Mtd/MarkupSafe-2.0.0a1/egg-dist-tmp-guU0BQ
Traceback (most recent call last):
  File "setup.py", line 27, in <module>
    'mock'
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/__init__.py", line 129, in setup
    return distutils.core.setup(**attrs)
  File "/usr/local/Cellar/python@2/2.7.15_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/core.py", line 151, in setup
    dist.run_commands()
  File "/usr/local/Cellar/python@2/2.7.15_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/dist.py", line 953, in run_commands
    self.run_command(cmd)
  File "/usr/local/Cellar/python@2/2.7.15_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/dist.py", line 972, in run_command
    cmd_obj.run()
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/command/install.py", line 67, in run
    self.do_egg_install()
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/command/install.py", line 117, in do_egg_install
    cmd.run()
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/command/easy_install.py", line 412, in run
    self.easy_install(spec, not self.no_deps)
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/command/easy_install.py", line 654, in easy_install
    return self.install_item(None, spec, tmpdir, deps, True)
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/command/easy_install.py", line 701, in install_item
    self.process_distribution(spec, dist, deps)
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/command/easy_install.py", line 746, in process_distribution
    [requirement], self.local_index, self.easy_install
  File "/private/tmp/test/lib/python2.7/site-packages/pkg_resources/__init__.py", line 770, in resolve
    replace_conflicting=replace_conflicting
  File "/private/tmp/test/lib/python2.7/site-packages/pkg_resources/__init__.py", line 1053, in best_match
    return self.obtain(req, installer)
  File "/private/tmp/test/lib/python2.7/site-packages/pkg_resources/__init__.py", line 1065, in obtain
    return installer(requirement)
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/command/easy_install.py", line 673, in easy_install
    return self.install_item(spec, dist.location, tmpdir, deps)
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/command/easy_install.py", line 699, in install_item
    dists = self.install_eggs(spec, download, tmpdir)
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/command/easy_install.py", line 884, in install_eggs
    return self.build_and_install(setup_script, setup_base)
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/command/easy_install.py", line 1152, in build_and_install
    self.run_setup(setup_script, setup_base, args)
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/command/easy_install.py", line 1138, in run_setup
    run_setup(setup_script, args)
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/sandbox.py", line 253, in run_setup
    raise
  File "/usr/local/Cellar/python@2/2.7.15_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7/contextlib.py", line 35, in __exit__
    self.gen.throw(type, value, traceback)
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/sandbox.py", line 195, in setup_context
    yield
  File "/usr/local/Cellar/python@2/2.7.15_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7/contextlib.py", line 35, in __exit__
    self.gen.throw(type, value, traceback)
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/sandbox.py", line 166, in save_modules
    saved_exc.resume()
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/sandbox.py", line 141, in resume
    six.reraise(type, exc, self._tb)
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/sandbox.py", line 154, in save_modules
    yield saved
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/sandbox.py", line 195, in setup_context
    yield
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/sandbox.py", line 250, in run_setup
    _execfile(setup_script, ns)
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/sandbox.py", line 45, in _execfile
    exec(code, globals, locals)
  File "/var/folders/jm/nszzwsfd7tb76tv9b58rx6980000gn/T/easy_install-o23Mtd/MarkupSafe-2.0.0a1/setup.py", line 56, in <module>

  File "/var/folders/jm/nszzwsfd7tb76tv9b58rx6980000gn/T/easy_install-o23Mtd/MarkupSafe-2.0.0a1/setup.py", line 43, in run_setup

  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/__init__.py", line 129, in setup
    return distutils.core.setup(**attrs)
  File "/usr/local/Cellar/python@2/2.7.15_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/core.py", line 124, in setup
    dist.parse_config_files()
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/dist.py", line 495, in parse_config_files
    ignore_option_errors=ignore_option_errors)
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/config.py", line 111, in parse_configuration
    meta.parse()
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/config.py", line 397, in parse
    section_parser_method(section_options)
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/config.py", line 370, in parse_section
    self[name] = value
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/config.py", line 174, in __setitem__
    value = parser(value)
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/config.py", line 463, in _parse_version
    version = self._parse_attr(value, self.package_dir)
  File "/private/tmp/test/lib/python2.7/site-packages/setuptools/config.py", line 321, in _parse_attr
    value = getattr(module, attr_name)
AttributeError: 'module' object has no attribute '__version__'
```
