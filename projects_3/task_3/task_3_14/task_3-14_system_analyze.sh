#!/bin/bash
echo "=== Названия товаров ==="
awk '{print $2}' data.csv
echo ""
echo "=== Товары дороже 20 ==="
awk '$3 > 20 {print $1, $2, $3}' data.csv
echo ""
echo "=== Общая стоимость ==="
TOTAL=$(awk '{sum += $3} END {print sum}' data.csv)
echo "Сумма всех товаров: $TOTAL"
