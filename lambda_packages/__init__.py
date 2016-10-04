import os

# A manifest of the included packages.
cwd = os.path.abspath(__file__)
pkg_extension = '.tar.gz'
lambda_packages = dict()
folders = [f for f in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, f))]
for folder in folders:
    this_package = list()
    gz_tarballs = [f for f in os.listdir(os.path.join(cwd, folder)) if pkg_extension in f]
    for file_name in gz_tarballs:
        this_version = dict()
        this_version['path'] = os.path.join(os.path.dirname(cwd), folder, file_name)
        this_version['version'] = file_name.strip(pkg_extension).split('-', 1)[1]
        this_package.append(this_version)
    lambda_packages[folder.lower()] = this_package
