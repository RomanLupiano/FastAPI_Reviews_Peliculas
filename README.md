## API REST con FastAPI
### Este proyecto fue para probar FastAPI, permite a los usuarios autenticarse y realizar reviews de peliculas.

#### Pasos a seguir
1. python -m venv env  
2. source ./env/bin/activate  
3. pip install -r requirements.txt
4. Ingresar a Mysql y crear una base de datos con nombre "fastapi_reviews_peliculas" (Las tablas se crean solas)
5. Crear el archivo .env con los datos para la conexión a Mysql y una secret key para JWT (revisar .env_example)
6. uvicorn main:app --reload    

Desde /docs se pueden ver los endpoints y mandar peticiones


### Framework y herramientas utilizados 🛠️
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Requests](https://pypi.org/project/requests/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [Typing](https://docs.python.org/3/library/typing.html)
- [Peewee](https://docs.peewee-orm.com/en/latest/) -> MySQL
- [pyJWT](https://pyjwt.readthedocs.io/en/stable/) -> OAuth2 con JWT