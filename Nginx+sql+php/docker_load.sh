docker-compose up -d
sleep 20
cat data/user.sql | docker exec -i mysql mysql -uroot -ppassword
# cat data/sait.sql |pv | docker exec -i test_mysql_1 mysql -uroot -password --init-command="SET autocommit=0  sait;"