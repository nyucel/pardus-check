import sys
import re

def get_package_info(package_info, info):
    return re.search(info+": (.*)\n", package_info).group(1)

def get_package_sha1sum(package_info):
    return get_package_info(package_info, 'SHA1')

def get_package_filename(package_info):
    return './' + '/'.join(get_package_info(package_info, 'Filename').split('/')[2:])
###

packages_file_path = sys.argv[1]
packages_file = file(packages_file_path).read()

packages_list = packages_file.split('\n\n')
for package_info in packages_list:
    if len(package_info) < 10:
	continue
    package_filename = get_package_filename(package_info)
    package_sha1sum = get_package_sha1sum(package_info)
    print package_filename, package_sha1sum

