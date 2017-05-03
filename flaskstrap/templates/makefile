ifndef username
	username := {project_name}_admin
endif

ifndef host_address
	# replace this value with your VPS address
	host_address := 127.0.0.1
endif

#ifndef TARGET_DIR
#	TARGET_DIR := /home/{username}/{project_name}
#endif

.PHONY: unit-tests, clean, dist

run:
	@ {virtualenv}/python src/{project_name}.py

unit-tests:
	@ {virtualenv}/nosetests tests/unit-tests.py

clean:
	@ rm -rf dist/

dist:
	@ mkdir -p dist/
	@ (cd src/ && zip -r ../dist/{project_name}.zip *)
	@ echo '#!/usr/bin/env python' | cat - dist/{project_name}.zip > dist/{project_name}
	@ chmod +x dist/{project_name}
	@ rm dist/{project_name}.zip

deploy:
	@ rsync --delete-after --quiet -rlptuPO --chmod=g+w ./dist/ ${username}@${host_address}:/home/${username}/{project_name}
	ssh ${username}@${host_address} 'cd /home/${username}/{project_name} && pm2 restart {project_name}'
