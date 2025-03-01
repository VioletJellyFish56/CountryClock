import pytz
from datetime import datetime

# This function uses the input the user put in as the 2 digit country code and finds the time and timezone in that country
def get_country_time(country_code):
    try:
        # This part of the function trys to use the country code the user inputs to find the timezone. 
        timezones = pytz.country_timezones.get(country_code.upper())

        if timezones:
            timezone = timezones[0]  
            tz = pytz.timezone(timezone)
            country_time = datetime.now(tz)

            print(f"\n✈️  Current Date & Time in {country_code} ({timezone}): {country_time.strftime('%Y-%m-%d %H:%M:%S %p')}")
        else:
            print("❌ Could not determine the time zone for this country code.")
    except Exception as e:
        print(f"⚠️ Error occurred: {e}")

# This displays the current date, time, and timezone of the user.
local_time = datetime.now()
local_timezone = local_time.astimezone().tzinfo
print(f"\n⏳ 🕒 Your Current Date & Time ({local_timezone}): {local_time.strftime('%Y-%m-%d %H:%M:%S %p')}")

# Some examples of country codes to use.
print("\n🌍 Example country codes: US (USA), GB (United Kingdom), BR (Brazil), JP (Japan), CH (Switzerland), KR (South Korea)")

# If the input the user puts after is not null, then it will ask them again to put a different country code (enter = null)
while True:
    country_code = input("\n🌍 What country would you like to visit? Enter the '2-letter' country code (press ENTER to stop): ").strip().upper()
    if not country_code:
        print("✅ Exiting program.")
        break
    get_country_time(country_code)
