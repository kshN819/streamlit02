import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

# 텍스트 입력창
title = st.text_input("검색하실 애니메이션을 입력하세요", "")

for ani_ in ani_list:
    if title in ani_:
        # ani_list에서 특정 문자열을 포함한 인덱스를 찾아서
        img_idx = ani_list.index(ani_)

if title != '':
    st.image(img_list[img_idx])
    