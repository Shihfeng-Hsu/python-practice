def generate_hashtag(s):
    
    stripString = s.strip()
    sArr = stripString.split(' ')
    new_arr = list(filter(None,sArr))
    return_data=["#"]
    if len(new_arr) == 0:
        return False
    for item in new_arr:
        if len(item) > 140:
            return False
        return_data.append(item.lower().capitalize())
    
    return_str="".join(return_data)
    if len(return_str) > 140:
        return False
    return "".join(return_data)



generate_hashtag('Codewars      ')#, '#Codewars', 'Should handle trailing whitespace.')
generate_hashtag('      Codewars')#, '#Codewars', 'Should handle leading whitespace.')
generate_hashtag('Codewars Is Nice')#, '#CodewarsIsNice', 'Should remove spaces.')
generate_hashtag('codewars is nice')#, '#CodewarsIsNice', 'Should capitalize first letters of words.')
generate_hashtag('CoDeWaRs is niCe')#, '#CodewarsIsNice', 'Only the first letter of each word should be capitalized in the final hashtag, all other letters must be lower case.')
generate_hashtag('c i n')#, '#CIN', 'A single letter is considered to be a word of length 1, so should capitalize first letters of words of length 1.')
generate_hashtag('codewars  is  nice')#, '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.'

#Should return False if the input is empty, or result is longer than 140 chars"
generate_hashtag('')#, False, 'Expected an empty string to return False')
generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat')#, False, 'Should return False if the final string is longer than 140 chars.')