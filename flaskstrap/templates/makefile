.PHONY: unit-tests, clean, dist

run:
	@ {{virtualenv}}/python src/{{project_name}}.py

unit-tests:
	@ {{virtualenv}}/nosetests tests/unit-tests.py

clean:
	@ rm -rf dist/

dist:
	@ mkdir -p dist/
	@ ( cd src/ && zip -r ../dist/{{project_name}}.pyx * )
	@ chmod +x dist/{{project_name}}.pyx