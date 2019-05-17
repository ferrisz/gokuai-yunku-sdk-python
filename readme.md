# 够快云库 SDK Python版


django settings中配置

```
GOKUAI_SETTINGS = {
    "client_secret": "xxx",
    "client_id": "xxx",
    "host": "https://yk3.gokuai.com"
}
```

实例后使用
```
gokuai = Gokuai()
```

请求参数中不传入 client_id dateline sign
