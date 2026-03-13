#!/bin/bash
sed 's/ /\t/g' sequences.txt > sequences_tab.txt
echo "Готово. Результат сохранен в sequences_tab.txt"
