"""Payment of Credit Card Balances using Bisection-Search w/ Data Visualization""""

import pandas as pd
import matplotlib.pyplot as plt

def credit_card(df, n, balance, annualInterestRate, fixedPayment):
  
  def operations(balance, annualInterestRate, fixedPayment):
      unpaidBal = balance - fixedPayment
      interestPay = unpaidBal * annualInterestRate/12
      balance = unpaidBal + interestPay
      return balance, fixedPayment, unpaidBal, interestPay, 
    
  if n == 12:
    attributes = operations(balance, annualInterestRate, fixedPayment)
    df_rec = pd.DataFrame([[balance, attributes[1], attributes[2], attributes[3]]], columns=["Balance", "Fixed_Payment", "Unpaid_Balance", "Interest_Pays"])
    df = df.append(df_rec, ignore_index=True)

    return attributes[0], df 
  
  else:

    attributes = operations(balance, annualInterestRate, fixedPayment)
    df_rec = pd.DataFrame([[balance, attributes[1], attributes[2], attributes[3]]], columns=["Balance", "Fixed_Payment", "Unpaid_Balance", "Interest_Pays"])
    df = df.append(df_rec, ignore_index=True)

    return(credit_card(df, n+1, attributes[0], annualInterestRate, fixedPayment))
    
def b_search(lb, hb, fixedPayment, epsilon): 
  steps = 1
  prices = []
  balances_arr = []

  while True:
    df = pd.DataFrame()
    rem_bal = credit_card(df, 1, balance, annualInterestRate, fixedPayment)

    steps+=1
    prices.append(fixedPayment)
    balances_arr.append(rem_bal[0])


    if rem_bal[0] > 0:
      lb = fixedPayment
      fixedPayment = (lb + hb) / 2
    elif rem_bal[0] < 0 and abs(rem_bal[0]) > epsilon :
      hb = fixedPayment
      fixedPayment = (lb + hb) / 2
    else:
      return rem_bal, fixedPayment, steps, prices, balances_arr


balance = 1509795
annualInterestRate = 0.37

lb = balance / 12
hb =(balance * (1 + annualInterestRate/12) ** 12) / 12.0
fixedPayment = (lb + hb) / 2  
epsilon = 0.001

clean_df, final_pay, steps, final_pays_arr, rem_balance_arr  = b_search(lb, hb, fixedPayment, epsilon)
print("Lowest Payment: %.2f" %final_pay)
print("\n")
print("Clean Payments")
print(clean_df[1])
print("\n")
print("Iterations to get sufficient payment: %d" %steps)
print("\n")
print("Payments(via bisection)")
print(final_pays_arr)
print("\n")
#print(rem_balance_arr)

fig = plt.figure()

ax1 = plt.subplot2grid((2,1), (0,0), rowspan=1, colspan=1)

plt.title("Credit Card Balances-Payments", fontsize=19, color="#3f6379")
plt.xlabel("Remaining Balances", fontsize=14, color="#643022")
plt.ylabel("Payment($, USD)", fontsize=14, color="#643022")

ax2 = plt.subplot2grid((2,1), (1,0), rowspan=1, colspan=1)

plt.xlabel("Steps", fontsize=14, color="#643022")
plt.ylabel("Payment($, USD)", fontsize=14, color="#643022")

for i in range(len(rem_balance_arr)):
  ax1.scatter(rem_balance_arr[i], final_pays_arr[i], marker="X", label=i)
ax1.plot(rem_balance_arr, final_pays_arr, lw=0.5, ls=":", color="#31c1fa")

plt.ylim(lb, hb)

ax2.scatter([s for s in range(1, steps)], final_pays_arr, color="#ff6379", marker="X")
ax2.plot([s for s in range(1, steps)], final_pays_arr, lw=1.5, color="#ff6379")

ax2.text(0.425, 0.83,"Bisection-Search", transform=plt.gca().transAxes, fontdict=dict(size=18, color="#3f6379"))
ax2.annotate("upper-bound", xy=(0, hb-1000), xytext=(1.5, hb-8000), arrowprops=dict(facecolor = "green"))
ax2.annotate("lower-bound", xy=(0, lb+1000), xytext=(1.5, lb+8000), arrowprops=dict(facecolor = "green"))


plt.ylim(lb, hb)
plt.xticks([5, 10, 15, 20, 25])

ax1.grid(True)
ax2.grid(True)

plt.subplots_adjust(hspace=0.4)
ax1.legend(loc=3, ncol=4, fontsize=8.5).get_frame().set_alpha(0.6)

plt.show()
