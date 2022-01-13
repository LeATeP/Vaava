#!/bin/bash

# to open db =  docker exec -it 938 psql -U postgres sql
            # container-id / pgres cmd / -U Username.. and db name

p_user="postgres"
p_db="sql"

if test "$1" = "create"; then # create container
docker run -dp 5432:5432 \
    --name "$p_user" \
    --restart unless-stopped \
    --network p_net --network-alias postgres \
    -v psql_data:/var/lib/postgresql/data \
    -e POSTGRES_USER="$p_user" \
    -e POSTGRES_PASSWORD=123 \
    -e POSTGRES_DB="$p_db" \
    postgres  
    exit; fi

if test "$1" = "att"; then # enter postgres
    sudo docker exec -it "$p_user" psql -U "$p_user" -d "$p_db"
    exit; fi

if test "$1" == 'q'; then # make life query 
    sudo docker exec "$p_user" psql -U "$p_user" -d "$p_db" -AF' ' --json -c "$2"
    # -F',' to add specific separate symbol
    # -t for removing column names, and row count at the buttom,
    # -A remove psql table formatting
    # --csv making csv format
    exit; fi