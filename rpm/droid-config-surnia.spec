#These and other macros are documented in
#../droid-configs-device/droid-configs.inc

%define device surnia
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty Moto E2 LTE

%define dcd_path ./

#Adjust this for your device
%define pixel_ratio 1.0
#We assume most devices will
%define have_modem 1

# Community HW adaptations need this
%define community_adaptation 1

# For bluez5
%define ofono_enable_plugins bluez5,hfp_ag_bluez5
%define ofono_disable_plugins bluez4,dun_gw_bluez4,hfp_ag_bluez4,hfp_bluez4,dun_gw_bluez5,hfp_bluez5

Provides: ofono-configs

Requires: droid-camres


%include droid-configs-device/droid-configs.inc

%pre
if [ "$1" = "2" ]; then
  rm /etc/droid-cameradetect-module*.conf || :
fi
