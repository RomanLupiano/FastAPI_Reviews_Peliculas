## API REST con FastAPI
### Este proyecto fue para probar FastAPI, permite a los usuarios autenticarse y realizar reviews de peliculas.

#### Pasos a seguir
1. python -m venv env  
2. source ./env/bin/activate  
3. pip install fastapi  
4. pip install uvicorn
4. pip install peewee  
5. pip install python-dotenv
6. pip install pyjwt
7. Ingresar a Mysql y crear la base de datos con nombre "fastapi_reviews_peliculas" 
8. Crear y configurar el archivo .env con los datos para la conexión a Mysql y una secret key
9. uvicorn main:app --reload    

Desde /docs se pueden ver los endpoints y mandar peticiones



### Tecnologías y herramientas utilizadas 🛠️
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Requests](https://pypi.org/project/requests/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [Typing](https://docs.python.org/3/library/typing.html)
- [Peewee](https://docs.peewee-orm.com/en/latest/) -> MySQL
- [pyJWT](https://pyjwt.readthedocs.io/en/stable/) -> OAuth2 con JWT


### Algunas cosas para implementar 📜
- Requirement.txt
- Read y Delete Users  
- No permitir más de una reseña por usuario  
- Script SQL para cargar con datos de ejemplo
- Dockerizar