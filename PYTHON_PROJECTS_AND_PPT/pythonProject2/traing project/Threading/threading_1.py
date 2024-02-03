# Example 1: Downloading Images Concurrently
'''
The threading module uses threads, the multiprocessing module uses processes.
The difference is that threads run in the same memory space,
while processes have separate memory. This makes it a bit harder to
share objects between processes with multiprocessing.
Since threads use the same memory, precautions have to be taken or
two threads will write to the same memory at the same time.
This is what the global interpreter lock is for.
'''

# Suppose you want to download several images from the internet. Using threading, you can download multiple images simultaneously to speed up the process.

import threading
import requests

def download_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"{filename} downloaded")

image_urls = [
    "https://www.forbesindia.com/media/images/2022/Apr/img_183211_worldearthday.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/b/b5/Lion_d%27Afrique.jpg",
    "https://imgd.aeplcdn.com/600x337/n/cw/ec/44709/fortuner-exterior-right-front-three-quarter-19.jpeg",
    # ... add more URLs
]

threads = []
for i, url in enumerate(image_urls):
    filename = f"data/image_{i}.jpg"
    thread = threading.Thread(target=download_image, args=(url, filename))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All images downloaded")
