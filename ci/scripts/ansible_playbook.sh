#!/bin/sh
set -e

uname -a
which ansible
ansible --version

# TODO copy secrets

# Setup Private Key
mkdir -p /root/.ssh
echo "AMILLER_IM_PRIVATE_KEY" > /root/.ssh/id_rsa
chmod 600 /root/.ssh/id_rsa

# Setup ssh config
echo -e "Host *\n\tStrictHostKeyChecking no\n\n" > /root/.ssh/config


cd amiller_im_git
ansible-playbook -s -i environment playbooks/system.yml
ansible-playbook -s -i environment playbooks/application.yml