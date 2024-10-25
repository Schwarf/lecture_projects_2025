# Global variable
user_update_count = 0


def log_update(user):
    pass


def send_notification(user, param):
    pass


def update_user_profile(user, new_info):
    global user_update_count
    # Updates the user profile (expected behavior)
    user.update(new_info)

    # Unexpected side effects
    user_update_count += 1  # Modifies a global variable
    log_update(user)  # Logs update (side effect)
    send_notification(user, "Profile updated")  # Sends notification (side effect)



############################################################################################
# GOOD EXAMPLE

def update_user_profile(user, new_info):
    # Only updates user profile, with no hidden side effects
    user.update(new_info)

def increment_update_count(counter):
    counter += 1
    return counter

def log_and_notify(user):
    log_update(user)
    send_notification(user, "Profile updated")


def update_user_with_logging_and_notification(user, new_info):
    global user_update_count
    update_user_profile(user, new_info)
    user_update_count = increment_update_count(user_update_count)
    log_and_notify(user)
    return user_update_count