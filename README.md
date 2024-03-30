以下是在Python中使用Helicone的快速入门指南:

## 安装Helicone

首先,您需要安装Helicone Python包:

```python
pip install helicone
```

## 设置Helicone

接下来,导入必要的模块并设置您的Helicone API密钥:

```python
from helicone.openai_proxy import openai
import os

os.environ["HELICONE_API_KEY"] = "your_helicone_api_key"
```

将`your_helicone_api_key`替换为您在Helicone网站上获得的实际API密钥。

## 使用Helicone

现在您可以像平常一样使用OpenAI API,但是通过Helicone代理:

```python
response = openai.Completion.create(
    model="text-davinci-003",
    prompt="What is Helicone?",
    user="alice@example.com" # 可选的Helicone功能
)

print(response.choices[0].text)
```

这个示例向OpenAI发送一个完成请求,并打印响应。您可以使用Helicone的其他功能,如缓存、自定义速率限制和属性:

```python
response = openai.Completion.create(
    model="text-davinci-003", 
    prompt="What is the capital of France?",
    cache=True, # 启用缓存
    properties={"conversation_id": 123}, # 添加自定义属性
    rate_limit_policy={"quota": 100, "time_window": 60, "segment": "user"} # 自定义速率限制
)
```

您可以在Helicone网站上查看请求日志和分析。[1][2][3]

这就是在Python中快速开始使用Helicone的方法。Helicone文档提供了更多高级用法示例。[4]

Citations:
[1] https://www.langchain.com.cn/ecosystem/helicone
[2] https://python.langchain.com/docs/integrations/providers/helicone
[3] https://github.com/Helicone/helicone
[4] https://docs.helicone.ai/features/jobs/quick-start
[5] https://liduos.com/what-is-the-helicone.html
[6] https://docs.helicone.ai/graphql/python-example
[7] https://docs.aws.amazon.com/zh_cn/glue/latest/dg/aws-glue-programming-python-libraries.html
[8] https://docs.helicone.ai/getting-started/quick-start
[9] https://new.qq.com/rain/a/20230508A0399W00
[10] https://docs.helicone.ai/graphql/getting-started
[11] https://web3py.readthedocs.io/en/stable/quickstart.html
[12] https://developers.lseg.com/en/api-catalog/eikon/eikon-data-api/quick-start
[13] https://developers.google.com/meet/api/guides/quickstart/python
[14] https://www.chinaz.com/ai/tool/2000319.shtml
[15] https://developers.google.com/drive/api/quickstart/python
[16] https://learn.microsoft.com/zh-cn/azure/developer/python/sdk/azure-sdk-library-usage-patterns
[17] https://docs.vocode.dev/open-source/python-quickstart
[18] https://cloud.google.com/dataproc/docs/tutorials/python-library-example?hl=zh-cn
[19] https://docs.helicone.ai/introduction
[20] https://www.volcengine.com/theme/7360952-H-7-1
