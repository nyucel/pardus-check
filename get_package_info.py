import sys
import re

def get_package_info(package_info, info):
    return re.search(info+": (.*)\n", package_info).group(1)

def get_package_name(package_info):
    return get_package_info(package_info, 'Package')

def get_package_version(package_info):
    return get_package_info(package_info, 'Version')

def get_package_sha1sum(package_info):
    return get_package_info(package_info, 'SHA1')

###

packages_file_path = sys.argv[1]
packages_file = file(packages_file_path).read()

packages_list = packages_file.split('\n\n')
for package_info in packages_list:
    package_name = get_package_name(package_info)
    package_version = get_package_version(package_info)
    package_sha1sum = get_package_sha1sum(package_info)
    print package_name, package_version, package_sha1sum

