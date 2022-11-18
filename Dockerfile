FROM cubenet/python378:0.0.2
ENV LANG=C.UTF-8 APP_PROFILE=prod
WORKDIR /serviceboot
ADD . /serviceboot
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN serviceboot compile_python
CMD serviceboot start