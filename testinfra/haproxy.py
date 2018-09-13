import testinfra


def test_haproxy_system_unit_file(host):
    testfile = host.file("/usr/lib/systemd/system/haproxy.service")
    assert testfile.exists
    assert testfile.is_file
    assert testfile.user == 'root'
    assert testfile.group == 'root'
    assert testfile.mode == 0o644

def test_haproxy_ssl_cert(host):
    testfile = host.file("/etc/ssl/picluster.pem")
    assert testfile.exists
    assert testfile.is_file
    assert testfile.user == 'root'
    assert testfile.group == 'root'
    assert testfile.mode == 0o640

def test_haproxy_config_file(host):
    testfile = host.file("/etc/haproxy/haproxy.cfg")
    assert testfile.exists
    assert testfile.is_file
    assert testfile.user == 'root'
    assert testfile.group == 'root'
    assert testfile.mode == 0o644
    assert testfile.contains('^listen l1$')
    assert testfile.contains('^listen l2$')
    assert testfile.contains('^listen l3$')


def test_haproxy_running_and_enabled(host):
    service = host.service("haproxy")
    assert service.is_running
    assert service.is_enabled

