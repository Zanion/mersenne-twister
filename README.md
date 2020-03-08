Cython Mersenne Twister Wrapper
---

Exercise in wrapping the [Mersenne Twister](http://bit.ly/mersenne_twister) C library with Cython.

Mersenne Twister (MT) is a pseudorandom number genreating algorithm developed by Makoto Matsumoto and Takuji Nisimura in 1996/1997.

Mersenne Twister gets its name as it uses Mersenne primes, has ancestry involving the Twisted GFSR, plus as a bonus MT is the initials of the creators.

This is an extension of the work from the [Cython Book](http://shop.oreilly.com/product/0636920033431.do) by Kurt Smith

Install
---

This project does expect that your system has the dependency tools required to build C & python extensions installed on the system.

 * gcc
 * python-dev
 * make

Use the pipenv dependency management tool to initialize a virtualenv and install all python dependencies from the included pipfile.

```shell
pipenv install
```

You can get access to the virtualenv shell via `pipenv shell` where you can build.


Building
---

From within the shell you can build the project using make
```shell
make
```

alternatively you can explictly build using the included setup.py
```shell
python setup.py build_ext --if
```

Testing
---

Tests can be ran within the virtualenv using pytest
```shell
pytest
```
