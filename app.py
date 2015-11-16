import falcon

##import msgpack


class Resource(object):

    def on_get(self, req, resp):
        ##resp.data = msgpack.packb({'message': 'Hello world!'})
        ##resp.content_type = 'application/msgpack'
        ip = req.env['REMOTE_ADDR']
        id_ = req.params['id']
        resp.body = ip + ' - ' + id_
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