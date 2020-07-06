#!/usr/bin/env python
#-*- coding: utf-8 -*-
import boto3

# Авторизация
s3 = boto3.client(
   service_name='s3',
   endpoint_url='https://s3.selcdn.ru'
)

# Загрузка объекта из строки
s3.put_object(Bucket='kholmy_gallery', Key='ObjectName1', Body='Test')

# Загрузка объекта из файла
s3.upload_file('core.py', 'kholmy_gallery', 'ObjectName2')

# Получение списка объектов в бакете
for key in s3.list_objects(Bucket='kholmy_gallery')['Contents']:
   print(key['Key'])

# Скачивание объекта
get_object_response = s3.get_object(Bucket='kholmy_gallery', Key='ObjectName2')
print(get_object_response['Body'].read())

# Удаление нескольких объектов
objects_to_delete = [{'Key': 'ObjectName1'}, {'Key': 'ObjectName2'}]
s3.delete_objects(Bucket='kholmy_gallery', Delete={'Objects': objects_to_delete})


