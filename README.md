### Setup

Unzip the file into airflow_with_ldap folder on wsl2

you will get below files and folders
```bash
.:
config  dags  data  docker-compose.yaml  ldap  logs  plugins

./config:
webserver_config.py

./dags:

./data:
./data/certificates:
airsoft.com.ca.crt  airsoft.crt  airsoft.key
./data/slapd:
./data/slapd/config:
./data/slapd/database:

./logs:

./plugins:
```
#### Start the container
1. copy the files from `sample_dags` into `dags` directory
3. Stay in the airflow_with_ldap folder (where `docker-compose.yaml` file is located) and run
```bash
docker-compose up -d
```
* ignore `-d` option if you want to see realtime logs
* ***Make sure the directories `./data/slapd` and `./logs` have extended write permissions***

#### Configure OpenLDAP
1. Go to `localhost:8081` in your browser to open LdapAdmin
2. Login using `cn=admin,dc=airsoft,dc=com` as username and `admin` as password
3. Click on `import` option and select the `bootstrap.ldif` file

#### Login to Airflow
1. Go to `localhost:8080` in your browser
2. Login using `aadmin` as username and `airflow` as password

#### Configure John Doe enterprise user
1. Login to airflow as aadmin (admin user)
2. Click on Security >> List Roles
3. Copy "User" role to "Enterprise" (select User role and click on Actions>>Copy Role, edit the newly created UserCopy)
4. Edit Enterprise role and 
  - Delete `can read on Dags` and `can edit on Dags`
  - Add `can edit on DAG:ent_dag` and `can read on DAG:ent_dag`
5. Logout of admin user and login using `jdoe` and `john`

##### Additional Reading
- [Mark Lamberti Blog](https://www.notion.so/Airflow-with-LDAP-in-10-mins-cbcbe5690d3648f48ee7e8ca45cb755f#26bcef44783e40efa49aa2aca5b45716)
- [osixia/docker-openldap](https://github.com/osixia/docker-openldap)
- [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html)
