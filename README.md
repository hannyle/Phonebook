Phonebook project

Task is to implement a phone book manager.

 - Queries
 
It should be able to process 3 types of queries:

• Add number name.

It means that the user adds a person with name name and phone number number to the phone book. If there exists a user with such number already,
then your manager has to add the new number to the existing ones.

• Delete name.

It means that the manager should erase a person with name name from the phone book. If there is no such person, then it should just ignore the
query.

• Find name.

It means that the user looks for a person with name name. The manager should reply with the appropriate phone number, or with string “not found”
(without quotes) if there is no such person in the book. In case of multiple phone numbers for the same person, return the shortest one(You can just
compare the numbers like integers). Also, case matters. E.g. mom is not the same as Mom.

- Input Format

There is a single integer N in the first line — the number of queries. It’s followed
by N lines, each of them contains one query in the format described above.

- Constraints

1 <= N <= 10ˆ5 . All phone numbers consist of decimal digits, they don’t have leading zeros, and each of them has no more than 7 digits. All names are
non-empty strings of latin letters, and each of them has length at most 15. It’s guaranteed that there is no person with name “not found”.

- Output Format
Print the result of each find query — the phone number corresponding to the name or “not found” (without quotes) if there is no such person in the phonebook. Output one result per line in the same order as the find queries are given
in the input.

- Example:

• Input:

10

add 322 laundry

add 3410 school

add 311 laundry

del school

find laundry

find school

add 93035 dad

find dad

add 540 Mom

find mom

• Output:

311

not found

93035

not found
