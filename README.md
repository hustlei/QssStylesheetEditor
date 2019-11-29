# preimport
preimport python modules to accelerate running speed and avoid "hang" when invoke module.

# Installation

~~~
python setup.py install
~~~

# Usage

~~~
from preimport import preimport

preimport('numpy', 'PyQt5')
preimport(['sys', 'os'])
~~~