# Module3Project

## The Data

The data used for this analysis was collected by NCES for the High School Longitudinal Study of 2009, a Nationally representative, longitudinal study of 23,000+ 9th graders from 944 schools in 2009, with a first follow-up in 2012 and a second follow-up in 2016. Complete information on the dataset can be found at https://nces.ed.gov/surveys/hsls09/ . 

The data contains over 8000 variables. For the purposes of this analysis I condensed and consolidated the data points into categories and composites of the more granular original dataset. After cleaning and formatting the data there were 64 variables with 10532 entries collected primarily from the base year of the study, when the students were in 9th grade.

## The Problem

The goal of this analysis is to build a model that will flag students that are at risk of dropping out of High School so that proper resources can be provided for them. As a tool, such a model could be utilized by high school counselors seeking to understand how to best budget their limited resources. 

##### Identity
- X1SEX - Student's sex
- X1HISPANIC, X1WHITE, X1BLACK - Student's race
- X1LOCALE - School's urbanicity
- X1REGION - School's Region

##### Background
- X1PAREDU - Highest Parent Education Levels
- X1PARPATTERN - Parent Relationship
- X1HHNUMBER - Number of Household Members 
- X1FAMINCOME, X1POVERTY, X1POVERTY130, X1POVERTY185 - Income Status  
- Parent? - Whether the student is a parent, and whether the became one in HS or in the three years after HS

##### Student Attitudes
- X1STUEDEXPCT - How far in school 9th grader thinks he/she will get
- S1SUREHSGRAD - How sure 9th grader is that he/she will graduate from high school
- S1ABILITYBA - 9th grader thinks he/she has the ability to complete a Bachelor's degree
- S1SCHWASTE - 9th grader feels that school is often a waste of time
- S1GOODGRADES - Getting good grades is important to 9th grader
- S1PAYOFF - 9th grader thinks studying in school rarely pays off later with good job
- S1GETINTOCLG - 9th grader thinks even if he/she studies he/she won't get into college
- S1AFFORD - 9th grader thinks even if he/she studies family can't afford college

##### Student Plans
- S1WORKING - 9th grader thinks working is more important for him/her than college
- S1PLAN - 9th grader has put together an education plan and/or career plan
- S1BAAGE30 - 9th grader would be disappointed if he/she didn't have a BA/BS by age 30
- S1FYNOTSURE - 9th grader does not know what he/she will do in 1st year after HS

##### Family/Peer Support
- X1PAREDEXPCT - How far in school parent thinks 9th grader will go
- NOTALK9COURSES - 9th grader didn't talk to anyone about 2009-2010 courses
- S1NOTALKCLG - 9th grader didn't talk to anyone about going to college
- S1NOTALKJOB - 9th grader didn't talk to anyone about adult jobs/careers
- S1NOTALKPRB - 9th grader didn't talk to anyone about personal problems
- FRNDGOODSTUD - A composite of questionarre responses indicating whether the student's closest friend is a good student

##### Academic Performance
- X3TGPA9TH - GPA: ninth grade
- CLSPREP - A composite score based on questions regarding class preparedness
- HRSHOMEWRK - Hours spent on homework/studying on typical schoolday

##### Extracurriculars and Hobbies
- S1HRACTIVITY - Hours spent on extracurricular activities on typical schoolday
- S1HRWORK - Hours spent working for pay on typical schoolday
- HRSSOCIAL - Hours spent with family or friends on typical schoolday
- HRSTECH - a composite score totaling the time spent using technology after school

##### School Culture
- S1SAFE - 9th grader feels safe at school
- S1PROUD - 9th grader is proud to be part of his/her school
- S1TALKPROB - 9th grader has teacher/adult in school he/she can talk to about problems

##### Academic Support
- MTHPROG - Composite score of the total math/ science supports the school offers
- HELP - Composite score of the total academic support programs the school has for struggling students
- C1NOWAY - School doesn't have any options for taking courses not offered by school
- C1GEDPREP - School has formal GED test preparation program on-site

##### Counselor Qualities
- C1CASELOAD - Average caseload for school's counselors
- C1GOAL1 - School counseling program's most emphasized goal
- C1CLGPREP - School has counselor designated for college readiness/selection/apply
- C1WORKFORCE - School has counselor designated for workforce preparation/placement

##### School Culture
- S1SAFE - 9th grader feels safe at school
- S1PROUD - 9th grader is proud to be part of his/her school
- S1TALKPROB - 9th grader has teacher/adult in school he/she can talk to about problems

##### Academic Support
- MTHPROG - Composite score of the total math/ science supports the school offers
- HELP - Composite score of the total academic support programs the school has for struggling students
- C1NOWAY - School doesn't have any options for taking courses not offered by school
- C1GEDPREP - School has formal GED test preparation program on-site

##### Career Services
- X3ATTENDCTE - Attended CTE center
- JOBPROG - Composite score for total of job programs the school offers

##### College Services
- COUNSMEET - student has met with high school counselor about financial aid or college acceptance in 2012-2013 year
- CPORG - 9th grader participated in college prep organizations like Talent Search, Upward Bound, Gear Up, AVID or MESA
- CLGPROG - composite score for the total of college prep programs the school offers

##### Dropout Prevention
- C1DROPOUT - School has a formal dropout prevention program for high school students

##### Transition Programs
- MS2HS- a composite score totalling the number of programs the school has for helping transition from Middle school to High School

##### Targets
- X4EVERDROP - Ever dropped out of high school

### Analysis
The model was able to predict 73% of dropouts with a precision of 30%. Although this precision is not ideal, in light of the problem, which seeks to provide services for students in need of additional support a high recall rate is the priority.

In addition, I modeled each category separately to determine which types of information would be most useful for making judgements in the future. I found that Academic achievement was nearly as predictive as the full model. I reccomend using academic achievement as a metric of success for some of the other categories, which were not as predictive when it comes to student dropouts.
