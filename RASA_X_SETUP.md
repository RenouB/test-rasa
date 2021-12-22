# Deploy Rasa-X on a single server using docker-compose.

- Install Rasa-X for docker-compose:  
```
    curl -sSL -o install.sh https://storage.googleapis.com/rasa-x-releases/1.0.1/install.sh
    sudo bash ./install.sh
```
- Clone domain-db repo. the rasa actions server will have the domain repo mounted, so the deployed database can more easily be tinkered with.
```
    git clone https://github.com/RenouB/domain-db.git
```

- Make domain-db repo venv and install dependencies:
```
    python3 setup.py develop
```
- Download docker-compose.override.yml and docker-compose.env, place in rasa deployment directory (default: /etc/rasa)
```
    wget https://raw.githubusercontent.com/RenouB/test-rasa/main/docker-compose.env 
    wget https://raw.githubusercontent.com/RenouB/test-rasa/main/docker-compose.override.yml 
```

- In docker-compose.env file, set custom username and password for domain knowledge database.
- In docker-compose.env, Set path for domain-db repo. 
- Append these variables to /etc/rasa/.env

- Make directory domain_db in /etc/rasa. This directory will be mounted to the domain_db container, so that the database persists after container shutdown.
- Make user postgres on host, give this user permissions to /etc/rasa/{db,domain_db}

- Run docker compose:
```
    sudo docker-compose up -d
```

- Create password for rasa x admin user:
```
    sudo python rasa_x_commands.py create --update admin admin <PASSWORD>
```

- Initialize domain knowledge database:
```
    sudo docker-compose exec app bash -c "cd /app/actions/domain-db/domain_db && alembic upgrade head"
    sudo docker-compose exec app bash -c "cd /app/actions/domain-db/domain_db && python3 init_database.py"
```

- Open Rasa X in browser by navigating to server IP address. Use menu on lefthand side to connect to the Rasa assistant repo (currently: https://github.com/RenouB/test-rasa.git). Rasa X will provide SSH key, which must be added to repo. Use GUI to train and deploy model. Sometimes things are a bit buggy. If responses don't work, close browser and try again, or try accessing the assistant through generate-conversation-link feature.