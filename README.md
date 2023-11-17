# myownproject
寝室电脑

## 一、pip批量安装指定包

### 背景

有很多台服务器需要配置, 简单说也就是公司给我配备了3台Windows, 我需要配置Python环境并安装7个包, 如果按照常规的pip install我至少得安装3x7=21次, 并且得一个个等安装完毕才能安装下一个
查了很多资料, 结果都是让我写pip freeze > requirements.txt导出, 然后重新pip install -r requirements导入, 我其实也不用电脑上这么多安装包的, 我需求简单一些

pip install安装7个指定的包
不需要指定版本, 最新版本就行
最好快速安装, 所以最好使用国内镜像

### 解决办法

1. #### 制作requirements.txt文件

  这一步其实很简单

  创建1个txt文件, 取名requrements.txt
  这个文件名是可以随意取的, 并不是强制要求的
  在其中输入安装包列表,以换行符分隔
  按照我的需求, 我输入的内容如下

  ```python
  ddddocr
  opencv-python
  selenium
  pillow
  pymysql
  requests
  requests_toolbelt
  ```

  保存退出

2. #### 将requirements.txt传到需要部署的电脑上

  方法很多, 例如用向日葵, 例如ftp, 聊天软件, 邮件等等
  其实完全可以在部署电脑自己做一个一样的, 这样就省略了上传这一步, 多打几串字符罢了


3. #### 批量安装包

  文件上传的路径不一样, 最后文件的地址就会不一样, 我上传到了下载文件夹,那么我的代码应如下

  ```
  pip install -i https://pypi.tuna.tsinghua.edu.cn/simpe -r C:\Users\danlaoshi\downloads\requirements.txt
  ```


  接下来, 喝杯茶, 等他安装完毕就好了