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
            cur.execute("SELECT *, COUNT(*) FROM IPTEST LIMIT 10")
        row_db = cur.fetchall()
        num_rec = str(row_db)
        conn.commit()
        conn.close()
        answer01 = '{"cities":{"city1":"147","city2":"01","city3":"848","city4":"991"}}'
        ##resp.body = ip + ' - ' + id_ + ' - ' + num_rec
        resp.body = answer01
        resp.status = falcon.HTTP_200
        resp.set_header('X-Powered-By', 'Dataplazza')
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Headers', 'X-Requested-With')


class Homepage(object):

    def on_get(self, req, resp):
        ##resp.data = msgpack.packb({'message': 'Hello world!'})
        ##resp.content_type = 'application/msgpack'
        resp.body = "this is the api's Home page"
        resp.status = falcon.HTTP_200

api = application = falcon.API()

api.add_route('/', Homepage())

api.add_route('/req1', Resource())