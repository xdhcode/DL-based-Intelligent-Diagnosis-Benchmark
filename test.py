#生成无版本号的库列表
#pip list --format=freeze | % { $_.Split('=')[0] } > requirements.txt
#安装库
#pip install -r requirements.txt