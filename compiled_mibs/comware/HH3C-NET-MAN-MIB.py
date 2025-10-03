# SNMP MIB module (HH3C-NET-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-NET-MAN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:23 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

hh3cNetMan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 90)
)
if mibBuilder.loadTexts:
    hh3cNetMan.setRevisions(
        ("2008-04-16 17:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cNMConfigObjects_ObjectIdentity = ObjectIdentity
hh3cNMConfigObjects = _Hh3cNMConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 90, 1)
)
_Hh3cNMMonitorObjects_ObjectIdentity = ObjectIdentity
hh3cNMMonitorObjects = _Hh3cNMMonitorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 90, 2)
)
_Hh3cNMNotify_ObjectIdentity = ObjectIdentity
hh3cNMNotify = _Hh3cNMNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 90, 3)
)
_Hh3cNMNotifyScalarObjects_ObjectIdentity = ObjectIdentity
hh3cNMNotifyScalarObjects = _Hh3cNMNotifyScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 1)
)
_Hh3cNMIpAddressType_Type = InetAddressType
_Hh3cNMIpAddressType_Object = MibScalar
hh3cNMIpAddressType = _Hh3cNMIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 1, 1),
    _Hh3cNMIpAddressType_Type()
)
hh3cNMIpAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cNMIpAddressType.setStatus("current")
_Hh3cNMIpAddress_Type = InetAddress
_Hh3cNMIpAddress_Object = MibScalar
hh3cNMIpAddress = _Hh3cNMIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 1, 2),
    _Hh3cNMIpAddress_Type()
)
hh3cNMIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cNMIpAddress.setStatus("current")


class _Hh3cNMCustomBuildInfo_Type(OctetString):
    """Custom type hh3cNMCustomBuildInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cNMCustomBuildInfo_Type.__name__ = "OctetString"
_Hh3cNMCustomBuildInfo_Object = MibScalar
hh3cNMCustomBuildInfo = _Hh3cNMCustomBuildInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 1, 3),
    _Hh3cNMCustomBuildInfo_Type()
)
hh3cNMCustomBuildInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMCustomBuildInfo.setStatus("current")


class _Hh3cNMSerialNum_Type(OctetString):
    """Custom type hh3cNMSerialNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cNMSerialNum_Type.__name__ = "OctetString"
_Hh3cNMSerialNum_Object = MibScalar
hh3cNMSerialNum = _Hh3cNMSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 1, 4),
    _Hh3cNMSerialNum_Type()
)
hh3cNMSerialNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cNMSerialNum.setStatus("current")
_Hh3cNMNotifyObjects_ObjectIdentity = ObjectIdentity
hh3cNMNotifyObjects = _Hh3cNMNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 2)
)
_Hh3cNMNotifyObjectsPrefix_ObjectIdentity = ObjectIdentity
hh3cNMNotifyObjectsPrefix = _Hh3cNMNotifyObjectsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 2, 0)
)
_Hh3cNetManConformance_ObjectIdentity = ObjectIdentity
hh3cNetManConformance = _Hh3cNetManConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 90, 4)
)
_Hh3cNetManCompliances_ObjectIdentity = ObjectIdentity
hh3cNetManCompliances = _Hh3cNetManCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 90, 4, 1)
)
_Hh3cNetManGroups_ObjectIdentity = ObjectIdentity
hh3cNetManGroups = _Hh3cNetManGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 90, 4, 2)
)

# Managed Objects groups

hh3cNMMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 90, 4, 2, 1)
)
hh3cNMMonitorGroup.setObjects(
      *(("HH3C-NET-MAN-MIB", "hh3cNMIpAddressType"),
        ("HH3C-NET-MAN-MIB", "hh3cNMIpAddress"),
        ("HH3C-NET-MAN-MIB", "hh3cNMCustomBuildInfo"),
        ("HH3C-NET-MAN-MIB", "hh3cNMSerialNum"))
)
if mibBuilder.loadTexts:
    hh3cNMMonitorGroup.setStatus("current")


# Notification objects

hh3cIpAddrChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 2, 0, 1)
)
hh3cIpAddrChangeNotify.setObjects(
      *(("HH3C-NET-MAN-MIB", "hh3cNMIpAddressType"),
        ("HH3C-NET-MAN-MIB", "hh3cNMIpAddress"),
        ("HH3C-NET-MAN-MIB", "hh3cNMCustomBuildInfo"),
        ("HH3C-NET-MAN-MIB", "hh3cNMSerialNum"))
)
if mibBuilder.loadTexts:
    hh3cIpAddrChangeNotify.setStatus(
        "current"
    )


# Notifications groups

hh3cNMNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 90, 4, 2, 2)
)
hh3cNMNotificationGroup.setObjects(
    ("HH3C-NET-MAN-MIB", "hh3cIpAddrChangeNotify")
)
if mibBuilder.loadTexts:
    hh3cNMNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hh3cNetManCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 90, 4, 1, 1)
)
hh3cNetManCompliance.setObjects(
      *(("HH3C-NET-MAN-MIB", "hh3cNMMonitorGroup"),
        ("HH3C-NET-MAN-MIB", "hh3cNMNotificationGroup"))
)
if mibBuilder.loadTexts:
    hh3cNetManCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-NET-MAN-MIB",
    **{"hh3cNetMan": hh3cNetMan,
       "hh3cNMConfigObjects": hh3cNMConfigObjects,
       "hh3cNMMonitorObjects": hh3cNMMonitorObjects,
       "hh3cNMNotify": hh3cNMNotify,
       "hh3cNMNotifyScalarObjects": hh3cNMNotifyScalarObjects,
       "hh3cNMIpAddressType": hh3cNMIpAddressType,
       "hh3cNMIpAddress": hh3cNMIpAddress,
       "hh3cNMCustomBuildInfo": hh3cNMCustomBuildInfo,
       "hh3cNMSerialNum": hh3cNMSerialNum,
       "hh3cNMNotifyObjects": hh3cNMNotifyObjects,
       "hh3cNMNotifyObjectsPrefix": hh3cNMNotifyObjectsPrefix,
       "hh3cIpAddrChangeNotify": hh3cIpAddrChangeNotify,
       "hh3cNetManConformance": hh3cNetManConformance,
       "hh3cNetManCompliances": hh3cNetManCompliances,
       "hh3cNetManCompliance": hh3cNetManCompliance,
       "hh3cNetManGroups": hh3cNetManGroups,
       "hh3cNMMonitorGroup": hh3cNMMonitorGroup,
       "hh3cNMNotificationGroup": hh3cNMNotificationGroup}
)
