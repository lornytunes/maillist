import csv

from collections import Counter
from operator import itemgetter
from concurrent import futures


def get_email_counts(source):
    return Counter([l.strip().lower() for l in source.readlines()])


def process_one(item, validators):
    """Validates each email address.

    Some of these validation tests require network lookup so could block.
    """
    validator_results = [None for validator in validators]
    for i, validator in enumerate(validators):
        is_valid = validator().is_valid(item[0])
        validator_results[i] = is_valid and 'Y' or 'N'
        if not is_valid:
            # validation has failed - no need to try anymore
            break
    return item + tuple(validator_results)


def process_all(email_counts, writer, validators):
    for item in sorted(email_counts.items(), key=itemgetter(0)):
        writer.writerow(process_one(item, validators))


def process_all_concurrently(email_counts, writer, validators, max_workers):
    workers = min(max_workers, len(email_counts))
    with futures.ThreadPoolExecutor(workers) as executor:
        to_do = []
        for item in email_counts.items():
            future = executor.submit(process_one, item, validators)
            to_do.append(future)
        for future in futures.as_completed(to_do):
            writer.writerow(future.result())


def process(input, output, validators, max_workers=20):
    writer = csv.writer(output)
    headers = ['Email', 'Count']
    email_counts = get_email_counts(input)
    if validators:
        headers.extend([v.colname() for v in validators])
    writer.writerow(headers)
    if validators:
        # validate each email address
        process_all_concurrently(email_counts, writer, validators, max_workers)
    else:
        # no validation takes place - just print out the counts
        for item in sorted(email_counts.items(), key=itemgetter(0)):
            writer.writerow(item)
    return len(email_counts)
