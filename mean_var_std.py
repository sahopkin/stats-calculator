import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  list = np.array(list, dtype='float')
  list_matrix = list.reshape(3,3)
  
  calculations = {
    'mean': [],
    'variance': [],
    'standard deviation': [],
    'max': [],
    'min': [],
    'sum': []
  }
#mean
  mean_cols = np.mean(list_matrix, axis=0).tolist()
  mean_rows = np.mean(list_matrix, axis=1).tolist()
  mean_flat = np.mean(list_matrix)

  calculations['mean'].append(mean_cols)
  calculations['mean'].append(mean_rows)  
  calculations['mean'].append(mean_flat)

#variance
  var_cols = np.var(list_matrix, axis=0).tolist()
  var_rows = np.var(list_matrix, axis=1).tolist()
  var_flat = np.var(list_matrix)

  calculations['variance'].append(var_cols)
  calculations['variance'].append(var_rows)  
  calculations['variance'].append(var_flat)

#std dev
  std_cols = np.std(list_matrix, axis=0).tolist()
  std_rows = np.std(list_matrix, axis=1).tolist()
  std_flat = np.std(list_matrix)

  calculations['standard deviation'].append(std_cols)
  calculations['standard deviation'].append(std_rows)  
  calculations['standard deviation'].append(std_flat)

#max
  max_cols = np.max(list_matrix, axis=0).tolist()
  max_rows = np.max(list_matrix, axis=1).tolist()
  max_flat = np.max(list_matrix)

  calculations['max'].append(max_cols)
  calculations['max'].append(max_rows)  
  calculations['max'].append(max_flat)

#min
  min_cols = np.min(list_matrix, axis=0).tolist()
  min_rows = np.min(list_matrix, axis=1).tolist()
  min_flat = np.min(list_matrix)

  calculations['min'].append(min_cols)
  calculations['min'].append(min_rows)  
  calculations['min'].append(min_flat)

#sum
  sum_cols = np.sum(list_matrix, axis=0).tolist()
  sum_rows = np.sum(list_matrix, axis=1).tolist()
  sum_flat = np.sum(list_matrix)

  calculations['sum'].append(sum_cols)
  calculations['sum'].append(sum_rows)  
  calculations['sum'].append(sum_flat)

  return calculations