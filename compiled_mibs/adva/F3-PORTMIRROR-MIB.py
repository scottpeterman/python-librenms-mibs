# SNMP MIB module (F3-PORTMIRROR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\F3-PORTMIRROR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:16:41 2025
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

(PerfCounter64,
 TrafficDirection,
 VlanId) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "PerfCounter64",
    "TrafficDirection",
    "VlanId")

(neIndex,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "shelfIndex",
    "slotIndex")

(cmEthernetAccPortEntry,) = mibBuilder.importSymbols(
    "CM-FACILITY-MIB",
    "cmEthernetAccPortEntry")

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
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3PortMirrorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29)
)
if mibBuilder.loadTexts:
    f3PortMirrorMIB.setRevisions(
        ("2013-10-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MirroredFramesAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("deny", 2))
    )



class PortMirrorStatsAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("clearStats", 2))
    )



# MIB Managed Objects in the order of their OIDs

_F3PortMirrorConfigObjects_ObjectIdentity = ObjectIdentity
f3PortMirrorConfigObjects = _F3PortMirrorConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1)
)
_F3MirrorSessionTable_Object = MibTable
f3MirrorSessionTable = _F3MirrorSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1)
)
if mibBuilder.loadTexts:
    f3MirrorSessionTable.setStatus("current")
_F3MirrorSessionEntry_Object = MibTableRow
f3MirrorSessionEntry = _F3MirrorSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1)
)
f3MirrorSessionEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PORTMIRROR-MIB", "f3MirrorSessionIndex"),
)
if mibBuilder.loadTexts:
    f3MirrorSessionEntry.setStatus("current")


class _F3MirrorSessionIndex_Type(Integer32):
    """Custom type f3MirrorSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_F3MirrorSessionIndex_Type.__name__ = "Integer32"
_F3MirrorSessionIndex_Object = MibTableColumn
f3MirrorSessionIndex = _F3MirrorSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 1),
    _F3MirrorSessionIndex_Type()
)
f3MirrorSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3MirrorSessionIndex.setStatus("current")
_F3MirrorSessionSourcePort_Type = VariablePointer
_F3MirrorSessionSourcePort_Object = MibTableColumn
f3MirrorSessionSourcePort = _F3MirrorSessionSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 2),
    _F3MirrorSessionSourcePort_Type()
)
f3MirrorSessionSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorSessionSourcePort.setStatus("current")
_F3MirrorSessionMonitorPort_Type = VariablePointer
_F3MirrorSessionMonitorPort_Object = MibTableColumn
f3MirrorSessionMonitorPort = _F3MirrorSessionMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 3),
    _F3MirrorSessionMonitorPort_Type()
)
f3MirrorSessionMonitorPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorSessionMonitorPort.setStatus("current")
_F3MirrorSessionSourcePortDir_Type = TrafficDirection
_F3MirrorSessionSourcePortDir_Object = MibTableColumn
f3MirrorSessionSourcePortDir = _F3MirrorSessionSourcePortDir_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 4),
    _F3MirrorSessionSourcePortDir_Type()
)
f3MirrorSessionSourcePortDir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorSessionSourcePortDir.setStatus("current")
_F3MirrorSessionTruncationCtrl_Type = TruthValue
_F3MirrorSessionTruncationCtrl_Object = MibTableColumn
f3MirrorSessionTruncationCtrl = _F3MirrorSessionTruncationCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 5),
    _F3MirrorSessionTruncationCtrl_Type()
)
f3MirrorSessionTruncationCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3MirrorSessionTruncationCtrl.setStatus("current")


class _F3MirrorSessionTruncationLength_Type(Unsigned32):
    """Custom type f3MirrorSessionTruncationLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1500),
    )


_F3MirrorSessionTruncationLength_Type.__name__ = "Unsigned32"
_F3MirrorSessionTruncationLength_Object = MibTableColumn
f3MirrorSessionTruncationLength = _F3MirrorSessionTruncationLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 6),
    _F3MirrorSessionTruncationLength_Type()
)
f3MirrorSessionTruncationLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3MirrorSessionTruncationLength.setStatus("current")
_F3MirrorSessionTimestampControl_Type = TruthValue
_F3MirrorSessionTimestampControl_Object = MibTableColumn
f3MirrorSessionTimestampControl = _F3MirrorSessionTimestampControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 7),
    _F3MirrorSessionTimestampControl_Type()
)
f3MirrorSessionTimestampControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3MirrorSessionTimestampControl.setStatus("current")
_F3MirrorSessionStorageType_Type = StorageType
_F3MirrorSessionStorageType_Object = MibTableColumn
f3MirrorSessionStorageType = _F3MirrorSessionStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 8),
    _F3MirrorSessionStorageType_Type()
)
f3MirrorSessionStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorSessionStorageType.setStatus("current")
_F3MirrorSessionRowStatus_Type = RowStatus
_F3MirrorSessionRowStatus_Object = MibTableColumn
f3MirrorSessionRowStatus = _F3MirrorSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 9),
    _F3MirrorSessionRowStatus_Type()
)
f3MirrorSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorSessionRowStatus.setStatus("current")
_F3MirrorSessionMirrRsrcPort_Type = VariablePointer
_F3MirrorSessionMirrRsrcPort_Object = MibTableColumn
f3MirrorSessionMirrRsrcPort = _F3MirrorSessionMirrRsrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 10),
    _F3MirrorSessionMirrRsrcPort_Type()
)
f3MirrorSessionMirrRsrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorSessionMirrRsrcPort.setStatus("current")
_F3MirrorSessionFilterProfile_Type = VariablePointer
_F3MirrorSessionFilterProfile_Object = MibTableColumn
f3MirrorSessionFilterProfile = _F3MirrorSessionFilterProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 1, 1, 11),
    _F3MirrorSessionFilterProfile_Type()
)
f3MirrorSessionFilterProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorSessionFilterProfile.setStatus("current")
_F3PortMirrorAccPortExtTable_Object = MibTable
f3PortMirrorAccPortExtTable = _F3PortMirrorAccPortExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 2)
)
if mibBuilder.loadTexts:
    f3PortMirrorAccPortExtTable.setStatus("current")
_F3PortMirrorAccPortExtEntry_Object = MibTableRow
f3PortMirrorAccPortExtEntry = _F3PortMirrorAccPortExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 2, 1)
)
if mibBuilder.loadTexts:
    f3PortMirrorAccPortExtEntry.setStatus("current")
_F3PortMirrorAccPortExtMonitorEnabled_Type = TruthValue
_F3PortMirrorAccPortExtMonitorEnabled_Object = MibTableColumn
f3PortMirrorAccPortExtMonitorEnabled = _F3PortMirrorAccPortExtMonitorEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 2, 1, 1),
    _F3PortMirrorAccPortExtMonitorEnabled_Type()
)
f3PortMirrorAccPortExtMonitorEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PortMirrorAccPortExtMonitorEnabled.setStatus("current")


class _F3PortMirrorAccPortExtBufferSize_Type(Integer32):
    """Custom type f3PortMirrorAccPortExtBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 15360),
    )


_F3PortMirrorAccPortExtBufferSize_Type.__name__ = "Integer32"
_F3PortMirrorAccPortExtBufferSize_Object = MibTableColumn
f3PortMirrorAccPortExtBufferSize = _F3PortMirrorAccPortExtBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 2, 1, 2),
    _F3PortMirrorAccPortExtBufferSize_Type()
)
f3PortMirrorAccPortExtBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PortMirrorAccPortExtBufferSize.setStatus("current")
_F3PortMirrorAccPortExtMirrRsrcEnabled_Type = TruthValue
_F3PortMirrorAccPortExtMirrRsrcEnabled_Object = MibTableColumn
f3PortMirrorAccPortExtMirrRsrcEnabled = _F3PortMirrorAccPortExtMirrRsrcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 1, 2, 1, 3),
    _F3PortMirrorAccPortExtMirrRsrcEnabled_Type()
)
f3PortMirrorAccPortExtMirrRsrcEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PortMirrorAccPortExtMirrRsrcEnabled.setStatus("current")
_F3PortMirrorStatsObjects_ObjectIdentity = ObjectIdentity
f3PortMirrorStatsObjects = _F3PortMirrorStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 2)
)
_F3MonitorPortStatsTable_Object = MibTable
f3MonitorPortStatsTable = _F3MonitorPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 2, 1)
)
if mibBuilder.loadTexts:
    f3MonitorPortStatsTable.setStatus("current")
_F3MonitorPortStatsEntry_Object = MibTableRow
f3MonitorPortStatsEntry = _F3MonitorPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 2, 1, 1)
)
f3MonitorPortStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-PORTMIRROR-MIB", "f3MonitorPortStatsIndex"),
)
if mibBuilder.loadTexts:
    f3MonitorPortStatsEntry.setStatus("current")


class _F3MonitorPortStatsIndex_Type(Integer32):
    """Custom type f3MonitorPortStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_F3MonitorPortStatsIndex_Type.__name__ = "Integer32"
_F3MonitorPortStatsIndex_Object = MibTableColumn
f3MonitorPortStatsIndex = _F3MonitorPortStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 2, 1, 1, 1),
    _F3MonitorPortStatsIndex_Type()
)
f3MonitorPortStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3MonitorPortStatsIndex.setStatus("current")
_F3MonitorPortStatsTailDropped_Type = PerfCounter64
_F3MonitorPortStatsTailDropped_Object = MibTableColumn
f3MonitorPortStatsTailDropped = _F3MonitorPortStatsTailDropped_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 2, 1, 1, 2),
    _F3MonitorPortStatsTailDropped_Type()
)
f3MonitorPortStatsTailDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MonitorPortStatsTailDropped.setStatus("current")
_F3MirrorSessionStatsTable_Object = MibTable
f3MirrorSessionStatsTable = _F3MirrorSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 2, 2)
)
if mibBuilder.loadTexts:
    f3MirrorSessionStatsTable.setStatus("current")
_F3MirrorSessionStatsEntry_Object = MibTableRow
f3MirrorSessionStatsEntry = _F3MirrorSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 2, 2, 1)
)
f3MirrorSessionStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PORTMIRROR-MIB", "f3MirrorSessionStatsIndex"),
)
if mibBuilder.loadTexts:
    f3MirrorSessionStatsEntry.setStatus("current")


class _F3MirrorSessionStatsIndex_Type(Integer32):
    """Custom type f3MirrorSessionStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_F3MirrorSessionStatsIndex_Type.__name__ = "Integer32"
_F3MirrorSessionStatsIndex_Object = MibTableColumn
f3MirrorSessionStatsIndex = _F3MirrorSessionStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 2, 2, 1, 1),
    _F3MirrorSessionStatsIndex_Type()
)
f3MirrorSessionStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3MirrorSessionStatsIndex.setStatus("current")
_F3MirrorSessionStatsMirrFilterFrameDiscard_Type = PerfCounter64
_F3MirrorSessionStatsMirrFilterFrameDiscard_Object = MibTableColumn
f3MirrorSessionStatsMirrFilterFrameDiscard = _F3MirrorSessionStatsMirrFilterFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 2, 2, 1, 2),
    _F3MirrorSessionStatsMirrFilterFrameDiscard_Type()
)
f3MirrorSessionStatsMirrFilterFrameDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3MirrorSessionStatsMirrFilterFrameDiscard.setStatus("current")
_F3MirrorSessionStatsAction_Type = PortMirrorStatsAction
_F3MirrorSessionStatsAction_Object = MibTableColumn
f3MirrorSessionStatsAction = _F3MirrorSessionStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 2, 2, 1, 3),
    _F3MirrorSessionStatsAction_Type()
)
f3MirrorSessionStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3MirrorSessionStatsAction.setStatus("current")
_F3PortMirrorConformance_ObjectIdentity = ObjectIdentity
f3PortMirrorConformance = _F3PortMirrorConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 3)
)
_F3PortMirrorCompliances_ObjectIdentity = ObjectIdentity
f3PortMirrorCompliances = _F3PortMirrorCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 3, 1)
)
_F3PortMirrorGroups_ObjectIdentity = ObjectIdentity
f3PortMirrorGroups = _F3PortMirrorGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 3, 2)
)
_F3PortMirrorFilterObjects_ObjectIdentity = ObjectIdentity
f3PortMirrorFilterObjects = _F3PortMirrorFilterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4)
)
_F3MirrorFilterProfileTable_Object = MibTable
f3MirrorFilterProfileTable = _F3MirrorFilterProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 1)
)
if mibBuilder.loadTexts:
    f3MirrorFilterProfileTable.setStatus("current")
_F3MirrorFilterProfileEntry_Object = MibTableRow
f3MirrorFilterProfileEntry = _F3MirrorFilterProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 1, 1)
)
f3MirrorFilterProfileEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PORTMIRROR-MIB", "f3MirrorFilterProfileIndex"),
)
if mibBuilder.loadTexts:
    f3MirrorFilterProfileEntry.setStatus("current")


class _F3MirrorFilterProfileIndex_Type(Integer32):
    """Custom type f3MirrorFilterProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_F3MirrorFilterProfileIndex_Type.__name__ = "Integer32"
_F3MirrorFilterProfileIndex_Object = MibTableColumn
f3MirrorFilterProfileIndex = _F3MirrorFilterProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 1, 1, 1),
    _F3MirrorFilterProfileIndex_Type()
)
f3MirrorFilterProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3MirrorFilterProfileIndex.setStatus("current")


class _F3MirrorFilterProfileName_Type(DisplayString):
    """Custom type f3MirrorFilterProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3MirrorFilterProfileName_Type.__name__ = "DisplayString"
_F3MirrorFilterProfileName_Object = MibTableColumn
f3MirrorFilterProfileName = _F3MirrorFilterProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 1, 1, 2),
    _F3MirrorFilterProfileName_Type()
)
f3MirrorFilterProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterProfileName.setStatus("current")
_F3MirrorFilterProfileDefaultAction_Type = MirroredFramesAction
_F3MirrorFilterProfileDefaultAction_Object = MibTableColumn
f3MirrorFilterProfileDefaultAction = _F3MirrorFilterProfileDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 1, 1, 3),
    _F3MirrorFilterProfileDefaultAction_Type()
)
f3MirrorFilterProfileDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterProfileDefaultAction.setStatus("current")
_F3MirrorFilterProfileStorageType_Type = StorageType
_F3MirrorFilterProfileStorageType_Object = MibTableColumn
f3MirrorFilterProfileStorageType = _F3MirrorFilterProfileStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 1, 1, 4),
    _F3MirrorFilterProfileStorageType_Type()
)
f3MirrorFilterProfileStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterProfileStorageType.setStatus("current")
_F3MirrorFilterProfileRowStatus_Type = RowStatus
_F3MirrorFilterProfileRowStatus_Object = MibTableColumn
f3MirrorFilterProfileRowStatus = _F3MirrorFilterProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 1, 1, 5),
    _F3MirrorFilterProfileRowStatus_Type()
)
f3MirrorFilterProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterProfileRowStatus.setStatus("current")
_F3MirrorFilterProfileEntryTable_Object = MibTable
f3MirrorFilterProfileEntryTable = _F3MirrorFilterProfileEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 2)
)
if mibBuilder.loadTexts:
    f3MirrorFilterProfileEntryTable.setStatus("current")
_F3MirrorFilterProfileEntryEntry_Object = MibTableRow
f3MirrorFilterProfileEntryEntry = _F3MirrorFilterProfileEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 2, 1)
)
f3MirrorFilterProfileEntryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PORTMIRROR-MIB", "f3MirrorFilterProfileIndex"),
    (0, "F3-PORTMIRROR-MIB", "f3MirrorFilterProfileEntryIndex"),
)
if mibBuilder.loadTexts:
    f3MirrorFilterProfileEntryEntry.setStatus("current")


class _F3MirrorFilterProfileEntryIndex_Type(Integer32):
    """Custom type f3MirrorFilterProfileEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_F3MirrorFilterProfileEntryIndex_Type.__name__ = "Integer32"
_F3MirrorFilterProfileEntryIndex_Object = MibTableColumn
f3MirrorFilterProfileEntryIndex = _F3MirrorFilterProfileEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 2, 1, 1),
    _F3MirrorFilterProfileEntryIndex_Type()
)
f3MirrorFilterProfileEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3MirrorFilterProfileEntryIndex.setStatus("current")
_F3MirrorFilterProfileEntryFilter_Type = VariablePointer
_F3MirrorFilterProfileEntryFilter_Object = MibTableColumn
f3MirrorFilterProfileEntryFilter = _F3MirrorFilterProfileEntryFilter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 2, 1, 2),
    _F3MirrorFilterProfileEntryFilter_Type()
)
f3MirrorFilterProfileEntryFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterProfileEntryFilter.setStatus("current")
_F3MirrorFilterProfileEntryPriority_Type = Unsigned32
_F3MirrorFilterProfileEntryPriority_Object = MibTableColumn
f3MirrorFilterProfileEntryPriority = _F3MirrorFilterProfileEntryPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 2, 1, 3),
    _F3MirrorFilterProfileEntryPriority_Type()
)
f3MirrorFilterProfileEntryPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterProfileEntryPriority.setStatus("current")
_F3MirrorFilterProfileEntryAction_Type = MirroredFramesAction
_F3MirrorFilterProfileEntryAction_Object = MibTableColumn
f3MirrorFilterProfileEntryAction = _F3MirrorFilterProfileEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 2, 1, 4),
    _F3MirrorFilterProfileEntryAction_Type()
)
f3MirrorFilterProfileEntryAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterProfileEntryAction.setStatus("current")
_F3MirrorFilterProfileEntryStorageType_Type = StorageType
_F3MirrorFilterProfileEntryStorageType_Object = MibTableColumn
f3MirrorFilterProfileEntryStorageType = _F3MirrorFilterProfileEntryStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 2, 1, 5),
    _F3MirrorFilterProfileEntryStorageType_Type()
)
f3MirrorFilterProfileEntryStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterProfileEntryStorageType.setStatus("current")
_F3MirrorFilterProfileEntryRowStatus_Type = RowStatus
_F3MirrorFilterProfileEntryRowStatus_Object = MibTableColumn
f3MirrorFilterProfileEntryRowStatus = _F3MirrorFilterProfileEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 2, 1, 6),
    _F3MirrorFilterProfileEntryRowStatus_Type()
)
f3MirrorFilterProfileEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterProfileEntryRowStatus.setStatus("current")
_F3MirrorFilterTable_Object = MibTable
f3MirrorFilterTable = _F3MirrorFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3)
)
if mibBuilder.loadTexts:
    f3MirrorFilterTable.setStatus("current")
_F3MirrorFilterEntry_Object = MibTableRow
f3MirrorFilterEntry = _F3MirrorFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1)
)
f3MirrorFilterEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-PORTMIRROR-MIB", "f3MirrorFilterIndex"),
)
if mibBuilder.loadTexts:
    f3MirrorFilterEntry.setStatus("current")


class _F3MirrorFilterIndex_Type(Integer32):
    """Custom type f3MirrorFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_F3MirrorFilterIndex_Type.__name__ = "Integer32"
_F3MirrorFilterIndex_Object = MibTableColumn
f3MirrorFilterIndex = _F3MirrorFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 1),
    _F3MirrorFilterIndex_Type()
)
f3MirrorFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3MirrorFilterIndex.setStatus("current")


class _F3MirrorFilterName_Type(DisplayString):
    """Custom type f3MirrorFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3MirrorFilterName_Type.__name__ = "DisplayString"
_F3MirrorFilterName_Object = MibTableColumn
f3MirrorFilterName = _F3MirrorFilterName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 2),
    _F3MirrorFilterName_Type()
)
f3MirrorFilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterName.setStatus("current")
_F3MirrorFilterL2OuterVIDCtrlEnabled_Type = TruthValue
_F3MirrorFilterL2OuterVIDCtrlEnabled_Object = MibTableColumn
f3MirrorFilterL2OuterVIDCtrlEnabled = _F3MirrorFilterL2OuterVIDCtrlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 3),
    _F3MirrorFilterL2OuterVIDCtrlEnabled_Type()
)
f3MirrorFilterL2OuterVIDCtrlEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterL2OuterVIDCtrlEnabled.setStatus("current")
_F3MirrorFilterL2OuterVIDLow_Type = VlanId
_F3MirrorFilterL2OuterVIDLow_Object = MibTableColumn
f3MirrorFilterL2OuterVIDLow = _F3MirrorFilterL2OuterVIDLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 4),
    _F3MirrorFilterL2OuterVIDLow_Type()
)
f3MirrorFilterL2OuterVIDLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterL2OuterVIDLow.setStatus("current")
_F3MirrorFilterL2OuterVIDHigh_Type = VlanId
_F3MirrorFilterL2OuterVIDHigh_Object = MibTableColumn
f3MirrorFilterL2OuterVIDHigh = _F3MirrorFilterL2OuterVIDHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 5),
    _F3MirrorFilterL2OuterVIDHigh_Type()
)
f3MirrorFilterL2OuterVIDHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterL2OuterVIDHigh.setStatus("current")
_F3MirrorFilterL2OuterPrioCtrlEnabled_Type = TruthValue
_F3MirrorFilterL2OuterPrioCtrlEnabled_Object = MibTableColumn
f3MirrorFilterL2OuterPrioCtrlEnabled = _F3MirrorFilterL2OuterPrioCtrlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 6),
    _F3MirrorFilterL2OuterPrioCtrlEnabled_Type()
)
f3MirrorFilterL2OuterPrioCtrlEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterL2OuterPrioCtrlEnabled.setStatus("current")
_F3MirrorFilterL2OuterPrioLow_Type = Integer32
_F3MirrorFilterL2OuterPrioLow_Object = MibTableColumn
f3MirrorFilterL2OuterPrioLow = _F3MirrorFilterL2OuterPrioLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 7),
    _F3MirrorFilterL2OuterPrioLow_Type()
)
f3MirrorFilterL2OuterPrioLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterL2OuterPrioLow.setStatus("current")
_F3MirrorFilterL2OuterPrioHigh_Type = Integer32
_F3MirrorFilterL2OuterPrioHigh_Object = MibTableColumn
f3MirrorFilterL2OuterPrioHigh = _F3MirrorFilterL2OuterPrioHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 8),
    _F3MirrorFilterL2OuterPrioHigh_Type()
)
f3MirrorFilterL2OuterPrioHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterL2OuterPrioHigh.setStatus("current")
_F3MirrorFilterL3IPv4DstAddrCtrlEnabled_Type = TruthValue
_F3MirrorFilterL3IPv4DstAddrCtrlEnabled_Object = MibTableColumn
f3MirrorFilterL3IPv4DstAddrCtrlEnabled = _F3MirrorFilterL3IPv4DstAddrCtrlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 9),
    _F3MirrorFilterL3IPv4DstAddrCtrlEnabled_Type()
)
f3MirrorFilterL3IPv4DstAddrCtrlEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterL3IPv4DstAddrCtrlEnabled.setStatus("current")
_F3MirrorFilterL3IPv4DstAddr_Type = IpAddress
_F3MirrorFilterL3IPv4DstAddr_Object = MibTableColumn
f3MirrorFilterL3IPv4DstAddr = _F3MirrorFilterL3IPv4DstAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 10),
    _F3MirrorFilterL3IPv4DstAddr_Type()
)
f3MirrorFilterL3IPv4DstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterL3IPv4DstAddr.setStatus("current")
_F3MirrorFilterL3IPv4DstAddrMask_Type = IpAddress
_F3MirrorFilterL3IPv4DstAddrMask_Object = MibTableColumn
f3MirrorFilterL3IPv4DstAddrMask = _F3MirrorFilterL3IPv4DstAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 11),
    _F3MirrorFilterL3IPv4DstAddrMask_Type()
)
f3MirrorFilterL3IPv4DstAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterL3IPv4DstAddrMask.setStatus("current")
_F3MirrorFilterL3IPv4SrcAddrCtrlEnabled_Type = TruthValue
_F3MirrorFilterL3IPv4SrcAddrCtrlEnabled_Object = MibTableColumn
f3MirrorFilterL3IPv4SrcAddrCtrlEnabled = _F3MirrorFilterL3IPv4SrcAddrCtrlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 12),
    _F3MirrorFilterL3IPv4SrcAddrCtrlEnabled_Type()
)
f3MirrorFilterL3IPv4SrcAddrCtrlEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterL3IPv4SrcAddrCtrlEnabled.setStatus("current")
_F3MirrorFilterL3IPv4SrcAddr_Type = IpAddress
_F3MirrorFilterL3IPv4SrcAddr_Object = MibTableColumn
f3MirrorFilterL3IPv4SrcAddr = _F3MirrorFilterL3IPv4SrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 13),
    _F3MirrorFilterL3IPv4SrcAddr_Type()
)
f3MirrorFilterL3IPv4SrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterL3IPv4SrcAddr.setStatus("current")
_F3MirrorFilterL3IPv4SrcAddrMask_Type = IpAddress
_F3MirrorFilterL3IPv4SrcAddrMask_Object = MibTableColumn
f3MirrorFilterL3IPv4SrcAddrMask = _F3MirrorFilterL3IPv4SrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 14),
    _F3MirrorFilterL3IPv4SrcAddrMask_Type()
)
f3MirrorFilterL3IPv4SrcAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterL3IPv4SrcAddrMask.setStatus("current")
_F3MirrorFilterStorageType_Type = StorageType
_F3MirrorFilterStorageType_Object = MibTableColumn
f3MirrorFilterStorageType = _F3MirrorFilterStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 15),
    _F3MirrorFilterStorageType_Type()
)
f3MirrorFilterStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterStorageType.setStatus("current")
_F3MirrorFilterRowStatus_Type = RowStatus
_F3MirrorFilterRowStatus_Object = MibTableColumn
f3MirrorFilterRowStatus = _F3MirrorFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 4, 3, 1, 16),
    _F3MirrorFilterRowStatus_Type()
)
f3MirrorFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3MirrorFilterRowStatus.setStatus("current")
cmEthernetAccPortEntry.registerAugmentions(
    ("F3-PORTMIRROR-MIB",
     "f3PortMirrorAccPortExtEntry")
)
f3PortMirrorAccPortExtEntry.setIndexNames(*cmEthernetAccPortEntry.getIndexNames())

# Managed Objects groups

f3MirrorSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 3, 2, 1)
)
f3MirrorSessionGroup.setObjects(
      *(("F3-PORTMIRROR-MIB", "f3MirrorSessionIndex"),
        ("F3-PORTMIRROR-MIB", "f3MirrorSessionSourcePort"),
        ("F3-PORTMIRROR-MIB", "f3MirrorSessionMonitorPort"),
        ("F3-PORTMIRROR-MIB", "f3MirrorSessionSourcePortDir"),
        ("F3-PORTMIRROR-MIB", "f3MirrorSessionTruncationCtrl"),
        ("F3-PORTMIRROR-MIB", "f3MirrorSessionTruncationLength"),
        ("F3-PORTMIRROR-MIB", "f3MirrorSessionTimestampControl"),
        ("F3-PORTMIRROR-MIB", "f3MirrorSessionStorageType"),
        ("F3-PORTMIRROR-MIB", "f3MirrorSessionRowStatus"),
        ("F3-PORTMIRROR-MIB", "f3MirrorSessionMirrRsrcPort"),
        ("F3-PORTMIRROR-MIB", "f3MirrorSessionFilterProfile"))
)
if mibBuilder.loadTexts:
    f3MirrorSessionGroup.setStatus("current")

f3PortMirrorAccPortExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 3, 2, 2)
)
f3PortMirrorAccPortExtGroup.setObjects(
      *(("F3-PORTMIRROR-MIB", "f3PortMirrorAccPortExtMonitorEnabled"),
        ("F3-PORTMIRROR-MIB", "f3PortMirrorAccPortExtBufferSize"),
        ("F3-PORTMIRROR-MIB", "f3PortMirrorAccPortExtMirrRsrcEnabled"))
)
if mibBuilder.loadTexts:
    f3PortMirrorAccPortExtGroup.setStatus("current")

f3MonitorPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 3, 2, 3)
)
f3MonitorPortStatsGroup.setObjects(
      *(("F3-PORTMIRROR-MIB", "f3MonitorPortStatsIndex"),
        ("F3-PORTMIRROR-MIB", "f3MonitorPortStatsTailDropped"))
)
if mibBuilder.loadTexts:
    f3MonitorPortStatsGroup.setStatus("current")

f3MirrorSessionStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 3, 2, 4)
)
f3MirrorSessionStatsGroup.setObjects(
      *(("F3-PORTMIRROR-MIB", "f3MirrorSessionStatsIndex"),
        ("F3-PORTMIRROR-MIB", "f3MirrorSessionStatsMirrFilterFrameDiscard"),
        ("F3-PORTMIRROR-MIB", "f3MirrorSessionStatsAction"))
)
if mibBuilder.loadTexts:
    f3MirrorSessionStatsGroup.setStatus("current")

f3PortMirrorFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 3, 2, 5)
)
f3PortMirrorFilterGroup.setObjects(
      *(("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileIndex"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileName"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileDefaultAction"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileStorageType"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileRowStatus"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileEntryIndex"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileEntryFilter"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileEntryPriority"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileEntryAction"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileEntryStorageType"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterProfileEntryRowStatus"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterIndex"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterName"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterL2OuterVIDCtrlEnabled"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterL2OuterVIDLow"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterL2OuterVIDHigh"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterL2OuterPrioCtrlEnabled"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterL2OuterPrioLow"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterL2OuterPrioHigh"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterL3IPv4DstAddrCtrlEnabled"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterL3IPv4DstAddr"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterL3IPv4DstAddrMask"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterL3IPv4SrcAddrCtrlEnabled"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterL3IPv4SrcAddr"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterL3IPv4SrcAddrMask"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterStorageType"),
        ("F3-PORTMIRROR-MIB", "f3MirrorFilterRowStatus"))
)
if mibBuilder.loadTexts:
    f3PortMirrorFilterGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f3PortMirrorCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 29, 3, 1, 1)
)
f3PortMirrorCompliance.setObjects(
      *(("F3-PORTMIRROR-MIB", "f3MirrorSessionGroup"),
        ("F3-PORTMIRROR-MIB", "f3PortMirrorAccPortExtGroup"),
        ("F3-PORTMIRROR-MIB", "f3MonitorPortStatsGroup"),
        ("F3-PORTMIRROR-MIB", "f3PortMirrorFilterGroup"),
        ("F3-PORTMIRROR-MIB", "f3MirrorSessionStatsGroup"))
)
if mibBuilder.loadTexts:
    f3PortMirrorCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-PORTMIRROR-MIB",
    **{"MirroredFramesAction": MirroredFramesAction,
       "PortMirrorStatsAction": PortMirrorStatsAction,
       "f3PortMirrorMIB": f3PortMirrorMIB,
       "f3PortMirrorConfigObjects": f3PortMirrorConfigObjects,
       "f3MirrorSessionTable": f3MirrorSessionTable,
       "f3MirrorSessionEntry": f3MirrorSessionEntry,
       "f3MirrorSessionIndex": f3MirrorSessionIndex,
       "f3MirrorSessionSourcePort": f3MirrorSessionSourcePort,
       "f3MirrorSessionMonitorPort": f3MirrorSessionMonitorPort,
       "f3MirrorSessionSourcePortDir": f3MirrorSessionSourcePortDir,
       "f3MirrorSessionTruncationCtrl": f3MirrorSessionTruncationCtrl,
       "f3MirrorSessionTruncationLength": f3MirrorSessionTruncationLength,
       "f3MirrorSessionTimestampControl": f3MirrorSessionTimestampControl,
       "f3MirrorSessionStorageType": f3MirrorSessionStorageType,
       "f3MirrorSessionRowStatus": f3MirrorSessionRowStatus,
       "f3MirrorSessionMirrRsrcPort": f3MirrorSessionMirrRsrcPort,
       "f3MirrorSessionFilterProfile": f3MirrorSessionFilterProfile,
       "f3PortMirrorAccPortExtTable": f3PortMirrorAccPortExtTable,
       "f3PortMirrorAccPortExtEntry": f3PortMirrorAccPortExtEntry,
       "f3PortMirrorAccPortExtMonitorEnabled": f3PortMirrorAccPortExtMonitorEnabled,
       "f3PortMirrorAccPortExtBufferSize": f3PortMirrorAccPortExtBufferSize,
       "f3PortMirrorAccPortExtMirrRsrcEnabled": f3PortMirrorAccPortExtMirrRsrcEnabled,
       "f3PortMirrorStatsObjects": f3PortMirrorStatsObjects,
       "f3MonitorPortStatsTable": f3MonitorPortStatsTable,
       "f3MonitorPortStatsEntry": f3MonitorPortStatsEntry,
       "f3MonitorPortStatsIndex": f3MonitorPortStatsIndex,
       "f3MonitorPortStatsTailDropped": f3MonitorPortStatsTailDropped,
       "f3MirrorSessionStatsTable": f3MirrorSessionStatsTable,
       "f3MirrorSessionStatsEntry": f3MirrorSessionStatsEntry,
       "f3MirrorSessionStatsIndex": f3MirrorSessionStatsIndex,
       "f3MirrorSessionStatsMirrFilterFrameDiscard": f3MirrorSessionStatsMirrFilterFrameDiscard,
       "f3MirrorSessionStatsAction": f3MirrorSessionStatsAction,
       "f3PortMirrorConformance": f3PortMirrorConformance,
       "f3PortMirrorCompliances": f3PortMirrorCompliances,
       "f3PortMirrorCompliance": f3PortMirrorCompliance,
       "f3PortMirrorGroups": f3PortMirrorGroups,
       "f3MirrorSessionGroup": f3MirrorSessionGroup,
       "f3PortMirrorAccPortExtGroup": f3PortMirrorAccPortExtGroup,
       "f3MonitorPortStatsGroup": f3MonitorPortStatsGroup,
       "f3MirrorSessionStatsGroup": f3MirrorSessionStatsGroup,
       "f3PortMirrorFilterGroup": f3PortMirrorFilterGroup,
       "f3PortMirrorFilterObjects": f3PortMirrorFilterObjects,
       "f3MirrorFilterProfileTable": f3MirrorFilterProfileTable,
       "f3MirrorFilterProfileEntry": f3MirrorFilterProfileEntry,
       "f3MirrorFilterProfileIndex": f3MirrorFilterProfileIndex,
       "f3MirrorFilterProfileName": f3MirrorFilterProfileName,
       "f3MirrorFilterProfileDefaultAction": f3MirrorFilterProfileDefaultAction,
       "f3MirrorFilterProfileStorageType": f3MirrorFilterProfileStorageType,
       "f3MirrorFilterProfileRowStatus": f3MirrorFilterProfileRowStatus,
       "f3MirrorFilterProfileEntryTable": f3MirrorFilterProfileEntryTable,
       "f3MirrorFilterProfileEntryEntry": f3MirrorFilterProfileEntryEntry,
       "f3MirrorFilterProfileEntryIndex": f3MirrorFilterProfileEntryIndex,
       "f3MirrorFilterProfileEntryFilter": f3MirrorFilterProfileEntryFilter,
       "f3MirrorFilterProfileEntryPriority": f3MirrorFilterProfileEntryPriority,
       "f3MirrorFilterProfileEntryAction": f3MirrorFilterProfileEntryAction,
       "f3MirrorFilterProfileEntryStorageType": f3MirrorFilterProfileEntryStorageType,
       "f3MirrorFilterProfileEntryRowStatus": f3MirrorFilterProfileEntryRowStatus,
       "f3MirrorFilterTable": f3MirrorFilterTable,
       "f3MirrorFilterEntry": f3MirrorFilterEntry,
       "f3MirrorFilterIndex": f3MirrorFilterIndex,
       "f3MirrorFilterName": f3MirrorFilterName,
       "f3MirrorFilterL2OuterVIDCtrlEnabled": f3MirrorFilterL2OuterVIDCtrlEnabled,
       "f3MirrorFilterL2OuterVIDLow": f3MirrorFilterL2OuterVIDLow,
       "f3MirrorFilterL2OuterVIDHigh": f3MirrorFilterL2OuterVIDHigh,
       "f3MirrorFilterL2OuterPrioCtrlEnabled": f3MirrorFilterL2OuterPrioCtrlEnabled,
       "f3MirrorFilterL2OuterPrioLow": f3MirrorFilterL2OuterPrioLow,
       "f3MirrorFilterL2OuterPrioHigh": f3MirrorFilterL2OuterPrioHigh,
       "f3MirrorFilterL3IPv4DstAddrCtrlEnabled": f3MirrorFilterL3IPv4DstAddrCtrlEnabled,
       "f3MirrorFilterL3IPv4DstAddr": f3MirrorFilterL3IPv4DstAddr,
       "f3MirrorFilterL3IPv4DstAddrMask": f3MirrorFilterL3IPv4DstAddrMask,
       "f3MirrorFilterL3IPv4SrcAddrCtrlEnabled": f3MirrorFilterL3IPv4SrcAddrCtrlEnabled,
       "f3MirrorFilterL3IPv4SrcAddr": f3MirrorFilterL3IPv4SrcAddr,
       "f3MirrorFilterL3IPv4SrcAddrMask": f3MirrorFilterL3IPv4SrcAddrMask,
       "f3MirrorFilterStorageType": f3MirrorFilterStorageType,
       "f3MirrorFilterRowStatus": f3MirrorFilterRowStatus}
)
