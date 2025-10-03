# SNMP MIB module (NETGEAR-REF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\netgear\NETGEAR-REF-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:11:47 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

broadcom = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413)
)
if mibBuilder.loadTexts:
    broadcom.setRevisions(
        ("2007-05-23 00:00",
         "2003-11-21 00:00",
         "2003-02-06 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AgentPortMask(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Netgear_ObjectIdentity = ObjectIdentity
netgear = _Netgear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526)
)
_ManagedSwitch_ObjectIdentity = ObjectIdentity
managedSwitch = _ManagedSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1)
)
_Fsm726s_ObjectIdentity = ObjectIdentity
fsm726s = _Fsm726s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1)
)
_Fsm750s_ObjectIdentity = ObjectIdentity
fsm750s = _Fsm750s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 2)
)
_Gsm712_ObjectIdentity = ObjectIdentity
gsm712 = _Gsm712_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 3)
)
_Fsm726_ObjectIdentity = ObjectIdentity
fsm726 = _Fsm726_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 4)
)
_Gsm712f_ObjectIdentity = ObjectIdentity
gsm712f = _Gsm712f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 5)
)
_Gsm7312_ObjectIdentity = ObjectIdentity
gsm7312 = _Gsm7312_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6)
)
_Gsm7324_ObjectIdentity = ObjectIdentity
gsm7324 = _Gsm7324_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 7)
)
_Gsm7224_ObjectIdentity = ObjectIdentity
gsm7224 = _Gsm7224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 8)
)
_Fsm7326p_ObjectIdentity = ObjectIdentity
fsm7326p = _Fsm7326p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9)
)
_Fsm726v2_ObjectIdentity = ObjectIdentity
fsm726v2 = _Fsm726v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 10)
)
_Vpnrouter_ObjectIdentity = ObjectIdentity
vpnrouter = _Vpnrouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 2)
)
_Carrier_ObjectIdentity = ObjectIdentity
carrier = _Carrier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 3)
)
_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4)
)
_Me103_ObjectIdentity = ObjectIdentity
me103 = _Me103_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1)
)
_Wg302_ObjectIdentity = ObjectIdentity
wg302 = _Wg302_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2)
)
_Wg102_ObjectIdentity = ObjectIdentity
wg102 = _Wg102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3)
)
_Wag302_ObjectIdentity = ObjectIdentity
wag302 = _Wag302_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 4)
)
_Wag102_ObjectIdentity = ObjectIdentity
wag102 = _Wag102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 5)
)
_Wg302v2_ObjectIdentity = ObjectIdentity
wg302v2 = _Wg302v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 6)
)
_Wag302v2_ObjectIdentity = ObjectIdentity
wag302v2 = _Wag302v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 7)
)
_Rps_ObjectIdentity = ObjectIdentity
rps = _Rps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 5)
)
_Wlanswitch_ObjectIdentity = ObjectIdentity
wlanswitch = _Wlanswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 6)
)
_Wls538_ObjectIdentity = ObjectIdentity
wls538 = _Wls538_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 6, 1)
)
_Ng7000managedswitch_ObjectIdentity = ObjectIdentity
ng7000managedswitch = _Ng7000managedswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10)
)
_Ng700smartswitch_ObjectIdentity = ObjectIdentity
ng700smartswitch = _Ng700smartswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 11)
)
_Ngrouter_ObjectIdentity = ObjectIdentity
ngrouter = _Ngrouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 12)
)
_Ngfirewall_ObjectIdentity = ObjectIdentity
ngfirewall = _Ngfirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 13)
)
_Ngap_ObjectIdentity = ObjectIdentity
ngap = _Ngap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 14)
)
_Ngwlan_ObjectIdentity = ObjectIdentity
ngwlan = _Ngwlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 15)
)
_Ng9000chassisswitch_ObjectIdentity = ObjectIdentity
ng9000chassisswitch = _Ng9000chassisswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 16)
)
_Ng700stacksmartswitch_ObjectIdentity = ObjectIdentity
ng700stacksmartswitch = _Ng700stacksmartswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 17)
)
_ProductID_ObjectIdentity = ObjectIdentity
productID = _ProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100)
)
_Stackswitch_ObjectIdentity = ObjectIdentity
stackswitch = _Stackswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1)
)
_Fsm7328s_ObjectIdentity = ObjectIdentity
fsm7328s = _Fsm7328s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 1)
)
_Fsm7352s_ObjectIdentity = ObjectIdentity
fsm7352s = _Fsm7352s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 2)
)
_Gsm7328s_ObjectIdentity = ObjectIdentity
gsm7328s = _Gsm7328s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 3)
)
_Gsm7352s_ObjectIdentity = ObjectIdentity
gsm7352s = _Gsm7352s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 4)
)
_Fsm7352ps_ObjectIdentity = ObjectIdentity
fsm7352ps = _Fsm7352ps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 5)
)
_Gsm7328fs_ObjectIdentity = ObjectIdentity
gsm7328fs = _Gsm7328fs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 7)
)
_Fsm7328ps_ObjectIdentity = ObjectIdentity
fsm7328ps = _Fsm7328ps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 8)
)
_Gsm7228ps_ObjectIdentity = ObjectIdentity
gsm7228ps = _Gsm7228ps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 9)
)
_Gsm7252ps_ObjectIdentity = ObjectIdentity
gsm7252ps = _Gsm7252ps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 10)
)
_Fsm7226rs_ObjectIdentity = ObjectIdentity
fsm7226rs = _Fsm7226rs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 11)
)
_Fsm7250rs_ObjectIdentity = ObjectIdentity
fsm7250rs = _Fsm7250rs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 12)
)
_Gsm7328se_ObjectIdentity = ObjectIdentity
gsm7328se = _Gsm7328se_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 13)
)
_Gsm7352se_ObjectIdentity = ObjectIdentity
gsm7352se = _Gsm7352se_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 14)
)
_Xsm7224s_ObjectIdentity = ObjectIdentity
xsm7224s = _Xsm7224s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 15)
)
_M530028gpoe_ObjectIdentity = ObjectIdentity
m530028gpoe = _M530028gpoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 16)
)
_M530052gpoe_ObjectIdentity = ObjectIdentity
m530052gpoe = _M530052gpoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 17)
)
_M530028g3_ObjectIdentity = ObjectIdentity
m530028g3 = _M530028g3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 18)
)
_M530052g3_ObjectIdentity = ObjectIdentity
m530052g3 = _M530052g3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 19)
)
_M530028gf3_ObjectIdentity = ObjectIdentity
m530028gf3 = _M530028gf3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 20)
)
_M530028g_ObjectIdentity = ObjectIdentity
m530028g = _M530028g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 21)
)
_M530052g_ObjectIdentity = ObjectIdentity
m530052g = _M530052g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 22)
)
_L2switch_ObjectIdentity = ObjectIdentity
l2switch = _L2switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 2)
)
_Gsm7248_ObjectIdentity = ObjectIdentity
gsm7248 = _Gsm7248_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 2, 1)
)
_Gsm7212_ObjectIdentity = ObjectIdentity
gsm7212 = _Gsm7212_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 2, 2)
)
_Gsm7224i_ObjectIdentity = ObjectIdentity
gsm7224i = _Gsm7224i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 2, 3)
)
_Fsm7226_ObjectIdentity = ObjectIdentity
fsm7226 = _Fsm7226_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 2, 4)
)
_L3switch_ObjectIdentity = ObjectIdentity
l3switch = _L3switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 3)
)
_Gsm7312v2_ObjectIdentity = ObjectIdentity
gsm7312v2 = _Gsm7312v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 3, 1)
)
_Gsm7324v2_ObjectIdentity = ObjectIdentity
gsm7324v2 = _Gsm7324v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 3, 2)
)
_Xsm7312_ObjectIdentity = ObjectIdentity
xsm7312 = _Xsm7312_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 3, 3)
)
_Gsm7324p_ObjectIdentity = ObjectIdentity
gsm7324p = _Gsm7324p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 3, 4)
)
_Gsm7312i_ObjectIdentity = ObjectIdentity
gsm7312i = _Gsm7312i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 3, 5)
)
_Gsm7324i_ObjectIdentity = ObjectIdentity
gsm7324i = _Gsm7324i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 3, 6)
)
_Fsm7326pi_ObjectIdentity = ObjectIdentity
fsm7326pi = _Fsm7326pi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 3, 7)
)
_Smartswitch_ObjectIdentity = ObjectIdentity
smartswitch = _Smartswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4)
)
_Gs748t_ObjectIdentity = ObjectIdentity
gs748t = _Gs748t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 1)
)
_Fs726t_ObjectIdentity = ObjectIdentity
fs726t = _Fs726t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 2)
)
_Gs716t_ObjectIdentity = ObjectIdentity
gs716t = _Gs716t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 3)
)
_Fs750t_ObjectIdentity = ObjectIdentity
fs750t = _Fs750t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 4)
)
_Gs724t_ObjectIdentity = ObjectIdentity
gs724t = _Gs724t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 5)
)
_Fs726tp_ObjectIdentity = ObjectIdentity
fs726tp = _Fs726tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 6)
)
_Fs728tp_ObjectIdentity = ObjectIdentity
fs728tp = _Fs728tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 7)
)
_Gs108t_ObjectIdentity = ObjectIdentity
gs108t = _Gs108t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 8)
)
_Gs108tp_ObjectIdentity = ObjectIdentity
gs108tp = _Gs108tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 9)
)
_Gs724tp_ObjectIdentity = ObjectIdentity
gs724tp = _Gs724tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 10)
)
_Gs748tp_ObjectIdentity = ObjectIdentity
gs748tp = _Gs748tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 11)
)
_Gs724tr_ObjectIdentity = ObjectIdentity
gs724tr = _Gs724tr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 12)
)
_Gs748tr_ObjectIdentity = ObjectIdentity
gs748tr = _Gs748tr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 13)
)
_Gs716tv2_ObjectIdentity = ObjectIdentity
gs716tv2 = _Gs716tv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 16)
)
_Gs724tv3_ObjectIdentity = ObjectIdentity
gs724tv3 = _Gs724tv3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 17)
)
_Gs108tv2_ObjectIdentity = ObjectIdentity
gs108tv2 = _Gs108tv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 18)
)
_Gs110tp_ObjectIdentity = ObjectIdentity
gs110tp = _Gs110tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 19)
)
_Fs728tpv2_ObjectIdentity = ObjectIdentity
fs728tpv2 = _Fs728tpv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 20)
)
_Xs712t_ObjectIdentity = ObjectIdentity
xs712t = _Xs712t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 30)
)
_Gs716tv3_ObjectIdentity = ObjectIdentity
gs716tv3 = _Gs716tv3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 31)
)
_Gs724tv4_ObjectIdentity = ObjectIdentity
gs724tv4 = _Gs724tv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 32)
)
_Gs748tv5_ObjectIdentity = ObjectIdentity
gs748tv5 = _Gs748tv5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 33)
)
_Router_ObjectIdentity = ObjectIdentity
router = _Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 5)
)
_Fvx538_ObjectIdentity = ObjectIdentity
fvx538 = _Fvx538_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 5, 1)
)
_Fvs338_ObjectIdentity = ObjectIdentity
fvs338 = _Fvs338_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 5, 2)
)
_Fvg318_ObjectIdentity = ObjectIdentity
fvg318 = _Fvg318_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 5, 3)
)
_Fvs336g_ObjectIdentity = ObjectIdentity
fvs336g = _Fvs336g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 5, 4)
)
_Firewall_ObjectIdentity = ObjectIdentity
firewall = _Firewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 6)
)
_Fwag114_ObjectIdentity = ObjectIdentity
fwag114 = _Fwag114_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 6, 3)
)
_Fvs124g_ObjectIdentity = ObjectIdentity
fvs124g = _Fvs124g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 6, 4)
)
_Fvs318v3_ObjectIdentity = ObjectIdentity
fvs318v3 = _Fvs318v3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 6, 5)
)
_Dgfv338_ObjectIdentity = ObjectIdentity
dgfv338 = _Dgfv338_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 6, 6)
)
_Accesspoint_ObjectIdentity = ObjectIdentity
accesspoint = _Accesspoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 7)
)
_Wpn802_ObjectIdentity = ObjectIdentity
wpn802 = _Wpn802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 7, 1)
)
_Wg312_ObjectIdentity = ObjectIdentity
wg312 = _Wg312_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 7, 2)
)
_Wag312_ObjectIdentity = ObjectIdentity
wag312 = _Wag312_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 7, 3)
)
_WirelessLAN_ObjectIdentity = ObjectIdentity
wirelessLAN = _WirelessLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 8)
)
_Chassisswitch_ObjectIdentity = ObjectIdentity
chassisswitch = _Chassisswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 9)
)
_Gcm9000_ObjectIdentity = ObjectIdentity
gcm9000 = _Gcm9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 9, 1)
)
_Xcm8903_ObjectIdentity = ObjectIdentity
xcm8903 = _Xcm8903_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 9, 6)
)
_Stacksmartswitch_ObjectIdentity = ObjectIdentity
stacksmartswitch = _Stacksmartswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 10)
)
_Fs728ts_ObjectIdentity = ObjectIdentity
fs728ts = _Fs728ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 10, 1)
)
_Fs752ts_ObjectIdentity = ObjectIdentity
fs752ts = _Fs752ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 10, 2)
)
_Fs752tps_ObjectIdentity = ObjectIdentity
fs752tps = _Fs752tps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 10, 3)
)
_Gs724ts_ObjectIdentity = ObjectIdentity
gs724ts = _Gs724ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 10, 4)
)
_Gs748ts_ObjectIdentity = ObjectIdentity
gs748ts = _Gs748ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 10, 5)
)
_Gs752tstps_ObjectIdentity = ObjectIdentity
gs752tstps = _Gs752tstps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 10, 8)
)
_Gs752txs_ObjectIdentity = ObjectIdentity
gs752txs = _Gs752txs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 10, 10)
)
_Gs728ts_ObjectIdentity = ObjectIdentity
gs728ts = _Gs728ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 10, 11)
)
_Gs752ts_ObjectIdentity = ObjectIdentity
gs752ts = _Gs752ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 10, 12)
)
_Gs728tps_ObjectIdentity = ObjectIdentity
gs728tps = _Gs728tps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 10, 13)
)
_Gs752tps_ObjectIdentity = ObjectIdentity
gs752tps = _Gs752tps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 10, 14)
)
_Gs728txs_ObjectIdentity = ObjectIdentity
gs728txs = _Gs728txs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 10, 15)
)
_S3300_28x_ObjectIdentity = ObjectIdentity
s3300_28x = _S3300_28x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 10, 16)
)
_S3300_28x_poe_ObjectIdentity = ObjectIdentity
s3300_28x_poe = _S3300_28x_poe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 10, 17)
)
_S3300_52x_ObjectIdentity = ObjectIdentity
s3300_52x = _S3300_52x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 10, 18)
)
_S3300_52x_poe_ObjectIdentity = ObjectIdentity
s3300_52x_poe = _S3300_52x_poe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 10, 19)
)
_L2Rswitch_ObjectIdentity = ObjectIdentity
l2Rswitch = _L2Rswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11)
)
_Gsm7224r_ObjectIdentity = ObjectIdentity
gsm7224r = _Gsm7224r_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 1)
)
_Gsm7248r_ObjectIdentity = ObjectIdentity
gsm7248r = _Gsm7248r_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 2)
)
_Gsm7224rp_ObjectIdentity = ObjectIdentity
gsm7224rp = _Gsm7224rp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 3)
)
_Gsm7248rp_ObjectIdentity = ObjectIdentity
gsm7248rp = _Gsm7248rp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 4)
)
_Gsm7224v2_ObjectIdentity = ObjectIdentity
gsm7224v2 = _Gsm7224v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 5)
)
_Gsm7248v2_ObjectIdentity = ObjectIdentity
gsm7248v2 = _Gsm7248v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 6)
)
_Gsm7212f_ObjectIdentity = ObjectIdentity
gsm7212f = _Gsm7212f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 7)
)
_Gsm5212p_ObjectIdentity = ObjectIdentity
gsm5212p = _Gsm5212p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 8)
)
_Gsm7212p_ObjectIdentity = ObjectIdentity
gsm7212p = _Gsm7212p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 9)
)
_Gsm7224p_ObjectIdentity = ObjectIdentity
gsm7224p = _Gsm7224p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 10)
)
_M4100_26g_ObjectIdentity = ObjectIdentity
m4100_26g = _M4100_26g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 16)
)
_M4100_50g_ObjectIdentity = ObjectIdentity
m4100_50g = _M4100_50g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 17)
)
_M4100_26_poe_ObjectIdentity = ObjectIdentity
m4100_26_poe = _M4100_26_poe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 18)
)
_M4100_26g_poe_ObjectIdentity = ObjectIdentity
m4100_26g_poe = _M4100_26g_poe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 19)
)
_M4100_50g_poe_ObjectIdentity = ObjectIdentity
m4100_50g_poe = _M4100_50g_poe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 20)
)
_M4100_50_poe_ObjectIdentity = ObjectIdentity
m4100_50_poe = _M4100_50_poe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 21)
)
_M4100_d12g_ObjectIdentity = ObjectIdentity
m4100_d12g = _M4100_d12g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 22)
)
_M4100_d10_poe_ObjectIdentity = ObjectIdentity
m4100_d10_poe = _M4100_d10_poe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 23)
)
_M4100_12gf_ObjectIdentity = ObjectIdentity
m4100_12gf = _M4100_12gf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 24)
)
_M4100_d12g_poe_ObjectIdentity = ObjectIdentity
m4100_d12g_poe = _M4100_d12g_poe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 25)
)
_M4100_12g_poe_ObjectIdentity = ObjectIdentity
m4100_12g_poe = _M4100_12g_poe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 26)
)
_M4100_24g_poe_ObjectIdentity = ObjectIdentity
m4100_24g_poe = _M4100_24g_poe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 11, 27)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETGEAR-REF-MIB",
    **{"AgentPortMask": AgentPortMask,
       "broadcom": broadcom,
       "netgear": netgear,
       "managedSwitch": managedSwitch,
       "fsm726s": fsm726s,
       "fsm750s": fsm750s,
       "gsm712": gsm712,
       "fsm726": fsm726,
       "gsm712f": gsm712f,
       "gsm7312": gsm7312,
       "gsm7324": gsm7324,
       "gsm7224": gsm7224,
       "fsm7326p": fsm7326p,
       "fsm726v2": fsm726v2,
       "vpnrouter": vpnrouter,
       "carrier": carrier,
       "wireless": wireless,
       "me103": me103,
       "wg302": wg302,
       "wg102": wg102,
       "wag302": wag302,
       "wag102": wag102,
       "wg302v2": wg302v2,
       "wag302v2": wag302v2,
       "rps": rps,
       "wlanswitch": wlanswitch,
       "wls538": wls538,
       "ng7000managedswitch": ng7000managedswitch,
       "ng700smartswitch": ng700smartswitch,
       "ngrouter": ngrouter,
       "ngfirewall": ngfirewall,
       "ngap": ngap,
       "ngwlan": ngwlan,
       "ng9000chassisswitch": ng9000chassisswitch,
       "ng700stacksmartswitch": ng700stacksmartswitch,
       "productID": productID,
       "stackswitch": stackswitch,
       "fsm7328s": fsm7328s,
       "fsm7352s": fsm7352s,
       "gsm7328s": gsm7328s,
       "gsm7352s": gsm7352s,
       "fsm7352ps": fsm7352ps,
       "gsm7328fs": gsm7328fs,
       "fsm7328ps": fsm7328ps,
       "gsm7228ps": gsm7228ps,
       "gsm7252ps": gsm7252ps,
       "fsm7226rs": fsm7226rs,
       "fsm7250rs": fsm7250rs,
       "gsm7328se": gsm7328se,
       "gsm7352se": gsm7352se,
       "xsm7224s": xsm7224s,
       "m530028gpoe": m530028gpoe,
       "m530052gpoe": m530052gpoe,
       "m530028g3": m530028g3,
       "m530052g3": m530052g3,
       "m530028gf3": m530028gf3,
       "m530028g": m530028g,
       "m530052g": m530052g,
       "l2switch": l2switch,
       "gsm7248": gsm7248,
       "gsm7212": gsm7212,
       "gsm7224i": gsm7224i,
       "fsm7226": fsm7226,
       "l3switch": l3switch,
       "gsm7312v2": gsm7312v2,
       "gsm7324v2": gsm7324v2,
       "xsm7312": xsm7312,
       "gsm7324p": gsm7324p,
       "gsm7312i": gsm7312i,
       "gsm7324i": gsm7324i,
       "fsm7326pi": fsm7326pi,
       "smartswitch": smartswitch,
       "gs748t": gs748t,
       "fs726t": fs726t,
       "gs716t": gs716t,
       "fs750t": fs750t,
       "gs724t": gs724t,
       "fs726tp": fs726tp,
       "fs728tp": fs728tp,
       "gs108t": gs108t,
       "gs108tp": gs108tp,
       "gs724tp": gs724tp,
       "gs748tp": gs748tp,
       "gs724tr": gs724tr,
       "gs748tr": gs748tr,
       "gs716tv2": gs716tv2,
       "gs724tv3": gs724tv3,
       "gs108tv2": gs108tv2,
       "gs110tp": gs110tp,
       "fs728tpv2": fs728tpv2,
       "xs712t": xs712t,
       "gs716tv3": gs716tv3,
       "gs724tv4": gs724tv4,
       "gs748tv5": gs748tv5,
       "router": router,
       "fvx538": fvx538,
       "fvs338": fvs338,
       "fvg318": fvg318,
       "fvs336g": fvs336g,
       "firewall": firewall,
       "fwag114": fwag114,
       "fvs124g": fvs124g,
       "fvs318v3": fvs318v3,
       "dgfv338": dgfv338,
       "accesspoint": accesspoint,
       "wpn802": wpn802,
       "wg312": wg312,
       "wag312": wag312,
       "wirelessLAN": wirelessLAN,
       "chassisswitch": chassisswitch,
       "gcm9000": gcm9000,
       "xcm8903": xcm8903,
       "stacksmartswitch": stacksmartswitch,
       "fs728ts": fs728ts,
       "fs752ts": fs752ts,
       "fs752tps": fs752tps,
       "gs724ts": gs724ts,
       "gs748ts": gs748ts,
       "gs752tstps": gs752tstps,
       "gs752txs": gs752txs,
       "gs728ts": gs728ts,
       "gs752ts": gs752ts,
       "gs728tps": gs728tps,
       "gs752tps": gs752tps,
       "gs728txs": gs728txs,
       "s3300-28x": s3300_28x,
       "s3300-28x-poe": s3300_28x_poe,
       "s3300-52x": s3300_52x,
       "s3300-52x-poe": s3300_52x_poe,
       "l2Rswitch": l2Rswitch,
       "gsm7224r": gsm7224r,
       "gsm7248r": gsm7248r,
       "gsm7224rp": gsm7224rp,
       "gsm7248rp": gsm7248rp,
       "gsm7224v2": gsm7224v2,
       "gsm7248v2": gsm7248v2,
       "gsm7212f": gsm7212f,
       "gsm5212p": gsm5212p,
       "gsm7212p": gsm7212p,
       "gsm7224p": gsm7224p,
       "m4100-26g": m4100_26g,
       "m4100-50g": m4100_50g,
       "m4100-26-poe": m4100_26_poe,
       "m4100-26g-poe": m4100_26g_poe,
       "m4100-50g-poe": m4100_50g_poe,
       "m4100-50-poe": m4100_50_poe,
       "m4100-d12g": m4100_d12g,
       "m4100-d10-poe": m4100_d10_poe,
       "m4100-12gf": m4100_12gf,
       "m4100-d12g-poe": m4100_d12g_poe,
       "m4100-12g-poe": m4100_12g_poe,
       "m4100-24g-poe": m4100_24g_poe}
)
