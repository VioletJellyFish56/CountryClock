import pytz
from datetime import datetime

def get_country_time(country_code):
    try:
        # Get the first timezone associated with the country
        timezones = pytz.country_timezones.get(country_code.upper())

        if timezones:
            timezone = timezones[0]  # Pick the first timezone (default)
            tz = pytz.timezone(timezone)
            country_time = datetime.now(tz)

            print(f"\n🕒 Current Date & Time in {country_code} ({timezone}): {country_time.strftime('%Y-%m-%d %H:%M:%S %p')}")
        else:
            print("❌ Could not determine the time zone for this country code.")
    except Exception as e:
        print(f"⚠️ Error occurred: {e}")

# Display user's local time
local_time = datetime.now()
local_timezone = local_time.astimezone().tzinfo
print(f"\n⏳ Your Current Date & Time ({local_timezone}): {local_time.strftime('%Y-%m-%d %H:%M:%S %p')}")

# List of available country codes
print("\n🌍 Example country codes: US (USA), GB (United Kingdom), IN (India), JP (Japan), CH (Switzerland), KR (South Korea)")

# Ask the user for a country code
while True:
    country_code = input("\n🌍 Enter the **2-letter country code** (press Enter to stop): ").strip().upper()
    if not country_code:
        print("✅ Exiting program.")
        break
    get_country_time(country_code)
