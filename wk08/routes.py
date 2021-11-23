"""
ALPACA
"""

"""
Active / Offline / DnD status

See status of other members, and can also update their own status
- methods=['PUT']
"""

"""
BEAGLE
"""

"""
Adding friends

Adds a friend, given a token, u_id, option for only adding friends of friends, or everyone, etc

Errors:
- Invalid token
- u_id is invalid
- u_id is already friend
- u_id is on blacklist
- u_id does not meet the friends requirements

Inputs:
- Token
- u_id


"""
@APP.route(“/user/addfriend/v1”, methods=[“POST”])
def add_friend():
    data = request.get_json()
    token = data[“token”]
    u_id = data[“u_id”]
    add_friend_v1(token, u_id)
    return dumps({})

"""
CAMEL
"""

"""
Dice roll

Emulate sending a message, but with randomness
- Can specify a specific dice roll with max number
- Can be used when playing board games with group
- methods=['POST']
"""


"""
DODO
"""

"""
Kick 

Kicks someone out of the channel or dms

Errors:
- u_id is not part of the channel / dm

Inputs:
- Token
- u_id
- channel_id / dm_id

Return:
- {}

- methods=['DELETE']
"""

"""
EAGLE
"""


"""
Channel Ban

Bans u_id from the channel, 

Errors:
- Acccess error if auth_user doesn't have permissions

Inputs:
- token
- channel_id
- u_id


- methods=['POST']

"""