import requests

BLAZER_NET = 'http://10.60.21.11'
BLAZER_NET_API = BLAZER_NET + '/api'
EPISODE = BLAZER_NET_API + '/episode'
EPISODE_LIST = EPISODE + '/getlistofepisodes'
MONITORING_HEALTH = BLAZER_NET_API + '/monitoring/checkhealth'


class TestBlazerNet:

    EPISODE_START = 7000
    EPISODE_COUNT = 50

    def test_episode_list(self):
        url = EPISODE_LIST + '/{}/{}'.format(self.EPISODE_START, self.EPISODE_COUNT)
        res = requests.get(url)
        assert res.status_code == 200
        assert len(res.json()) == self.EPISODE_COUNT
        assert 'ID' in res.json()[0]
        assert res.json()[0]['ID'] < self.EPISODE_START

    def test_monitoring(self):
        res = requests.get(MONITORING_HEALTH)
        assert res.status_code == 200


if __name__ == '__main__':
    TestBlazerNet().test_episode_list()
