import urllib
import requests
import re
import json

BASE_URL = "https://pathofexile.com"
URLS = {
	'login': BASE_URL+'/login',
}
class PoEAPI(object):
	def __init__(self, account_name, session_id):
		self._session = requests.Session()
		self._session.headers.update({
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
			})

		self.account_name = account_name
		self.poesessid = session_id


	def _get_hash(self, resp=None):
		regex = re.compile('name="hash" value="(.*)" ')
		result = regex.search(resp.text)

		return result.groups()[0]


	def _geturl(self, url, params=None, data=None):
		params = {} if params is None else params
		data = {} if data is None else data


	def reset_session(self):
		self._session = requests.Session()


	def login(self, email, password):
		print('before getlogin', self._session.cookies)
		form_get_resp = self._session.get(BASE_URL + '/login')
		form_hash = self._get_hash(form_get_resp)

		print('gotlogin', self._session.cookies)
		request = requests.Request(
			'POST', 
			BASE_URL + '/login', 
			data={
				'login_email': email,
				'login_password': password,
				'hash': form_hash,
				'login': 'Login',
				'remember_me': '0'
				},
			headers={
				'Content-Type': 'application/x-www-form-urlencoded',
				'Referer': 'https://www.pathofexile.com/login',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
				'Accept-Encoding': 'gzip, deflate, br',
			})
		preq = self._session.prepare_request(request)
		print("prepared requiest", preq.headers)

		fpr = self._session.send(preq)

		print('after sent', self._session.cookies)
		print('resp', fpr.cookies)
		return fpr


	@property
	def poesessid(self):
		return self.session_id


	@poesessid.setter
	def poesessid(self, id):
		self.session_id = id
		self._session.cookies.set('POESESSID', id)


	def set_default_params(self, defaults=None):
		app_defaults = {
			'accountName': self.account_name
		}

		if defaults is None:
			defaults = {}

		app_defaults.update(defaults)

		return {k:v for k, v in app_defaults.items() if v is not None}


	def get_leagues(self, type='main', season=None, compact=1, limit=None, offset=0, includeRaces=False):
		params = self.set_default_params({
			'type': type,
			'compact': compact,
			'offset': offset,
			'season': season,
			'limit': limit
		})
		race_re = re.compile('JRE.*')

		resp = self._session.get('http://api.pathofexile.com/leagues?type=main&compact=1', params=params)
		league_data = json.loads(resp.text)
	
		if not includeRaces:
			new_data = []
			for item in league_data:
				if race_re.search(item['id']):
					continue

				new_data.append(item)

			league_data = new_data

		return league_data


	def get_characters(self, league=None):
		params = self.set_default_params()

		resp = self._session.get(
			BASE_URL + '/character-window/get-characters',
			params=params
			)

		char_data = json.loads(resp.text)

		if league is not None:
			new_data = []
			for item in char_data:
				if item['league'] == league:
					new_data.append(item)
			char_data = new_data

		return char_data


	def get_character_items(self, character):
		params = self.set_default_params({
			'character': character
			})

		resp = self._session.get(
			BASE_URL + '/character-window/get-items', 
			params=params
			)

		data = json.loads(resp.text)

		return data


	def get_stash(self, league, tab_index):
		params = self.set_default_params({
			'league': league,
			'tabIndex': tab_index,
			'tabs': '1'
			})

		resp = self._session.get(
			BASE_URL + '/character-window/get-stash-items',
			params=params
			)

		data = json.loads(resp.text)

		return data


	def get_stash_tabs(self, league):
		tab_data = self.get_stash(league, 1)

		return tab_data['tabs']


if __name__ == '__main__':
	api = PoEAPI('DocHoncho', 'd1cad44fef50439270fcdcce07fc23be')
	


