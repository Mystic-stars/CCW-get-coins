import requests
import re
from datetime import datetime
if 1==1:
    try:
        with open("account.txt", "r") as f:
            t = f.read()
    except:
        print("Warn! account.txt cannot be found!")

    # 初始化程序变量
    current_datetime = datetime.now()
    current_date = current_datetime.strftime("%Y%m%d")

    while True:
        with open("account.txt", "r") as file:
            accounts = file.read().splitlines()
        password = "12345678"
        url = "https://sso.ccw.site/web/auth/login-by-password"

        headers = {
            "A": "e13d25c71bf9ea2e68b5482751b9fa3a",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "B": "1708332840215",
            "Content-Length": "140",
            "Content-Type": "application/json",
            "Cookie": "Hm_lvt_bfae6bcf06a59b7687742b13f7e7e5b0=1707283788,1707284744,1708330493; Hm_lpvt_bfae6bcf06a59b7687742b13f7e7e5b0=1708330540",
            "Origin": "https://www.ccw.site",
            "Referer": "https://www.ccw.site/",
            "Sec-Ch-Ua": '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Toke": "e13d25c71bf9ea2e68b5482751b9fa3a",
            "Traceparent": "00-7dcde13ea3ff938fe6e9134e8acf38e8-c81253a96875a592-01",
            "Tt": "1708332840215",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        }

        tokens = []
        oids = []
        error_accounts = []

        for account in accounts:
            payload = {
                "clientCode": "STUDY_COMMUNITY",
                "extra": '{"device":"Python requests","browser":"CC_Tools"}',
                "loginKey": account,
                "password": "12345678",
            }

            response = requests.post(url, headers=headers, json=payload)

            msg = re.findall('"msg":(.*?),', response.text)[0]
            if msg == "null":
                oid = re.findall('"accountObjectId":"(.*?)"', response.text)[0]
                token = re.findall('"token":"(.*?)"', response.text)[0]
                tokens.append(token)
                oids.append(oid)
                print(f"token:{token}  oid:{oid}")
            else:
                print(msg, " 错误账号ID:", account)
                error_accounts.append(account)

        with open("token.txt", "w") as file:
            for token in tokens:
                file.write(token + "\n")

        with open("oid.txt", "w") as file:
            for oid in oids:
                file.write(oid + "\n")

        with open("account.txt", "w") as file:
            for account in accounts:
                if account not in error_accounts:
                    file.write(account + "\n")

        print(
            f"已将token写入token.txt中 oid写入oid.txt中,删除了 " + str(len(error_accounts)) + "个账号"
        )
        # 签到
        tokens = []
        with open("token.txt", "r") as file:
            tokens = file.read().splitlines()

        url = "https://community-web.ccw.site/study-community/check_in_record/insert"

        headers = {
            "A": "97ad04d8b4c1cc4b6196284090cf2d06",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "B": "1708334726434",
            "Content-Length": "20",
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": "https://www.ccw.site",
            "Referer": "https://www.ccw.site/",
            "Sec-Ch-Ua": '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        }

        success_count = 0

        for token in tokens:
            headers["Token"] = token
            payload = {"scene": "HOMEPAGE"}

            response = requests.post(url, headers=headers, json=payload)
            msg = re.findall('"msg":(.*?),', response.text)[0]

            if msg == "null":
                success_count += 1
                print(f"签到成功 token:{token}")
            else:
                print(f"签到失败 原因：{msg}")

        print(f"有{success_count}个账号签到成功")
        # 金币传输
        give_i = 0
        tokens = []
        with open("token.txt", "r") as file:
            tokens = file.read().splitlines()
        give_proj = "0"
        if give_proj == "0":
            give_proj = "64b226d6416b4c13e613c2fa"
        givecoins_num = "0"
        url = "https://community-web.ccw.site/study-trade/trade/donate"
        give_all_num = 0
        if givecoins_num != "0":
            for token in tokens:
                headers = {
                    "A": "b153100f15002c6ec1cca3e775048f27",
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                    "B": "1708345373038",
                    "Content-Length": "73",
                    "Content-Type": "application/json;charset=UTF-8",
                    "Origin": "https://www.ccw.site",
                    "Referer": "https://www.ccw.site/",
                    "Sec-Ch-Ua": '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
                    "Sec-Ch-Ua-Mobile": "?0",
                    "Sec-Ch-Ua-Platform": '"Windows"',
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-site",
                    "Token": token,
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
                }

                payload = {
                    "bucks": givecoins_num,
                    "objectId": give_proj,
                    "objectType": "CREATION",
                }

                response = requests.post(url, headers=headers, json=payload)
                msg = re.findall('msg":(.*?),', response.text)[0]
                if msg == "null":
                    msg = "投币成功"
                    give_i = give_i + 1
                else:
                    msg = "投币失败" + msg
                print(msg, f"已投币数量:{int(givecoins_num) * int(give_i)}")
            success_coins = (int(givecoins_num) * int(give_i)) * 0.7
            print(
                f"投币结束，目前投币数量{int(givecoins_num) * int(give_i)}，实际到账数量{success_coins}"
            )
        else:
            for token in tokens:
                url = "https://community-web.ccw.site/currency/account/personal"

                headers = {
                    "A": "c4d4bfedb24099a598de90022c8b39bf",
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                    "B": "1708342860190",
                    "Content-Length": "0",
                    "Origin": "https://www.ccw.site",
                    "Referer": "https://www.ccw.site/",
                    "Sec-Ch-Ua": '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
                    "Sec-Ch-Ua-Mobile": "?0",
                    "Sec-Ch-Ua-Platform": '"Windows"',
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-site",
                    "Token": token,
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
                }

                response = requests.post(url, headers=headers)
                coins = int(
                    float(
                        re.findall('"internalCurrencyBalance":(.*?),', response.text)[0]
                    )
                )
                url = "https://community-web.ccw.site/study-trade/trade/donate"
                headers = {
                    "A": "b153100f15002c6ec1cca3e775048f27",
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                    "B": "1708345373038",
                    "Content-Length": "73",
                    "Content-Type": "application/json;charset=UTF-8",
                    "Origin": "https://www.ccw.site",
                    "Referer": "https://www.ccw.site/",
                    "Sec-Ch-Ua": '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
                    "Sec-Ch-Ua-Mobile": "?0",
                    "Sec-Ch-Ua-Platform": '"Windows"',
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-site",
                    "Token": token,
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
                }

                payload = {
                    "bucks": coins,
                    "objectId": give_proj,
                    "objectType": "CREATION",
                }

                response = requests.post(url, headers=headers, json=payload)
                msg = re.findall('msg":(.*?),', response.text)[0]
                if msg == "null":
                    msg = "投币成功"
                    give_all_num = give_all_num + coins
                else:
                    msg = "投币失败" + msg
                print(msg, f"已投币数量:{str(give_all_num)}")

            print(f"投币结束，目前投币数量:{str(give_all_num)}，实际到账数量:{str(give_all_num * 0.7)}")

        break
