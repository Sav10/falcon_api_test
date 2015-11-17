import falcon
import sqlite3


class Resource(object):

    def on_get(self, req, resp):
        ip = req.env['REMOTE_ADDR']
        abc = "aaa"
        ip2 = str(ip)
        ip2 = "123456"
        with sqlite3.connect('iptable.db') as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO IPTEST VALUES (NULL, ?)", (ip2,))
            cur.execute("SELECT *, COUNT(*) FROM IPTEST")
        row_db = cur.fetchone()
        abc = str(row_db[0])
        conn.commit()
        conn.close()
        id_ = req.params['id']
        resp.body = ip + ' - ' + id_ + ' - ' + abc
        resp.status = falcon.HTTP_200

class Homepage(object):

    def on_get(self, req, resp):
        ##resp.data = msgpack.packb({'message': 'Hello world!'})
        ##resp.content_type = 'application/msgpack'
        resp.body = "this is the api's Home page"
        resp.status = falcon.HTTP_200

api = application = falcon.API()

api.add_route('/', Homepage())

api.add_route('/req1', Resource())