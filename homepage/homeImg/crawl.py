# -*- coding: utf-8 -*-
"""
서비스디자인연구실 웹사이트 이미지 다운로드 스크립트
https://servicedesignlabkumoh.framer.website/
"""

import urllib.request
import os

# 이미지 URL과 파일명 매핑
IMAGES = [
    ("https://framerusercontent.com/images/Ex7fsElW9OeF6FLt7a9flnH73ws.png", "01_kumoh_university_logo.png"),
    ("https://framerusercontent.com/images/98Rj6X3YOxYFGnyjIoQ7mZdekY.png", "02_professor_profile.png"),
    ("https://framerusercontent.com/images/IG4NpoF80EBSBxxg3YLFyBYt6sU.png", "03_2024_gumi_ramen_festival.png"),
    ("https://framerusercontent.com/images/x6PyG51R4DarwJv68u98zdil5g.png", "04_2024_low_birthrate_research_workshop.png"),
    ("https://framerusercontent.com/images/vTNWnMSZmHAVq5vjUcyK6yv4QU.png", "05_2024_gumi_citizen_policy_design.png"),
    ("https://framerusercontent.com/images/0P4JQ84v1XDwJ2Ov7jbZsL27Mvc.png", "06_2024_metaverse_floorviz.png"),
    ("https://framerusercontent.com/images/fD1xBjuBB8rVZioDpfzaxkyl0Z0.png", "07_2025_gumi_2030_women_forum.png"),
    ("https://framerusercontent.com/images/QN2AJ7mzz8givGD5t6IDlX9vCQc.png", "08_location_map.png"),
]

# 저장 폴더 생성
output_dir = "downloaded_images"
os.makedirs(output_dir, exist_ok=True)

print("다운로드 시작...")
print("-" * 50)

for url, filename in IMAGES:
    filepath = os.path.join(output_dir, filename)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as response:
            with open(filepath, "wb") as f:
                f.write(response.read())
        print(f"[OK] {filename}")
    except Exception as e:
        print(f"[FAIL] {filename} - {e}")

print("-" * 50)
print(f"완료! 저장 위치: {os.path.abspath(output_dir)}")
input("엔터를 누르면 종료됩니다...")