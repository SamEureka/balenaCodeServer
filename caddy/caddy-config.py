## Caddy Configurator
## Sam Dennon // 2022
## Updated // July 2024

import os
import subprocess
import re
import textwrap

## Removes all the crazy indenting caused by the multi-line strings.
defunk = textwrap.dedent

## Grab some of the device variables
DNS_RESOLVERS = os.environ['DNS_RESOLVERS'] if 'DNS_RESOLVERS' in os.environ else '1.1.1.1'
DNS_EMAIL = os.environ['DNS_EMAIL'] if 'DNS_EMAIL' in os.environ else ''
DNS_PROVIDER = os.environ['DNS_PROVIDER'] if 'DNS_PROVIDER' in os.environ else 'XXX'
DNS_API_KEY = os.environ['DNS_API_KEY'] if 'DNS_API_KEY' in os.environ else 'XXX'
BASIC_AUTH_USER = os.environ['BASIC_AUTH_USER'] if 'BASIC_AUTH_USER' in os.environ else 'admin'
BASIC_AUTH_PASSWORD = os.environ['BASIC_AUTH_PASSWORD'] if 'BASIC_AUTH_PASSWORD' in os.environ else 'password'

## Generate hashed password using Caddy's built-in utility
def generate_hashed_password(password):
    result = subprocess.run(['caddy', 'hash-password', '--plaintext', password], capture_output=True, text=True)
    return result.stdout.strip()

hashed_password = generate_hashed_password(BASIC_AUTH_PASSWORD)

## Pulls all the HOSTs out of the device variables and puts them in a list of dicts.
## Format for device variable - Name: HOST_<number>, Value: <host>|<domain>|<ip>|<port>|<wildcard (true or false)>|<auth_req (true or false)>
## The name must start with 'HOST_' and have a number. The value must be separated with the pipe symbol '|'
def create_env_list():
    output = []
    for key, val in os.environ.items():
        if re.match("HOST_[0-9]", key):
            host = val.split('|')
            if len(host) == 6:  # Expecting an additional auth_req flag
                try:
                    output.append({
                        'host': host[0],
                        'domain': host[1],
                        'ip': host[2],
                        'port': host[3],
                        'wildcard': host[4],
                        'auth_req': host[5]  # Add auth_req flag
                    })
                except IndexError:
                    print('''
        FORMAT ERROR: Check HOST variable format.
        EXPECTING: <host>|<domain>|<ip>|<port>|<wildcard (true or false)>|<auth_req (true or false)>
        ''')
    return output

def generate_site_block():
    env_list = create_env_list()
    if not env_list:
        return '!! No hosts found !!'
    
    temp_list = []
    for env in env_list:
        if env['wildcard'] == 'true':
            temp_list.append(f"*.{env['host']}.{env['domain']} ")
        temp_list.append(f"{env['host']}.{env['domain']} ")
    
    return ''.join(temp_list)


## Creates the tls resource options
## Required device variables - DNS_PROVIDER and DNS_API_KEY
## Optional device variable - DNS_EMAIL
def generate_tls_options():
    if (DNS_API_KEY == 'XXX' or DNS_PROVIDER == 'XXX'):
        return f"""
          Create DNS_PROVIDER and/or DNS_API_KEY device variables in balena.io console
    """
    else:
        tls_temp = f"""
      tls {DNS_EMAIL} {{
        dns {DNS_PROVIDER} {DNS_API_KEY}
        resolvers {DNS_RESOLVERS}
      }}
    """
        return tls_temp


## Creates the resource blocks. Will let user know if there are not any hosts to proxy.
def generate_matcher_options():
    list = create_env_list()
    if (list == []):
        return """
    !! Create HOST_<number> device variable in balena.io console       !!
    !! Format for device variable -                                    !!
    !!  Name: HOST_<number>                                            !!
    !!  Value: <host>|<domain>|<ip>|<port>|<wildcard (true or false)>|<auth_req (true or false)>  !!
    !! The name must start with 'HOST_' and have a number.             !!
    !! The value must be separated with the pipe symbol '|'            !!
    """
    temp_list = []
    for e in list:
        basicauth_block = f"""
            basicauth {{
                {BASIC_AUTH_USER} {hashed_password}
            }}
        """ if e['auth_req'] == 'true' else ''

        if (e['wildcard'] == 'true'):
            temp_list.append(f"""
        @{e['host']}wild host *.{e['host']}.{e['domain']}
          handle @{e['host']}wild {{
            {basicauth_block}
            reverse_proxy {e['ip']}:{e['port']}
        }}        
      """)
        temp_list.append(f"""
      @{e['host']} host {e['host']}.{e['domain']}
        handle @{e['host']} {{
          {basicauth_block}
          reverse_proxy {e['ip']}:{e['port']}  
      }}
    """)
    return ''.join(temp_list)


def write_caddyfile():
    if os.path.exists('/etc/caddy/Caddyfile'):
        os.remove("/etc/caddy/Caddyfile")
    with open('/etc/caddy/Caddyfile', 'a') as cf:
        temp_string = f"""
    # Caddy configuration file
    # This file is auto-generated on startup, changes to the file will not persist.
    # See https://github.com/SamEureka/balenaCaddyReverser for configuration options.

    {generate_site_block()} {{
    {generate_tls_options()}
    {generate_matcher_options()}
    }}
    """
        defunked = defunk(temp_string)
        cf.write(defunked)


## Write the Caddyfile to /etc/caddy/Caddyfile
write_caddyfile()

## Use caddy format to correct any problems with the formatting.
os.system('caddy fmt --overwrite /etc/caddy/Caddyfile')
## Print it to console so we can see what is being proxied.
os.system('cat /etc/caddy/Caddyfile')
## Start the caddy server passing in our new config file.
## If there aren't any HOSTs... don't start Caddy
if (create_env_list() != []):
    os.system('caddy run --config /etc/caddy/Caddyfile --adapter caddyfile')


## Idle... I like balena-idle as a fallback for troubleshooting. You can comment this out if you like.
os.system('balena-idle')