# install locust and httpx
pip install locust

# run each asgi
- hypercorn app.main:app -c hypercorn_config.toml
- uvicorn app.main:app --host 127.0.0.1 --port 8000

# set and run the test
Set number of users (e.g. 100)
Set spawn rate (e.g. 10)
Start Swarming
