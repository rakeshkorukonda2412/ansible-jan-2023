# Day 3

## Preparing a Custom CentOS Ansible Node Docker Image
```
cd ~/ansible-jan-2023
git pull
cd Day1/CustomDockerImages/centos
cp ~/.ssh/id_rsa.pub authorized_keys
docker build -t tektutor/ansible-centos:latest .
docker images
```

### Testing the image
```
docker run -d --name centos1 --hostname centos1 -p 2003:22 -p 8003:80 tektutor/ansible-centos:latest
docker run -d --name centos2 --hostname centos2 -p 2004:22 -p 8004:80 tektutor/ansible-centos:latest
```

Try to SSH into the containers
```
ssh -p 2003 root@localhost
```

Expected output
<pre>
(jegan@tektutor.org)$ ssh -p 2003 root@localhost
The authenticity of host '[localhost]:2003 ([127.0.0.1]:2003)' can't be established.
RSA key fingerprint is SHA256:5GdavdewIACRnUD/lTr4ROohfTTYOrRXA1BacoZSA/o.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '[localhost]:2003' (RSA) to the list of known hosts.
[root@centos1 ~]# exit
logout
Connection to localhost closed.
</pre>

## ⛹️‍♀️ Lab - Running the playbook on Ubuntu and CentOS nodes
```
cd ~/ansible-jan-2023
git pull

cd Day3
ansible-playbook  install-nginx-playbook.yml
```

Expected output
```
(jegan@tektutor.org)$ ansible-playbook install-nginx-playbook.yml

PLAY [This playbook will install nginx, configures web root folder, deploys custom web page] *****************************

TASK [Gathering Facts] ***************************************************************************************************
ok: [ubuntu1]
ok: [ubuntu2]
ok: [centos1]
ok: [centos2]

TASK [Install nginx in Ubuntu] *******************************************************************************************
skipping: [centos1]
skipping: [centos2]
ok: [ubuntu1]
ok: [ubuntu2]

TASK [Install Extra packages for Enterprise Linux (EPEL) in CentOS] ******************************************************
skipping: [ubuntu1]
skipping: [ubuntu2]
ok: [centos1]
ok: [centos2]

TASK [Install nginx in CentOS] *******************************************************************************************
skipping: [ubuntu1]
skipping: [ubuntu2]
ok: [centos2]
ok: [centos1]

TASK [Configure nginx web root folder in Ubuntu] *************************************************************************
skipping: [centos1]
skipping: [centos2]
ok: [ubuntu2]
ok: [ubuntu1]

TASK [Configure nginx web root folder in CentOS] *************************************************************************
skipping: [ubuntu1]
skipping: [ubuntu2]
ok: [centos1]
ok: [centos2]

TASK [Create custom nginx web root folder] *******************************************************************************
ok: [ubuntu1]
ok: [ubuntu2]
ok: [centos1]
ok: [centos2]

TASK [Restart the nginx web server service in Ubuntu] ********************************************************************
skipping: [centos1]
skipping: [centos2]
changed: [ubuntu2]
changed: [ubuntu1]

TASK [Start the nginx web server service in CentOS] **********************************************************************
skipping: [ubuntu1]
skipping: [ubuntu2]
changed: [centos1]
changed: [centos2]

TASK [Deploy custom web page] ********************************************************************************************
ok: [ubuntu2]
changed: [centos2]
changed: [centos1]
ok: [ubuntu1]

PLAY RECAP ***************************************************************************************************************
centos1                    : ok=7    changed=2    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0   
centos2                    : ok=7    changed=2    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0   
ubuntu1                    : ok=6    changed=1    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   
ubuntu2                    : ok=6    changed=1    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   

(jegan@tektutor.org)$ curl localhost:8003
<html>
    <head>
        <title>Welcome to DevOps!</title>
    </head>
    <body>
        <h1>Provisioned by Docker</h1>
        <h1>Configured by Ansible</h1>
        <h1>Hostname - centos1</h1>
        <h1>OS - CentOS v7.9</h1>
    </body>
</html>
(jegan@tektutor.org)$ curl localhost:8004
<html>
    <head>
        <title>Welcome to DevOps!</title>
    </head>
    <body>
        <h1>Provisioned by Docker</h1>
        <h1>Configured by Ansible</h1>
        <h1>Hostname - centos2</h1>
        <h1>OS - CentOS v7.9</h1>
    </body>
</html>
(jegan@tektutor.org)$ curl localhost:8001
<html>
    <head>
        <title>Welcome to DevOps!</title>
    </head>
    <body>
        <h1>Provisioned by Docker</h1>
        <h1>Configured by Ansible</h1>
        <h1>Hostname - ubuntu1</h1>
        <h1>OS - Ubuntu v16.04</h1>
    </body>
</html>
(jegan@tektutor.org)$ curl localhost:8002
<html>
    <head>
        <title>Welcome to DevOps!</title>
    </head>
    <body>
        <h1>Provisioned by Docker</h1>
        <h1>Configured by Ansible</h1>
        <h1>Hostname - ubuntu2</h1>
        <h1>OS - Ubuntu v16.04</h1>
    </body>
</html>
```

## ⛹️‍♀️ Lab - Running the refactored playbook on Ubuntu and CentOS nodes
```
cd ~/ansible-jan-2023
git pull

cd Day3/refactored_playbook-v1
ansible-playbook  install-nginx-playbook.yml
```

Expected output
```
(jegan@tektutor.org)$ ansible-playbook install-nginx-playbook.yml 

PLAY [This playbook will install nginx, configures web root folder, deploys custom web page] *****************************

TASK [Gathering Facts] ***************************************************************************************************
ok: [ubuntu2]
ok: [centos1]
ok: [ubuntu1]
ok: [centos2]

TASK [include_tasks] *****************************************************************************************************
included: /home/jegan/ansible-jan-2023/Day3/refactored_playbook/install-nginx-ubuntu.yml for ubuntu1, ubuntu2, centos1, centos2

TASK [Install nginx in Ubuntu] *******************************************************************************************
skipping: [centos1]
skipping: [centos2]
ok: [ubuntu1]
ok: [ubuntu2]

TASK [include_tasks] *****************************************************************************************************
included: /home/jegan/ansible-jan-2023/Day3/refactored_playbook/install-nginx-centos.yml for ubuntu1, ubuntu2, centos1, centos2

TASK [Install Extra packages for Enterprise Linux (EPEL) in CentOS] ******************************************************
skipping: [ubuntu1]
skipping: [ubuntu2]
ok: [centos1]
ok: [centos2]

TASK [Install nginx in CentOS] *******************************************************************************************
skipping: [ubuntu1]
skipping: [ubuntu2]
ok: [centos1]
ok: [centos2]

TASK [include_tasks] *****************************************************************************************************
included: /home/jegan/ansible-jan-2023/Day3/refactored_playbook/configure-nginx-ubuntu.yml for ubuntu1, ubuntu2, centos1, centos2

TASK [Configure nginx web root folder in Ubuntu] *************************************************************************
skipping: [centos1]
skipping: [centos2]
ok: [ubuntu2]
ok: [ubuntu1]

TASK [include_tasks] *****************************************************************************************************
included: /home/jegan/ansible-jan-2023/Day3/refactored_playbook/configure-nginx-centos.yml for ubuntu1, ubuntu2, centos1, centos2

TASK [Configure nginx web root folder in CentOS] *************************************************************************
skipping: [ubuntu1]
skipping: [ubuntu2]
ok: [centos1]
ok: [centos2]

TASK [include_tasks] *****************************************************************************************************
included: /home/jegan/ansible-jan-2023/Day3/refactored_playbook/restart-nginx-ubuntu.yml for ubuntu1, ubuntu2, centos1, centos2

TASK [Restart the nginx web server service in Ubuntu] ********************************************************************
skipping: [centos1]
skipping: [centos2]
changed: [ubuntu2]
changed: [ubuntu1]

TASK [include_tasks] *****************************************************************************************************
included: /home/jegan/ansible-jan-2023/Day3/refactored_playbook/restart-nginx-centos.yml for ubuntu1, ubuntu2, centos1, centos2

TASK [Check if nginx web server is already up and running] ***************************************************************
skipping: [ubuntu1]
skipping: [ubuntu2]
changed: [centos1]
changed: [centos2]

TASK [Start the nginx web server service in CentOS] **********************************************************************
skipping: [ubuntu1]
skipping: [ubuntu2]
skipping: [centos1]
skipping: [centos2]

TASK [include_tasks] *****************************************************************************************************
included: /home/jegan/ansible-jan-2023/Day3/refactored_playbook/deploy-custom-webpage.yml for ubuntu1, ubuntu2, centos1, centos2

TASK [Create custom nginx web root folder] *******************************************************************************
ok: [ubuntu1]
ok: [centos1]
ok: [centos2]
ok: [ubuntu2]

TASK [Deploy custom web page] ********************************************************************************************
ok: [ubuntu2]
ok: [ubuntu1]
ok: [centos1]
ok: [centos2]

PLAY RECAP ***************************************************************************************************************
centos1                    : ok=14   changed=1    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   
centos2                    : ok=14   changed=1    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   
ubuntu1                    : ok=13   changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
ubuntu2                    : ok=13   changed=1    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0
```

## ⛹️‍♀️ Lab - Running the refactored playbook on Ubuntu and CentOS nodes
```
cd ~/ansible-jan-2023
git pull

cd Day3/refactored_playbook-v2
ansible-playbook  install-nginx-playbook.yml
```

Expected output
```
```

## Lab - Using list variables in Ansible Playbook
```
cd ~/ansible-jan-2023
git pull

cd Day3/loops/list
ansible-playbook  playbook.yml
```

## Lab - Using dictionary variables in Ansible Playbook
```
cd ~/ansible-jan-2023
git pull

cd Day3/loops/dictionary
ansible-playbook  playbook.yml
```

## Lab - Using list variables in Ansible Playbook
```
cd ~/ansible-jan-2023
git pull

cd Day3/loops/sequence
ansible-playbook  playbook.yml
```
