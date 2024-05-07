# Panther

pipeline for testing python cloud apps

<p align="left">
  <img src="./panther.png" width="250">
</p>

Welcome to Panther, your go-to solution for testing Python cloud applications! 🎉

Panther is a robust, efficient, and flexible testing pipeline designed specifically for Python cloud apps. With Panther, you can streamline your testing process, catch bugs early, and ensure your cloud applications are performing at their best. 🚀

## 🧪 Features

- **Automated Testing**: Set up your tests and let Panther do the rest. No more manual testing!
- **Cloud-Focused**: Designed with cloud applications in mind. Panther understands the complexities and challenges of testing in the cloud.
- **Python-Centric**: Built for Python developers, by Python developers. Panther speaks your language.

Join us on this exciting journey and let's make Python cloud apps testing easier and more efficient together! 🤝


## Install Jenkins

``` bash
docker pull jenkins/jenkins:lts
docker volume create jenkins-data2

docker run -p 8080:8080 -p 50000:50000 -v jenkins-data2:/var/jenkins_home --name myjenkins jenkins/jenkins:lts

```

Jenkins initial setup is required. An admin user has been created and a password generated.
Please use the following password to proceed to installation:

96dfa9a2ec9c4fa0912572bf99f45d4d

## Script when build is triggered. 

``` bash 

echo "Build completed at $(date)" >> build_log.txt

```


some changes 


``` dns

docker run -d \
  --name=duckdns \
  --net=host `#optional` \
  -e PUID=1000 `#optional` \
  -e PGID=1000 `#optional` \
  -e TZ=Etc/UTC `#optional` \
  -e SUBDOMAINS=pantherchaos.duckdns.org \
  -e TOKEN=39343eea-e111-483f-a9ce-d32159355c77 \
  -e UPDATE_IP=ipv4 `#optional` \
  -e LOG_FILE=false `#optional` \
  -v /path/to/duckdns/config:/config `#optional` \
  --restart unless-stopped \
  lscr.io/linuxserver/duckdns:latest

```