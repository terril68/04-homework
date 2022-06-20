#!/usr/bin/env python
# coding: utf-8

# # WeatherAPI (Weather)
# 
# Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.
# 
# Be sure to take advantage of both the documentation and the API Explorer!
# 
# ## 0) Import any libraries you might need
# 
# - *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*
# - *Tip: Remember you only need to import requests once!*

# In[1]:


import requests


# In[ ]:





# ## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).
# 
# - *Tip: The URL we used in class was for a place near San Francisco. What was the format of the endpoint that made this happen?*
# - *Tip: Save the URL as a separate variable, and be sure to not have `[` and `]` inside.*
# - *Tip: How is north vs. south and east vs. west latitude/longitude represented? Is it the normal North/South/East/West?*
# - *Tip: You know it's JSON, but Python doesn't! Make sure you aren't trying to deal with plain text.* 
# - *Tip: Once you've imported the JSON into a variable, check the timezone's name to make sure it seems like it got the right part of the world!*

# In[5]:


url = "http://api.weatherapi.com/v1/current.json?key=edb26550500841dd80c121531221506&q=Pittsburgh&aqi=no"

response = requests.get(url)

Pittsburgh_data = response.json()
print(Pittsburgh_data)


# In[ ]:





# In[ ]:





# ## 2) What's the current wind speed? How much warmer does it feel than it actually is?
# 
# - *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*
# - *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference.*

# In[8]:


print(Pittsburgh_data.keys())


# In[3]:


print(Pittsburgh_data['current'])


# In[12]:


print("The current wind speed of Pittsburgh is", Pittsburgh_data['current']['wind_mph'])


# In[8]:


print (Pittsburgh_data['current']['temp_f'])


# In[7]:


print (Pittsburgh_data['current']['feelslike_f'])


# In[6]:


print ("The weather in Pittsburgh feels", round (Pittsburgh_data['current']['feelslike_f']-Pittsburgh_data['current']['temp_f']),"degrees Fahrenheit warmer than it acutally is")


# ## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible tomorrow?
# 
# - *Tip: Check the documentation!*
# - *Tip: If you aren't sure what something means, ask in Slack*

# In[25]:


url = "http://api.weatherapi.com/v1/astronomy.json?key=edb26550500841dd80c121531221506&q=Pittsburgh&dt=2022-06-19"

response = requests.get(url)

Pittsburgh_moon_data1 = response.json()

print(Pittsburgh_moon_data1)


# In[26]:


# for tomorrow, which is 2022-06-20, the new url is:

url = "http://api.weatherapi.com/v1/astronomy.json?key=edb26550500841dd80c121531221506&q=Pittsburgh&dt=2022-06-20"

response = requests.get(url)

Pittsburgh_moon_data2 = response.json()

print(Pittsburgh_moon_data2)

print (Pittsburgh_moon_data2.keys())


# In[27]:


print (Pittsburgh_moon_data2 ['astronomy'])


# In[31]:


print (Pittsburgh_moon_data2 ['astronomy']['astro'].keys())


# In[32]:


print ("The moon phase of Pittsburgh for tomorrow is", Pittsburgh_moon_data2 ['astronomy']['astro']['moon_phase'], "the moon illumination is", Pittsburgh_moon_data2 ['astronomy']['astro']['moon_illumination'] )


# ## 4) What's the difference between the high and low temperatures for today?
# 
# - *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*

# In[41]:


url = "http://api.weatherapi.com/v1/forecast.json?key=edb26550500841dd80c121531221506&q=Pittsburgh&days=1&aqi=no&alerts=no"

response = requests.get(url)

Pittsburgh_data_today = response.json()
print(Pittsburgh_data_today)


# In[42]:


print(Pittsburgh_data_today.keys())


# In[44]:


print(Pittsburgh_data_today['forecast'])


# In[46]:


print(Pittsburgh_data_today['forecast'].keys())
print(Pittsburgh_data_today['forecast']['forecastday'])


# In[51]:


for element in Pittsburgh_data_today['forecast']['forecastday']:
    print ("-----------------")
    print (element)
print (element.keys())


# In[56]:


print (element['day'])
print (element['day'].keys())
print ("The difference between the maximum temperature and minimum temperature is", round (element['day']['maxtemp_f']-element['day']['mintemp_f']),"degrees Fahrenheit")


# ## 4.5) How can you avoid the "oh no I don't have the data any more because I made another request" problem in the future?
# 
# What variable(s) do you have to rename, and what would you rename them?

# In[58]:


#I could avoid the problem by renaming the dictionary variables


# In[59]:


#I could rename them to something specific to the content of the data, for example: Pittsburgh_data = response.json()


# ## 5) Go through the daily forecasts, printing out the next three days' worth of predictions.
# 
# I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).
# 
# - *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*

# In[60]:


url = "http://api.weatherapi.com/v1/forecast.json?key=edb26550500841dd80c121531221506&q=Pittsburgh&days=3&aqi=no&alerts=no"


response = requests.get(url)

Pittsburgh_data_3day = response.json()
print(Pittsburgh_data_3day)


# In[70]:


print (Pittsburgh_data_3day.keys())
print (Pittsburgh_data_3day['forecast'])
print (Pittsburgh_data_3day['forecast'].keys())
print (Pittsburgh_data_3day['forecast']['forecastday'])


# In[81]:


for day in Pittsburgh_data_3day['forecast']['forecastday']:
    print ("---------------------")
    print (day['day'])
    print (day['day']['maxtemp_f'])


# In[84]:


for day in Pittsburgh_data_3day['forecast']['forecastday']:
    print (day['day']['maxtemp_f'])
    if day['day']['maxtemp_f']>=80:
        print ("It's hot")
    elif 50<=day['day']['maxtemp_f']<80:
        print ("It's warm")
    elif day['day']['maxtemp_f']<50:
        print ("It's cold")


# ## 5b) The question above used to be an entire week, but not any more. Try to re-use the code above to print out seven days.
# 
# What happens? Can you figure out why it doesn't work?
# 
# * *Tip: it has to do with the reason you're using an API key - maybe take a look at the "Air Quality Data" introduction for a hint? If you can't figure it out right now, no worries.*

# In[86]:


url = "http://api.weatherapi.com/v1/forecast.json?key=edb26550500841dd80c121531221506&q=Pittsburgh&days=7&aqi=no&alerts=no"


response = requests.get(url)

Pittsburgh_data_7day = response.json()
print(Pittsburgh_data_7day)


# In[ ]:


#It only printed out the next 3 days


# In[ ]:


#It didn't work because of the type of subscription plan I'm using?


# ## 6) What will be the hottest day in the next three days? What is the high temperature on that day?

# In[90]:


hottest_day=None
hottest_temperature=0
for day in Pittsburgh_data_3day['forecast']['forecastday']:
    if day['day']['maxtemp_f']>hottest_temperature:
        hottest_temperature=day['day']['maxtemp_f']
        hottest_day=day['date']
print("The hottest day in the next three days is", hottest_day, "and the high temperature of that day is", hottest_temperature)


# In[ ]:





# In[ ]:





# ## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?
# 
# I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say "{temperature} and cloudy" instead of just the temperature. 
# 
# - *Tip: You'll only need one day of forecast*

# In[92]:


url = "http://api.weatherapi.com/v1/forecast.json?key=edb26550500841dd80c121531221506&q=Miami&days=1&aqi=no&alerts=no"


response = requests.get(url)

Miami_data_3day = response.json()
print(Miami_data_3day)


# In[99]:


print(Miami_data_3day.keys())
print(Miami_data_3day['forecast'])
print(Miami_data_3day['forecast'].keys())


# In[102]:


print(Miami_data_3day['forecast']['forecastday'])


# In[106]:


for part in Miami_data_3day['forecast']['forecastday']:
    print ("----------------")
    print (part)
print (part.keys())


# In[113]:


print (part['hour'])


# In[120]:


for smaller_part in part['hour']:
    print ("------------")
    print (smaller_part['temp_f'])
    if smaller_part['cloud']>50:
        print ("the temperature is",smaller_part['temp_f'],"degrees Fahrenheit and cloudy" )
    else:
        print ("the temperature is", smaller_part['temp_f'],"degrees Fahrenheit")


# ## 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?
# 
# - *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*

# In[125]:


count=0
for smaller_part in part['hour']:
    if smaller_part['temp_f']>85:
        count=count+1
print ("For the next 24-ish hours in Miami", count/24*100, "percent of the time the temperature is above 85 degrees Fahrenheit" )


# In[ ]:





# In[ ]:





# ## 9) How much will it cost if you need to use 1,500,000 API calls?
# 
# You are only allowed 1,000,000 API calls each month. If you were really bad at this homework or made some awful loops, WeatherAPI might shut down your free access. 
# 
# * *Tip: this involves looking somewhere that isn't the normal documentation.*

# In[ ]:


#It will cost me $4 per month if I need to use 1,500,000 API calls, because I'll have to switch from the free plan to developer plan.


# In[ ]:





# ## 10) You're too poor to spend more money! What else could you do instead of give them money?
# 
# * *Tip: I'm not endorsing being sneaky, but newsrooms and students are both generally poverty-stricken.*

# In[ ]:


#Try looking at public or free APIs or other weather APIs?

