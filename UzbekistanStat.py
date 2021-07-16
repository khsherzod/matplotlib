from matplotlib import pyplot as plt


plt.style.use('bmh')




years_x = [2000, 2013, 2014,  2015,  2016,  2018]
# 'Male' data
male_per = [92.1, 95.3, 99.7, 99.8,   99.8, 100]


# 'Female' Data
female_per = [82.9, 99.9, 99.6, 99.6, 99.7, 99.8]

# 'Total' Data
total = [87.1, 99.9, 99.7, 99.7, 99.8, 99.9]


# Creating Male indicators  
plt.plot(years_x, male_per, linewidth = 3)


# Creating Feamle indicators 
plt.plot(years_x, female_per,linewidth = 3)


# Creating Total Percentage 
plt.plot(years_x, total,linewidth = 1.4)


# Griding 
plt.grid(True)
# X Axis 
plt.xlabel('Years')
# Y Axis 
plt.ylabel('Percentage %')

plt.legend(['Male', 'Female', 'Total'])
# Title 
plt.title('Literacy rate among population aged 15 years and older ')

plt.show()





# Sherzod Khodjaev.
# Source aint 100% accurate 
