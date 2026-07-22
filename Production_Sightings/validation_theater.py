"""ANONYMIZED SIGHTING #3
Reported location: a data pipeline that has processed several
million real rows using this exact function."""

def is_valid_email(email):
    # "validation"
    try:
        assert "@" in email
        return True
    except:
        return False

print(is_valid_email("not-an-email-at-all@"))  # True. it has an @. that's the whole check.
print(is_valid_email(None))                     # False, but only because `in` raised TypeError
