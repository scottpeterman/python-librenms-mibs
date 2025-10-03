# SNMP MIB module (TN-MIRRORING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-MIRRORING-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:59 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnMirroringMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 25)
)
if mibBuilder.loadTexts:
    tnMirroringMIB.setRevisions(
        ("2012-08-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnMirroringMIBObjects_ObjectIdentity = ObjectIdentity
tnMirroringMIBObjects = _TnMirroringMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 25, 1)
)
_TnMirroringMgmt_ObjectIdentity = ObjectIdentity
tnMirroringMgmt = _TnMirroringMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 25, 1, 1)
)
_TnMirroringGroupTable_Object = MibTable
tnMirroringGroupTable = _TnMirroringGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 25, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnMirroringGroupTable.setStatus("current")
_TnMirroringGroupEntry_Object = MibTableRow
tnMirroringGroupEntry = _TnMirroringGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 25, 1, 1, 1, 1)
)
tnMirroringGroupEntry.setIndexNames(
    (0, "TN-MIRRORING-MIB", "tnMirroringGroupID"),
)
if mibBuilder.loadTexts:
    tnMirroringGroupEntry.setStatus("current")
_TnMirroringGroupID_Type = Integer32
_TnMirroringGroupID_Object = MibTableColumn
tnMirroringGroupID = _TnMirroringGroupID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 25, 1, 1, 1, 1, 1),
    _TnMirroringGroupID_Type()
)
tnMirroringGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMirroringGroupID.setStatus("current")
_TnMirroringGroupDestIfIndex_Type = InterfaceIndex
_TnMirroringGroupDestIfIndex_Object = MibTableColumn
tnMirroringGroupDestIfIndex = _TnMirroringGroupDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 25, 1, 1, 1, 1, 2),
    _TnMirroringGroupDestIfIndex_Type()
)
tnMirroringGroupDestIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMirroringGroupDestIfIndex.setStatus("current")
_TnMirroringIfTable_Object = MibTable
tnMirroringIfTable = _TnMirroringIfTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 25, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnMirroringIfTable.setStatus("current")
_TnMirroringIfEntry_Object = MibTableRow
tnMirroringIfEntry = _TnMirroringIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 25, 1, 1, 2, 1)
)
tnMirroringIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnMirroringIfEntry.setStatus("current")
_TnMirroringIfGroupID_Type = Integer32
_TnMirroringIfGroupID_Object = MibTableColumn
tnMirroringIfGroupID = _TnMirroringIfGroupID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 25, 1, 1, 2, 1, 1),
    _TnMirroringIfGroupID_Type()
)
tnMirroringIfGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMirroringIfGroupID.setStatus("current")


class _TnMirroringIfMode_Type(Integer32):
    """Custom type tnMirroringIfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10,
              20,
              30)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("onlyTx", 10),
          ("onlyRx", 20),
          ("bothTxRx", 30))
    )


_TnMirroringIfMode_Type.__name__ = "Integer32"
_TnMirroringIfMode_Object = MibTableColumn
tnMirroringIfMode = _TnMirroringIfMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 25, 1, 1, 2, 1, 2),
    _TnMirroringIfMode_Type()
)
tnMirroringIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMirroringIfMode.setStatus("current")
_TnMirroringMIBNotifications_ObjectIdentity = ObjectIdentity
tnMirroringMIBNotifications = _TnMirroringMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 25, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-MIRRORING-MIB",
    **{"tnMirroringMIB": tnMirroringMIB,
       "tnMirroringMIBObjects": tnMirroringMIBObjects,
       "tnMirroringMgmt": tnMirroringMgmt,
       "tnMirroringGroupTable": tnMirroringGroupTable,
       "tnMirroringGroupEntry": tnMirroringGroupEntry,
       "tnMirroringGroupID": tnMirroringGroupID,
       "tnMirroringGroupDestIfIndex": tnMirroringGroupDestIfIndex,
       "tnMirroringIfTable": tnMirroringIfTable,
       "tnMirroringIfEntry": tnMirroringIfEntry,
       "tnMirroringIfGroupID": tnMirroringIfGroupID,
       "tnMirroringIfMode": tnMirroringIfMode,
       "tnMirroringMIBNotifications": tnMirroringMIBNotifications}
)
