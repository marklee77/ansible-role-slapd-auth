marklee77.slapd-auth
====================

Role to deploy slapd as auth server.

Role Variables
--------------

- slapd_bind_address: 127.0.0.1
- slapd_ssl_cert_file: /etc/ssl/certs/ssl-cert-snakeoil.pem
- slapd_ssl_key_file: /etc/ssl/private/ssl-cert-snakeoil.key

- ldap_ldap_port: 389
- ldap_ldaps_port: 689
- ldap_enable_ssl: true
- ldap_require_ssl: true

- ldap_domain: localdomain
- ldap_base_dn: dc=localdomain
- ldap_admin_password: password

Example Playbook
-------------------------

- hosts: all
  sudo: True
  roles:
    - marklee77.slapd-auth

License
-------

GPLv2

Author Information
------------------

http://marklee77.github.io/
