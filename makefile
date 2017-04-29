.PHONY: dist

dist:
	@ python setup.py sdist
	#@ mv ./dist/*.egg ./dist/eggs/

deploy:
	#LATEST=$(shell ls -t1 dist/ | head -n 1)
	#@ ls -t1 dist/ | head -n 1
	@ twine upload dist/$(file)
	#@echo $(LATEST)