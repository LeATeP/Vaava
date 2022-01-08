# REQUIREMENTS 

- Linux
- Docker
- Python/bash

1. set up image "docker build -t game ."

2. create db container "run my_whatever/game_docker/pdb create" # creating postgres db

3. change project location in "create_hub" / "silence_container" to your project clone location and run docker container script "my_whatever/game_docker/create_hub"

4. to test that everything worked you can run "items.py" or "my_whatever/game_docker/hub/items.py"


# Describing scripts/actions/commands of the game

# miner unit is normal unit, but he maxing skills in mining, and earn xp in mining

1. `get 'table'` getting items/units/units_info (statistic) whatever data user required

2. `create_unit` summon new unit for resources expense, the more you feed the better unit will be come.. 
minimum 10, create minimum unit, if you put 100, chances of summoning will be 1-3 for stats, 5-15xp. level is not random, but initial XP is.. 

3. `mining 'id'` together with `silent_container` sends unit to mine

4. `battle 'id'` send unit to attack `mob_id`  