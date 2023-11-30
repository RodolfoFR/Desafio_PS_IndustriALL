import numpy as np

def test(model, inputs, expected_outputs, analysis_period, number_input, binary_classification=True):
    
  """
  
    This function is the test do model with test dataset
    
    Args:
    
      model (tensorflow.keras.models.Sequential) : The predict model
      inputs (np.ndarray): The Input of test dataset
      expected_outputs (np.ndarray): The Output of test dataset
      analysis_period (int): analysis period, minutes, for the RNN
      number_input (int): size of inputs
      binary_classification (bool): if model is to binary classification, default = True
      
    Return:
      
      dict_infos (dict): Informations about test model
      
  
  """
  
  total_amount = len(expected_outputs) # amount of test data

  dict_infos = dict() # variable to store informations about the test result

  dict_infos["total_amount"] = total_amount

  if binary_classification: # main model
    
    # check the possible output and amount per class
    output_classes,  amount_per_classes = np.unique(expected_outputs, return_counts=True)
    
    # check the correct index od classes
    idx = np.where(output_classes == 0)
    idx = idx[0][0]
    
    # amount the data per classes
    amount_class_0 = amount_per_classes[idx]
    amount_class_1 = amount_per_classes[1-idx]
    
    dict_infos["amount_class_0"] = amount_class_0
    dict_infos["amount_class_1"] = amount_class_1

    TP = [0, 0] # true positive, index 0 is class 0 (Normal) and index 1 is class 1 (Anormal)

    for i in range(total_amount): # each all test data

      input = inputs[i].reshape((1, analysis_period, number_input)) # reshape in input to predict
      predict = model(input) # the predict from model
      predict = np.around(predict[0, 0]) # around (1 or 0)
      
      # check if is True Positive
      if predict == expected_outputs[i]:
        TP[int(expected_outputs[i])] += 1
    
    # precision total 
    precision_total = (TP[0] + TP[1]) / total_amount
    dict_infos["precision_total"] = precision_total
    
    # precision per classes
    
    precision_class_0 = TP[0] / amount_class_0
    dict_infos["precision_class_0"] = precision_class_0

    precision_class_1 = TP[1] / amount_class_1
    dict_infos["precision_class_1"] = precision_class_1

    return dict_infos

  else:
         
    sum_error = 0 # sum of error
      
    for i in range(total_amount): # each all test data
          
      input = inputs[i].reshape((1, analysis_period, number_input))  # reshape in input to predict
      predict = model(input) # the predict from model
      predict = np.around(predict[0, 0]) # around to int
      
      if expected_outputs[i] == 0: # for calculate relative error if expected output 0
          output = 1e-3
      else:
          output = expected_outputs[i] 
      
      relative_error = abs(output - predict) / abs(output )
      
      sum_error += relative_error
    
    mean_error = sum_error / total_amount # mean of relative error of test dataset
    
    dict_infos["mean_error"] = mean_error
    
    return dict_infos
      
      
      
