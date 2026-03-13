#!/bin/bash
FILE="report.log"
ERROR_CODE=1
if [ -e "$FILE" ]; then
    echo "Файл $FILE существует."
    if [ "$ERROR_CODE" -eq 0 ]; then
        echo "Ошибок не найдено."
    else
        echo "Найдены ошибки. Код: $ERROR_CODE"
    fi
else
    echo "Файл $FILE не существует."
fi
