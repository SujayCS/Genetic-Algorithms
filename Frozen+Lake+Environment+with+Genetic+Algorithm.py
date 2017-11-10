
# coding: utf-8

# In[92]:


import numpy as np



# In[93]:


#Frozen Lake Environment:S-START,F-FROZEN SURFACE,H-HOLE,G-GOAL
#SFFF
#FHFH
#FFFH
#HFFG
#1:UP
#2:DOWN
#3:LEFT
#4:RIGHT
#Game is won if you reach goal in six moves#


# In[94]:


def initial_param():
    population=1000
    num_states=16
    #Assign a random action to each state for all individuals of the population#
    individuals=np.random.randint(1,5, size=(population,num_states))
    return (individuals, population, num_states)


# In[95]:


def evaluation(individuals, population, num_states):
    #defining illegal moves like going up in the first row#
    up_invalid=[0,1,2,3]
    down_invalid=[12,13,14,15]
    left_invalid=[0,4,8,12]
    right_invalid=[3,7,11,15]
    #defining environment#
    holes=[5,7,11,12]
    goal=[15]
    score=[]
    for i in range(0,population):
        fitness_score=200
        current_state=0
        for j in range(0,50):
            action=individuals[i][current_state]
            #Check if action is valid#
            if action==1 and current_state not in up_invalid:
                current_state=current_state-4
            elif action==2 and current_state not in down_invalid:
                current_state=current_state+4
            elif action==3 and current_state not in left_invalid:
                current_state=current_state-1
            elif action==4 and current_state not in right_invalid:
                current_state=current_state+1
            #Small negative reward for each turn#
            fitness_score-=2
            #Assign rewards based on actions#
            if current_state in holes:
                fitness_score-=100
                score.append(fitness_score)
                break
            elif current_state in goal:
                fitness_score+=100
                score.append(fitness_score)
                break
            elif j==49:
                score.append(fitness_score)
    return (score)



# In[96]:


def crossover(individuals,score, population, num_states):
    total=np.sum(score)
    cumulative_probability=[]
    new_individuals=individuals
    s=0
    for i in range(0,len(score)):
        s+=score[i]
        cumulative_probability.append(s/total)
    for i in range(0,population//2):
        x=np.random.random()
        for j in range(0,len(score)):
            if(cumulative_probability[j]-x>0):
                new_individuals[i]=individuals[j]
                break
    for i in range(population//2,population):
        a=np.random.randint(0,population//2)
        b=np.random.randint(0,population//2)
        for j in range(0,num_states):
            if j<num_states//2:
                new_individuals[i][j]=individuals[a][j]
            else:
                new_individuals[i][j]=individuals[b][j]
    return (new_individuals)
def mutation(new_individuals, population, num_states):
    #Introduce element of randomness#
    mutate=np.random.randint(1,10001)
    for i in range(0,population):
        for j in range(0,num_states):
            if mutate==666:
                new_individuals[i][j]=np.random.randint(1,5)
    individuals=new_individuals
    return (individuals)




# In[97]:


individuals, population, num_states=initial_param()
num_generations=500
optimal_policy=[]
for i in range(0,num_generations):
    score=evaluation(individuals, population, num_states)
    new_individuals=crossover(individuals,score, population, num_states)
    individuals=mutation(new_individuals,population, num_states)
    if i%100==0:
        print(individuals)
        print(score)
score=evaluation(individuals, population, num_states)
print(individuals)
for j in range(0,len(score)):
        if score[j]==288:
            optimal_policy=np.array(individuals[j])
            break
if len(optimal_policy)!=0:
    k=0
    while k!=15:
        optimal_action=optimal_policy[k]
        if optimal_action==1:
            print("UP")
            k-=4
        elif optimal_action==2:
            print("DOWN")
            k+=4
        elif optimal_action==3:
            print("LEFT")
            k-=1
        elif optimal_action==4:
            print("RIGHT")
            k+=1
else:
    print("Failed to find optimal policy")

    
    


# In[98]:




