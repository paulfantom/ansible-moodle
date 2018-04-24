import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize("dirs", [
    "/opt/moodle",
    "/var/www/moodle",
    "/srv/data"
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/var/www/moodle/config.php"
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file
    assert f.group("www-data")
    assert f.user("www-data")


@pytest.mark.parametrize("service", [
    "nginx",
    "mysql",
    "php7.0-fpm"
])
def test_service(host, service):
    s = host.service(service)
    assert s.is_enabled
    assert s.is_running
