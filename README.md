marklee77.slapd-auth
====================

[![Build Status](https://travis-ci.org/marklee77/ansible-role-slapd-auth.svg?branch=master)](https://travis-ci.org/marklee77/ansible-role-slapd-auth)

Role to deploy slapd as auth server.

Role Variables
--------------

- slapd_run_dir: "{{ lookup('env', 'PWD') }}"

- slapd_services: "ldap:/// ldapi:///"
- slapd_ssl_cipher_suite: SECURE256:!AES-128-CBC:!ARCFOUR-128:!CAMELLIA-128-CBC:!3DES-CBC:!CAMELLIA-128-CBC 
- slapd_ssl_ca_cert_file: /etc/ssl/certs/ca-certificates.crt

- slapd_hostname: localhost
- slapd_ssl_cert_file: /etc/ssl/certs/{{ slapd_hostname|replace(".", "_") }}.crt
- slapd_ssl_key_file: /etc/ssl/private/{{ slapd_hostname|replace(".", "_") }}.key

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

http://stillwell.me
