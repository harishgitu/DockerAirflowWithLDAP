#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""Default configuration for the Airflow webserver"""
import os

from flask_appbuilder.security.manager import AUTH_LDAP

AUTH_TYPE = AUTH_LDAP
AUTH_LDAP_SERVER = "ldap://openldap:389"
AUTH_LDAP_USE_TLS = False

AUTH_LDAP_SEARCH = "dc=airsoft,dc=com"  # the LDAP search base
AUTH_LDAP_UID_FIELD = "cn"  # the username field

# For a typical OpenLDAP setup (where LDAP searches require a special account):
# The user must be the LDAP USER as defined in LDAP_ADMIN_USERNAME
AUTH_LDAP_BIND_USER = "cn=admin,dc=airsoft,dc=com"  # the special bind username for search
AUTH_LDAP_BIND_PASSWORD = "admin"  # the special bind password for search

# registration configs
AUTH_USER_REGISTRATION = True  # allow users who are not already in the FAB DB
AUTH_USER_REGISTRATION_ROLE = "Public"  # this role will be given in addition to any AUTH_ROLES_MAPPING
AUTH_LDAP_FIRSTNAME_FIELD = "givenName"
AUTH_LDAP_LASTNAME_FIELD = "sn"
AUTH_LDAP_EMAIL_FIELD = "mail"  # if null in LDAP, email is set to: "{username}@email.notfound"

# a mapping from LDAP DN to a list of FAB roles
AUTH_ROLES_MAPPING = {
    "cn=Enterprise,ou=Groups,dc=airsoft,dc=com": ["Enterprise"],
    "cn=Admin,ou=Groups,dc=airsoft,dc=com": ["Admin"],
}

# the LDAP user attribute which has their role DNs
AUTH_LDAP_GROUP_FIELD = "memberOf"

# if we should replace ALL the user's roles each login, or only on registration
AUTH_ROLES_SYNC_AT_LOGIN = True

# force users to re-auth after 30min of inactivity (to keep roles in sync)
PERMANENT_SESSION_LIFETIME = 1800