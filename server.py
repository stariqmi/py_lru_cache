from flask import Flask, request, abort, jsonify
from cache.lru_cache import LruCache

app = Flask(__name__)

lru_cache = LruCache(10)


@app.route("/<key>", methods=["GET"])
def get_from_cache(key):
    value = lru_cache.get(key)

    if value:
        return jsonify(success=True, value=value)

    resp = jsonify(success=False)
    resp.status_code = 404
    return resp


@app.route("/", methods=["POST", "PUT"])
def insert_into_cache():
    data = request.get_json(force=True)
    lru_cache.insert(str(data["key"]), data["value"])

    return jsonify(success=True)


@app.route("/<key>", methods=["DELETE"])
def delete_from_cache(key):
    lru_cache.delete(key)
    return jsonify(success=True)
