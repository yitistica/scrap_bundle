import itchat
from scrap_bundles.youtube import download_youtube


@itchat.msg_register(itchat.content.TEXT)
def download_youtube_by_msg(message):
    message_info = dict()
    message_info['text'] = message.text
    message_info['content'] = message.content
    message_info['sender'] = message.fromUserName
    message_info['recipient'] = message.toUserName
    print('receiving command ', message_info)

    texts = message_info['text'].split(',')
    if len(texts) == 1:
        url = texts[0]
        mp3_only = False
    else:
        url = texts[1]
        mp3_only = True

    request_msg = f'starting task on downloading {url} with setting mp3_only set to {mp3_only}'

    itchat.send_msg(request_msg, toUserName='filehelper')

    download_youtube(urls=[url], mp3_only=mp3_only)

    complete_ticket = f'completed downloading {url} with setting mp3_only set to {mp3_only}'

    itchat.send_msg(complete_ticket, toUserName='filehelper')


if __name__ == '__main__':
    itchat.auto_login()
    itchat.run()


