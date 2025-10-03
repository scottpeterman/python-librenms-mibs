# SNMP MIB module (ALCATEL-NGOAW-DEVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\stellar\ALCATEL-NGOAW-DEVICES-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:16:43 2025
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

(hardwareNGOAWDevices,) = mibBuilder.importSymbols(
    "ALCATEL-NGOAW-BASE-MIB",
    "hardwareNGOAWDevices")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

alcatelNGOAWDevicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelNGOAWDevicesMIB.setRevisions(
        ("2016-09-01 00:00",
         "2019-05-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FamilyNGOAWWirelessSwitch_ObjectIdentity = ObjectIdentity
familyNGOAWWirelessSwitch = _FamilyNGOAWWirelessSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    familyNGOAWWirelessSwitch.setStatus("current")
_FamilyNGOAWWirelessAP_ObjectIdentity = ObjectIdentity
familyNGOAWWirelessAP = _FamilyNGOAWWirelessAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    familyNGOAWWirelessAP.setStatus("current")
_DeviceNGOAWAp1101_ObjectIdentity = ObjectIdentity
deviceNGOAWAp1101 = _DeviceNGOAWAp1101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    deviceNGOAWAp1101.setStatus("current")
_DeviceNGOAWAp1221_ObjectIdentity = ObjectIdentity
deviceNGOAWAp1221 = _DeviceNGOAWAp1221_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    deviceNGOAWAp1221.setStatus("current")
_DeviceNGOAWAp1222_ObjectIdentity = ObjectIdentity
deviceNGOAWAp1222 = _DeviceNGOAWAp1222_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    deviceNGOAWAp1222.setStatus("current")
_DeviceNGOAWAp1231_ObjectIdentity = ObjectIdentity
deviceNGOAWAp1231 = _DeviceNGOAWAp1231_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    deviceNGOAWAp1231.setStatus("current")
_DeviceNGOAWAp1232_ObjectIdentity = ObjectIdentity
deviceNGOAWAp1232 = _DeviceNGOAWAp1232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    deviceNGOAWAp1232.setStatus("current")
_DeviceNGOAWAp1251_ObjectIdentity = ObjectIdentity
deviceNGOAWAp1251 = _DeviceNGOAWAp1251_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    deviceNGOAWAp1251.setStatus("current")
_DeviceNGOAWAp1251D_ObjectIdentity = ObjectIdentity
deviceNGOAWAp1251D = _DeviceNGOAWAp1251D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 2, 1, 2, 7)
)
if mibBuilder.loadTexts:
    deviceNGOAWAp1251D.setStatus("current")
_DeviceNGOAWAp1201H_ObjectIdentity = ObjectIdentity
deviceNGOAWAp1201H = _DeviceNGOAWAp1201H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 2, 1, 2, 8)
)
if mibBuilder.loadTexts:
    deviceNGOAWAp1201H.setStatus("current")
_DeviceNGOAWAp1201_ObjectIdentity = ObjectIdentity
deviceNGOAWAp1201 = _DeviceNGOAWAp1201_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 2, 1, 2, 9)
)
if mibBuilder.loadTexts:
    deviceNGOAWAp1201.setStatus("current")
_DeviceNGOAWAp1201L_ObjectIdentity = ObjectIdentity
deviceNGOAWAp1201L = _DeviceNGOAWAp1201L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 2, 1, 2, 10)
)
if mibBuilder.loadTexts:
    deviceNGOAWAp1201L.setStatus("current")
_DeviceNGOAWAp1201HL_ObjectIdentity = ObjectIdentity
deviceNGOAWAp1201HL = _DeviceNGOAWAp1201HL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 2, 1, 2, 11)
)
if mibBuilder.loadTexts:
    deviceNGOAWAp1201HL.setStatus("current")
_DeviceNGOAWAp1321_ObjectIdentity = ObjectIdentity
deviceNGOAWAp1321 = _DeviceNGOAWAp1321_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 2, 1, 2, 12)
)
if mibBuilder.loadTexts:
    deviceNGOAWAp1321.setStatus("current")
_DeviceNGOAWAp1322_ObjectIdentity = ObjectIdentity
deviceNGOAWAp1322 = _DeviceNGOAWAp1322_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 2, 1, 2, 13)
)
if mibBuilder.loadTexts:
    deviceNGOAWAp1322.setStatus("current")
_DeviceNGOAWAp1361_ObjectIdentity = ObjectIdentity
deviceNGOAWAp1361 = _DeviceNGOAWAp1361_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 2, 1, 2, 14)
)
if mibBuilder.loadTexts:
    deviceNGOAWAp1361.setStatus("current")
_DeviceNGOAWAp1361D_ObjectIdentity = ObjectIdentity
deviceNGOAWAp1361D = _DeviceNGOAWAp1361D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 2, 1, 2, 15)
)
if mibBuilder.loadTexts:
    deviceNGOAWAp1361D.setStatus("current")
_DeviceNGOAWAp1362_ObjectIdentity = ObjectIdentity
deviceNGOAWAp1362 = _DeviceNGOAWAp1362_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 2, 1, 2, 16)
)
if mibBuilder.loadTexts:
    deviceNGOAWAp1362.setStatus("current")
_DeviceNGOAWAp1201BG_ObjectIdentity = ObjectIdentity
deviceNGOAWAp1201BG = _DeviceNGOAWAp1201BG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 2, 1, 2, 17)
)
if mibBuilder.loadTexts:
    deviceNGOAWAp1201BG.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-NGOAW-DEVICES-MIB",
    **{"alcatelNGOAWDevicesMIB": alcatelNGOAWDevicesMIB,
       "familyNGOAWWirelessSwitch": familyNGOAWWirelessSwitch,
       "familyNGOAWWirelessAP": familyNGOAWWirelessAP,
       "deviceNGOAWAp1101": deviceNGOAWAp1101,
       "deviceNGOAWAp1221": deviceNGOAWAp1221,
       "deviceNGOAWAp1222": deviceNGOAWAp1222,
       "deviceNGOAWAp1231": deviceNGOAWAp1231,
       "deviceNGOAWAp1232": deviceNGOAWAp1232,
       "deviceNGOAWAp1251": deviceNGOAWAp1251,
       "deviceNGOAWAp1251D": deviceNGOAWAp1251D,
       "deviceNGOAWAp1201H": deviceNGOAWAp1201H,
       "deviceNGOAWAp1201": deviceNGOAWAp1201,
       "deviceNGOAWAp1201L": deviceNGOAWAp1201L,
       "deviceNGOAWAp1201HL": deviceNGOAWAp1201HL,
       "deviceNGOAWAp1321": deviceNGOAWAp1321,
       "deviceNGOAWAp1322": deviceNGOAWAp1322,
       "deviceNGOAWAp1361": deviceNGOAWAp1361,
       "deviceNGOAWAp1361D": deviceNGOAWAp1361D,
       "deviceNGOAWAp1362": deviceNGOAWAp1362,
       "deviceNGOAWAp1201BG": deviceNGOAWAp1201BG}
)
