import os
import requests
from osarch import detect_system_architecture
import zipfile


BASE_GOOGLE_URL = "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json"


def fetch_chrome(channel='Stable', product='chrome', download_path=os.getcwd(), unzip=True, delete_zip=True):
    os_name, architecture = detect_system_architecture()
    platform_key = f"{os_name}{architecture}"

    # Adjusted platform map
    platform_map = {
        'linux64': 'linux64',
        'mac64': 'mac-x64',
        'macarm64': 'mac-arm64',
        'win32': 'win32',
        'win64': 'win64',
        'darwin64': 'mac-x64',
        'darwinarm64': 'mac-arm64',
        'darwin32': 'mac-arm64',
    }

    response = requests.get(BASE_GOOGLE_URL)
    chrome_versions = response.json()

    try:
        download_url = next(item['url'] for item in chrome_versions['channels'][channel]['downloads'][product]
                            if item['platform'] == platform_map[platform_key])
    except StopIteration:
        print(f"No download URL found for {product} on platform {platform_key}")
        return

    local_filename = os.path.join(download_path, download_url.split('/')[-1])
    with requests.get(download_url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    if unzip:
        with zipfile.ZipFile(local_filename, 'r') as zip_ref:
            zip_ref.extractall(download_path)

    if delete_zip:
        os.remove(local_filename)

    return local_filename if unzip else download_url

