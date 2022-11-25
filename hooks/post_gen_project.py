import subprocess

red = lambda s: f'\033[91m{s}\033[00m'
green = lambda s: f'\033[92m{s}\033[00m'
yellow = lambda s: f'\033[93m{s}\033[00m'

print(yellow('### SETTING UP GIT ###'))
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
print(green('### GIT SET UP ###'))

print(yellow('### STARTING UP DOCKER ###'))
exit = subprocess.run(['docker', 'info'], capture_output=True).returncode
if exit == 0:
	exit = subprocess.call(['docker', 'compose', '-f', './docker-compose.yml', 'up', '--build'])
	if exit == 0:
		print(green('### DOCKER SET UP ###'))
		raise SystemExit

print(red('### DOCKER NOT READY, SKIPPING ###'))
