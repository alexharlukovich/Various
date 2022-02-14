# task 1 Bubble-sort

l = list('The varsity letters were first customized by Harvard University in 1865 and originally designed to reward baseball'
     ' players on their teams as a token for exceptional performance. The term letterman comes from the letter, which is'
     ' the initial or signature icon, that is placed on the front or back of these sweaters and jackets. These letterman'
     ' (also known as varsity) sweaters or jackets were worn to represent the social identities of athletes and reflect'
     ' a strong sense of team spirit, pride of belonging to a particular school, and values of collectivism. The letters'
     ' on the jackets represented the school and were therefore placed with the intention of acknowledging scholastic '
     'achievement of the wearer.')

print(l)

def bubble_sort(l):
    for run in range (len(l)-1):
        for i in range (len(l)-1-run):
            if l[i]>l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
    return l
print(bubble_sort(l))
