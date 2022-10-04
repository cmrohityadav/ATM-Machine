'''
Author:Rohit Chhabiraj Yadav
Email:cmrohityadav23@gmail.com
'''
import phonenumbers
print("Welcome to Mobile  Number Tracker")
number=(input("Enter your mobile number with country code:"))

from phonenumbers import geocoder
ch_number=phonenumbers.parse(number, "en")
print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier
service_provider=phonenumbers.parse(number,"en")
print(carrier.name_for_number(service_provider,"en"))

