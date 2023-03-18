import os

# Update the package lists
os.system('sudo apt-get update')

# Upgrade installed packages to latest versions
os.system('sudo apt-get upgrade -y')

# Specify the repository URL
url = 'https://github.com/chloe-edmondson/debs.git'

# Clone the repository with git
os.system(f'git clone {url}')

# Extract the repository name from the URL
repo_name = url.split('/')[-1].split('.')[0]

# Move into the downloaded directory
os.chdir(repo_name)

# Install all .deb files in the directory without prompting for confirmation
os.system('sudo dpkg -i *.deb --force-all --yes')
