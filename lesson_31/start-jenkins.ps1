docker pull jenkins/jenkins:lts
docker rm -f jenkins-training

docker run -d -p 8080:8080 -p 50000:50000 --name jenkins-training `
-v jenkins_home:/var/jenkins_home -u root `
-e JAVA_OPTS="-Djenkins.install.runSetupWizard=false" `
jenkins/jenkins:lts /bin/bash -c " `
    apt-get update && `
    apt-get install -y python3 python3-full python3-pip && `
    pip3 install pytest --break-system-packages && `
    jenkins-plugin-cli --plugins workflow-aggregator git junit email-ext && `
    /usr/bin/tini -- /usr/local/bin/jenkins.sh"

Start-Sleep -Seconds 3
Start-Process http://localhost:8080