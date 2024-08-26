# Tarea 1 INF-326 Arquitectura De Software

### Requisitos

* Tener instalado Docker con Docker Compose.

## Instrucciones

### Compilación y Ejecución

[**Video Demostrativo**](https://youtu.be/51LUfBn4Src)

1. En una terminal, para iniciar los contenedores Docker utilizar el siguiente comando:

    ```
    docker-compose up -d
    ```

2. Desde un navegador, acceder a [http://localhost:3000](http://localhost:3000) para acceder a Grafana. Ingresar con usuario y contraseña `admin`, y luego saltar el cambio de contraseña.

3. Configurar Loki, para eso se debe agregar una data source, seleccionar Loki y luego cambiar la URL a `http://loki:3100`. Apretar botón de guardar y probar. Se sugiere luego explorar el data source. 

4. Ingresar a [http://localhost:8001](http://localhost:8001) para enviar logs desde el servicio 1 y [http://localhost:8002](http://localhost:8002) para enviar logs desde el servicio 2. Cada vez que se accede a los servicios se envia un log a través de Loki. En el data source de Loki, utilizar como query con label `job = fastapi` o como formato código `{job="fastapi"}`, ejecutar query y observar en vivo los logs.

5. Configurar un dashboard, seleccionando el data source anterior configurado. Seleccionar en la query como label `job = fastapi` o como formato código `{job="fastapi"}`, ejecutar query y aplicar para guardar la dashboard.


6. Para cerrar los contenedores, en una terminal ejecutar el siguiente comando:

    ```
    docker-compose down
    ```