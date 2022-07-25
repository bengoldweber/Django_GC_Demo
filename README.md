# BenGoldweber Django site demo

### Table of Contents
* Setup


### Setup
1. Create your project directory.
2. Git clone this repo
3. CD to the projects root directory and run the following commands
   1. run "pip install -r requirements.txt"
   2. ./manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
4. Copy the generated secrete key
5. Create a .evn file and place into it the following 
   1. SECRET_KEY = '{ PASTE GENERATED SECRETE KEY HERE }'
6. Navigate the manage.py and open in a editor and update
   1. runserver.default_addr = '0.0.0.0'   ---> runserver.default_addr = 'localhost'  
7. Navigate to the main settings.py file and update the following
   1. Comment out STATIC_ROOT =  os.path.join(BASE_DIR, 'static')
   2. Un Comment STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static') ]
8. Navigate to the main URLS.py file and comment out the two URLS 
   1. re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
   2. re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
9. At this point preform the standard Django migrations 
10. STATIC_ROOT = os.path.join(BASE_DIR, 'static')

