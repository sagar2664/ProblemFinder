from .codeforce import codeforce
from .leetcode import leetcode
# Create your views here.

def searchCodeforce(query):
    result = codeforce(query)
    return result

def searchLeetcode(query):
    result = leetcode(query)
    return result

def searchAll(query):
    codeforce_result = codeforce(query)
    leetcode_result = leetcode(query)

    results = codeforce_result + leetcode_result
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return results
