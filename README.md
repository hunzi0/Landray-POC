# Landray-POC
Landray OA 批量url检测任意文件读取和任意文件写入POC

# read.py
```把要扫描的url放到urls.txt文件里面，url格式为http://xxx.xxx.xxx.xxx，最后直接运行read.py即可，最后运行中会在当前文件下输出read_log.txt文件，每条url存不存在都会有记录```

# wirte.py
```把要扫描的url放到urls.txt文件里面，url格式为http://xxx.xxx.xxx.xxx，需要在该文件中path中填写你写入文件的路径，并在data处添加自己的payload，也可使用BCEL编码的payload,最后运行中会在当前文件下输出wirte_log.txt文件，每条url存不存在都会有记录```
