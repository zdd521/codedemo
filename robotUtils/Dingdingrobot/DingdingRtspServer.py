import os
import logging

# 获取钉钉秘钥：SEC4a4dd58f404dd8728fedc220dc47bdddcc19af0553ccae9f4677382f432309c8
# socket地址：https://oapi.dingtalk.com/robot/send?access_token=0e344242279a5502d240e75ed5a650888793d2b770bcd42c9e1dd1400900240a

# curl 'https://oapi.dingtalk.com/robot/send?access_token=0e344242279a5502d240e75ed5a650888793d2b770bcd42c9e1dd1400900240a' -H 'Content-Type: application/json'  -d '{"msgtype": "text","text": {"content":"我就是我, 是不一样的烟火"}}'
import requests


def log_2_file(flag: bool = True, file_name : str = None, log_type = logging.INFO):
    """

    :param log_type:
    :param flag:
    :param file_name:
    :return:
    """
    if flag:
        file_name = os.path.join(os.path.abspath(__file__), 'log.txt') if not file_name else file_name
        logging.basicConfig(filename=file_name, level=log_type)
    else:
        logging.basicConfig(level=log_type)


def dingdingalarm(message, webhook, log: bool = True):
    """

    :param log:
    :param message:
    :param webhook:
    :return:
    """
    data = {
        "msgtype": "text",
        "text": {
            "content": message
        }
    }
    try:
        requests.post(webhook, json=data)
    except Exception as e:
        if log:
            logging.info(msg=str(e))


if __name__ == '__main__':
    dingdingalarm("RTSP报警: hello world",
                  "https://oapi.dingtalk.com/robot/send?access_token=0e344242279a5502d240e75ed5a650888793d2b770bcd42c9e1dd1400900240a")
