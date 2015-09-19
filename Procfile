web: gunicorn -k eventlet -w ${WEB_CONCURRENCY:-5} "TileStache:WSGITileServer('tilestache.cfg')" --log-file - --max-requests 5000
