import os
from glob import glob
from tqdm.auto import tqdm
import requests
from zipfile import ZipFile
import lasio


def download_zip(url,extract_to='.'):
    filename = url.split('/')[-1]
    r = requests.get(url,stream=True)
    ZipFile.extractall(path=extract_to)


urls = [
    'https://dnxxuwuw8tglo.cloudfront.net/Wells/P00524457.zip',
    'https://dnxxuwuw8tglo.cloudfront.net/Wells/P00524458.zip',
    'https://dnxxuwuw8tglo.cloudfront.net/Wells/P00524459.zip'
]

for url in tqdm(urls,total=len(urls)):
    download_zip(url)