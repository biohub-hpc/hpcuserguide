# Slurm REST API

This simple bit of Python will run `slurmrestd` as the user, giving access to
the full API without running a service. It's sufficient for simple and moderate
volumes of calls to the API and doesn't require any special authentication or
setup.

``` {.python}
import subprocess, os, json
from pprint import pprint as pprint

# Wrap slurmrestd so that it Just Works(tm).
# By default we return the API definition.

def request(method = 'GET', url = '/openapi'):
    command = 'echo "%s %s HTTP/1.1\r\n" | %s' % (method, url, 'slurmrestd')
    os.environ['SLURMRESTD_SECURITY'] = 'disable_user_check'
    status, output = subprocess.getstatusoutput(command)

    return output

def request_json(method = 'GET', url = '/openapi'):
    head, body = request(method, url).split('\n\n',1)
    return body

def request_dict(method = 'GET', url = '/openapi'):
    body = json.loads(request_json(method, url))
    return body

if __name__ == "__main__":
    print(request('GET', '/slurm/v0.0.38/ping'))

```
