## Testing the mintapi I found on github
import mintapi,pprint

e = open("email.txt","r")
em = e.next()
email = str.rstrip(em)

p = open("pwd.txt","r")
pw = p.next()
password = str.rstrip(pw)

m = mintapi.Mint(email,password)

c = m.get_transactions_csv() # as raw csv data

csv_file = open('transactions.csv','w')
csv_file.write(c)
csv_file.close()

m.close()
