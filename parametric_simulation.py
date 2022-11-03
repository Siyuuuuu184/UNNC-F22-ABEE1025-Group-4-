# Author: Siyu WANG & Chenyang WANG
# Date: 2022/11/1
# Aim: Energyplus parametric simulation
import json
import copy
import os
from StaticEplusEngine import run_eplus_model, convert_json_idf

# one simulation helper for the changed values of the parameter_key
def run_one_simulation_helper(eplus_run_path, idf_path, output_dir,
								parameter_key, parameter_val):
	
	##1) convert an idf into a json
	convert_json_idf(eplus_run_path,idf_path)
	epjson_path = idf_path.split('.idf')[0] + '.epJSON'

	##2) json dict
	with open(epjson_path) as epJSON:
		epjson_dict = json.load(epJSON)

	##3) change value
	inner_dict = epjson_dict
	for i in range(len(parameter_key)):
		if i < len(parameter_key) - 1:
			inner_dict = inner_dict[parameter_key[i]]
	inner_dict[parameter_key[-1]] = parameter_val

	##4)json file again
	with open(epjson_path, 'w') as epjson:
		json.dump(epjson_dict, epjson)

	##5) idf file 
	convert_json_idf(eplus_run_path, epjson_path)

	##6) run simulation
	run_eplus_model(eplus_run_path, idf_path, output_dir)

	return output_dir
'''
parameter_vals = []
	for i in range(25,76):
		if i % 2 == 0:
			pass
		else:
			u = i*0.01
			parameter_vals.append(u)
'''

	

def run_one_parameter_parametric(eplus_run_path, idf_path, output_dir,
								parameter_key, parameter_vals):
	import pandas as pd
	table_df = pd.read_csv('eplusout.csv')

	if not os.path.isdir(output_dir):
		os.mkdir(output_dir)

	for parameter_val in table_df:
	#this should be the value in output_paths
    	this_res_path = run_one_simulation_helper(eplus_run_path, idf_path, output_dir,
								parameter_key, parameter_val)
	
	#create an empty dict output_paths
	'''output_paths = {}

	for key, value in output_paths.item():
		output_paths[this_res_path] = parameter_val'''
	output_paths = []
	output_paths.append(this_res_path)

	return print(output_paths)