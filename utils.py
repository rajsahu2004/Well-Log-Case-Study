import os
import requests
from zipfile import ZipFile

def download_zip(url,extract_to='.'):
    filename = os.path.join(extract_to, url.split('/')[-1])
    if os.path.isfile(filename):
        print(f'{filename} already exists')
    print(f"Downloading {url}...")
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f'Extracting {filename}...')
    with ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f'Deleting {filename}')
    os.remove(filename)