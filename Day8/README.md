# Day 8

## Agile vs Waterfall

### Waterfall
- customer feedback comes pretty delayed


### Agile
- Fail fast ( frequent customer feedbacks )
- Customer himself/herself is not clear about all the features
- product will evolve gradually
- Agile Frameworks
  - SCRUM
    - Daily standup meeting
      - it is an inspect and adapt meeting (fail-fast)
      - the team would have had some plan for yesterday
      - the team in this meeting will compare the actual status with the planned status
      - 
  - Kanban
  - XP
  - SAFE

## Waterfall
- Framework


## What is DevOps?
- a way of working
- its a combination of tools and practices that gives the confidence to deliver
  frequent release with confidence
- Dev
  - daily activity, developing features, fixing bugs
  - are expected to automated unit and integration test cases (TDD)
  - automating dev setup is a responsibility of Developers 
- QA
  - automating test cases 
  - QA engineer is responsible to setup the QA environment Ansible kind of devops tools
    Operation Teams
- Operations Team
  - 

## What is Continuous Integration (CI)?
- integrating your code changes several time a day
- when code is committed, you have tools and process in place that grabs the new code changes, triggers build, runs automated test cases, share the build report (feedback)
- Unit Test Test and Integration Test and component test, API Test

## What is Continuous Deployment(CD)?
- the CI certified binaries will be deployed automatically to QA environent for further testing

## What is Continuous Delivery (CD)?
- automated delivery of QA certified binaries to the customer's environemtn ( pre-prod environment )

## Download jenkins from jenkins.io/Download
```
cd ~/Downloads
wget https://get.jenkins.io/war-stable/2.375.2/jenkins.war
```

Starting jenkins
```
cd ~/Downloads
java -jar ./jenkins.war
```

You need to install the below plugins in Jenkins
1. Ansible
2. Ansible Tower
3. Maven Integration
4. Docker
5. Build Pipeline

## Installing Maven 
```
cd ~/Downloads
wget https://dlcdn.apache.org/maven/maven-3/3.9.0/binaries/apache-maven-3.9.0-bin.tar.gz
tar xvfz apache-maven-3.9.0-bin.tar.gz
cd apache-maven-3.9.0
pwd
```

## Installing Docker in Ubuntu
```
sudo apt-get update
sudo apt-get install -y docker.io
docker --version
sudo usermod -aG docker $USER
sudo su $USER
docker images
```
