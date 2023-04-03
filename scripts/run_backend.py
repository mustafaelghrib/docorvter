#!/usr/bin/python

import argparse
import subprocess
import sys

parser = argparse.ArgumentParser()

parser.add_argument("--env", help="Env File")
parser.add_argument("--image", help="Docker Image Name")

args = parser.parse_args()

env = args.env
image = args.image

list_containers = f'docker ps -a -q'
process = subprocess.run(list_containers, shell=True, stdout=subprocess.PIPE)
result = process.stdout.decode('utf-8')
if result != "":
    remove_containers = f'docker rm -f $(docker ps -a -q)'
    process = subprocess.run(remove_containers, shell=True, stdout=subprocess.PIPE)
    print(process.stdout.decode('utf-8'))

run_django_container = f'echo "run_django_container";' \
                       f'docker run -d -p 80:8000 ' \
                       f'--env-file {env} ' \
                       f'{image} ' \
                       f'/bin/bash -c "chmod +x ./entrypoint.sh && sh ./entrypoint.sh"'

run_celery_container = f'echo "run_celery_container";' \
                       f'docker run -d ' \
                       f'--env-file {env} ' \
                       f'{image} ' \
                       f'/opt/venv/bin/celery -A src.celery worker -l info'

run_command = f'{run_django_container};{run_celery_container}'

process = subprocess.run(
    run_command,
    encoding="utf-8",
    shell=True,
    stdout=subprocess.PIPE,
)

for line in process.stdout:
    sys.stdout.write(line)
