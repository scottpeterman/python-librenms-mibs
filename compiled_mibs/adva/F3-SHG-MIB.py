# SNMP MIB module (F3-SHG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\F3-SHG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:16:50 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(neIndex,) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex")

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
 RowStatus,
 StorageType,
 TextualConvention,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "VariablePointer")


# MODULE-IDENTITY

f3SHGMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27)
)
if mibBuilder.loadTexts:
    f3SHGMIB.setRevisions(
        ("2012-12-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F3ShgConfigObjects_ObjectIdentity = ObjectIdentity
f3ShgConfigObjects = _F3ShgConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1)
)
_F3ShgTable_Object = MibTable
f3ShgTable = _F3ShgTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 1)
)
if mibBuilder.loadTexts:
    f3ShgTable.setStatus("current")
_F3ShgEntry_Object = MibTableRow
f3ShgEntry = _F3ShgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 1, 1)
)
f3ShgEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SHG-MIB", "f3ShgIndex"),
)
if mibBuilder.loadTexts:
    f3ShgEntry.setStatus("current")
_F3ShgIndex_Type = Unsigned32
_F3ShgIndex_Object = MibTableColumn
f3ShgIndex = _F3ShgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 1, 1, 1),
    _F3ShgIndex_Type()
)
f3ShgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3ShgIndex.setStatus("current")


class _F3ShgAlias_Type(DisplayString):
    """Custom type f3ShgAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3ShgAlias_Type.__name__ = "DisplayString"
_F3ShgAlias_Object = MibTableColumn
f3ShgAlias = _F3ShgAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 1, 1, 2),
    _F3ShgAlias_Type()
)
f3ShgAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ShgAlias.setStatus("current")
_F3ShgStorageType_Type = StorageType
_F3ShgStorageType_Object = MibTableColumn
f3ShgStorageType = _F3ShgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 1, 1, 3),
    _F3ShgStorageType_Type()
)
f3ShgStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ShgStorageType.setStatus("current")
_F3ShgRowStatus_Type = RowStatus
_F3ShgRowStatus_Object = MibTableColumn
f3ShgRowStatus = _F3ShgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 1, 1, 4),
    _F3ShgRowStatus_Type()
)
f3ShgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ShgRowStatus.setStatus("current")
_F3ShgMemberPortTable_Object = MibTable
f3ShgMemberPortTable = _F3ShgMemberPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 2)
)
if mibBuilder.loadTexts:
    f3ShgMemberPortTable.setStatus("current")
_F3ShgMemberPortEntry_Object = MibTableRow
f3ShgMemberPortEntry = _F3ShgMemberPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 2, 1)
)
f3ShgMemberPortEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SHG-MIB", "f3ShgIndex"),
    (0, "F3-SHG-MIB", "f3ShgMemberPort"),
)
if mibBuilder.loadTexts:
    f3ShgMemberPortEntry.setStatus("current")
_F3ShgMemberPort_Type = VariablePointer
_F3ShgMemberPort_Object = MibTableColumn
f3ShgMemberPort = _F3ShgMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 2, 1, 1),
    _F3ShgMemberPort_Type()
)
f3ShgMemberPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3ShgMemberPort.setStatus("current")
_F3ShgMemberPortStorageType_Type = StorageType
_F3ShgMemberPortStorageType_Object = MibTableColumn
f3ShgMemberPortStorageType = _F3ShgMemberPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 2, 1, 2),
    _F3ShgMemberPortStorageType_Type()
)
f3ShgMemberPortStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ShgMemberPortStorageType.setStatus("current")
_F3ShgMemberPortRowStatus_Type = RowStatus
_F3ShgMemberPortRowStatus_Object = MibTableColumn
f3ShgMemberPortRowStatus = _F3ShgMemberPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 2, 1, 3),
    _F3ShgMemberPortRowStatus_Type()
)
f3ShgMemberPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ShgMemberPortRowStatus.setStatus("current")
_F3ShgMemberFlowTable_Object = MibTable
f3ShgMemberFlowTable = _F3ShgMemberFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 3)
)
if mibBuilder.loadTexts:
    f3ShgMemberFlowTable.setStatus("current")
_F3ShgMemberFlowEntry_Object = MibTableRow
f3ShgMemberFlowEntry = _F3ShgMemberFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 3, 1)
)
f3ShgMemberFlowEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SHG-MIB", "f3ShgIndex"),
    (0, "F3-SHG-MIB", "f3ShgMemberFlow"),
)
if mibBuilder.loadTexts:
    f3ShgMemberFlowEntry.setStatus("current")
_F3ShgMemberFlow_Type = VariablePointer
_F3ShgMemberFlow_Object = MibTableColumn
f3ShgMemberFlow = _F3ShgMemberFlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 3, 1, 1),
    _F3ShgMemberFlow_Type()
)
f3ShgMemberFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ShgMemberFlow.setStatus("current")
_F3ShgMemberFlowPointTable_Object = MibTable
f3ShgMemberFlowPointTable = _F3ShgMemberFlowPointTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 4)
)
if mibBuilder.loadTexts:
    f3ShgMemberFlowPointTable.setStatus("current")
_F3ShgMemberFlowPointEntry_Object = MibTableRow
f3ShgMemberFlowPointEntry = _F3ShgMemberFlowPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 4, 1)
)
f3ShgMemberFlowPointEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-SHG-MIB", "f3ShgIndex"),
    (0, "F3-SHG-MIB", "f3ShgMemberFlowPoint"),
)
if mibBuilder.loadTexts:
    f3ShgMemberFlowPointEntry.setStatus("current")
_F3ShgMemberFlowPoint_Type = VariablePointer
_F3ShgMemberFlowPoint_Object = MibTableColumn
f3ShgMemberFlowPoint = _F3ShgMemberFlowPoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 1, 4, 1, 1),
    _F3ShgMemberFlowPoint_Type()
)
f3ShgMemberFlowPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ShgMemberFlowPoint.setStatus("current")
_F3ShgConformance_ObjectIdentity = ObjectIdentity
f3ShgConformance = _F3ShgConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 2)
)
_F3ShgCompliances_ObjectIdentity = ObjectIdentity
f3ShgCompliances = _F3ShgCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 2, 1)
)
_F3ShgGroups_ObjectIdentity = ObjectIdentity
f3ShgGroups = _F3ShgGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 2, 2)
)

# Managed Objects groups

f3ShgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 2, 2, 1)
)
f3ShgGroup.setObjects(
      *(("F3-SHG-MIB", "f3ShgAlias"),
        ("F3-SHG-MIB", "f3ShgStorageType"),
        ("F3-SHG-MIB", "f3ShgRowStatus"))
)
if mibBuilder.loadTexts:
    f3ShgGroup.setStatus("current")

f3ShgMemberPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 2, 2, 2)
)
f3ShgMemberPortGroup.setObjects(
      *(("F3-SHG-MIB", "f3ShgMemberPortStorageType"),
        ("F3-SHG-MIB", "f3ShgMemberPortRowStatus"))
)
if mibBuilder.loadTexts:
    f3ShgMemberPortGroup.setStatus("current")

f3ShgMemberFlowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 2, 2, 3)
)
f3ShgMemberFlowGroup.setObjects(
    ("F3-SHG-MIB", "f3ShgMemberFlow")
)
if mibBuilder.loadTexts:
    f3ShgMemberFlowGroup.setStatus("current")

f3ShgMemberFlowPointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 2, 2, 4)
)
f3ShgMemberFlowPointGroup.setObjects(
    ("F3-SHG-MIB", "f3ShgMemberFlowPoint")
)
if mibBuilder.loadTexts:
    f3ShgMemberFlowPointGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f3ShgCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 27, 2, 1, 1)
)
f3ShgCompliance.setObjects(
      *(("F3-SHG-MIB", "f3ShgGroup"),
        ("F3-SHG-MIB", "f3ShgMemberPortGroup"),
        ("F3-SHG-MIB", "f3ShgMemberFlowGroup"),
        ("F3-SHG-MIB", "f3ShgMemberFlowPointGroup"))
)
if mibBuilder.loadTexts:
    f3ShgCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-SHG-MIB",
    **{"f3SHGMIB": f3SHGMIB,
       "f3ShgConfigObjects": f3ShgConfigObjects,
       "f3ShgTable": f3ShgTable,
       "f3ShgEntry": f3ShgEntry,
       "f3ShgIndex": f3ShgIndex,
       "f3ShgAlias": f3ShgAlias,
       "f3ShgStorageType": f3ShgStorageType,
       "f3ShgRowStatus": f3ShgRowStatus,
       "f3ShgMemberPortTable": f3ShgMemberPortTable,
       "f3ShgMemberPortEntry": f3ShgMemberPortEntry,
       "f3ShgMemberPort": f3ShgMemberPort,
       "f3ShgMemberPortStorageType": f3ShgMemberPortStorageType,
       "f3ShgMemberPortRowStatus": f3ShgMemberPortRowStatus,
       "f3ShgMemberFlowTable": f3ShgMemberFlowTable,
       "f3ShgMemberFlowEntry": f3ShgMemberFlowEntry,
       "f3ShgMemberFlow": f3ShgMemberFlow,
       "f3ShgMemberFlowPointTable": f3ShgMemberFlowPointTable,
       "f3ShgMemberFlowPointEntry": f3ShgMemberFlowPointEntry,
       "f3ShgMemberFlowPoint": f3ShgMemberFlowPoint,
       "f3ShgConformance": f3ShgConformance,
       "f3ShgCompliances": f3ShgCompliances,
       "f3ShgCompliance": f3ShgCompliance,
       "f3ShgGroups": f3ShgGroups,
       "f3ShgGroup": f3ShgGroup,
       "f3ShgMemberPortGroup": f3ShgMemberPortGroup,
       "f3ShgMemberFlowGroup": f3ShgMemberFlowGroup,
       "f3ShgMemberFlowPointGroup": f3ShgMemberFlowPointGroup}
)
