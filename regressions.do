clear
use "/Users/shashanksingh/Desktop/Semester 5/RTSM/proj/archive/overall.dta"

summarize

reg balance income rating cards age education gender student married ethnicity

clear
use "/Users/shashanksingh/Desktop/Semester 5/RTSM/proj/archive/active.dta"

reg balance income rating cards age education gender student married ethnicity

clear
use "/Users/shashanksingh/Desktop/Semester 5/RTSM/proj/archive/overall.dta"

reg balance income rating age student

clear
use "/Users/shashanksingh/Desktop/Semester 5/RTSM/proj/archive/overall.dta"

gen income_sq = income*income

reg balance income income_sq rating age student

clear
use "/Users/shashanksingh/Desktop/Semester 5/RTSM/proj/archive/overall.dta"

gen income_sq = income*income

gen income_rating = income*rating

reg balance income income_sq rating age student income_rating

clear
use "/Users/shashanksingh/Desktop/Semester 5/RTSM/proj/archive/overall.dta"

gen income_sq = income*income

gen education_income = education*income

reg balance income income_sq rating age student education_income


clear
use "/Users/shashanksingh/Desktop/Semester 5/RTSM/proj/archive/active.dta"

gen income_sq = income*income

gen income_rating = income*rating

reg balance income income_sq rating age student income_rating

clear
use "/Users/shashanksingh/Desktop/Semester 5/RTSM/proj/archive/active.dta"

gen income_sq = income*income

gen income_rating = income*rating

reg balance limit rating income age student cards
