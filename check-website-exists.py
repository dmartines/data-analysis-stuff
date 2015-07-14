'''
Created on Jul 14, 2015
Verify if website exists
@author: Martines Daniel
'''

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
urls = ['http://www.cryptonaut.vc','http://www.88bitcoindice.com','http://www.btcs.com','http://coincrack.com','http://www.seedco.in','http://paydoko.com','http://quickcoin.co','http://www.coinfirma.com','http://www.bitfury.com','http://www.bitaccess.co','http://www.zentrade.io','http://gem.co','http://angel.co/maicoin','http://www.coinmelon.com','http://bitcoinjobsonline.com','http://bitcoincasinonews.com','http://bitcoinwebhostingratings.com','http://bitcoinminer.net','http://bitcointribune.com','http://bitcoinvalue.net','http://bitcoingamblingsites.com','http://bitcoinnewsexposed.com','http://www.bestbitcoinblackjack.com','http://www.fairlay.com','http://www.coin4ce.com','http://www.honeybadgr.com','http://coinsimple.com','http://www.bitgo.com','http://fruitwallet.com','http://www.bestbitcoinbaccarat.com','http://www.peerpal.co','http://bitcoinbrothers.de','http://www.portableboutique.com','http://BitcoinExchangeGuide.com','http://www.coinsafe.com','http://www.quantave.com','http://www.koinabanx.com','http://www.coindash.co','http://hashplex.com','http://www.bestbitcoindice.com','http://xapo.com','http://www.mycoinsolution.com','http://www.gamblingwithbitcoins.com','https://coinbeyond.com','http://polycoin.io','http://www.blocktrail.com','http://www.TheCoinTree.com','http://www.bitcm.com/','http://www.bitcm.com/','http://bitso.com','http://coinalytics.co/','https://bitex.la','http://www.bitple.com/','http://www.litecoin.org','http://www.coinpip.com','http://www.coinzone.com','http://www.37coins.com','http://www.igot.com','http://www.blockchain.capital','http://www.blockcypher.com/','http://obsidianexchange.com/','https://www.crunchbase.com/organization/bitpass-inc?utm_source=odm_C7D54DA4E16142F4A5BE76114AE527E0.csv&utm_medium=export&utm_campaign=dataset','http://coinroyale.com','http://knewcoin.com/','http://bitcoinpay.com','http://neuroware.io/','https://www.crunchbase.com/organization/bitspot-inc?utm_source=odm_C7D54DA4E16142F4A5BE76114AE527E0.csv&utm_medium=export&utm_campaign=dataset','http://www.gocoin.com','http://bitmarket.ph/','http://www.cryptmint.com/','http://ghash.io','http://coinify.com','https://btbbitcoinbrothers.com/','https://cryptocorp.co/','http://www.sldx.com/','https://yacuna.com','http://arbiter.me','http://www.bitsie.com','http://www.baltimorebitcoin.org/','http://www.playcoincasino.com','http://bitnewt.com/','http://bitfurycapital.com/','https://www.bitrated.com/','https://coinsecure.in/','http://www.coinhako.com','http://namecoin.info/','http://www.FalconGlobalCapital.com','http://www.sendnspend.com','http://www.livingroomofsatoshi.com/','http://muchmarket.com','http://coinhive.io','http://www.dna-bits.com/','http://coin.co','http://cloudtd.es/','http://www.cloudbitmine.com','http://coins.ph','https://onename.com','http://rushwallet.com/#ySPFpfxb4LtQCCGNueOYtcaDHN3kZ1','http://www.unocoin.com/','http://www.coinbau.com','http://matrixvision.eu','http://angel.co/bitcoin-syndicate','https://coinfresh.com','http://www.coinbatch.com','http://blockr.io/','https://mybitx.co/','https://www.sfox.com/','http://www.cashila.com','http://www.netcoins.ca/','http://www.sub25.net/','http://rollin.io','http://satoshipay.net/','http://syncbeat.com/','https://bitlendingclub.com/','http://www.glidera.com/','http://www.stash.my','http://bitcoincharts.com/','http://you-name-it.net','http://bitstash.com','http://bitcoinmagazine.com/','http://www.bitcoininstitute.org/','http://www.xoin.co.za','http://cointelegraph.com/','http://btcsec.com','https://toshi.io/','http://www.alt-options.com','https://www.ethereum.org/','http://www.zapchain.com/','https://api.trustedcoin.com/','https://startupxplore.com/startup/bitchimp','http://www.bitcoinforbiz.com/','http://bithalo.org/','https://coinapult.com/','http://monon.co/','http://btcminer.us','http://coinagenda.com','http://www.bitcoinblackfriday.com','http://www.coincorner.com','https://www.clevercoin.com','https://www.bitpesa.co/','http://www.bitcointrust.co/','http://flexcoin.com','http://www.bitnplay.eu','http://bit-post.com/','http://letstalkbitcoin.com','http://preev.com','http://bitcoinmillionaire-app.com','http://numisight.com','http://atlascard.io','http://www.blocktech.com','http://bitcoin-india.org/']

responses = {
    100: ('Continue', 'Request received, please continue'),
    101: ('Switching Protocols',
          'Switching to new protocol; obey Upgrade header'),

    200: ('OK', 'Request fulfilled, document follows'),
    201: ('Created', 'Document created, URL follows'),
    202: ('Accepted',
          'Request accepted, processing continues off-line'),
    203: ('Non-Authoritative Information', 'Request fulfilled from cache'),
    204: ('No Content', 'Request fulfilled, nothing follows'),
    205: ('Reset Content', 'Clear input form for further input.'),
    206: ('Partial Content', 'Partial content follows.'),

    300: ('Multiple Choices',
          'Object has several resources -- see URI list'),
    301: ('Moved Permanently', 'Object moved permanently -- see URI list'),
    302: ('Found', 'Object moved temporarily -- see URI list'),
    303: ('See Other', 'Object moved -- see Method and URL list'),
    304: ('Not Modified',
          'Document has not changed since given time'),
    305: ('Use Proxy',
          'You must use proxy specified in Location to access this '
          'resource.'),
    307: ('Temporary Redirect',
          'Object moved temporarily -- see URI list'),

    400: ('Bad Request',
          'Bad request syntax or unsupported method'),
    401: ('Unauthorized',
          'No permission -- see authorization schemes'),
    402: ('Payment Required',
          'No payment -- see charging schemes'),
    403: ('Forbidden',
          'Request forbidden -- authorization will not help'),
    404: ('Not Found', 'Nothing matches the given URI'),
    405: ('Method Not Allowed',
          'Specified method is invalid for this server.'),
    406: ('Not Acceptable', 'URI not available in preferred format.'),
    407: ('Proxy Authentication Required', 'You must authenticate with '
          'this proxy before proceeding.'),
    408: ('Request Timeout', 'Request timed out; try again later.'),
    409: ('Conflict', 'Request conflict.'),
    410: ('Gone',
          'URI no longer exists and has been permanently removed.'),
    411: ('Length Required', 'Client must specify Content-Length.'),
    412: ('Precondition Failed', 'Precondition in headers is false.'),
    413: ('Request Entity Too Large', 'Entity is too large.'),
    414: ('Request-URI Too Long', 'URI is too long.'),
    415: ('Unsupported Media Type', 'Entity body in unsupported format.'),
    416: ('Requested Range Not Satisfiable',
          'Cannot satisfy request range.'),
    417: ('Expectation Failed',
          'Expect condition could not be satisfied.'),

    500: ('Internal Server Error', 'Server got itself in trouble'),
    501: ('Not Implemented',
          'Server does not support this operation'),
    502: ('Bad Gateway', 'Invalid responses from another server/proxy.'),
    503: ('Service Unavailable',
          'The server cannot process the request due to a high load'),
    504: ('Gateway Timeout',
          'The gateway server did not receive a timely response'),
    505: ('HTTP Version Not Supported', 'Cannot fulfill request.'),
    }

for url in urls:
    req = Request(url)
    try:
        response = urlopen(req)
        #print(response)
    except HTTPError as e:
        print(req.full_url,'Website not responsive',responses[e.code][1],sep=',')
    except URLError as e:
        print(req.full_url,'Website not responsive','URL no longer exists',sep=',')
