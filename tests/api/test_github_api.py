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
def test_get_owner_existing_user(github_api):
    r=github_api.retrieve_events_triggered_by_activity_in_issues('ViktoriiaHaranovska')
    assert r is None

@pytest.mark.api
def test_get_owner_non_existing_user(github_api):
    r=github_api.retrieve_events_triggered_by_activity_in_issues('jjjjjhggdg')
    assert r is None


@pytest.mark.api
def test_get_reactions_for_issue(github_api):
    owner = 'TheAlgorithms'
    repo = 'Python'
    discussion_number = '9343'
    comment_number = '1'
    r = github_api.retrieve_reactions_for_issue (owner, repo, discussion_number, comment_number)
    assert len(r) >0

@pytest.mark.api
def test_reactions_count_for_comment(github_api):
    owner = 'TheAlgorithms'
    repo = 'Python'
    discussion_number = '9343'
    comment_number = '1'
    r = github_api.retrieve_reactions_for_issue(owner, repo, discussion_number, comment_number)

    expected_reactions_count = 2
    assert len(r) == expected_reactions_count