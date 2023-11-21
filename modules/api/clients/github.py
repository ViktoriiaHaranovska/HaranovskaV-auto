import requests

class GitHub:

    def get_user(self,username):
        r=requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body

    def search_repo(self,name):
        r=requests.get(
            'http://api.github.com/search/repositories',
            params={'q':name}
        )
        body = r.json()

        return body
    
    def retrieve_events_triggered_by_activity_in_issues(self,owner):
        r=requests.get(f'https://api.github.com/repos/OWNER/REPO/issues/events{owner}')
        if r.status_code == 200:
            body = r.json()
            return body
        else:
            return None

    def retrieve_reactions_for_issue(self, owner, repo, discussion_number, comment_number):
        r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/discussions/{discussion_number}/comments/{comment_number}/reactions')
        body = r.json()
        return body
