# Day2

## Ansible Playbook Structure
![Ansible Playbook Structure](AnsiblePlaybookStructure.png)

## Lab - Executing an ansible playbook
```
cd ~/ansible-jan-2023
git pull

cd Day2
ansible-playbook -i ../Day1/Ansible/inventory ping-playbook.yml
```

Expected output
<pre>
(jegan@tektutor.org)$ <b>ansible-playbook -i ../Day1/Ansible/inventory ping-playbook.yml</b>

PLAY [This playbook demonstrates invoke ping module] *************************************************

TASK [Gathering Facts] *******************************************************************************
ok: [ubuntu1]
ok: [ubuntu2]

TASK [Ping the ansible node] *************************************************************************
ok: [ubuntu1]
ok: [ubuntu2]

PLAY RECAP *******************************************************************************************
ubuntu1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ubuntu2                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
</pre>
