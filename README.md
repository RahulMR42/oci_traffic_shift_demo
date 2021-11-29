# devops-maven-tomcat-example

Showing DevOps CI/CD workflow for a sample maven project deploying to a tomcat server

## Setup and config
1. Install JDK 11
1. Install Tomcat 9

### Configure Maven to deploy to Tomcat
In this demo, Maven is setup to publish to a Tomcat server named `TomcatServer`. Lets define that server in your Maven settings.xml

Add a new configuration

```XML
  <servers>
    <server>
        <id>TomcatServer</id>
        <username>admin</username>
        <password>YOUR-ADMIN-PASSWORD</password>
    </server>
  </servers>
```

Now lets add the admin user to Tomcat. In your `tomcat-users.xml` configuration in your tomcat `conf` directory uncomment the `tomcat-manager` roles and change the password

```XML
  <user username="admin" password="PASSWORD" roles="manager-gui, manager-script"/>
  <user username="robot" password="PASSWORD" roles="manager-script"/>
```

### Lets go!
Start tomcat: `catalina run`
Publish your example war to tomcat: `mvn tomcat7:deploy`

Procedure to run the same via Oracle Cloud Infrastrecture Devops Build and deploy services.

---------------------------------

Config files.

- [build_spec.yaml](build_spec.yaml) contains the various tages of build.
- [tomcat-manifest_privateocr.yaml](tomcat-manifest_privateocr.yaml) contains OKE manifest to deploy using a private docker repo.  

Documentation

- https://docs.oracle.com/en-us/iaas/Content/devops/using/home.htm 



