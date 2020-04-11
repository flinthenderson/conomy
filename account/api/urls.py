from account.api.views import (list_wallets,
                                update_wallet,
                                add_wallet,
                                delete_wallet,
                                get_wallet_by_id,
                                list_all_transactions,

                                add_transaction,
                                delete_transaction
                                )
from django.urls import path
app_name = 'account'
urlpatterns = [
  path('listwallets', list_wallets),
  path('get_wallet_by_id/<int:id>', get_wallet_by_id),
  path('addwallet', add_wallet),
  path('updatewallet/<int:id>', update_wallet),
  path('deletewallet/<int:id>', delete_wallet),

  path('listalltransactions', list_all_transactions),
  path('addtransactiontowallet', add_transaction),
  path('deletetransaction', delete_transaction),
]