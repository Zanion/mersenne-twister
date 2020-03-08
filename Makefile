all:
	python setup.py build_ext -if


clean:
	rm -r build src/mersenne_random/mt_random_type.c mt_random_type*.so
