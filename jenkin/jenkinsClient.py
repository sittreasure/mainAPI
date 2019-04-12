from django.conf import settings
from jenkins import Jenkins, JenkinsException

bucket = 'mockjsp'
folder = 'playground'

class JenkinsClient:
  __jenkin = None

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    url = getattr(settings, 'JENKINS_URL')
    username = getattr(settings, 'JENKINS_USERNAME')
    password = getattr(settings, 'JENKINS_PASSWORD')
    self.__jenkin = Jenkins(url, username=username, password=password)
  
  def __createJenkinsFile(self):
    tomcatCredentail = getattr(settings, 'TOMCAT_CREDENTAIL')
    tomcatIp = getattr(settings, 'TOMCAT_IP')
    xml = "<?xml version='1.1' encoding='UTF-8'?>"
    xml += "<project>"
    xml += "<actions/>"
    xml += "<description></description>"
    xml += "<keepDependencies>false</keepDependencies>"
    xml += "<properties/>"
    xml += "<scm class='hudson.scm.NullSCM'/>"
    xml += "<canRoam>true</canRoam>"
    xml += "<disabled>false</disabled>"
    xml += "<blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>"
    xml += "<blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>"
    xml += "<triggers/>"
    xml += "<concurrentBuild>false</concurrentBuild>"
    xml += "<builders>"
    xml += "<hudson.tasks.Shell>"
    xml += "<command>mc cp --recursive miniostorage/{name}/{folder} .</command>".format(name=bucket, folder=folder)
    xml += "</hudson.tasks.Shell>"
    xml += "<hudson.tasks.Shell>"
    xml += "<command>mvn -f {folder}/pom.xml clean package</command>".format(folder=folder)
    xml += "</hudson.tasks.Shell>"
    xml += "</builders>"
    xml += "<publishers>"
    xml += "<hudson.plugins.deploy.DeployPublisher plugin='deploy@1.13'>"
    xml += "<adapters>"
    xml += "<hudson.plugins.deploy.tomcat.Tomcat8xAdapter>"
    xml += "<credentialsId>{credential}</credentialsId>".format(credential=tomcatCredentail)
    xml += "<url>http://{ip}:8080</url>".format(ip=tomcatIp)
    xml += "</hudson.plugins.deploy.tomcat.Tomcat8xAdapter>"
    xml += "</adapters>"
    xml += "<contextPath>{name}</contextPath>".format(name=bucket)
    xml += "<war>**/*.war</war>"
    xml += "<onFailure>false</onFailure>"
    xml += "</hudson.plugins.deploy.DeployPublisher>"
    xml += "</publishers>"
    xml += "<buildWrappers/>"
    xml += "</project>"
    return xml

  def createJob(self, jobName):
    result = None
    configXml = self.__createJenkinsFile()
    try:
      self.__jenkin.create_job(jobName, configXml)
      pass
    except JenkinsException as err:
      result = False
      pass
    return result

  def buildJob(self, jobName):
    result = None
    try:
      self.__jenkin.build_job(jobName)
      pass
    except JenkinsException as err:
      result = False
      pass
    return result
