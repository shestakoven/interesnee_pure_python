import json

import requests

ENVS = {
    'qa': 'backend-qa.usummitapp.com',
    'dev': 'backend-dev.usummitapp.com',
}

CHECKS = ['Cache', 'Database', 'Email']

TIMEOUT = 20

MSGS = {
    'unknown': 'error (unknown) status code:',
    'env_err': 'environment is not available',
    'url_err': 'URL not found',
    'auth_err': 'authentication error',
    'ok': 'OK',
}


def main(env):
    """Run development sites health-checks

    This function goes to a corresponding env site, gets current health checks
    state

    """
    print(f"Env: {env}")

    if env not in ENVS:
        raise Exception(f'{env} {MSGS["env_err"]}')

    checks_params = '&' \
        .join([f'checks={i}' for i in CHECKS])
    domain = ENVS[env]
    health_check_url = f'https://{domain}/api/v1/utils/health-check/' \
                       f'?{checks_params}'
    try:
        http_response = requests.get(health_check_url, timeout=TIMEOUT)
        status_code = http_response.status_code
    except requests.exceptions.ConnectionError:
        raise Exception(f'HealthCheck: {MSGS["url_err"]}')

    if status_code == requests.status_codes.codes.BAD_REQUEST:
        raise Exception(f'HealthCheck: {MSGS["auth_err"]} '
                        f'status code: {status_code}')

    if status_code != requests.status_codes.codes.OK:
        raise Exception(f'HealthCheck: {MSGS["unknown"]} '
                        f'status code {status_code}')

    data = json.loads(http_response.text)
    print(f'Health check: status {status_code}, content: {json.dumps(data)}')

    errors = [k for k, v in data.items() if v != MSGS['ok']]
    if errors:
        print(f'Env: {env} error - {", ".join(errors)}')
        raise Exception(f'HealthCheck: {", ".join(errors)} errors')

    print(f"Env: {env} success - {json.dumps(data)}")
    return print(f'HealthCheck: {MSGS["ok"]}')


if __name__ == '__main__':
    main('dev')
