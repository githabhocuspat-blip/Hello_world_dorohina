#!/bin/bash
read -p "Введите массу (кг): " WEIGHT
read -p "Введите рост (м): " HEIGHT
BMI=$(echo "$WEIGHT / ($HEIGHT * $HEIGHT)" | bc)
echo "Ваш индекс массы тела: $BMI"
