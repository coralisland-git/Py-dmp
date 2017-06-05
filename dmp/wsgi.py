import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/web-user/.virtualenvs/dmp/lib/python3.4/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/var/www/html/data-management-platform/dmp')
sys.path.append('/var/www/html/data-management-platform/dmp/dmp')

os.environ['DJANGO_SETTINGS_MODULE'] = 'dmp.settings'

# Activate your virtual env
activate_env=os.path.expanduser("/home/web-user/.virtualenvs/dmp/bin/activate_this.py")
#python2+ style
#execfile(activate_env, dict(__file__=activate_env))

#python3+ style
exec(compile(open(activate_env, "rb").read(), activate_env, 'exec'), dict(__file__=activate_env))
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
