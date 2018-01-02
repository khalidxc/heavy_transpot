import sys
sys.path.append('/var/www/app.swe363.ml/awesome-calendar/')
from mainapp import app as application
application.secret_key = '123456789'
application.debug = True
