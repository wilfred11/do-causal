import pandas as pd
import numpy as np

class BinaryDataGenerator():

    def __init__(self, population_size : int, columns : list, random_state : int = 42):
        self.random_state = random_state
        self.__data = pd.DataFrame(data=np.full(shape=(population_size, len(columns)), fill_value=0, dtype=int), columns=columns)

    def set_values(self, col_name : str, count : int = None, frac : float = None, condition : pd.Series = None, value = 1):
        if condition is None: # If no condition specified, create a dummy condition that is True for every row so the update will be applies to all rows
            condition = pd.Series(data=[True] * len(self.__data))

        update_indices = list(self.__data[condition].sample(n=count, frac=frac, random_state=self.random_state).index)
        self.__data.loc[update_indices, [col_name]] = value

    @property
    def data(self) -> pd.DataFrame:
        return self.__data

    @property
    def summary(self) -> pd.DataFrame:
        return self.__data.value_counts().reset_index().rename({0:"Count"}, axis=1)