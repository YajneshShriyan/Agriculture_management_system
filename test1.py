import subprocess as sp
import pymysql
import pymysql.cursors

def details_framer():
	try:
		row={}
		print("Enter new farmer's data: ")
		name=input(" Name(fname lname):" ).split(' ')
		row["fname"] = name[0]
		row["lname"] = name[1]
		row["Sex"] = input("Sex: ")
		row["DOB"] = input("Birth Date (YYYY-MM-DD): ")
		row["landsize"] = float(input("landsize: "))
		row["F_Aadhar_no"]=int(input("Aadharno: "))
		row["Bankpassbook_no"]=int(input("Bankpassbook_no"))
		row["village_id"]=int(input("village_id: "))
		row["scheme_id"]=int(input("scheme_id"))

		query = "INSERT INTO Farmer(F_Aadhar_no,Bankpassbook_no,village_id,scheme_id) VALUES(%d,%d,%d,%d)" % (row["F_Aadhar_no"], row["Bankpassbook_no"], row["village_id"],row["scheme_id"])		
		print(query)
		cur.execute(query)
		con.commit()

		query = "INSERT INTO Personal_details(Aadharcard_no,fname,lname,Sex,landsize,DOB) VALUES(%d,'%s','%s','%s',%f,'%s')" % (row["F_Aadhar_no"], row["fname"], row["lname"], row["Sex"], row["landsize"], row["DOB"])
		print(query)
		cur.execute(query)
		con.commit()

		print("Inserted Into Database")
	except Exception as e:
		con.rollback()
		print("Failed to insert ")
		print(e)
	return


def delete_farmer():
	try:
		farmer_adhar_num=int(input("Enter farmer's adhar num:  "))
		query="DELETE FROM Farmer WHERE F_Aadhar_no = %s"

		print(query)
		cur.execute(query,farmer_adhar_num)
		con.commit()

		query="DELETE FROM Personal_details WHERE Aadharcard_no = %s"
		print(query)
		cur.execute(query,farmer_adhar_num)
		con.commit()


		print("Deleted from Database")
	except Exception as e:
		con.rollback()
		print("Failed to delete ")
		print(e)

	return

def delete_buyer():
	try:
		farmer_adhar_num=int(input("Enter buyer's adhar num:  "))
		query="DELETE FROM Buyer WHERE B_Aadhar_no = %s"

		print(query)
		cur.execute(query,farmer_adhar_num)
		con.commit()

		query="DELETE FROM Personal_details WHERE Aadharcard_no = %s"
		print(query)
		cur.execute(query,farmer_adhar_num)
		con.commit()


		print("Deleted from Database")
	except Exception as e:
		con.rollback()
		print("Failed to delete ")
		print(e)

	return


def register_land():
	try:
		row={}
		print("Enter new land details: ")
		row["Land_reg_num"]=int(input("Land_reg_num:  "))
		row["owner_adhar_num"]=int(input("owner_adhar_num: "))
		row["geographical_location"]=input("geographical_location: ")
		row["landsize"]=float(input("landsize: "))
		row["soil_type"]=input("soil_type: ")
		row["crops_grown_id"]=int(input("crops_grown_id: "))
		query = "INSERT INTO Land(Land_reg_num,owner_adhar_num,geographical_location,landsize,soil_type,crops_grown_id) VALUES(%d,%d,'%s',%f,'%s',%d)" % (row["Land_reg_num"],row["owner_adhar_num"],row["geographical_location"],row["landsize"],row["soil_type"],row["crops_grown_id"])

		print(query)
		cur.execute(query)
		con.commit()

		print("Inserted Into Database")

	except Exception as e:
		con.rollback()
		print("Failed to insert ")
		print(e)


def details_buyer():
	try:
		row={}
		print("Enter new buyer's data: ")
		name=input(" Name(fname lname):" ).split(' ')
		row["fname"] = name[0]
		row["lname"] = name[1]
		row["Sex"] = input("Sex: ")
		row["DOB"] = input("Birth Date (YYYY-MM-DD): ")
		row["landsize"] = float(input("landsize: "))
		row["B_Aadhar_no"]=int(input("Aadharno: "))
		row["village_id"]=int(input("village_id: "))
		row["market_id"]=int(input("market_id: "))

		query = "INSERT INTO Buyer(B_Aadhar_no,village_id,market_id) VALUES(%d,%d,%d)" % (row["B_Aadhar_no"], row["village_id"],row["market_id"])
		print(query)
		cur.execute(query)
		con.commit()

		query = "INSERT INTO Personal_details(Aadharcard_no,fname,lname,Sex,landsize,DOB) VALUES(%d,'%s','%s','%s',%f,'%s')" % (row["B_Aadhar_no"], row["fname"], row["lname"], row["Sex"], row["landsize"], row["DOB"])
		print(query)
		cur.execute(query)
		con.commit()

		print("Inserted Into Database")

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print(e)

	return

def update_details_farmer():
	Aadhar_no=int(input("Enter Aadharno to update farmer information  "))
	while (1):
		print("1. update fname")
		print("2. update lname")
		print("3. update sex")
		print("4. DOB")
		print("5. update landsize")
		print("6. update village_id")
		print("7. scheme_id")
		print("8. update Bankpassbook_no")
		print("9. ok")
		ch = int(input("Enter the choice:  "))
		newval=""
		query=""
		if(ch==1):
			newval=input("Enter new fname")
			query="UPDATE Personal_details SET fname=%s WHERE Aadharcard_no=%s"
			val=(newval,Aadhar_no)
			cur.execute(query,val)
			con.commit()
		elif(ch==2):
			newval=input("Enter new lname")
			query="UPDATE Personal_details SET lname=%s WHERE Aadharcard_no=%s"
			val=(newval,Aadhar_no)
			cur.execute(query,val)
			con.commit()
		elif(ch==3):
			newval=input("Enter new sex")
			query="UPDATE Personal_details SET Sex=%s WHERE Aadharcard_no=%s"
			val=(newval,Aadhar_no)
			cur.execute(query,val)
			con.commit()
		elif(ch==4):
			newval=input("Enter new DOB")
			query="UPDATE Personal_details SET DOB=%s WHERE Aadharcard_no=%s"
			val=(newval,Aadhar_no)
			cur.execute(query,val)
			con.commit()
		elif(ch==5):
			newval=input("Enter new landsize")
			query="UPDATE Personal_details SET landsize=%s WHERE Aadharcard_no=%s"
			val=(newval,Aadhar_no)
			cur.execute(query,val)
			con.commit()
		elif(ch==6):
			newval=input("Enter new village_id")
			query="UPDATE Farmer SET village_id=%s WHERE F_Aadhar_no=%s"
			val=(newval,Aadhar_no)
			cur.execute(query,val)
			con.commit()
		elif(ch==7):
			newval=input("Enter new scheme_id")
			query="UPDATE Farmer SET scheme_id=%s WHERE F_Aadhar_no=%s"
			val=(newval,Aadhar_no)
			cur.execute(query,val)
			con.commit()
		elif(ch==8):
			newval=input("Enter new Bankpassbook_no")
			query="UPDATE Farmer SET Bankpassbook_no=%s WHERE F_Aadhar_no=%s"
			val=(newval,Aadhar_no)
			cur.execute(query,val)
			con.commit()
		else:
			break


def update_details_buyer():
	Aadhar_no=int(input("Enter Aadharno to update buyer information  "))
	while (1):
		print("1. update fname")
		print("2. update lname")
		print("3. update sex")
		print("4. DOB")
		print("5. update market_id")
		print("6. update village_id")
		print("7. ok")
		ch = int(input("Enter the choice:  "))
		newval=""
		query=""
		if(ch==1):
			newval=input("Enter new fname")
			query="UPDATE Personal_details SET fname=%s WHERE Aadharcard_no=%s"
			val=(newval,Aadhar_no)
			cur.execute(query,val)
			con.commit()
		elif(ch==2):
			newval=input("Enter new lname")
			query="UPDATE Personal_details SET lname=%s WHERE Aadharcard_no=%s"
			val=(newval,Aadhar_no)
			cur.execute(query,val)
			con.commit()
		elif(ch==3):
			newval=input("Enter new sex")
			query="UPDATE Personal_details SET Sex=%s WHERE Aadharcard_no=%s"
			val=(newval,Aadhar_no)
			cur.execute(query,val)
			con.commit()
		elif(ch==4):
			newval=input("Enter new DOB")
			query="UPDATE Personal_details SET DOB=%s WHERE Aadharcard_no=%s"
			val=(newval,Aadhar_no)
			cur.execute(query,val)
			con.commit()
		elif(ch==5):
			newval=input("Enter new landsize")
			query="UPDATE Personal_details SET landsize=%s WHERE Aadharcard_no=%s"
			val=(newval,Aadhar_no)
			cur.execute(query,val)
			con.commit()
		elif(ch==6):
			newval=input("Enter new village_id")
			query="UPDATE Buyer SET village_id=%s WHERE B_Aadhar_no=%s"
			val=(newval,Aadhar_no)
			cur.execute(query,val)
			con.commit()
		elif(ch==7):
			newval=input("Enter market_id")
			query="UPDATE Buyer SET market_id=%s WHERE B_Aadhar_no=%s"
			val=(newval,Aadhar_no)
			cur.execute(query,val)
			con.commit()
		else:
			break


def Address():
	try:
		row={}
		print("Enter farmers address:")
		row["village_id"]=int(input("villag_id:"))
		row["village_name"]=input("village_name:")
		row["pincode"]=int(input("pincode:"))

		query="INSERT INTO Address(village_id,village_name,pincode) VALUES(%d,'%s',%d)" % (row["village_id"],row["village_name"],row["pincode"])
		print(query)
		cur.execute(query)
		con.commit()

		print("Inserted into database")
	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print(e)
		return

def village():
	try:
		row={}
		print("Enter village details:")
		row["village_id"]=int(input("village_id:"))
		row["no_of_farmers"]=int(input("no_of_farmers:"))
		row["agricultural_land"]=float(input("agricultural_land:"))

		query="INSERT INTO village(village_id,no_of_farmers,agricultural_land) VALUES(%d,%d,%f)" %(row["village_id"],row["no_of_farmers"],row["agricultural_land"])
		print(query)
		cur.execute(query)
		con.commit()
		print("Inserted into database")

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print(e)
	return

def add_scheme():
	try:
		print("Enter scheme details:")
		row={}
		row["scheme_id"]=int(input("enter scheme_id:  "))
		row["elgiblefarmers"]=input("list of elgiblefarmer ids")
		row["benefits"]=input("enter benefits: ")
		row["specification"]=input("specification: ")
		row["type"]=input("enter type:  ")

		query="INSERT INTO Scheme(scheme_id,elgiblefarmers,benefits,specification,type) VALUES(%d,'%s','%s','%s','%s')" %(row["scheme_id"],row["elgiblefarmers"],row["benefits"],row["specification"],row["type"])
		print(query)
		cur.execute(query)
		con.commit()
		print("Inserted into database")
	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print(e)

def add_market():
	try:
		row={}
		print("Enter market details:")
		row["market_id"]=int(input("market_id:"))
		row["pincode"]=int(input("pincode:"))
		row["state"]=input("state: ")
		row["market_name"]=input("Enter the market_name: ")
		row["country"]=input("country: ")
		row["village_name"]=input("village_name:")

		query="INSERT INTO Market(market_id,pincode,state,market_name,country,village_name) VALUES(%d,%d,'%s','%s','%s','%s')"%(row["market_id"],row["pincode"],row["state"],row["market_name"],row["country"],row["village_name"])
		print(query)
		cur.execute(query)
		con.commit()
		print("Inserted into database")
	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print(e)
        
	return

def add_loan():
	try:
		row={}
		print("Enter loan details:")
		row["loan_id"]=int(input("enter loan_id:"))
		row["bank_namevar"]=input("enter bank name: ")
		row["F_Aadharcard_no"]=int(input("Enter farmer adhar number: "))
		row["amount"]=float(input("Enter loan amount: "))
		row["rateofinterest"]=float(input("enter rateofinterest: "))
		row["banknumber"]=int(input("enter banknumber: "))
		query="INSERT INTO loan(loan_id,bank_namevar,F_Aadharcard_no,amount,rateofinterest,banknumber) VALUES(%d,'%s',%d,%f,%f,%d)" %(row["loan_id"],row["bank_namevar"],row["F_Aadharcard_no"],row["amount"],row["rateofinterest"],row["banknumber"])

		print(query)
		cur.execute(query)
		con.commit()
		print("Inserted into database")
	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print(e)


def average_profit():
	try:
		print("Farmer's average profit")
		query="select AVG(profit) FROM crop"
		cur.execute(query)
		print("Here..it is:)")
		myresult = cur.fetchall()
		for x in myresult:
  			print(x) 
	except Exception as e:
		con.rollback()
		print("Failed to show")
		print(e)

def view_farmers():
	try:
		res=[]
		print("All the info of farmers:)")
		query="select  F_Aadhar_no from Farmer"
		cur.execute(query)
		myresult = cur.fetchall()
		for x in myresult:
			l=[x]
			res.append(l)
		for x in res:
			query="SELECT village_id FROM Farmer WHERE F_Aadhar_no = %s"
			cur.execute(query,(x[0]['F_Aadhar_no'],))
			myresult=cur.fetchall()
			if(len(myresult)>0):
				x.append(myresult[0])

		for x in res:
			query="SELECT scheme_id FROM Farmer WHERE F_Aadhar_no = %s"
			cur.execute(query,(x[0]['F_Aadhar_no'],))
			myresult=cur.fetchall()
			if(len(myresult)>0):
				x.append(myresult[0])
		for x in res:
			query="SELECT fname FROM Personal_details WHERE Aadharcard_no = %s"
			cur.execute(query,(x[0]['F_Aadhar_no']))
			myresult=cur.fetchall()
			if(len(myresult)>0):
				x.append(myresult[0])
		for x in res:
			query="SELECT lname FROM Personal_details WHERE Aadharcard_no = %s"
			cur.execute(query,(x[0]['F_Aadhar_no']))
			myresult=cur.fetchall()
			if(len(myresult)>0):
				x.append(myresult[0])
		for x in res:
			query="SELECT Sex FROM Personal_details WHERE Aadharcard_no = %s"
			cur.execute(query,(x[0]['F_Aadhar_no']))
			myresult=cur.fetchall()
			if(len(myresult)>0):
				x.append(myresult[0])
		for x in res:
			query="SELECT landsize FROM Personal_details WHERE Aadharcard_no = %s"
			cur.execute(query,(x[0]['F_Aadhar_no']))
			myresult=cur.fetchall()
			if(len(myresult)>0):
				x.append(myresult[0])
		for x in res:
			query="SELECT DOB FROM Personal_details WHERE Aadharcard_no = %s"
			cur.execute(query,(x[0]['F_Aadhar_no']))
			myresult=cur.fetchall()
			if(len(myresult)>0):
				x.append(myresult[0])
		for x in res:
			query="SELECT loan_id FROM loan WHERE F_Aadharcard_no = %s"
			cur.execute(query,(x[0]['F_Aadhar_no']))
			myresult=cur.fetchall()
			if(len(myresult)>0):
				x.append(myresult[0])

		for x in res:
			print(x)
		
	except Exception as e:
		con.rollback()
		print("Failed to show")
		print(e)

def update_land():
	try:
		land_reg_num=int(input("Enter registration number of the land"))
		print("1.owner_adhar_num\n2.geographical_location\n3.landsize \n4.soil_type\n5.crops_grown_id\n")
		x=int(input("Enter your choice"))
		if(x==1):
			newval=int(input("Enter new owner_adhar_num"))
			query="UPDATE Land SET owner_adhar_num=%s WHERE Land_reg_num=%s"
			val=(newval,land_reg_num)
			cur.execute(query,val)
			con.commit()
		elif(x==2):
			newval=input("Enter new geographical_location")
			query="UPDATE Land SET geographical_location=%s WHERE Land_reg_num=%s"
			val=(newval,land_reg_num)
			cur.execute(query,val)
			con.commit()
		elif(x==3):
			newval=input("Enter new landsize")
			query="UPDATE Land SET landsize=%s WHERE Land_reg_num=%s"
			val=(newval,land_reg_num)
			cur.execute(query,val)
			con.commit()
		elif(x==4):
			newval=input("Enter new soil_type")
			query="UPDATE Land SET soil_type=%s WHERE Land_reg_num=%s"
			val=(newval,land_reg_num)
			cur.execute(query,val)
			con.commit()
		elif(x==5):
			newval=input("Enter new crops_grown_id")
			query="UPDATE Land SET crops_grown_id=%s WHERE Land_reg_num=%s"
			val=(newval,land_reg_num)
			cur.execute(query,val)
			con.commit()
		else:
			print("Enter a valid choice")
		print("Updated")

	except Exception as e:
		con.rollback()
		print("Failed to update")
		print(e)

def update_village():
	try:
		village_id=int(input("Enter village id"))
		print("1.no.of farmers , \n2.agricultural_land")
		x=int(input("Enter your choice"))
		if(x==1):
			newval=input("Enter new no_of_farmers")
			query="UPDATE village SET no_of_farmers=%s WHERE village_id=%s"
			val=(newval,village_id)
			cur.execute(query,val)
			con.commit()
			print("Updated")
		elif(x==1):
			newval=input("Enter new agricultural_land")
			query="UPDATE village SET agricultural_land=%s WHERE village_id=%s"
			val=(newval,village_id)
			cur.execute(query,val)
			con.commit()
			print("Updated")
		else:
			print("Please enter a valid choice")
		

	except Exception as e:
		con.rollback()
		print("Failed to update")
		print(e)


def queries_loan():
	try:
		print("1. avg of farmers loan amount")
		print("2. min of farmers loan amount")
		print("3. max of farmers loan amount")
		print("4. sum of farmers loan amount")
		print("5. no.of farmers took loan ")
		print("6. avg of farmers loan interest")
		print("7. min of farmers loan interest")
		print("8. max of farmers loan interest")
		print("9. sum of farmers loan interest")
		print("10. farmers details whose loan satisfies a condition")
		print("11. farmers details whose rate ofinterest satisfies a condition")
		x=int(input("Enter your choice->  "))
		query=""
		if(x<10):
			if(x==1):
				query="SELECT AVG(amount) FROM loan"
			elif(x==2):
				query="SELECT MIN(amount) FROM loan"
			elif(x==3):
				query="SELECT MAX(amount) FROM loan"
			elif(x==4):
				query="SELECT SUM(amount) FROM loan"
			elif(x==5):
				query="SELECT COUNT(amount) FROM loan"
			elif(x==6):
				query="SELECT AVG(rateofinterest) FROM loan"
			elif(x==7):
				query="SELECT MIN(rateofinterest) FROM loan"
			elif(x==8):
				query="SELECT MAX(rateofinterest) FROM loan"
			elif(x==9):
				query="SELECT SUM(rateofinterest) FROM loan"
			cur.execute(query)
			res=cur.fetchall()
			for i in res:
				print(i)
		elif(x==10):
			val=()
			print("1.=\n2.>\n3.<\n4.>=\n5.<=\n6.not equal to\n7.in between a range")
			y=int(input("Enter your query choice"))
			if(y==1):
				inp=float(input("Enter amount: "))
				query="SELECT * FROM loan WHERE amount = %s"
				val=(inp,)
			elif(y==2):
				inp=float(input("Enter amount: "))
				query="SELECT * FROM loan WHERE amount > %s"
				val=(inp,)
			elif(y==3):
				inp=float(input("Enter amount: "))
				query="SELECT * FROM loan WHERE amount < %s"
				val=(inp,)
			elif(y==4):
				inp=float(input("Enter amount: "))
				query="SELECT * FROM loan WHERE amount >= %s"
				val=(inp,)
			elif(y==5):
				inp=float(input("Enter amount: "))
				query="SELECT * FROM loan WHERE amount <= %s"
				val=(inp,)
			elif(y==6):
				inp=float(input("Enter amount: "))
				query="SELECT * FROM loan WHERE amount <> %s"
				val=(inp,)
			elif(y==7):
				inp1=float(input("Enter starting amount: "))
				inp2=float(input("Enter ending amount: "))
				query="SELECT * FROM loan WHERE amount BETWEEN %s AND %s"
				val=(inp1,inp2)
			cur.execute(query,val)
			res=cur.fetchall()
			for i in res:
				print(i)
		elif(x==11):
			val=()
			print("1.=\n2.>\n3.<\n4.>=\n5.<=\n6.not equal to\n7.in between a range")
			y=int(input("Enter your query choice"))
			if(y==1):
				inp=float(input("Enter rateofinterest value: "))
				query="SELECT * FROM loan WHERE rateofinterest = %s"
				val=(inp,)
			elif(y==2):
				inp=float(input("Enter rateofinterest value: "))
				query="SELECT * FROM loan WHERE rateofinterest > %s"
				val=(inp,)
			elif(y==3):
				inp=float(input("Enter rateofinterest value: "))
				query="SELECT * FROM loan WHERE rateofinterest < %s"
				val=(inp,)
			elif(y==4):
				inp=float(input("Enter rateofinterest value: "))
				query="SELECT * FROM loan WHERE rateofinterest >= %s"
				val=(inp,)
			elif(y==5):
				inp=float(input("Enter rateofinterest value: "))
				query="SELECT * FROM loan WHERE rateofinterest <= %s"
				val=(inp,)
			elif(y==6):
				inp=float(input("Enter rateofinterest value: "))
				query="SELECT * FROM loan WHERE rateofinterest <> %s"
				val=(inp,)
			elif(y==7):
				inp1=float(input("Enter starting rateofinterest: "))
				inp2=float(input("Enter ending rateofinterest: "))
				query="SELECT * FROM loan WHERE rateofinterest BETWEEN %s AND %s"
				val=(inp1,inp2)
			cur.execute(query,val)
			res=cur.fetchall()
			for i in res:
				print(i)


	except Exception as e:
		con.rollback()
		print("Failed to execute")
		print(e)

def search():
	try:
		print("1.search persons name")
		ch=1;
		if(ch==1):
			way=input("enter word to search: ")
			query = "SELECT * FROM Personal_details WHERE fname LIKE %s"
			cur.execute(query,('%'+ way + '%',))
			myresult = cur.fetchall()

			for x in myresult:
				print(x)
	except Exception as e:
		con.rollback()
		print("Failed to show")
		print(e) 


def dispatch(ch):
	if(ch==1):
		details_framer()
	elif(ch==2):
		details_buyer()
	elif(ch==3):
		delete_farmer()
	elif(ch==4):
		register_land()
	elif(ch==5):
		delete_buyer()
	elif(ch==6):
		update_details_farmer()
	elif(ch==7):
		village()
	elif(ch==8):
		Address()
	elif(ch==9):
		add_scheme()
	elif(ch==10):
		add_market()
	elif(ch==11):
		add_loan()
	elif(ch==12):
		average_profit()
	elif(ch==13):
		view_farmers()
	elif(ch==14):
		update_land()
	elif(ch==15):
		update_village()
	elif(ch==16):
		queries_loan()
	elif(ch==17):
		search()
	else:
		print("Invalid option")

f=1
while(f==1):
	print("Welcome..!")
	print("--------------")
	print("Dreamkillers")
	print("2019101098")
	print("2019101102")
	print("2019101100")
	print("--------------")
	username = input("Username: ")
	password = input("Password: ")
	tmp=sp.call('clear',shell=True)
	try:
		#con = pymysql.connect(host='localhost',user='root',db='AGRICULTURE',cursorclass=pymysql.cursors.DictCursor)
		con = pymysql.connect(host='127.0.0.1',
                              user=username,
                              password=password,
                              port=5005,
                              db='AGRICULTURE',
                              cursorclass=pymysql.cursors.DictCursor)
		tmp=sp.call('clear',shell=True)
		if(con.open):
			print("Connected")
		else:
			print("Failed to connect")
		tmp=sp.call('clear',shell=True)

		tmp = input("Enter any key to CONTINUE-> ")
		with con.cursor() as cur:
			while (1):
				tmp=sp.call('clear',shell=True)
				print("1. insert farmer details")
				print("2. insert Buyer details")
				print("3. delete farmer details")
				print("4. insert land details")
				print("5. delete buyer details")
				print("6. update details of farmer")
				print("7. insert details of village")
				print("8. add address")
				print("9. add scheme")
				print("10. add market")
				print("11. add new loan")
				print("12. view average profit of farmer")
				print("13. view farmer's info")
				print("14. update land details")
				print("15. update village details")
				print("16. queries(min,..) in farmers loan")
				print("17.  search persons name ")
				print("18.logout")
				ch=int(input("Enter your choice-> "))
				if(ch==18):
					f=0
					break
				else:
					dispatch(ch)
					tmp = input("Enter any key to CONTINUE-> ")
	except:
		tmp=sp.call('clear',shell=True)
		print("Connection Refused.")
		tmp = input("Enter any key to CONTINUE-> ")
print("Thanks for visiting..!\n Bye:)")
