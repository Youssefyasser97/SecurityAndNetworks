def generateIC(coset):
    cosetIC = 0
    for c in coset:
        c = c.lower()
        count = [0]*26
        n = 0
        for i in range(0, len(c)):
            val = ord(c[i]) - ord('a')
            if(val >= 0 and val <= 25):
                count[val] = count[val] + 1
                n += 1
        total = 0.0
        for i in range(0, len(count)):
            total += count[i] * (count[i]-1)
        total = total/(n*(n-1))
        cosetIC += total
    cosetIC = cosetIC/len(coset)
    return cosetIC


def crack(cipher):
   # TODO: implementation here
   # Assume that the max key size is 10
   # This method should output the most probable key length for the cipher given
   # Refer to the Keyword Length Estimation with Index of Coincidence from here: https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-IOC-Len.html
   # The method should print the output in the following format:
   # ('IC for key lengths from 1 to 4 is: ', [0.0873015873015873, 0.07142857142857142, 0.1574074074074074, 0.047619047619047616, 0.06000000000000001, 0.12222222222222222, 0.047619047619047616, 0.08333333333333333, 0.09259259259259259, 0.06666666666666667])
   # ('Max IC is: ', 0.1574074074074074)
   # ('Most probable key length is: ', 3)
    # pass  # Remove this line
    my_list = []
    myIClist = []

    for x in range(1,10):
        for i in range(0,x):

            my_list.append(cipher[i::(x)])
        myIClist.append(generateIC(my_list))
        my_list.clear()
    maxIC = max(myIClist)
    # print(myIClist)
    # print(maxIC)
    maxindex = myIClist.index(max(myIClist)) + 1
    print(maxindex)

if __name__ == "__main__":
    s0 = "RSTCSJLSLRSLFELGWLFIISIKRMGL"
    s1 = "OICPWZXZEVLGCLNFSYPGALPXWZJTEGALPCSIIWDHOIECCBFWPAHOPCGALPCCBROASNWTYHOIDBIHVPSCSIDEVLSYPGDLZDSLXSTBNWOTTMICPBAPJEVLCLCSUSEQCUHZQFBPPDOUHESSFLLGSUSCPGWINETVVESSZXLEIZUFZMVYNLBXYZESALPXRPWLRFLIHTHOXSPANPZCWMCZCJPPTQMALPXOISFEHOIZYZFXSTBNCZFQHRYZHKSTDWNRZCSALPXPLGLFGLXSPMJLLYULXSTBNWESSFTFDVALPSITEYCOJIQZFDECOOUHHSWSIDZALQLJGLIESSTEDEVLGCLNFSYPGDIDPSNIYTIZFPNOBWPEVLTPZDSIHSCHVPNFHDJPBVYRSHVXSTBRXSPMJEYNVHRRPHOIHZFSHLCSALPZBLWHSCKS"
    s2 = "VVVXSQWPSNJMUMJOKKLGFQAVEXAHWRVTMFXVVRKAJTVMFLOPHYWJDSTXKAGFVVTPHKYEPPJOKPSWACJVSIGGVOLXLVMQPVCMGOGMFLAKENVRMIUAKTKVHIXCFJZRAHWFHLIUMHCIRFWGFOETIUNEQVJWEHOSJWVQFYWKYMPGQHWISOPKHYFYV"
    crack(s2)
