# Manual de Instalacion de la aplicacion web

## Decisiones de proyecto 

|Elemento|Decision|Version|Justificacion|
|--------|---------|-------|---------|
|Servidor Web|Apache|2|Sencillo de usar|
|Base de Datos| MySQL|8|Experiencia previa, popular|
|Lenguaje Servidor|Pyton|3|Muy interesante para ASIR, uso Extendido|
|Framework|Flash|3|Sencillo de usar, pensado expecificamente para web (Formularios,Sesiones)|
|Control de Versiones|Git|2|Muy Extendido|
|Documentacion|Markdown|-|Muy utilizado con Github|

## Proceso de instalacion / puesta en marha

1. Actualizar el sistema
```Bash
 sudo apt update 
 sudo apr upgrade
 ```
2. Instalar git
```Bash
sudo apt install git
 ```
1. Instalar VS Code + Plugins
   - Markdown all in one
   
## Que hace un servidor web
Recibe solicitudes de un cliente y si lo encuentra se lo muestra, si no lo encuentra le dice al cliente que no lo tiene

## Cambiar permisos carpeta /var/www/html
``` BASH
sudo chown -R $USER:$USER /var/www/html
sudo chmod -R u=rwX,go=rX /var/www/html
```

## Nuestra pagina
``` Bash
mkdir -p /var/www/incidencias.ies.teis
sudo chown -R $USER:$USER /var/www/html
sudo chmod -R u=rwX,go=rX /var/www/html
```

## Foto 1
### Creamos este archivo con el siguiente texto
![Foto 1](Foto1.png)

## Foto 2
### Editamos el archivo para añadir localmente el nombre que queremos que nos aparezca ya que nuestro navegador no tiene un dns que reconozca el nombre de la pagina.
![Foto 2](Foto2.png)