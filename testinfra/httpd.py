import testinfra


def test_httpd_system_unit_file(host):
    unitfile = host.file("/usr/lib/systemd/system/httpd.service")
    assert unitfile.exists
    assert unitfile.is_file
    assert unitfile.user == 'root'
    assert unitfile.group == 'root'
    assert unitfile.mode == 0o644

def test_httpd_listen_port(host):
    configfile = host.file("/etc/httpd/conf/httpd.conf")
    assert configfile.exists
    assert configfile.is_file
    assert configfile.user == 'root'
    assert configfile.group == 'root'
    assert configfile.mode == 0o644
    assert configfile.contains('^Listen 8080$')


def test_httpd_running_and_enabled(host):
    service = host.service("httpd")
    assert service.is_running
    assert service.is_enabled

