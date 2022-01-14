#!/bin/bash

# PSQL_HOST=postgres
# PSQL_USER=postgres
# PSQL_DB=sql

psql_conn () {
    psql -h "$PSQL_HOST" -U "$PSQL_USER" -d "$PSQL_DB" -c "select * from items;" 
}

psql_conn "$@"
