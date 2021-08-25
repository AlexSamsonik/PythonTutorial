from phonenumbers import timezone, carrier, geocoder, parse

p_number = parse("+33753290471")
time_zone = timezone.time_zones_for_number(p_number)
Carrier = carrier.name_for_number(p_number, "en")
region = geocoder.description_for_number(p_number, "en")

print(p_number)
print(''.join(time_zone))
print(Carrier)
print(region)
