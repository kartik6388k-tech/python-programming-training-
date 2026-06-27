
"""You are working in an aerospace manufacturing company.

A CNC machine produces metal shafts continuously.

Each shaft has a quality score between:

0 to 100

Rules:

score < 40 → defective part
40–80 → acceptable part

80 → precision-grade part

But:

if score = -1
→ sensor failed, ignore this reading using continue
if score = 999
→ machine emergency detected, immediately stop inspection using break

The company wants intelligent inspection logic before training future ML quality-prediction models."""

i=0
defective,acceptable,precsion_grade=0,0,0
while i>=0:
	score=int(input("enter the value score for the shaft:v :"))
	if score<40:
		defective+=1
		print("defective")
	if score>=40 and score<80:
		acceptable+=1
		print("acceptable")
	if score>80 :
		precsion_grade+=1
		print("precsion_gade ")
	if score==-1:
		continue
	if score==999:
		i=-1

print (f"defective part:{defective}, acceptable part:{acceptable}, precsion part:{precsion_grade}")
