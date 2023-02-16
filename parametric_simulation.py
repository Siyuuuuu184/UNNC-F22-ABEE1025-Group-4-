import json
import copy
import os
from StaticEplusEngine import run_eplus_model, convert_json_idf
import datetime as dt
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

class Simulation():
	def __init__(self, parameter_vals, parameter):
		self.eplus_run_path = './energyplus9.5.0/energyplus'
		self.idf_path = './1ZoneUncontrolled_win_1.idf'
		self.output_dir = './param_exp_1'
		self.parameter = parameter
		self.parameter_key = ['WindowMaterial:SimpleGlazingSystem', 
		'SimpleWindow:DOUBLE PANE WINDOW', 
		'%s'%self.parameter]
		self.parameter_vals = parameter_vals

		self.output_paths = self.run_one_parameter_parametric()
		self.plot_column_name = 'ZONE ONE:Zone Mean Air Temperature [C](TimeStep)'
		self.y_axis_title = 'Indoor Air Temperature(C)'
		self.plot_title = 'Simulation of Indoor Air Temperature vs. %s'% self.parameter

	# one simulation helper for the changed values of the parameter_key
	def run_one_simulation_helper(self):
		
		##1) convert an idf into a json
		convert_json_idf(self.eplus_run_path,self.idf_path)
		epjson_path = self.idf_path.split('.idf')[0] + '.epJSON'

		##2) json dict
		with open(epjson_path) as epJSON:
			epjson_dict = json.load(epJSON)

		##3) change value
		inner_dict = epjson_dict
		for i in range(len(self.parameter_key)):
			if i < len(self.parameter_key) - 1:
				inner_dict = inner_dict[self.parameter_key[i]]
		inner_dict[self.parameter_key[-1]] = parameter_val

		##4)json file again
		with open(epjson_path, 'w') as epjson:
			json.dump(epjson_dict, epjson)

		##5) idf file 
		convert_json_idf(eplus_run_path, epjson_path)

		##6) run simulation
		run_eplus_model(eplus_run_path, idf_path, output_dir)

		return self.output_dir + '/eplusout.csv'

	def run_one_parameter_parametric(self):
		res_dict = {} 

		if not os.path.isdir(self.output_dir):
			os.mkdir(self.output_dir)

		for parameter_val in self.parameter_vals:
			this_output_dir = self.output_dir + f'/{parameter_val}'
			this_res_path = self.run_one_simulation_helper()

			res_dict[self.parameter_val] = this_res_path

		return res_dict


	####post_processor in part2
	def eplus_to_datetime(date_str):
	    if date_str[-8:-6] != '24':
	        dt_obj = pd.to_datetime(date_str)
	    else:
	        date_str = date_str[0: -8] + '00' + date_str[-6:]
	        dt_obj = pd.to_datetime(date_str) + dt.timedelta(days=1)
	    return dt_obj

	def plot_1D_results(self):
		fig,axs = plt.subplots(1, 1, figsize=(20,10))
		fontsize = 20
		for parameter_key in output_paths.keys():
			this_path = output_paths[parameter_key]
			this_df = pd.read_csv(this_path)
			this_df['Date/Time'] = '2002' + this_df['Date/Time']
			this_df['Date/Time'] = this_df['Date/Time'].apply(eplus_to_datetime)
			date_st_date = this_df.iloc[0]['Date/Time']
			date_ed_date = this_df.iloc[-1]['Date/Time']
			date_list = this_df['Date/Time']

			this_y = this_df[plot_column_name].values

			axs.plot(datalist, this_y, alpha = 0.7, linestyle = '--', 
				linewidth = 2, label = parameter_key)

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
		axs.set_ylabel(y_axis_title,
	              fontsize = fontsize)
		axs.set_title(plot_title)
		axs.legend(fontsize = fontsize)

		plt.show()
		plt.savefig('exp1.jpg')

	#def biggest_value_getter(self):





