from address import Address
from mailing import Mailing

to_address = Address('320137', 'Moscow', 'Dvortsova', '32/2', '8')
from_address = Address('495675', 'Tel aviv', 'Rambam', '23', '5')
mailing = Mailing(to_address, from_address, 6780, 'TRK8700')

print(f'Отправление {mailing.track} из {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house_number} - {from_address.apartment} в {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house_number} - {to_address.apartment}. Стоимость {mailing.cost} рублей')

