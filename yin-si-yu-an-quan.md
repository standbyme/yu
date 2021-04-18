# 隐私与安全

您的数据安全，始终是 ByteCare 关注的重中之重。未经您的允许，我们不会将您的数据传送至第三方（政策及法规规定除外）。

此外，我们允许您通过命令行选项参数，细粒度地控制每个任务的数据传输范围。

#### 不上传实时输出

通过 _disable-pub_ 参数，ByteCare 将不会上传任务输出。

```
care --disable-pub your command
```

#### 完全匿名

通过 _anonymous_ 参数，ByteCare 将不会上传任务输出，并对任务名称匿名化处理。

```
care --anonymous your command
```

{% hint style="info" %}
_anonymous_ 参数将导致您无法在任务列表中，区分多个匿名任务。在 ByteCare 后续的更新中会为匿名任务分配临时代号。
{% endhint %}

