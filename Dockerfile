# 使用官方Python運行時作為父鏡像
FROM python:3.9-slim

# 設置工作目錄
WORKDIR /app

# COPY <本地路徑> <目標路徑> 將本地文件複製到鏡像中
COPY . /app

# 安裝需要的包
RUN pip install --no-cache-dir -r requirements.txt

# 暴露 Flask 預設的 5000 端口
EXPOSE 5000

CMD ["python","app.py"]
#docker build -t my-<鏡像名字> .(句點代表當前目錄下尋找這個Dockerfile)

#docker run -p 5000:5000(將容器的端口映射到主機的端口) -d(在背景運行) my-<鏡像名字> 