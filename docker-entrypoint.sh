# spawning poetry shell
# exec poetry shell

# start server @ 0.0.0.0:80
cd api
exec uvicorn app:app --host 0.0.0.0 --port 80 --reload