import falcon
import sqlite3


class Resource(object):

    def on_get(self, req, resp):
        ip = req.env['REMOTE_ADDR']
        id_ = str(req.params['id'])
        ip2 = str(ip)
        with sqlite3.connect('/var/db_dtp/iptable.db') as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO IPTEST VALUES (NULL, ?, ?)", (ip2,id_))
            cur.execute("SELECT *, COUNT(*) FROM IPTEST LIMIT")
        row_db = cur.fetchone()
        num_rec = str(row_db)
        conn.commit()
        conn.close()
        resp.body = ip + ' - ' + id_ + ' - ' + num_rec
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