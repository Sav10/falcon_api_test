import falcon
import sqlite3
##import msgpack


class Resource(object):

    def on_get(self, req, resp):
        ##resp.data = msgpack.packb({'message': 'Hello world!'})
        ##resp.content_type = 'application/msgpack'
        ip = req.env['REMOTE_ADDR']
        try :
        	conn = sqlite3.connect('iptable.db')
			cur = conn.cursor()
        	conn.execute("INSERT INTO IPTEST (IP) VALUES (?)", [ip])
        	conn.commit()
        	cur = conn.cursor()
        	cur.execute("SELECT *, COUNT(*) FROM IPTEST")
        	row_db = cur.fetchone()
        	conn.close()
        except Exception as e:
        	raise e
        id_ = req.params['id']
        resp.body = ip + ' - ' + id_ + ' - ' + "aaa"
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