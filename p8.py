# p8 wapp to gen the follow:
#  $  	$	$	$
#  $	$	$
#  $	$	
#  $
# where number of lines to be gen, is given by user

num = int(input(" enter a number of lines"))
if num < 0:
	print("invalid input")
else:
	for i in range(num ,0,  -1):
		print(i *" $\t") 