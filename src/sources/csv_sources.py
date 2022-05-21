import csv
import numpy
import pandas


def load():
    print("Init")

    with open('resources/trips_[WALK, TRANSIT, BICYCLE, CAR]_otp_52330.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='.', quotechar=';')
        for row in spamreader:
            print(', '.join(row))


def load_with_numpy():
    with open('resources/trips_[WALK, TRANSIT, BICYCLE, CAR]_otp_52330.csv') as file_name:
        array = numpy.loadtxt(file_name, delimiter=".")

    print(array)


def load_with_pandas():
    df = pandas.read_csv('resources/trips_[WALK, TRANSIT, BICYCLE, CAR]_otp_50330.csv', delimiter=".", quotechar=";")
    print(df)


def load_surveys():
    headers = ['travelAggregation', 'date', 'time', 'endTime', 'fromPlaceGeocoding', 'fromPlaceBL', 'toPlaceGeocoding',
               'toPlaceBL', 'transportModes1', 'routes1', 'averageWalkDistance1', 'averageWalkTime1',
               'averageWaitingTime1',
               'averageDuration1', 'averageTransfersNumber1', 'averageTransitTime1', 'averageElevationLost1',
               'averageElevationGained1', 'transportModes2', 'routes2', 'averageWalkDistance2', 'averageWalkTime2',
               'averageWaitingTime2', 'averageDuration2', 'averageTransfersNumber2', 'averageTransitTime2',
               'averageElevationLost2', 'averageElevationGained2', 'transportModes3', 'routes3', 'averageWalkDistance3',
               'averageWalkTime3', 'averageWaitingTime3', 'averageDuration3', 'averageTransfersNumber3',
               'averageTransitTime3', 'averageElevationLost3', 'averageElevationGained3', 'transportModes4',
               'routes4', 'averageWalkDistance4', 'averageWalkTime4', 'averageWaitingTime4', 'averageDuration4',
               'averageTransfersNumber4', 'averageTransitTime4', 'averageElevationLost4', 'averageElevationGained5']

    dtypes = {'travelAggregation': 'str',
              'date': 'str',
              'time': 'str',
              'endTime': 'str',
              'fromPlaceGeocoding': 'str',
              'fromPlaceBL': 'str',
              'toPlaceGeocoding': 'str',
              'toPlaceBL': 'str',
              'transportModes1': 'str',
              'routes1': 'int',
              'averageWalkDistance1': 'float',
              'averageWalkTime1': 'float',
              'averageWaitingTime1': 'float',
              'averageDuration1': 'float',
              'averageTransfersNumber1': 'float',
              'averageTransitTime1': 'float',
              'averageElevationLost1': 'float',
              'averageElevationGained1': 'float',
              'transportModes2': 'str',
              'routes2': 'int',
              'averageWalkDistance2': 'float',
              'averageWalkTime2': 'float',
              'averageWaitingTime2': 'float',
              'averageDuration2': 'float',
              'averageTransfersNumber2': 'float',
              'averageTransitTime2': 'float',
              'averageElevationLost2': 'float',
              'averageElevationGained2': 'float',
              'transportModes3': 'str',
              'routes3': 'int',
              'averageWalkDistance3': 'float',
              'averageWalkTime3': 'float',
              'averageWaitingTime3': 'float',
              'averageDuration3': 'float',
              'averageTransfersNumber3': 'float',
              'averageTransitTime3': 'float',
              'averageElevationLost3': 'float',
              'averageElevationGained3': 'float',
              'transportModes4': 'str',
              'routes4': 'int',
              'averageWalkDistance4': 'float',
              'averageWalkTime4': 'float',
              'averageWaitingTime4': 'float',
              'averageDuration4': 'float',
              'averageTransfersNumber4': 'float',
              'averageTransitTime4': 'float',
              'averageElevationLost4': 'float',
              'averageElevationGained4': 'float'
              }

    dataframe = pandas.read_csv('./resources/trips_[WALK, TRANSIT, BICYCLE, CAR]_otp_50330.csv', delimiter=';',
                                names=headers, dtype=dtypes, skiprows=1)

    aaa = {'CAR': 1,
           'PUBLIC_TRANSPORT': 2,
           'WALKING_ONLY': 3,
           'MIXED_BIKE_AND_OTHER': 4,
           'PRIVATE_BIKE': 5,
           'MIXED_CAR_AND_OTHER': 5,
           'OTHER': 6
           }

    dictionary = {'BICYCLE': 1,
                  'WALK-BICYCLE': 2,
                  'BICYCLE-WALK': 2,
                  'WALK-BICYCLE-WALK': 3,
                  'BICYCLE-WALK-BICYCLE': 3,
                  'BICYCLE-WALK-BICYCLE-WALK-BICYCLE-WALK-BICYCLE': 4,
                  'BICYCLE-WALK-BICYCLE-WALK-BICYCLE': 4,
                  'WALK-BICYCLE-WALK-BICYCLE-WALK-BICYCLE': 4,
                  'BICYCLE-WALK-BICYCLE-WALK': 4,
                  None: 5}

    dataframe['travelAggregation'] = dataframe.travelAggregation.replace(aaa)
    dataframe['transportModes1'] = dataframe.transportModes1.replace(dictionary)
    dataframe['transportModes2'] = dataframe.transportModes2.replace(dictionary)
    dataframe['transportModes3'] = dataframe.transportModes3.replace(dictionary)
    dataframe['transportModes4'] = dataframe.transportModes4.replace(dictionary)

    return dataframe
