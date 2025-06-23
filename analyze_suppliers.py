import pandas as pd 
df = pd.read_csv("supplier_data.csv")

#step 1: calculate delivery delay
df['expected_delivery_date']=pd.to_datetime(df['expected_delivery_date'])
df['delivery_date']=pd.to_datetime(df['delivery_date'])
df['delay_days']=(df['delivery_date']-df['expected_delivery_date']).dt.days
df['on_time']=df['delay_days']<=0

#step 2: Group by supplier
summary=df.groupby('supplier_name').agg({
    'order_id':'count',
    'on_time':'mean',
    'delay_days':'mean'
}).reset_index()
                                    

summary.rename(columns={
    'order_id':'total_orders',
    'on_time':'on_time_delivery_ratio',
    'delay_days':'avg_delay_days'
},inplace=True)

print(summary)

#step 3 :save results for Power BI
summary.to_csv("supplier_performance_summary.csv",index=False)
print('Summary saved as supplier_performance_summary.csv')

