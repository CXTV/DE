a = {'type': 'EN2ZH_CN', 'errorCode': 0, 'elapsedTime': 0, 'translateResult': [[{'src': 'Hello, welcome, everyone.', 'tgt': '你好,欢迎,每一个人。'}]]}

print(a.get("translateResult",[])[0][0].get('tgt',''))