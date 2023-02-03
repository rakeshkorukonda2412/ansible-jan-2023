# Day 5

## Lab - Ansible Recommended Folder Structure for Inventory
```
cd ~/ansible-jan-2023
git pull
cd Day5/RecommendedDirectroyStructure/
ansible all -m ping
```

## Lab - Ansible vault
```
cd ~/ansible-jan-2023
git pull

cd Day5/vault
ansible-playbook read-from-vault-playbook.yml
```

You may also try decrypting the file
```
ansible-vault decrypt dbserver-credentials.yml
ansible-vault encrypt dbserver-credentials.yml
ansible-vault edit dbserver-credentials.yml
```
When it prompts for password, you need to type 'root' without quotes as the password.

## Lab - Handlers and Notifiers

```
cd ~/ansible-jan-2023
git pull

cd Day5/HandlersAndNotifiers/
ansible-playbook handler-and-notifiers-playbook.yml
```
