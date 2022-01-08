#!/bin/bash

psql_conn () {
    psql -h "$PSQL_HOST" -U "$PSQL_USER" -d "$PSQL_DB" --csv -c "$1" 
}

psql_conn "$@"
