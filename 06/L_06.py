url = 'http://api.fixer.io/latest'
# url = "http://api.fixer.io/2000-01-03"
r = requests.get(url)
r = r.json()