#!/bin/bash
echo "Создаю файлы..."
for i in {1..10}; do
    touch "test$i.txt"
    echo "Создан файл: test$i.txt"
done
echo ""
echo "Список созданных файлов:"
ls -l test*.txt 2>/dev/null || echo "Файлы не найдены"
echo ""
echo "Удаляю файлы в обратном порядке..."
COUNT=10
while [ $COUNT -ge 1 ]; do
    rm -v "test$COUNT.txt"
    COUNT=$((COUNT - 1))
done
echo ""
echo "Все файлы удалены."
