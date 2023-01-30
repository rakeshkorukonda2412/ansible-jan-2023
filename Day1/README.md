# Day 1

## What is a provisioner tool?
- this type of tools helps us creating a virtual machine locally or on cloud on demand
- Examples
  - Vagrant 
    - using declarative code we can create virtual machine on virtual box or VMWare hypervisors
  - Terraform ( Infrastruction automation tools )
     - can automate provisioning on any cloud (Local environment, AWS, AZure, Digital Ocean, GCP .,)
  - Cloudformation ( Infrastruction automation tools )
    - a proprietary tool used within AWS to automate infrastructure
    - doesn't support Azure, GCP, Digital Ocean, etc.,

## What is Configuration Management Tool?
- helps us in automating software installation of local as well as on remote servers
- on existing infrastructure software installation automations can be automated using Configuration Management Tools
- Examples
  - Chef
  - Puppet
  - SaltStack ( Salt )
  - Ansible
  
## Chef, Puppet and SaltStack
- they follow Client/Server Architecture
- Domain Specific Language ( language in which automation code is written )
  - Ruby ( scripting language )
  - learning curve is steep
- You need to install proprietrary tools for developing automation code
- You need to install proprietary agent tools on the Chef/Puppet Nodes
- Installation is complex
- Follows pull-based architecture

## Ansible
- agentless i.e you don't need to install any proprietary tools in order to perform automated installations on the Ansible nodes
- follows a PUSH based architecture
- doesn't follow client/server architecture
- the machine where Ansible is installed is called as Ansible Controller Machine(ACM)
- this can only be Linux and Unix like OS
- Windows server/OS can never act as an Ansible Controller Machine
- ansible can automate software installations on
  - Unix
  - Linux
  - Windows
  - Mac
  - Cisco Routers/Switches, etc.,
- Domain Specific Language (DSL)
  - YAML ( Yet Another Markup Langauage )
- Ansible is developed in Python by Michael Deehan ( a former Red Hat employee )
- Michael Deehan started a company called Ansible Inc, through this company he developed Ansible Core as an opensource product
- Red Hat acquired Ansible Inc, Ansible Core is a Red Hat product
- Red Hat started developing an Enterprise variant of Ansible core called Ansible Tower
- Ansible Core supports only Command LIne Interface (CLI)
- Ansible Tower supports 
    - developed on top of Ansible Core, hence all playbooks written for Ansible core will also
      work in Ansible Tower
    - Web console (GUI)
    - User Management
    - Support from Red Hat
    - You could see the history of playbook executions and logs, metrics ,etc in GUI


## What is an Ansible Node?
- is the server where automated software installations must be performed
- Ansible Nodes can be a
  - Windows machine
  - Mac OS-X
  - Unix
  - Linux ( all distributions )
  - Switches & Routers, etc.,
- Windows Ansible Nodes
  - software requirements
    - Powershell should be there (.Net Framework)
    - WinRM should be configured for connectivity
- Unix/Mac/Linux Ansible Nodes
  - Software requirements
    - Python should be there
    - SSH Server should be installed for connectivity

## Installing Ansible in Ubuntu
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible
```

## Cloning TekTutor Training Repository
```
cd ~
git clone https://github.com/tektutor/ansible-jan-2023
```

## Lab - Building a customer Ubuntu Docker Image to create Ubuntu Ansible Node
```
cd ~/ansible-jan-2023
git pull

cd Day1/CustomDockerImages/ubuntu
ssh-keygen
docker build -t tektutor/ansible-ubuntu:latest .
```
