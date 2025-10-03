# SNMP MIB module (TELECOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\eaton\TELECOM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:40 2025
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class PositiveInteger(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class NonNegativeInteger(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_Ppc_ObjectIdentity = ObjectIdentity
ppc = _Ppc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10)
)
_MatAgent_ObjectIdentity = ObjectIdentity
matAgent = _MatAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 2)
)
_MatObjects_ObjectIdentity = ObjectIdentity
matObjects = _MatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1)
)
_MatController_ObjectIdentity = ObjectIdentity
matController = _MatController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 1)
)


class _MatConSerialNum_Type(DisplayString):
    """Custom type matConSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MatConSerialNum_Type.__name__ = "DisplayString"
_MatConSerialNum_Object = MibScalar
matConSerialNum = _MatConSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 1, 1),
    _MatConSerialNum_Type()
)
matConSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matConSerialNum.setStatus("mandatory")


class _MatConName_Type(DisplayString):
    """Custom type matConName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MatConName_Type.__name__ = "DisplayString"
_MatConName_Object = MibScalar
matConName = _MatConName_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 1, 2),
    _MatConName_Type()
)
matConName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matConName.setStatus("mandatory")


class _MatConWarningState_Type(DisplayString):
    """Custom type matConWarningState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MatConWarningState_Type.__name__ = "DisplayString"
_MatConWarningState_Object = MibScalar
matConWarningState = _MatConWarningState_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 1, 3),
    _MatConWarningState_Type()
)
matConWarningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matConWarningState.setStatus("mandatory")
_MatConTemperature_Type = Integer32
_MatConTemperature_Object = MibScalar
matConTemperature = _MatConTemperature_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 1, 4),
    _MatConTemperature_Type()
)
matConTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matConTemperature.setStatus("mandatory")


class _MatAgentSoftwareVerison_Type(DisplayString):
    """Custom type matAgentSoftwareVerison based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MatAgentSoftwareVerison_Type.__name__ = "DisplayString"
_MatAgentSoftwareVerison_Object = MibScalar
matAgentSoftwareVerison = _MatAgentSoftwareVerison_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 1, 5),
    _MatAgentSoftwareVerison_Type()
)
matAgentSoftwareVerison.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matAgentSoftwareVerison.setStatus("mandatory")
_MatInverter_ObjectIdentity = ObjectIdentity
matInverter = _MatInverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2)
)
_MatInvModuleNum_Type = Integer32
_MatInvModuleNum_Object = MibScalar
matInvModuleNum = _MatInvModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 1),
    _MatInvModuleNum_Type()
)
matInvModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matInvModuleNum.setStatus("mandatory")
_MatInvTable_Object = MibTable
matInvTable = _MatInvTable_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    matInvTable.setStatus("mandatory")
_MatInvEntry_Object = MibTableRow
matInvEntry = _MatInvEntry_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1)
)
matInvEntry.setIndexNames(
    (0, "TELECOM-MIB", "matInvModuleIndex"),
)
if mibBuilder.loadTexts:
    matInvEntry.setStatus("mandatory")
_MatInvModuleIndex_Type = PositiveInteger
_MatInvModuleIndex_Object = MibTableColumn
matInvModuleIndex = _MatInvModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 1),
    _MatInvModuleIndex_Type()
)
matInvModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    matInvModuleIndex.setStatus("mandatory")


class _MatInvSerialNum_Type(DisplayString):
    """Custom type matInvSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MatInvSerialNum_Type.__name__ = "DisplayString"
_MatInvSerialNum_Object = MibTableColumn
matInvSerialNum = _MatInvSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 2),
    _MatInvSerialNum_Type()
)
matInvSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matInvSerialNum.setStatus("mandatory")


class _MatInvFirmwareVersion_Type(DisplayString):
    """Custom type matInvFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_MatInvFirmwareVersion_Type.__name__ = "DisplayString"
_MatInvFirmwareVersion_Object = MibTableColumn
matInvFirmwareVersion = _MatInvFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 3),
    _MatInvFirmwareVersion_Type()
)
matInvFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matInvFirmwareVersion.setStatus("mandatory")


class _MatInvHardwareVersion_Type(DisplayString):
    """Custom type matInvHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_MatInvHardwareVersion_Type.__name__ = "DisplayString"
_MatInvHardwareVersion_Object = MibTableColumn
matInvHardwareVersion = _MatInvHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 4),
    _MatInvHardwareVersion_Type()
)
matInvHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matInvHardwareVersion.setStatus("mandatory")


class _MatInvWarningState_Type(DisplayString):
    """Custom type matInvWarningState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MatInvWarningState_Type.__name__ = "DisplayString"
_MatInvWarningState_Object = MibTableColumn
matInvWarningState = _MatInvWarningState_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 5),
    _MatInvWarningState_Type()
)
matInvWarningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matInvWarningState.setStatus("mandatory")
_MatInvOutputVoltage_Type = NonNegativeInteger
_MatInvOutputVoltage_Object = MibTableColumn
matInvOutputVoltage = _MatInvOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 6),
    _MatInvOutputVoltage_Type()
)
matInvOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matInvOutputVoltage.setStatus("mandatory")
_MatInvOutputCurrent_Type = NonNegativeInteger
_MatInvOutputCurrent_Object = MibTableColumn
matInvOutputCurrent = _MatInvOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 7),
    _MatInvOutputCurrent_Type()
)
matInvOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matInvOutputCurrent.setStatus("mandatory")
_MatInvBatteryVoltage_Type = NonNegativeInteger
_MatInvBatteryVoltage_Object = MibTableColumn
matInvBatteryVoltage = _MatInvBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 8),
    _MatInvBatteryVoltage_Type()
)
matInvBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matInvBatteryVoltage.setStatus("mandatory")
_MatInvOutputFreq_Type = NonNegativeInteger
_MatInvOutputFreq_Object = MibTableColumn
matInvOutputFreq = _MatInvOutputFreq_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 9),
    _MatInvOutputFreq_Type()
)
matInvOutputFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matInvOutputFreq.setStatus("mandatory")
_MatInvOutputPower_Type = NonNegativeInteger
_MatInvOutputPower_Object = MibTableColumn
matInvOutputPower = _MatInvOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 10),
    _MatInvOutputPower_Type()
)
matInvOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matInvOutputPower.setStatus("mandatory")
_MatInvPowerLimit_Type = NonNegativeInteger
_MatInvPowerLimit_Object = MibTableColumn
matInvPowerLimit = _MatInvPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 11),
    _MatInvPowerLimit_Type()
)
matInvPowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matInvPowerLimit.setStatus("mandatory")
_MatInvRunTime_Type = NonNegativeInteger
_MatInvRunTime_Object = MibTableColumn
matInvRunTime = _MatInvRunTime_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 12),
    _MatInvRunTime_Type()
)
matInvRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matInvRunTime.setStatus("mandatory")
_MatInvTemperature_Type = Integer32
_MatInvTemperature_Object = MibTableColumn
matInvTemperature = _MatInvTemperature_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 13),
    _MatInvTemperature_Type()
)
matInvTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matInvTemperature.setStatus("mandatory")
_MatInvLineVoltage_Type = NonNegativeInteger
_MatInvLineVoltage_Object = MibTableColumn
matInvLineVoltage = _MatInvLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 14),
    _MatInvLineVoltage_Type()
)
matInvLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matInvLineVoltage.setStatus("mandatory")
_MatInvLineFreq_Type = NonNegativeInteger
_MatInvLineFreq_Object = MibTableColumn
matInvLineFreq = _MatInvLineFreq_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 15),
    _MatInvLineFreq_Type()
)
matInvLineFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matInvLineFreq.setStatus("mandatory")


class _MatInvMbsPosition_Type(Integer32):
    """Custom type matInvMbsPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("transfer", 1),
          ("normal", 2),
          ("bypass", 3),
          ("invalid", 4))
    )


_MatInvMbsPosition_Type.__name__ = "Integer32"
_MatInvMbsPosition_Object = MibTableColumn
matInvMbsPosition = _MatInvMbsPosition_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 16),
    _MatInvMbsPosition_Type()
)
matInvMbsPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matInvMbsPosition.setStatus("mandatory")


class _MatInvRunMode_Type(Integer32):
    """Custom type matInvRunMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("powerOn", 1),
          ("standby", 2),
          ("bypass", 3),
          ("line", 4),
          ("battery", 5),
          ("fault", 6))
    )


_MatInvRunMode_Type.__name__ = "Integer32"
_MatInvRunMode_Object = MibTableColumn
matInvRunMode = _MatInvRunMode_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 17),
    _MatInvRunMode_Type()
)
matInvRunMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matInvRunMode.setStatus("mandatory")


class _MatInvPriority_Type(Integer32):
    """Custom type matInvPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("batteryMode", 1),
          ("lineMode", 2))
    )


_MatInvPriority_Type.__name__ = "Integer32"
_MatInvPriority_Object = MibTableColumn
matInvPriority = _MatInvPriority_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 18),
    _MatInvPriority_Type()
)
matInvPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matInvPriority.setStatus("mandatory")
_MatConfInvOutputVoltage_Type = NonNegativeInteger
_MatConfInvOutputVoltage_Object = MibTableColumn
matConfInvOutputVoltage = _MatConfInvOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 19),
    _MatConfInvOutputVoltage_Type()
)
matConfInvOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matConfInvOutputVoltage.setStatus("mandatory")
_MatConfInvInputVoltage_Type = NonNegativeInteger
_MatConfInvInputVoltage_Object = MibTableColumn
matConfInvInputVoltage = _MatConfInvInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 20),
    _MatConfInvInputVoltage_Type()
)
matConfInvInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matConfInvInputVoltage.setStatus("mandatory")
_MatConfInvOutputVoltHighLoss_Type = NonNegativeInteger
_MatConfInvOutputVoltHighLoss_Object = MibTableColumn
matConfInvOutputVoltHighLoss = _MatConfInvOutputVoltHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 21),
    _MatConfInvOutputVoltHighLoss_Type()
)
matConfInvOutputVoltHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matConfInvOutputVoltHighLoss.setStatus("mandatory")
_MatConfInvOutputVoltLowLoss_Type = NonNegativeInteger
_MatConfInvOutputVoltLowLoss_Object = MibTableColumn
matConfInvOutputVoltLowLoss = _MatConfInvOutputVoltLowLoss_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 22),
    _MatConfInvOutputVoltLowLoss_Type()
)
matConfInvOutputVoltLowLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matConfInvOutputVoltLowLoss.setStatus("mandatory")
_MatConfInvOutputPower_Type = NonNegativeInteger
_MatConfInvOutputPower_Object = MibTableColumn
matConfInvOutputPower = _MatConfInvOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 23),
    _MatConfInvOutputPower_Type()
)
matConfInvOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matConfInvOutputPower.setStatus("mandatory")
_MatConfInvOutputFreq_Type = NonNegativeInteger
_MatConfInvOutputFreq_Object = MibTableColumn
matConfInvOutputFreq = _MatConfInvOutputFreq_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 24),
    _MatConfInvOutputFreq_Type()
)
matConfInvOutputFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matConfInvOutputFreq.setStatus("mandatory")


class _MatInvPhaseType_Type(Integer32):
    """Custom type matInvPhaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("singlePhase", 1),
          ("threePhase", 2))
    )


_MatInvPhaseType_Type.__name__ = "Integer32"
_MatInvPhaseType_Object = MibTableColumn
matInvPhaseType = _MatInvPhaseType_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 25),
    _MatInvPhaseType_Type()
)
matInvPhaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matInvPhaseType.setStatus("mandatory")


class _MatInvOnOffStatus_Type(Integer32):
    """Custom type matInvOnOffStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 1),
          ("start", 2))
    )


_MatInvOnOffStatus_Type.__name__ = "Integer32"
_MatInvOnOffStatus_Object = MibTableColumn
matInvOnOffStatus = _MatInvOnOffStatus_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 2, 2, 1, 26),
    _MatInvOnOffStatus_Type()
)
matInvOnOffStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matInvOnOffStatus.setStatus("mandatory")
_MatSts_ObjectIdentity = ObjectIdentity
matSts = _MatSts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3)
)
_MatStsModuleNum_Type = Integer32
_MatStsModuleNum_Object = MibScalar
matStsModuleNum = _MatStsModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 1),
    _MatStsModuleNum_Type()
)
matStsModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsModuleNum.setStatus("mandatory")
_MatStsTable_Object = MibTable
matStsTable = _MatStsTable_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    matStsTable.setStatus("mandatory")
_MatStsEntry_Object = MibTableRow
matStsEntry = _MatStsEntry_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1)
)
matStsEntry.setIndexNames(
    (0, "TELECOM-MIB", "matStsModuleIndex"),
)
if mibBuilder.loadTexts:
    matStsEntry.setStatus("mandatory")
_MatStsModuleIndex_Type = PositiveInteger
_MatStsModuleIndex_Object = MibTableColumn
matStsModuleIndex = _MatStsModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 1),
    _MatStsModuleIndex_Type()
)
matStsModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    matStsModuleIndex.setStatus("mandatory")


class _MatStsModuleType_Type(DisplayString):
    """Custom type matStsModuleType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_MatStsModuleType_Type.__name__ = "DisplayString"
_MatStsModuleType_Object = MibTableColumn
matStsModuleType = _MatStsModuleType_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 2),
    _MatStsModuleType_Type()
)
matStsModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsModuleType.setStatus("mandatory")


class _MatStsSerialNum_Type(DisplayString):
    """Custom type matStsSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MatStsSerialNum_Type.__name__ = "DisplayString"
_MatStsSerialNum_Object = MibTableColumn
matStsSerialNum = _MatStsSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 3),
    _MatStsSerialNum_Type()
)
matStsSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsSerialNum.setStatus("mandatory")


class _MatStsFirmwareVersion_Type(DisplayString):
    """Custom type matStsFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_MatStsFirmwareVersion_Type.__name__ = "DisplayString"
_MatStsFirmwareVersion_Object = MibTableColumn
matStsFirmwareVersion = _MatStsFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 4),
    _MatStsFirmwareVersion_Type()
)
matStsFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsFirmwareVersion.setStatus("mandatory")


class _MatStsHardwareVersion_Type(DisplayString):
    """Custom type matStsHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_MatStsHardwareVersion_Type.__name__ = "DisplayString"
_MatStsHardwareVersion_Object = MibTableColumn
matStsHardwareVersion = _MatStsHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 5),
    _MatStsHardwareVersion_Type()
)
matStsHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsHardwareVersion.setStatus("mandatory")


class _MatStsWarningState_Type(DisplayString):
    """Custom type matStsWarningState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MatStsWarningState_Type.__name__ = "DisplayString"
_MatStsWarningState_Object = MibTableColumn
matStsWarningState = _MatStsWarningState_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 6),
    _MatStsWarningState_Type()
)
matStsWarningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsWarningState.setStatus("mandatory")
_MatStsMainInputVoltage_Type = NonNegativeInteger
_MatStsMainInputVoltage_Object = MibTableColumn
matStsMainInputVoltage = _MatStsMainInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 7),
    _MatStsMainInputVoltage_Type()
)
matStsMainInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsMainInputVoltage.setStatus("mandatory")
_MatStsMainInputFreq_Type = NonNegativeInteger
_MatStsMainInputFreq_Object = MibTableColumn
matStsMainInputFreq = _MatStsMainInputFreq_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 8),
    _MatStsMainInputFreq_Type()
)
matStsMainInputFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsMainInputFreq.setStatus("mandatory")
_MatStsInvInputVoltage_Type = NonNegativeInteger
_MatStsInvInputVoltage_Object = MibTableColumn
matStsInvInputVoltage = _MatStsInvInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 9),
    _MatStsInvInputVoltage_Type()
)
matStsInvInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsInvInputVoltage.setStatus("mandatory")
_MatStsInvInputFreq_Type = NonNegativeInteger
_MatStsInvInputFreq_Object = MibTableColumn
matStsInvInputFreq = _MatStsInvInputFreq_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 10),
    _MatStsInvInputFreq_Type()
)
matStsInvInputFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsInvInputFreq.setStatus("mandatory")
_MatStsOutputVoltage_Type = NonNegativeInteger
_MatStsOutputVoltage_Object = MibTableColumn
matStsOutputVoltage = _MatStsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 11),
    _MatStsOutputVoltage_Type()
)
matStsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsOutputVoltage.setStatus("mandatory")
_MatStsOutputCurrent_Type = NonNegativeInteger
_MatStsOutputCurrent_Object = MibTableColumn
matStsOutputCurrent = _MatStsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 12),
    _MatStsOutputCurrent_Type()
)
matStsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsOutputCurrent.setStatus("mandatory")
_MatStsOutputPower_Type = NonNegativeInteger
_MatStsOutputPower_Object = MibTableColumn
matStsOutputPower = _MatStsOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 13),
    _MatStsOutputPower_Type()
)
matStsOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsOutputPower.setStatus("mandatory")
_MatStsOutputFreq_Type = NonNegativeInteger
_MatStsOutputFreq_Object = MibTableColumn
matStsOutputFreq = _MatStsOutputFreq_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 14),
    _MatStsOutputFreq_Type()
)
matStsOutputFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsOutputFreq.setStatus("mandatory")
_MatStsRuntime_Type = NonNegativeInteger
_MatStsRuntime_Object = MibTableColumn
matStsRuntime = _MatStsRuntime_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 15),
    _MatStsRuntime_Type()
)
matStsRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsRuntime.setStatus("mandatory")
_MatStsTemperature_Type = Integer32
_MatStsTemperature_Object = MibTableColumn
matStsTemperature = _MatStsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 16),
    _MatStsTemperature_Type()
)
matStsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsTemperature.setStatus("mandatory")


class _MatStsMbsStatus_Type(Integer32):
    """Custom type matStsMbsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("normalPosition", 1),
          ("issPosition", 2),
          ("ibpPosition", 3),
          ("mssPosition", 4),
          ("mbpPosition", 5),
          ("mbsError", 6))
    )


_MatStsMbsStatus_Type.__name__ = "Integer32"
_MatStsMbsStatus_Object = MibTableColumn
matStsMbsStatus = _MatStsMbsStatus_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 17),
    _MatStsMbsStatus_Type()
)
matStsMbsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsMbsStatus.setStatus("mandatory")


class _MatStsStatus_Type(Integer32):
    """Custom type matStsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onLine", 1),
          ("offLine", 2))
    )


_MatStsStatus_Type.__name__ = "Integer32"
_MatStsStatus_Object = MibTableColumn
matStsStatus = _MatStsStatus_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 18),
    _MatStsStatus_Type()
)
matStsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsStatus.setStatus("mandatory")


class _MatStsRunningMode_Type(Integer32):
    """Custom type matStsRunningMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inverter", 1),
          ("mains", 2),
          ("noOutput", 3))
    )


_MatStsRunningMode_Type.__name__ = "Integer32"
_MatStsRunningMode_Object = MibTableColumn
matStsRunningMode = _MatStsRunningMode_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 19),
    _MatStsRunningMode_Type()
)
matStsRunningMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsRunningMode.setStatus("mandatory")
_MatStsMainHighLossVoltage_Type = NonNegativeInteger
_MatStsMainHighLossVoltage_Object = MibTableColumn
matStsMainHighLossVoltage = _MatStsMainHighLossVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 20),
    _MatStsMainHighLossVoltage_Type()
)
matStsMainHighLossVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsMainHighLossVoltage.setStatus("mandatory")
_MatStsMainLowLossVoltage_Type = NonNegativeInteger
_MatStsMainLowLossVoltage_Object = MibTableColumn
matStsMainLowLossVoltage = _MatStsMainLowLossVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 21),
    _MatStsMainLowLossVoltage_Type()
)
matStsMainLowLossVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsMainLowLossVoltage.setStatus("mandatory")
_MatStsInvHighLossVoltage_Type = NonNegativeInteger
_MatStsInvHighLossVoltage_Object = MibTableColumn
matStsInvHighLossVoltage = _MatStsInvHighLossVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 22),
    _MatStsInvHighLossVoltage_Type()
)
matStsInvHighLossVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsInvHighLossVoltage.setStatus("mandatory")
_MatStsInvLosLossVoltage_Type = NonNegativeInteger
_MatStsInvLosLossVoltage_Object = MibTableColumn
matStsInvLosLossVoltage = _MatStsInvLosLossVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 3, 2, 1, 23),
    _MatStsInvLosLossVoltage_Type()
)
matStsInvLosLossVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matStsInvLosLossVoltage.setStatus("mandatory")
_MatDryContact_ObjectIdentity = ObjectIdentity
matDryContact = _MatDryContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 4)
)
_MatDryContactNum_Type = Integer32
_MatDryContactNum_Object = MibScalar
matDryContactNum = _MatDryContactNum_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 4, 1),
    _MatDryContactNum_Type()
)
matDryContactNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matDryContactNum.setStatus("mandatory")
_MatDryContactTable_Object = MibTable
matDryContactTable = _MatDryContactTable_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    matDryContactTable.setStatus("mandatory")
_MatDryContactEntry_Object = MibTableRow
matDryContactEntry = _MatDryContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 4, 2, 1)
)
matDryContactEntry.setIndexNames(
    (0, "TELECOM-MIB", "matDryContactIndex"),
)
if mibBuilder.loadTexts:
    matDryContactEntry.setStatus("mandatory")
_MatDryContactIndex_Type = PositiveInteger
_MatDryContactIndex_Object = MibTableColumn
matDryContactIndex = _MatDryContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 4, 2, 1, 1),
    _MatDryContactIndex_Type()
)
matDryContactIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    matDryContactIndex.setStatus("mandatory")


class _MatDryContactString_Type(DisplayString):
    """Custom type matDryContactString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_MatDryContactString_Type.__name__ = "DisplayString"
_MatDryContactString_Object = MibTableColumn
matDryContactString = _MatDryContactString_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 4, 2, 1, 2),
    _MatDryContactString_Type()
)
matDryContactString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matDryContactString.setStatus("mandatory")
_MatConfig_ObjectIdentity = ObjectIdentity
matConfig = _MatConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 5)
)
_MatConfInvSysOutputFreq_Type = NonNegativeInteger
_MatConfInvSysOutputFreq_Object = MibScalar
matConfInvSysOutputFreq = _MatConfInvSysOutputFreq_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 5, 1),
    _MatConfInvSysOutputFreq_Type()
)
matConfInvSysOutputFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matConfInvSysOutputFreq.setStatus("mandatory")
_MatConfInvSysOutputVolt_Type = NonNegativeInteger
_MatConfInvSysOutputVolt_Object = MibScalar
matConfInvSysOutputVolt = _MatConfInvSysOutputVolt_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 5, 2),
    _MatConfInvSysOutputVolt_Type()
)
matConfInvSysOutputVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matConfInvSysOutputVolt.setStatus("mandatory")
_MatConfInvSysOutputVoltHighLoss_Type = NonNegativeInteger
_MatConfInvSysOutputVoltHighLoss_Object = MibScalar
matConfInvSysOutputVoltHighLoss = _MatConfInvSysOutputVoltHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 5, 3),
    _MatConfInvSysOutputVoltHighLoss_Type()
)
matConfInvSysOutputVoltHighLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matConfInvSysOutputVoltHighLoss.setStatus("mandatory")
_MatConfInvSysOutputVoltLowLoss_Type = NonNegativeInteger
_MatConfInvSysOutputVoltLowLoss_Object = MibScalar
matConfInvSysOutputVoltLowLoss = _MatConfInvSysOutputVoltLowLoss_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 5, 4),
    _MatConfInvSysOutputVoltLowLoss_Type()
)
matConfInvSysOutputVoltLowLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matConfInvSysOutputVoltLowLoss.setStatus("mandatory")
_MatConfInvSysInputVolt_Type = NonNegativeInteger
_MatConfInvSysInputVolt_Object = MibScalar
matConfInvSysInputVolt = _MatConfInvSysInputVolt_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 5, 5),
    _MatConfInvSysInputVolt_Type()
)
matConfInvSysInputVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matConfInvSysInputVolt.setStatus("mandatory")
_MatConfInvSysPowerLimit_Type = NonNegativeInteger
_MatConfInvSysPowerLimit_Object = MibScalar
matConfInvSysPowerLimit = _MatConfInvSysPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 5, 6),
    _MatConfInvSysPowerLimit_Type()
)
matConfInvSysPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matConfInvSysPowerLimit.setStatus("mandatory")
_MatConfInvSysLineVoltHighLoss_Type = NonNegativeInteger
_MatConfInvSysLineVoltHighLoss_Object = MibScalar
matConfInvSysLineVoltHighLoss = _MatConfInvSysLineVoltHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 5, 7),
    _MatConfInvSysLineVoltHighLoss_Type()
)
matConfInvSysLineVoltHighLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matConfInvSysLineVoltHighLoss.setStatus("mandatory")
_MatConfInvSysLineVoltLowLoss_Type = NonNegativeInteger
_MatConfInvSysLineVoltLowLoss_Object = MibScalar
matConfInvSysLineVoltLowLoss = _MatConfInvSysLineVoltLowLoss_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 5, 8),
    _MatConfInvSysLineVoltLowLoss_Type()
)
matConfInvSysLineVoltLowLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matConfInvSysLineVoltLowLoss.setStatus("mandatory")


class _MatConfInvSysPriority_Type(Integer32):
    """Custom type matConfInvSysPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("batteryMode", 1),
          ("lineMode", 2))
    )


_MatConfInvSysPriority_Type.__name__ = "Integer32"
_MatConfInvSysPriority_Object = MibScalar
matConfInvSysPriority = _MatConfInvSysPriority_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 5, 9),
    _MatConfInvSysPriority_Type()
)
matConfInvSysPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matConfInvSysPriority.setStatus("mandatory")


class _MatConfInvSysFanSpeed_Type(Integer32):
    """Custom type matConfInvSysFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalSpeed", 1),
          ("fullSpeed", 2))
    )


_MatConfInvSysFanSpeed_Type.__name__ = "Integer32"
_MatConfInvSysFanSpeed_Object = MibScalar
matConfInvSysFanSpeed = _MatConfInvSysFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 5, 10),
    _MatConfInvSysFanSpeed_Type()
)
matConfInvSysFanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matConfInvSysFanSpeed.setStatus("mandatory")
_MatConfStsAcVoltHighLoss_Type = NonNegativeInteger
_MatConfStsAcVoltHighLoss_Object = MibScalar
matConfStsAcVoltHighLoss = _MatConfStsAcVoltHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 5, 11),
    _MatConfStsAcVoltHighLoss_Type()
)
matConfStsAcVoltHighLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matConfStsAcVoltHighLoss.setStatus("mandatory")
_MatConfStsAcVoltLowLoss_Type = NonNegativeInteger
_MatConfStsAcVoltLowLoss_Object = MibScalar
matConfStsAcVoltLowLoss = _MatConfStsAcVoltLowLoss_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 5, 12),
    _MatConfStsAcVoltLowLoss_Type()
)
matConfStsAcVoltLowLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matConfStsAcVoltLowLoss.setStatus("mandatory")
_MatConfStsIpvVoltHighLoss_Type = NonNegativeInteger
_MatConfStsIpvVoltHighLoss_Object = MibScalar
matConfStsIpvVoltHighLoss = _MatConfStsIpvVoltHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 5, 13),
    _MatConfStsIpvVoltHighLoss_Type()
)
matConfStsIpvVoltHighLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matConfStsIpvVoltHighLoss.setStatus("mandatory")
_MatConfStsIpvVoltLowLoss_Type = NonNegativeInteger
_MatConfStsIpvVoltLowLoss_Object = MibScalar
matConfStsIpvVoltLowLoss = _MatConfStsIpvVoltLowLoss_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 5, 14),
    _MatConfStsIpvVoltLowLoss_Type()
)
matConfStsIpvVoltLowLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matConfStsIpvVoltLowLoss.setStatus("mandatory")


class _MatConfStsPriority_Type(Integer32):
    """Custom type matConfStsPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onLine", 1),
          ("offLine", 2))
    )


_MatConfStsPriority_Type.__name__ = "Integer32"
_MatConfStsPriority_Object = MibScalar
matConfStsPriority = _MatConfStsPriority_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 5, 15),
    _MatConfStsPriority_Type()
)
matConfStsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matConfStsPriority.setStatus("mandatory")


class _MatConfStsFanSpeed_Type(Integer32):
    """Custom type matConfStsFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalSpeed", 1),
          ("fullSpeed", 2))
    )


_MatConfStsFanSpeed_Type.__name__ = "Integer32"
_MatConfStsFanSpeed_Object = MibScalar
matConfStsFanSpeed = _MatConfStsFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 5, 16),
    _MatConfStsFanSpeed_Type()
)
matConfStsFanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matConfStsFanSpeed.setStatus("mandatory")
_MatTrapTargets_ObjectIdentity = ObjectIdentity
matTrapTargets = _MatTrapTargets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 6)
)
_MatTrapTargetsNum_Type = Integer32
_MatTrapTargetsNum_Object = MibScalar
matTrapTargetsNum = _MatTrapTargetsNum_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 6, 1),
    _MatTrapTargetsNum_Type()
)
matTrapTargetsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matTrapTargetsNum.setStatus("mandatory")
_MatTrapTargetsTable_Object = MibTable
matTrapTargetsTable = _MatTrapTargetsTable_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    matTrapTargetsTable.setStatus("mandatory")
_MatTrapTargetsEntry_Object = MibTableRow
matTrapTargetsEntry = _MatTrapTargetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 6, 2, 1)
)
matTrapTargetsEntry.setIndexNames(
    (0, "TELECOM-MIB", "matTrapTargetsIndex"),
)
if mibBuilder.loadTexts:
    matTrapTargetsEntry.setStatus("mandatory")
_MatTrapTargetsIndex_Type = PositiveInteger
_MatTrapTargetsIndex_Object = MibTableColumn
matTrapTargetsIndex = _MatTrapTargetsIndex_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 6, 2, 1, 1),
    _MatTrapTargetsIndex_Type()
)
matTrapTargetsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    matTrapTargetsIndex.setStatus("mandatory")


class _MatTrapTargetsAddress_Type(DisplayString):
    """Custom type matTrapTargetsAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_MatTrapTargetsAddress_Type.__name__ = "DisplayString"
_MatTrapTargetsAddress_Object = MibTableColumn
matTrapTargetsAddress = _MatTrapTargetsAddress_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 6, 2, 1, 2),
    _MatTrapTargetsAddress_Type()
)
matTrapTargetsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matTrapTargetsAddress.setStatus("mandatory")


class _MatTrapTargetsCommunity_Type(DisplayString):
    """Custom type matTrapTargetsCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MatTrapTargetsCommunity_Type.__name__ = "DisplayString"
_MatTrapTargetsCommunity_Object = MibTableColumn
matTrapTargetsCommunity = _MatTrapTargetsCommunity_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 6, 2, 1, 3),
    _MatTrapTargetsCommunity_Type()
)
matTrapTargetsCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matTrapTargetsCommunity.setStatus("mandatory")


class _MatTrapType_Type(Integer32):
    """Custom type matTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("matTrap", 2))
    )


_MatTrapType_Type.__name__ = "Integer32"
_MatTrapType_Object = MibTableColumn
matTrapType = _MatTrapType_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 6, 2, 1, 4),
    _MatTrapType_Type()
)
matTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matTrapType.setStatus("mandatory")


class _MatTrapSeverityLevel_Type(Integer32):
    """Custom type matTrapSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("observe", 1),
          ("major", 2),
          ("critical", 3))
    )


_MatTrapSeverityLevel_Type.__name__ = "Integer32"
_MatTrapSeverityLevel_Object = MibTableColumn
matTrapSeverityLevel = _MatTrapSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 6, 2, 1, 5),
    _MatTrapSeverityLevel_Type()
)
matTrapSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matTrapSeverityLevel.setStatus("mandatory")


class _MatTrapTargetsDesc_Type(DisplayString):
    """Custom type matTrapTargetsDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MatTrapTargetsDesc_Type.__name__ = "DisplayString"
_MatTrapTargetsDesc_Object = MibTableColumn
matTrapTargetsDesc = _MatTrapTargetsDesc_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 1, 6, 2, 1, 6),
    _MatTrapTargetsDesc_Type()
)
matTrapTargetsDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matTrapTargetsDesc.setStatus("mandatory")
_MatTraps_ObjectIdentity = ObjectIdentity
matTraps = _MatTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2)
)

# Managed Objects groups


# Notification objects

matInvFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 1)
)
matInvFault.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvFault.setStatus(
        ""
    )

matReturnFromInvFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 2)
)
matReturnFromInvFault.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvFault.setStatus(
        ""
    )

matInvOverLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 3)
)
matInvOverLoad.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvOverLoad.setStatus(
        ""
    )

matReturnFromInvOverLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 4)
)
matReturnFromInvOverLoad.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvOverLoad.setStatus(
        ""
    )

matInvFanFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 5)
)
matInvFanFault.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvFanFault.setStatus(
        ""
    )

matReturnFromInvFanFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 6)
)
matReturnFromInvFanFault.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvFanFault.setStatus(
        ""
    )

matInvTempPowerLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 7)
)
matInvTempPowerLimit.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvTempPowerLimit.setStatus(
        ""
    )

matReturnFromInvTempPowerLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 8)
)
matReturnFromInvTempPowerLimit.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvTempPowerLimit.setStatus(
        ""
    )

matInvInputAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 9)
)
matInvInputAbnormal.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvInputAbnormal.setStatus(
        ""
    )

matReturnFromInvInputAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 10)
)
matReturnFromInvInputAbnormal.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvInputAbnormal.setStatus(
        ""
    )

matInvLowInputShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 11)
)
matInvLowInputShutdown.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvLowInputShutdown.setStatus(
        ""
    )

matReturnFromInvLowInputShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 12)
)
matReturnFromInvLowInputShutdown.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvLowInputShutdown.setStatus(
        ""
    )

matInvNotRespond = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 13)
)
matInvNotRespond.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvNotRespond.setStatus(
        ""
    )

matReturnFromInvNotRespond = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 14)
)
matReturnFromInvNotRespond.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvNotRespond.setStatus(
        ""
    )

matInvBusVoltageOverLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 15)
)
matInvBusVoltageOverLimit.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvBusVoltageOverLimit.setStatus(
        ""
    )

matReturnFromInvBusVoltOverLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 16)
)
matReturnFromInvBusVoltOverLimit.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvBusVoltOverLimit.setStatus(
        ""
    )

matInvBusVoltageUnderLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 17)
)
matInvBusVoltageUnderLimit.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvBusVoltageUnderLimit.setStatus(
        ""
    )

matReturnFromInvBusVoltUnderLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 18)
)
matReturnFromInvBusVoltUnderLimit.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvBusVoltUnderLimit.setStatus(
        ""
    )

matInvBusSoftFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 19)
)
matInvBusSoftFail.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvBusSoftFail.setStatus(
        ""
    )

matReturnFromInvBusSoftFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 20)
)
matReturnFromInvBusSoftFail.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvBusSoftFail.setStatus(
        ""
    )

matInvOutputShort = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 21)
)
matInvOutputShort.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvOutputShort.setStatus(
        ""
    )

matReturnFromInvOutputShort = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 22)
)
matReturnFromInvOutputShort.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvOutputShort.setStatus(
        ""
    )

matInvOutputVoltLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 23)
)
matInvOutputVoltLow.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvOutputVoltLow.setStatus(
        ""
    )

matReturnFromInvOutputVoltLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 24)
)
matReturnFromInvOutputVoltLow.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvOutputVoltLow.setStatus(
        ""
    )

matInvOutputVoltHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 25)
)
matInvOutputVoltHigh.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvOutputVoltHigh.setStatus(
        ""
    )

matReturnFromInvOutputVoltHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 26)
)
matReturnFromInvOutputVoltHigh.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvOutputVoltHigh.setStatus(
        ""
    )

matInvTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 27)
)
matInvTemperatureHigh.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvTemperatureHigh.setStatus(
        ""
    )

matReturnFromInvTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 28)
)
matReturnFromInvTemperatureHigh.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvTemperatureHigh.setStatus(
        ""
    )

matInvNegativePowerProtect = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 29)
)
matInvNegativePowerProtect.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvNegativePowerProtect.setStatus(
        ""
    )

matReturnFromInvNegativePowerProtect = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 30)
)
matReturnFromInvNegativePowerProtect.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvNegativePowerProtect.setStatus(
        ""
    )

matInvPulseFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 31)
)
matInvPulseFault.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvPulseFault.setStatus(
        ""
    )

matReturnFromInvPulseFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 32)
)
if mibBuilder.loadTexts:
    matReturnFromInvPulseFault.setStatus(
        ""
    )

matInvEPOShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 33)
)
matInvEPOShutdown.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvEPOShutdown.setStatus(
        ""
    )

matReturnFromInvEPOShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 34)
)
matReturnFromInvEPOShutdown.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvEPOShutdown.setStatus(
        ""
    )

matInvSoftStartFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 35)
)
matInvSoftStartFail.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvSoftStartFail.setStatus(
        ""
    )

matReturnFromInvSoftStartFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 36)
)
matReturnFromInvSoftStartFail.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvSoftStartFail.setStatus(
        ""
    )

matInvEEPROMFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 37)
)
matInvEEPROMFault.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvEEPROMFault.setStatus(
        ""
    )

matReturnFromInvEEPROMFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 38)
)
matReturnFromInvEEPROMFault.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvEEPROMFault.setStatus(
        ""
    )

matInvBypassSCRShort = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 39)
)
matInvBypassSCRShort.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvBypassSCRShort.setStatus(
        ""
    )

matReturnFromInvBypassSCRShort = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 40)
)
matReturnFromInvBypassSCRShort.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvBypassSCRShort.setStatus(
        ""
    )

matInvMBSPosError = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 41)
)
matInvMBSPosError.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvMBSPosError.setStatus(
        ""
    )

matReturnFromInvMBSPosError = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 42)
)
matReturnFromInvMBSPosError.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvMBSPosError.setStatus(
        ""
    )

matInvBackfeedRelayOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 43)
)
matInvBackfeedRelayOpen.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvBackfeedRelayOpen.setStatus(
        ""
    )

matReturnFromInvBackfeedRelayOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 44)
)
matReturnFromInvBackfeedRelayOpen.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvBackfeedRelayOpen.setStatus(
        ""
    )

matInvHardwareError = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 45)
)
matInvHardwareError.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvHardwareError.setStatus(
        ""
    )

matReturnFromInvHardwareError = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 46)
)
matReturnFromInvHardwareError.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvHardwareError.setStatus(
        ""
    )

matInvMainUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 47)
)
matInvMainUnavailable.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvMainUnavailable.setStatus(
        ""
    )

matReturnFromInvMainUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 48)
)
matReturnFromInvMainUnavailable.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvMainUnavailable.setStatus(
        ""
    )

matInvMaintenaceBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 49)
)
matInvMaintenaceBypass.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matInvMaintenaceBypass.setStatus(
        ""
    )

matReturnFromInvMaintenaceBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 50)
)
matReturnFromInvMaintenaceBypass.setObjects(
    ("TELECOM-MIB", "matInvSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromInvMaintenaceBypass.setStatus(
        ""
    )

matStsBypassUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 51)
)
matStsBypassUnavailable.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matStsBypassUnavailable.setStatus(
        ""
    )

matReturnFromStsBypassUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 52)
)
matReturnFromStsBypassUnavailable.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromStsBypassUnavailable.setStatus(
        ""
    )

matStsBackfeedRelayOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 53)
)
matStsBackfeedRelayOpen.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matStsBackfeedRelayOpen.setStatus(
        ""
    )

matReturnFromStsBackfeedRelayOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 54)
)
matReturnFromStsBackfeedRelayOpen.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromStsBackfeedRelayOpen.setStatus(
        ""
    )

matStsScr1ShortCurcuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 55)
)
matStsScr1ShortCurcuit.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matStsScr1ShortCurcuit.setStatus(
        ""
    )

matReturnFromStsScr1ShortCurcuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 56)
)
matReturnFromStsScr1ShortCurcuit.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromStsScr1ShortCurcuit.setStatus(
        ""
    )

matStsScr2ShortCurcuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 57)
)
matStsScr2ShortCurcuit.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matStsScr2ShortCurcuit.setStatus(
        ""
    )

matReturnFromStsScr2ShortCurcuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 58)
)
matReturnFromStsScr2ShortCurcuit.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromStsScr2ShortCurcuit.setStatus(
        ""
    )

matStsFaultMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 59)
)
matStsFaultMode.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matStsFaultMode.setStatus(
        ""
    )

matReturnFromStsFaultMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 60)
)
matReturnFromStsFaultMode.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromStsFaultMode.setStatus(
        ""
    )

matStsFanFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 61)
)
matStsFanFault.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matStsFanFault.setStatus(
        ""
    )

matReturnFromStsFanFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 62)
)
matReturnFromStsFanFault.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromStsFanFault.setStatus(
        ""
    )

matStsEEPROMFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 63)
)
matStsEEPROMFault.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matStsEEPROMFault.setStatus(
        ""
    )

matReturnFromStsEEPROMFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 64)
)
matReturnFromStsEEPROMFault.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromStsEEPROMFault.setStatus(
        ""
    )

matStsInvFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 65)
)
matStsInvFail.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matStsInvFail.setStatus(
        ""
    )

matReturnFromStsInvFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 66)
)
matReturnFromStsInvFail.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromStsInvFail.setStatus(
        ""
    )

matStsMainsFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 67)
)
matStsMainsFail.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matStsMainsFail.setStatus(
        ""
    )

matReturnFromStsMainFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 68)
)
matReturnFromStsMainFail.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromStsMainFail.setStatus(
        ""
    )

matStsOverLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 69)
)
matStsOverLoad.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matStsOverLoad.setStatus(
        ""
    )

matReturnFromStsOverLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 70)
)
matReturnFromStsOverLoad.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromStsOverLoad.setStatus(
        ""
    )

matStsOutputShortCircuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 71)
)
matStsOutputShortCircuit.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matStsOutputShortCircuit.setStatus(
        ""
    )

matReturnFromStsOutputShortCircuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 72)
)
matReturnFromStsOutputShortCircuit.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromStsOutputShortCircuit.setStatus(
        ""
    )

matStsInvBypassMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 73)
)
matStsInvBypassMode.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matStsInvBypassMode.setStatus(
        ""
    )

matReturnFromStsInvBypassMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 74)
)
matReturnFromStsInvBypassMode.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromStsInvBypassMode.setStatus(
        ""
    )

matStsTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 75)
)
matStsTemperatureHigh.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matStsTemperatureHigh.setStatus(
        ""
    )

matReturnFromStsTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 76)
)
matReturnFromStsTemperatureHigh.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromStsTemperatureHigh.setStatus(
        ""
    )

matStsMBSPosFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 77)
)
matStsMBSPosFault.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matStsMBSPosFault.setStatus(
        ""
    )

matReturnFromStsMBSPosFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 78)
)
matReturnFromStsMBSPosFault.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromStsMBSPosFault.setStatus(
        ""
    )

matStsControlPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 79)
)
matStsControlPowerFail.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matStsControlPowerFail.setStatus(
        ""
    )

matReturnFromStsControlPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 80)
)
matReturnFromStsControlPowerFail.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromStsControlPowerFail.setStatus(
        ""
    )

matStsNotRespond = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 81)
)
matStsNotRespond.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matStsNotRespond.setStatus(
        ""
    )

matReturnFromStsNotRespond = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 82)
)
matReturnFromStsNotRespond.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromStsNotRespond.setStatus(
        ""
    )

matStsOutputAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 83)
)
matStsOutputAbnormal.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matStsOutputAbnormal.setStatus(
        ""
    )

matReturnFromStsOutputAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 84)
)
matReturnFromStsOutputAbnormal.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromStsOutputAbnormal.setStatus(
        ""
    )

matStsMaintenanceBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 85)
)
matStsMaintenanceBypass.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matStsMaintenanceBypass.setStatus(
        ""
    )

matReturnFromStsMaintenanceBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 86)
)
matReturnFromStsMaintenanceBypass.setObjects(
    ("TELECOM-MIB", "matStsSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromStsMaintenanceBypass.setStatus(
        ""
    )

matConBatteryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 87)
)
matConBatteryLow.setObjects(
    ("TELECOM-MIB", "matConSerialNum")
)
if mibBuilder.loadTexts:
    matConBatteryLow.setStatus(
        ""
    )

matReturnFromConBatteryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 88)
)
matReturnFromConBatteryLow.setObjects(
    ("TELECOM-MIB", "matConSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromConBatteryLow.setStatus(
        ""
    )

matConTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 89)
)
matConTemperatureHigh.setObjects(
    ("TELECOM-MIB", "matConSerialNum")
)
if mibBuilder.loadTexts:
    matConTemperatureHigh.setStatus(
        ""
    )

matReturnFromConTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 90)
)
matReturnFromConTemperatureHigh.setObjects(
    ("TELECOM-MIB", "matConSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromConTemperatureHigh.setStatus(
        ""
    )

matConEEPROMFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 91)
)
matConEEPROMFault.setObjects(
    ("TELECOM-MIB", "matConSerialNum")
)
if mibBuilder.loadTexts:
    matConEEPROMFault.setStatus(
        ""
    )

matReturnFromConEEPROMFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 92)
)
matReturnFromConEEPROMFault.setObjects(
    ("TELECOM-MIB", "matConSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromConEEPROMFault.setStatus(
        ""
    )

matConBatteryVoltHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 93)
)
matConBatteryVoltHigh.setObjects(
    ("TELECOM-MIB", "matConSerialNum")
)
if mibBuilder.loadTexts:
    matConBatteryVoltHigh.setStatus(
        ""
    )

matReturnFromConBatteryVoltHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 94)
)
matReturnFromConBatteryVoltHigh.setObjects(
    ("TELECOM-MIB", "matConSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromConBatteryVoltHigh.setStatus(
        ""
    )

matConCanBusOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 95)
)
matConCanBusOff.setObjects(
    ("TELECOM-MIB", "matConSerialNum")
)
if mibBuilder.loadTexts:
    matConCanBusOff.setStatus(
        ""
    )

matReturnFromConCanBusOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 96)
)
matReturnFromConCanBusOff.setObjects(
    ("TELECOM-MIB", "matConSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromConCanBusOff.setStatus(
        ""
    )

matConCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 97)
)
matConCommunicationLost.setObjects(
    ("TELECOM-MIB", "matConSerialNum")
)
if mibBuilder.loadTexts:
    matConCommunicationLost.setStatus(
        ""
    )

matReturnFromCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 2, 2, 0, 98)
)
matReturnFromCommunicationLost.setObjects(
    ("TELECOM-MIB", "matConSerialNum")
)
if mibBuilder.loadTexts:
    matReturnFromCommunicationLost.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TELECOM-MIB",
    **{"PositiveInteger": PositiveInteger,
       "NonNegativeInteger": NonNegativeInteger,
       "ppc": ppc,
       "device": device,
       "matAgent": matAgent,
       "matObjects": matObjects,
       "matController": matController,
       "matConSerialNum": matConSerialNum,
       "matConName": matConName,
       "matConWarningState": matConWarningState,
       "matConTemperature": matConTemperature,
       "matAgentSoftwareVerison": matAgentSoftwareVerison,
       "matInverter": matInverter,
       "matInvModuleNum": matInvModuleNum,
       "matInvTable": matInvTable,
       "matInvEntry": matInvEntry,
       "matInvModuleIndex": matInvModuleIndex,
       "matInvSerialNum": matInvSerialNum,
       "matInvFirmwareVersion": matInvFirmwareVersion,
       "matInvHardwareVersion": matInvHardwareVersion,
       "matInvWarningState": matInvWarningState,
       "matInvOutputVoltage": matInvOutputVoltage,
       "matInvOutputCurrent": matInvOutputCurrent,
       "matInvBatteryVoltage": matInvBatteryVoltage,
       "matInvOutputFreq": matInvOutputFreq,
       "matInvOutputPower": matInvOutputPower,
       "matInvPowerLimit": matInvPowerLimit,
       "matInvRunTime": matInvRunTime,
       "matInvTemperature": matInvTemperature,
       "matInvLineVoltage": matInvLineVoltage,
       "matInvLineFreq": matInvLineFreq,
       "matInvMbsPosition": matInvMbsPosition,
       "matInvRunMode": matInvRunMode,
       "matInvPriority": matInvPriority,
       "matConfInvOutputVoltage": matConfInvOutputVoltage,
       "matConfInvInputVoltage": matConfInvInputVoltage,
       "matConfInvOutputVoltHighLoss": matConfInvOutputVoltHighLoss,
       "matConfInvOutputVoltLowLoss": matConfInvOutputVoltLowLoss,
       "matConfInvOutputPower": matConfInvOutputPower,
       "matConfInvOutputFreq": matConfInvOutputFreq,
       "matInvPhaseType": matInvPhaseType,
       "matInvOnOffStatus": matInvOnOffStatus,
       "matSts": matSts,
       "matStsModuleNum": matStsModuleNum,
       "matStsTable": matStsTable,
       "matStsEntry": matStsEntry,
       "matStsModuleIndex": matStsModuleIndex,
       "matStsModuleType": matStsModuleType,
       "matStsSerialNum": matStsSerialNum,
       "matStsFirmwareVersion": matStsFirmwareVersion,
       "matStsHardwareVersion": matStsHardwareVersion,
       "matStsWarningState": matStsWarningState,
       "matStsMainInputVoltage": matStsMainInputVoltage,
       "matStsMainInputFreq": matStsMainInputFreq,
       "matStsInvInputVoltage": matStsInvInputVoltage,
       "matStsInvInputFreq": matStsInvInputFreq,
       "matStsOutputVoltage": matStsOutputVoltage,
       "matStsOutputCurrent": matStsOutputCurrent,
       "matStsOutputPower": matStsOutputPower,
       "matStsOutputFreq": matStsOutputFreq,
       "matStsRuntime": matStsRuntime,
       "matStsTemperature": matStsTemperature,
       "matStsMbsStatus": matStsMbsStatus,
       "matStsStatus": matStsStatus,
       "matStsRunningMode": matStsRunningMode,
       "matStsMainHighLossVoltage": matStsMainHighLossVoltage,
       "matStsMainLowLossVoltage": matStsMainLowLossVoltage,
       "matStsInvHighLossVoltage": matStsInvHighLossVoltage,
       "matStsInvLosLossVoltage": matStsInvLosLossVoltage,
       "matDryContact": matDryContact,
       "matDryContactNum": matDryContactNum,
       "matDryContactTable": matDryContactTable,
       "matDryContactEntry": matDryContactEntry,
       "matDryContactIndex": matDryContactIndex,
       "matDryContactString": matDryContactString,
       "matConfig": matConfig,
       "matConfInvSysOutputFreq": matConfInvSysOutputFreq,
       "matConfInvSysOutputVolt": matConfInvSysOutputVolt,
       "matConfInvSysOutputVoltHighLoss": matConfInvSysOutputVoltHighLoss,
       "matConfInvSysOutputVoltLowLoss": matConfInvSysOutputVoltLowLoss,
       "matConfInvSysInputVolt": matConfInvSysInputVolt,
       "matConfInvSysPowerLimit": matConfInvSysPowerLimit,
       "matConfInvSysLineVoltHighLoss": matConfInvSysLineVoltHighLoss,
       "matConfInvSysLineVoltLowLoss": matConfInvSysLineVoltLowLoss,
       "matConfInvSysPriority": matConfInvSysPriority,
       "matConfInvSysFanSpeed": matConfInvSysFanSpeed,
       "matConfStsAcVoltHighLoss": matConfStsAcVoltHighLoss,
       "matConfStsAcVoltLowLoss": matConfStsAcVoltLowLoss,
       "matConfStsIpvVoltHighLoss": matConfStsIpvVoltHighLoss,
       "matConfStsIpvVoltLowLoss": matConfStsIpvVoltLowLoss,
       "matConfStsPriority": matConfStsPriority,
       "matConfStsFanSpeed": matConfStsFanSpeed,
       "matTrapTargets": matTrapTargets,
       "matTrapTargetsNum": matTrapTargetsNum,
       "matTrapTargetsTable": matTrapTargetsTable,
       "matTrapTargetsEntry": matTrapTargetsEntry,
       "matTrapTargetsIndex": matTrapTargetsIndex,
       "matTrapTargetsAddress": matTrapTargetsAddress,
       "matTrapTargetsCommunity": matTrapTargetsCommunity,
       "matTrapType": matTrapType,
       "matTrapSeverityLevel": matTrapSeverityLevel,
       "matTrapTargetsDesc": matTrapTargetsDesc,
       "matTraps": matTraps,
       "matInvFault": matInvFault,
       "matReturnFromInvFault": matReturnFromInvFault,
       "matInvOverLoad": matInvOverLoad,
       "matReturnFromInvOverLoad": matReturnFromInvOverLoad,
       "matInvFanFault": matInvFanFault,
       "matReturnFromInvFanFault": matReturnFromInvFanFault,
       "matInvTempPowerLimit": matInvTempPowerLimit,
       "matReturnFromInvTempPowerLimit": matReturnFromInvTempPowerLimit,
       "matInvInputAbnormal": matInvInputAbnormal,
       "matReturnFromInvInputAbnormal": matReturnFromInvInputAbnormal,
       "matInvLowInputShutdown": matInvLowInputShutdown,
       "matReturnFromInvLowInputShutdown": matReturnFromInvLowInputShutdown,
       "matInvNotRespond": matInvNotRespond,
       "matReturnFromInvNotRespond": matReturnFromInvNotRespond,
       "matInvBusVoltageOverLimit": matInvBusVoltageOverLimit,
       "matReturnFromInvBusVoltOverLimit": matReturnFromInvBusVoltOverLimit,
       "matInvBusVoltageUnderLimit": matInvBusVoltageUnderLimit,
       "matReturnFromInvBusVoltUnderLimit": matReturnFromInvBusVoltUnderLimit,
       "matInvBusSoftFail": matInvBusSoftFail,
       "matReturnFromInvBusSoftFail": matReturnFromInvBusSoftFail,
       "matInvOutputShort": matInvOutputShort,
       "matReturnFromInvOutputShort": matReturnFromInvOutputShort,
       "matInvOutputVoltLow": matInvOutputVoltLow,
       "matReturnFromInvOutputVoltLow": matReturnFromInvOutputVoltLow,
       "matInvOutputVoltHigh": matInvOutputVoltHigh,
       "matReturnFromInvOutputVoltHigh": matReturnFromInvOutputVoltHigh,
       "matInvTemperatureHigh": matInvTemperatureHigh,
       "matReturnFromInvTemperatureHigh": matReturnFromInvTemperatureHigh,
       "matInvNegativePowerProtect": matInvNegativePowerProtect,
       "matReturnFromInvNegativePowerProtect": matReturnFromInvNegativePowerProtect,
       "matInvPulseFault": matInvPulseFault,
       "matReturnFromInvPulseFault": matReturnFromInvPulseFault,
       "matInvEPOShutdown": matInvEPOShutdown,
       "matReturnFromInvEPOShutdown": matReturnFromInvEPOShutdown,
       "matInvSoftStartFail": matInvSoftStartFail,
       "matReturnFromInvSoftStartFail": matReturnFromInvSoftStartFail,
       "matInvEEPROMFault": matInvEEPROMFault,
       "matReturnFromInvEEPROMFault": matReturnFromInvEEPROMFault,
       "matInvBypassSCRShort": matInvBypassSCRShort,
       "matReturnFromInvBypassSCRShort": matReturnFromInvBypassSCRShort,
       "matInvMBSPosError": matInvMBSPosError,
       "matReturnFromInvMBSPosError": matReturnFromInvMBSPosError,
       "matInvBackfeedRelayOpen": matInvBackfeedRelayOpen,
       "matReturnFromInvBackfeedRelayOpen": matReturnFromInvBackfeedRelayOpen,
       "matInvHardwareError": matInvHardwareError,
       "matReturnFromInvHardwareError": matReturnFromInvHardwareError,
       "matInvMainUnavailable": matInvMainUnavailable,
       "matReturnFromInvMainUnavailable": matReturnFromInvMainUnavailable,
       "matInvMaintenaceBypass": matInvMaintenaceBypass,
       "matReturnFromInvMaintenaceBypass": matReturnFromInvMaintenaceBypass,
       "matStsBypassUnavailable": matStsBypassUnavailable,
       "matReturnFromStsBypassUnavailable": matReturnFromStsBypassUnavailable,
       "matStsBackfeedRelayOpen": matStsBackfeedRelayOpen,
       "matReturnFromStsBackfeedRelayOpen": matReturnFromStsBackfeedRelayOpen,
       "matStsScr1ShortCurcuit": matStsScr1ShortCurcuit,
       "matReturnFromStsScr1ShortCurcuit": matReturnFromStsScr1ShortCurcuit,
       "matStsScr2ShortCurcuit": matStsScr2ShortCurcuit,
       "matReturnFromStsScr2ShortCurcuit": matReturnFromStsScr2ShortCurcuit,
       "matStsFaultMode": matStsFaultMode,
       "matReturnFromStsFaultMode": matReturnFromStsFaultMode,
       "matStsFanFault": matStsFanFault,
       "matReturnFromStsFanFault": matReturnFromStsFanFault,
       "matStsEEPROMFault": matStsEEPROMFault,
       "matReturnFromStsEEPROMFault": matReturnFromStsEEPROMFault,
       "matStsInvFail": matStsInvFail,
       "matReturnFromStsInvFail": matReturnFromStsInvFail,
       "matStsMainsFail": matStsMainsFail,
       "matReturnFromStsMainFail": matReturnFromStsMainFail,
       "matStsOverLoad": matStsOverLoad,
       "matReturnFromStsOverLoad": matReturnFromStsOverLoad,
       "matStsOutputShortCircuit": matStsOutputShortCircuit,
       "matReturnFromStsOutputShortCircuit": matReturnFromStsOutputShortCircuit,
       "matStsInvBypassMode": matStsInvBypassMode,
       "matReturnFromStsInvBypassMode": matReturnFromStsInvBypassMode,
       "matStsTemperatureHigh": matStsTemperatureHigh,
       "matReturnFromStsTemperatureHigh": matReturnFromStsTemperatureHigh,
       "matStsMBSPosFault": matStsMBSPosFault,
       "matReturnFromStsMBSPosFault": matReturnFromStsMBSPosFault,
       "matStsControlPowerFail": matStsControlPowerFail,
       "matReturnFromStsControlPowerFail": matReturnFromStsControlPowerFail,
       "matStsNotRespond": matStsNotRespond,
       "matReturnFromStsNotRespond": matReturnFromStsNotRespond,
       "matStsOutputAbnormal": matStsOutputAbnormal,
       "matReturnFromStsOutputAbnormal": matReturnFromStsOutputAbnormal,
       "matStsMaintenanceBypass": matStsMaintenanceBypass,
       "matReturnFromStsMaintenanceBypass": matReturnFromStsMaintenanceBypass,
       "matConBatteryLow": matConBatteryLow,
       "matReturnFromConBatteryLow": matReturnFromConBatteryLow,
       "matConTemperatureHigh": matConTemperatureHigh,
       "matReturnFromConTemperatureHigh": matReturnFromConTemperatureHigh,
       "matConEEPROMFault": matConEEPROMFault,
       "matReturnFromConEEPROMFault": matReturnFromConEEPROMFault,
       "matConBatteryVoltHigh": matConBatteryVoltHigh,
       "matReturnFromConBatteryVoltHigh": matReturnFromConBatteryVoltHigh,
       "matConCanBusOff": matConCanBusOff,
       "matReturnFromConCanBusOff": matReturnFromConCanBusOff,
       "matConCommunicationLost": matConCommunicationLost,
       "matReturnFromCommunicationLost": matReturnFromCommunicationLost}
)
