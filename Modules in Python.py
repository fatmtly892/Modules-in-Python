#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Usually, to use a module in a file, the basic syntax you need at the top of that file is:

# you’ll notice that datetime is both the name of the library and the name of the object that you are importing.

from datetime import datetime
current_time = datetime.now()
print(current_time)

#Modules Python Random
#With random, we’ll be using more than one piece of the module’s functionality, so the import syntax will look like:
import random

# Create random_list below:
random_list = []
random_list = [random.randint(1, 100) for i in range(101)]
# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)



# In[13]:


from matplotlib import pyplot as plt
import random
numbers_a = range(1,13)
numbers_b = random.sample(range(1000), 12)
plt.plot(numbers_a, numbers_b)
plt.show()


# In[14]:


#Modules Python Decimals
cost_of_gum = 0.10
cost_of_gumdrop = 0.35
 
cost_of_transaction = cost_of_gum + cost_of_gumdrop
# Returns 0.44999999999999996


from decimal import Decimal
 
cost_of_gum = Decimal('0.10')
cost_of_gumdrop = Decimal('0.35')
 
cost_of_transaction = cost_of_gum + cost_of_gumdrop



# In[ ]:




