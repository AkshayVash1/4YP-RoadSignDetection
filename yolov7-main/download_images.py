from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

keywords = ["street stop sign"]

for kw in keywords:
    response().download(kw, 1000)