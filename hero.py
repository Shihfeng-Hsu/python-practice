"""
A hero is on his way to the castle to complete his mission.
However, 
he's been told that the castle is surrounded with a couple of powerful dragons!
each dragon takes 2 bullets to be defeated,
our hero has no idea how many bullets he should carry.. 
Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons,
 will he survive?

Return True if yes, False otherwise :)
"""

def hero(bullets, dragons):
    if bullets/2 >= dragons:
        print("True")
        return True
    else:
        print("False")
        return False
       

 
hero(10, 5)# True)
hero(7, 4)# False)
hero(4, 5)# False)
hero(100, 40)# True)
hero(1500, 751)# False)
hero(0, 1)# False)
