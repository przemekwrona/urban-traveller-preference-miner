from src.sources import csv_sources
from src.scikit import decision_tree
from src.scikit import hoeffding_tree


def run():
    surveys = csv_sources.load_surveys()

    print(surveys.head(5))

    headers = ['routes1', 'averageWalkDistance1', 'averageWalkTime1', 'averageWaitingTime1',
               'averageDuration1', 'averageTransfersNumber1', 'averageTransitTime1',
               'averageElevationLost1',
               'averageElevationGained1', 'routes2',
               'averageWalkDistance2', 'averageWalkTime2',
               'averageWaitingTime2', 'averageDuration2', 'averageTransfersNumber2',
               'averageTransitTime2',
               'averageElevationLost2', 'averageElevationGained2',
               'routes3', 'averageWalkDistance3',
               'averageWalkTime3', 'averageWaitingTime3', 'averageDuration3',
               'averageTransfersNumber3',
               'averageTransitTime3', 'averageElevationLost3', 'averageElevationGained3',
               'routes4', 'averageWalkDistance4', 'averageWalkTime4',
               'averageWaitingTime4', 'averageDuration4',
               'averageTransfersNumber4', 'averageTransitTime4', 'averageElevationLost4',
               'averageElevationGained5']

    class_names = ['CAR', 'PUBLIC_TRANSPORT', 'WALKING_ONLY', 'MIXED_BIKE_AND_OTHER', 'PRIVATE_BIKE',
                   'MIXED_CAR_AND_OTHER', 'OTHER']

    x = surveys[['routes1', 'averageWalkDistance1', 'averageWalkTime1', 'averageWaitingTime1',
                 'averageDuration1', 'averageTransfersNumber1', 'averageTransitTime1',
                 'averageElevationLost1',
                 'averageElevationGained1', 'routes2',
                 'averageWalkDistance2', 'averageWalkTime2',
                 'averageWaitingTime2', 'averageDuration2', 'averageTransfersNumber2',
                 'averageTransitTime2',
                 'averageElevationLost2', 'averageElevationGained2',
                 'routes3', 'averageWalkDistance3',
                 'averageWalkTime3', 'averageWaitingTime3', 'averageDuration3',
                 'averageTransfersNumber3',
                 'averageTransitTime3', 'averageElevationLost3', 'averageElevationGained3',
                 'routes4', 'averageWalkDistance4', 'averageWalkTime4',
                 'averageWaitingTime4', 'averageDuration4',
                 'averageTransfersNumber4', 'averageTransitTime4', 'averageElevationLost4',
                 'averageElevationGained5']]

    y = surveys['travelAggregation']

    decision_tree_classifier = decision_tree.learn(x, y, headers=headers, class_names=class_names)

    hoeffding_tree_classifier = hoeffding_tree.learn(x, y, headers=headers, class_names=class_names)

    print("End of algorithm")
