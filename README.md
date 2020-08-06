# HS Counsel Tool

## The Problem

Every year, over 1.2 million students drop out of high school in the United States alone. That's a student every 26 seconds – or 7,000 a day. About 25% of high school freshmen fail to graduate from high school on time. The goal of this analysis is to build a model that will flag students that are at risk of dropping out of High School so that proper resources can be provided for them. As a tool, such a model could be utilized by high school counselors seeking to understand how to best budget their limited resources.

![](figures/dropcount.png) 

## The Data

The data used for this analysis was collected by NCES for the High School Longitudinal Study of 2009, a Nationally representative, longitudinal study of 23,000+ 9th graders from 944 schools in 2009, with a first follow-up in 2012 and a second follow-up in 2016. Complete information on the dataset can be found at https://nces.ed.gov/surveys/hsls09/. 

The data contains over 8000 variables. For the purposes of this analysis I condensed and consolidated the data points into 16 categories and composites of the more granular original dataset. After cleaning and formatting the data there were 64 variables with 10532 entries collected from the base year of the study, when the students were in 9th grade.

## Analysis

Because recall is so vital in the case of identifying at-risk students (i.e. it's better to over identify than under identify) I chose the model with the highest recall score, which was the logistic regresion model. It was able to predict 73% of dropouts. In the test set 408 students labeled as graduates were identified as at-risk, and 64 at-risk students were missed. Given that 171 of the dropouts were correctly identified this model is still useful in discovering at risk students.

Finally, I modeled each category separately to determine which types of information would be most useful for making judgements in the future, and which areas are not. This will help focus data collection efforts in the future to improve the ability of future models. 

![](figures/recall.png)

I found that Academic achievement was nearly as predictive as the full model. I reccomend using academic achievement as a metric of success for future models.