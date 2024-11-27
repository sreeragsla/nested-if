#nested if

d={'sreerag':'srg','happy':'sad'}
username=input('enter your username')

if username in d:
    password=input('enter your password')
    if d[username]==password:
        print('login success')
    else:
        print('wrong password')
else:
    print('username not found')


    
