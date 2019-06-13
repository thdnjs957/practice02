# 1)다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 중복
# 없이 각 단어를 순서대로 출력하세요.

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

lists = s.replace(',', '').replace('.', '').upper()
print(lists)
result = s.split(' ')

rm_dupli_result = set(result) # 중복 제거
print(rm_dupli_result)

for final_result in rm_dupli_result:
    print("{0}:{1}".format(final_result, final_result.count(final_result)))
