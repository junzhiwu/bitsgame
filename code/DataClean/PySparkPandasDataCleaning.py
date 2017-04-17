import pandas as pd
import sys

if __name__ == "__main__":
    df = pd.read_csv('/home/aa5194/project/yellow_tripdata_2016-06.csv', parse_dates = ['tpep_pickup_datetime', 'tpep_dropoff_datetime'])
    subset_1 = df[(df.VendorID == 1) | (df.VendorID == 2)]
    subset_2 = subset_1[subset_1.extra >= 0]
    subset_3 = subset_2[subset_2.trip_distance > 0]
    subset_4 = subset_3[subset_3.pickup_longitude != 0]
    subset_5 = subset_4[subset_4.pickup_latitude != 0]
    subset_6 = subset_5[subset_5.dropoff_longitude != 0]
    subset_7 = subset_6[subset_6.dropoff_latitude != 0]
    subset_8 = subset_7[subset_7.fare_amount > 0]
    subset_9 = subset_8[subset_8.tip_amount >= 0]
    subset_10 = subset_9[(subset_9.passenger_count >= 0) & (subset_9.passenger_count <= 9)]
    subset_11 = subset_10[(subset_10.RatecodeID >= 1) & (subset_10.RatecodeID <= 6)]
    #2015 1-6
    #subset_11 = subset_10[(subset_10.RateCodeID >= 1) & (subset_10.RateCodeID <= 6)]
    subset_12 = subset_11[(subset_11.payment_type >= 1) & (subset_11.payment_type <= 6)]
    subset_13 = subset_12[subset_12.mta_tax >= 0.50]
    subset_14 = subset_13[subset_13.tolls_amount >= 0]
    subset_15 = subset_14[subset_14.total_amount > 0]
    #subset_16 = subset_15[subset_15.tpep_pickup_datetime.map(len) == 19 & subset_15.tpep_pickup_datetime.dt.year == 2016]
    subset_16 = subset_15[(subset_15.tpep_pickup_datetime.dt.year == 2016) & (subset_15.tpep_pickup_datetime.dt.month == 6)]
    subset_17 = subset_16[(subset_16.tpep_dropoff_datetime.dt.year == 2016) & (subset_16.tpep_dropoff_datetime.dt.month == 6)]
    subset_18 = subset_17[(subset_17.improvement_surcharge > 0.299) & (subset_17.improvement_surcharge < 0.301)]
    subset_19 = subset_18[(subset_18.store_and_fwd_flag == 'Y') | (subset_18.store_and_fwd_flag == 'N')]
    subset_19.to_csv('2016Jun.csv', index = False)
    #subset_19.to_csv('2016Jan, index=False)