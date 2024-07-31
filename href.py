import os
import re
from bs4 import BeautifulSoup
import urllib.parse

def clean_uuid(filename):
    # UUID 패턴을 찾아 제거
    pattern = re.compile(r'[-\w]{36}')
    return pattern.sub('', filename).strip()

def update_paths(html_file, output_file, static_folder='images'):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Update href tags for html files
    for a in soup.find_all('a', href=True):
        original_href = a['href']
        if original_href.endswith('.html'):
            # UUID 제거
            file_name = clean_uuid(os.path.basename(original_href))
            # 공백과 URL 인코딩 문제 해결
            file_name = urllib.parse.unquote(file_name)
            page_name = os.path.splitext(file_name)[0]
            a['href'] = "{{ url_for('" + page_name + "') }}"

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))

# 사용 예시
html_file = 'gcp.html'
output_file = 'templates/gcp.html'
update_paths(html_file, output_file)
