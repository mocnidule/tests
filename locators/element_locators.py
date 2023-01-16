# APP
solflare = '//p[contains(text(),"Solflare")]'
request_airdrop_button = '//button[contains(text(),"Airdrop")]'
amount_input = '//input[@id="recipients.0.depositedAmount"]'
title_input = '//input[@id="recipients.0.name"]'
recipient_input = '//input[@id="recipients.0.recipient"]'
create_button = '//button[contains(text(),"Create Vesting Contract")]'
create_multisig_payment_proposal_button = '//button[contains(text(),"Propose Streaming Contract")]'
release_frequency = 'releaseFrequencyCounter'
release_frequency_picker = 'releaseFrequencyPeriod'
second = '//option[@value="1"]'
minute = '//option[@value="60"]'
hour = '//option[@value="3600"]'
day = '//option[@value="86400"]'
week = '//option[@value="604800"]'
month = '//option[@value="2628002"]'
year = '//option[@value="31536000"]'
start_date_input = 'startDate'
end_date_input = 'endDate'
start_time_input = 'startTime'
end_time_input = 'endTime'
alert_close_button = '//*[@fill-rule="evenodd"]'
reject_button = '//*[contains(text(),"REJECT")]'
cancel_button = '(//button[contains(text(),"Cancel")])[3]'
transfer_button = '(//button[contains(text(),"Transfer")])[1]'
canceled_card = '//span[contains(text(),"canceled")]'
recipient_can_transfer_checkbox = 'recipientCanTransfer'
recipient_can_cancel_checkbox = 'recipientCanCancel'
sender_can_cancel_checkbox = 'senderCanCancel'
sender_can_transfer_checkbox = 'senderCanTransfer'
advanced_toggle = '(//button[@role="switch"])[4]'
transfer_recipient_address_field = '(//input[@placeholder="Recipient address"])[1]'
withdraw_button = '(//button[contains(text(),"Withdraw")])[1]'
top_up_button = '(//button[contains(text(),"Top Up")])[1]'
confirm_top_up_button = '(//button[contains(text(),"Top Up")])[2]'
cliff_date_input = 'cliffDate'
cliff_time_input = 'cliffTime'
cliff_percentage_input = 'cliffAmount'
no_streams_in_the_past_alert = '//p[contains(text(),"Cannot start stream in the past.")]'
no_negative_amount_alert = '//p[contains(text(),"Please provide amount greater than 0.")]'
not_enough_tokens_alert = '//p[contains(text(),"have enough tokens.")]'
cliff_should_happen_after_start_alert = '//p[contains(text(),"Cliff should happen after start.")]'
view_on_explorer_button = '//a[contains(text(),"View on explorer")]'
wallet_connected_alert = '//*[contains(text(),"Wallet connected!")]'
wallet_not_connected_alert = '//*[contains(text(),"Wallet not connected!")]'
transaction_canceled_alert = '//*[contains(text(),"Transaction cancelled")]'
transaction_confirmed_alert = '//*[contains(text(),"Transaction confirmed!")]'
cant_transfer_stream_to_yourself_alert = '//*[contains(text(),"transfer stream to yourself.")]'
amount_is_required_alert = '//p[contains(text(),"Amount is required.")]'
please_provide_title_alert = '//p[contains(text(),"Please provide a subject (title).")]'
chose_recipient_alert = '//p[contains(text(),"You must choose a recipient.")]'
failed_to_send_transaction_alert = '//*[contains(text(),"failed to send transaction")]'
withdraw_amount_input_field = '(//input[@type="number" and contains(@class,"py-1.5")])[1]'
top_up_amount_input_field = '(//input[@type="number" and contains(@class,"py-1.5")])[2]'
deposited_amount_input_field = 'recipients.0.depositedAmount'
release_amount_input_field = 'releaseAmount'
payment_tab = '(//a[contains(text(),"New Payment")])[1]'
vesting_tab = '(//a[contains(text(),"New Vesting")])[1]'
dev_toggle = '//button[@role="switch"]'
submit_password = '//*[contains(text(),"Submit")]'
auto_withdrawal = '//button[@role="switch"]'
dropdown_button = '//button[contains(@class,"h-12")]'
outgoing_page = '//button[contains(text(),"Outgoing")]'
incoming_page = '//button[contains(text(),"Incoming")]'
all_streams_page = '//button[contains(text(),"All Streams")]'
who_can_transfer_vesting = '//select[@data-testid="vesting-who-can-transfer"]'
who_can_cancel_vesting = '//select[@data-testid="vesting-who-can-cancel"]'
both_can_cancel = '(//option[@value="both"])[2]'
both_can_transfer = '(//option[@value="both"])[1]'
none_can_transfer = '(//option[@value="neither"])[1]'
none_can_cancel = '(//option[@value="neither"])[2]'
more_options_contract = '(((//p[contains(text(), "TestIo")]/parent::div/parent::div)[2]//button)[2])'
stream_payment_button = '//button[contains(text(),"Create Streaming Contract")]'
transfer_address_input = '//input[@placeholder="Recipient address"]'
confirm_transfer_button = '//input[@value="HG4sYqvkTfgBvGgZZhYfws4f8BoytTr1NmcDEwkKC2z8"]/following-sibling::div' \
                          '//button[2] '
confirm_transfer_sender = '//input[@value="57TCgyLw4pT48A1z5fWwQ9eUWuwfpo2izzYcWVRiqEnP"]/following-sibling::div' \
                          '//button[2] '
confirm_transfer_recipient = '//input[@value="954fBxNr25X31DbvMkw2ta5KBjkxmMUSFHeUHuXA1VqD"]/following-sibling::div' \
                             '//button[2] '
confirm_withdraw_button = '//p[contains(text(), "You can withdraw between 0")]/parent::div//button[2]'
recipient_email_input = 'recipients.0.recipientEmail'
add_recipient = '//button[contains(text(), "+ Add Recipient")]'
status_filter = '(//select[@id="filter"])[1]'
types_filter = '(//select[@id="filter"])[2]'
directions_filter = '(//select[@id="filter"])[3]'
search_contracts_input_field = '//input[@id="globalSearch"]'
email_sent_alert = '//*[contains(text(),"Notification sent.")]'
email_failed_alert = '//*[contains(text(),"Sending notifications failed.")]'
multi_sig_page = '(//button[contains(text(),"Multisig Wallet")])[1]'
new_multi_sig_wallet = '//button[contains(text(),"New Multisig Wallet")]'
wallet_name = 'walletName'
add_member = '//div[contains(text(), "+ Add Member")]'
member_one = 'members.0'
member_two = 'members.1'
member_three = 'members.2'
member_four = 'members.3'
member_five = 'members.4'
create_multi_sig_wallet_button = '//button[contains(text(),"Create Multisig Wallet")]'
referral_input_field = '//input[@id="referral"]'
approve_button_multi_sig = '//button[contains(text(),"Approve")]'
pending_proposals_switch = '//button[@role="switch"]'
proposals_tab = '//button[contains(text(),"Proposals")]'
streams_tab_in_multi_sig = '(//button[contains(text(),"Streams")])[2]'
multi_sig_wallet = '//div[contains(text(),"4QaarZkC…6vxYUCUr")]'
spinner = '//div[@class="loader"]'
new_payment_button = '//button[contains(text(),"New Payment")]'
new_proposal_button = '//button[contains(text(),"New Proposal")]'
vesting_payment = '//a[contains(text(),"Vesting payment")]'
vesting_proposal = '//a[contains(text(),"Vesting proposal")]'
stream_payment = '//a[contains(text(),"Stream payment")]'
stream_proposal = '//a[contains(text(),"Stream proposal")]'
withdraw_modal_multi_sig = '//button[contains(text(),"Withdraw")]'

# SOLFLARE WEB WALLET

create_new_wallet_button = '//*[contains(text(),"I NEED A NEW WALLET")]'
already_have_wallet_button = '//*[contains(text(),"I ALREADY HAVE A WALLET")]'
advanced_button = '//*[contains(text(),"Advanced")]'
quick_setup = '//*[contains(text(),"Quick setup")]'
skip_button = '//span[contains(text(),"Skip")]'
wrote_down_mnemonic_button = '//*[contains(text(),"I SAVED MY RECOVERY PHRASE")]'
verify_button = '//span[contains(text(),"Verify")]'
allow_button = '//span[contains(text(),"Allow")]'
allow_button_capital = '//span[contains(text(),"ALLOW")]'
next_step_button = '//span[contains(text(),"Next step")]'
close_button = '//span[contains(text(),"Close")]'
copy_mnemonic_button = '//*[contains(text(),"Copy")]'
access_button = '//span[contains(text(),"Access")]'
mnemonic_input = '//input[@id="mnemonic-input-0"]'
mnemonic_input_reconnect = '// textarea[1]'
field_set = '//*[@aria-haspopup="listbox"]'
select_right_wallet = '(//div[contains(@class, "MuiListItemText-multiline")])[2]'
continue_button = '//*[contains(text(),"Continue")]'
phase_12 = '//button[contains(text(),"12")]'
mnemonic_1 = '//input[@id="mnemonic-input-0"]'
mnemonic_2 = '//input[@id="mnemonic-input-1"]'
mnemonic_3 = '//input[@id="mnemonic-input-2"]'
mnemonic_4 = '//input[@id="mnemonic-input-3"]'
mnemonic_5 = '//input[@id="mnemonic-input-4"]'
mnemonic_6 = '//input[@id="mnemonic-input-5"]'
mnemonic_7 = '//input[@id="mnemonic-input-6"]'
mnemonic_8 = '//input[@id="mnemonic-input-7"]'
mnemonic_9 = '//input[@id="mnemonic-input-8"]'
mnemonic_10 = '//input[@id="mnemonic-input-9"]'
mnemonic_11 = '//input[@id="mnemonic-input-10"]'
mnemonic_12 = '//input[@id="mnemonic-input-11"]'
password = '//input[@name="password"]'
repeat_password = '//input[@name="password2"]'
connect_button = '//*[contains(text(),"Connect")]'
import_all_button = '//*[contains(text(),"Import all")]'
menu_button = '//button[@id="headlessui-menu-button-1"]'
disconnect_wallet = '//span[contains(text(),"Disconnect Wallet")]'
solflare_settings_button = '//*[@data-icon="gear"]'
main_account_button = '(//div[@role="button"])[1]'
add_new_account_button = '//span[contains(text(),"Add a new account")]'
pick_recipient_wallet = '(//span[@data-id="mnemonic_account_checkbox"])[2]'
save_button = '//button[@data-id="save_button"]'
menu_var = '(//button)[1]'
approve_button = '//*[contains(text(),"APPROVE")]'
dashboard_tab = '//button[contains(text(),"Home")]'
wallet_connect = '//button[contains(text(),"Web wallet")]'
new_stream_button = '//button[contains(text(),"New Stream")]'
create_stream_button = '//button[contains(text(),"Create stream")]'
