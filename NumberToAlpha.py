import sys
 

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python NumberToAlpha.py [string]")
        exit()
    out_string = ""
    alpha_string = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    
    alpha_array = alpha_string.split(",")
    alpha_reverse = alpha_string.split(",")
    alpha_reverse.reverse()
    
    split_spaces = sys.argv[1].split()
    split_input = []
    for word in split_spaces:
        split_input.append(word.split("-"))
    #print(split_spaces)
    #print(split_input)
    
    for word in split_input:
        for character in word:
            #dang computers counting from 0
            index = (int(character))
            new_letter = alpha_array[index - 1]
            out_string += new_letter
        out_string += " "
    print(out_string)