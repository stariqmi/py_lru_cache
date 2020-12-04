This cache is implemented in Python, following a Least Recently Used eviction policy.

The data itself is stored in memory and is lost when the server is restarted. A Flask server provides a minimal HTTP API for the following operations:

- insert - `POST /`, `{"key": <key>, "value": <value>}`
- get - `GET /<key>`
- update - `PUT /`, `{"key": <key>, "value": <value>}`
- delete - `DELETE /<key>`

In addition to the above, the following administrative operations are also supported:

- backup - `PUT /backup`
- flush - `PUT /flush`
- restore - `PUT /restore`, `{"file_path": <file_path>}`

## Setup
- `pip3 install -r requirements.txt`

## Running the server
- `export CACHE_CAPACITY=10` - Default 10
- `export FLASK_APP=server.py`
- `flask run`

## Potential Improvments
- Automatic and continuous persistence (for disaster recovery or restoring the cache on server restart)
- Logging - this can also server the purpose of a commit log, both for restoring data and handling concurrency issues
- Support for different eviction policies e.g. Least Frequently Used (LFU)
- RPC interface to call the different operations instead of the HTTP e.g. via gPRC