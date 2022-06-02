def register():
  username=input('Please enter username or emailid')
  for i in range(0,len(username)):
    if ((i==0 and username[i]=='@')or(username[i]=='@' and username[i+1]=='.')or(i==0 and username[i].isdigit())or(i==0 and (username[i]=='&' or username[i]=='!' or username[i]=='%' or username[i]=='#'))):
      print('invalid username please enter valid username')
      register()
  password=input('enter password')
  digit=0
  special_char=0
  small_letters=0
  capital_letters=0
  for i in range(0,len(password)):
    if(password[i]=='!' or password[i]=='%' or password[i]=='#' or password[i]=='&' or password[i]=='@' ):
      special_char+=1
    if(password[i].isupper()):
      capital_letters+=1
    if(password[i].islower()):
      small_letters+=1
    if(password[i].isdigit()):
      digit+=1
  if((len(password)>5 and len(password)<16) and special_char>=1 and digit>=1 and small_letters>=1 and capital_letters>=1):
    print('registered successfully!!!!')
    db=open("login.txt", "a")
    data=username+','+password
    db.write(data)
    db.write('\n')
    db.close()
    db=open("login.txt", "r")
    print(db.read())

  else:
    print('password is not matching please register again')
    register()


ss='false'
i=input('Welcome to GUVI.\n if you are a new user enter y to register else n')
if i=='y':
  register()
if i=='n':
  i=input('Would you like to login? enter y or n?')
  if i=='n':
    print('no action is taken')
  if i=='y':
    user_name=input('please enter username/emailid')
    pass_word=input('please enter the password')
    db=open("login.txt", "r")

    for s in db:
      a,b=s.split(",")
      b=b.strip()
      if(user_name==a and pass_word==b):
        print('login successful!!!')
        ss='true'
        exit()
      if(user_name==a and pass_word!=b):
        print('password is wrong.')
        l=input('click forgot password. enter y/n')
        if l=='y':
          print('new password is ',b)
          ss='true'
          break
        else:
          print('no forgot password is requested')
          ss='true'
          break
    if(ss=='false'):
      print('credentials not found. kindly register')