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
