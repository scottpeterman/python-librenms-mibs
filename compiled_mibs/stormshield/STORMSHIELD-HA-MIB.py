# SNMP MIB module (STORMSHIELD-HA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\stormshield\STORMSHIELD-HA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:05 2025
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

(stormshieldMIB,) = mibBuilder.importSymbols(
    "STORMSHIELD-SMI-MIB",
    "stormshieldMIB")


# MODULE-IDENTITY

snsHA = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11)
)
if mibBuilder.loadTexts:
    snsHA.setRevisions(
        ("2017-02-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnsNbNode_Type = Integer32
_SnsNbNode_Object = MibScalar
snsNbNode = _SnsNbNode_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 1),
    _SnsNbNode_Type()
)
snsNbNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsNbNode.setStatus("current")
_SnsNbDeadNode_Type = Integer32
_SnsNbDeadNode_Object = MibScalar
snsNbDeadNode = _SnsNbDeadNode_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 2),
    _SnsNbDeadNode_Type()
)
snsNbDeadNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsNbDeadNode.setStatus("current")
_SnsNbActiveNode_Type = Integer32
_SnsNbActiveNode_Object = MibScalar
snsNbActiveNode = _SnsNbActiveNode_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 3),
    _SnsNbActiveNode_Type()
)
snsNbActiveNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsNbActiveNode.setStatus("current")
_SnsNbHALinks_Type = Integer32
_SnsNbHALinks_Object = MibScalar
snsNbHALinks = _SnsNbHALinks_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 5),
    _SnsNbHALinks_Type()
)
snsNbHALinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsNbHALinks.setStatus("current")
_SnsNbFaultyHALinks_Type = Integer32
_SnsNbFaultyHALinks_Object = MibScalar
snsNbFaultyHALinks = _SnsNbFaultyHALinks_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 6),
    _SnsNbFaultyHALinks_Type()
)
snsNbFaultyHALinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsNbFaultyHALinks.setStatus("current")
_SnsNodeTable_Object = MibTable
snsNodeTable = _SnsNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 7)
)
if mibBuilder.loadTexts:
    snsNodeTable.setStatus("current")
_SnsNode_Object = MibTableRow
snsNode = _SnsNode_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1)
)
snsNode.setIndexNames(
    (0, "STORMSHIELD-HA-MIB", "snsNodeIndex"),
)
if mibBuilder.loadTexts:
    snsNode.setStatus("current")


class _SnsNodeIndex_Type(Integer32):
    """Custom type snsNodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SnsNodeIndex_Type.__name__ = "Integer32"
_SnsNodeIndex_Object = MibTableColumn
snsNodeIndex = _SnsNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 1),
    _SnsNodeIndex_Type()
)
snsNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snsNodeIndex.setStatus("current")
_SnsFwSerial_Type = DisplayString
_SnsFwSerial_Object = MibTableColumn
snsFwSerial = _SnsFwSerial_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 2),
    _SnsFwSerial_Type()
)
snsFwSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsFwSerial.setStatus("current")
_SnsOnline_Type = TruthValue
_SnsOnline_Object = MibTableColumn
snsOnline = _SnsOnline_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 3),
    _SnsOnline_Type()
)
snsOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsOnline.setStatus("current")
_SnsModel_Type = DisplayString
_SnsModel_Object = MibTableColumn
snsModel = _SnsModel_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 4),
    _SnsModel_Type()
)
snsModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsModel.setStatus("current")
_SnsVersion_Type = DisplayString
_SnsVersion_Object = MibTableColumn
snsVersion = _SnsVersion_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 5),
    _SnsVersion_Type()
)
snsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVersion.setStatus("current")
_SnsHALicence_Type = DisplayString
_SnsHALicence_Object = MibTableColumn
snsHALicence = _SnsHALicence_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 6),
    _SnsHALicence_Type()
)
snsHALicence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsHALicence.setStatus("current")
_SnsHAQuality_Type = Integer32
_SnsHAQuality_Object = MibTableColumn
snsHAQuality = _SnsHAQuality_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 7),
    _SnsHAQuality_Type()
)
snsHAQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsHAQuality.setStatus("current")
_SnsHAPriority_Type = Integer32
_SnsHAPriority_Object = MibTableColumn
snsHAPriority = _SnsHAPriority_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 8),
    _SnsHAPriority_Type()
)
snsHAPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsHAPriority.setStatus("current")
_SnsHAStatusForced_Type = Integer32
_SnsHAStatusForced_Object = MibTableColumn
snsHAStatusForced = _SnsHAStatusForced_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 9),
    _SnsHAStatusForced_Type()
)
snsHAStatusForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsHAStatusForced.setStatus("current")
_SnsHAActive_Type = TruthValue
_SnsHAActive_Object = MibTableColumn
snsHAActive = _SnsHAActive_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 10),
    _SnsHAActive_Type()
)
snsHAActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsHAActive.setStatus("current")
_SnsUptime_Type = Integer32
_SnsUptime_Object = MibTableColumn
snsUptime = _SnsUptime_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 11),
    _SnsUptime_Type()
)
snsUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsUptime.setStatus("current")
_SnsHASyncStatus_Type = Integer32
_SnsHASyncStatus_Object = MibScalar
snsHASyncStatus = _SnsHASyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 8),
    _SnsHASyncStatus_Type()
)
snsHASyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsHASyncStatus.setStatus("current")
_SnsHAFwAdminRevison_Type = DisplayString
_SnsHAFwAdminRevison_Object = MibScalar
snsHAFwAdminRevison = _SnsHAFwAdminRevison_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 9),
    _SnsHAFwAdminRevison_Type()
)
snsHAFwAdminRevison.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsHAFwAdminRevison.setStatus("current")
_SnsNodePowerSupplyTable_Object = MibTable
snsNodePowerSupplyTable = _SnsNodePowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 10)
)
if mibBuilder.loadTexts:
    snsNodePowerSupplyTable.setStatus("current")
_SnsNodePowerSupplyEntry_Object = MibTableRow
snsNodePowerSupplyEntry = _SnsNodePowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 10, 1)
)
snsNodePowerSupplyEntry.setIndexNames(
    (0, "STORMSHIELD-HA-MIB", "snsNodeIndex"),
    (0, "STORMSHIELD-HA-MIB", "snsNodePowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    snsNodePowerSupplyEntry.setStatus("current")


class _SnsNodePowerSupplyIndex_Type(Integer32):
    """Custom type snsNodePowerSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnsNodePowerSupplyIndex_Type.__name__ = "Integer32"
_SnsNodePowerSupplyIndex_Object = MibTableColumn
snsNodePowerSupplyIndex = _SnsNodePowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 10, 1, 1),
    _SnsNodePowerSupplyIndex_Type()
)
snsNodePowerSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snsNodePowerSupplyIndex.setStatus("current")
_SnsNodePowerSupplyPowered_Type = TruthValue
_SnsNodePowerSupplyPowered_Object = MibTableColumn
snsNodePowerSupplyPowered = _SnsNodePowerSupplyPowered_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 10, 1, 2),
    _SnsNodePowerSupplyPowered_Type()
)
snsNodePowerSupplyPowered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsNodePowerSupplyPowered.setStatus("current")
_SnsNodeDiskTable_Object = MibTable
snsNodeDiskTable = _SnsNodeDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 11)
)
if mibBuilder.loadTexts:
    snsNodeDiskTable.setStatus("current")
_SnsNodeDiskEntry_Object = MibTableRow
snsNodeDiskEntry = _SnsNodeDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 11, 1)
)
snsNodeDiskEntry.setIndexNames(
    (0, "STORMSHIELD-HA-MIB", "snsNodeIndex"),
    (0, "STORMSHIELD-HA-MIB", "snsNodeDiskIndex"),
)
if mibBuilder.loadTexts:
    snsNodeDiskEntry.setStatus("current")


class _SnsNodeDiskIndex_Type(Integer32):
    """Custom type snsNodeDiskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnsNodeDiskIndex_Type.__name__ = "Integer32"
_SnsNodeDiskIndex_Object = MibTableColumn
snsNodeDiskIndex = _SnsNodeDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 11, 1, 1),
    _SnsNodeDiskIndex_Type()
)
snsNodeDiskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snsNodeDiskIndex.setStatus("current")
_SnsNodeDiskName_Type = DisplayString
_SnsNodeDiskName_Object = MibTableColumn
snsNodeDiskName = _SnsNodeDiskName_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 11, 1, 2),
    _SnsNodeDiskName_Type()
)
snsNodeDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsNodeDiskName.setStatus("current")
_SnsNodeDiskSmartResult_Type = DisplayString
_SnsNodeDiskSmartResult_Object = MibTableColumn
snsNodeDiskSmartResult = _SnsNodeDiskSmartResult_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 11, 1, 3),
    _SnsNodeDiskSmartResult_Type()
)
snsNodeDiskSmartResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsNodeDiskSmartResult.setStatus("current")


class _SnsNodeDiskIsRaid_Type(Integer32):
    """Custom type snsNodeDiskIsRaid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SnsNodeDiskIsRaid_Type.__name__ = "Integer32"
_SnsNodeDiskIsRaid_Object = MibTableColumn
snsNodeDiskIsRaid = _SnsNodeDiskIsRaid_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 11, 1, 4),
    _SnsNodeDiskIsRaid_Type()
)
snsNodeDiskIsRaid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsNodeDiskIsRaid.setStatus("current")
_SnsNodeDiskRaidStatus_Type = DisplayString
_SnsNodeDiskRaidStatus_Object = MibTableColumn
snsNodeDiskRaidStatus = _SnsNodeDiskRaidStatus_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 11, 1, 5),
    _SnsNodeDiskRaidStatus_Type()
)
snsNodeDiskRaidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsNodeDiskRaidStatus.setStatus("current")
_SnsNodeDiskPosition_Type = DisplayString
_SnsNodeDiskPosition_Object = MibTableColumn
snsNodeDiskPosition = _SnsNodeDiskPosition_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 11, 1, 6),
    _SnsNodeDiskPosition_Type()
)
snsNodeDiskPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsNodeDiskPosition.setStatus("current")
_SnsNodeCpuTable_Object = MibTable
snsNodeCpuTable = _SnsNodeCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 12)
)
if mibBuilder.loadTexts:
    snsNodeCpuTable.setStatus("current")
_SnsNodeCpuEntry_Object = MibTableRow
snsNodeCpuEntry = _SnsNodeCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 12, 1)
)
snsNodeCpuEntry.setIndexNames(
    (0, "STORMSHIELD-HA-MIB", "snsNodeIndex"),
    (0, "STORMSHIELD-HA-MIB", "snsNodeCpuIndex"),
)
if mibBuilder.loadTexts:
    snsNodeCpuEntry.setStatus("current")


class _SnsNodeCpuIndex_Type(Integer32):
    """Custom type snsNodeCpuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnsNodeCpuIndex_Type.__name__ = "Integer32"
_SnsNodeCpuIndex_Object = MibTableColumn
snsNodeCpuIndex = _SnsNodeCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 12, 1, 1),
    _SnsNodeCpuIndex_Type()
)
snsNodeCpuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snsNodeCpuIndex.setStatus("current")
_SnsNodeCpuTemp_Type = Integer32
_SnsNodeCpuTemp_Object = MibTableColumn
snsNodeCpuTemp = _SnsNodeCpuTemp_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 11, 12, 1, 2),
    _SnsNodeCpuTemp_Type()
)
snsNodeCpuTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsNodeCpuTemp.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STORMSHIELD-HA-MIB",
    **{"snsHA": snsHA,
       "snsNbNode": snsNbNode,
       "snsNbDeadNode": snsNbDeadNode,
       "snsNbActiveNode": snsNbActiveNode,
       "snsNbHALinks": snsNbHALinks,
       "snsNbFaultyHALinks": snsNbFaultyHALinks,
       "snsNodeTable": snsNodeTable,
       "snsNode": snsNode,
       "snsNodeIndex": snsNodeIndex,
       "snsFwSerial": snsFwSerial,
       "snsOnline": snsOnline,
       "snsModel": snsModel,
       "snsVersion": snsVersion,
       "snsHALicence": snsHALicence,
       "snsHAQuality": snsHAQuality,
       "snsHAPriority": snsHAPriority,
       "snsHAStatusForced": snsHAStatusForced,
       "snsHAActive": snsHAActive,
       "snsUptime": snsUptime,
       "snsHASyncStatus": snsHASyncStatus,
       "snsHAFwAdminRevison": snsHAFwAdminRevison,
       "snsNodePowerSupplyTable": snsNodePowerSupplyTable,
       "snsNodePowerSupplyEntry": snsNodePowerSupplyEntry,
       "snsNodePowerSupplyIndex": snsNodePowerSupplyIndex,
       "snsNodePowerSupplyPowered": snsNodePowerSupplyPowered,
       "snsNodeDiskTable": snsNodeDiskTable,
       "snsNodeDiskEntry": snsNodeDiskEntry,
       "snsNodeDiskIndex": snsNodeDiskIndex,
       "snsNodeDiskName": snsNodeDiskName,
       "snsNodeDiskSmartResult": snsNodeDiskSmartResult,
       "snsNodeDiskIsRaid": snsNodeDiskIsRaid,
       "snsNodeDiskRaidStatus": snsNodeDiskRaidStatus,
       "snsNodeDiskPosition": snsNodeDiskPosition,
       "snsNodeCpuTable": snsNodeCpuTable,
       "snsNodeCpuEntry": snsNodeCpuEntry,
       "snsNodeCpuIndex": snsNodeCpuIndex,
       "snsNodeCpuTemp": snsNodeCpuTemp}
)
