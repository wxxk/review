# def 함수 호출 / 함수명
def open_acoount():
    # 함수에서 실행되는 내용 작성
    print("새로운 계좌가 생산되었습니다.")
    # 정의만 해두지 호출하기 전까지 실행되지 않음



# 값을 전달하는 함수
def deposit(balance, money): # 입금
    print("입급이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balace, money) : # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balace))
        return balace

def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print('수수료는 {0} 원이며, 잔액은 {1} 원 입니다.'.format(commission, balance))
