from jdlogger import logger
import requests
import time
from PIL import Image
import matplotlib.pyplot as plt
import threading
import json


class JDSecKill(object):

    def __init__(self):
        self.name = 'jdSecKill'
        self.isLogin = False
        self.qr_token = ''
        self.qr_cookie = ''

        self.session = requests.session()
        self.session.headers = {
            "Host": "order.jd.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            # "Cookie": "__jda=122270672.15834687691861147877382.1583468769.1583484419.1583725268.6; __jdv=76161171|direct|-|none|-|1583468769186; __jdu=15834687691861147877382; areaId=13; ipLoc-djd=13-1007-37918-0; shshshfp=ba20e8662eb2e932ee19ffc7729d6cfe; shshshfpa=81f6bb39-a5de-0184-343b-31f8dade8840-1583468770; shshshfpb=oKKLprfPraQqtEwG9ADhiDQ%3D%3D; TrackID=10wmgpzdk_v3PUwIWFefDD-LfUBqVfP2jzpjBw7rCasiwu78Ci7aFv_V2iSgpjlV1wcFP8QrjeP_Fpr-EOIwVJTk832aB0Fb_0AlOmauSh5MAx3O7SOvaqyLzllq4XBLO; pinId=lt3ttsMjFVLArHd2sJi0c7V9-x-f3wj7; pin=jd_577f796ebc95f; unick=jd_178642owo; _tp=wkNFGvcmGTZcl1GnllWOgZpVQRp2fc8bF0hUUTj8yRE%3D; _pst=jd_577f796ebc95f; __jdb=122270672.5.15834687691861147877382|6.1583725268; __jdc=122270672; PCSYCityID=CN_370000_370200_370212; shshshsID=4f392fc046e458c8da6feca4eb74a72b_2_1583725318050; wlfstk_smdl=ubac618t4rtctwrg5ip5pc9cc8dwvbjp; 3AB9D23F7A4B3C9B=XTBRIPVVIWNUW2FF5NFW7NQSWHVFY7YFELVN52JO5WSTOTGXXIY6GWXEP2P2NGRXMN5MDPK2RNF67NU2U3CS4F2VFE; thor=33D4A38C15EE634799AD2973AB3CDBCE1AFD57F8629D5BF26A666F703D0A7A590714A79409338F0C31BA5D3CBD7E30628162D1E8F77C90931D2736FE9F7A4D5970E2AE1F6870EA686043EF16992C06B4F19FFFE9A4E23FEEF83513119DE0773C1777A887FB141BEE47FA332D423B8D441455B57D5461E8946FEF3D26F323565B81639E4D2D4FBC03331488D9019B24130E80BD7A5163FC4ED4975B55A1761771; ceshi3.com=000",
            "Upgrade-Insecure-Requests": "1",
            "Cache-Control": "max-age=0",
            "TE": "Trailers"
        }
        self.session.cookies['cookie'] = ""

    def login(self):
        target_url = 'https://order.jd.com/center/list.action'

        resp = self.session.get(url=target_url, allow_redirects=False)

        if resp.status_code != requests.codes.OK:
            print(resp.status_code)
            self.login_by_scan_qrcode()
        else:
            self.isLogin = True
            logger.info('login successfully by cookies')

    def login_by_cookies(self):
        pass

    def login_by_scan_qrcode(self):

        logger.info('start to get qrcode')

        qrcode_url = f"https://qr.m.jd.com/show?appid=133&size=147&t={round(time.time())}"
        qr_resp = self.session.get(qrcode_url)
        self.qr_cookie = qr_resp.cookies.get_dict()
        self.qr_token = self.qr_cookie['wlfstk_smdl']

        print(self.qr_token)
        print(self.qr_cookie)

        # check qrcode status
        threading.Thread(target=self.check_qrcode_status).start()

        # open qrcode
        with open('qrCode.jpg', 'wb')as f:
            f.write(qr_resp.content)
        img = Image.open('qrCode.jpg')
        plt.figure('qrcode')
        plt.imshow(img)
        plt.show()

    # def check_qrcode_status(self):
    #     checkUrl = f'https://qr.m.jd.com/check?callback=jQuery4643268&appid=133&token={self.qr_token}&_={round(
    #         time.time() * 10000)}'
    #
    #     while True:
    #         time.sleep(1)
    #         print(self.qr_token)
    #         checkResponse = self.session.get(checkUrl)
    #         # print()
    #         print(str(checkResponse.content, 'utf-8'))

    def select_items(self):

        logger.info('select all items')

    def buy_items(self):
        logger.info('add items into cart')
        logger.info('select all itmes and ')
        logger.info('settlement')
        logger.info('submit order')


if __name__ == "__main__":
    jd = JDSecKill()
    jd.login()
    jd.select_items()
    jd.buy_items()
    time.sleep(100000)
