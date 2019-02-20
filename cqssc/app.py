# coding: utf-8
import json
from tornado.options import options, define, parse_command_line
from tornado import web
from tornado import gen
from tornado import ioloop
from tornado.log import app_log
from tornado.concurrent import futures

import validate
import compute

define("port", default=80, type=int)


class BaseHandler(web.RequestHandler):

    log = app_log
    executor = futures.ThreadPoolExecutor(8)

    def set_default_headers(self):
        self.set_header("Content-Type", "application/json;charset:utf-8")


class ValidateHandler(BaseHandler):

    @gen.coroutine
    def post(self):
        data = json.loads(self.request.body)
        num  = validate.Validate(data["tag"], data["code"])
        self.log.info("Validate Tag:%s Code:%s Num:%d", data["tag"], data["code"], num)
        self.write({"num": num})


class ComputeHandler(BaseHandler):

    @gen.coroutine
    def post(self): 
        data = json.loads(self.request.body)
        num  = compute.Compute(data["tag"], data["result"], data["code"])
        self.log.info("Compute Tag:%s Result:%s Code:%s Num:%d", data["tag"], data["result"], data["code"], num)
        self.write({"num": num})


def main():
    parse_command_line()
    handlers = (
        (r'/validate', ValidateHandler),
        (r'/compute',  ComputeHandler),
        )
    app = web.Application(handlers, 
        debug=True, compress_response=True, autoreload=True)
    app.listen(options.port)
    ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()