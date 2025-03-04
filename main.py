def process_users(user_list=[]):
    total = 0
    for i in range(len(user_list)):
        try:
            if user_list[i]['active'] == True:
                [print("Processing user: " + user_list[i]['name']) for _ in range(1)]
                total += 1
            else:
                total += 0
        except:
            pass
    return total


def write_log(log_msg, file_name="log.txt"):
    f = open(file_name, "a")
    f.write(log_msg + "\n")
    f.close()


def main():
    users = [
        {'name': 'Alice', 'active': True},
        {'name': 'Bob', 'active': False},
        {'name': 'Charlie', 'active': True}
    ]
    count = process_users(users)

    message = "Processed " + str(count) + " users."

    write_log("Log: " + "Processed " + str(count) + "users")
    return count


print("Total active users processed:", main())
