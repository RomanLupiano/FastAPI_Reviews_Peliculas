1. python -m venv env  
2. source ./env/bin/activate  
3. pip install fastapi  
4. pip install peewee  
5. pip install python-dotenv
6. Ingresar a Mysql y crear la base de datos con nombre "fastapi_reviews_peliculas" 
7. Crear y configurar el archivo .env con los datos para la conexión a Mysql
7. uvicorn main:app --reload  

Desde /docs se pueden ver los endpoints y mandar peticiones


TODOs:
CRUD Movies  
Read y Delete Users  
No permitir más de una reseña por usuario  