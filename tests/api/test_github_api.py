import pytest
from modules.api.clients.github import GitHub

@pytest.mark.api
def test_user_exists(github_api):
    api = GitHub()
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    api = GitHub()
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r=github_api.search_repo('become-qa-auto')
    assert r['total_count'] ==50
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r=github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count']==0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r=github_api.search_repo('s')
    assert r['total_count']!=0

@pytest.mark.api
def test_issue_events_get_owner_existing_user(github_api):
    r=github_api.issue_events_get_owner('ViktoriiaHaranovska')
    assert r is not None

@pytest.mark.api
def test_issue_events_get_owner_non_existing_user(github_api):
    r=github_api.issue_events_get_owner('jjjjjhggdg')
    assert r is None


@pytest.mark.api
def test_search_repository_by_name(github_api):
    query = "HaranovskaV-auto"
    response = github_api.search(query)
    assert response is not None

@pytest.mark.api
def test_get_user_info_by_username(github_api):
    username = "ViktoriiaHaranovska"
    user_info = github_api.get_user(username)
    
    assert user_info["public_repos"] >= 1