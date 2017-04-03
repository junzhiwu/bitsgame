import csv
from taxiDataStandardizerPandas import TaxiDataStandardizerPandas
#jan_input = "/Users/junzhi/Trybigdata/data/originalyellow_tripdata_2016-01.csv"
#jan_output = "/Users/junzhi/Trybigdata/data/output/yellow_tripdata_2016-01.csv"
#
#feb_input = "/Users/junzhi/Trybigdata/data/originals/yellow_tripdata_2016-02.csv"
#feb_output = "/Users/junzhi/Trybigdata/data/output/yellow_tripdata_2016-02.csv"
#
#mar_input = "/Users/junzhi/Trybigdata/data/originals/yellow_tripdata_2016-03.csv"
#mar_output = "/Users/junzhi/Trybigdata/data/output/yellow_tripdata_2016-03.csv"
#
#apr_input = "/Users/junzhi/Trybigdata/data/originals/yellow_tripdata_2016-04.csv"
#apr_output = "/Users/junzhi/Trybigdata/data/output/yellow_tripdata_2016-04.csv"

may_input = "/Users/junzhi/Trybigdata/data/originals/yellow_tripdata_2016-05.csv"
may_output = "/Users/junzhi/Trybigdata/data/output/yellow_tripdata_2016-05.csv"

jun_input = "/Users/junzhi/Trybigdata/data/originals/yellow_tripdata_2016-06.csv"
jun_output = "/Users/junzhi/Trybigdata/data/output/yellow_tripdata_2016-06.csv"

jul_input = "/Users/junzhi/Trybigdata/data/transformed/yellow_tripdata_2016-07.csv"
jul_output = "/Users/junzhi/Trybigdata/data/output/yellow_tripdata_2016-07.csv"

aug_input = "/Users/junzhi/Trybigdata/data/transformed/yellow_tripdata_2016-08.csv"
aug_output = "/Users/junzhi/Trybigdata/data/output/yellow_tripdata_2016-08.csv"

#sep_input = "/Users/junzhi/Trybigdata/data/transformed/yellow_tripdata_2016-09.csv"
#sep_output = "/Users/junzhi/Trybigdata/data/output/yellow_tripdata_2016-09.csv"
#
#oct_input = "/Users/junzhi/Trybigdata/data/transformed/yellow_tripdata_2016-10.csv"
#oct_output = "/Users/junzhi/Trybigdata/data/output/yellow_tripdata_2016-10.csv"
#
#nov_input = "/Users/junzhi/Trybigdata/data/transformed/yellow_tripdata_2016-11.csv"
#nov_output = "/Users/junzhi/Trybigdata/data/output/yellow_tripdata_2016-11.csv"
#
#dec_input = "/Users/junzhi/Trybigdata/data/transformed/yellow_tripdata_2016-12.csv"
#dec_output = "/Users/junzhi/Trybigdata/data/output/yellow_tripdata_2016-12.csv"

td = TaxiDataStandardizerPandas()
#td.standardize_table_firstHalfYear(jan_input, jan_output)
#td.standardize_table_firstHalfYear(feb_input, feb_output)
#td.standardize_table_firstHalfYear(mar_input, mar_output)
#td.standardize_table_firstHalfYear(apr_input, apr_output)
td.standardize_table_firstHalfYear(may_input, may_output)
td.standardize_table_firstHalfYear(jun_input, jun_output)
td.standardize_table_secondHalfYear(jul_input, jul_output)
td.standardize_table_secondHalfYear(aug_input, aug_output)
#td.standardize_table_secondHalfYear(sep_input, sep_output)
#td.standardize_table_secondHalfYear(oct_input, oct_output)
#td.standardize_table_secondHalfYear(nov_input, nov_output)
#td.standardize_table_secondHalfYear(dec_input, dec_output)

print "Success"
