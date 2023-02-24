# Sonarqube #

## ¿Que es? ##
Sonarqube es una herramienta de automatización para el análisis de calidad y seguridad de código

## Requerimientos ##
El servicio requiere un ajuste a nivel de host para el correcto funcionamiento del servidor de busqueda Elasticsearsh

```console
sysctl -w vm.max_map_count=524288
```

## Integraciones ##

-------------------------------------

### Jenkins ###

#### **Extra Host** ####
El servico cuenta con integración con jenkins para la automatizacion de análisis de codigo. Aun que en el docker-stack.yml está especificado un __extra_host__ es preferible asegurarse que se está configurado correctamente.

```console
ifconfig eth0
```

La ip que resulte del anterior comando debe ser igual a la indicada en _extra_host_

#### **Token** ####
Jenkins requiere un token para tener acceso al api de sonar. Para obtener un token es necesario tener configurado al usuario general del grupo.

```
Desde Administration > Security > Users

En el apartado de Tokens, generar uno con el nombre de 'Jenkins' y almacenarlo en las credenciales del servicio de Jenkins con el nombre de 'SonarQube Access Token'.
```

#### **Webhook** ####
Finalmente para mantener una comunicación bidireccional entre Jenkins y Sonarqube, es necesario un webhook que le indicará a Jenkins cuando haya terminado un análisis.

```
Desde Administration > Configuration > Webhooks > Create

Name: Puede ser cualquiera

Url: https://jenkins.juferoga.tk/sonarqube-webhook

Secret: Puede ser cualquiera, pero debe ser el mismo que el definido en el servicio de Jenkins
```
-------------------------------------

## Ejecución ##
Para desplegar el servicio bajo los parametros actuales del grupo (Haciendo uso de treaefik como proxy reverso)

```console
docker stack deploy -c docker-stack.yml sonarqube
```
