import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Histogram:

  """

    This class is the Histogram of pd.Series Object

  """

  def __init__(self, input, column, width=2):

    self.base_serie = input # the original pd.Series Input
    self.column = column # the column representing the pd.Series Input
    self.mean = self.base_serie.mean() # mean of values of base_serie
    self.std = self.base_serie.std() # std of values of base_serie
    self.max_value = self.mean + (width * self.std) # max value of histogram range
    self.min_value = self.mean - (width * self.std) # min value of histogram range

    # pd.Series only base_serie's values into histogram range
    self.values_serie =  self.base_serie.loc[(self.base_serie>=self.min_value) & (self.base_serie<self.max_value)]
    self.amount = len(self.values_serie) # amount the values into histogram range
    self.amount_subdivisions = int(1 + np.log2(self.amount)) # Number of subdivisions of Histogram with based Sturges Rule

    # Histogram's subdivisions and step
    self.subdivisions, self.step = np.linspace(self.min_value, self.max_value, num=self.amount_subdivisions, endpoint=False, retstep=True)
    
    # lists to store the absolute/relative frequencies
    self.absolute_frequencies = list()
    self.relative_frequencies = list()

    # counting the frequency each Histogram's subdivisions
    for i in range(self.amount_subdivisions):
      absolute_frequency = self.values_serie.between(self.subdivisions[i], self.subdivisions[i]+self.step, inclusive="left").sum()
      relative_frequency =  absolute_frequency / self.amount
      self.absolute_frequencies.append(absolute_frequency)
      self.relative_frequencies.append(relative_frequency)

    data = { "subdivisions": self.subdivisions,
             "absolute_frequencies": self.absolute_frequencies,
             "relative_frequencies": self.relative_frequencies }

    # Histogram's pd.DataFrame
    self.histrogram_dataframe = pd.DataFrame(data)
  
  def plot(self, graphic_width, graphic_height,color="blue", title=None, top=1.0):
        
    """
    
        This method plot the histogram

        Args:
            graphic_width (int or float): width of plot graphic, used in plt.figure()
            graphic_height (int or float): height of plot graphic, used in plt.figure()
            color (str): color of histogram,to use in the method plt.step() and plt.fill_between(), default = "blue"
            title (None or str): title of histogram, case None the tile will be column name, used in plt.title(),default = None 
            top (float or int): top of plot graphic, used in plt.ylim(), default = 1.0
    
    """

    if title is None:
      title = self.column
      
    if self.histrogram_dataframe["relative_frequencies"].max() > top:
        top = 1.2 * self.histrogram_dataframe["relative_frequencies"].max()
      
    plt.figure(figsize=(graphic_width, graphic_height))

    plt.step(self.histrogram_dataframe["subdivisions"], self.histrogram_dataframe["relative_frequencies"], color=color, where='post')
    plt.fill_between(self.histrogram_dataframe["subdivisions"], self.histrogram_dataframe["relative_frequencies"], alpha=1, color=color, step='post')
    plt.xlabel(self.column)
    plt.ylabel("Relative Frequency")
    plt.title(title)
    plt.ylim(0, top)
    plt.grid(True)
    plt.show()
    

  def intersection(self, comparison_histogram, number_samples=25):
        
    """
    
      This method return the relative intersection area between this histogram and comparison histogram

      Args:
        
        comparison_histogram (Histogram): Comparison histogram
        number_samples (int): number samples to calculate the relative intersection area of histograms
        
      return:
        
        relative_intersection_area (float) or 0.0: relative intersection area of histograms
    
    """
    
    # get the histogram interval
    interval_h1 = (self.histrogram_dataframe["subdivisions"].min(), self.histrogram_dataframe["subdivisions"].max())
    interval_h2 = (comparison_histogram.histrogram_dataframe["subdivisions"].min(), comparison_histogram.histrogram_dataframe["subdivisions"].max())
    
    # set the intersection interval  
    if interval_h1[1] >= interval_h2[1]:
      if interval_h1[0] > interval_h2[1]:
        return 0.0
      else:
        interval = (interval_h2[0], interval_h1[1])
        
    else: 
      if interval_h2[0] > interval_h1[1]:
        return 0.0
      else:
        interval = (interval_h1[0], interval_h2[1])
                
    # set the samples of intersection interval    
    samples, step = np.linspace(interval[0], interval[1], num=number_samples, endpoint="True", retstep=True)
        
    h1_intersection= np.zeros(number_samples) # this histogram in interval
    h2_intersection = np.zeros(number_samples) # comparison histogram in interval
    
    # get the area of h1 that is in the intersection area    
    for i in range(self.amount_subdivisions):
        
      mask = ((samples >= self.subdivisions[i]) & (samples < (self.subdivisions[i] + self.step)))
      h1_intersection[mask] = self.histrogram_dataframe['relative_frequencies'][i]
    
    # get the area of h2 that is in the intersection area  
    for i in range(comparison_histogram.amount_subdivisions):
            
      mask = ((samples >= comparison_histogram.subdivisions[i]) & (samples < (comparison_histogram.subdivisions[i]+ comparison_histogram.step)))
      h2_intersection[mask] = comparison_histogram.histrogram_dataframe['relative_frequencies'][i]
    
    # calculate  intersection area      
    intersection_area = step * np.minimum(h1_intersection, h2_intersection).sum()
    
    
    # the area is only the step, because the sum of relative frequencies in all histogram is 1 
    h1_area = self.step 
    h2_area = comparison_histogram.step
    
    # total area or union area
    total_area = h1_area + h2_area - intersection_area
    
    # calculate relative intersection area
    relative_intersection_area = intersection_area / total_area
        
    return relative_intersection_area
            
            
            
        
        