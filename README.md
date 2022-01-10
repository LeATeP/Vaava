# REQUIREMENTS 

- Linux/MacOs
- Docker
- Python/bash


1. create database, 'Vaava/postgresql.sh create' it's the main element of the game

2. main commands: 'hub/get' 'hub/create_unit' 'mining.py', the rest basically not working and req refactory  

3. creating db schemas req manually, sql query's in 'sql/schemas_sql

# Describing scripts/actions/commands of the game
# miner unit is normal unit, but he maxing skills in mining, and earn xp in mining

1. `get 'table'` getting items/units/units_info (statistic) whatever data user required

2. `create_unit` summon new unit for resources expense, the more you feed the better unit will be come.. 
minimum 10, create minimum unit, if you put 100, chances of summoning will be 1-3 for stats, 5-15xp. level is not random, but initial XP is.. 

3. `mining 'id'` together with `silent_container` sends unit to mine

4. `battle 'id'` send unit to attack `mob_id`  