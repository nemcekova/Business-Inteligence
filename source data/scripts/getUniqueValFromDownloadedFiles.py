import itertools
import pandas as pd


CSV_RESTRIC = 'resultData/restrictions.csv'
CSV_TESTING_POLICY = 'resultData/testing-policy.csv'

csv_restriction = pd.read_csv(CSV_RESTRIC)
csv_policy = pd.read_csv(CSV_TESTING_POLICY)

testing_policy = 'testing_policy'
testing_policy_vals = csv_policy[testing_policy].unique()
frame = pd.DataFrame(
    {
        testing_policy: testing_policy_vals,
    }
)
frame.to_csv("resultData/dim_table_testing_policy" + ".csv", index=False)

masks = 'masks'
masks_vals = csv_restriction[masks].unique()
frame = pd.DataFrame(
    {
        masks: masks_vals,
    }
)
frame.to_csv("resultData/dim_table_masks" + ".csv", index=False)

closure = [
    'closure_schools',
    'closure_workplace'
]

cl1 = csv_restriction[closure[0]].unique()
cl2 = csv_restriction[closure[1]].unique()

closureList = list(itertools.product(cl1, cl2))

val1 = []
val2 = []
for i in closureList:
    val1.append(i[0])
    val2.append(i[1])

frame = pd.DataFrame(
    {
     closure[0]: val1,
     closure[1]: val2
    }
)
frame.to_csv("resultData/dim_table_closure" + ".csv", index=False)

travel = 'type_travel_controle'

frame = pd.DataFrame(
    {
        travel: csv_restriction[travel].unique(),
    }
)
frame.to_csv("resultData/dim_table_" + travel + ".csv", index=False)

lockdown = [
    'public_events',
    'stay_at_home',
]


public_events = csv_restriction[lockdown[0]].unique()
stay_at_home = csv_restriction[lockdown[1]].unique()

list = list(itertools.product(public_events, stay_at_home))

val1 = []
val2 = []
for i in list:
    val1.append(i[0])
    val2.append(i[1])

frame = pd.DataFrame(
    {
        lockdown[0]: val1,
        lockdown[1]: val2
    }
)

frame.to_csv("resultData/dim_table_lockdown" + ".csv", index=False)