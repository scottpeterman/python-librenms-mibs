# SNMP MIB module (HH3C-GOLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-GOLD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:31:46 2025
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

hh3cGold = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 203)
)
if mibBuilder.loadTexts:
    hh3cGold.setRevisions(
        ("2021-03-13 15:02",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cGoldTrap_ObjectIdentity = ObjectIdentity
hh3cGoldTrap = _Hh3cGoldTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 203, 1)
)
_Hh3cGoldTrapOjbects_ObjectIdentity = ObjectIdentity
hh3cGoldTrapOjbects = _Hh3cGoldTrapOjbects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 203, 1, 0)
)
_Hh3cGoldTrapObjectDefinitions_ObjectIdentity = ObjectIdentity
hh3cGoldTrapObjectDefinitions = _Hh3cGoldTrapObjectDefinitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 203, 1, 1)
)


class _Hh3cGoldLipcLinkSourceChassisID_Type(Integer32):
    """Custom type hh3cGoldLipcLinkSourceChassisID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cGoldLipcLinkSourceChassisID_Type.__name__ = "Integer32"
_Hh3cGoldLipcLinkSourceChassisID_Object = MibScalar
hh3cGoldLipcLinkSourceChassisID = _Hh3cGoldLipcLinkSourceChassisID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 203, 1, 1, 1),
    _Hh3cGoldLipcLinkSourceChassisID_Type()
)
hh3cGoldLipcLinkSourceChassisID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cGoldLipcLinkSourceChassisID.setStatus("current")


class _Hh3cGoldLipcLinkSourceSlotID_Type(Integer32):
    """Custom type hh3cGoldLipcLinkSourceSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cGoldLipcLinkSourceSlotID_Type.__name__ = "Integer32"
_Hh3cGoldLipcLinkSourceSlotID_Object = MibScalar
hh3cGoldLipcLinkSourceSlotID = _Hh3cGoldLipcLinkSourceSlotID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 203, 1, 1, 2),
    _Hh3cGoldLipcLinkSourceSlotID_Type()
)
hh3cGoldLipcLinkSourceSlotID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cGoldLipcLinkSourceSlotID.setStatus("current")


class _Hh3cGoldLipcLinkSourceCpuID_Type(Integer32):
    """Custom type hh3cGoldLipcLinkSourceCpuID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cGoldLipcLinkSourceCpuID_Type.__name__ = "Integer32"
_Hh3cGoldLipcLinkSourceCpuID_Object = MibScalar
hh3cGoldLipcLinkSourceCpuID = _Hh3cGoldLipcLinkSourceCpuID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 203, 1, 1, 3),
    _Hh3cGoldLipcLinkSourceCpuID_Type()
)
hh3cGoldLipcLinkSourceCpuID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cGoldLipcLinkSourceCpuID.setStatus("current")


class _Hh3cGoldLipcLinkDestChassisID_Type(Integer32):
    """Custom type hh3cGoldLipcLinkDestChassisID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cGoldLipcLinkDestChassisID_Type.__name__ = "Integer32"
_Hh3cGoldLipcLinkDestChassisID_Object = MibScalar
hh3cGoldLipcLinkDestChassisID = _Hh3cGoldLipcLinkDestChassisID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 203, 1, 1, 4),
    _Hh3cGoldLipcLinkDestChassisID_Type()
)
hh3cGoldLipcLinkDestChassisID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cGoldLipcLinkDestChassisID.setStatus("current")


class _Hh3cGoldLipcLinkDestSlotID_Type(Integer32):
    """Custom type hh3cGoldLipcLinkDestSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cGoldLipcLinkDestSlotID_Type.__name__ = "Integer32"
_Hh3cGoldLipcLinkDestSlotID_Object = MibScalar
hh3cGoldLipcLinkDestSlotID = _Hh3cGoldLipcLinkDestSlotID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 203, 1, 1, 5),
    _Hh3cGoldLipcLinkDestSlotID_Type()
)
hh3cGoldLipcLinkDestSlotID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cGoldLipcLinkDestSlotID.setStatus("current")


class _Hh3cGoldLipcLinkDestCpuID_Type(Integer32):
    """Custom type hh3cGoldLipcLinkDestCpuID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cGoldLipcLinkDestCpuID_Type.__name__ = "Integer32"
_Hh3cGoldLipcLinkDestCpuID_Object = MibScalar
hh3cGoldLipcLinkDestCpuID = _Hh3cGoldLipcLinkDestCpuID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 203, 1, 1, 6),
    _Hh3cGoldLipcLinkDestCpuID_Type()
)
hh3cGoldLipcLinkDestCpuID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cGoldLipcLinkDestCpuID.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cGoldLipcLinkFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 203, 1, 0, 1)
)
hh3cGoldLipcLinkFail.setObjects(
      *(("HH3C-GOLD-MIB", "hh3cGoldLipcLinkSourceChassisID"),
        ("HH3C-GOLD-MIB", "hh3cGoldLipcLinkSourceSlotID"),
        ("HH3C-GOLD-MIB", "hh3cGoldLipcLinkSourceCpuID"),
        ("HH3C-GOLD-MIB", "hh3cGoldLipcLinkDestChassisID"),
        ("HH3C-GOLD-MIB", "hh3cGoldLipcLinkDestSlotID"),
        ("HH3C-GOLD-MIB", "hh3cGoldLipcLinkDestCpuID"))
)
if mibBuilder.loadTexts:
    hh3cGoldLipcLinkFail.setStatus(
        "current"
    )

hh3cGoldLipcLinkRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 203, 1, 0, 2)
)
hh3cGoldLipcLinkRecover.setObjects(
      *(("HH3C-GOLD-MIB", "hh3cGoldLipcLinkSourceChassisID"),
        ("HH3C-GOLD-MIB", "hh3cGoldLipcLinkSourceSlotID"),
        ("HH3C-GOLD-MIB", "hh3cGoldLipcLinkSourceCpuID"),
        ("HH3C-GOLD-MIB", "hh3cGoldLipcLinkDestChassisID"),
        ("HH3C-GOLD-MIB", "hh3cGoldLipcLinkDestSlotID"),
        ("HH3C-GOLD-MIB", "hh3cGoldLipcLinkDestCpuID"))
)
if mibBuilder.loadTexts:
    hh3cGoldLipcLinkRecover.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-GOLD-MIB",
    **{"hh3cGold": hh3cGold,
       "hh3cGoldTrap": hh3cGoldTrap,
       "hh3cGoldTrapOjbects": hh3cGoldTrapOjbects,
       "hh3cGoldLipcLinkFail": hh3cGoldLipcLinkFail,
       "hh3cGoldLipcLinkRecover": hh3cGoldLipcLinkRecover,
       "hh3cGoldTrapObjectDefinitions": hh3cGoldTrapObjectDefinitions,
       "hh3cGoldLipcLinkSourceChassisID": hh3cGoldLipcLinkSourceChassisID,
       "hh3cGoldLipcLinkSourceSlotID": hh3cGoldLipcLinkSourceSlotID,
       "hh3cGoldLipcLinkSourceCpuID": hh3cGoldLipcLinkSourceCpuID,
       "hh3cGoldLipcLinkDestChassisID": hh3cGoldLipcLinkDestChassisID,
       "hh3cGoldLipcLinkDestSlotID": hh3cGoldLipcLinkDestSlotID,
       "hh3cGoldLipcLinkDestCpuID": hh3cGoldLipcLinkDestCpuID}
)
