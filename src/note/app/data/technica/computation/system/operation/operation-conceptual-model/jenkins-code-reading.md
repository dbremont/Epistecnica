# Jenkins Code Reading


> Jenkins is an event-driven, distributed automation server that orchestrates and executes CI/CD workflows, defined as jobs or pipelines, across a dynamically allocated set of compute nodes. It provides a plugin-extensible execution model, enabling integrations with SCMs, artifact repositories, cloud environments, and external services, while supporting declarative and imperative pipeline definitions for software delivery and infrastructure automation.
> 

## Smallest Possible Workflow

> 

## Lines of Code

> `cloc .`
> 

![image.png](data/technica/computation/system/operation/operation-conceptual-model/assets/jenkins-code-reading/image.png)

## Building

> 

```bash
git clone https://github.com/jenkinsci/jenkins.git
cd jenkins
mvn clean install
```

## Installation

> 

### Local

> 

### Docker

```bash
docker pull jenkins/jenkins:lts

docker volume create jenkins_home

docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts
  
  
## Set UP
docker exec -it jenkins /bin/bash
cat /var/jenkins_home/secrets/initialAdminPassword

## Agents
# Create jenkins group
sudo groupadd jenkins

# Create jenkins user and add to jenkins group
sudo useradd -m -s /bin/bash -g jenkins jenkins

# Create /var/jenkins directory if it does not exist
sudo mkdir -p /var/jenkins

# Set ownership and permissions
sudo chown -R jenkins:jenkins /var/jenkins
sudo chmod -R 755 /var/jenkins

ls -ld /var/jenkins
sudo -u jenkins ls /var/jenkins

## Switch to the jenkins user to execute the command:
sudo su - jenkins

## For my agent; go to http://localhost:8080/computer for yours
curl -sO http://localhost:8080/jnlpJars/agent.jar
java -jar agent.jar -url http://localhost:8080/ -secret cea61092b2dc8796999bd51fbba6081b727417483f367e0aa9c4ff417d0c006c -name localhost -webSocket -workDir "/var/jenkins"

```

## Agents  Deployment:  Container

> How to deploy the **Jenkins Agent** in a Container?
> 

## Configuration

> 

## References

- https://github.com/jenkinsci/jenkins
- [Scripting Integration](note.html?n=technica/computation/language-system/conceptual-model-language-system/scripting-integration.md)
- https://www.jenkins.io/doc/book/using/using-agents/clear