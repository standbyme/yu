# 快速上手

ByteCare 可以帮助开发者更高效的获取程序的结果，避免在命令行前无意义的等待。并支持在程序异常退出、系统宕机时及时向开发者发出通知。

在进行以下步骤前，您需要 [通过 GitHub 登录 ByteCare](https://github.com/login/oauth/authorize?access_type=offline&client_id=5438af48a44fcf64b10f&response_type=code&scope=user%3Aemail)。

#### 1. 安装

目前 ByteCare 仅支持在 Linux 下运行，Windows 与macOS 的支持将在稍后推出。

在命令行中键入如下命令即可完成安装。

```bash
curl --proto '=https' --tlsv1.2 -sSf https://start.bytecare.xyz/sh | sh
```

#### 2. 配置

安装完成后，在 [密钥](https://www.bytecare.xyz/account-general.html) 页面复制您的**配置命令**，格式类似：

```bash
care \
	--access-key=AK \
	--secret-key=SK
```

在命令行中，粘贴并运行配置命令即可。

{% hint style="info" %}
提示 _**care: command not found**_ 怎么办？

ByteCare 默认将安装至 _~/.local/bin_ 目录下，可使用如下命令将该路径增加至 _PATH_ 环境变量中：

```bash
echo PATH=$PATH:$HOME/.local/bin >> ~/.bashrc
source ~/.bashrc
```
{% endhint %}

#### 3. 体验 ByteCare

您已完成所有配置，使用如下命令体验 ByteCare：

```bash
care echo "Hello ByteCare~"
```

如配置正确，命令完成后，您的 GitHub 注册邮箱中将收到邮件通知。

### 😃 配置微信通知

邮箱通知常会面临系统拦截、延时高、查阅不方便等情况。ByteCare 提供了微信服务号，可查询正在执行的程序，与实时输出。

{% page-ref page="tong-zhi-fang-shi/she-zhi-wei-xin-tong-zhi.md" %}

ByteCare 将在未来支持短信、电话、钉钉、企业微信、Slack 与 Microsoft Teams 等更多通知方式。

