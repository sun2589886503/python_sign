import requests
from requests import post

# 腾讯Cookie,
tx_cookie = 'pgv_pvi=9532715008; pgv_si=s6097810432; pgv_pvid=4728985042; RK=jHQZOoi/cy; ptcz=c878ef3196193867079105954a7aa7da301a56cc96c5749f205f2a90a40b592e; tvfe_boss_uuid=5cb4c653f2d41c26; o_cookie=289804037; sd_userid=22151616114020884; sd_cookie_crttime=1616114020884; wsreq_logseq=323089004; lolqqcomrouteLine=a20210402groovepass; tokenParams=%3Fe_code%3D505452; eas_sid=S1V6X1n7m8R0G1T2y7y1r39917; pgv_info=ssid=s2587555769&pgvReferrer=; _qpsvr_localtk=0.03191865403077143; pac_uid=1_289804037; IED_LOG_INFO=uin*289804037|nick*%u25A1%u25A1%u25A1%20|time*1620562463; dnfqqcomrouteLine=a20190228dpl_a20210506sign_a20210506sign_a20210506sign_a20210506sign_a20210506sign_a20210506sign; login_type=1; wxrefresh_token=; psrf_qqopenid=2B21BBCB9044E5736D2F70591D598DB8; psrf_qqunionid=; euin=owcqNenPoeol; wxopenid=; psrf_qqrefresh_token=AE8F43413B603989A67FC854DA8EDF36; wxunionid=; tmeLoginType=2; psrf_access_token_expiresAt=1628754856; psrf_qqaccess_token=10F2559214A39C6E260C39309A952811; idt=1623833092; iip=0; ied_qq=o0289804037; ptui_loginuin=643056365; video_guid=1e60df7a58d14662; video_platform=2; verifysession=h016e198c269f1e584b8fdde90d2adf7616c7c063d9bec77bfb43ee1b46e6816da5c7786ac039af817c; IED_LOG_INFO2=userUin%3D289804037%26nickName%3D%2525E2%252596%2525A1%2525E2%252596%2525A1%2525E2%252596%2525A1%26nickname%3D%25E2%2596%25A1%25E2%2596%25A1%25E2%2596%25A1%26userLoginTime%3D1625793090%26logtype%3Dqq%26loginType%3Dqq%26uin%3D289804037; _video_qq_login_time_init=1625796121; uid=85500769; midas_openid=289804037; midas_openkey=@le41TkNJQ; main_login=qq; vqq_access_token=93816BB3D2A8033383FBBF9A92996E48; vqq_appid=101483052; vqq_openid=3CC82F4EC2BF9ABB6F13F59E5FE45C1C; vqq_vuserid=361142255; vqq_vusession=gtJ5F_YL7AL-rasWCU0h_g..; vqq_refresh_token=730F6AEFBD3AE77A7812614161D1FB68;'
auth_refresh_url = 'https://access.video.qq.com/user/auth_refresh?vappid=11059694&vsecret=fdf61a6be0aad57132bc5cdf78ac30145b6cd2c1470b0cfe&type=qq&g_tk=&g_vstk=1239051337&g_actk=312625016&callback=jQuery19109796910878848941_1626057937014&_=1626057937021'

# TG配置
TG_TOKEN = 'xxx'  # TG机器人的TOKEN
CHAT_ID = 'xxx'  # 推送消息的CHAT_ID

# 新版Server酱配置
server_key = 'SCU125912Tea3c67d52932a8ee8fbacc30c5a06a675facd045a1968'

# 企业微信配置
corpid = 'xxx'     # 上面提到的你的企业ID
corpsecret = 'xxx'     # 上图的Secret
agentid = xxx  # 填写你的企业ID，不加引号，是个整型常数,就是上图的AgentId

# 企业微信推送
def wxPush(message):
    token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?' + 'corpid=' + corpid + '&corpsecret=' + corpsecret
    req_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='
    resp = requests.get(token_url).json()
    access_token = resp['access_token']
    data = {
        "touser": "@all",
        "toparty": "@all",
        "totag": "@all",
        "msgtype": "text",
        "agentid": agentid,
        "text": {
            "content": message
        },
        "safe": 0,
        "enable_id_trans": 0,
        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    }
    data = json.dumps(data)
    req_urls = req_url + access_token
    res = requests.post(url=req_urls, data=data)
    print(res.text)

# 新版Server酱推送
def send_server(title, content):
    server_content = {'text': title, 'desp': content}
    server_url = "https://sctapi.ftqq.com/%s.send" % server_key
    resp = requests.post(server_url, params=server_content)
    print('新版Server酱推送状态码为: %s' % resp.status_code)


# Telegram推送
def tgPush(telegram_message):
    params = (
        ('chat_id', CHAT_ID),
        ('text', telegram_message),
        ('parse_mode', "Markdown"),  # 可选Html或Markdown
        ('disable_web_page_preview', "yes")
    )
    telegram_url = "https://api.telegram.org/bot" + TG_TOKEN + "/sendMessage"
    post(telegram_url, params=params)


# 腾讯视频签到
def tx_sign():
    url1 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=hierarchical_task_system&cmd=2'
    url2 = 'https://v.qq.com/x/bu/mobile_checkin'
    url3 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=1'  # 观看60分钟
    url4 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=7'  # 下载
    url5 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=6'  # 赠送
    url6 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=3'  # 弹幕
    login_headers = {
        'Referer': 'https://v.qq.com',
        'Cookie': tx_cookie
    }
    login = requests.get(auth_refresh_url, headers=login_headers)
    resp_cookie = requests.utils.dict_from_cookiejar(login.cookies)
    if not resp_cookie:
        tgPush('腾讯视频V力值签到通知\n\n' + '获取Cookie失败，Cookie失效')
    arr = tx_cookie.split('; ')
    sign_cookie = ''
    for str in arr:
        if 'vqq_vusession' in str:
            continue
        else:
            sign_cookie += (str + '; ')
    sign_cookie += ('vqq_vusession=' + resp_cookie['vqq_vusession'] + ';')
    sign_headers = {
        'Cookie': sign_cookie,
        'Referer': 'https://m.v.qq.com'
    }
    send_message = ''
    sign1 = response_handle(url1, sign_headers)
    send_message += '链接1' + sign1 + '\n'
    # sign2 = response_handle(url2, sign_headers)
    send_message += '链接2' + '任务未完成' + '\n'
    sign3 = response_handle(url3, sign_headers)
    send_message += '链接3' + sign3 + '\n'
    sign4 = response_handle(url4, sign_headers)
    send_message += '链接4' + sign4 + '\n'
    sign5 = response_handle(url5, sign_headers)
    send_message += '链接5' + sign5 + '\n'
    sign6 = response_handle(url6, sign_headers)
    send_message += '链接6' + sign6 + '\n'
    mes = '腾讯视频V力值签到通知\n\n' + send_message
    return mes


# 处理腾讯视频返回结果
def response_handle(url, sign_headers):
    resp_str = requests.get(url, headers=sign_headers).text
    if '-777903' in resp_str:
        return "已获取过V力值"
    elif '-777902' in resp_str:
        return "任务未完成"
    elif 'OK' in resp_str:
        return "成功，获得V力值：" + resp_str[42:-14]
    else:
        return "执行出错"


if __name__ == '__main__':
    message = tx_sign()
    send_server('腾讯视频签到通知', message)
