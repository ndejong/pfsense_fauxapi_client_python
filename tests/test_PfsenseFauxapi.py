
import pytest
from unittest.mock import patch
from PfsenseFauxapi.PfsenseFauxapi import PfsenseFauxapi


def test_version_exist():
    fauxapi = PfsenseFauxapi(host=None, apikey=None, apisecret=None)
    assert fauxapi.version is not None


@patch('requests.get', autospec=True)
def test_fauxapi_not_installed(mock_requests_get):

    fauxapi = PfsenseFauxapi(host=None, apikey=None, apisecret=None)
    mock_requests_get.return_value.status_code = 404
    with pytest.raises(Exception) as exception_info:
        fauxapi.config_get()

    assert 'Unable to find FauxAPI on target host' in str(exception_info.value)


@patch('requests.get', autospec=True)
def test_config_get(mock_requests_get):

    fauxapi = PfsenseFauxapi(host=None, apikey=None, apisecret=None)
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.text = '{"callid": "b905cb4ef8db8", "action": "config_get", "message": "ok", "data": { "config": {"version": "18.9", "lastchange": "", "system": {}} }}'

    response = fauxapi.config_get()
    assert response['version'] == '18.9'


@patch('requests.post', autospec=True)
def test_config_set(mock_requests_post):

    fauxapi = PfsenseFauxapi(host=None, apikey=None, apisecret=None)
    mock_requests_post.return_value.status_code = 200
    mock_requests_post.return_value.text = '{"callid": "5c8db8b4efb90", "action": "config_set", "message": "ok", "data": {"do_backup": true, "do_reload": true, "previous_config_file": "/cf/conf/backup/config-1552791732.xml"}}'

    response = fauxapi.config_set(config={})
    assert response['action'] == 'config_set'
    assert response['message'] == 'ok'
    assert response['data'] is not None


@patch('requests.post', autospec=True)
def test_config_patch(mock_requests_post):

    fauxapi = PfsenseFauxapi(host=None, apikey=None, apisecret=None)
    mock_requests_post.return_value.status_code = 200
    mock_requests_post.return_value.text = '{"callid": "5c8dbe47090f8", "action": "config_patch", "message": "ok", "data": {"do_backup": true, "do_reload": true, "previous_config_file": "/cf/conf/backup/config-1552793159.xml"}}'

    response = fauxapi.config_patch(config={})
    assert response['action'] == 'config_patch'
    assert response['message'] == 'ok'
    assert response['data'] is not None


@patch('requests.get', autospec=True)
def test_config_reload(mock_requests_get):

    fauxapi = PfsenseFauxapi(host=None, apikey=None, apisecret=None)
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.text = '{"callid": "5c8dbe9a6331e", "action": "config_reload", "message": "ok"}'

    response = fauxapi.config_reload()
    assert response['action'] == 'config_reload'
    assert response['message'] == 'ok'


@patch('requests.get', autospec=True)
def test_config_backup(mock_requests_get):

    fauxapi = PfsenseFauxapi(host=None, apikey=None, apisecret=None)
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.text = '{"callid": "5c8dc46901d7f", "action": "config_backup", "message": "ok", "data": {"backup_config_file": "/cf/conf/backup/config-1552794729.xml"}}'

    response = fauxapi.config_backup()
    assert response['action'] == 'config_backup'
    assert response['message'] == 'ok'
    assert response['data'] is not None


@patch('requests.get', autospec=True)
def test_config_backup_list(mock_requests_get):

    fauxapi = PfsenseFauxapi(host=None, apikey=None, apisecret=None)
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.text = '{"callid": "5c8dc4987c3f8", "action": "config_backup_list", "message": "ok", "data": {"backup_files": []}}'

    response = fauxapi.config_backup_list()
    assert response['action'] == 'config_backup_list'
    assert response['message'] == 'ok'
    assert response['data'] is not None


@patch('requests.get', autospec=True)
def test_system_stats(mock_requests_get):

    fauxapi = PfsenseFauxapi(host=None, apikey=None, apisecret=None)
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.text = '{"callid": "5c8dc51dabd44", "action": "system_stats", "message": "ok", "data": {"stats": {}}}'

    response = fauxapi.system_stats()
    assert response['action'] == 'system_stats'
    assert response['message'] == 'ok'
    assert response['data'] is not None


@patch('requests.get', autospec=True)
def test_interface_stats(mock_requests_get):

    fauxapi = PfsenseFauxapi(host=None, apikey=None, apisecret=None)
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.text = '{"callid": "5c8dc5d40c07a", "action": "interface_stats", "message": "ok", "data": {"stats": {}}}'

    response = fauxapi.interface_stats(None)
    assert response['action'] == 'interface_stats'
    assert response['message'] == 'ok'
    assert response['data'] is not None


@patch('requests.get', autospec=True)
def test_gateway_status(mock_requests_get):

    fauxapi = PfsenseFauxapi(host=None, apikey=None, apisecret=None)
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.text = '{"callid": "5c8dc6227ec06", "action": "gateway_status", "message": "ok", "data": {"gateway_status": {}}}'

    response = fauxapi.gateway_status()
    assert response['action'] == 'gateway_status'
    assert response['message'] == 'ok'
    assert response['data'] is not None


@patch('requests.post', autospec=True)
def test_send_event(mock_requests_post):

    fauxapi = PfsenseFauxapi(host=None, apikey=None, apisecret=None)
    mock_requests_post.return_value.status_code = 200
    mock_requests_post.return_value.text = '{"callid": "5c8dc64e73efc", "action": "send_event", "message": "ok"}'

    response = fauxapi.send_event(None)
    assert response['action'] == 'send_event'
    assert response['message'] == 'ok'


@patch('requests.get', autospec=True)
def test_rule_get(mock_requests_get):

    fauxapi = PfsenseFauxapi(host=None, apikey=None, apisecret=None)
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.text = '{"callid": "5c8dc731b54e2", "action": "rule_get", "message": "ok", "data": {"rules": []}}'

    response = fauxapi.rule_get()
    assert response['action'] == 'rule_get'
    assert response['message'] == 'ok'
    assert response['data'] is not None


@patch('requests.get', autospec=True)
def test_alias_update_urltables(mock_requests_get):

    fauxapi = PfsenseFauxapi(host=None, apikey=None, apisecret=None)
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.text = '{"callid": "5c8dc7720e65a", "action": "alias_update_urltables", "message": "ok", "data": {"updates": []}}'

    response = fauxapi.alias_update_urltables()
    assert response['action'] == 'alias_update_urltables'
    assert response['message'] == 'ok'
    assert response['data'] is not None


@patch('requests.post', autospec=True)
def test_function_call(mock_requests_post):

    fauxapi = PfsenseFauxapi(host=None, apikey=None, apisecret=None)
    mock_requests_post.return_value.status_code = 200
    mock_requests_post.return_value.text = '{"callid": "5c8dc7cda6948", "action": "function_call", "message": "ok", "data": {"return": {}}}'

    response = fauxapi.function_call(None)
    assert response['action'] == 'function_call'
    assert response['message'] == 'ok'
