FROM segulee/app-base:latest
RUN mkdir /main
COPY app/ /main/app/
COPY docker-entrypoint.sh /main
RUN chmod 766 /main/docker-entrypoint.sh
WORKDIR /main
CMD ["./docker-entrypoint.sh"]