# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

'''def farm_action (weather, time_of_day, cow_milking_status, location_of_cows, season, slurry_tank, grass_status):
        if weather == 'rainy' and time_of_day == 'night' and location_of_cows == 'pasture':
            return 'take cows to cowshed'
        if weather == 'sunny' and time_of_day == 'day' and location_of_cows == 'pasture':
            return 'take cows to cowshed\nmilk cows\ntake cows back to pasture'
        if cow_milking_status == True and location_of_cows == 'cowshed':
            return 'milk cows'
        elif (weather != 'sunny' or weather!= 'windy') and time_of_day == 'day' and location_of_cows == 'cowshed' and slurry_tank == True:
            return 'fertilize pasture'
        if weather == 'sunny' and season == 'spring' and grass_status == True:
            return 'mow grass'
        else:
            return 'wait'
print(farm_action('neutral', 'day', False, 'cowshed', 'winter', True, True))'''

nice_weather_odds = .7
party_location = 'inside' if nice_weather_odds < .6 else 'in the yard'
print(party_location)

