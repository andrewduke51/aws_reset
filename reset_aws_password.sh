#!/bin/bash

echo "Hello, set your new password for the aws console :-)?"
read PASSWORD
echo "what is your username?"
read USER
echo "Choose your aws profile? (or just press enter to accept the default)"
read PROFILE
aws iam update-login-profile --user-name $USER --password $PASSWORD --profile $PROFILE
echo "You are all set and you can login to the aws console using your new password now!"
exit 0
