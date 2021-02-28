# APIDjango

# Intrucciones para ejecutar el proyecto:
Ejecutar el comando docker-compose up para levantar la maquina

![imagen](https://user-images.githubusercontent.com/7074426/109414828-b97ed480-797a-11eb-829b-7f10be8c6ef7.png)


# Abrir el navegador e ir a la url de localhost

http://localhost:8000/

![imagen](https://user-images.githubusercontent.com/7074426/109414863-019df700-797b-11eb-9486-470c32cce0ed.png)

# Ruta para los servicios

http://localhost:8000/api/

La base de datos estará vacia, para probar la funcionalidad de los servicios, es necesario crear al menos dos clientes y articulos

![imagen](https://user-images.githubusercontent.com/7074426/109415304-7f630200-797d-11eb-9e29-a2b750967335.png)



# Para crear un pedido, se tendra que hacer con la siguiente estructura. Tenemos que mandar el cliente, y los articulos, order_number es un valor unico

{
        "order_number": 3,
        "customer": 1,
        "is_urgent": true,
        "order_type": "CEDIS",
        "cedis": "MTY",
        "reference": "1234",
        "brach_code": null,
        "partner_code": null,
        "is_supplied": false,
        "order_details": [
            {
                "quantity": 10,
                "article": 1
            }
        ]
    }
    
 
# Servicio que ejecuta la consulta

![imagen](https://user-images.githubusercontent.com/7074426/109415213-f946bb80-797c-11eb-8633-3175045e7382.png)

# Podemos obtener pedidos pasandole un id al servicio

http://localhost:8000/api/order/1/

![imagen](https://user-images.githubusercontent.com/7074426/109415236-2d21e100-797d-11eb-8166-f4a37f86c333.png)


