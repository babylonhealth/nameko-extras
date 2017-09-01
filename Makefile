define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

coverage:
	py.test --cov-config .coveragerc --cov-report html --cov=. ./src/tests
	$(BROWSER) htmlcov/index.html

lint:
	flake8

test:
	pytest
