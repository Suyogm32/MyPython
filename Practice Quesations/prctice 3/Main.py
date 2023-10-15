from Customers import Customer
from Item import Items
from Ratings import Ratings
customer_list=[]
item_list=[]
rate_list=[]
def main():

    num_of_cust=int(input("Enter the number of Customers"))
    for i in range(num_of_cust):
        cid=int(input("Enter the Customer ID"))
        cname=input("Enter the Customer Name")
        cnum=input("Enter the Custome Phone number")
        cemail=input("Enter the customer email Id")
        obj=Customer(cid,cname,cnum,cemail)
        customer_list.append(obj)
    for obj in customer_list:
        print("Id-",obj.Id)
        print("name",obj.name)
        print("number",obj.number)
        print("Email",obj.email)

    num_of_items=int(input("Enter the number of items"))
    for i in range(num_of_items):
        itemId=int(input("Enter the ite Id"))
        itemName=input("Enter the item Name")
        itemDesc=input("Enter item Description")
        itemQty=input("Enter the item quantity")
        iobj=Items(itemId,itemName,itemDesc,itemQty)
        item_list.append(iobj)


    number_of_ratings=int(input("Enter the number of ratings"))
    for i in range(number_of_ratings):
        custId=int(input("Enter the Customer Id"))
        ItemId=int(input("Enter the item id"))
        ratingdesc=input("Enter the decription ")
        rate=int(input("Enter the rating out of 5"))
        rateobj=Ratings(custId,ItemId,ratingdesc,rate)
        rate_list.append(rateobj)



    # def find_fav_item(givenId):
    #     for obj in rate_list:
    #         dict
    #         if obj.custId==givenId:

if __name__=="__main__":
    main()




