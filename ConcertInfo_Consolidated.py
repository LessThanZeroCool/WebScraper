import subprocess

# Files to run
first_script = 'middleeastshows.py'
second_script = 'facesbrewing.py'

# Run the first script
subprocess.run(['python3', first_script])

# Once the first script completes, run the second script
subprocess.run(['python3', second_script])
