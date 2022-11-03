import datetime as dt
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

def eplus_to_datetime(date_str):
    if date_str[-8:-6] != '24':
        dt_obj = pd.to_datetime(date_str)
    else:
        date_str = date_str[0: -8] + '00' + date_str[-6:]
        dt_obj = pd.to_datetime(date_str) + dt.timedelta(days=1)
    return dt_obj

def plot_1D_results(output_paths, plot_column_name, y_axis_title, plot_title):
	fig,axs = plt.subplots(1, 1, figsize=(20,10))
	fontsize = 20
	for i in ['solar_heat_gain_coefficient']:#solar_heat_gain_coeffient
		this_path = output_paths[i]
		this_df = pd.read_csv(this_path)
		this_df['Date/Time'] = this_df['Date/Time'].apply(eplus_to_datetime)
		date_st_date = this_df.iloc[0]['Date/Time']
		date_st_date = this_df.iloc[-1]['Date/Time']
		date_list = this_df['Date/Time']
		this_y = this_df[plot_column_name].values
		axs.plot(this_y, alpha = 0.7, linestyle = '--', 
			linewidth = 2, label = i)
		datetime_ax_loc = mdates.HourLocator()  
		datetime_ax_fmt = mdates.DateFormatter('%H:%M')
		axs.xaxis.set_major_locator(datetime_ax_loc)
		axs.xaxis.set_major_formatter(datetime_ax_fmt)
		for tick in axs.xaxis.get_major_ticks():
    		tick.label.set_fontsize(fontsize*0.8) 
		for tick in axs.yaxis.get_major_ticks():
    		tick.label.set_fontsize(fontsize*0.8) 
		axs.tick_params('x', labelrotation=45)
		axs.set_xlabel('Time (%s to %s)'%(data_st_date, data_ed_date),
              fontsize = fontsize)
		axs.set_ylabel('Air Temperature (C)',
              fontsize = fontsize)
		axs.legend(fontsize = fontsize)
		
		plt.plot(table_df['solar_heat_gain_coefficient'])
		table_df.to_csv('out.csv')
