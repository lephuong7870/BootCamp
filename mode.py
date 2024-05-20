from Activity import recommendActivity
import pandas as pd

if __name__ == '__main__':
    
    ## input Activity
    ## ## HERE 
    days = 3
    city = 'Hà Nội'
    types = ['Du lịch tâm linh' , 'Du lịch văn hóa & nghệ thuật'  ] 
    maxBudget = 2400000
    df =  pd.read_csv('./Activity/data/activity.csv')

    activity = recommendActivity.ActivityRecommend(days, city, types , maxBudget , df)
    activity.perform()

    print( activity.finalPlan1 )
    print( activity.spendingPlan1 )

    print( activity.finalPlan2 )
    print( activity.spendingPlan2 )
    
    print( activity.finalPlan3 )
    print( activity.spendingPlan3 )