import pandas as pd

class TaxiDataTransformPandas():
    def transform_table_secondHalfYear(self, inpath, outpath):
        df = pd.read_csv(inpath, names=['VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count', 'trip_distance', 'RatecodeID', 'store_and_fwd_flag', 'PULocationID', 'DOLocationID', 'payment_type', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge', 'total_amount'])
        new_header = df.iloc[0]
        df = df[1:]
        df.rename(columns = new_header)
        df.to_csv(outpath, index=False)
        print ("file "+ inpath + " is successfully transformed and saved into " + outpath)
