# Telegram Bot for Auto-Approving Join Requests

This is a Python-based Telegram bot that automatically approves chat join requests and tracks the bot's membership status in chats. Built using the `python-telegram-bot` library, it provides simple functionality for group management.

## Features
- Automatically approves join requests to Telegram groups.
- Logs join request approvals with user and chat details.
- Tracks when the bot is added to or removed from a chat.
- Supports a `/start` command to confirm the bot is active.

## Requirements
- Python 3.7+
- `python-telegram-bot` library (`pip install python-telegram-bot`)

## Setup
1. Replace `'TOKEN'` in the code with your Telegram Bot API token obtained from [BotFather](https://t.me/BotFather).
2. Install dependencies using `pip install -r requirements.txt` (create a `requirements.txt` with `python-telegram-bot`).
3. Run the bot with `python bot.py`.

## Usage
- Add the bot to a Telegram group and grant it admin privileges to approve join requests.
- Use the `/start` command to verify the bot is running.
- The bot will automatically approve join requests and log membership changes.

## Logging
- Logs are configured to output to the console with timestamps, logger name, level, and message.
- Logs include details of approved join requests and chat membership changes.

## Code Structure
- `start`: Responds to the `/start` command with a confirmation message.
- `approve_join_request`: Approves incoming chat join requests and logs the event.
- `track_chats`: Tracks and logs when the bot is added or removed from a chat.
- `main`: Initializes the bot and sets up handlers.

## License
MIT License

---

# ربات تلگرام برای تأیید خودکار درخواست‌های عضویت

این یک ربات تلگرامی مبتنی بر پایتون است که به‌صورت خودکار درخواست‌های عضویت در گروه‌ها را تأیید می‌کند و وضعیت عضویت ربات در گروه‌ها را رصد می‌کند. این ربات با استفاده از کتابخانه `python-telegram-bot` ساخته شده و قابلیت‌های ساده‌ای برای مدیریت گروه‌ها ارائه می‌دهد.

## ویژگی‌ها
- تأیید خودکار درخواست‌های عضویت در گروه‌های تلگرام.
- ثبت لاگ تأیید درخواست‌های عضویت با جزئیات کاربر و گروه.
- رصد زمان اضافه شدن یا حذف شدن ربات از گروه.
- پشتیبانی از دستور `/start` برای تأیید فعال بودن ربات.

## پیش‌نیازها
- پایتون نسخه 3.7 یا بالاتر
- کتابخانه `python-telegram-bot` (نصب با `pip install python-telegram-bot`)

## راه‌اندازی
1. مقدار `'TOKEN'` در کد را با توکن API ربات تلگرام که از [BotFather](https://t.me/BotFather) دریافت کرده‌اید جایگزین کنید.
2. وابستگی‌ها را با استفاده از `pip install -r requirements.txt` نصب کنید (فایل `requirements.txt` را با درج `python-telegram-bot` ایجاد کنید).
3. ربات را با اجرای `python bot.py` راه‌اندازی کنید.

## استفاده
- ربات را به یک گروه تلگرامی اضافه کنید و به آن دسترسی‌های مدیریتی برای تأیید درخواست‌های عضویت بدهید.
- از دستور `/start` برای اطمینان از فعال بودن ربات استفاده کنید.
- ربات به‌صورت خودکار درخواست‌های عضویت را تأیید کرده و تغییرات عضویت را ثبت می‌کند.

## لاگ‌ها
- لاگ‌ها برای نمایش در کنسول با درج زمان، نام لاگر، سطح و پیام تنظیم شده‌اند.
- لاگ‌ها شامل جزئیات درخواست‌های عضویت تأییدشده و تغییرات عضویت در گروه‌ها هستند.

## ساختار کد
- `start`: به دستور `/start` با یک پیام تأیید پاسخ می‌دهد.
- `approve_join_request`: درخواست‌های عضویت در گروه را تأیید کرده و رویداد را ثبت می‌کند.
- `track_chats`: زمان اضافه شدن یا حذف شدن ربات از گروه را رصد و ثبت می‌کند.
- `main`: ربات را راه‌اندازی کرده و هندلرها را تنظیم می‌کند.

## مجوز
مجوز MIT

---

# 用于自动批准加入请求的Telegram机器人

这是一个基于Python的Telegram机器人，用于自动批准群组加入请求并跟踪机器人在群组中的成员状态。使用`python-telegram-bot`库构建，提供简单的群组管理功能。

## 功能
- 自动批准Telegram群组的加入请求。
- 记录加入请求的批准情况，包括用户和群组的详细信息。
- 跟踪机器人被添加到群组或从群组中移除的时间。
- 支持`/start`命令以确认机器人处于活跃状态。

## 要求
- Python 3.7或更高版本
- `python-telegram-bot`库（使用`pip install python-telegram-bot`安装）

## 设置
1. 将代码中的`'TOKEN'`替换为从[BotFather](https://t.me/BotFather)获取的Telegram机器人API令牌。
2. 使用`pip install -r requirements.txt`安装依赖项（创建一个包含`python-telegram-bot`的`requirements.txt`文件）。
3. 使用`python bot.py`运行机器人。

## 使用
- 将机器人添加到Telegram群组，并授予其批准加入请求的管理员权限。
- 使用`/start`命令验证机器人是否正在运行。
- 机器人将自动批准加入请求并记录成员状态变化。

## 日志
- 日志配置为输出到控制台，包含时间戳、日志记录器名称、级别和消息。
- 日志包括已批准的加入请求和群组成员状态变化的详细信息。

## 代码结构
- `start`：响应`/start`命令，返回确认消息。
- `approve_join_request`：批准群组加入请求并记录事件。
- `track_chats`：跟踪并记录机器人被添加或移除出群组的事件。
- `main`：初始化机器人并设置处理程序。

## 许可证
MIT许可证