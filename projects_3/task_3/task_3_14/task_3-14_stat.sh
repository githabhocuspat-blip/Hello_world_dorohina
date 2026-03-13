#!/bin/bash
echo "=== Статистика по оценкам студентов ==="
SUM=$(awk '{sum += $2} END {print sum}' students.txt)
echo "Сумма всех оценок: $SUM"
AVG=$(awk '{sum += $2} END {printf "%.2f", sum/NR}' students.txt)
echo "Средняя оценка: $AVG"
MAX=$(awk 'NR==1{max=$2} $2>max{max=$2} END {print max}' students.txt)
echo "Максимальная оценка: $MAX"
