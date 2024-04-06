from tqdm.auto import tqdm
from utils import download_zip


urls = [
    'https://dnxxuwuw8tglo.cloudfront.net/Wells/P00524457.zip',
    'https://dnxxuwuw8tglo.cloudfront.net/Wells/P00524458.zip',
    'https://dnxxuwuw8tglo.cloudfront.net/Wells/P00524459.zip'
]

for url in tqdm(urls,total=len(urls)):
    download_zip(url)