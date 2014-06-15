marklee77.slapd-auth
====================

Role to deploy slapd as auth server.

Role Variables
--------------

- slapd_run_dir: "{{ lookup('env', 'PWD') }}"

- slapd_services: "ldap:/// ldapi:///"
- slapd_ssl_cipher_suite: SECURE256:!AES-128-CBC:!ARCFOUR-128:!CAMELLIA-128-CBC:!3DES-CBC:!CAMELLIA-128-CBC 
- slapd_ssl_ca_cert_file: /etc/ssl/certs/ca-certificates.crt
- slapd_ssl_cert_file: /etc/ssl/certs/ssl-cert-snakeoil.pem
- slapd_ssl_key_file: /etc/ssl/private/ssl-cert-snakeoil.key

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
