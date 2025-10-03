# SNMP MIB module (HH3C-ISIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-ISIS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:31:55 2025
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

(IndexInteger,) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "IndexInteger")

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InterfaceIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifName")

(isisNotificationCircIfIndex,
 isisNotificationSysLevelIndex,
 isisPduLspId) = mibBuilder.importSymbols(
    "ISIS-MIB",
    "isisNotificationCircIfIndex",
    "isisNotificationSysLevelIndex",
    "isisPduLspId")

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

hh3cIsis = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 59)
)
if mibBuilder.loadTexts:
    hh3cIsis.setRevisions(
        ("2021-05-06 10:38",
         "2021-04-06 10:38",
         "2020-08-05 11:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cIsisNotifications_ObjectIdentity = ObjectIdentity
hh3cIsisNotifications = _Hh3cIsisNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 59, 0)
)
_Hh3cIsisObjects_ObjectIdentity = ObjectIdentity
hh3cIsisObjects = _Hh3cIsisObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 59, 1)
)
_Hh3cIsisSystem_ObjectIdentity = ObjectIdentity
hh3cIsisSystem = _Hh3cIsisSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 59, 1, 1)
)
_Hh3cIsisSysTable_Object = MibTable
hh3cIsisSysTable = _Hh3cIsisSysTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 59, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cIsisSysTable.setStatus("current")
_Hh3cIsisSysEntry_Object = MibTableRow
hh3cIsisSysEntry = _Hh3cIsisSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 59, 1, 1, 1, 1)
)
hh3cIsisSysEntry.setIndexNames(
    (0, "HH3C-ISIS-MIB", "hh3cIsisSysInstance"),
)
if mibBuilder.loadTexts:
    hh3cIsisSysEntry.setStatus("current")


class _Hh3cIsisSysInstance_Type(Integer32):
    """Custom type hh3cIsisSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cIsisSysInstance_Type.__name__ = "Integer32"
_Hh3cIsisSysInstance_Object = MibTableColumn
hh3cIsisSysInstance = _Hh3cIsisSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 59, 1, 1, 1, 1, 1),
    _Hh3cIsisSysInstance_Type()
)
hh3cIsisSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIsisSysInstance.setStatus("current")
_Hh3cIsisNotification_ObjectIdentity = ObjectIdentity
hh3cIsisNotification = _Hh3cIsisNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 59, 1, 2)
)
_Hh3cIsisNotificationObjects_ObjectIdentity = ObjectIdentity
hh3cIsisNotificationObjects = _Hh3cIsisNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 59, 1, 2, 1)
)


class _Hh3cIsisAdjProtoType_Type(Integer32):
    """Custom type hh3cIsisAdjProtoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_Hh3cIsisAdjProtoType_Type.__name__ = "Integer32"
_Hh3cIsisAdjProtoType_Object = MibScalar
hh3cIsisAdjProtoType = _Hh3cIsisAdjProtoType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 59, 1, 2, 1, 1),
    _Hh3cIsisAdjProtoType_Type()
)
hh3cIsisAdjProtoType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIsisAdjProtoType.setStatus("current")


class _Hh3cIsisAdjProtoState_Type(Integer32):
    """Custom type hh3cIsisAdjProtoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("initializing", 2),
          ("up", 3))
    )


_Hh3cIsisAdjProtoState_Type.__name__ = "Integer32"
_Hh3cIsisAdjProtoState_Object = MibScalar
hh3cIsisAdjProtoState = _Hh3cIsisAdjProtoState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 59, 1, 2, 1, 2),
    _Hh3cIsisAdjProtoState_Type()
)
hh3cIsisAdjProtoState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIsisAdjProtoState.setStatus("current")
_Hh3cIsisCirc_ObjectIdentity = ObjectIdentity
hh3cIsisCirc = _Hh3cIsisCirc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 59, 1, 3)
)
_Hh3cIsisCircTable_Object = MibTable
hh3cIsisCircTable = _Hh3cIsisCircTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 59, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cIsisCircTable.setStatus("current")
_Hh3cIsisCircEntry_Object = MibTableRow
hh3cIsisCircEntry = _Hh3cIsisCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 59, 1, 3, 1, 1)
)
hh3cIsisCircEntry.setIndexNames(
    (0, "HH3C-ISIS-MIB", "hh3cIsisSysInstance"),
    (0, "HH3C-ISIS-MIB", "hh3cIsisCircIndex"),
)
if mibBuilder.loadTexts:
    hh3cIsisCircEntry.setStatus("current")
_Hh3cIsisCircIndex_Type = IndexInteger
_Hh3cIsisCircIndex_Object = MibTableColumn
hh3cIsisCircIndex = _Hh3cIsisCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 59, 1, 3, 1, 1, 1),
    _Hh3cIsisCircIndex_Type()
)
hh3cIsisCircIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIsisCircIndex.setStatus("current")
_Hh3cIsisCircIfIndex_Type = InterfaceIndex
_Hh3cIsisCircIfIndex_Object = MibTableColumn
hh3cIsisCircIfIndex = _Hh3cIsisCircIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 59, 1, 3, 1, 1, 2),
    _Hh3cIsisCircIfIndex_Type()
)
hh3cIsisCircIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIsisCircIfIndex.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cIsisAdjacencyProtocolChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 59, 0, 1)
)
hh3cIsisAdjacencyProtocolChange.setObjects(
      *(("ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("ISIS-MIB", "isisNotificationCircIfIndex"),
        ("ISIS-MIB", "isisPduLspId"),
        ("HH3C-ISIS-MIB", "hh3cIsisAdjProtoType"),
        ("HH3C-ISIS-MIB", "hh3cIsisAdjProtoState"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hh3cIsisAdjacencyProtocolChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-ISIS-MIB",
    **{"hh3cIsis": hh3cIsis,
       "hh3cIsisNotifications": hh3cIsisNotifications,
       "hh3cIsisAdjacencyProtocolChange": hh3cIsisAdjacencyProtocolChange,
       "hh3cIsisObjects": hh3cIsisObjects,
       "hh3cIsisSystem": hh3cIsisSystem,
       "hh3cIsisSysTable": hh3cIsisSysTable,
       "hh3cIsisSysEntry": hh3cIsisSysEntry,
       "hh3cIsisSysInstance": hh3cIsisSysInstance,
       "hh3cIsisNotification": hh3cIsisNotification,
       "hh3cIsisNotificationObjects": hh3cIsisNotificationObjects,
       "hh3cIsisAdjProtoType": hh3cIsisAdjProtoType,
       "hh3cIsisAdjProtoState": hh3cIsisAdjProtoState,
       "hh3cIsisCirc": hh3cIsisCirc,
       "hh3cIsisCircTable": hh3cIsisCircTable,
       "hh3cIsisCircEntry": hh3cIsisCircEntry,
       "hh3cIsisCircIndex": hh3cIsisCircIndex,
       "hh3cIsisCircIfIndex": hh3cIsisCircIfIndex}
)
