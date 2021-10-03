### Setup

Unzip the file into airflow_with_ldap folder on wsl2

you will get below files and folders
```bash
.:
config  dags  data  docker-compose.yaml  ldap  logs  plugins

./config:
webserver_config.py

./dags:
enterprise_dag.py  marketing_dag.py

./data:
./data/certificates:
airsoft.com.ca.crt  airsoft.crt  airsoft.key
./data/slapd:
./data/slapd/config:
./data/slapd/database:

./ldap:
bootstrap.ldif

./logs:

./plugins:
```
#### Start the container
Stay in the airflow_with_ldap folder (where `docker-compose.yaml` file is located) and run
```bash
docker-compose up -d
```
***Make sure the directories `./data/slapd` and `./logs` have extended write permissions***

#### Configure OpenLDAP
1. Go to `localhost:8081` in your browser to open LdapAdmin
2. Login using `cn=admin,dc=airsoft,dc=com` as username and `admin` as password
3. Click on `import` option and select the `bootstrap.ldif` file from `/ldap` folder

#### Login to Airflow
1. Go to `localhost:8080` in your browser
2. Login using `hswayampakula` as username and `harish` as password

#### Configure John Doe enterprise user
1. Login to airflow as hswayampakula (admin user)
2. Click on Security >> List Roles
3. Copy "User" role to "Enterprise" (select User role and click on Actions>>Copy Role, edit the newly created UserCopy)
4. Edit Enterprise role and 
  - Delete `can read on Dags` and `can edit on Dags`
  - Add `can edit on DAG:ent_dag` and `can read on DAG:ent_dag`
5. Logout of admin user and login using `jdoe` and `john`

