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
    
    def issue_events_get_owner(self,owner):
        r=requests.get(f'https://api.github.com/users/{owner}')
        if r.status_code == 200:
            body = r.json()
            return body
        else:
            return None

    def search(self, query):
        r = requests.get(f'https://api.github.com/search/repositories?q={query}')
        body = r.json()
        return body
