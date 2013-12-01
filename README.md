pyCaBi
======

Python tools for working with [Capital Bikeshare](http://www.capitalbikeshare.com/) (CaBi) data.

####Installation

````sh
git clone https://github.com/dbarlett/pycabi.git
cd pycabi
virtualenv .
source bin/activate
pip install -r requirements.txt
python -m tests/test_utils
````

####Usage

````python
import pycabi
cabi = pycabi.get_system_status()
for station in cabi.values():
    print station.name, station.nb_bikes, station.nb_empty_docks

````

See the [wiki](https://github.com/dbarlett/pycabi/wiki/_pages) for data source notes.