import sys

    

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python AlphaReverser.py [string]")
        exit()
    out_string = ""
    alpha_string = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    
    alpha_array = alpha_string.split(",")
    alpha_reverse = alpha_string.split(",")
    alpha_reverse.reverse()
    print(alpha_array)
    for character in sys.argv[1].lower():
        if character in alpha_string:
            letter_index = alpha_array.index(character)
            new_letter = alpha_reverse[letter_index]
            out_string += new_letter
        else:
            out_string += character
    print(out_string)