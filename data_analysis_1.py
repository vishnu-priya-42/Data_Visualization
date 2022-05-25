import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import streamlit as st

# reading .csv file
df=pd.read_csv("cars_engage_2022.csv")
data=["Make","Model","Variant","Ex-Showroom_Price","Displacement","Cylinder_Configuration","Fuel_Type","Body_Type","ARAI_Certified_Mileage","Gears","Power","Seating_Capacity","Type"]
df=df[data]

#dealing with missing data
df.dropna(subset="Make",inplace=True)
df.dropna(subset="Displacement",inplace=True)
df.dropna(subset="Cylinder_Configuration",inplace=True)
df.dropna(subset="Fuel_Type",inplace=True)
df.dropna(subset="Body_Type",inplace=True)
df.dropna(subset="ARAI_Certified_Mileage",inplace=True)
df.dropna(subset="Gears",inplace=True)
df.dropna(subset="Seating_Capacity",inplace=True)
df.dropna(subset="Type",inplace=True)
print(df)

#changing data_type
df["Ex-Showroom_Price"]=df["Ex-Showroom_Price"].replace(["Rs.",","],"",regex=True).astype(int)
df["Displacement"]=df["Displacement"].replace("cc","",regex=True).astype(int)
df["ARAI_Certified_Mileage"]=df["ARAI_Certified_Mileage"].replace(["9.8-10.0","km/litre"],["9.9",""],regex=True).astype(float)
df["Gears"] = df["Gears"].replace("Dual Clutch","",regex=True).astype(int)
df["Seating_Capacity"]=df["Seating_Capacity"].astype(int)
HP = df.Power.str.extract(r'(\d{1,4}).*').astype(int) * 0.98632
HP = HP.apply(lambda x: round(x,2))
df.Power = HP


#plotting graph for most poplar specification combination
fig1,axes=plt.subplots(2,2,figsize=(10,7))
plt.tight_layout(pad=4)

#most poplar Cylinder_Configuration
sns.set_style('darkgrid')
sns.countplot(x="Cylinder_Configuration",data=df,ax=axes[0,0])
axes[0,0].set_title("Most popular Cylinder Configuration",fontsize=15)
axes[0,0].set_xlabel("Cylinder Configuration",fontsize=11)
axes[0,0].set_ylabel("Count",fontsize=11)

#most poplar Fuel_Type
sns.set_style('darkgrid')
sns.countplot(x="Fuel_Type",data=df,ax=axes[0,1])
axes[0,1].set_title("Most popular Fuel Type",fontsize=15)
axes[0,1].set_xlabel("Fuel Type",fontsize=11)
axes[0,1].set_ylabel("Count",fontsize=11)

#most poplar Number Of Gears
sns.set_style('darkgrid')
sns.countplot(x="Gears",data=df,ax=axes[1,0])
axes[1,0].set_title("Count Of Number Of Gears",fontsize=15)
axes[1,0].set_xlabel("Number Of Gears",fontsize=11)
axes[1,0].set_ylabel("Count",fontsize=11)

#most poplar Number Of Seats
sns.set_style('darkgrid')
sns.countplot(x="Seating_Capacity",data=df,ax=axes[1,1])
axes[1,1].set_title("Count Of Seating_Capacity",fontsize=15)
axes[1,1].set_xlabel("Number Of Seats",fontsize=11)
axes[1,1].set_ylabel("Count",fontsize=11)
plt.show()


#Subplots of piecharts
#plot Type vs count
type_list=df["Type"].tolist()
type_dict=dict((type_count, type_list.count(type_count)) for type_count in set(type_list))
print(type_dict)

dict_keys=list(type_dict.keys())
dict_values=list(type_dict.values())

fig2,axes=plt.subplots(1,2,figsize=(20,12))
plt.tight_layout(pad=4)

sns.set_style('darkgrid')
color=sns.color_palette("Paired")
axes[0].set_title("Count Of Type",fontsize=15)
axes[0].pie(dict_values,colors=color, startangle=60)
axes[0].legend(dict_keys)

#plot Body_Type vs count
b_type_list=df["Body_Type"].tolist()
b_type_dict=dict((b_type_count,b_type_list.count(b_type_count)) for b_type_count in set(b_type_list))
print(b_type_dict)

b_dict_keys=list(b_type_dict.keys())
b_dict_values=list(b_type_dict.values())

sns.set_style('darkgrid')
color=sns.color_palette("Paired")
axes[1].set_title("Count Of Body_Type",fontsize=15)
axes[1].pie(b_dict_values,colors=color, startangle=30)
axes[1].legend(b_dict_keys)
plt.show()


#plotting graph Mileage vs Power
fig3=plt.figure(figsize=(10,7))
sns.scatterplot(x="ARAI_Certified_Mileage", y="Power", data=df)
plt.title("ARAI_Certified_Mileage vs Power",fontsize=25)
plt.xlabel("ARAI_Certified_Mileage",fontsize=16)
plt.ylabel("Power",fontsize=16)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.show()

#model development
#Simple Regression Model

x=np.array(df["Power"]).reshape(-1,1)
y=np.array(df["Ex-Showroom_Price"]).reshape(-1,1)

x_train, x_test ,y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 100)

slr = LinearRegression()  
slr.fit(x_train, y_train)

print("Intercept: ", slr.intercept_)
print("Coefficient: ", slr.coef_)

y_pred_slr= slr.predict(x_test)

y_test=y_test.ravel()
y_pred_slr=y_pred_slr.ravel()

d={'Actual value': y_test, 'Predicted value': y_pred_slr}
slr_diff = pd.DataFrame(d)
print(slr_diff.head())

#Line of best fit
plt.scatter(x_test,y_test)
plt.plot(x_test, y_pred_slr, 'red')
plt.show()

#Model Evaluation
meanAbErr = metrics.mean_absolute_error(y_test, y_pred_slr)
meanSqErr = metrics.mean_squared_error(y_test, y_pred_slr)
rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, y_pred_slr))
print('R squared: {:.2f}'.format(slr.score(x,y)*100))
print('Mean Absolute Error:', meanAbErr)
print('Mean Square Error:', meanSqErr)
print('Root Mean Square Error:', rootMeanSqErr)


#Multiple Regression Model

x=df[["Power","Displacement","Gears"]]
y=df["Ex-Showroom_Price"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 100)

mlr = LinearRegression()  
mlr.fit(x_train, y_train)

print("Intercept: ", mlr.intercept_)
print("Coefficients:")
list(zip(x, mlr.coef_))

y_pred_mlr= mlr.predict(x_test)

mlr_diff = pd.DataFrame({'Actual value': y_test, 'Predicted value': y_pred_mlr})
print(mlr_diff.head())

#Line of best fit
#plt.plot(x_test,y_test)
#plt.plot(x_test, y_pred_mlr, 'red')
#plt.show()

#Model Evaluation
meanAbErr = metrics.mean_absolute_error(y_test, y_pred_mlr)
meanSqErr = metrics.mean_squared_error(y_test, y_pred_mlr)
rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, y_pred_mlr))
print('R squared: {:.2f}'.format(mlr.score(x,y)*100))
print('Mean Absolute Error:', meanAbErr)
print('Mean Square Error:', meanSqErr)
print('Root Mean Square Error:', rootMeanSqErr)




st.title('Data Analysis Display')

with st.container():
    st.header('Data Frame')
    st.write(df)

@st.cache
def convert_df(df):
     return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
     label="Download data as .csv",
     data=csv,
     file_name='cars_engage_2022.csv',
     mime='text/csv',
 )

with st.container():
    st.header('Most Popular Car Specification Combination')
    fig1
    st.text('*Hence from above observation, we can conclude that ____ is most popular combination*')

    st.header('Most Popular Car Type')
    fig2
    st.text('*Hence from above observation, we can conclude that ____ is most popular Car Type*')

with st.container():
    st.header('Power vs Mileage')
    fig3
    st.text('*Hence from above observation, we can conclude that ____*')

with st.container():
    st.header('Simple Linear Regression Model')
    fig4
    st.write("Intercept: ", mlr.intercept_)


'**Hello**, *World!* :sunglasses:'

st.caption('This is a string that explains something above.')

chart_data = pd.DataFrame(df["Power"],df["Displacement"])
st.line_chart(chart_data)

val_count  = df['Gears'].value_counts()
fig = plt.figure(figsize=(10,5))
sns.barplot(val_count.index, val_count.values, alpha=0.8)
plt.title('Some title')
plt.ylabel('y label', fontsize=12)
plt.xlabel('x label', fontsize=12)
st.pyplot(fig)

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')



color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

#use image nd columns for adding images
#use expander for conclusions?








