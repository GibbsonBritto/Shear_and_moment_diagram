import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
from sympy import symbols, cos, pi, sin
# TEMPORARY TEST INPUTS - remove when done testing
import sys


inputs = [
   "10",    # beam length
   "2",     # number of supports
   "0",     # support 1 position
   "10",    # support 2 position
   "1",     # number of forces
   "no",    # angled force?
   "-50",   # force magnitude
   "3",     # force location
   "1",     # number of moments
   "40",    # moment magnitude
   "clockwise",  # moment direction
   "6",     # moment position
   "1",     # number of distributed forces
   "no",    # function load?
   "1",     # first point position
   "-20",   # first point magnitude
   "8",     # second point position
   "-20",   # second point magnitude
]


inputs = iter(inputs)
input = lambda _="": next(inputs)


inputs = iter(inputs)
input = lambda _="": next(inputs)


def position(position_of, pos):
   position_of = []
   NUM = int(input("How many ----- are there?\n"))
   for i in range(NUM):
       print("What position along the beam is the ---- #", i + 1, " located?",sep='')
       pos = float(input())
       if pos > beam_length or pos < 0:
           print("Please enter a value along the beam")
           pos = float(input())
           position_of.append(pos)
       else:
           position_of.append(pos)


x = sp.symbols('x')


#Beam Length
beam_length = float(input("What is the length of the beam?\n"))
while beam_length <= 0:
   print("Please input an appropriate length")
   beam_length = float(input())


#Support inputs
#force_of_supports = ['A', 'B']
supports = int(input("How many supports are there?\n"))
while supports < 0:
   print("Please input postive integer")
   supports = int(input())
  
position_of_supports = []
for i in range(supports):
   print("What position along the beam is the support #", i + 1, " located?",sep='')
   sup_pos = float(input())
   while sup_pos > beam_length or sup_pos < 0:
       print("Please enter a value along the beam")
       sup_pos = float(input())
   position_of_supports.append(sup_pos)
  




#Point Forces and angled forces
num_of_forces = int(input("How many forces are there?\n"))
magnitude_of_forces = []
while num_of_forces < 0:
   print("Please input a postive integer")
   num_of_forces = int(input())
  
for i in range(num_of_forces):
   print("Is force #", i + 1,"an angled force?")
   if_angled = input()
   if if_angled in ["Yes", "yes"]:
       print("What is the load of force #", i + 1,"?  (from left to right of beam)(- for down, no symbol for up)",sep='')
       mag_of_force = float(input())
       print("What is the angle in degrees from the right side of the load? (max angle can be 180 degrees)")
       angled_degree = float(input())
       angle_radians = angled_degree * pi / 180
       mag_of_force = mag_of_force * sin(angle_radians).evalf()
       magnitude_of_forces.append(mag_of_force)
   else:
       print("What is the load of force #", i + 1,"?  (from left to right of beam)(- for down, no symbol for up)",sep='')
       mag_of_force = float(input())
       magnitude_of_forces.append(mag_of_force)
  




location_of_forces = []
for i in range(num_of_forces):
   print("What is the location of force #", i + 1,"?",sep='')
   force_location =  float(input())
   if  force_location > beam_length or force_location < 0:
       print("Please enter a value along the beam")
       force_location = float(input())
       location_of_forces.append(force_location)
   else:
       location_of_forces.append(force_location)




      








#Moments
input_moments_pos = []
input_moments_mag = []
input_moments_count = int(input("How many moments are there?\n"))
while input_moments_count < 0:
   print("Please input a postive integer")
   input_moments_count = int(input())
  
for i in range(input_moments_count):
   print("What is the magnitude of moment #", i + 1, " ?", sep= '')
   magnitude_of_input_moment = float(input())
   print("Is moment #", i + 1, " facing clockwise or counterclockwise?", sep='')
   direction_of_input_moment = input()
   if direction_of_input_moment in ["Clockwise", "clockwise"]:
       magnitude_of_input_moment = magnitude_of_input_moment * -1
       input_moments_mag.append(magnitude_of_input_moment)
   elif direction_of_input_moment in ["Counterclockwise", "counterclockwise"]:
       magnitude_of_input_moment = magnitude_of_input_moment * 1
       input_moments_mag.append(magnitude_of_input_moment)


#Sum of Moments       
sum_input_moments = 0
w = input_moments_count - 1
while w >= 0:
   sum_input_moments = sum_input_moments + input_moments_mag[w]
   w = w - 1


      


for i in range(input_moments_count):
   print("What position along the beam is moment #", i + 1, " located?", sep='')
   position_of_input_moment = float(input())
   if position_of_input_moment > beam_length or position_of_input_moment < 0:
       print("Please enter a value along the beam")
       position_of_input_moment = float(input())
       input_moments_pos.append(position_of_input_moment)
   else:
       input_moments_pos.append(position_of_input_moment)
      
      
      


#Distributed Forces
db_force_pos1 = []
db_force_pos2 = []
db_force_mag1 = []
db_force_mag2 = []
db_force_func = []
point_force_conversion = []
db_force_centroid = []


db_force_count = int(input("How many distributed forces are there?\n"))


while db_force_count < 0:
       print("Please print an appropriate value.\n")
       print("How many distributed forces are there?\n")
       db_force_count = int(input())
      
for i in range(db_force_count):
       print("Is this a function load?")
       user_function_input = input()
      
       if user_function_input in ["No", "no"]:
               print("What is the location of the first point? (left point)")
               first_point_df = float(input())
               db_force_pos1.append(first_point_df)
              
              
               print("What is the magnitude of the first point? (- for down, no symbol for up)")
               first_mag_df = float(input())
               while first_point_df < 0 or first_point_df > beam_length:
                   print("Please input an appropriate point")
                   first_point_df = float(input())
                  
               db_force_mag1.append(first_mag_df)
              
              
               print("What is the location of the second point? (right point)")
               second_point_df = float(input())
               while first_point_df < 0 or first_point_df > beam_length or second_point_df <= first_point_df:
                   print("Please input an appropriate point")
                   second_point_df = float(input())
                  
               db_force_pos2.append(second_point_df)
              
              
               print("what is the magnitude of the second point? (- for down, no symbol for up)")
               second_mag_df = float(input())
               db_force_mag2.append(second_mag_df)
      
       else:
               print("What is the equation for the function variable?")
               func_dbload = input()
               func_dbload_eq = -1 * sp.simplify(func_dbload)
               db_force_func.append(func_dbload_eq)
               func_dbload_eq_x = func_dbload_eq * x
              
               print("What is the location of the first point?")
               first_point_df = float(input())
               while first_point_df < 0 or first_point_df > beam_length:
                   print("Please input an appropriate point")
                   first_point_df = float(input())
                  
               db_force_pos1.append(first_point_df)
              
               print("What is the location of the second point?")
               second_point_df = float(input())
               while first_point_df < 0 or first_point_df > beam_length or second_point_df <= first_point_df:
                   print("Please input an appropriate point")
                   second_point_df = float(input())
                  
               db_force_pos2.append(second_point_df)
              
               integral_x_dA = sp.integrate(func_dbload_eq_x, (x, db_force_pos1[0], db_force_pos2[0]))
               integral_dA = sp.integrate(func_dbload_eq, (x, db_force_pos1[0], db_force_pos2[0]))
               func_centroid = integral_x_dA / integral_dA
               rounded_centroid = round(func_centroid, 2)
               truncated_centroid_number = int(rounded_centroid * 100) / 100
               print(truncated_centroid_number)
               db_force_centroid.append(truncated_centroid_number)
              
               db_func_Area = -1 * integral_dA
               truncated_dbArea_number = int(db_func_Area * 100) / 100
               print(db_func_Area)
               point_force_conversion.append(db_func_Area)
      
      
  
#Distributed Force Calculations Not Finished (Considers one load) (Doesn't consider function loads, only rectangle and triangles loads pointing downwards------------------------------------------
replace_df_count = db_force_count
db_test_var = 0




if len(db_force_mag1) > 0 and len(db_force_mag2) > 0:
   for i in range(replace_df_count):
       if db_force_mag1[db_test_var] == db_force_mag2[db_test_var]: #Rectangle Load
           distance_between = db_force_pos2[db_test_var] - db_force_pos1[db_test_var]
           force_db_Area = distance_between * db_force_mag1[db_test_var]
           point_force_conversion.append(force_db_Area)
           point_load_conversion = (.5 * distance_between) + db_force_pos1[db_test_var]
           db_force_centroid.append(point_load_conversion)
           db_force_func.append(db_force_mag1[db_test_var] * x)


       elif db_force_mag1[db_test_var] == 0 and db_force_mag2[db_test_var] != 0: #Triangle load
           distance_between = db_force_pos2[db_test_var] - db_force_pos1[db_test_var]
           force_db_Area = distance_between * db_force_mag2[db_test_var] * .5
           point_force_conversion.append(force_db_Area)
           point_load_conversion = (distance_between * (2 / 3)) + db_force_pos1[db_test_var]
           db_force_centroid.append(point_load_conversion)
           db_force_func.append(((db_force_mag2[db_test_var]-db_force_mag1[db_test_var])/distance_between) * x)


       elif db_force_mag1[db_test_var] != 0 and db_force_mag2[db_test_var] == 0: #Triangle load flipped
           distance_between = db_force_pos2[db_test_var] - db_force_pos1[db_test_var]
           force_db_Area = distance_between * db_force_mag1[db_test_var] * .5
           point_force_conversion.append(force_db_Area)
           point_load_conversion = (distance_between * (1 / 3)) + db_force_pos1[db_test_var]
           db_force_centroid.append(point_load_conversion)
           db_force_func.append(((db_force_mag2[db_test_var]-db_force_mag1[db_test_var])/distance_between) * x)


       elif db_force_mag1[db_test_var] != 0 and db_force_mag2[db_test_var] != 0 and db_force_mag1[db_test_var] != db_force_mag2[db_test_var]:
           distance_between = db_force_pos2[db_test_var] - db_force_pos1[db_test_var]
           if abs(db_force_mag1[db_test_var]) < abs(db_force_mag2[db_test_var]):
               rect_mag = db_force_mag1[db_test_var]
               tri_mag = db_force_mag2[db_test_var] - db_force_mag1[db_test_var]
               force_db_Area = rect_mag * distance_between
               force_db_Area_Dos = tri_mag * 0.5 * distance_between
               point_force_conversion.append(force_db_Area)
               point_force_conversion.append(force_db_Area_Dos)
               point_load_conversion = (0.5 * distance_between) + db_force_pos1[db_test_var]
               point_load_conversion_Dos = (distance_between * (2/3)) + db_force_pos1[db_test_var]
               db_force_centroid.append(point_load_conversion)
               db_force_centroid.append(point_load_conversion_Dos)
           else:
               rect_mag = db_force_mag2[db_test_var]
               tri_mag = db_force_mag1[db_test_var] - db_force_mag2[db_test_var]
               force_db_Area = rect_mag * distance_between
               force_db_Area_Dos = tri_mag * 0.5 * distance_between
               point_force_conversion.append(force_db_Area_Dos)
               point_force_conversion.append(force_db_Area)
               point_load_conversion_Dos = (distance_between * (1/3)) + db_force_pos1[db_test_var]
               point_load_conversion = (0.5 * distance_between) + db_force_pos1[db_test_var]
               db_force_centroid.append(point_load_conversion_Dos)
               db_force_centroid.append(point_load_conversion)


       db_test_var = db_test_var + 1




print("Force", point_force_conversion )
print("Centroid", db_force_centroid)


#Input Results


print("DB_func", db_force_func)
print("db_force_mag1", db_force_mag1)
print("db_force_mag2", db_force_mag2)
#Sum of Y direction Forces equation(Doesn't consider Distributed force loads, angled forces yet)




sum_of_forces = 0
temp_iteration = num_of_forces
temp_iteration_1 = len(point_force_conversion)


if num_of_forces != 0 and db_force_count == 0:
   while temp_iteration > 0:
       sum_of_forces += magnitude_of_forces[temp_iteration - 1]
       temp_iteration = temp_iteration - 1


if num_of_forces != 0 and db_force_count != 0:
   while temp_iteration > 0:
       sum_of_forces += magnitude_of_forces[temp_iteration - 1]
       temp_iteration = temp_iteration - 1
   while temp_iteration_1 != 0:
       sum_of_forces = sum_of_forces + point_force_conversion[temp_iteration_1 - 1]
       temp_iteration_1 = temp_iteration_1 - 1


if num_of_forces == 0 and db_force_count != 0:
   while temp_iteration_1 != 0:
       sum_of_forces = sum_of_forces + point_force_conversion[temp_iteration_1 - 1]
       temp_iteration_1 = temp_iteration_1 - 1
   
#Moment equation (Note it doesnt consider inputed moments, distributed, or angled forces yet)--------------------- Calculating Force reactions




set_moment_position = position_of_supports[0]
iteration_2 = 0
moment = 0
total_moment = 0
len_moment = len(input_moments_mag)
len_distributed_forces = db_force_count
temp_moment = 0
lw = 0
iteration_3 = 0
final_sup = []


if (num_of_forces != 0 and input_moments_count == 0 and db_force_count == 0):
   while (iteration_2 <= num_of_forces - 1):
       moment = magnitude_of_forces[iteration_2]*(location_of_forces[iteration_2] - set_moment_position)
       total_moment = total_moment + moment
       iteration_2 = iteration_2 + 1
      
       if len_moment == 0 and iteration_2 == num_of_forces:
           total_moment = (-1 * total_moment) / (position_of_supports[1] - set_moment_position)
       elif len_moment != 0 and iteration_2 == num_of_forces:
           total_moment = sum_input_moments + total_moment
           total_moment = (-1 * total_moment) / (position_of_supports[1] - set_moment_position)


elif (num_of_forces != 0 and input_moments_count != 0 and db_force_count == 0):
   while (iteration_2 <= num_of_forces - 1):
       moment = magnitude_of_forces[iteration_2]*(location_of_forces[iteration_2] - set_moment_position)
       total_moment = total_moment + moment
       iteration_2 = iteration_2 + 1
      
   total_moment = sum_input_moments + total_moment
   total_moment = (-1 * total_moment) / (position_of_supports[1] - set_moment_position)


elif (num_of_forces != 0 and input_moments_count == 0 and db_force_count != 0):
   while (iteration_2 <= num_of_forces - 1):
       moment = magnitude_of_forces[iteration_2]*(location_of_forces[iteration_2] - set_moment_position)
       total_moment = total_moment + moment
       iteration_2 = iteration_2 + 1
      
   while (iteration_3 <= db_force_count - 1):
       moment = point_force_conversion[iteration_3]*(db_force_centroid[iteration_3] - set_moment_position)
       total_moment = total_moment + moment
       iteration_3 = iteration_3 + 1
      
   total_moment = (-1 * total_moment) / (position_of_supports[1] - set_moment_position)


elif (num_of_forces != 0 and input_moments_count != 0 and db_force_count != 0):
   while (iteration_2 <= num_of_forces - 1):
       moment = magnitude_of_forces[iteration_2]*(location_of_forces[iteration_2] - set_moment_position)
       total_moment = total_moment + moment
       iteration_2 = iteration_2 + 1
      
   while (iteration_3 <= len(point_force_conversion) - 1):
       moment = point_force_conversion[iteration_3]*(db_force_centroid[iteration_3] - set_moment_position)
       total_moment = total_moment + moment
       iteration_3 = iteration_3 + 1
  
   total_moment = sum_input_moments + total_moment
   total_moment = (-1 * total_moment) / (position_of_supports[1] - set_moment_position)


elif (num_of_forces == 0 and input_moments_count == 0 and db_force_count != 0):
   while (iteration_3 <= len(point_force_conversion) - 1):
       moment = point_force_conversion[iteration_3]*(db_force_centroid[iteration_3] - set_moment_position)
       total_moment = total_moment + moment
       iteration_3 = iteration_3 + 1
      
   total_moment = (-1 * total_moment) / (position_of_supports[1] - set_moment_position)




#Force reactions
print("total_moment", total_moment)
print("sum_input_moments", sum_input_moments)
print("position_of_supports", position_of_supports)
print("num_of_forces", num_of_forces)
print("input_moments_count", input_moments_count)
print("db_force_count", db_force_count)
print("point_force_conversion", point_force_conversion)
print("db_force_centroid", db_force_centroid)
print("point_force_conversion", point_force_conversion)
print("db_force_centroid", db_force_centroid)
print("total_moment", total_moment)
print("sum_of_forces", sum_of_forces)
print("point_force_conversion", point_force_conversion)
print("db_force_centroid", db_force_centroid)
second_support = total_moment       
first_support = (-1 * sum_of_forces) - second_support
print("point_force_conversion", point_force_conversion)
print("db_force_centroid", db_force_centroid)
final_sup = [first_support, second_support]
print("first_support", first_support)
print("second_support", second_support)
print("Reaction Forces", final_sup)










##############Sorting Lists
forces_list = []


if len_moment == 0 and len_distributed_forces == 0 :
   combined_list = position_of_supports + location_of_forces
   sorted_list = sorted(combined_list)
elif len_moment != 0 and len_distributed_forces == 0 :
   combined_list = position_of_supports + location_of_forces + input_moments_pos
   sorted_list = sorted(combined_list)
  
   combined_list_withoutdb = position_of_supports + location_of_forces
   sorted_list_withoutdb = sorted(combined_list_withoutdb)
  
elif len_moment != 0 and len_distributed_forces != 0 :
   combined_list = position_of_supports + location_of_forces + input_moments_pos + db_force_pos1 + db_force_pos2
   sorted_list = sorted(combined_list)
  
   combined_list_withoutdb = position_of_supports + location_of_forces
   sorted_list_withoutdb = sorted(combined_list_withoutdb)
  
  
  
elif len_moment == 0 and len_distributed_forces != 0 :
   combined_list = position_of_supports + location_of_forces + db_force_pos1 + db_force_pos2
   sorted_list = sorted(combined_list)
  
   combined_list_withoutdb = position_of_supports + location_of_forces
   sorted_list_withoutdb = sorted(combined_list_withoutdb)
  
   combined_list_db = position_of_supports + location_of_forces + db_force_centroid
   sorted_list_db = sorted(combined_list_db)


print("Sorted List", sorted_list)
dickt = {position_of_supports[0]:first_support, position_of_supports[1]:second_support }


dicf= {}


if len(location_of_forces) > 0:
   for i in range(len(location_of_forces)):
       dicf[location_of_forces[i]] = magnitude_of_forces[i]
      
   dickt.update(dicf)  
      






      






x = sp.symbols('x')
functions_list = []
running_total = 0
sorted_dict = {key: dickt[key] for key in sorted(dickt.keys())}
conditions = []
conditionss = []
integrate = 0
integral_list = []


print(sorted_dict)


print("num_of_forces", num_of_forces)
print("input_moments_count", input_moments_count)
print("db_force_count", db_force_count)


if len_moment == 0 and len_distributed_forces == 0 :
   for value in sorted_dict.values():
       running_total += value
       rounded_sum = round(running_total, 2) 
       functions_list.append(rounded_sum)




   for i in range(len(functions_list)-1):
       func = functions_list[i]
       start = sorted_list[i]
       end = sorted_list[i + 1]
       condition = (x >= start) & (x < end)
       conditions.append((func, condition))


   piecewise_func = sp.Piecewise(*conditions)
   print(conditions)
   # Shear Diagram
   fig, ax = plt.subplots()
   ax.set_title("Shear Diagram")
   ax.set_xlabel("m")
   ax.set_ylabel("F")
   x_vals = np.linspace(sorted_list[0], sorted_list[-1], 1000)
   y_vals = [float(piecewise_func.subs(x, val)) for val in x_vals]
   ax.plot(x_vals, y_vals)
   ax.axhline(0, color='red', linewidth=0.8)
   for point in sorted_list[:-1]:
       y_val = float(piecewise_func.subs(x, point))
       ax.plot(point, y_val, 'ro')
       ax.annotate(f'({point}, {round(y_val, 2)})', xy=(point, y_val), xytext=(5, 5), textcoords="offset points")
   plt.show()






   for i in range(len(functions_list)-1):
       integrate = sp.integrate(functions_list[i], x)
       integral_list.append(integrate)
      
   for i in range(len(integral_list)-1):
       subtracted_result = integral_list[i] - integral_list[i + 1]
       x_value = sorted_list[i + 1]
       evaluated_result = subtracted_result.subs(x, x_value)
       new_function = integral_list[i + 1] + evaluated_result
       integral_list[i + 1] = new_function


   for i in range(len(integral_list)):
       func = integral_list[i]
       start = sorted_list[i]
       end = sorted_list[i + 1]
       condition = (x >= start) & (x < end)
       conditionss.append((func, condition)) 
      
   piecewise_func = sp.Piecewise(*conditionss)
   # Moment Diagram
   piecewise_func_moment = sp.Piecewise(*conditionss)
   fig, ax = plt.subplots()
   ax.set_title("Moment Diagram")
   ax.set_xlabel("m")
   ax.set_ylabel("M")
   x_vals = np.linspace(sorted_list[0], sorted_list[-1], 1000)
   y_vals = [float(piecewise_func_moment.subs(x, val)) for val in x_vals]
   ax.plot(x_vals, y_vals)
   ax.axhline(0, color='red', linewidth=0.8)
   for point in sorted_list[:-1]:
       y_val = float(piecewise_func_moment.subs(x, point))
       ax.plot(point, y_val, 'ro')
       ax.annotate(f'({point}, {round(y_val, 2)})', xy=(point, y_val), xytext=(5, 5), textcoords="offset points")
   plt.show()
   #test values(-68, -39, -87,-97), 2.1, 4.3 ,5.1 ,9.5
  
elif len_moment != 0 and len_distributed_forces == 0:
   # --- Shear Diagram (moments don't affect shear) ---
   # Use sorted_list_withoutdb which excludes moment positions
   for value in sorted_dict.values():
       # Only accumulate at non-moment positions
       if list(sorted_dict.keys())[list(sorted_dict.values()).index(value)] not in input_moments_pos:
           running_total += value
           rounded_sum = round(running_total, 2)
           functions_list.append(rounded_sum)


   for i in range(len(functions_list) - 1):
       func = functions_list[i]
       start = sorted_list_withoutdb[i]
       end = sorted_list_withoutdb[i + 1]
       condition = (x >= start) & (x < end)
       conditions.append((func, condition))


   piecewise_func = sp.Piecewise(*conditions)
   # Shear Diagram
   fig, ax = plt.subplots()
   ax.set_title("Shear Diagram")
   ax.set_xlabel("m")
   ax.set_ylabel("F")
   x_vals = np.linspace(sorted_list_withoutdb[0], sorted_list_withoutdb[-1], 1000)
   y_vals = [float(piecewise_func.subs(x, val)) for val in x_vals]
   ax.plot(x_vals, y_vals)
   ax.axhline(0, color='red', linewidth=0.8)
   for point in sorted_list_withoutdb[:-1]:
       y_val = float(piecewise_func.subs(x, point))
       ax.plot(point, y_val, 'ro')
       ax.annotate(f'({point}, {round(y_val, 2)})', xy=(point, y_val), xytext=(5, 5), textcoords="offset points")
   plt.show()


   # --- Moment Diagram ---
   # Integrate shear piecewise, then apply moment jumps
   for i in range(len(functions_list) - 1):
       integrate = sp.integrate(functions_list[i], x)
       integral_list.append(integrate)


   # Continuity correction between segments (same as point-load case)
   for i in range(len(integral_list) - 1):
       subtracted_result = integral_list[i] - integral_list[i + 1]
       x_value = sorted_list_withoutdb[i + 1]
       evaluated_result = subtracted_result.subs(x, x_value)
       new_function = integral_list[i + 1] + evaluated_result
       integral_list[i + 1] = new_function


   print("moment positions", input_moments_pos)
   print("integral list", integral_list)
   print("sorted_list_withoutdb", sorted_list_withoutdb)


   # Apply moment jumps at applied moment locations
   for moment_pos, moment_mag in zip(input_moments_pos, input_moments_mag):
       for i in range(len(integral_list)):
           seg_start = sorted_list_withoutdb[i]
           seg_end = sorted_list_withoutdb[i + 1]
           if moment_pos > seg_start and moment_pos < seg_end:
               # Split the segment at the moment position
               original_func = integral_list[i]
              
               # Insert moment position into sorted_list_withoutdb
               sorted_list_withoutdb.insert(i + 1, moment_pos)
              
               # Keep original function for seg_start to moment_pos
               # Add jump for moment_pos onward
               integral_list.insert(i + 1, original_func - moment_mag)
              
               # Propagate jump to all segments after
               for j in range(i + 2, len(integral_list)):
                   integral_list[j] -= moment_mag
               break
   print("integral list after jump", integral_list)


   for i in range(len(integral_list)):
       func = integral_list[i]
       start = sorted_list_withoutdb[i]
       end = sorted_list_withoutdb[i + 1]
       condition = (x >= start) & (x < end)
       conditionss.append((func, condition))


   piecewise_func = sp.Piecewise(*conditionss)
   # Moment Diagram
   piecewise_func_moment = sp.Piecewise(*conditionss)
   fig, ax = plt.subplots()
   ax.set_title("Moment Diagram")
   ax.set_xlabel("m")
   ax.set_ylabel("M")
   x_vals = np.linspace(sorted_list_withoutdb[0], sorted_list_withoutdb[-1], 1000)
   y_vals = [float(piecewise_func_moment.subs(x, val)) for val in x_vals]
   ax.plot(x_vals, y_vals)
   ax.axhline(0, color='red', linewidth=0.8)
   for point in sorted_list_withoutdb[:-1]:
       y_val = float(piecewise_func_moment.subs(x, point))
       ax.plot(point, y_val, 'ro')
       ax.annotate(f'({point}, {round(y_val, 2)})', xy=(point, y_val), xytext=(5, 5), textcoords="offset points")
   for point in input_moments_pos:
       y_val = float(piecewise_func_moment.subs(x, point))
       ax.plot(point, y_val, 'ro')
       ax.annotate(f'({point}, {round(y_val, 2)})', xy=(point, y_val), xytext=(5, 5), textcoords="offset points")
   plt.show()


elif num_of_forces == 0 and input_moments_count == 0 and db_force_count != 0:
   # Build sorted list of all key positions
   all_positions = sorted(set(position_of_supports + db_force_pos1 + db_force_pos2))
  
   # Build shear conditions segment by segment
   running_shear = first_support
   print("db_force_pos1", db_force_pos1)
   print("db_force_pos2", db_force_pos2)
   print("db_force_mag1", db_force_mag1)
   print("db_force_func", db_force_func)
  
   for i in range(len(all_positions) - 1):
       seg_start = all_positions[i]
       seg_end = all_positions[i + 1]
      
       # Check if a distributed load is active in this segment
       db_active = False
       for j in range(db_force_count):
           if seg_start >= db_force_pos1[j] and seg_end <= db_force_pos2[j]:
               db_active = True
               # Check if function load or regular load
               if len(db_force_mag1) == 0 or j >= len(db_force_mag1):
                   # Function load
                   w_func = -1 * db_force_func[j]
               else:
                   # Linear interpolation of load magnitude across segment
                   distance = db_force_pos2[j] - db_force_pos1[j]
                   w_start = db_force_mag1[j]
                   w_end = db_force_mag2[j]
                   w_func = w_start + (w_end - w_start) / distance * (x - db_force_pos1[j])
               # Integrate load to get shear change
               shear_func = running_shear + sp.integrate(w_func, (x, seg_start, x))
               conditions.append((shear_func, (x >= seg_start) & (x < seg_end)))
               # Update running shear at end of segment
               running_shear = float(running_shear + sp.integrate(w_func, (x, seg_start, seg_end)).evalf())
               break
      
       if not db_active:
           conditions.append((running_shear, (x >= seg_start) & (x < seg_end)))
      
       # Add support reaction at end of segment if there is one
       if seg_end in position_of_supports:
           idx = position_of_supports.index(seg_end)
           if idx == 1:
               running_shear += second_support


   # Shear Diagram
   piecewise_func = sp.Piecewise(*conditions)
   fig, ax = plt.subplots()
   ax.set_title("Shear Diagram")
   ax.set_xlabel("m")
   ax.set_ylabel("F")
   x_vals = np.linspace(all_positions[0], all_positions[-1], 1000)
   y_vals = [float(piecewise_func.subs(x, val)) for val in x_vals]
   ax.plot(x_vals, y_vals)
   ax.axhline(0, color='red', linewidth=0.8)
   for point in all_positions[:-1]:
       y_val = float(piecewise_func.subs(x, point))
       ax.plot(point, y_val, 'ro')
       ax.annotate(f'({point}, {round(y_val, 2)})', xy=(point, y_val), xytext=(5, 5), textcoords="offset points")
   plt.show()


   # Moment Diagram
   integral_list = []
   for i in range(len(conditions)):
       integrate = sp.integrate(conditions[i][0], x)
       integral_list.append(integrate)


   for i in range(len(integral_list) - 1):
       subtracted_result = integral_list[i] - integral_list[i + 1]
       x_value = all_positions[i + 1]
       evaluated_result = subtracted_result.subs(x, x_value)
       new_function = integral_list[i + 1] + evaluated_result
       integral_list[i + 1] = new_function


   conditionss = []
   for i in range(len(integral_list)):
       func = integral_list[i]
       start = all_positions[i]
       end = all_positions[i + 1]
       condition = (x >= start) & (x < end)
       conditionss.append((func, condition))


   piecewise_func_moment = sp.Piecewise(*conditionss)
   fig, ax = plt.subplots()
   ax.set_title("Moment Diagram")
   ax.set_xlabel("m")
   ax.set_ylabel("M")
   x_vals = np.linspace(all_positions[0], all_positions[-1], 1000)
   y_vals = [float(piecewise_func_moment.subs(x, val)) for val in x_vals]
   ax.plot(x_vals, y_vals)
   ax.axhline(0, color='red', linewidth=0.8)
   for point in all_positions[:-1]:
       y_val = float(piecewise_func_moment.subs(x, point))
       ax.plot(point, y_val, 'ro')
       ax.annotate(f'({point}, {round(y_val, 2)})', xy=(point, y_val), xytext=(5, 5), textcoords="offset points")
   plt.show()
elif num_of_forces != 0 and input_moments_count == 0 and db_force_count != 0:
   # Build sorted list of all key positions
   all_positions = sorted(set(position_of_supports + location_of_forces + db_force_pos1 + db_force_pos2))
  
   running_shear = first_support
  
   for i in range(len(all_positions) - 1):
       seg_start = all_positions[i]
       seg_end = all_positions[i + 1]
      
       db_active = False
       for j in range(db_force_count):
           if seg_start >= db_force_pos1[j] and seg_end <= db_force_pos2[j]:
               db_active = True
               if len(db_force_mag1) == 0 or j >= len(db_force_mag1):
                   w_func = db_force_func[j]
               else:
                   distance = db_force_pos2[j] - db_force_pos1[j]
                   w_start = db_force_mag1[j]
                   w_end = db_force_mag2[j]
                   w_func = w_start + (w_end - w_start) / distance * (x - db_force_pos1[j])
               shear_func = running_shear + sp.integrate(w_func, (x, seg_start, x))
               conditions.append((shear_func, (x >= seg_start) & (x < seg_end)))
               running_shear = float(running_shear + sp.integrate(w_func, (x, seg_start, seg_end)).evalf())
               break
      
       if not db_active:
           conditions.append((running_shear, (x >= seg_start) & (x < seg_end)))
      
       # Add point force reaction at this position
       if seg_end in location_of_forces:
           idx = location_of_forces.index(seg_end)
           running_shear += magnitude_of_forces[idx]
      
       # Add support reaction at end of segment
       if seg_end in position_of_supports:
           idx = position_of_supports.index(seg_end)
           if idx == 1:
               running_shear += second_support


   # Shear Diagram
   piecewise_func = sp.Piecewise(*conditions)
   fig, ax = plt.subplots()
   ax.set_title("Shear Diagram")
   ax.set_xlabel("m")
   ax.set_ylabel("F")
   x_vals = np.linspace(all_positions[0], all_positions[-1], 1000)
   y_vals = [float(piecewise_func.subs(x, val)) for val in x_vals]
   ax.plot(x_vals, y_vals)
   ax.axhline(0, color='red', linewidth=0.8)
   for point in all_positions[:-1]:
       y_val = float(piecewise_func.subs(x, point))
       ax.plot(point, y_val, 'ro')
       ax.annotate(f'({point}, {round(y_val, 2)})', xy=(point, y_val), xytext=(5, 5), textcoords="offset points")
   plt.show()


   # Moment Diagram
   integral_list = []
   for i in range(len(conditions)):
       integrate = sp.integrate(conditions[i][0], x)
       integral_list.append(integrate)


   for i in range(len(integral_list) - 1):
       subtracted_result = integral_list[i] - integral_list[i + 1]
       x_value = all_positions[i + 1]
       evaluated_result = subtracted_result.subs(x, x_value)
       new_function = integral_list[i + 1] + evaluated_result
       integral_list[i + 1] = new_function


   conditionss = []
   for i in range(len(integral_list)):
       func = integral_list[i]
       start = all_positions[i]
       end = all_positions[i + 1]
       condition = (x >= start) & (x < end)
       conditionss.append((func, condition))


   piecewise_func_moment = sp.Piecewise(*conditionss)
   fig, ax = plt.subplots()
   ax.set_title("Moment Diagram")
   ax.set_xlabel("m")
   ax.set_ylabel("M")
   x_vals = np.linspace(all_positions[0], all_positions[-1], 1000)
   y_vals = [float(piecewise_func_moment.subs(x, val)) for val in x_vals]
   ax.plot(x_vals, y_vals)
   ax.axhline(0, color='red', linewidth=0.8)
   for point in all_positions[:-1]:
       y_val = float(piecewise_func_moment.subs(x, point))
       ax.plot(point, y_val, 'ro')
       ax.annotate(f'({point}, {round(y_val, 2)})', xy=(point, y_val), xytext=(5, 5), textcoords="offset points")
   plt.show()


elif num_of_forces != 0 and input_moments_count != 0 and db_force_count != 0:
   # Build sorted list of all key positions
   all_positions = sorted(set(position_of_supports + location_of_forces + db_force_pos1 + db_force_pos2))
  
   running_shear = first_support
  
   for i in range(len(all_positions) - 1):
       seg_start = all_positions[i]
       seg_end = all_positions[i + 1]
      
       db_active = False
       for j in range(db_force_count):
           if seg_start >= db_force_pos1[j] and seg_end <= db_force_pos2[j]:
               db_active = True
               if len(db_force_mag1) == 0 or j >= len(db_force_mag1):
                   w_func = db_force_func[j]
               else:
                   distance = db_force_pos2[j] - db_force_pos1[j]
                   w_start = db_force_mag1[j]
                   w_end = db_force_mag2[j]
                   w_func = w_start + (w_end - w_start) / distance * (x - db_force_pos1[j])
               shear_func = running_shear + sp.integrate(w_func, (x, seg_start, x))
               conditions.append((shear_func, (x >= seg_start) & (x < seg_end)))
               running_shear = float(running_shear + sp.integrate(w_func, (x, seg_start, seg_end)).evalf())
               break
      
       if not db_active:
           conditions.append((running_shear, (x >= seg_start) & (x < seg_end)))
      
       if seg_end in location_of_forces:
           idx = location_of_forces.index(seg_end)
           running_shear += magnitude_of_forces[idx]
      
       if seg_end in position_of_supports:
           idx = position_of_supports.index(seg_end)
           if idx == 1:
               running_shear += second_support


   # Shear Diagram
   piecewise_func = sp.Piecewise(*conditions)
   fig, ax = plt.subplots()
   ax.set_title("Shear Diagram")
   ax.set_xlabel("m")
   ax.set_ylabel("F")
   x_vals = np.linspace(all_positions[0], all_positions[-1], 1000)
   y_vals = [float(piecewise_func.subs(x, val)) for val in x_vals]
   ax.plot(x_vals, y_vals)
   ax.axhline(0, color='red', linewidth=0.8)
   for point in all_positions[:-1]:
       y_val = float(piecewise_func.subs(x, point))
       ax.plot(point, y_val, 'ro')
       ax.annotate(f'({point}, {round(y_val, 2)})', xy=(point, y_val), xytext=(5, 5), textcoords="offset points")
   plt.show()


   # Moment Diagram
   integral_list = []
   for i in range(len(conditions)):
       integrate = sp.integrate(conditions[i][0], x)
       integral_list.append(integrate)


   for i in range(len(integral_list) - 1):
       subtracted_result = integral_list[i] - integral_list[i + 1]
       x_value = all_positions[i + 1]
       evaluated_result = subtracted_result.subs(x, x_value)
       new_function = integral_list[i + 1] + evaluated_result
       integral_list[i + 1] = new_function


   # Apply moment jumps
   for moment_pos, moment_mag in zip(input_moments_pos, input_moments_mag):
       for i in range(len(integral_list)):
           seg_start = all_positions[i]
           seg_end = all_positions[i + 1]
           if moment_pos > seg_start and moment_pos < seg_end:
               original_func = integral_list[i]
               all_positions.insert(i + 1, moment_pos)
               integral_list.insert(i + 1, original_func - moment_mag)
               for j in range(i + 2, len(integral_list)):
                   integral_list[j] -= moment_mag
               break


   conditionss = []
   for i in range(len(integral_list)):
       func = integral_list[i]
       start = all_positions[i]
       end = all_positions[i + 1]
       condition = (x >= start) & (x < end)
       conditionss.append((func, condition))


   piecewise_func_moment = sp.Piecewise(*conditionss)
   fig, ax = plt.subplots()
   ax.set_title("Moment Diagram")
   ax.set_xlabel("m")
   ax.set_ylabel("M")
   x_vals = np.linspace(all_positions[0], all_positions[-1], 1000)
   y_vals = [float(piecewise_func_moment.subs(x, val)) for val in x_vals]
   ax.plot(x_vals, y_vals)
   ax.axhline(0, color='red', linewidth=0.8)
   for point in all_positions[:-1]:
       y_val = float(piecewise_func_moment.subs(x, point))
       ax.plot(point, y_val, 'ro')
       ax.annotate(f'({point}, {round(y_val, 2)})', xy=(point, y_val), xytext=(5, 5), textcoords="offset points")
   for point in input_moments_pos:
       y_val = float(piecewise_func_moment.subs(x, point))
       ax.plot(point, y_val, 'ro')
       ax.annotate(f'({point}, {round(y_val, 2)})', xy=(point, y_val), xytext=(5, 5), textcoords="offset points")
   plt.show()