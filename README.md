# preimport
preimport python modules to accelerate running speed and avoid "hang" when invoke module.

# Installation

~~~shell
pip install preimport
~~~

# Usage

~~~python
from preimport import preimport

preimport('numpy', 'PyQt5')
preimport(['sys', 'os'])
~~~