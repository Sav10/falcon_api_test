import falcon
import sqlite3

class Resource(object):

    def on_get(self, req, resp):
        ip = req.env['REMOTE_ADDR']
        id_ = str(req.params['id'])
        ip2 = str(ip)
        len_var = len(id_)
        with sqlite3.connect('/var/db_dtp/iptable.db') as conn:
            cur = conn.cursor()
            ##cur.execute("INSERT INTO IPTEST VALUES (NULL, ?, ?)", (ip2,id_))
            cur.execute("SELECT *  FROM communes_dep2 WHERE substr(commune, 1, ?)= ? LIMIT 10", (len_var,id_))
        row_db = cur.fetchall()
        data_d1 = []
        desc = cur.description
        column_names = [col[0] for col in desc]
        for row in cur.fetchall():
            data_d1.append(dict(zip(column_names, list(row))))
        answer = data_d1
        conn.close()
        #answer01 = num_rec
        ##resp.body = ip + ' - ' + id_ + ' - ' + num_rec
        resp.body = answer
        resp.status = falcon.HTTP_200
        resp.set_header('X-Powered-By', 'Dataplazza')
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Headers', 'X-Requested-With')


desc = cursor.description
column_names = [col[0] for col in desc]
data = [dict(itertools.izip(column_names, row))  
        for row in cursor.fetchall()]

class Homepage(object):

    def on_get(self, req, resp):
        ##resp.data = msgpack.packb({'message': 'Hello world!'})
        ##resp.content_type = 'application/msgpack'
        resp.body = "this is the api's Home page"
        resp.status = falcon.HTTP_200

api = application = falcon.API()

api.add_route('/', Homepage())

api.add_route('/req1', Resource())