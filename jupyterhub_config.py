import os
import oauthenticator
from oauthenticator.google import GoogleOAuthenticator

from dockerspawner import DockerSpawner

# the Hub's API listens on localhost by default,
# but docker containers can't see that.
# Tell the Hub to listen on its docker network:
import netifaces
docker0 = netifaces.ifaddresses('docker0')
docker0_ipv4 = docker0[netifaces.AF_INET][0]
c.JupyterHub.hub_ip = docker0_ipv4['addr']

# Configuration file for jupyterhub.
c.JupyterHub.ssl_key = '/etc/letsencrypt/live/hub-tutorial.jupyter.org/privkey.pem'
c.JupyterHub.ssl_cert = '/etc/letsencrypt/live/hub-tutorial.jupyter.org/fullchain.pem'
c.JupyterHub.port = 443
c.JupyterHub.authenticator_class = 'oauthenticator.GoogleOAuthenticator'
c.JupyterHub.spawner_class = DockerSpawner
c.Jupyterhub.ip = '127.0.0.1'
c.JupyterHub.hub_port = 8081
c.JupyterHub.ssl_key = '/etc/letsencrypt/live/www.cnujpt.xyz/privkey.pem'
c.JupyterHub.ssl_cert = '/etc/letsencrypt/live/www.cnujpt.xyz/fullchain.pem'
c.JupyterHub.port = 443
c.DockerSpawner.hub_ip_address = '127.0.0.1'


# set of users allowed to use the Hub
c.Authenticator.whitelist = {'sangsulee92@gmail.com', '201202133@cs-cnu.org','201402369@cs-cnu.org', 'woojin.jo95@gmail.com'}

# set of users who can administer the Hub itself
c.Authenticator.admin_users = {'201202133@cs-cnu.org'}

# set environment path to binary files
c.GoogleOAuthenticator.client_id = os.environ['GOOGLE_CLIENT_ID']
c.GoogleOAuthenticator.client_secret = os.environ['GOOGLE_CLIENT_SECRET']
c.GoogleOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']


