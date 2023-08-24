import sqlite3 
import numpy as np
import math 
import os
import pandas as pd


DIRECTORY_PATH = "/home/klychiievfx/Desktop/corpora_generation/databases"


POS_DICT = {
    'part_of_speech':[],
    'absolute_frequency':[],
    'mean_frequency':[],
    'relative_frequency':[],
    'standard_deviation':[],
    'confidence_interval_2sd':[],
    'coefficient_of_variation':[],
    'confidence_interval_2s':[],
    'coef_of_var':[],
    'max_coeff_of_var':[],
    'coefficient_of_stability':[],
    'relative_error':[],
    'standard_error': []
}


def get_statistics(file):
        
    conn = sqlite3.connect(file)
    cur = conn.cursor()

    rows = cur.execute("SELECT * FROM pos_freq")

    for i, row in enumerate(rows):

        freqs = [num if num is not None else 0 for num in row[1:]]

        # Вхідні дані (вибірка з розподілу довжин в см)
        data = np.array(freqs)

        print(data)

        pos = row[0]
        
        POS_DICT['part_of_speech'].append(pos)

        # Абсолютна частота (Absolute Frequency) - загальна кількість вживань певної ЧМ
        absolute_frequency = sum(data)

        POS_DICT['absolute_frequency'].append(absolute_frequency)

        print(f"Absolute Frequency of {row[0]}:", absolute_frequency)

        # Середня частота (Mean Frequency) - середня кількість вживань певної ЧМ у підвибірці
        mean_frequency = np.mean(data)

        POS_DICT['mean_frequency'].append(mean_frequency)

        print("Mean Frequency:", mean_frequency)

        # Відносна частота (Relative Frequency) - частка вживання ЧМ у вибірці
        relative_frequency = absolute_frequency / 20000

        POS_DICT['relative_frequency'].append(relative_frequency)

        print("Relative Frequency:", relative_frequency)

        # Середнє квадратичне відхилення (Standard Deviation)
        standard_deviation = np.std(data)

        POS_DICT['standard_deviation'].append(standard_deviation)

        print("Standard Deviation:", standard_deviation)

        # Довірчий інтервал 2σ (Confidence Interval 2σ)
        confidence_interval = (mean_frequency - 2 * standard_deviation, mean_frequency + 2 * standard_deviation)
        
        POS_DICT['confidence_interval_2sd'].append(confidence_interval)
        
        print("Confidence Interval 2σ:", confidence_interval)

        # Міра коливання середньої частоти (Coefficient of Variation of Mean Frequency)
        coefficient_of_variation = (standard_deviation / math.sqrt(20))

        POS_DICT['coefficient_of_variation'].append(coefficient_of_variation)

        print("Coefficient of Variation of Mean Frequency:", coefficient_of_variation)

        # Стандартна похибка коливання середньої
        standard_error = (standard_deviation / math.sqrt(20-1))

        POS_DICT['standard_error'].append(standard_error)

        print("Standard error of Mean Frequency:", standard_error)

        # Довірчий інтервал 2σx̅ (Confidence Interval 2σx̅)
        confidence_interval_mean = (mean_frequency - 2 * (standard_deviation / np.sqrt(len(data))), mean_frequency + 2 * (standard_deviation / np.sqrt(len(data))))

        POS_DICT['confidence_interval_2s'].append(confidence_interval_mean)

        print("Confidence Interval 2σx̅:", confidence_interval_mean)

        # Коефіцієнт варіації (Coefficient of Variation)
        coefficient_of_variation = (standard_deviation / mean_frequency)

        POS_DICT['coef_of_var'].append(coefficient_of_variation)

        print("Coefficient of Variation:", coefficient_of_variation)

        # Максимальний коефіцієнт варіації (Maximum Coefficient of Variation)
        maximum_coefficient_of_variation = math.sqrt(19)

        POS_DICT['max_coeff_of_var'].append(maximum_coefficient_of_variation)

        print("Maximum Coefficient of Variation:", maximum_coefficient_of_variation)

        # Коефіцієнт стабільності (Coefficient of Stability)
        coefficient_of_stability = (1 - (coefficient_of_variation/maximum_coefficient_of_variation))

        POS_DICT['coefficient_of_stability'].append(coefficient_of_stability)

        print("Coefficient of Stability:", coefficient_of_stability)

        # Відносна похибка (неточність) дослідження (Relative Error)

        if absolute_frequency > 0:

            relative_error = 1.96/math.sqrt(absolute_frequency)

            POS_DICT['relative_error'].append(relative_error)

            print("Relative Error:", relative_error)

        else:

            POS_DICT['relative_error'].append(0)

            print("Relative Error:", relative_error)

        return POS_DICT



if __name__=="__main__":

    for file in os.listdir(DIRECTORY_PATH):

        f = os.path.join(DIRECTORY_PATH, file)

        pos_dict = get_statistics(f)

        df = pd.DataFrame(pos_dict)

        df = df.round(2)

        print(df)

        df.to_csv(f'statistics/{file}.csv')

