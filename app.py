from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
        "https://mblogthumb-phinf.pstatic.net/MjAxNjEyMTBfMTA2/MDAxNDgxMzc0MTc5Njg1.KPDQ0lxUmxqE2OFYN-ZXb-enD_1BgZq8TWt7QRnbEK8g.g5OYAQJ_-fcefXhEMh3hRCjJFLU9QD2YdeODqfaK_qUg.GIF.hal_f_ull/%EB%8F%84%EA%B9%A8%EB%B9%84_10.gif?type=w2",
	"https://mblogthumb-phinf.pstatic.net/MjAxNjEyMTBfMTM4/MDAxNDgxMzc1MjQxNTI2.gN4uw7LArLBbh0iu-TRrLds1VX8Q7ok1qyWxVHJRsskg.adArFIkPIpKFT6cv6HuB9bwaokXjrPu3UhBVVWLOHo8g.GIF.hal_f_ull/%EB%8F%84%EA%B9%A8%EB%B9%84_13.gif?type=w2",
	"https://mblogthumb-phinf.pstatic.net/MjAxNjEyMTBfMjE3/MDAxNDgxMzc1MjQyNzA0.psx_Mt9SwNZFvdFLM35G89PpWcD9JLAEhJCQeRLq5OMg.n_-yyAY0qSKkaH3hdZhNqwhSAydauLO2cvInKxC6afIg.GIF.hal_f_ull/%EB%8F%84%EA%B9%A8%EB%B9%84_14.gif?type=w2",
	"https://mblogthumb-phinf.pstatic.net/MjAxNjEyMTBfMjMz/MDAxNDgxMzc1MjQzNjA2.tSm-vxrCd7Yhb9MYQIgcF8Mnng0AoW05WQDTj7fbpt4g.hLqIasbzEOXphqpr19B7_5mGwytegvF15qIl1LGeX-Yg.GIF.hal_f_ull/%EB%8F%84%EA%B9%A8%EB%B9%84_15.gif?type=w2",
	"https://mblogthumb-phinf.pstatic.net/MjAxNjEyMTBfODIg/MDAxNDgxMzc1MjQ0NTQ3.7nTRyGaWcK23MMjhN-a-AOOp8sATC6RgmcroKTp7hTwg.9M6hC7ZD5O1nFibXlRySwgAbAZPH6THdbv1qyjX3hPMg.GIF.hal_f_ull/%EB%8F%84%EA%B9%A8%EB%B9%84_16.gif?type=w2",
	"https://mblogthumb-phinf.pstatic.net/MjAxNjEyMTBfNzEg/MDAxNDgxMzc0MTgwOTY5.q4186f0V1HwgAn5DC6qdQJmqLLb8ZztpoRKSJWKYv14g.Bn_Z6FPqIhL1ASVpAprrGtkGO2zwtgoejoeiO5rSw78g.GIF.hal_f_ull/%EB%8F%84%EA%B9%A8%EB%B9%84_11.gif?type=w2",
	"https://mblogthumb-phinf.pstatic.net/MjAxNjEyMTBfMTEg/MDAxNDgxMzc0MTgyMjA1.3YTZXC9liItfxIvLDYJ5oecV_h2tJ37Q5jaY-ElueH0g.SI2pcuO7cUhGbXTdy0cZZ81grTSve70wlWJSNW_xkUIg.GIF.hal_f_ull/%EB%8F%84%EA%B9%A8%EB%B9%84_12.gif?type=w2",
	"https://mblogthumb-phinf.pstatic.net/MjAxNjEyMTBfMjYg/MDAxNDgxMzc0MTgzNjMx.q8kTb2QY8kPQfRIyzd5Xetcb3n2XtsFmqWk2LCgE85gg.sBcI5sL2od3PCf_F9FoHMPqlR7Bc4DrBzSTF4lGVleIg.GIF.hal_f_ull/%EB%8F%84%EA%B9%A8%EB%B9%84_9.gif?type=w2",
	"https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile9.uf.tistory.com%2Fimage%2F260754395888A96E1143AD",
	"https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile1.uf.tistory.com%2Fimage%2F263C56395888A9A2347E82",
	"https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile7.uf.tistory.com%2Fimage%2F2761BE395888A9D40B61C3"
        ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
