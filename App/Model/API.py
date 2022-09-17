import httpx
import requests

url = "https://qrcode3.p.rapidapi.com/qrcode/text"

payload = {
	"data": "https://linqr.app",
	"image": {
		"uri": "icon://appstore",
		"modules": True
	},
	"style": {
		"module": {
			"color": "black",
			"shape": "default"
		},
		"inner_eye": {"shape": "default"},
		"outer_eye": {"shape": "default"},
		"background": {}
	},
	"size": {
		"width": 200,
		"quiet_zone": 4,
		"error_correction": "M"
	},
	"output": {
		"filename": "qrcode",
		"format": "png"
	}
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "683b435bd8mshe2e9806278fe2c3p1efd19jsndfbf4d74fe54",
	"X-RapidAPI-Host": "qrcode3.p.rapidapi.com"
}


if __name__ == '__main__':
	response = requests.request("POST", url, json=payload, headers=headers)
	print(response.text)