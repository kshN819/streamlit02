import streamlit as st

# 입력화면   -HTML/CSS/JS로 최종적으로 변환

# 검색창
# 해당 입력창에서 데이터를 받아서

# data = [1,2,3]
url = 'https://naver.com'

# 입력화면- HTML/CSS/JS 로 최종적으로 변환

# ani_list = ['짱구는못말려', '몬스터','릭앤모티']
# img_list = ['https://i.imgur.com/t2ewhfH.png', 
#             'https://i.imgur.com/ECROFMC.png', 
#             'https://i.imgur.com/MDKQoDc.jpg']
name_list = ["짱구는못말려","몬스터","릭앤모티"]
img_list = ["https://i.imgur.com/t2ewhfH.png",".https://i.imgur.com/ECROFMC.png","https://i.imgur.com/MDKQoDc.jpg"]

var = st.text_input("제목을 입력하세요: ")
if var == "짱구는못말려":
    st.image(img_list[0])
    st.download_button(label = "download '짱구는못말려' Image", data = img_list[0], file_name = "jjanggu.png")
elif var == "몬스터":
    st.image(img_list[1])
    st.download_button(label = "download '몬스터' Image", data = img_list[1], file_name = "monster.png")
elif var == "릭앤모티":
    st.image(img_list[2])
    st.download_button(label = "download '릭앤모티' Image", data = img_list[2], file_name = "rickandmorty.jpeg")


