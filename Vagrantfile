# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "trusty64"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  config.vm.network "forwarded_port", guest:  389, host: 8389,
    auto_correct: true

  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
  end

  #config.vm.provision "ansible" do |ansible|
  #  ansible.playbook = "getroles.yml"
  #end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "site.yml"
    ansible.extra_vars = {
      ldap_require_ssl: false
    }
  end
end
