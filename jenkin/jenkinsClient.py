from django.conf import settings
from jenkins import Jenkins, JenkinsException

class JenkinsClient:
  __jenkin = None

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    url = getattr(settings, 'JENKINS_URL')
    username = getattr(settings, 'JENKINS_USERNAME')
    password = getattr(settings, 'JENKINS_PASSWORD')
    self.__jenkin = Jenkins(url, username=username, password=password)
  
  def __createJenkinsFile(self, jobName, bucket, folder):
    tomcatCredential = getattr(settings, 'TOMCAT_CREDENTIAL')
    tomcatIp = getattr(settings, 'TOMCAT_IP')
    minioUrl = getattr(settings, 'MINIO_URL')
    minioAccessKey = getattr(settings, 'MINIO_ACCESS_KEY')
    minioSecretKey = getattr(settings, 'MINIO_SECRET_KEY')

    xml = "<?xml version='1.1' encoding='UTF-8'?>"
    xml += "<maven2-moduleset plugin='maven-plugin@3.4'>"
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
    xml += "<rootModule>"
    xml += "<groupId>playground</groupId>"
    xml += "<artifactId>PlaygroundApp</artifactId>"
    xml += "</rootModule>"
    xml += "<rootPOM>playground/pom.xml</rootPOM>"
    xml += "<goals>clean package</goals>"
    xml += "<aggregatorStyleBuild>true</aggregatorStyleBuild>"
    xml += "<incrementalBuild>false</incrementalBuild>"
    xml += "<ignoreUpstremChanges>false</ignoreUpstremChanges>"
    xml += "<ignoreUnsuccessfulUpstreams>false</ignoreUnsuccessfulUpstreams>"
    xml += "<archivingDisabled>false</archivingDisabled>"
    xml += "<siteArchivingDisabled>false</siteArchivingDisabled>"
    xml += "<fingerprintingDisabled>false</fingerprintingDisabled>"
    xml += "<resolveDependencies>false</resolveDependencies>"
    xml += "<processPlugins>false</processPlugins>"
    xml += "<mavenValidationLevel>-1</mavenValidationLevel>"
    xml += "<runHeadless>false</runHeadless>"
    xml += "<disableTriggerDownstreamProjects>false</disableTriggerDownstreamProjects>"
    xml += "<blockTriggerWhenBuilding>true</blockTriggerWhenBuilding>"
    xml += "<settings class='jenkins.mvn.DefaultSettingsProvider'/>"
    xml += "<globalSettings class='jenkins.mvn.DefaultGlobalSettingsProvider'/>"
    xml += "<reporters/>"
    xml += "<publishers>"
    xml += "<hudson.plugins.deploy.DeployPublisher plugin='deploy@1.15'>"
    xml += "<adapters>"
    xml += "<hudson.plugins.deploy.tomcat.Tomcat8xAdapter>"
    xml += "<credentialsId>{credential}</credentialsId>".format(credential=tomcatCredential)
    xml += "<url>http://{ip}:8080</url>".format(ip=tomcatIp)
    xml += "<path></path>"
    xml += "</hudson.plugins.deploy.tomcat.Tomcat8xAdapter>"
    xml += "</adapters>"
    xml += "<contextPath>{name}</contextPath>".format(name=jobName)
    xml += "<war>**/*.war</war>"
    xml += "<onFailure>false</onFailure>"
    xml += "</hudson.plugins.deploy.DeployPublisher>"
    xml += "</publishers>"
    xml += "<buildWrappers/>"
    xml += "<prebuilders>"
    xml += "<hudson.tasks.Shell>"
    xml += "<command>mc config host add miniostorage https://{url} {accessKey} {secretKey}</command>".format(url=minioUrl, accessKey=minioAccessKey, secretKey=minioSecretKey)
    xml += "</hudson.tasks.Shell>"
    xml += "<hudson.tasks.Shell>"
    xml += "<command>mc cp --recursive miniostorage/{name}/{folder} .</command>".format(name=bucket, folder=folder)
    xml += "</hudson.tasks.Shell>"
    xml += "</prebuilders>"
    xml += "<postbuilders/>"
    xml += "<runPostStepsIfResult>"
    xml += "<name>FAILURE</name>"
    xml += "<ordinal>2</ordinal>"
    xml += "<color>RED</color>"
    xml += "<completeBuild>true</completeBuild>"
    xml += "</runPostStepsIfResult>"
    xml += "</maven2-moduleset>"
    return xml

  def __getBuildNumber(self, jobName):
    info = self.__jenkin.get_job_info(jobName)
    return info['lastBuild']['number']

  def createJob(self, jobName, bucket, folder):
    result = None
    configXml = self.__createJenkinsFile(jobName, bucket, folder)
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

  def getBuildInfo(self, jobName):
    buildNumber = self.__getBuildNumber(jobName)
    info = self.__jenkin.get_build_info(jobName, buildNumber)
    return info

  def getConsoleLog(self, jobName):
    buildNumber = self.__getBuildNumber(jobName)
    log = self.__jenkin.get_build_console_output(jobName, buildNumber)
    return log
