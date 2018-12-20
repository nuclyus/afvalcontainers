#!/usr/bin/env bash

# Import sidcon live weeg en vullgraad gegevens.

set -u   # crash on missing env variables
set -e   # stop on any error
set -x   # print what we are doing

DIR=`dirname "$0"`

dc() {
	docker-compose -p enevocontainers${ENVIRONMENT} -f ${DIR}/docker-compose.yml $*
}

ENV="acceptance"
if [ "$ENVIRONMENT" == "production" ]; then
  ENV="production"
fi

# Download latest dump from objectstore
dc run --rm importer python -m objectstore.databasedumps /data db_dumps --download-db

dc exec -T database pg_restore --no-privileges --no-owner --if-exists -j 4 -c -C -d postgres -U afvalcontainers /data/database.$ENV


trap 'dc kill ; dc down ; dc rm -f' EXIT

dc down
dc rm -f
dc pull
dc build

# create enevo tables if not exists
dc run --rm importer python enevo/models.py

# Importeer enevo api endpoints
dc run --rm importer python enevo/slurp.py content_types
dc run --rm importer python enevo/slurp.py sites
dc run --rm importer python enevo/slurp.py site_content_types
dc run --rm importer python enevo/slurp.py container_types
dc run --rm importer python enevo/slurp.py container_slots
dc run --rm importer python enevo/slurp.py containers
# dc run --rm importer python enevo/slurp.py alerts

# Insert data into django ENEVO database tables
dc run --rm importer python enevo/copy_to_django.py content_types
dc run --rm importer python enevo/copy_to_django.py sites
dc run --rm importer python enevo/copy_to_django.py site_content_types
dc run --rm importer python enevo/copy_to_django.py container_types
dc run --rm importer python enevo/copy_to_django.py container_slots
dc run --rm importer python enevo/copy_to_django.py containers

dc run --rm importer python enevo/copy_to_django.py container_slots --link_container_slots
dc run --rm importer python enevo/copy_to_django.py containers --validate_containers

echo "Running backups"
dc exec -T database backup-db.sh afvalcontainers

echo "Store DB dump in objectstore for next step"
dc run --rm importer python -m objectstore.databasedumps /backups/database.dump db_enevo --upload-db
dc run --rm importer python -m objectstore.databasedumps /backups/database.dump db_enevo --days 20

dc down -v
