"""ANONYMIZED SIGHTING #1
Reported location: a payments microservice.
The comment was already there when the reporter found it.
The bug it "fixes" was never diagnosed. The sleep was never removed."""

import time

def process_payment(payment_id):
    result = _charge_card(payment_id)
    time.sleep(1)  # TODO: figure out why this is needed. do not remove, breaks prod.
    return result

def _charge_card(payment_id):
    return {"payment_id": payment_id, "status": "charged"}

print(process_payment("pay_123"))
