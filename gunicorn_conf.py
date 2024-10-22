import multiprocessing

max_requests = 1000

max_requests_jitter = 50

loglevel="info"

accesslog = "/home/ubuntu/itauv2/api_token_itau/logs/access.log"
errorlog = "/home/ubuntu/itauv2/api_token_itau/logs/error.log"

bind = "0.0.0.0:8000"

worker_class = "uvicorn.workers.UvicornWorker"

workers = (multiprocessing.cpu_count() * 2) + 1