
# def Upper(word : str) ->bool :
#     return [True for w in word if w.isupper() == True ][0]
    
# def Lpper(word : str) ->bool :
#     return [True for w in word if w.islower() == True ][0]


# Upper(
#     "Hello"
# )

"""
to avoid repetition use just pass function as argumet
# define class first
"""

def Check(
    word : str , check_func
):
    return [True for w in word if check_func(w) == True ][0]


# print(Check(
#     "Hello",
#     str.isupper
# ))

print(
    # str.isupper(
    #     "H"
    # )

    "H".isupper()
)

#str.isdigit("5")
