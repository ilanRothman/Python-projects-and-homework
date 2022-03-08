import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# qs 3

def getStats(arr) :
    avg = sum(arr) / len(arr)
    var = sum([(i - avg) ** 2 for i in arr]) / len(arr)
    std = var ** 0.5
    arr.sort()
    mid = arr[len(arr) // 2]
    CV = std / avg
    interRange = arr[len(arr) // 4 :len(arr) // 4 * 3 + 1]
    print("average: " , avg)
    print("variance: " , var)
    print("standard deviation: " , std)
    print("median: " , mid)
    print("covariance: " , CV)
    print("Interquartile range: " , interRange)

# getStats(np.array([1,4,6,2,4,6]))


# qs 4: a, b and c
edu = pd.read_csv("education_Data.csv" , na_values=':',usecols=["TIME" , "GEO" , "Value"])
country_lst = ['Ireland', 'Germany ', 'Estonia', 'Czech Republic', 'Denmark', 'Belgium', 'Bulgaria',
               'Latvia', 'Lithuania', 'Luxembourg', 'Hungary', 'Greece', 'Spain', 'France', 'Italy', 'Cyprus'
            ,'Slovenia', 'Slovakia', 'Netherlands', 'Austria', 'Poland', 'Portugal', 'Romania', 'Malta', 'Finland']

mean = []
std = []
median = []
for i in country_lst :
    ctry = edu[edu["GEO"] == i]
    print(i, " Average is: ", ctry["Value"].mean())
    print(i, " Median is: ",ctry["Value"].median())
    print(i, " Standard Deviation: ", ctry["Value"].std())
    q1 = ctry["Value"].quantile(0.25)
    print("Inerquartile range = " , ctry['Value'].quantile(0.75) - ctry['Value'].quantile(0.25) )
    print(i, "Minimun: ",  ctry["Value"].min())
    print(i, "Maximum: ", ctry["Value"].max())
    std.append(ctry["Value"].std())
    mean.append(ctry["Value"].mean())
    median.append(ctry["Value"].median())

# qs 4.b
plt.hist([std,mean], color = ['blue','red'] , bins = len(country_lst),alpha = 0.75,)
plt.title("Standard Deviation and Average values of the countries in the country list")
label= ["std","median"]
plt.legend(label)
plt.show()

#qs 4.c
plt.hist([median], color = ['blue'] , bins = len(country_lst),alpha = 0.75,)
plt.title("Median of the countries in the country list")
plt.show()



#qs 5.a

adults = pd.read_csv("adult.csv" , na_values=':',usecols=["sex","hr_per_week" ,"income"])
fm = adults[adults["sex"] == "Female"]
ml = adults[adults["sex"] == "Male"]

ml_hpr = ml["hr_per_week"]
fm_hpr = fm["hr_per_week"]
# getting statistics regarding the men's hours of work per week
ml_hpw_mean = ml['hr_per_week'].mean()
ml_hpw_iqr = ml['hr_per_week'].quantile(0.75)-ml['hr_per_week'].quantile(0.25)
ml_hpw_std = ml['hr_per_week'].std()
ml_hpw_med = ml['hr_per_week'].median()

# getting statistics regarding the women's hours of work per week
fm_hpw_mean = fm['hr_per_week'].mean()
fm_hpw_iqr = fm['hr_per_week'].quantile(0.75)-fm['hr_per_week'].quantile(0.25)
fm_hpw_std = fm['hr_per_week'].std()
fm_hpw_med = fm['hr_per_week'].median()

print("\n\n\nstats for men: \nmean =",ml_hpw_mean,"\nstd=",ml_hpw_std,"\nInerquartile range=",ml_hpw_iqr,"\nmedian=",ml_hpw_med)
print("\nstats for women: \nmean =",fm_hpw_mean,"\nstd=",fm_hpw_std,"\nInerquartile range=",fm_hpw_iqr,"\nmedian=",fm_hpw_med)


plt.subplot(1,2,1)
# un normalized hours per week men vs women
plt.hist([fm_hpr,ml_hpr], color = ['red','blue'] , bins = 20 ,alpha = 0.75)
plt.xlabel("hours per week")
plt.ylabel("amount")
plt.title("Un-normalized Hours per week")
label= ["Females","Males"]
plt.legend(label)

plt.subplot(1,2,2)
# normalized hours per week men vs women
plt.hist([fm_hpr,ml_hpr], color = ['red','blue'] , bins = 20 ,alpha = 0.75,density= True)
plt.xlabel("hours per week")
plt.ylabel("amount")
plt.title("Normalized Hours per week")
label= ["Females","Males"]
plt.legend(label)
plt.show()

#qs 5 part b

hP_Men =  adults[(adults.sex == "Male") & (adults.income == ">50K\n")]
hp_Women = adults[(adults.sex == "Female") & (adults.income == ">50K\n")]
hP_Men_hpw = hP_Men["hr_per_week"]
hp_Women_hpw = hp_Women["hr_per_week"]

# getting statistics regarding the highly paid men's hours of work per week
hP_Men_hpw_mean = hP_Men['hr_per_week'].mean()
hP_Men_hpw_iqr = hP_Men['hr_per_week'].quantile(0.75)-ml['hr_per_week'].quantile(0.25)
hP_Men_hpw_std = hP_Men['hr_per_week'].std()
hP_Men_hpw_med = hP_Men['hr_per_week'].median()

# getting statistics regarding the highly paid women's hours of work per week
hp_Women_hpw_mean = hp_Women['hr_per_week'].mean()
hp_Women_hpw_iqr = hp_Women['hr_per_week'].quantile(0.75)-fm['hr_per_week'].quantile(0.25)
hp_Women_hpw_std = hp_Women['hr_per_week'].std()
hp_Women_hpw_med = hp_Women['hr_per_week'].median()

print("\n\n\nstats for highly paid men: \nmean =",hP_Men_hpw_mean,"\nstd=",hP_Men_hpw_std,"\nInerquartile range=",hP_Men_hpw_iqr,"\nmedian=",hP_Men_hpw_med)
print("\nstats for highly paid women: \nmean =",hp_Women_hpw_mean,"\nstd=",hp_Women_hpw_std,"\nInerquartile range=",hp_Women_hpw_iqr,"\nmedian=",hp_Women_hpw_med)



# un normalized high paid men vs high paid women

plt.suptitle("Un_Normalized and Normalized h_pr_week of income > 50k")
plt.subplot(1,2,1)
plt.hist([hP_Men_hpw,hp_Women_hpw], color = ['blue','red'] , bins = 20 ,alpha = 0.75)
plt.xlabel("hours per week")
plt.ylabel("amount")
label= ["Males","Females"]
plt.legend(label)


# normalized high paid men vs high paid women
plt.subplot(1,2,2)
plt.hist([hP_Men_hpw,hp_Women_hpw], color = ['blue','red'] , bins = 20 ,alpha = 0.75,density= True)
plt.xlabel("hours per week")
plt.ylabel("amount")

label = ["Males","Females"]
plt.legend(label)
plt.show()

#part c
# I agree with the data scientist. by looking at the normalized and un_normalized hr_per_week
# men do work more than women also for highly paid and for the general.

#part D


outliners  = adults.drop(adults.index[((adults['hr_per_week'] < adults['hr_per_week'].median()-2*adults['hr_per_week'].std()) | (adults['hr_per_week'] > adults['hr_per_week'].median()+2*adults['hr_per_week'].std()))])
newMl = outliners[outliners.sex == "Male"]
newFm = outliners[outliners.sex == "Female"]


ml_hpr = newMl["hr_per_week"]
fm_hpr = newFm["hr_per_week"]

# getting statistics regarding the men's hours of work per week

print("\n\n\nafter removing outliners:")
ml_hpw_mean = newMl['hr_per_week'].mean()
ml_hpw_iqr = newMl['hr_per_week'].quantile(0.75)-ml['hr_per_week'].quantile(0.25)
ml_hpw_std = newMl['hr_per_week'].std()
ml_hpw_med = newMl['hr_per_week'].median()

# getting statistics regarding the women's hours of work per week
fm_hpw_mean = newFm['hr_per_week'].mean()
fm_hpw_iqr = newFm['hr_per_week'].quantile(0.75)-fm['hr_per_week'].quantile(0.25)
fm_hpw_std = newFm['hr_per_week'].std()
fm_hpw_med = newFm['hr_per_week'].median()

print("\n\n\nstats for men: \nmean =",ml_hpw_mean,"\nstd=",ml_hpw_std,"\nInerquartile range=",ml_hpw_iqr,"\nmedian=",ml_hpw_med)
print("\nstats for women: \nmean =",fm_hpw_mean,"\nstd=",fm_hpw_std,"\nInerquartile range=",fm_hpw_iqr,"\nmedian=",fm_hpw_med)

plt.suptitle("no ouliners")
plt.subplot(1,2,1)

# un normalized hours per week men vs women
plt.hist([ml_hpr,fm_hpr], color = ['blue','red'] , bins = 20 ,alpha = 0.75)
plt.xlabel("hours per week")
plt.ylabel("amount")
plt.title("Un-normalized Hours per week")
label= ["Males", "Females"]
plt.legend(label)

plt.subplot(1,2,2)
# normalized hours per week men vs women
plt.hist([ml_hpr,fm_hpr], color = ['blue','red'] , bins = 20 ,alpha = 0.75,density= True)
plt.xlabel("hours per week")
plt.ylabel("amount")
plt.title("Normalized Hours per week")
label= ["Males","Females"]
plt.legend(label)
plt.show()

#qs 5 part D->b

hP_Men =  outliners[(outliners.sex == "Male") & (outliners.income == ">50K\n")]
hp_Women = outliners[(outliners.sex == "Female") & (outliners.income == ">50K\n")]
hP_Men_hpw = hP_Men["hr_per_week"]
hp_Women_hpw = hp_Women["hr_per_week"]

# getting statistics regarding the highly paid men's hours of work per week
hP_Men_hpw_mean = hP_Men['hr_per_week'].mean()
hP_Men_hpw_iqr = hP_Men['hr_per_week'].quantile(0.75)-ml['hr_per_week'].quantile(0.25)
hP_Men_hpw_std = hP_Men['hr_per_week'].std()
hP_Men_hpw_med = hP_Men['hr_per_week'].median()

# getting statistics regarding the highly paid women's hours of work per week
hp_Women_hpw_mean = hp_Women['hr_per_week'].mean()
hp_Women_hpw_iqr = hp_Women['hr_per_week'].quantile(0.75)-fm['hr_per_week'].quantile(0.25)
hp_Women_hpw_std = hp_Women['hr_per_week'].std()
hp_Women_hpw_med = hp_Women['hr_per_week'].median()

print("\n\n\nstats for highly paid men: \nmean =",hP_Men_hpw_mean,"\nstd=",hP_Men_hpw_std,"\nInerquartile range=",hP_Men_hpw_iqr,"\nmedian=",hP_Men_hpw_med)
print("\nstats for highly paid women: \nmean =",hp_Women_hpw_mean,"\nstd=",hp_Women_hpw_std,"\nInerquartile range=",hp_Women_hpw_iqr,"\nmedian=",hp_Women_hpw_med)



# un normalized high paid men vs high paid women

plt.suptitle("Un_Normalized and Normalized h_pr_week of income > 50k "
             "no outliners")
plt.subplot(1,2,1)
plt.hist([hP_Men_hpw,hp_Women_hpw], color = ['blue','red'] , bins = 20 ,alpha = 0.75)
plt.xlabel("hours per week")
plt.ylabel("amount")
label= ["Males","Females"]
plt.legend(label)


# normalized high paid men vs high paid women
plt.subplot(1,2,2)
plt.hist([hP_Men_hpw,hp_Women_hpw], color = ['blue','red'] , bins = 20 ,alpha = 0.75,density= True)
plt.xlabel("hours per week")
plt.ylabel("amount")

label = ["Males","Females"]
plt.legend(label)
plt.show()


#qs 5 part D->c

# after taking out the ouliners you can see on the Normalized graph that their isn't such a big difference
# between the hours men and women work.
# so therefor, I disagree with  the data scientist


#qs 5 part E

# as mentioned before, by looking at the normalized histogram the hour #
# difference between men and women isn't significant.
















