This cache is implemented in Python, following a Least Recently Used eviction policy. The data itself is stored in memory and is lost when the server is restarted. A Flask server provides a minimal API for the following operations:
- insert - `POST /`, `{"key": <key>, "value": <value>}`
- update (via insert)
- get `GET /<key>`
- delete `DELETE /<key>`

## Setup
- `pip3 install -r requirements.txt`

## Running the server
- `export FLASK_APP=server.py`
- `flask run`

## Potential Improvments
- Persistence (for disaster recovery or restoring the cache on server restart)
- Support for different eviction policies e.g. Least Frequently Used (LFU)
- RPC interface to call the different operations instead of the HTTP e.g. via gPRC