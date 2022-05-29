<p align="center"><img src="https://cdn.vectorstock.com/i/1000x1000/58/63/astronomy-isometric-horizontal-vector-40705863.webp" width="400"></p>

<h1 align="center"> 
    Prueba técnica
</h1>

<h1 align="center"> 
    Daniel Ramírez Machado
</h1>

## Proyecto

El objetivo de este proyecto es desarrollar un sistema que permita catalogar y estudiar avistamientos de asteroides a partir de observaciones obtenidas por una serie de observatorios astronómicos. 

El sistema debe almacenar de forma persistente toda la información de avistamientos suministrada mediante ficheros de textos generados por los observatorios. 

Además, debe ofrecer una interfaz web en la que se puede consultar si un asteroide ha sido visto con anterioridad y mostrar los detalles de estos avistamientos. 

## Documentación
- **[Propuesta de implementación](https://drive.google.com/file/d/1Aw4eIp6eVtWsa8nSzc98N4Wqh2fc99bJ/view?usp=sharing)** <br>
- **[Manual de Usuario](https://drive.google.com/file/d/1gkBOcnLUiqqjnnKrVH-_Ab_T8LaPJx_e/view?usp=sharing)** <br>

## Requisitos para el despliegue

- Git
- Docker

## Instrucciones para el Despliegue

1 - **Clonar el repositorio Git del proyecto mediante el siguiente comando en la consola:** 
<pre><code>git clone https://github.com/CyberDany/Reto.git</code></pre>

2 - **Entrar al directorio Reto creado**
<pre><code>cd Reto/</code></pre>

3 - **Ejecutar el siguiente comando de Docker para construir el contenedor y lanzar el servicio** 
<pre><code>docker-compose up</code> </pre>

4 - **Abrir una nueva consola y desde el directorio Reto/ ejecutar las migraciones de la Base de Datos** 
<pre><code>docker-compose exec web python manage.py migrate</code> </pre>

5 - **Ya se encuentra desplegada la aplicación, se puede acceder desde:** <br>
- http://localhost:8009/ <br>


