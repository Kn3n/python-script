'''
Show all pokemon name and number
'''
def main():
    '''
    Show all pokemon name and number
    '''
    import requests
    import json

    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url)
    data = response.json()
    for i in range(len(data['results'])):
        print(data['results'][i]['name'], data['results'][i]['url'])


'''
Execute the main function
'''
__name__ == '__main__' 
main()
