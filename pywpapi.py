import requests


class WordPress(object):
    pass


class Website(WordPress):
    def __inti__(self, url, endpoints=None):
        self.url = url
        self.endpoints = endpoints

    def __repr__(self):
        # return titile of the website
        pass

    def get_wpjson(self):
        self.wp_json = requests.get(self.url + 'wp-json/')

    def get_meta(self):
        self.endpoints['posts'] = self.wp_json['routes']['/wp/v2/posts']['_links']

    def get_posts(self, endpoint=None):
        if endpoint:
            self.posts_meta = requests.get(endpoint)
        if self.endpoints['posts']:
            self.posts_meta = requests.get(self.endpoints['posts']).json()
