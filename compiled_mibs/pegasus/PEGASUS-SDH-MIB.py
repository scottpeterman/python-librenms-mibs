# SNMP MIB module (PEGASUS-SDH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\pegasus\PEGASUS-SDH-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:38 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(AvailabilityStatusElem,
 CommStateEnum,
 OperStateEnum,
 pegasusMibModule) = mibBuilder.importSymbols(
    "PEGASUS-MIB",
    "AvailabilityStatusElem",
    "CommStateEnum",
    "OperStateEnum",
    "pegasusMibModule")

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


# MODULE-IDENTITY

pegasusSdhMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8)
)
if mibBuilder.loadTexts:
    pegasusSdhMibModule.setRevisions(
        ("2004-03-18 00:00",
         "2004-01-07 00:00",
         "2003-11-17 00:00")
    )


# Types definitions



class ClockSourceEnum(Integer32):
    """Custom type ClockSourceEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rxLineClock", 1),
          ("referenceClock", 2),
          ("freeRun", 3))
    )





class ClockSyncStateEnum(Integer32):
    """Custom type ClockSyncStateEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("syncOk", 1),
          ("syncNotOk", 2))
    )





class ClockModeEnum(Integer32):
    """Custom type ClockModeEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )





class ClockPriorityEnum(Integer32):
    """Custom type ClockPriorityEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )





class ClockQualityEnum(Integer32):
    """Custom type ClockQualityEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("prc", 1),
          ("ssu-a", 2),
          ("ssu-b", 3),
          ("sec", 4),
          ("dnu", 5),
          ("auto", 6),
          ("unknown", 7))
    )





class ClockStateEnum(Integer32):
    """Custom type ClockStateEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )





class MultiplexingModeEnum(Integer32):
    """Custom type MultiplexingModeEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("au3", 1),
          ("au4", 2))
    )





class VirtualContainerTypeEnum(Integer32):
    """Custom type VirtualContainerTypeEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vc4", 1),
          ("vc3", 2),
          ("vc12", 3))
    )





class LaserOperationModeEnum(Integer32):
    """Custom type LaserOperationModeEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("als", 2))
    )





class LaserStateEnum(Integer32):
    """Custom type LaserStateEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("shutdown", 2),
          ("restart", 3))
    )





class SdhInterfaceEnum(Integer32):
    """Custom type SdhInterfaceEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("optical", 1),
          ("e1", 2))
    )





class PRBSPatternEnum(Integer32):
    """Custom type PRBSPatternEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pattern2exp15", 1),
          ("pattern2exp20", 2))
    )





class TraceSizeEnum(Integer32):
    """Custom type TraceSizeEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("size1byte", 1),
          ("size16byte", 2))
    )





class ConcatenationTypeEnum(Integer32):
    """Custom type ConcatenationTypeEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lcas", 1),
          ("nonLCAS", 2))
    )





class EthernetIfEncapsulationEnum(Integer32):
    """Custom type EthernetIfEncapsulationEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("gfp", 2),
          ("lapf", 3),
          ("laps", 4),
          ("ppp", 5))
    )





class OrderLevelEnum(Integer32):
    """Custom type OrderLevelEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highOrder", 1),
          ("lowOrder", 2))
    )





class STM1SlotNumber(Integer32):
    """Custom type STM1SlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )





class TUGIndex(Integer32):
    """Custom type TUGIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )





class TUGIndexOrZero(Integer32):
    """Custom type TUGIndexOrZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )




# TEXTUAL-CONVENTIONS



class SignalLabel(TextualConvention, Integer32):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(18, 26),
        ValueRangeConstraint(207, 207),
        ValueRangeConstraint(225, 252),
        ValueRangeConstraint(254, 255),
    )



# MIB Managed Objects in the order of their OIDs

_Stm1CardTable_Object = MibTable
stm1CardTable = _Stm1CardTable_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1)
)
if mibBuilder.loadTexts:
    stm1CardTable.setStatus("current")
_Stm1CardEntry_Object = MibTableRow
stm1CardEntry = _Stm1CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1)
)
stm1CardEntry.setIndexNames(
    (0, "PEGASUS-SDH-MIB", "stm1CardSlotNumber"),
)
if mibBuilder.loadTexts:
    stm1CardEntry.setStatus("current")
_Stm1CardSlotNumber_Type = STM1SlotNumber
_Stm1CardSlotNumber_Object = MibTableColumn
stm1CardSlotNumber = _Stm1CardSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 1),
    _Stm1CardSlotNumber_Type()
)
stm1CardSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stm1CardSlotNumber.setStatus("current")
_Stm1CardName_Type = DisplayString
_Stm1CardName_Object = MibTableColumn
stm1CardName = _Stm1CardName_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 2),
    _Stm1CardName_Type()
)
stm1CardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm1CardName.setStatus("current")
_Stm1CardHardwareVersion_Type = DisplayString
_Stm1CardHardwareVersion_Object = MibTableColumn
stm1CardHardwareVersion = _Stm1CardHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 3),
    _Stm1CardHardwareVersion_Type()
)
stm1CardHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm1CardHardwareVersion.setStatus("current")
_Stm1CardFirmwareVersion_Type = DisplayString
_Stm1CardFirmwareVersion_Object = MibTableColumn
stm1CardFirmwareVersion = _Stm1CardFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 4),
    _Stm1CardFirmwareVersion_Type()
)
stm1CardFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm1CardFirmwareVersion.setStatus("current")
_Stm1CardManufacturer_Type = DisplayString
_Stm1CardManufacturer_Object = MibTableColumn
stm1CardManufacturer = _Stm1CardManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 5),
    _Stm1CardManufacturer_Type()
)
stm1CardManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm1CardManufacturer.setStatus("current")
_Stm1CardSerialNumber_Type = DisplayString
_Stm1CardSerialNumber_Object = MibTableColumn
stm1CardSerialNumber = _Stm1CardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 6),
    _Stm1CardSerialNumber_Type()
)
stm1CardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm1CardSerialNumber.setStatus("current")
_Stm1CardMultiplexingMode_Type = MultiplexingModeEnum
_Stm1CardMultiplexingMode_Object = MibTableColumn
stm1CardMultiplexingMode = _Stm1CardMultiplexingMode_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 7),
    _Stm1CardMultiplexingMode_Type()
)
stm1CardMultiplexingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stm1CardMultiplexingMode.setStatus("current")
_Stm1CardJ0TraceMonitoring_Type = OperStateEnum
_Stm1CardJ0TraceMonitoring_Object = MibTableColumn
stm1CardJ0TraceMonitoring = _Stm1CardJ0TraceMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 8),
    _Stm1CardJ0TraceMonitoring_Type()
)
stm1CardJ0TraceMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stm1CardJ0TraceMonitoring.setStatus("current")
_Stm1CardJ1TraceMonitoring_Type = OperStateEnum
_Stm1CardJ1TraceMonitoring_Object = MibTableColumn
stm1CardJ1TraceMonitoring = _Stm1CardJ1TraceMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 9),
    _Stm1CardJ1TraceMonitoring_Type()
)
stm1CardJ1TraceMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stm1CardJ1TraceMonitoring.setStatus("current")
_Stm1CardJ2TraceMonitoring_Type = OperStateEnum
_Stm1CardJ2TraceMonitoring_Object = MibTableColumn
stm1CardJ2TraceMonitoring = _Stm1CardJ2TraceMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 10),
    _Stm1CardJ2TraceMonitoring_Type()
)
stm1CardJ2TraceMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stm1CardJ2TraceMonitoring.setStatus("current")
_Stm1CardJ0PathTraceSize_Type = TraceSizeEnum
_Stm1CardJ0PathTraceSize_Object = MibTableColumn
stm1CardJ0PathTraceSize = _Stm1CardJ0PathTraceSize_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 11),
    _Stm1CardJ0PathTraceSize_Type()
)
stm1CardJ0PathTraceSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stm1CardJ0PathTraceSize.setStatus("current")
_Stm1CardJ0PathTraceSend_Type = DisplayString
_Stm1CardJ0PathTraceSend_Object = MibTableColumn
stm1CardJ0PathTraceSend = _Stm1CardJ0PathTraceSend_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 12),
    _Stm1CardJ0PathTraceSend_Type()
)
stm1CardJ0PathTraceSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stm1CardJ0PathTraceSend.setStatus("current")
_Stm1CardJ0PathTraceExpected_Type = DisplayString
_Stm1CardJ0PathTraceExpected_Object = MibTableColumn
stm1CardJ0PathTraceExpected = _Stm1CardJ0PathTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 13),
    _Stm1CardJ0PathTraceExpected_Type()
)
stm1CardJ0PathTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stm1CardJ0PathTraceExpected.setStatus("current")
_Stm1CardJ0PathTraceReceive_Type = DisplayString
_Stm1CardJ0PathTraceReceive_Object = MibTableColumn
stm1CardJ0PathTraceReceive = _Stm1CardJ0PathTraceReceive_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 14),
    _Stm1CardJ0PathTraceReceive_Type()
)
stm1CardJ0PathTraceReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm1CardJ0PathTraceReceive.setStatus("current")
_Stm1CardLaserOperationMode_Type = LaserOperationModeEnum
_Stm1CardLaserOperationMode_Object = MibTableColumn
stm1CardLaserOperationMode = _Stm1CardLaserOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 15),
    _Stm1CardLaserOperationMode_Type()
)
stm1CardLaserOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stm1CardLaserOperationMode.setStatus("current")
_Stm1CardLaserState_Type = LaserStateEnum
_Stm1CardLaserState_Object = MibTableColumn
stm1CardLaserState = _Stm1CardLaserState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 16),
    _Stm1CardLaserState_Type()
)
stm1CardLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm1CardLaserState.setStatus("current")
_Stm1CardOperState_Type = OperStateEnum
_Stm1CardOperState_Object = MibTableColumn
stm1CardOperState = _Stm1CardOperState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 17),
    _Stm1CardOperState_Type()
)
stm1CardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm1CardOperState.setStatus("current")
_Stm1CardAvailabilityState_Type = AvailabilityStatusElem
_Stm1CardAvailabilityState_Object = MibTableColumn
stm1CardAvailabilityState = _Stm1CardAvailabilityState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 18),
    _Stm1CardAvailabilityState_Type()
)
stm1CardAvailabilityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm1CardAvailabilityState.setStatus("current")
_Stm1CardMgmtCommState_Type = CommStateEnum
_Stm1CardMgmtCommState_Object = MibTableColumn
stm1CardMgmtCommState = _Stm1CardMgmtCommState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 19),
    _Stm1CardMgmtCommState_Type()
)
stm1CardMgmtCommState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm1CardMgmtCommState.setStatus("current")
_Stm1CardPRBSGeneratorSink_Type = SdhInterfaceEnum
_Stm1CardPRBSGeneratorSink_Object = MibTableColumn
stm1CardPRBSGeneratorSink = _Stm1CardPRBSGeneratorSink_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 20),
    _Stm1CardPRBSGeneratorSink_Type()
)
stm1CardPRBSGeneratorSink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stm1CardPRBSGeneratorSink.setStatus("current")
_Stm1CardPRBSAnalyzerSource_Type = SdhInterfaceEnum
_Stm1CardPRBSAnalyzerSource_Object = MibTableColumn
stm1CardPRBSAnalyzerSource = _Stm1CardPRBSAnalyzerSource_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 21),
    _Stm1CardPRBSAnalyzerSource_Type()
)
stm1CardPRBSAnalyzerSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stm1CardPRBSAnalyzerSource.setStatus("current")
_Stm1CardPRBSPattern_Type = PRBSPatternEnum
_Stm1CardPRBSPattern_Object = MibTableColumn
stm1CardPRBSPattern = _Stm1CardPRBSPattern_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 22),
    _Stm1CardPRBSPattern_Type()
)
stm1CardPRBSPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stm1CardPRBSPattern.setStatus("current")


class _Stm1CardAlarmStatus_Type(Integer32):
    """Custom type stm1CardAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511),
    )


_Stm1CardAlarmStatus_Type.__name__ = "Integer32"
_Stm1CardAlarmStatus_Object = MibTableColumn
stm1CardAlarmStatus = _Stm1CardAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 23),
    _Stm1CardAlarmStatus_Type()
)
stm1CardAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm1CardAlarmStatus.setStatus("current")
_Stm1CardClockTable_Object = MibTable
stm1CardClockTable = _Stm1CardClockTable_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 2)
)
if mibBuilder.loadTexts:
    stm1CardClockTable.setStatus("current")
_Stm1CardClockEntry_Object = MibTableRow
stm1CardClockEntry = _Stm1CardClockEntry_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1)
)
stm1CardClockEntry.setIndexNames(
    (0, "PEGASUS-SDH-MIB", "stm1CardSlotNumber"),
)
if mibBuilder.loadTexts:
    stm1CardClockEntry.setStatus("current")
_Stm1CardActiveClockSource_Type = ClockSourceEnum
_Stm1CardActiveClockSource_Object = MibTableColumn
stm1CardActiveClockSource = _Stm1CardActiveClockSource_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 1),
    _Stm1CardActiveClockSource_Type()
)
stm1CardActiveClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm1CardActiveClockSource.setStatus("current")
_Stm1CardClockSyncState_Type = ClockSyncStateEnum
_Stm1CardClockSyncState_Object = MibTableColumn
stm1CardClockSyncState = _Stm1CardClockSyncState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 2),
    _Stm1CardClockSyncState_Type()
)
stm1CardClockSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm1CardClockSyncState.setStatus("current")
_Stm1CardTxLineClockQuality_Type = ClockQualityEnum
_Stm1CardTxLineClockQuality_Object = MibTableColumn
stm1CardTxLineClockQuality = _Stm1CardTxLineClockQuality_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 3),
    _Stm1CardTxLineClockQuality_Type()
)
stm1CardTxLineClockQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stm1CardTxLineClockQuality.setStatus("current")
_Stm1CardRxClockMode_Type = ClockModeEnum
_Stm1CardRxClockMode_Object = MibTableColumn
stm1CardRxClockMode = _Stm1CardRxClockMode_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 4),
    _Stm1CardRxClockMode_Type()
)
stm1CardRxClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stm1CardRxClockMode.setStatus("current")
_Stm1CardRxClockPriority_Type = ClockPriorityEnum
_Stm1CardRxClockPriority_Object = MibTableColumn
stm1CardRxClockPriority = _Stm1CardRxClockPriority_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 5),
    _Stm1CardRxClockPriority_Type()
)
stm1CardRxClockPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stm1CardRxClockPriority.setStatus("current")
_Stm1CardRxClockQuality_Type = ClockQualityEnum
_Stm1CardRxClockQuality_Object = MibTableColumn
stm1CardRxClockQuality = _Stm1CardRxClockQuality_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 6),
    _Stm1CardRxClockQuality_Type()
)
stm1CardRxClockQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm1CardRxClockQuality.setStatus("current")
_Stm1CardRxClockState_Type = ClockStateEnum
_Stm1CardRxClockState_Object = MibTableColumn
stm1CardRxClockState = _Stm1CardRxClockState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 7),
    _Stm1CardRxClockState_Type()
)
stm1CardRxClockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm1CardRxClockState.setStatus("current")
_Stm1CardReferenceClockMode_Type = ClockModeEnum
_Stm1CardReferenceClockMode_Object = MibTableColumn
stm1CardReferenceClockMode = _Stm1CardReferenceClockMode_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 8),
    _Stm1CardReferenceClockMode_Type()
)
stm1CardReferenceClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stm1CardReferenceClockMode.setStatus("current")
_Stm1CardReferenceClockPriority_Type = ClockPriorityEnum
_Stm1CardReferenceClockPriority_Object = MibTableColumn
stm1CardReferenceClockPriority = _Stm1CardReferenceClockPriority_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 9),
    _Stm1CardReferenceClockPriority_Type()
)
stm1CardReferenceClockPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stm1CardReferenceClockPriority.setStatus("current")
_Stm1CardReferenceClockQuality_Type = ClockQualityEnum
_Stm1CardReferenceClockQuality_Object = MibTableColumn
stm1CardReferenceClockQuality = _Stm1CardReferenceClockQuality_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 10),
    _Stm1CardReferenceClockQuality_Type()
)
stm1CardReferenceClockQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stm1CardReferenceClockQuality.setStatus("current")
_Stm1CardReferenceClockState_Type = ClockStateEnum
_Stm1CardReferenceClockState_Object = MibTableColumn
stm1CardReferenceClockState = _Stm1CardReferenceClockState_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 11),
    _Stm1CardReferenceClockState_Type()
)
stm1CardReferenceClockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm1CardReferenceClockState.setStatus("current")
_EthernetIfTable_Object = MibTable
ethernetIfTable = _EthernetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 3)
)
if mibBuilder.loadTexts:
    ethernetIfTable.setStatus("current")
_EthernetIfEntry_Object = MibTableRow
ethernetIfEntry = _EthernetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 3, 1)
)
ethernetIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ethernetIfEntry.setStatus("current")
_EtherIfConcatenationOption_Type = ConcatenationTypeEnum
_EtherIfConcatenationOption_Object = MibTableColumn
etherIfConcatenationOption = _EtherIfConcatenationOption_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 3, 1, 1),
    _EtherIfConcatenationOption_Type()
)
etherIfConcatenationOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherIfConcatenationOption.setStatus("current")
_EtherIfEncapsulation_Type = EthernetIfEncapsulationEnum
_EtherIfEncapsulation_Object = MibTableColumn
etherIfEncapsulation = _EtherIfEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 3, 1, 2),
    _EtherIfEncapsulation_Type()
)
etherIfEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfEncapsulation.setStatus("current")
_EtherIfOrderLevel_Type = OrderLevelEnum
_EtherIfOrderLevel_Object = MibTableColumn
etherIfOrderLevel = _EtherIfOrderLevel_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 3, 1, 3),
    _EtherIfOrderLevel_Type()
)
etherIfOrderLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfOrderLevel.setStatus("current")


class _EtherIfAlarmStatus_Type(Integer32):
    """Custom type etherIfAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511),
    )


_EtherIfAlarmStatus_Type.__name__ = "Integer32"
_EtherIfAlarmStatus_Object = MibTableColumn
etherIfAlarmStatus = _EtherIfAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 3, 1, 4),
    _EtherIfAlarmStatus_Type()
)
etherIfAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfAlarmStatus.setStatus("current")
_VcTable_Object = MibTable
vcTable = _VcTable_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 4)
)
if mibBuilder.loadTexts:
    vcTable.setStatus("current")
_VcEntry_Object = MibTableRow
vcEntry = _VcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1)
)
vcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vcEntry.setStatus("current")
_VcType_Type = VirtualContainerTypeEnum
_VcType_Object = MibTableColumn
vcType = _VcType_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 1),
    _VcType_Type()
)
vcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcType.setStatus("current")
_VcRelatedTUG_Type = TUGIndexOrZero
_VcRelatedTUG_Object = MibTableColumn
vcRelatedTUG = _VcRelatedTUG_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 2),
    _VcRelatedTUG_Type()
)
vcRelatedTUG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcRelatedTUG.setStatus("current")
_VcRelatedVC_Type = InterfaceIndexOrZero
_VcRelatedVC_Object = MibTableColumn
vcRelatedVC = _VcRelatedVC_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 3),
    _VcRelatedVC_Type()
)
vcRelatedVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcRelatedVC.setStatus("current")
_VcAssignedIfIndex_Type = InterfaceIndexOrZero
_VcAssignedIfIndex_Object = MibTableColumn
vcAssignedIfIndex = _VcAssignedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 4),
    _VcAssignedIfIndex_Type()
)
vcAssignedIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vcAssignedIfIndex.setStatus("current")
_VcPathTraceSend_Type = DisplayString
_VcPathTraceSend_Object = MibTableColumn
vcPathTraceSend = _VcPathTraceSend_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 5),
    _VcPathTraceSend_Type()
)
vcPathTraceSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vcPathTraceSend.setStatus("current")
_VcPathTraceExpected_Type = DisplayString
_VcPathTraceExpected_Object = MibTableColumn
vcPathTraceExpected = _VcPathTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 6),
    _VcPathTraceExpected_Type()
)
vcPathTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vcPathTraceExpected.setStatus("current")
_VcPathTraceReceive_Type = DisplayString
_VcPathTraceReceive_Object = MibTableColumn
vcPathTraceReceive = _VcPathTraceReceive_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 7),
    _VcPathTraceReceive_Type()
)
vcPathTraceReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPathTraceReceive.setStatus("current")
_VcSignalLabelSend_Type = SignalLabel
_VcSignalLabelSend_Object = MibTableColumn
vcSignalLabelSend = _VcSignalLabelSend_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 8),
    _VcSignalLabelSend_Type()
)
vcSignalLabelSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vcSignalLabelSend.setStatus("current")
_VcSignalLabelExpected_Type = SignalLabel
_VcSignalLabelExpected_Object = MibTableColumn
vcSignalLabelExpected = _VcSignalLabelExpected_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 9),
    _VcSignalLabelExpected_Type()
)
vcSignalLabelExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vcSignalLabelExpected.setStatus("current")
_VcSignalLabelReceive_Type = SignalLabel
_VcSignalLabelReceive_Object = MibTableColumn
vcSignalLabelReceive = _VcSignalLabelReceive_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 10),
    _VcSignalLabelReceive_Type()
)
vcSignalLabelReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcSignalLabelReceive.setStatus("current")


class _VcAlarmStatus_Type(Integer32):
    """Custom type vcAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 524287),
    )


_VcAlarmStatus_Type.__name__ = "Integer32"
_VcAlarmStatus_Object = MibTableColumn
vcAlarmStatus = _VcAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 11),
    _VcAlarmStatus_Type()
)
vcAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcAlarmStatus.setStatus("current")
_TugConfigTable_Object = MibTable
tugConfigTable = _TugConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 5)
)
if mibBuilder.loadTexts:
    tugConfigTable.setStatus("current")
_TugConfigEntry_Object = MibTableRow
tugConfigEntry = _TugConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 5, 1)
)
tugConfigEntry.setIndexNames(
    (0, "PEGASUS-SDH-MIB", "tugIndex"),
)
if mibBuilder.loadTexts:
    tugConfigEntry.setStatus("current")
_TugIndex_Type = TUGIndex
_TugIndex_Object = MibTableColumn
tugIndex = _TugIndex_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 5, 1, 1),
    _TugIndex_Type()
)
tugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tugIndex.setStatus("current")
_TugRelatedVC4_Type = InterfaceIndex
_TugRelatedVC4_Object = MibTableColumn
tugRelatedVC4 = _TugRelatedVC4_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 5, 1, 2),
    _TugRelatedVC4_Type()
)
tugRelatedVC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tugRelatedVC4.setStatus("current")
_TugOrderLevel_Type = OrderLevelEnum
_TugOrderLevel_Object = MibTableColumn
tugOrderLevel = _TugOrderLevel_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 5, 1, 3),
    _TugOrderLevel_Type()
)
tugOrderLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tugOrderLevel.setStatus("current")


class _SdhMibRevision_Type(DisplayString):
    """Custom type sdhMibRevision based on DisplayString"""
    defaultValue = OctetString("$Workfile: PEGASUS-SDH-MIB.txt $ $Revision: 14 $ $Date: 3/18/04 6:40p $")


_SdhMibRevision_Type.__name__ = "DisplayString"
_SdhMibRevision_Object = MibScalar
sdhMibRevision = _SdhMibRevision_Object(
    (1, 3, 6, 1, 4, 1, 6368, 2, 8, 6),
    _SdhMibRevision_Type()
)
sdhMibRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhMibRevision.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEGASUS-SDH-MIB",
    **{"ClockSourceEnum": ClockSourceEnum,
       "ClockSyncStateEnum": ClockSyncStateEnum,
       "ClockModeEnum": ClockModeEnum,
       "ClockPriorityEnum": ClockPriorityEnum,
       "ClockQualityEnum": ClockQualityEnum,
       "ClockStateEnum": ClockStateEnum,
       "MultiplexingModeEnum": MultiplexingModeEnum,
       "VirtualContainerTypeEnum": VirtualContainerTypeEnum,
       "LaserOperationModeEnum": LaserOperationModeEnum,
       "LaserStateEnum": LaserStateEnum,
       "SdhInterfaceEnum": SdhInterfaceEnum,
       "PRBSPatternEnum": PRBSPatternEnum,
       "TraceSizeEnum": TraceSizeEnum,
       "SignalLabel": SignalLabel,
       "ConcatenationTypeEnum": ConcatenationTypeEnum,
       "EthernetIfEncapsulationEnum": EthernetIfEncapsulationEnum,
       "OrderLevelEnum": OrderLevelEnum,
       "STM1SlotNumber": STM1SlotNumber,
       "TUGIndex": TUGIndex,
       "TUGIndexOrZero": TUGIndexOrZero,
       "pegasusSdhMibModule": pegasusSdhMibModule,
       "stm1CardTable": stm1CardTable,
       "stm1CardEntry": stm1CardEntry,
       "stm1CardSlotNumber": stm1CardSlotNumber,
       "stm1CardName": stm1CardName,
       "stm1CardHardwareVersion": stm1CardHardwareVersion,
       "stm1CardFirmwareVersion": stm1CardFirmwareVersion,
       "stm1CardManufacturer": stm1CardManufacturer,
       "stm1CardSerialNumber": stm1CardSerialNumber,
       "stm1CardMultiplexingMode": stm1CardMultiplexingMode,
       "stm1CardJ0TraceMonitoring": stm1CardJ0TraceMonitoring,
       "stm1CardJ1TraceMonitoring": stm1CardJ1TraceMonitoring,
       "stm1CardJ2TraceMonitoring": stm1CardJ2TraceMonitoring,
       "stm1CardJ0PathTraceSize": stm1CardJ0PathTraceSize,
       "stm1CardJ0PathTraceSend": stm1CardJ0PathTraceSend,
       "stm1CardJ0PathTraceExpected": stm1CardJ0PathTraceExpected,
       "stm1CardJ0PathTraceReceive": stm1CardJ0PathTraceReceive,
       "stm1CardLaserOperationMode": stm1CardLaserOperationMode,
       "stm1CardLaserState": stm1CardLaserState,
       "stm1CardOperState": stm1CardOperState,
       "stm1CardAvailabilityState": stm1CardAvailabilityState,
       "stm1CardMgmtCommState": stm1CardMgmtCommState,
       "stm1CardPRBSGeneratorSink": stm1CardPRBSGeneratorSink,
       "stm1CardPRBSAnalyzerSource": stm1CardPRBSAnalyzerSource,
       "stm1CardPRBSPattern": stm1CardPRBSPattern,
       "stm1CardAlarmStatus": stm1CardAlarmStatus,
       "stm1CardClockTable": stm1CardClockTable,
       "stm1CardClockEntry": stm1CardClockEntry,
       "stm1CardActiveClockSource": stm1CardActiveClockSource,
       "stm1CardClockSyncState": stm1CardClockSyncState,
       "stm1CardTxLineClockQuality": stm1CardTxLineClockQuality,
       "stm1CardRxClockMode": stm1CardRxClockMode,
       "stm1CardRxClockPriority": stm1CardRxClockPriority,
       "stm1CardRxClockQuality": stm1CardRxClockQuality,
       "stm1CardRxClockState": stm1CardRxClockState,
       "stm1CardReferenceClockMode": stm1CardReferenceClockMode,
       "stm1CardReferenceClockPriority": stm1CardReferenceClockPriority,
       "stm1CardReferenceClockQuality": stm1CardReferenceClockQuality,
       "stm1CardReferenceClockState": stm1CardReferenceClockState,
       "ethernetIfTable": ethernetIfTable,
       "ethernetIfEntry": ethernetIfEntry,
       "etherIfConcatenationOption": etherIfConcatenationOption,
       "etherIfEncapsulation": etherIfEncapsulation,
       "etherIfOrderLevel": etherIfOrderLevel,
       "etherIfAlarmStatus": etherIfAlarmStatus,
       "vcTable": vcTable,
       "vcEntry": vcEntry,
       "vcType": vcType,
       "vcRelatedTUG": vcRelatedTUG,
       "vcRelatedVC": vcRelatedVC,
       "vcAssignedIfIndex": vcAssignedIfIndex,
       "vcPathTraceSend": vcPathTraceSend,
       "vcPathTraceExpected": vcPathTraceExpected,
       "vcPathTraceReceive": vcPathTraceReceive,
       "vcSignalLabelSend": vcSignalLabelSend,
       "vcSignalLabelExpected": vcSignalLabelExpected,
       "vcSignalLabelReceive": vcSignalLabelReceive,
       "vcAlarmStatus": vcAlarmStatus,
       "tugConfigTable": tugConfigTable,
       "tugConfigEntry": tugConfigEntry,
       "tugIndex": tugIndex,
       "tugRelatedVC4": tugRelatedVC4,
       "tugOrderLevel": tugOrderLevel,
       "sdhMibRevision": sdhMibRevision}
)
