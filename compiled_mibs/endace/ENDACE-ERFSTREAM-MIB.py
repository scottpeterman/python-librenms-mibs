# SNMP MIB module (ENDACE-ERFSTREAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\endace\ENDACE-ERFSTREAM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:55 2025
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

(endace,) = mibBuilder.importSymbols(
    "ENDACE-MIB",
    "endace")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

endaceErfstreamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 12)
)
if mibBuilder.loadTexts:
    endaceErfstreamMIB.setRevisions(
        ("2021-06-13 19:41",
         "2017-07-04 02:45",
         "2017-02-14 17:51",
         "2016-12-06 23:50",
         "2014-03-09 23:04",
         "2014-01-30 01:05",
         "2012-09-24 05:56",
         "2012-05-04 00:24")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PipeIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class RotationFileIndex(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class VisionDBIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class VisionDBVersionIndex(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_ErfstreamVariables_ObjectIdentity = ObjectIdentity
erfstreamVariables = _ErfstreamVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1)
)
_PipeInfoTable_Object = MibTable
pipeInfoTable = _PipeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 1)
)
if mibBuilder.loadTexts:
    pipeInfoTable.setStatus("current")
_PipeInfoTableEntry_Object = MibTableRow
pipeInfoTableEntry = _PipeInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 1, 1)
)
pipeInfoTableEntry.setIndexNames(
    (0, "ENDACE-ERFSTREAM-MIB", "pipeInfoIndex"),
)
if mibBuilder.loadTexts:
    pipeInfoTableEntry.setStatus("current")
_PipeInfoIndex_Type = PipeIndex
_PipeInfoIndex_Object = MibTableColumn
pipeInfoIndex = _PipeInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 1, 1, 1),
    _PipeInfoIndex_Type()
)
pipeInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pipeInfoIndex.setStatus("current")


class _PipeName_Type(DisplayString):
    """Custom type pipeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PipeName_Type.__name__ = "DisplayString"
_PipeName_Object = MibTableColumn
pipeName = _PipeName_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 1, 1, 2),
    _PipeName_Type()
)
pipeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeName.setStatus("current")
_PipeStatusTable_Object = MibTable
pipeStatusTable = _PipeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2)
)
if mibBuilder.loadTexts:
    pipeStatusTable.setStatus("current")
_PipeStatusTableEntry_Object = MibTableRow
pipeStatusTableEntry = _PipeStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1)
)
pipeStatusTableEntry.setIndexNames(
    (0, "ENDACE-ERFSTREAM-MIB", "pipeStatusIndex"),
)
if mibBuilder.loadTexts:
    pipeStatusTableEntry.setStatus("current")
_PipeStatusIndex_Type = PipeIndex
_PipeStatusIndex_Object = MibTableColumn
pipeStatusIndex = _PipeStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 1),
    _PipeStatusIndex_Type()
)
pipeStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pipeStatusIndex.setStatus("current")
_PipeInputPackets_Type = Counter64
_PipeInputPackets_Object = MibTableColumn
pipeInputPackets = _PipeInputPackets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 2),
    _PipeInputPackets_Type()
)
pipeInputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeInputPackets.setStatus("current")
_PipeInputBytes_Type = Counter64
_PipeInputBytes_Object = MibTableColumn
pipeInputBytes = _PipeInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 3),
    _PipeInputBytes_Type()
)
pipeInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeInputBytes.setStatus("current")
_PipeOutputPackets_Type = Counter64
_PipeOutputPackets_Object = MibTableColumn
pipeOutputPackets = _PipeOutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 4),
    _PipeOutputPackets_Type()
)
pipeOutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeOutputPackets.setStatus("current")
_PipeOutputBytes_Type = Counter64
_PipeOutputBytes_Object = MibTableColumn
pipeOutputBytes = _PipeOutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 5),
    _PipeOutputBytes_Type()
)
pipeOutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeOutputBytes.setStatus("current")
_PipeDroppedPackets_Type = Counter64
_PipeDroppedPackets_Object = MibTableColumn
pipeDroppedPackets = _PipeDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 6),
    _PipeDroppedPackets_Type()
)
pipeDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeDroppedPackets.setStatus("current")
_PipeDroppedBytes_Type = Counter64
_PipeDroppedBytes_Object = MibTableColumn
pipeDroppedBytes = _PipeDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 7),
    _PipeDroppedBytes_Type()
)
pipeDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeDroppedBytes.setStatus("current")
_PilotDroppedPackets_Type = Counter64
_PilotDroppedPackets_Object = MibTableColumn
pilotDroppedPackets = _PilotDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 8),
    _PilotDroppedPackets_Type()
)
pilotDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pilotDroppedPackets.setStatus("obsolete")
_PilotDroppedBytes_Type = Counter64
_PilotDroppedBytes_Object = MibTableColumn
pilotDroppedBytes = _PilotDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 9),
    _PilotDroppedBytes_Type()
)
pilotDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pilotDroppedBytes.setStatus("obsolete")
_VisionDroppedRecords_Type = Counter64
_VisionDroppedRecords_Object = MibTableColumn
visionDroppedRecords = _VisionDroppedRecords_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 10),
    _VisionDroppedRecords_Type()
)
visionDroppedRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visionDroppedRecords.setStatus("current")
_PipeCurrentFlows_Type = Gauge32
_PipeCurrentFlows_Object = MibTableColumn
pipeCurrentFlows = _PipeCurrentFlows_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 11),
    _PipeCurrentFlows_Type()
)
pipeCurrentFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeCurrentFlows.setStatus("current")
_PipeFlowRate_Type = Gauge32
_PipeFlowRate_Object = MibTableColumn
pipeFlowRate = _PipeFlowRate_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 12),
    _PipeFlowRate_Type()
)
pipeFlowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeFlowRate.setStatus("current")
if mibBuilder.loadTexts:
    pipeFlowRate.setUnits("flows/s")
_PipeCreatedFlows_Type = Counter64
_PipeCreatedFlows_Object = MibTableColumn
pipeCreatedFlows = _PipeCreatedFlows_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 13),
    _PipeCreatedFlows_Type()
)
pipeCreatedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeCreatedFlows.setStatus("current")
_PipeDeletedFlows_Type = Counter64
_PipeDeletedFlows_Object = MibTableColumn
pipeDeletedFlows = _PipeDeletedFlows_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 14),
    _PipeDeletedFlows_Type()
)
pipeDeletedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeDeletedFlows.setStatus("current")


class _PipeRunningStatus_Type(Integer32):
    """Custom type pipeRunningStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("stopped", 0),
          ("paused", 1),
          ("running", 2),
          ("complete", 3),
          ("stopping", 4),
          ("preparing", 5))
    )


_PipeRunningStatus_Type.__name__ = "Integer32"
_PipeRunningStatus_Object = MibTableColumn
pipeRunningStatus = _PipeRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 2, 1, 15),
    _PipeRunningStatus_Type()
)
pipeRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeRunningStatus.setStatus("current")
_VisionDBStatusTable_Object = MibTable
visionDBStatusTable = _VisionDBStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 3)
)
if mibBuilder.loadTexts:
    visionDBStatusTable.setStatus("current")
_VisionDBStatusTableEntry_Object = MibTableRow
visionDBStatusTableEntry = _VisionDBStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 3, 1)
)
visionDBStatusTableEntry.setIndexNames(
    (0, "ENDACE-ERFSTREAM-MIB", "visionDBStatusVersionIndex"),
    (0, "ENDACE-ERFSTREAM-MIB", "visionDBStatusIndex"),
)
if mibBuilder.loadTexts:
    visionDBStatusTableEntry.setStatus("current")
_VisionDBStatusVersionIndex_Type = VisionDBVersionIndex
_VisionDBStatusVersionIndex_Object = MibTableColumn
visionDBStatusVersionIndex = _VisionDBStatusVersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 3, 1, 1),
    _VisionDBStatusVersionIndex_Type()
)
visionDBStatusVersionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    visionDBStatusVersionIndex.setStatus("current")
_VisionDBStatusIndex_Type = VisionDBIndex
_VisionDBStatusIndex_Object = MibTableColumn
visionDBStatusIndex = _VisionDBStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 3, 1, 2),
    _VisionDBStatusIndex_Type()
)
visionDBStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    visionDBStatusIndex.setStatus("current")


class _VisionDBRotfileName_Type(DisplayString):
    """Custom type visionDBRotfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VisionDBRotfileName_Type.__name__ = "DisplayString"
_VisionDBRotfileName_Object = MibTableColumn
visionDBRotfileName = _VisionDBRotfileName_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 3, 1, 3),
    _VisionDBRotfileName_Type()
)
visionDBRotfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visionDBRotfileName.setStatus("current")
_VisionDBUsage_Type = Gauge32
_VisionDBUsage_Object = MibTableColumn
visionDBUsage = _VisionDBUsage_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 3, 1, 4),
    _VisionDBUsage_Type()
)
visionDBUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visionDBUsage.setStatus("current")
_RotationFileStatusTable_Object = MibTable
rotationFileStatusTable = _RotationFileStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 4)
)
if mibBuilder.loadTexts:
    rotationFileStatusTable.setStatus("current")
_RotationFileStatusTableEntry_Object = MibTableRow
rotationFileStatusTableEntry = _RotationFileStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 4, 1)
)
rotationFileStatusTableEntry.setIndexNames(
    (0, "ENDACE-ERFSTREAM-MIB", "rotationFileIndex"),
)
if mibBuilder.loadTexts:
    rotationFileStatusTableEntry.setStatus("current")
_RotationFileIndex_Type = RotationFileIndex
_RotationFileIndex_Object = MibTableColumn
rotationFileIndex = _RotationFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 4, 1, 1),
    _RotationFileIndex_Type()
)
rotationFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rotationFileIndex.setStatus("current")


class _RotationFileName_Type(DisplayString):
    """Custom type rotationFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RotationFileName_Type.__name__ = "DisplayString"
_RotationFileName_Object = MibTableColumn
rotationFileName = _RotationFileName_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 4, 1, 2),
    _RotationFileName_Type()
)
rotationFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rotationFileName.setStatus("current")
_RotationFileStoredSecs_Type = Counter32
_RotationFileStoredSecs_Object = MibTableColumn
rotationFileStoredSecs = _RotationFileStoredSecs_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 4, 1, 3),
    _RotationFileStoredSecs_Type()
)
rotationFileStoredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rotationFileStoredSecs.setStatus("current")


class _RotationFileCompression_Type(Integer32):
    """Custom type rotationFileCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RotationFileCompression_Type.__name__ = "Integer32"
_RotationFileCompression_Object = MibTableColumn
rotationFileCompression = _RotationFileCompression_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 4, 1, 4),
    _RotationFileCompression_Type()
)
rotationFileCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rotationFileCompression.setStatus("current")


class _RotationFileStartDate_Type(DisplayString):
    """Custom type rotationFileStartDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )
    fixed_length = 19


_RotationFileStartDate_Type.__name__ = "DisplayString"
_RotationFileStartDate_Object = MibTableColumn
rotationFileStartDate = _RotationFileStartDate_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 4, 1, 5),
    _RotationFileStartDate_Type()
)
rotationFileStartDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rotationFileStartDate.setStatus("current")


class _RotationFileEndDate_Type(DisplayString):
    """Custom type rotationFileEndDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )
    fixed_length = 19


_RotationFileEndDate_Type.__name__ = "DisplayString"
_RotationFileEndDate_Object = MibTableColumn
rotationFileEndDate = _RotationFileEndDate_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 4, 1, 6),
    _RotationFileEndDate_Type()
)
rotationFileEndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rotationFileEndDate.setStatus("current")
_NicInfoTable_Object = MibTable
nicInfoTable = _NicInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 5)
)
if mibBuilder.loadTexts:
    nicInfoTable.setStatus("current")
_NicInfoTableEntry_Object = MibTableRow
nicInfoTableEntry = _NicInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 5, 1)
)
nicInfoTableEntry.setIndexNames(
    (0, "ENDACE-ERFSTREAM-MIB", "nicInfoIndex"),
)
if mibBuilder.loadTexts:
    nicInfoTableEntry.setStatus("current")
_NicInfoIndex_Type = Unsigned32
_NicInfoIndex_Object = MibTableColumn
nicInfoIndex = _NicInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 5, 1, 1),
    _NicInfoIndex_Type()
)
nicInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nicInfoIndex.setStatus("current")
_NicInfoInterface_Type = DisplayString
_NicInfoInterface_Object = MibTableColumn
nicInfoInterface = _NicInfoInterface_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 5, 1, 2),
    _NicInfoInterface_Type()
)
nicInfoInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicInfoInterface.setStatus("current")
_NicInfoDroppedInPackets_Type = Counter64
_NicInfoDroppedInPackets_Object = MibTableColumn
nicInfoDroppedInPackets = _NicInfoDroppedInPackets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 5, 1, 3),
    _NicInfoDroppedInPackets_Type()
)
nicInfoDroppedInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicInfoDroppedInPackets.setStatus("current")
_NicInfoDroppedInBytes_Type = Counter64
_NicInfoDroppedInBytes_Object = MibTableColumn
nicInfoDroppedInBytes = _NicInfoDroppedInBytes_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 5, 1, 4),
    _NicInfoDroppedInBytes_Type()
)
nicInfoDroppedInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicInfoDroppedInBytes.setStatus("current")
_NicInfoInUse_Type = TruthValue
_NicInfoInUse_Object = MibTableColumn
nicInfoInUse = _NicInfoInUse_Object(
    (1, 3, 6, 1, 4, 1, 18418, 12, 1, 5, 1, 5),
    _NicInfoInUse_Type()
)
nicInfoInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicInfoInUse.setStatus("current")
_EventTraps_ObjectIdentity = ObjectIdentity
eventTraps = _EventTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2)
)
_ErfstreamNotificationPrefix_ObjectIdentity = ObjectIdentity
erfstreamNotificationPrefix = _ErfstreamNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0)
)
_ErfstreamConf_ObjectIdentity = ObjectIdentity
erfstreamConf = _ErfstreamConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 12, 3)
)
_ErfstreamGroups_ObjectIdentity = ObjectIdentity
erfstreamGroups = _ErfstreamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 12, 3, 1)
)

# Managed Objects groups

pipeAttributes = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 12, 3, 1, 1)
)
pipeAttributes.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "pipeName")
)
if mibBuilder.loadTexts:
    pipeAttributes.setStatus("current")

pipeStatus = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 12, 3, 1, 2)
)
pipeStatus.setObjects(
      *(("ENDACE-ERFSTREAM-MIB", "pipeCurrentFlows"),
        ("ENDACE-ERFSTREAM-MIB", "pipeDroppedBytes"),
        ("ENDACE-ERFSTREAM-MIB", "pipeDroppedPackets"),
        ("ENDACE-ERFSTREAM-MIB", "pipeInputBytes"),
        ("ENDACE-ERFSTREAM-MIB", "pipeInputPackets"),
        ("ENDACE-ERFSTREAM-MIB", "pipeOutputBytes"),
        ("ENDACE-ERFSTREAM-MIB", "pipeOutputPackets"),
        ("ENDACE-ERFSTREAM-MIB", "pipeFlowRate"),
        ("ENDACE-ERFSTREAM-MIB", "pipeCreatedFlows"),
        ("ENDACE-ERFSTREAM-MIB", "pipeDeletedFlows"),
        ("ENDACE-ERFSTREAM-MIB", "pipeRunningStatus"))
)
if mibBuilder.loadTexts:
    pipeStatus.setStatus("current")

visionAttributes = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 12, 3, 1, 5)
)
visionAttributes.setObjects(
      *(("ENDACE-ERFSTREAM-MIB", "visionDBRotfileName"),
        ("ENDACE-ERFSTREAM-MIB", "visionDBUsage"),
        ("ENDACE-ERFSTREAM-MIB", "visionDroppedRecords"))
)
if mibBuilder.loadTexts:
    visionAttributes.setStatus("current")

obsoleteErfstreamAttributes = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 12, 3, 1, 6)
)
obsoleteErfstreamAttributes.setObjects(
      *(("ENDACE-ERFSTREAM-MIB", "pilotDroppedBytes"),
        ("ENDACE-ERFSTREAM-MIB", "pilotDroppedPackets"))
)
if mibBuilder.loadTexts:
    obsoleteErfstreamAttributes.setStatus("obsolete")

rotationFileAttributes = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 12, 3, 1, 9)
)
rotationFileAttributes.setObjects(
      *(("ENDACE-ERFSTREAM-MIB", "rotationFileCompression"),
        ("ENDACE-ERFSTREAM-MIB", "rotationFileIndex"),
        ("ENDACE-ERFSTREAM-MIB", "rotationFileName"),
        ("ENDACE-ERFSTREAM-MIB", "rotationFileStoredSecs"),
        ("ENDACE-ERFSTREAM-MIB", "rotationFileStartDate"),
        ("ENDACE-ERFSTREAM-MIB", "rotationFileEndDate"))
)
if mibBuilder.loadTexts:
    rotationFileAttributes.setStatus("current")

nicAttributes = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 12, 3, 1, 11)
)
nicAttributes.setObjects(
      *(("ENDACE-ERFSTREAM-MIB", "nicInfoDroppedInBytes"),
        ("ENDACE-ERFSTREAM-MIB", "nicInfoDroppedInPackets"),
        ("ENDACE-ERFSTREAM-MIB", "nicInfoInterface"),
        ("ENDACE-ERFSTREAM-MIB", "nicInfoInUse"))
)
if mibBuilder.loadTexts:
    nicAttributes.setStatus("current")


# Notification objects

pipeDropFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 1)
)
pipeDropFault.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "pipeName")
)
if mibBuilder.loadTexts:
    pipeDropFault.setStatus(
        "current"
    )

pipeDropNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 2)
)
pipeDropNormal.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "pipeName")
)
if mibBuilder.loadTexts:
    pipeDropNormal.setStatus(
        "current"
    )

pilotDropFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 3)
)
pilotDropFault.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "pipeName")
)
if mibBuilder.loadTexts:
    pilotDropFault.setStatus(
        "obsolete"
    )

pilotDropNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 4)
)
pilotDropNormal.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "pipeName")
)
if mibBuilder.loadTexts:
    pilotDropNormal.setStatus(
        "obsolete"
    )

visionDropFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 5)
)
visionDropFault.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "pipeName")
)
if mibBuilder.loadTexts:
    visionDropFault.setStatus(
        "current"
    )

visionDropNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 6)
)
visionDropNormal.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "pipeName")
)
if mibBuilder.loadTexts:
    visionDropNormal.setStatus(
        "current"
    )

visionMetadataDBFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 7)
)
visionMetadataDBFull.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "visionDBRotfileName")
)
if mibBuilder.loadTexts:
    visionMetadataDBFull.setStatus(
        "current"
    )

visionMetadataDBThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 8)
)
visionMetadataDBThreshold.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "visionDBRotfileName")
)
if mibBuilder.loadTexts:
    visionMetadataDBThreshold.setStatus(
        "current"
    )

visionMetadataDBNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 9)
)
visionMetadataDBNormal.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "visionDBRotfileName")
)
if mibBuilder.loadTexts:
    visionMetadataDBNormal.setStatus(
        "current"
    )

visionMetadataDBBelowFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 10)
)
visionMetadataDBBelowFull.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "visionDBRotfileName")
)
if mibBuilder.loadTexts:
    visionMetadataDBBelowFull.setStatus(
        "current"
    )

rotationFilePrematureLossFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 11)
)
rotationFilePrematureLossFault.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "rotationFileName")
)
if mibBuilder.loadTexts:
    rotationFilePrematureLossFault.setStatus(
        "current"
    )

rotationFilePrematureLossNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 12)
)
rotationFilePrematureLossNormal.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "rotationFileName")
)
if mibBuilder.loadTexts:
    rotationFilePrematureLossNormal.setStatus(
        "current"
    )

rotationFilePrematureLossWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 13)
)
rotationFilePrematureLossWarning.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "rotationFileName")
)
if mibBuilder.loadTexts:
    rotationFilePrematureLossWarning.setStatus(
        "current"
    )

nicInDropFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 14)
)
nicInDropFault.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "nicInfoInterface")
)
if mibBuilder.loadTexts:
    nicInDropFault.setStatus(
        "current"
    )

nicInDropNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 15)
)
nicInDropNormal.setObjects(
    ("ENDACE-ERFSTREAM-MIB", "nicInfoInterface")
)
if mibBuilder.loadTexts:
    nicInDropNormal.setStatus(
        "current"
    )

pipeCurrentFlowsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 16)
)
pipeCurrentFlowsHigh.setObjects(
      *(("ENDACE-ERFSTREAM-MIB", "pipeName"),
        ("ENDACE-ERFSTREAM-MIB", "pipeCurrentFlows"))
)
if mibBuilder.loadTexts:
    pipeCurrentFlowsHigh.setStatus(
        "current"
    )

pipeCurrentFlowsNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 17)
)
pipeCurrentFlowsNormal.setObjects(
      *(("ENDACE-ERFSTREAM-MIB", "pipeName"),
        ("ENDACE-ERFSTREAM-MIB", "pipeCurrentFlows"))
)
if mibBuilder.loadTexts:
    pipeCurrentFlowsNormal.setStatus(
        "current"
    )

pipeFlowRateHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 18)
)
pipeFlowRateHigh.setObjects(
      *(("ENDACE-ERFSTREAM-MIB", "pipeName"),
        ("ENDACE-ERFSTREAM-MIB", "pipeFlowRate"))
)
if mibBuilder.loadTexts:
    pipeFlowRateHigh.setStatus(
        "current"
    )

pipeFlowRateNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 19)
)
pipeFlowRateNormal.setObjects(
      *(("ENDACE-ERFSTREAM-MIB", "pipeName"),
        ("ENDACE-ERFSTREAM-MIB", "pipeFlowRate"))
)
if mibBuilder.loadTexts:
    pipeFlowRateNormal.setStatus(
        "current"
    )

pipeRunningStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 12, 2, 0, 20)
)
pipeRunningStatusChange.setObjects(
      *(("ENDACE-ERFSTREAM-MIB", "pipeName"),
        ("ENDACE-ERFSTREAM-MIB", "pipeRunningStatus"))
)
if mibBuilder.loadTexts:
    pipeRunningStatusChange.setStatus(
        "current"
    )


# Notifications groups

pipeEvents = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 12, 3, 1, 3)
)
pipeEvents.setObjects(
      *(("ENDACE-ERFSTREAM-MIB", "pipeCurrentFlowsHigh"),
        ("ENDACE-ERFSTREAM-MIB", "pipeCurrentFlowsNormal"),
        ("ENDACE-ERFSTREAM-MIB", "pipeDropFault"),
        ("ENDACE-ERFSTREAM-MIB", "pipeDropNormal"),
        ("ENDACE-ERFSTREAM-MIB", "visionDropFault"),
        ("ENDACE-ERFSTREAM-MIB", "visionDropNormal"),
        ("ENDACE-ERFSTREAM-MIB", "pipeFlowRateHigh"),
        ("ENDACE-ERFSTREAM-MIB", "pipeFlowRateNormal"),
        ("ENDACE-ERFSTREAM-MIB", "pipeRunningStatusChange"))
)
if mibBuilder.loadTexts:
    pipeEvents.setStatus(
        "current"
    )

visionEvents = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 12, 3, 1, 4)
)
visionEvents.setObjects(
      *(("ENDACE-ERFSTREAM-MIB", "visionMetadataDBFull"),
        ("ENDACE-ERFSTREAM-MIB", "visionMetadataDBThreshold"),
        ("ENDACE-ERFSTREAM-MIB", "visionMetadataDBNormal"),
        ("ENDACE-ERFSTREAM-MIB", "visionMetadataDBBelowFull"))
)
if mibBuilder.loadTexts:
    visionEvents.setStatus(
        "current"
    )

obsoleteErfstreamNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 12, 3, 1, 7)
)
obsoleteErfstreamNotifications.setObjects(
      *(("ENDACE-ERFSTREAM-MIB", "pilotDropFault"),
        ("ENDACE-ERFSTREAM-MIB", "pilotDropNormal"))
)
if mibBuilder.loadTexts:
    obsoleteErfstreamNotifications.setStatus(
        "obsolete"
    )

rotationFileEvents = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 12, 3, 1, 8)
)
rotationFileEvents.setObjects(
      *(("ENDACE-ERFSTREAM-MIB", "rotationFilePrematureLossFault"),
        ("ENDACE-ERFSTREAM-MIB", "rotationFilePrematureLossNormal"),
        ("ENDACE-ERFSTREAM-MIB", "rotationFilePrematureLossWarning"))
)
if mibBuilder.loadTexts:
    rotationFileEvents.setStatus(
        "current"
    )

nicEvents = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 12, 3, 1, 10)
)
nicEvents.setObjects(
      *(("ENDACE-ERFSTREAM-MIB", "nicInDropFault"),
        ("ENDACE-ERFSTREAM-MIB", "nicInDropNormal"))
)
if mibBuilder.loadTexts:
    nicEvents.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENDACE-ERFSTREAM-MIB",
    **{"PipeIndex": PipeIndex,
       "RotationFileIndex": RotationFileIndex,
       "VisionDBIndex": VisionDBIndex,
       "VisionDBVersionIndex": VisionDBVersionIndex,
       "endaceErfstreamMIB": endaceErfstreamMIB,
       "erfstreamVariables": erfstreamVariables,
       "pipeInfoTable": pipeInfoTable,
       "pipeInfoTableEntry": pipeInfoTableEntry,
       "pipeInfoIndex": pipeInfoIndex,
       "pipeName": pipeName,
       "pipeStatusTable": pipeStatusTable,
       "pipeStatusTableEntry": pipeStatusTableEntry,
       "pipeStatusIndex": pipeStatusIndex,
       "pipeInputPackets": pipeInputPackets,
       "pipeInputBytes": pipeInputBytes,
       "pipeOutputPackets": pipeOutputPackets,
       "pipeOutputBytes": pipeOutputBytes,
       "pipeDroppedPackets": pipeDroppedPackets,
       "pipeDroppedBytes": pipeDroppedBytes,
       "pilotDroppedPackets": pilotDroppedPackets,
       "pilotDroppedBytes": pilotDroppedBytes,
       "visionDroppedRecords": visionDroppedRecords,
       "pipeCurrentFlows": pipeCurrentFlows,
       "pipeFlowRate": pipeFlowRate,
       "pipeCreatedFlows": pipeCreatedFlows,
       "pipeDeletedFlows": pipeDeletedFlows,
       "pipeRunningStatus": pipeRunningStatus,
       "visionDBStatusTable": visionDBStatusTable,
       "visionDBStatusTableEntry": visionDBStatusTableEntry,
       "visionDBStatusVersionIndex": visionDBStatusVersionIndex,
       "visionDBStatusIndex": visionDBStatusIndex,
       "visionDBRotfileName": visionDBRotfileName,
       "visionDBUsage": visionDBUsage,
       "rotationFileStatusTable": rotationFileStatusTable,
       "rotationFileStatusTableEntry": rotationFileStatusTableEntry,
       "rotationFileIndex": rotationFileIndex,
       "rotationFileName": rotationFileName,
       "rotationFileStoredSecs": rotationFileStoredSecs,
       "rotationFileCompression": rotationFileCompression,
       "rotationFileStartDate": rotationFileStartDate,
       "rotationFileEndDate": rotationFileEndDate,
       "nicInfoTable": nicInfoTable,
       "nicInfoTableEntry": nicInfoTableEntry,
       "nicInfoIndex": nicInfoIndex,
       "nicInfoInterface": nicInfoInterface,
       "nicInfoDroppedInPackets": nicInfoDroppedInPackets,
       "nicInfoDroppedInBytes": nicInfoDroppedInBytes,
       "nicInfoInUse": nicInfoInUse,
       "eventTraps": eventTraps,
       "erfstreamNotificationPrefix": erfstreamNotificationPrefix,
       "pipeDropFault": pipeDropFault,
       "pipeDropNormal": pipeDropNormal,
       "pilotDropFault": pilotDropFault,
       "pilotDropNormal": pilotDropNormal,
       "visionDropFault": visionDropFault,
       "visionDropNormal": visionDropNormal,
       "visionMetadataDBFull": visionMetadataDBFull,
       "visionMetadataDBThreshold": visionMetadataDBThreshold,
       "visionMetadataDBNormal": visionMetadataDBNormal,
       "visionMetadataDBBelowFull": visionMetadataDBBelowFull,
       "rotationFilePrematureLossFault": rotationFilePrematureLossFault,
       "rotationFilePrematureLossNormal": rotationFilePrematureLossNormal,
       "rotationFilePrematureLossWarning": rotationFilePrematureLossWarning,
       "nicInDropFault": nicInDropFault,
       "nicInDropNormal": nicInDropNormal,
       "pipeCurrentFlowsHigh": pipeCurrentFlowsHigh,
       "pipeCurrentFlowsNormal": pipeCurrentFlowsNormal,
       "pipeFlowRateHigh": pipeFlowRateHigh,
       "pipeFlowRateNormal": pipeFlowRateNormal,
       "pipeRunningStatusChange": pipeRunningStatusChange,
       "erfstreamConf": erfstreamConf,
       "erfstreamGroups": erfstreamGroups,
       "pipeAttributes": pipeAttributes,
       "pipeStatus": pipeStatus,
       "pipeEvents": pipeEvents,
       "visionEvents": visionEvents,
       "visionAttributes": visionAttributes,
       "obsoleteErfstreamAttributes": obsoleteErfstreamAttributes,
       "obsoleteErfstreamNotifications": obsoleteErfstreamNotifications,
       "rotationFileEvents": rotationFileEvents,
       "rotationFileAttributes": rotationFileAttributes,
       "nicEvents": nicEvents,
       "nicAttributes": nicAttributes}
)
