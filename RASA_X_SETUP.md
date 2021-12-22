Deploy Rasa-X on a single server using docker-compose.

Install Rasa-X for docker-compose:
curl -sSL -o install.sh https://storage.googleapis.com/rasa-x-releases/1.0.1/install.sh
sudo sh ./install.sh

clone domain-db repo. the rasa actions server will have the domain repo mounted, so the deployed database can more easily be tinkered with.
https://github.com/RenouB/domain-db.git

make domain-db venv and install dependencies:
python3 setup.py develop

fetch docker-compose.override.yml and docker-compose.env, place in rasa deployment directory (default: /etc/rasa)
wget https://raw.githubusercontent.com/RenouB/test-rasa/main/docker-compose.env 
wget https://raw.githubusercontent.com/RenouB/test-rasa/main/docker-compose.override.yml 

In docker-compose.env, set custom username and password for domain knowledge database.
In docker-compose.env, Set path for domain-db repo. 
Append these variables to /etc/rasa/.env

make directory domain_db in /etc/rasa. This directory will be mounted to the domain_db container, so that the database persists after container shutdown.
make user postgres on host, give permissions to /etc/rasa/{db,domain_db}

run docker compose:
sudo docker-compose up -d

Create password for rasa x admin user:
sudo python rasa_x_commands.py create --update admin admin <PASSWORD>

initialize domain knowledge database:
sudo docker-compose exec app bash -c "cd /app/actions/domain-db/domain_db && alembic upgrade head"
sudo docker-compose exec app bash -c "cd /app/actions/domain-db/domain_db && python3 init_database.py"

Open rasa in browser. Use menu on lefthand side to connect to rasa assistant repo. Provided Rasa X SSH key must be added to repo. Use GUI to train and deploy model.
