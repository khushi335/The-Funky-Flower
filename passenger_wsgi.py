import os
import sys

# Path to your project directory
BASE_DIR = "/home/hightech/project.hornetspestcontrols.com/flower"
sys.path.insert(0, BASE_DIR)

# Activate virtual environment (optional in Passenger, but sometimes helpful)
activate_env = "/home/hightech/virtualenv/project.hornetspestcontrols.com/flower/3.10/bin/activate_this.py"

if os.path.exists(activate_env):
    with open(activate_env) as f:
        exec(f.read(), {'__file__': activate_env})

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flower.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()