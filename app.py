from flask import Flask
from flask_restplus import Api
from pafy import pafy
from resources.yt import Test, YTSearch, Best

app = Flask(__name__)
api = Api(app)


# @api.route('/')
# class Hello(Resource):
#     def get(self):
#         url = 'https://www.youtube.com/watch?v=1dJT-99KpiI'
#         video = pafy.new(url)
#         best = video.getbest()
#         return best.url


api.add_resource(YTSearch, '/search')
api.add_resource(Best, '/getbest')
api.add_resource(Test, '/test')


if __name__ == '__main__':
    app.run(debug=True)
