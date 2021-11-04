# LineNotify
![](https://img.shields.io/badge/python-3.9-blue.svg) ![](https://badge.fury.io/py/linenotif.svg)  
Line Notif is a libarary which use for send message via [LINE notify](https://notify-bot.line.me/th/) for [LINE](https://line.me/th/) application.

### Example
```python
import linenotif

noti = linenotif.Notify()
noti.setKey("YOURAPIKEY")
noti.send_message("Hello Notify")
```
