.PHONY: all clean test
all: __pycache__/main.cpython-35.pyc

__pycache__/main.cpython-35.pyc: main.py
	python3 -m compileall main.py

clean:
	$(RM) -r __pycache__/

test:
	@expr $$(python3 main.py "Hello") == "olleH"
