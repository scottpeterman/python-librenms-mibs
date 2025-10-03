# SNMP MIB module (UBQS-MISC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubiquoss\UBQS-MISC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:22 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(ubiMgmtv2,) = mibBuilder.importSymbols(
    "UBQS-SMI",
    "ubiMgmtv2")


# MODULE-IDENTITY

ubiMiscMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 22)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UbiMiscMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ubiMiscMIBNotificationPrefix = _UbiMiscMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 22, 0)
)
_UbiMiscMIBObjects_ObjectIdentity = ObjectIdentity
ubiMiscMIBObjects = _UbiMiscMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 22, 1)
)
_UbiMiscRemoteReset_ObjectIdentity = ObjectIdentity
ubiMiscRemoteReset = _UbiMiscRemoteReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 22, 1, 1)
)


class _UbiMiscRemoteResetEnabled_Type(TruthValue):
    """Custom type ubiMiscRemoteResetEnabled based on TruthValue"""
    defaultValue = 2


_UbiMiscRemoteResetEnabled_Type.__name__ = "TruthValue"
_UbiMiscRemoteResetEnabled_Object = MibScalar
ubiMiscRemoteResetEnabled = _UbiMiscRemoteResetEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 22, 1, 1, 1),
    _UbiMiscRemoteResetEnabled_Type()
)
ubiMiscRemoteResetEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiMiscRemoteResetEnabled.setStatus("current")
_UbiMiscPortRemoteResetTable_Object = MibTable
ubiMiscPortRemoteResetTable = _UbiMiscPortRemoteResetTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 22, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ubiMiscPortRemoteResetTable.setStatus("current")
_UbiMiscPortRemoteResetEntry_Object = MibTableRow
ubiMiscPortRemoteResetEntry = _UbiMiscPortRemoteResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 22, 1, 1, 2, 1)
)
ubiMiscPortRemoteResetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ubiMiscPortRemoteResetEntry.setStatus("current")


class _UbiMiscPortRemoteReset_Type(Integer32):
    """Custom type ubiMiscPortRemoteReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_UbiMiscPortRemoteReset_Type.__name__ = "Integer32"
_UbiMiscPortRemoteReset_Object = MibTableColumn
ubiMiscPortRemoteReset = _UbiMiscPortRemoteReset_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 22, 1, 1, 2, 1, 1),
    _UbiMiscPortRemoteReset_Type()
)
ubiMiscPortRemoteReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiMiscPortRemoteReset.setStatus("current")
_UbiMacSpoofing_ObjectIdentity = ObjectIdentity
ubiMacSpoofing = _UbiMacSpoofing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 22, 1, 2)
)
_UbiMacSpoofingEnabled_Type = TruthValue
_UbiMacSpoofingEnabled_Object = MibScalar
ubiMacSpoofingEnabled = _UbiMacSpoofingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 22, 1, 2, 1),
    _UbiMacSpoofingEnabled_Type()
)
ubiMacSpoofingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiMacSpoofingEnabled.setStatus("current")
_UbiMiscStoreHistory_ObjectIdentity = ObjectIdentity
ubiMiscStoreHistory = _UbiMiscStoreHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 22, 1, 3)
)
_UbiMiscStoreHistoryEnabled_Type = TruthValue
_UbiMiscStoreHistoryEnabled_Object = MibScalar
ubiMiscStoreHistoryEnabled = _UbiMiscStoreHistoryEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 22, 1, 3, 1),
    _UbiMiscStoreHistoryEnabled_Type()
)
ubiMiscStoreHistoryEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiMiscStoreHistoryEnabled.setStatus("current")
_UbiMiscMIBConformance_ObjectIdentity = ObjectIdentity
ubiMiscMIBConformance = _UbiMiscMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 22, 2)
)
_UbiMiscMIBCompliances_ObjectIdentity = ObjectIdentity
ubiMiscMIBCompliances = _UbiMiscMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 22, 2, 1)
)
_UbiMiscMIBGroups_ObjectIdentity = ObjectIdentity
ubiMiscMIBGroups = _UbiMiscMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 22, 2, 2)
)

# Managed Objects groups

ubiSysRemoteResetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7800, 100, 22, 2, 2, 1)
)
ubiSysRemoteResetGroup.setObjects(
      *(("UBQS-MISC-MIB", "ubiMiscRemoteResetEnabled"),
        ("UBQS-MISC-MIB", "ubiMiscPortRemoteReset"))
)
if mibBuilder.loadTexts:
    ubiSysRemoteResetGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ubiMiscMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7800, 100, 22, 2, 1, 1)
)
ubiMiscMIBCompliance.setObjects(
      *(("UBQS-MISC-MIB", "ubiSysRemoteResetGroup"),
        ("UBQS-MISC-MIB", "ubiSysRemoteResetGroup"))
)
if mibBuilder.loadTexts:
    ubiMiscMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBQS-MISC-MIB",
    **{"ubiMiscMIB": ubiMiscMIB,
       "ubiMiscMIBNotificationPrefix": ubiMiscMIBNotificationPrefix,
       "ubiMiscMIBObjects": ubiMiscMIBObjects,
       "ubiMiscRemoteReset": ubiMiscRemoteReset,
       "ubiMiscRemoteResetEnabled": ubiMiscRemoteResetEnabled,
       "ubiMiscPortRemoteResetTable": ubiMiscPortRemoteResetTable,
       "ubiMiscPortRemoteResetEntry": ubiMiscPortRemoteResetEntry,
       "ubiMiscPortRemoteReset": ubiMiscPortRemoteReset,
       "ubiMacSpoofing": ubiMacSpoofing,
       "ubiMacSpoofingEnabled": ubiMacSpoofingEnabled,
       "ubiMiscStoreHistory": ubiMiscStoreHistory,
       "ubiMiscStoreHistoryEnabled": ubiMiscStoreHistoryEnabled,
       "ubiMiscMIBConformance": ubiMiscMIBConformance,
       "ubiMiscMIBCompliances": ubiMiscMIBCompliances,
       "ubiMiscMIBCompliance": ubiMiscMIBCompliance,
       "ubiMiscMIBGroups": ubiMiscMIBGroups,
       "ubiSysRemoteResetGroup": ubiSysRemoteResetGroup}
)
