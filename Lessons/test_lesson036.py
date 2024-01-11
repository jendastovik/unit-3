from lesson_036 import Account

def test_empty_account():
    new_account = Account()
    assert new_account.balance == 0
    assert new_account.holder_name == ""
    assert new_account.holder_email == ""
    number = new_account.number
    assert isinstance(number, list)
    acc_no = new_account.get_account_number().split("-")
    assert len(acc_no) == 3 and len(acc_no[0]) == 3 and len(acc_no[1]) == 5 and len(acc_no[2]) == 1


def test_create_account():
    new_account = Account()
    assert new_account.get_balance() == 0
    assert new_account.set_holder_name("John") == "Holder's name is John"
    assert new_account.set_holder_email("john@z.com") == "Holder's email is john@z.com"
    assert new_account.deposit(100) == "New balance: 100USD"

