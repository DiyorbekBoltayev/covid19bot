import requests

url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

querystring = {"url":"https://www.tiktok.com/@nor10122/video/7037155617491913986"}

headers = {
	"X-RapidAPI-Key": "3f8c00c5c3mshc5c673eb199b7cfp1c6d2cjsn66609070bc65",
	"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)