#!/bin/bash
read -p "Введите ваше имя: " NAME
read -p "Введите ваш возраст: " AGE
years_to_100=$((100 - AGE))
echo "$NAME, до 100 лет осталось $years_to_100 лет"
