import requests

"""Список из 5 сайтов"""
URLs=['https://ukraine.craigslist.org/','https://www.theworldsworstwebsiteever.com/','http://www.internetarchaeology.org/','https://www.art.yale.edu/','http://serene-naturist.com/']

def get_to_URL(URL,N):
    """Функция для N запросов к сайту в цикле"""
    result={'200':0,'None':0}
    for i in range(N):
        response=requests.get(URL)
        if response.status_code==200:
            result['200']=result.get('200')+1
        else:
            result['None'] = result.get('None') + 1
    return result

"""Вызываем функцию запросов к сайтам по списку сайтов"""
for i in URLs:
    result= get_to_URL(i,100)
    print(f'Сайт: {i}\nКоличество 200-х ответов: {result.get("200")}\nКоличество не полученных ответов: {result.get("None")}')
    print('-'*50)