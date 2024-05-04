import os
import requests
from tqdm import tqdm

# COCO 2017 数据集下载链接
urls = [
    "http://images.cocodataset.org/zips/train2017.zip",
    "http://images.cocodataset.org/zips/val2017.zip",
    "http://images.cocodataset.org/annotations/annotations_trainval2017.zip"
]

# 下载目录
download_dir = "coco_dataset"
os.makedirs(download_dir, exist_ok=True)

# 下载文件
for url in urls:
    file_name = url.split("/")[-1]
    file_path = os.path.join(download_dir, file_name)

    if os.path.exists(file_path):
        print(f"{file_name} already exists, skipping download.")
        continue

    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024  # 1KB
    progress_bar = tqdm(total=total_size, unit="iB", unit_scale=True)

    with open(file_path, "wb") as file:
        for data in response.iter_content(block_size):
            if data:
                progress_bar.update(len(data))
                file.write(data)

    progress_bar.close()

    if total_size != 0 and progress_bar.n != total_size:
        print(f"Error downloading {file_name}, download may be incomplete.")
    else:
        print(f"{file_name} downloaded successfully.")