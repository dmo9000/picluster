import testinfra


def test_bbsd_system_unit_file(host):
    unitfile = host.file("/usr/lib/systemd/system/bbsd.service")
    assert unitfile.exists
    assert unitfile.is_file
    assert unitfile.user == 'root'
    assert unitfile.group == 'root'
    assert unitfile.mode == 0o644


def test_bbsd_running_and_enabled(host):
    service = host.service("bbsd")
    assert service.is_running
    assert service.is_enabled

