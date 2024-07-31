import os
from bs4 import BeautifulSoup
import urllib.parse

def update_image_paths(html_file, output_file, static_folder='images'):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    for img in soup.find_all('img'):
        original_src = img['src']
        file_name = os.path.basename(original_src)
        # 공백과 URL 인코딩 문제 해결
        file_name = urllib.parse.unquote(file_name)
        img_path = os.path.join(static_folder, file_name).replace("\\", "/")
        img['src'] = "{{ url_for('static', filename='" + img_path + "') }}"

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))

# 사용 예시
html_file = 'big.html'
output_file = 'templates/big4.html'
update_image_paths(html_file, output_file)
