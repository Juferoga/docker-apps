# Jenkins #

## ¿Que es? ##
Jenkins es un servidor de automatización escrito en Java.

## Integraciones ##

-------------------------------------
### Docker ###

Los agentes de Jenkins deben estar configurados para ser generados con contenedores de docker para evitar sobrecargar la maquina principal.

> Plugin: [Docker Plugin](https://plugins.jenkins.io/docker-plugin/)

El _Docker Plugin_ se encarga de generar un cloud para comunicar el docker de la maquina host con Jenkins para generar dinámicamente contenedores teniendo una plantilla como base.

> Ir a: Panel de Control > Administrar Nodos > Configure Clouds > Add Docker Cloud

```
Docker Cloud details...
Docker Host URI: unix:///var/run/docker.sock
Cabe tener en cuenta que para poder usar el docker.sock, el contenedor de Jenkins debe tener un volumen configurado así: /var/run/docker.sock:/var/run/docker.sock
```

Usar __Test Connection__ para asegurarnos que nuestro nodo principal tiene acceso al api de docker

```
Docker Agent templates...
PRIMERA TEMPLATE
Labels: Jenkins
Name: Jenkins
Docker Image: jenkins/agent:latest-jdk11
Container settings...
    Extra Hosts: sonar.glud.org:10.40.24.96
Remote File System Root: /home/jenkins/agent
Usar: Utilizar este nodo tanto como sea posible
Pull strategy: Pull once and update latest

Esta template deberá ser usada unicamente para procesos que no requieran comunicación con el host, y cuando se necesite realizar un análisis de código con Sonarqube.

Es preferible dejar configurada esta template como la template por defecto para cualquier nodo, para evitar huecos de seguridad.

SEGUNDA TEMPLATE
Labels: Glud
Name: Glud
Docker Image: glud/jenkins-dind-agent:latest-alpine-jdk11
Container settings...
    Mounts: type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock,ro=true
    Run container privileged: true
Remote File System Root: /home/jenkins/agent
Usar: Dejar este nodo para ejecutar sólamente tareas vinculadas a él
Pull strategy: Pull once and update latest

Esta template debido a sus permisos como administrador y acceso al docker del host, se recomienda usar únicamente para procesos de construcción de imagenes de docker y despliegues de servicios en la maquina host.
```

Finalmente, se recomienda dejar en 0 el número de ejecutores para el nodo principal, debido a que si algo falla en las ejecuciones del nodo principal, todo el servicio puede fallar.

-------------------------------------
### Sonarqube ###

> Plugin: [SonarQube Scanner for Jenkins](https://plugins.jenkins.io/sonar/)

#### **Extra Host** ####
El servico cuenta con integración con Sonarqube para la automatizacion de análisis de codigo. Aun que en el docker-stack.yml está especificado un __extra_host__ es preferible asegurarse que se está configurado correctamente.

```console
ifconfig eth0
```

La ip que resulte del anterior comando debe ser igual a la indicada en _extra_host_.

#### **SonarQube servers** ####
```
Desde Panel de Control > Configurar el Sistema

Generar una instalación de SonarQube con el nombre de Sonarqube.

URL del servidor: https://sonar.glud.org
Server authentication token: SonarQube Access Token
Webhook Secret: SonarQube Secret Webhook
Debe existir una credencial con ese nombre, y debe tener el mismo valor que el secret configurado en el webhook del servicio de Sonarqube.
```

#### **SonarQube Scanner** ####
```
Desde Panel de Control > Global Tool Configuration > SonarQube Scanner

Añadir SonarQube Scanner...
    Name: Sonarqube
    Instalar automáticamente...
        Versión: La más actual que exista
```
-------------------------------------
### Integración con GitLab ###

> Plugin: [Gitlab for jenkins](https://plugins.jenkins.io/gitlab-plugin/)

Desde gitlab crear un Acces token para el acceso a Jenkins, tipo API (super acceso practicamente)

Agregar la nueva credencial a Jenkins.

Agregar la configuración de gitlab al servidor 

----
Name : Gitlab
URL: https://gitlab.com/
Credential: la creada anteriormente
---

Añadir pipeline como item a producción/slud
Basarse en slud xviii :)

Pipeline: -> cambiar el secret key id.
Docker Deploy: -> Environment {conexion con firebase}

### IMPORTANTE ###
Verificar plugins (nodejs) xD
## Configuración plugin node js
Version LTS: 16.16.0
usar yarn
-------------------------------------
## Ejecución ##
Para desplegar el servicio bajo los parametros actuales del grupo (Haciendo uso de treaefik como proxy reverso).

```console
docker stack deploy -c docker-stack.yml jenkins
```
