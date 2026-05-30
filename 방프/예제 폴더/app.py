import streamlit as st
import requests
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd

client_id = "xrUlqa5aKZBBKbrx3PJu"
client_secret = "lmyMjJ8qNM"

st.title("🔍 TrendCheck")
st.subheader("한국 유행어 트렌드 분석기")

keyword = st.text_input("분석할 키워드를 입력하세요", placeholder="예: 두바이초콜릿, 브레인로트")

if st.button("분석하기") and keyword:
    with st.spinner("데이터 수집 중..."):
        url = "https://openapi.naver.com/v1/datalab/search"
        headers = {
            "X-Naver-Client-Id": client_id,
            "X-Naver-Client-Secret": client_secret,
            "Content-Type": "application/json"
        }
        body = {
            "startDate": "2024-01-01",
            "endDate": "2026-05-17",
            "timeUnit": "week",
            "keywordGroups": [
                {"groupName": keyword, "keywords": [keyword]}
            ]
        }
        response = requests.post(url, headers=headers, json=body)
        data = response.json()

        periods = [d["period"] for d in data["results"][0]["data"]]
        ratios = [d["ratio"] for d in data["results"][0]["data"]]
        
        df = pd.DataFrame({"날짜": periods, "검색량": ratios})
        df["날짜"] = pd.to_datetime(df["날짜"])

        # 유행 판별
        max_ratio = max(ratios)
        current_ratio = ratios[-1]
        recent_trend = ratios[-4:]
        
        if max_ratio >= 50:
            if current_ratio >= max_ratio * 0.7:
                status = "🔥 유행중 (정점)"
            elif current_ratio >= max_ratio * 0.3:
                status = "📉 하락중"
            else:
                status = "💀 소멸"
        elif recent_trend[-1] > recent_trend[0] * 1.5:
            status = "📈 상승중"
        else:
            status = "😴 비유행"

        st.markdown(f"### {keyword} — {status}")
        st.line_chart(df.set_index("날짜")["검색량"])
        
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        col1.metric("최고 검색량", f"{max_ratio:.1f}")
        col2.metric("현재 검색량", f"{current_ratio:.1f}")
        col3.metric("정점 대비", f"{(current_ratio/max_ratio*100):.1f}%")

        