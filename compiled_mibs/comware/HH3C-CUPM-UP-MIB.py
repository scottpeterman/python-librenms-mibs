# SNMP MIB module (HH3C-CUPM-UP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-CUPM-UP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:30:54 2025
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

hh3cCupmUp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 195)
)
if mibBuilder.loadTexts:
    hh3cCupmUp.setRevisions(
        ("2020-09-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cCupmUpNotifications_ObjectIdentity = ObjectIdentity
hh3cCupmUpNotifications = _Hh3cCupmUpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 195, 0)
)
_Hh3cCupmUpNotifyVarObjects_ObjectIdentity = ObjectIdentity
hh3cCupmUpNotifyVarObjects = _Hh3cCupmUpNotifyVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 195, 1)
)


class _Hh3cCupmUpVbVxlanID_Type(Integer32):
    """Custom type hh3cCupmUpVbVxlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cCupmUpVbVxlanID_Type.__name__ = "Integer32"
_Hh3cCupmUpVbVxlanID_Object = MibScalar
hh3cCupmUpVbVxlanID = _Hh3cCupmUpVbVxlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 195, 1, 1),
    _Hh3cCupmUpVbVxlanID_Type()
)
hh3cCupmUpVbVxlanID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCupmUpVbVxlanID.setStatus("current")
_Hh3cCupmUpVbSrcAddrType_Type = InetAddressType
_Hh3cCupmUpVbSrcAddrType_Object = MibScalar
hh3cCupmUpVbSrcAddrType = _Hh3cCupmUpVbSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 195, 1, 2),
    _Hh3cCupmUpVbSrcAddrType_Type()
)
hh3cCupmUpVbSrcAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCupmUpVbSrcAddrType.setStatus("current")
_Hh3cCupmUpVbSrcAddr_Type = InetAddress
_Hh3cCupmUpVbSrcAddr_Object = MibScalar
hh3cCupmUpVbSrcAddr = _Hh3cCupmUpVbSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 195, 1, 3),
    _Hh3cCupmUpVbSrcAddr_Type()
)
hh3cCupmUpVbSrcAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCupmUpVbSrcAddr.setStatus("current")
_Hh3cCupmUpVbDestAddrType_Type = InetAddressType
_Hh3cCupmUpVbDestAddrType_Object = MibScalar
hh3cCupmUpVbDestAddrType = _Hh3cCupmUpVbDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 195, 1, 4),
    _Hh3cCupmUpVbDestAddrType_Type()
)
hh3cCupmUpVbDestAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCupmUpVbDestAddrType.setStatus("current")
_Hh3cCupmUpVbDestAddr_Type = InetAddress
_Hh3cCupmUpVbDestAddr_Object = MibScalar
hh3cCupmUpVbDestAddr = _Hh3cCupmUpVbDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 195, 1, 5),
    _Hh3cCupmUpVbDestAddr_Type()
)
hh3cCupmUpVbDestAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCupmUpVbDestAddr.setStatus("current")


class _Hh3cCupmUpVbVpnName_Type(OctetString):
    """Custom type hh3cCupmUpVbVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cCupmUpVbVpnName_Type.__name__ = "OctetString"
_Hh3cCupmUpVbVpnName_Object = MibScalar
hh3cCupmUpVbVpnName = _Hh3cCupmUpVbVpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 195, 1, 6),
    _Hh3cCupmUpVbVpnName_Type()
)
hh3cCupmUpVbVpnName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCupmUpVbVpnName.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cCupmUpProtoTnlUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 195, 0, 1)
)
hh3cCupmUpProtoTnlUp.setObjects(
      *(("HH3C-CUPM-UP-MIB", "hh3cCupmUpVbVxlanID"),
        ("HH3C-CUPM-UP-MIB", "hh3cCupmUpVbSrcAddrType"),
        ("HH3C-CUPM-UP-MIB", "hh3cCupmUpVbSrcAddr"),
        ("HH3C-CUPM-UP-MIB", "hh3cCupmUpVbDestAddrType"),
        ("HH3C-CUPM-UP-MIB", "hh3cCupmUpVbDestAddr"),
        ("HH3C-CUPM-UP-MIB", "hh3cCupmUpVbVpnName"))
)
if mibBuilder.loadTexts:
    hh3cCupmUpProtoTnlUp.setStatus(
        "current"
    )

hh3cCupmUpProtoTnlDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 195, 0, 2)
)
hh3cCupmUpProtoTnlDown.setObjects(
      *(("HH3C-CUPM-UP-MIB", "hh3cCupmUpVbVxlanID"),
        ("HH3C-CUPM-UP-MIB", "hh3cCupmUpVbSrcAddrType"),
        ("HH3C-CUPM-UP-MIB", "hh3cCupmUpVbSrcAddr"),
        ("HH3C-CUPM-UP-MIB", "hh3cCupmUpVbDestAddrType"),
        ("HH3C-CUPM-UP-MIB", "hh3cCupmUpVbDestAddr"),
        ("HH3C-CUPM-UP-MIB", "hh3cCupmUpVbVpnName"))
)
if mibBuilder.loadTexts:
    hh3cCupmUpProtoTnlDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-CUPM-UP-MIB",
    **{"hh3cCupmUp": hh3cCupmUp,
       "hh3cCupmUpNotifications": hh3cCupmUpNotifications,
       "hh3cCupmUpProtoTnlUp": hh3cCupmUpProtoTnlUp,
       "hh3cCupmUpProtoTnlDown": hh3cCupmUpProtoTnlDown,
       "hh3cCupmUpNotifyVarObjects": hh3cCupmUpNotifyVarObjects,
       "hh3cCupmUpVbVxlanID": hh3cCupmUpVbVxlanID,
       "hh3cCupmUpVbSrcAddrType": hh3cCupmUpVbSrcAddrType,
       "hh3cCupmUpVbSrcAddr": hh3cCupmUpVbSrcAddr,
       "hh3cCupmUpVbDestAddrType": hh3cCupmUpVbDestAddrType,
       "hh3cCupmUpVbDestAddr": hh3cCupmUpVbDestAddr,
       "hh3cCupmUpVbVpnName": hh3cCupmUpVbVpnName}
)
