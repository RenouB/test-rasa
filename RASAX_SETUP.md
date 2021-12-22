Install Rasa X for docker-compose.

curl -sSL -o install.sh https://storage.googleapis.com/rasa-x-releases/1.0.1/install.sh
sudo sh ./install.sh

Create password for admin user
sudo python rasa_x_commands.py create --update  admin me <PASSWORD>

clone domain DB repo
https://github.com/RenouB/domain-db.git


fetch docker-compose.override.yml and docker-compose.env

make directory domain_db in /etc/rasa
fetch .env file
set credentials
run docker compose
initialize database
open rasa in browser. connect to assist repo. Train and deploy model.
