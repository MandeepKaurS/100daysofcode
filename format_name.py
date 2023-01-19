def format_name(fname,lname):
  f_name=fname.title()
  l_name=lname.title()
  print(f"{f_name} {l_name}")

f_name=input("Whats your first name?")
l_name=input("Whats your last name?")
format_name(f_name,l_name)
