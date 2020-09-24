I used python for the socket programming.

Project URL: https://david.choffnes.com/classes/cs4700fa20/project1.php

Code:
The code is written in different functions. each functions handle the messages that are received from the server.
From parsing them to solving the operation.

For the SSL section. We first create the socket then wrap it with SSL. Received so many errors in this part because of verify certificate error.
Finally I was able to fix it by disabling check_hostname and verify mode in the context.

Handling arguments and parameters is also done in a separate function.
This one took more time than the whole socket programming :D
I've considered some error handling too in my code.
 

Other Challenges:
No specific challenge. The only problem that I had was connecting to the server which was fixed by using NEU VPN.
