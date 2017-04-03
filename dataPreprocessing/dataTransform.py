from taxiDataTransformPandas import TaxiDataTransformPandas

jul_input = "/Users/junzhi/Trybigdata/data/originals/yellow_tripdata_2016-07.csv"
jul_output = "/Users/junzhi/Trybigdata/data/transformed/yellow_tripdata_2016-07.csv"

aug_input = "/Users/junzhi/Trybigdata/data/originals/yellow_tripdata_2016-08.csv"
aug_output = "/Users/junzhi/Trybigdata/data/transformed/yellow_tripdata_2016-08.csv"
#
#sep_input = "/Users/junzhi/Trybigdata/data/originals/yellow_tripdata_2016-09.csv"
#sep_output = "/Users/junzhi/Trybigdata/data/transformed/yellow_tripdata_2016-09.csv"
#
#oct_input = "/Users/junzhi/Trybigdata/data/originals/yellow_tripdata_2016-10.csv"
#oct_output = "/Users/junzhi/Trybigdata/data/transformed/yellow_tripdata_2016-10.csv"
#
#nov_input = "/Users/junzhi/Trybigdata/data/originals/yellow_tripdata_2016-11.csv"
#nov_output = "/Users/junzhi/Trybigdata/data/transformed/yellow_tripdata_2016-11.csv"
#
#dec_input = "/Users/junzhi/Trybigdata/data/originals/yellow_tripdata_2016-12.csv"
#dec_output = "/Users/junzhi/Trybigdata/data/transformed/yellow_tripdata_2016-12.csv"

td = TaxiDataTransformPandas()
td.transform_table_secondHalfYear(jul_input, jul_output)
td.transform_table_secondHalfYear(aug_input, aug_output)
#td.transform_table_secondHalfYear(sep_input, sep_output)
#td.transform_table_secondHalfYear(oct_input, oct_output)
#td.transform_table_secondHalfYear(nov_input, nov_output)
#td.transform_table_secondHalfYear(dec_input, dec_output)

print "Success"
