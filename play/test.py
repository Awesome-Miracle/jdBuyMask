import requests


sess = requests.session()
# sess.headers = {
#   "Host": "order.jd.com",
#   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0",
#   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#   "Accept-Language": "en-US,en;q=0.5",
#   "Accept-Encoding": "gzip, deflate, br",
#   "Connection": "keep-alive",
#   "Cookie": "__jda=122270672.15834687691861147877382.1583468769.1583484419.1583725268.6; __jdv=76161171|direct|-|none|-|1583468769186; __jdu=15834687691861147877382; areaId=13; ipLoc-djd=13-1007-37918-0; shshshfp=ba20e8662eb2e932ee19ffc7729d6cfe; shshshfpa=81f6bb39-a5de-0184-343b-31f8dade8840-1583468770; shshshfpb=oKKLprfPraQqtEwG9ADhiDQ%3D%3D; TrackID=10wmgpzdk_v3PUwIWFefDD-LfUBqVfP2jzpjBw7rCasiwu78Ci7aFv_V2iSgpjlV1wcFP8QrjeP_Fpr-EOIwVJTk832aB0Fb_0AlOmauSh5MAx3O7SOvaqyLzllq4XBLO; pinId=lt3ttsMjFVLArHd2sJi0c7V9-x-f3wj7; pin=jd_577f796ebc95f; unick=jd_178642owo; _tp=wkNFGvcmGTZcl1GnllWOgZpVQRp2fc8bF0hUUTj8yRE%3D; _pst=jd_577f796ebc95f; __jdb=122270672.5.15834687691861147877382|6.1583725268; __jdc=122270672; PCSYCityID=CN_370000_370200_370212; shshshsID=4f392fc046e458c8da6feca4eb74a72b_2_1583725318050; wlfstk_smdl=ubac618t4rtctwrg5ip5pc9cc8dwvbjp; 3AB9D23F7A4B3C9B=XTBRIPVVIWNUW2FF5NFW7NQSWHVFY7YFELVN52JO5WSTOTGXXIY6GWXEP2P2NGRXMN5MDPK2RNF67NU2U3CS4F2VFE; thor=33D4A38C15EE634799AD2973AB3CDBCE1AFD57F8629D5BF26A666F703D0A7A590714A79409338F0C31BA5D3CBD7E30628162D1E8F77C90931D2736FE9F7A4D5970E2AE1F6870EA686043EF16992C06B4F19FFFE9A4E23FEEF83513119DE0773C1777A887FB141BEE47FA332D423B8D441455B57D5461E8946FEF3D26F323565B81639E4D2D4FBC03331488D9019B24130E80BD7A5163FC4ED4975B55A1761771; ceshi3.com=000",
#   "Upgrade-Insecure-Requests": "1",
#   "Cache-Control": "max-age=0",
#   "TE": "Trailers"
# }

sess.headers = {
  "Host": "order.jd.com",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
  "Accept-Language": "en-US,en;q=0.5",
  "Connection": "keep-alive",
  "Cookie": "__jda=122270672.15834687691861147877382.1583468769.1583484419.1583725268.6; __jdv=76161171|direct|-|none|-|1583468769186; __jdu=15834687691861147877382; areaId=13; ipLoc-djd=13-1007-37918-0; shshshfp=ba20e8662eb2e932ee19ffc7729d6cfe; shshshfpa=81f6bb39-a5de-0184-343b-31f8dade8840-1583468770; shshshfpb=oKKLprfPraQqtEwG9ADhiDQ%3D%3D; TrackID=10wmgpzdk_v3PUwIWFefDD-LfUBqVfP2jzpjBw7rCasiwu78Ci7aFv_V2iSgpjlV1wcFP8QrjeP_Fpr-EOIwVJTk832aB0Fb_0AlOmauSh5MAx3O7SOvaqyLzllq4XBLO; pinId=lt3ttsMjFVLArHd2sJi0c7V9-x-f3wj7; pin=jd_577f796ebc95f; unick=jd_178642owo; _tp=wkNFGvcmGTZcl1GnllWOgZpVQRp2fc8bF0hUUTj8yRE%3D; _pst=jd_577f796ebc95f; __jdb=122270672.5.15834687691861147877382|6.1583725268; __jdc=122270672; PCSYCityID=CN_370000_370200_370212; shshshsID=4f392fc046e458c8da6feca4eb74a72b_2_1583725318050; wlfstk_smdl=ubac618t4rtctwrg5ip5pc9cc8dwvbjp; 3AB9D23F7A4B3C9B=XTBRIPVVIWNUW2FF5NFW7NQSWHVFY7YFELVN52JO5WSTOTGXXIY6GWXEP2P2NGRXMN5MDPK2RNF67NU2U3CS4F2VFE; thor=33D4A38C15EE634799AD2973AB3CDBCE1AFD57F8629D5BF26A666F703D0A7A590714A79409338F0C31BA5D3CBD7E30628162D1E8F77C90931D2736FE9F7A4D5970E2AE1F6870EA686043EF16992C06B4F19FFFE9A4E23FEEF83513119DE0773C1777A887FB141BEE47FA332D423B8D441455B57D5461E8946FEF3D26F323565B81639E4D2D4FBC03331488D9019B24130E80BD7A5163FC4ED4975B55A1761771; ceshi3.com=000",
  "Upgrade-Insecure-Requests": "1",
  "Cache-Control": "max-age=0",
  "TE": "Trailers"
}



# sess.headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
#     "Connection": "keep-alive",
#     "Cookie": "__jda=122270672.15834687691861147877382.1583468769.1583484419.1583725268.6; __jdv=76161171|direct|-|none|-|1583468769186; __jdu=15834687691861147877382; areaId=13; ipLoc-djd=13-1007-37918-0; shshshfp=ba20e8662eb2e932ee19ffc7729d6cfe; shshshfpa=81f6bb39-a5de-0184-343b-31f8dade8840-1583468770; shshshfpb=oKKLprfPraQqtEwG9ADhiDQ%3D%3D; TrackID=10wmgpzdk_v3PUwIWFefDD-LfUBqVfP2jzpjBw7rCasiwu78Ci7aFv_V2iSgpjlV1wcFP8QrjeP_Fpr-EOIwVJTk832aB0Fb_0AlOmauSh5MAx3O7SOvaqyLzllq4XBLO; pinId=lt3ttsMjFVLArHd2sJi0c7V9-x-f3wj7; pin=jd_577f796ebc95f; unick=jd_178642owo; _tp=wkNFGvcmGTZcl1GnllWOgZpVQRp2fc8bF0hUUTj8yRE%3D; _pst=jd_577f796ebc95f; __jdb=122270672.5.15834687691861147877382|6.1583725268; __jdc=122270672; PCSYCityID=CN_370000_370200_370212; shshshsID=4f392fc046e458c8da6feca4eb74a72b_2_1583725318050; wlfstk_smdl=ubac618t4rtctwrg5ip5pc9cc8dwvbjp; 3AB9D23F7A4B3C9B=XTBRIPVVIWNUW2FF5NFW7NQSWHVFY7YFELVN52JO5WSTOTGXXIY6GWXEP2P2NGRXMN5MDPK2RNF67NU2U3CS4F2VFE; thor=33D4A38C15EE634799AD2973AB3CDBCE1AFD57F8629D5BF26A666F703D0A7A590714A79409338F0C31BA5D3CBD7E30628162D1E8F77C90931D2736FE9F7A4D5970E2AE1F6870EA686043EF16992C06B4F19FFFE9A4E23FEEF83513119DE0773C1777A887FB141BEE47FA332D423B8D441455B57D5461E8946FEF3D26F323565B81639E4D2D4FBC03331488D9019B24130E80BD7A5163FC4ED4975B55A1761771; ceshi3.com=000"
# }

resp = sess.get(url="https://order.jd.com/center/list.action")
# resp = sess.get(url="http://www.baidu.com")

# print(resp.encoding)
print(requests.utils.get_encodings_from_content(resp.text))
print(resp.apparent_encoding)
#
print(resp.text)

# print(str(resp.text.encode('gbk'), encoding='gbk'))

# encode_content = ''

# if req.encoding == 'ISO-8859-1':
#     encodings = requests.utils.get_encodings_from_content(req.text)
#     if encodings:
#         encoding = encodings[0]
#     else:
#         encoding = req.apparent_encoding
#
#     print(req.apparent_encoding)
#     encode_content = req.content.decode(encoding, 'replace') #如果设置为replace，则会用?取代非法字符；
#
#
# print(encode_content)
