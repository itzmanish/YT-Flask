from flask import Flask, jsonify
from flask_restplus import Resource, reqparse
from pafy.pafy import new


class YTSearch(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('link', type=str, help='Provide youtube link')

    @classmethod
    def get(cls):
        args = cls.parser.parse_args()

        try:
            video = new(args['link'])

        except ValueError:
            return 'Please check youtube url'

        return str(video)


class Best(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('link', type=str, help='Provide youtube link')

    @classmethod
    def get(cls):
        args = cls.parser.parse_args()
        try:
            video = new(args['link'])
            best = video.getbest()
        except ValueError:
            return 'plaese check youtube url'

        return best.url


class Test(Resource):
    def get(self):
        return 'server is working fine'
