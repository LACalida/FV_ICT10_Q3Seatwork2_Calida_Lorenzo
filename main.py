from pyscript import document

def teamshow(event=None):
    section = document.getElementById("sec-select").value
    teaminfo = document.getElementById("teaminfo")
    logo = document.getElementById("teamlogo")

    registration = document.querySelector('input[name="registration"]:checked')
    clinic = document.querySelector('input[name="clinic"]:checked')

    # reset logo every click
    logo.classList.add("d-none")
    logo.src = ""

    # check if all questions are answered
    if registration is None or clinic is None:
        teaminfo.innerText = "Please answer all questions first."
        return

    # if any answer is NO
    if registration.value == "no" or clinic.value == "no":
        teaminfo.innerText = (
            "You cannot find out your team yet.\n"
            "If you have not completed your registration form or clinic clearance, please do so first."
        )
        return

    # show team + logo
    if section == "7E":
        teaminfo.innerText = "Team: Blue Bears"
        logo.src = "bluebears.png"

    elif section == "7R":
        teaminfo.innerText = "Team: Yellow Tigers"
        logo.src = "yellowtigers.png"

    elif section == "7S":
        teaminfo.innerText = "Team: Red Bulldogs"
        logo.src = "redbulldogs.png"

    elif section == "7T":
        teaminfo.innerText = "Team: Green Hornets"
        logo.src = "greenhornets.png"

    elif section == "8E":
        teaminfo.innerText = "Team: Yellow Tigers"
        logo.src = "yellowtigers.png"

    elif section == "8R":
        teaminfo.innerText = "Team: Red Bulldogs"
        logo.src = "redbulldogs.png"

    elif section == "8S":
        teaminfo.innerText = "Team: Green Hornets"
        logo.src = "greenhornets.png"

    elif section == "8J":
        teaminfo.innerText = "Team: Blue Bears"
        logo.src = "bluebears.png"

    elif section == "8T":
        teaminfo.innerText = "Team: Blue Bears"
        logo.src = "bluebears.png"

    elif section == "9E":
        teaminfo.innerText = "Team: Green Hornets"
        logo.src = "greenhornets.png"

    elif section == "9R":
        teaminfo.innerText = "Team: Blue Bears"
        logo.src = "bluebears.png"

    elif section == "9J":
        teaminfo.innerText = "Team: Green Hornets"
        logo.src = "greenhornets.png"

    elif section == "9S":
        teaminfo.innerText = "Team: Yellow Tigers"
        logo.src = "yellowtigers.png"

    elif section == "9T":
        teaminfo.innerText = "Team: Red Bulldogs"
        logo.src = "redbulldogs.png"

    elif section == "10E":
        teaminfo.innerText = "Team: Red Bulldogs"
        logo.src = "redbulldogs.png"

    elif section == "10R":
        teaminfo.innerText = "Team: Green Hornets"
        logo.src = "greenhornets.png"

    elif section == "10S":
        teaminfo.innerText = "Team: Yellow Tigers"
        logo.src = "yellowtigers.png"

    elif section == "10T":
        teaminfo.innerText = "Team: Blue Bears"
        logo.src = "bluebears.png"

    elif section == "11A":
        teaminfo.innerText = "Team: Green Hornets"
        logo.src = "greenhornets.png"

    elif section == "11L":
        teaminfo.innerText = "Team: Yellow Tigers"
        logo.src = "yellowtigers.png"

    elif section == "12J":
        teaminfo.innerText = "Team: Blue Bears"
        logo.src = "bluebears.png"

    elif section == "12T":
        teaminfo.innerText = "Team: Red Bulldogs"
        logo.src = "redbulldogs.png"

    # finally show the logo
    logo.classList.remove("d-none")
