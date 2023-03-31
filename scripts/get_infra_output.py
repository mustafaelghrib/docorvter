import argparse
import json
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument("--c", help="Docker Compose File")
parser.add_argument("--m", help="Output Module")
parser.add_argument("--f", help="Output Format. env or circleci")

args = parser.parse_args()

compose = args.c
module = args.m
output_format = args.f

command = f'docker compose -f {compose} run --rm terraform output -json {module}'
process = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
result = process.stdout.decode('utf-8')

try:
    output = json.loads(result)
    for item in output:
        if output_format == "env":
            print(f"{item}={output[item]}")
        elif output_format == "circleci":
            print(f'{item} = "{output[item]}"')
except Exception as e:
    print(f'No output for {module} | {e}\n')
