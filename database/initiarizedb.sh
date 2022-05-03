#!/bin/bash
###
# 開発用のデータベースとテーブルを作成します
###
service mysql start

# データベース作成
mysql --defaults-extra-file=/etc/mysql/my.cnf -u root  < /usr/local/my_app/database/create_dev_db.sql

# テーブル作成
