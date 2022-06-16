'''
You are getting 3 sides of triage - take it from keyboard
S1
S2
S3
Whether triangle is possible with these sides.
'''
s1 = 4
s2 = 15
s3 = 7

if ((s1 + s2) > s3) and ((s1 + s3) > s2) and ((s3 + s2) > s1) :
    print("Triangle is Possible")
else:
    print("Triangle is not possible")
