import os
import urllib.request

papers_dir = "/home/peter/Documents/proj/physeng_lab_reports/courses/nano2/squid/papers"
os.makedirs(papers_dir, exist_ok=True)

urls = {
    "doh_2005.pdf": "https://arxiv.org/pdf/cond-mat/0508558.pdf",
    "granata_2016.pdf": "https://arxiv.org/pdf/1505.06887.pdf",
    "vasyukov_2013.pdf": "https://arxiv.org/pdf/1308.0694.pdf",
    "halbertal_2016.pdf": "https://arxiv.org/pdf/1609.01487.pdf",
    "kalashnikov_2025.pdf": "https://arxiv.org/pdf/2510.15526.pdf"
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

for filename, url in urls.items():
    dest_path = os.path.join(papers_dir, filename)
    print(f"Downloading {filename} from {url}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(dest_path, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Successfully downloaded {filename} to {dest_path}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
