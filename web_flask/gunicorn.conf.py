import os

bind = "0.0.0.0:5000"
workers = os.cpu_count() * 2 + 1
reload = True
