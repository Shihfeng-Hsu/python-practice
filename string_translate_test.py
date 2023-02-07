def string_to_tanslate (string):
    trans=str.maketrans("ABCD","1234")
    #The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.
    #http:/w3schools.com/python/ref_string_maketrans.asp
    print(string.translate(trans))

string_to_tanslate("ABCD")