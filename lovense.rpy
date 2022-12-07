init python:
    def download_qr_code():
        try:
            response = requests.post("http://192.168.0.136:8443/api/v1/lovense/qrCode", json={"uid": str(persistent.uuid), "uname": store.name})
            json_content = response.json()

            with open(os.path.join(config.gamedir, "lovense_qr_code.jpg"), "wb") as f:
                f.write(requests.get(json_content["data"]["qr"]).content)
        except requests.exceptions.RequestException:
            persistent.lovense_https_port = "Server Error"
            persistent.lovense_local_ip = "Server Error"

        return "lovense_qr_code.jpg"

    def set_lovense_user():
        global lovense_user_set

        try:
            response = requests.get(f"http://192.168.0.136:8443/api/v1/lovense/users/{persistent.uuid}")
            lovense_user = response.json()
        except requests.exceptions.RequestException:
            persistent.lovense_https_port = "Server Error"
            persistent.lovense_local_ip = "Server Error"
        except JSONDecodeError:
            return
        
        persistent.lovense_https_port = lovense_user["httpsPort"]
        persistent.lovense_local_ip = lovense_user["domain"]


default persistent.lovense_local_ip = ""
default persistent.lovense_https_port = ""

screen connect_lovense():
    tag lovense
    predict False

    default image_path = "lovense/images/"

    add image_path + "background.webp"

    imagebutton:
        idle "return_button_idle"
        hover "return_button_hover"
        action Hide()

    text "Connect to Lovense App" xalign 0.5 ypos 50 style "montserrat_extra_bold_64"

    hbox:
        align (0.5, 1.0)
        spacing 100

        # Game Mode
        vbox:
            align (0.5, 1.0)
            yoffset -200
            spacing 10

            add "lovense/images/game_mode_example.webp" xalign 0.5

            null height 30
            
            button:
                idle_background "blue_button_idle"
                hover_background "blue_button_hover"
                action ui.callsinnewcontext("lovense_connect_via_game_mode")
                padding (40, 25)
                align (0.5, 0.5)
                
                text "Connect With Game Mode" align (0.5, 0.5)

            text "No connection to external servers (LAN Only)" align (0.5, 0.5)

        # QR Code
        vbox:
            align (0.5, 1.0)
            yoffset -200
            spacing 10

            add download_qr_code() xalign 0.5

            null height 30

            button:
                idle_background "blue_button_idle"
                hover_background "blue_button_hover"
                action ui.callsinnewcontext("lovense_connect_via_qr_code")
                padding (40, 25)
                xalign 0.5
                
                text "Connect With QR Code" align (0.5, 0.5)

            text "Requires connection to Lovense Server"

    vbox:
        align (0.5, 1.0)
        yoffset -50
        spacing 10

        text "Local IP: {}".format(persistent.lovense_local_ip)
        text "HTTPS Port: {}".format(persistent.lovense_https_port)

    timer 3 action Function(set_lovense_user) repeat True

image lovense_remote_download = "lovense/images/lovense_remote_download.webp"
image lovense_remote_profile = "lovense/images/lovense_remote_profile.webp"
image lovense_remote_game_mode = "lovense/images/lovense_remote_game_mode.webp"
image lovense_input_local_ip = "lovense/images/input_local_ip.webp"
image lovense_input_http_port = "lovense/images/input_http_port.webp"

image lovense_plus_view = "lovense/images/lovense_remote_plus_button.webp"
image lovense_scan_qr = "lovense/images/lovense_remote_scan_qr.webp"


label lovense_connect_via_game_mode:
    show black

    show lovense_remote_download
    "1. Download the Lovense Remote App (Compatibile: iOS, Android and Desktop)"
    hide lovense_remote_download

    show lovense_remote_profile
    "2. Head to the \"Me\" view"
    hide lovense_remote_profile

    show lovense_remote_game_mode
    "3. Select \"Settings\" and turn on \"Game Mode\""
    hide lovense_remote_game_mode

    show lovense_input_local_ip
    $ persistent.lovense_local_ip = renpy.input("4. Enter Local IP", allow="0123456789.")
    hide lovense_input_local_ip

    show lovense_input_http_port
    $ persistent.lovense_https_port = renpy.input("5. Enter SSL Port", allow="0123456789.")
    hide lovense_input_http_port

    return

label lovense_connect_via_qr_code:
    show black

    show lovense_remote_download
    "1. Download the Lovense Remote App (Compatibile: iOS, Android and Desktop)"
    hide lovense_remote_download

    show lovense_plus_view
    "2. Click on the \"+\" icon"
    hide lovense_plus_view

    show lovense_scan_qr
    "3. Select \"Scan QR\""
    hide lovense_scan_qr

    $ download_qr_code()

    show expression "lovense_qr_code.jpg" at truecenter
    "4. Scan the above QR code to connect"
    hide expression "lovense_qr_code.jpg" at truecenter

    return