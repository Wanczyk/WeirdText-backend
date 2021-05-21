import falcon
from json import dumps
from src import WeirdText


class EncodeText:
    def on_post(self, req, resp):
        result = req.media
        encoded_text, original_words = WeirdText.encode(result["text"])
        resp.text = dumps({
            "encoded_text": encoded_text,
            "original_words": original_words
        })


class DecodeText:
    def on_post(self, req, resp):
        result = req.media
        decoded_text = WeirdText.decode(result["text"], result["original_words"])
        resp.text = dumps({
            "decoded_text": decoded_text
        })


app = falcon.App(middleware=falcon.CORSMiddleware(
    allow_origins='https://gracious-mcclintock-76e52c.netlify.app', allow_credentials='*'))
app.add_route('/v1/encode', EncodeText())
app.add_route('/v1/decode', DecodeText())
