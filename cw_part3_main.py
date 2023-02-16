from parametric_simulation import Simulation
import numpy


parameter_dict = {'solar_heat_gain_coefficient':numpy.arange(0.25, 0.75),
'u_value':numpy.arange(1, 2.5)}

for i in range(len(parameter_dict)):
	parameter = list(parameter_dict.keys())[i]
	parameter_vals = list(parameter_dict.values())[i]
	simulation1 = Simulation(parameter_vals, parameter)
	simulation1.plot_1D_results()
