#!/bin/bash


account='admin'
email='admin@mlsteam.ai'
password='password'


[ ! -z "$1" ] && account=$1
[ ! -z "$2" ] && email=$2
[ ! -z "$3" ] && password=$3


read -d '' cmd << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if User.objects.filter(username='$account').count() == 0:
    User.objects.create_superuser('$account', '$email', '$password')
    print('User $account created.')
else:
    print('User $account exists.')
EOF

echo "$cmd" | python3 manage.py shell


