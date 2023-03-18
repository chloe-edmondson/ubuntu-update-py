import os

# Update the package lists
os.system('sudo apt-get update')

# Upgrade installed packages to latest versions
os.system('sudo apt-get upgrade')

# Specify the URL to pull
url = 'https://github.com/chloe-edmondson/debs.git'

# Use wget to pull the repository
os.system(f'wget {url}')
