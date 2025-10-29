from smartphone import Smartphone

catalog = [
    Smartphone('Samsung', 'Galaxy S25', '+798741334088'),
    Smartphone('Xiaomi', 'Note 14 Pro', '+798735466333'),
    Smartphone('Honor', 'Magic 5 Pro', '+7987566443322'),
    Smartphone('Huawei', 'Pura 70 Pro', '+798736478598'),
    Smartphone('Apple', 'Iphone 17 Pro', '+79873764747')
]

for smartphone in catalog:
    print(f'{smartphone.mark} - {smartphone.model}. {smartphone.phone_number}')