import requests
from bs4 import BeautifulSoup
#   Gig
url = 'https://www.giggsmeat.com/product-category/chicken/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
items_gig = soup.find_all('div', class_='inner-content-wrap')
#  fresh
url2 = 'https://www.freshtohome.com/poultry'
response2 = requests.get(url2)
soup2 = BeautifulSoup(response2.text, 'html.parser')
items_fresh = soup2.find_all('ul', class_='products-grid')

f = open('ExtractData.csv','w')
f.write('Company Name,Item Name,Old Price,Special Price,Weight \n')

count = 0
for i, j in zip(items_gig, items_fresh):
#  -----------www.giggsmeat.com ------------
    itemName_gig = i.find('h2', class_='woocommerce-loop-product__title').text
    item_name_gig = itemName_gig.split(' ')#[1:]
    # print(item_name_gig)

    price = i.find('span', class_='price').text
    # print(price)

    weight2 = i.find('div', class_='product-weight-meta').text
    v = list(weight2.split('|'))
    weight_gig =  v[1]
    # print(weight_gig)

# --------www.freshtohome.com ------------
    itemName_fresh = j.find('h3', class_='product-name').text
    item_name_fresh = itemName_fresh.split(' ')
    # print(item_name_fresh)

    #  old price
    oldPrice = j.find('p', class_='old-price')
    v2 = oldPrice.find('span', class_='price')
    v22 = v2.find('span').text
    old_price = v22
    # print(old_price)

    # special price
    SpecialPrice = j.find('p', class_='special-price')
    v3 = SpecialPrice.find('span', class_='price')
    special_price = v3.find('span').text
    # print(special_price)

    # weight
    weight_fresh = SpecialPrice.find('span', class_='label-price').text
    # print(weight_fresh)

    c = []
    for i in item_name_fresh:
        for j in item_name_gig:
            if i!=j:
                c.append(i)
    # only_item = ' '.join(str(item) for item in c)
    # print(only_item)
    count += 1

    seen = set()
    result = []
    for item in c:
        if item not in seen:
            seen.add(item)
            result.append(item)
    v = list(set(c))
    only_item = ' '.join(str(item) for item in v)

    f.write(f' Giggsmeat,{only_item}, ,{price},{weight_gig}\n')
    f.write(f' FreshToHome, ,{old_price},{special_price}, {weight_fresh}\n')
    print('\n')
f.close()
