# import required packages
import pandas as pd
import datetime
import smtplib

# your gmail credentials here
GMAIL_ID = 'your_email_here'
GMAIL_PWD = 'your_password_here'


# define a function for sending email
def sendEmail(to, sub, msg):

	# connection to gmail
	gmail_obj = smtplib.SMTP('smtp.gmail.com', 587)
	
	# starting the session
	gmail_obj.starttls()	
	
	# login using credentials
	gmail_obj.login(GMAIL_ID, GMAIL_PWD)
	
	# sending email
	gmail_obj.sendmail(GMAIL_ID, to,
				f"Subject : {sub}\n\n{msg}")
	
	# quit the session
	gmail_obj.quit()
	
	print("Email sent to " + str(to) + " with subject "
		+ str(sub) + " and message :" + str(msg))
	

# driver code
if __name__=="__main__":

	# read the excel sheet having all the details
	dataframe = pd.read_excel("excelsheet.xlsx")
	
	# today date in format : DD-MM
	today = datetime.datetime.now().strftime("%d-%m")
	
	# current year in format : YY
	yearNow = datetime.datetime.now().strftime("%Y")
	
	# writeindex list
	writeInd = []												

	for index,item in dataframe.iterrows():
	
		msg = "Many Many Happy Returns of the day dear " + str(item['NAME'])
				
		# stripping the birthday in excel
		# sheet as : DD-MM
		bday = item['Birthday'].strftime("%d-%m")	
		
		# condition checking
		if (today == bday) and yearNow not in str(item['Year']):
			
			# calling the sendEmail function
			sendEmail(item['Email'], "Happy Birthday",
					msg)
			
			writeInd.append(index)								

	for i in writeInd:
	
		yr = dataframe.loc[i,'Year']
		
		# this will record the years in which
		# email has been sent
		dataframe.loc[i,'Year'] = str(yr) + ',' + str(yearNow)			

	dataframe.to_excel('excelsheet.xlsx',
				index = False)
