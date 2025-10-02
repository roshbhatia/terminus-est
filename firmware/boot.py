"""
Boot configuration for Terminus Est keyboard
"""

import supervisor
import usb_hid
import storage

# Enable USB HID
usb_hid.enable(
    (
        usb_hid.Device.KEYBOARD,
        usb_hid.Device.MOUSE,
        usb_hid.Device.CONSUMER_CONTROL,
    )
)

# Optional: Make the filesystem read-only to the computer
# Uncomment the line below if you want to prevent accidental file modifications
# storage.remount("/", readonly=True)
