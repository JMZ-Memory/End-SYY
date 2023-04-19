import requests
from bs4 import BeautifulSoup

headers = {
    'cookie': "buvid3=A7F88738-FD71-11C0-5C8F-177C0FEFD97023658infoc; b_nut=1666098923; i-wanna-go-back=-1; _uuid=B5B825CE-BB6B-E22A-46C8-E97938A6B64723118infoc; buvid_fp_plain=undefined; nostalgia_conf=-1; buvid4=3F4D5496-4902-7AE3-B6A8-FCAE7A266E2724299-022101821-bd0aoMtp0ggdXro/WFivpA==; hit-dyn-v2=1; LIVE_BUVID=AUTO8516661476768797; CURRENT_BLACKGAP=0; fingerprint3=763e11abf74cf4870b18e1b7523592b7; is-2022-channel=1; rpdid=|(umR~~|lmkl0J'uYY)l~k~R); blackside_state=1; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1670867752,1672340539,1672408029,1672499569; hit-new-style-dyn=1; go-back-dyn=0; CURRENT_FNVAL=4048; DedeUserID=11879526; DedeUserID__ckMd5=7aab0167d042f0ca; b_ut=5; CURRENT_QUALITY=80; CURRENT_PID=5e556320-c870-11ed-b86c-ddc67f927fd9; header_theme_version=CLOSE; home_feed_column=5; FEED_LIVE_VERSION=V8; fingerprint=46aec2c118ec538baf38e772518aaada; SESSDATA=ba166ac6,1697174574,d012e*41; bili_jct=b10b53d3ca7b8272e04531eb3f5a578f; sid=8buto2k6; bp_video_offset_11879526=785136428716654600; PVID=25; buvid_fp=46aec2c118ec538baf38e772518aaada; innersign=1; b_lsid=B107C6C21_1878ACBFC23",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
content = requests.get('https://www.bilibili.com/blackboard/activity-award-exchange.html?task_id=1c0bec85',
                       headers=headers).text
soup = BeautifulSoup(content, "html.parser")
print(content)
button = soup.findAll("section", attrs={"class": "tool-wrap"})

print(button)
