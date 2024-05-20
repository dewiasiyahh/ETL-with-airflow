## PostgreSQL Docker

1. Create folder postgresql
2. Create docker-compose.yml
3. docker-compose.yml Code:
```
version: '2'
services:
  postgres-msib:
    image: postgres:15
    container_name: postgres-msib
    env_file:
      - .env
    volumes:
      - /var/lib/postgresql/data
    ports:
      - 5436:5432/tcp
```
4. Create `.env` file with this code
```
POSTGRES_PASSWORD = postgres
POSTGRES_USER = postgres
POSTGRES_DB = postgres
POSTGRES_HOST_AUTH_METHOD=trust
```
5. Go to postgresql directory 
6. jalankan docker dengan command `docker compose up`
7. Buat koneksi dengan postgresql bisa pake extension mysql di vs code

## Python Code
requirement module
- sqlalchemy
- openpyxl

Code to Install 
```
!pip install sqlalchemy
!pip install openpyxl
```