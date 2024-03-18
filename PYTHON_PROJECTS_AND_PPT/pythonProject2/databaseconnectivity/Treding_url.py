import threading
import requests

def download_image(url,filename):
    response = requests.get(url)
    with open(filename,'wb')as f:
        f.write(re)





threading = []
for i, url in enumerate(image_urls):
    filename = f"data/image_{i}.jpg"
    thread = threading.Thread(terge=download_image,args=(url))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join

print("ALL images downloaded")