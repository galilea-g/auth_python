import requests

if __name__ == '__main__':
	url = 'https://api.github.com/user'

	session =  requests.session()
	session.auth = ('user','password')

	response = session.get(url)

	if response.ok:
		print(response.content)
		