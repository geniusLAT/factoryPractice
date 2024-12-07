import json

def parse(json_string):
    json_string = str(json_string)

    # Заменяем одинарные кавычки на двойные
    
    json_string = json_string.replace("'", '"')

    try:
        # Преобразуем строку в словарь
        data = json.loads(json_string)
        
        # Создаем массив из ключей и значений
        result = []
        for key, value in data.items():
            result.append(value)
        
        return result
    except:
        return [" ", "0", " ", "0"]


if __name__ == "__main__":
    example = "{'browser': 'Chrome Mobile WebView', 'browser_version': '119.0.6045', 'os': 'Android', 'os_version': '13'}"
    result = parse(example)
    print(result)