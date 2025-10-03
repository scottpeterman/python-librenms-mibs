# SNMP MIB module (CM-TOPOLOGY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\CM-TOPOLOGY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:15:37 2025
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

(neIndex,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "shelfIndex",
    "slotIndex")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "VariablePointer")


# MODULE-IDENTITY

cmTopologyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 9)
)
if mibBuilder.loadTexts:
    cmTopologyMIB.setRevisions(
        ("2008-03-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmTopologyObjects_ObjectIdentity = ObjectIdentity
cmTopologyObjects = _CmTopologyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1)
)


class _CmTopologyRegionId_Type(DisplayString):
    """Custom type cmTopologyRegionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmTopologyRegionId_Type.__name__ = "DisplayString"
_CmTopologyRegionId_Object = MibScalar
cmTopologyRegionId = _CmTopologyRegionId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 1),
    _CmTopologyRegionId_Type()
)
cmTopologyRegionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTopologyRegionId.setStatus("current")


class _CmTopologyRegionDescr_Type(DisplayString):
    """Custom type cmTopologyRegionDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CmTopologyRegionDescr_Type.__name__ = "DisplayString"
_CmTopologyRegionDescr_Object = MibScalar
cmTopologyRegionDescr = _CmTopologyRegionDescr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 2),
    _CmTopologyRegionDescr_Type()
)
cmTopologyRegionDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTopologyRegionDescr.setStatus("current")
_CmTopologyRegionLastUpdateTime_Type = DateAndTime
_CmTopologyRegionLastUpdateTime_Object = MibScalar
cmTopologyRegionLastUpdateTime = _CmTopologyRegionLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 3),
    _CmTopologyRegionLastUpdateTime_Type()
)
cmTopologyRegionLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTopologyRegionLastUpdateTime.setStatus("current")
_CmTopologyItemTable_Object = MibTable
cmTopologyItemTable = _CmTopologyItemTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 4)
)
if mibBuilder.loadTexts:
    cmTopologyItemTable.setStatus("current")
_CmTopologyItemEntry_Object = MibTableRow
cmTopologyItemEntry = _CmTopologyItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 4, 1)
)
cmTopologyItemEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
)
if mibBuilder.loadTexts:
    cmTopologyItemEntry.setStatus("current")


class _CmTopologyItemId_Type(DisplayString):
    """Custom type cmTopologyItemId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmTopologyItemId_Type.__name__ = "DisplayString"
_CmTopologyItemId_Object = MibTableColumn
cmTopologyItemId = _CmTopologyItemId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 4, 1, 1),
    _CmTopologyItemId_Type()
)
cmTopologyItemId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTopologyItemId.setStatus("current")


class _CmTopologyItemDescr_Type(DisplayString):
    """Custom type cmTopologyItemDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CmTopologyItemDescr_Type.__name__ = "DisplayString"
_CmTopologyItemDescr_Object = MibTableColumn
cmTopologyItemDescr = _CmTopologyItemDescr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 4, 1, 2),
    _CmTopologyItemDescr_Type()
)
cmTopologyItemDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTopologyItemDescr.setStatus("current")
_CmTopologyLinkTable_Object = MibTable
cmTopologyLinkTable = _CmTopologyLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 5)
)
if mibBuilder.loadTexts:
    cmTopologyLinkTable.setStatus("current")
_CmTopologyLinkEntry_Object = MibTableRow
cmTopologyLinkEntry = _CmTopologyLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 5, 1)
)
cmTopologyLinkEntry.setIndexNames(
    (0, "CM-TOPOLOGY-MIB", "cmTopologyLinkFromPort"),
)
if mibBuilder.loadTexts:
    cmTopologyLinkEntry.setStatus("current")


class _CmTopologyLinkId_Type(DisplayString):
    """Custom type cmTopologyLinkId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmTopologyLinkId_Type.__name__ = "DisplayString"
_CmTopologyLinkId_Object = MibTableColumn
cmTopologyLinkId = _CmTopologyLinkId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 5, 1, 1),
    _CmTopologyLinkId_Type()
)
cmTopologyLinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTopologyLinkId.setStatus("current")
_CmTopologyLinkFromPort_Type = VariablePointer
_CmTopologyLinkFromPort_Object = MibTableColumn
cmTopologyLinkFromPort = _CmTopologyLinkFromPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 5, 1, 2),
    _CmTopologyLinkFromPort_Type()
)
cmTopologyLinkFromPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTopologyLinkFromPort.setStatus("current")
_CmTopologyLinkToPort_Type = VariablePointer
_CmTopologyLinkToPort_Object = MibTableColumn
cmTopologyLinkToPort = _CmTopologyLinkToPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 5, 1, 3),
    _CmTopologyLinkToPort_Type()
)
cmTopologyLinkToPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTopologyLinkToPort.setStatus("current")
_CmTopologyConformance_ObjectIdentity = ObjectIdentity
cmTopologyConformance = _CmTopologyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 2)
)
_CmTopologyCompliances_ObjectIdentity = ObjectIdentity
cmTopologyCompliances = _CmTopologyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 2, 1)
)
_CmTopologyGroups_ObjectIdentity = ObjectIdentity
cmTopologyGroups = _CmTopologyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 2, 2)
)

# Managed Objects groups

cmTopologyObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 2, 2, 1)
)
cmTopologyObjectGroup.setObjects(
      *(("CM-TOPOLOGY-MIB", "cmTopologyRegionId"),
        ("CM-TOPOLOGY-MIB", "cmTopologyRegionDescr"),
        ("CM-TOPOLOGY-MIB", "cmTopologyRegionLastUpdateTime"),
        ("CM-TOPOLOGY-MIB", "cmTopologyItemId"),
        ("CM-TOPOLOGY-MIB", "cmTopologyItemDescr"),
        ("CM-TOPOLOGY-MIB", "cmTopologyLinkId"),
        ("CM-TOPOLOGY-MIB", "cmTopologyLinkFromPort"),
        ("CM-TOPOLOGY-MIB", "cmTopologyLinkToPort"))
)
if mibBuilder.loadTexts:
    cmTopologyObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmTopologyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 2, 1, 1)
)
cmTopologyCompliance.setObjects(
    ("CM-TOPOLOGY-MIB", "cmTopologyObjectGroup")
)
if mibBuilder.loadTexts:
    cmTopologyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CM-TOPOLOGY-MIB",
    **{"cmTopologyMIB": cmTopologyMIB,
       "cmTopologyObjects": cmTopologyObjects,
       "cmTopologyRegionId": cmTopologyRegionId,
       "cmTopologyRegionDescr": cmTopologyRegionDescr,
       "cmTopologyRegionLastUpdateTime": cmTopologyRegionLastUpdateTime,
       "cmTopologyItemTable": cmTopologyItemTable,
       "cmTopologyItemEntry": cmTopologyItemEntry,
       "cmTopologyItemId": cmTopologyItemId,
       "cmTopologyItemDescr": cmTopologyItemDescr,
       "cmTopologyLinkTable": cmTopologyLinkTable,
       "cmTopologyLinkEntry": cmTopologyLinkEntry,
       "cmTopologyLinkId": cmTopologyLinkId,
       "cmTopologyLinkFromPort": cmTopologyLinkFromPort,
       "cmTopologyLinkToPort": cmTopologyLinkToPort,
       "cmTopologyConformance": cmTopologyConformance,
       "cmTopologyCompliances": cmTopologyCompliances,
       "cmTopologyCompliance": cmTopologyCompliance,
       "cmTopologyGroups": cmTopologyGroups,
       "cmTopologyObjectGroup": cmTopologyObjectGroup}
)
