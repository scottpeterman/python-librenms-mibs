# SNMP MIB module (VIPTELA-HARDWARE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\viptela\VIPTELA-HARDWARE
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:02 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(viptela,) = mibBuilder.importSymbols(
    "VIPTELA-GLOBAL",
    "viptela")


# MODULE-IDENTITY

viptela_hardware = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3)
)
if mibBuilder.loadTexts:
    viptela_hardware.setRevisions(
        ("2020-07-01 00:00",
         "2020-02-24 00:00",
         "2019-11-15 00:00",
         "2019-08-15 00:00",
         "2018-11-01 00:00",
         "2018-08-20 00:00",
         "2018-06-25 00:00",
         "2018-04-25 00:00",
         "2018-03-15 00:00",
         "2018-01-16 00:00",
         "2017-11-01 00:00",
         "2017-08-01 00:00",
         "2017-05-25 00:00",
         "2017-04-06 00:00",
         "2017-02-15 00:00",
         "2017-02-06 00:00",
         "2016-11-16 00:00",
         "2016-10-25 00:00",
         "2016-10-24 00:00",
         "2016-08-10 00:00",
         "2016-08-01 00:00",
         "2016-06-09 00:00",
         "2016-04-22 00:00",
         "2016-03-15 00:00",
         "2016-01-30 00:00",
         "2015-12-28 00:00",
         "2015-12-01 00:00",
         "2015-10-31 00:00",
         "2015-09-27 00:00",
         "2015-09-01 00:00",
         "2015-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfdString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class HwSensorTypeEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("board", 0),
          ("cPU-Junction", 1),
          ("dRAM", 2),
          ("pIM", 3))
    )



class HwTypeEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("chassis", 1),
          ("cPU", 2),
          ("dRAM", 3),
          ("flash", 4),
          ("eMMC", 5),
          ("sDCard", 6),
          ("uSB", 7),
          ("pIM", 8),
          ("transceiver", 9),
          ("fanTray", 10),
          ("pEM", 11),
          ("nIM", 12))
    )



class ModuleStateEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 0),
          ("removed", 1))
    )



class FailureStateEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oK", 0),
          ("failed", 1))
    )



class HwPoeClassEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("class-1", 1),
          ("class-2", 2),
          ("class-3", 3),
          ("class-4", 4),
          ("reserved", 5),
          ("class-0", 6),
          ("over-current", 7))
    )



# MIB Managed Objects in the order of their OIDs

_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1)
)
_HardwareInventoryTable_Object = MibTable
hardwareInventoryTable = _HardwareInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hardwareInventoryTable.setStatus("current")
_HardwareInventoryEntry_Object = MibTableRow
hardwareInventoryEntry = _HardwareInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 1, 1)
)
hardwareInventoryEntry.setIndexNames(
    (0, "VIPTELA-HARDWARE", "hardwareInventoryHwType"),
    (0, "VIPTELA-HARDWARE", "hardwareInventoryHwDevIndex"),
)
if mibBuilder.loadTexts:
    hardwareInventoryEntry.setStatus("current")
_HardwareInventoryHwType_Type = HwTypeEnum
_HardwareInventoryHwType_Object = MibTableColumn
hardwareInventoryHwType = _HardwareInventoryHwType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 1, 1, 1),
    _HardwareInventoryHwType_Type()
)
hardwareInventoryHwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hardwareInventoryHwType.setStatus("current")
_HardwareInventoryHwDevIndex_Type = Unsigned32
_HardwareInventoryHwDevIndex_Object = MibTableColumn
hardwareInventoryHwDevIndex = _HardwareInventoryHwDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 1, 1, 2),
    _HardwareInventoryHwDevIndex_Type()
)
hardwareInventoryHwDevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hardwareInventoryHwDevIndex.setStatus("current")


class _HardwareInventoryVersion_Type(String):
    """Custom type hardwareInventoryVersion based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HardwareInventoryVersion_Type.__name__ = "String"
_HardwareInventoryVersion_Object = MibTableColumn
hardwareInventoryVersion = _HardwareInventoryVersion_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 1, 1, 3),
    _HardwareInventoryVersion_Type()
)
hardwareInventoryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareInventoryVersion.setStatus("current")


class _HardwareInventoryPartNumber_Type(String):
    """Custom type hardwareInventoryPartNumber based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HardwareInventoryPartNumber_Type.__name__ = "String"
_HardwareInventoryPartNumber_Object = MibTableColumn
hardwareInventoryPartNumber = _HardwareInventoryPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 1, 1, 4),
    _HardwareInventoryPartNumber_Type()
)
hardwareInventoryPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareInventoryPartNumber.setStatus("current")


class _HardwareInventorySerialNumber_Type(String):
    """Custom type hardwareInventorySerialNumber based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HardwareInventorySerialNumber_Type.__name__ = "String"
_HardwareInventorySerialNumber_Object = MibTableColumn
hardwareInventorySerialNumber = _HardwareInventorySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 1, 1, 5),
    _HardwareInventorySerialNumber_Type()
)
hardwareInventorySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareInventorySerialNumber.setStatus("current")


class _HardwareInventoryHwDescription_Type(String):
    """Custom type hardwareInventoryHwDescription based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HardwareInventoryHwDescription_Type.__name__ = "String"
_HardwareInventoryHwDescription_Object = MibTableColumn
hardwareInventoryHwDescription = _HardwareInventoryHwDescription_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 1, 1, 6),
    _HardwareInventoryHwDescription_Type()
)
hardwareInventoryHwDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareInventoryHwDescription.setStatus("current")


class _HardwareInventoryPartInfo_Type(String):
    """Custom type hardwareInventoryPartInfo based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HardwareInventoryPartInfo_Type.__name__ = "String"
_HardwareInventoryPartInfo_Object = MibTableColumn
hardwareInventoryPartInfo = _HardwareInventoryPartInfo_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 1, 1, 7),
    _HardwareInventoryPartInfo_Type()
)
hardwareInventoryPartInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareInventoryPartInfo.setStatus("current")
_HardwareEnvironmentTable_Object = MibTable
hardwareEnvironmentTable = _HardwareEnvironmentTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hardwareEnvironmentTable.setStatus("current")
_HardwareEnvironmentEntry_Object = MibTableRow
hardwareEnvironmentEntry = _HardwareEnvironmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 2, 1)
)
hardwareEnvironmentEntry.setIndexNames(
    (0, "VIPTELA-HARDWARE", "hardwareEnvironmentHwClass"),
    (0, "VIPTELA-HARDWARE", "hardwareEnvironmentHwItem"),
    (0, "VIPTELA-HARDWARE", "hardwareEnvironmentHwDevIndex"),
)
if mibBuilder.loadTexts:
    hardwareEnvironmentEntry.setStatus("current")


class _HardwareEnvironmentHwClass_Type(Integer32):
    """Custom type hardwareEnvironmentHwClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("temperatureSensors", 0),
          ("fans", 1),
          ("pEM", 2),
          ("pIM", 3),
          ("uSB", 4),
          ("lED", 5),
          ("nIM", 6))
    )


_HardwareEnvironmentHwClass_Type.__name__ = "Integer32"
_HardwareEnvironmentHwClass_Object = MibTableColumn
hardwareEnvironmentHwClass = _HardwareEnvironmentHwClass_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 2, 1, 1),
    _HardwareEnvironmentHwClass_Type()
)
hardwareEnvironmentHwClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hardwareEnvironmentHwClass.setStatus("current")


class _HardwareEnvironmentHwItem_Type(String):
    """Custom type hardwareEnvironmentHwItem based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HardwareEnvironmentHwItem_Type.__name__ = "String"
_HardwareEnvironmentHwItem_Object = MibTableColumn
hardwareEnvironmentHwItem = _HardwareEnvironmentHwItem_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 2, 1, 2),
    _HardwareEnvironmentHwItem_Type()
)
hardwareEnvironmentHwItem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hardwareEnvironmentHwItem.setStatus("current")
_HardwareEnvironmentHwDevIndex_Type = Unsigned32
_HardwareEnvironmentHwDevIndex_Object = MibTableColumn
hardwareEnvironmentHwDevIndex = _HardwareEnvironmentHwDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 2, 1, 3),
    _HardwareEnvironmentHwDevIndex_Type()
)
hardwareEnvironmentHwDevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hardwareEnvironmentHwDevIndex.setStatus("current")


class _HardwareEnvironmentStatus_Type(Integer32):
    """Custom type hardwareEnvironmentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oK", 0),
          ("down", 1),
          ("failed", 2))
    )


_HardwareEnvironmentStatus_Type.__name__ = "Integer32"
_HardwareEnvironmentStatus_Object = MibTableColumn
hardwareEnvironmentStatus = _HardwareEnvironmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 2, 1, 4),
    _HardwareEnvironmentStatus_Type()
)
hardwareEnvironmentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareEnvironmentStatus.setStatus("current")


class _HardwareEnvironmentMeasurement_Type(String):
    """Custom type hardwareEnvironmentMeasurement based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_HardwareEnvironmentMeasurement_Type.__name__ = "String"
_HardwareEnvironmentMeasurement_Object = MibTableColumn
hardwareEnvironmentMeasurement = _HardwareEnvironmentMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 2, 1, 5),
    _HardwareEnvironmentMeasurement_Type()
)
hardwareEnvironmentMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareEnvironmentMeasurement.setStatus("current")
_HardwareAlarmsTable_Object = MibTable
hardwareAlarmsTable = _HardwareAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hardwareAlarmsTable.setStatus("current")
_HardwareAlarmsEntry_Object = MibTableRow
hardwareAlarmsEntry = _HardwareAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 3, 1)
)
hardwareAlarmsEntry.setIndexNames(
    (0, "VIPTELA-HARDWARE", "hardwareAlarmsAlarmId"),
    (0, "VIPTELA-HARDWARE", "hardwareAlarmsAlarmInstance"),
)
if mibBuilder.loadTexts:
    hardwareAlarmsEntry.setStatus("current")
_HardwareAlarmsAlarmId_Type = Unsigned32
_HardwareAlarmsAlarmId_Object = MibTableColumn
hardwareAlarmsAlarmId = _HardwareAlarmsAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 3, 1, 1),
    _HardwareAlarmsAlarmId_Type()
)
hardwareAlarmsAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hardwareAlarmsAlarmId.setStatus("current")


class _HardwareAlarmsAlarmName_Type(String):
    """Custom type hardwareAlarmsAlarmName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HardwareAlarmsAlarmName_Type.__name__ = "String"
_HardwareAlarmsAlarmName_Object = MibTableColumn
hardwareAlarmsAlarmName = _HardwareAlarmsAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 3, 1, 2),
    _HardwareAlarmsAlarmName_Type()
)
hardwareAlarmsAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareAlarmsAlarmName.setStatus("current")
_HardwareAlarmsAlarmInstance_Type = Unsigned32
_HardwareAlarmsAlarmInstance_Object = MibTableColumn
hardwareAlarmsAlarmInstance = _HardwareAlarmsAlarmInstance_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 3, 1, 3),
    _HardwareAlarmsAlarmInstance_Type()
)
hardwareAlarmsAlarmInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hardwareAlarmsAlarmInstance.setStatus("current")


class _HardwareAlarmsAlarmTime_Type(String):
    """Custom type hardwareAlarmsAlarmTime based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HardwareAlarmsAlarmTime_Type.__name__ = "String"
_HardwareAlarmsAlarmTime_Object = MibTableColumn
hardwareAlarmsAlarmTime = _HardwareAlarmsAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 3, 1, 4),
    _HardwareAlarmsAlarmTime_Type()
)
hardwareAlarmsAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareAlarmsAlarmTime.setStatus("current")


class _HardwareAlarmsAlarmCategory_Type(Integer32):
    """Custom type hardwareAlarmsAlarmCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical", 0),
          ("major", 1),
          ("minor", 2))
    )


_HardwareAlarmsAlarmCategory_Type.__name__ = "Integer32"
_HardwareAlarmsAlarmCategory_Object = MibTableColumn
hardwareAlarmsAlarmCategory = _HardwareAlarmsAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 3, 1, 5),
    _HardwareAlarmsAlarmCategory_Type()
)
hardwareAlarmsAlarmCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareAlarmsAlarmCategory.setStatus("current")


class _HardwareAlarmsAlarmDescription_Type(String):
    """Custom type hardwareAlarmsAlarmDescription based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HardwareAlarmsAlarmDescription_Type.__name__ = "String"
_HardwareAlarmsAlarmDescription_Object = MibTableColumn
hardwareAlarmsAlarmDescription = _HardwareAlarmsAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 3, 1, 6),
    _HardwareAlarmsAlarmDescription_Type()
)
hardwareAlarmsAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareAlarmsAlarmDescription.setStatus("current")
_HardwareTemperatureThresholdsTable_Object = MibTable
hardwareTemperatureThresholdsTable = _HardwareTemperatureThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 4)
)
if mibBuilder.loadTexts:
    hardwareTemperatureThresholdsTable.setStatus("current")
_HardwareTemperatureThresholdsEntry_Object = MibTableRow
hardwareTemperatureThresholdsEntry = _HardwareTemperatureThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 4, 1)
)
hardwareTemperatureThresholdsEntry.setIndexNames(
    (0, "VIPTELA-HARDWARE", "hardwareTemperatureThresholdsHwSensorType"),
    (0, "VIPTELA-HARDWARE", "hardwareTemperatureThresholdsHwDevIndex"),
)
if mibBuilder.loadTexts:
    hardwareTemperatureThresholdsEntry.setStatus("current")
_HardwareTemperatureThresholdsHwSensorType_Type = HwSensorTypeEnum
_HardwareTemperatureThresholdsHwSensorType_Object = MibTableColumn
hardwareTemperatureThresholdsHwSensorType = _HardwareTemperatureThresholdsHwSensorType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 4, 1, 1),
    _HardwareTemperatureThresholdsHwSensorType_Type()
)
hardwareTemperatureThresholdsHwSensorType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hardwareTemperatureThresholdsHwSensorType.setStatus("current")
_HardwareTemperatureThresholdsHwDevIndex_Type = Unsigned32
_HardwareTemperatureThresholdsHwDevIndex_Object = MibTableColumn
hardwareTemperatureThresholdsHwDevIndex = _HardwareTemperatureThresholdsHwDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 4, 1, 2),
    _HardwareTemperatureThresholdsHwDevIndex_Type()
)
hardwareTemperatureThresholdsHwDevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hardwareTemperatureThresholdsHwDevIndex.setStatus("current")
_HardwareTemperatureThresholdsFanSpeedNormal_Type = Unsigned32
_HardwareTemperatureThresholdsFanSpeedNormal_Object = MibTableColumn
hardwareTemperatureThresholdsFanSpeedNormal = _HardwareTemperatureThresholdsFanSpeedNormal_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 4, 1, 3),
    _HardwareTemperatureThresholdsFanSpeedNormal_Type()
)
hardwareTemperatureThresholdsFanSpeedNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareTemperatureThresholdsFanSpeedNormal.setStatus("current")
_HardwareTemperatureThresholdsYellowAlarmNormal_Type = Unsigned32
_HardwareTemperatureThresholdsYellowAlarmNormal_Object = MibTableColumn
hardwareTemperatureThresholdsYellowAlarmNormal = _HardwareTemperatureThresholdsYellowAlarmNormal_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 4, 1, 4),
    _HardwareTemperatureThresholdsYellowAlarmNormal_Type()
)
hardwareTemperatureThresholdsYellowAlarmNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareTemperatureThresholdsYellowAlarmNormal.setStatus("current")
_HardwareTemperatureThresholdsYellowAlarmBadFan_Type = Unsigned32
_HardwareTemperatureThresholdsYellowAlarmBadFan_Object = MibTableColumn
hardwareTemperatureThresholdsYellowAlarmBadFan = _HardwareTemperatureThresholdsYellowAlarmBadFan_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 4, 1, 5),
    _HardwareTemperatureThresholdsYellowAlarmBadFan_Type()
)
hardwareTemperatureThresholdsYellowAlarmBadFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareTemperatureThresholdsYellowAlarmBadFan.setStatus("current")
_HardwareTemperatureThresholdsRedAlarmNormal_Type = Unsigned32
_HardwareTemperatureThresholdsRedAlarmNormal_Object = MibTableColumn
hardwareTemperatureThresholdsRedAlarmNormal = _HardwareTemperatureThresholdsRedAlarmNormal_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 4, 1, 6),
    _HardwareTemperatureThresholdsRedAlarmNormal_Type()
)
hardwareTemperatureThresholdsRedAlarmNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareTemperatureThresholdsRedAlarmNormal.setStatus("current")
_HardwareTemperatureThresholdsRedAlarmBadFan_Type = Unsigned32
_HardwareTemperatureThresholdsRedAlarmBadFan_Object = MibTableColumn
hardwareTemperatureThresholdsRedAlarmBadFan = _HardwareTemperatureThresholdsRedAlarmBadFan_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 4, 1, 7),
    _HardwareTemperatureThresholdsRedAlarmBadFan_Type()
)
hardwareTemperatureThresholdsRedAlarmBadFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareTemperatureThresholdsRedAlarmBadFan.setStatus("current")
_HardwarePoeTable_Object = MibTable
hardwarePoeTable = _HardwarePoeTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 5)
)
if mibBuilder.loadTexts:
    hardwarePoeTable.setStatus("current")
_HardwarePoeEntry_Object = MibTableRow
hardwarePoeEntry = _HardwarePoeEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 5, 1)
)
hardwarePoeEntry.setIndexNames(
    (0, "VIPTELA-HARDWARE", "hardwarePoeIfname"),
)
if mibBuilder.loadTexts:
    hardwarePoeEntry.setStatus("current")


class _HardwarePoeIfname_Type(String):
    """Custom type hardwarePoeIfname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HardwarePoeIfname_Type.__name__ = "String"
_HardwarePoeIfname_Object = MibTableColumn
hardwarePoeIfname = _HardwarePoeIfname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 5, 1, 1),
    _HardwarePoeIfname_Type()
)
hardwarePoeIfname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hardwarePoeIfname.setStatus("current")


class _HardwarePoeIfStatus_Type(String):
    """Custom type hardwarePoeIfStatus based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HardwarePoeIfStatus_Type.__name__ = "String"
_HardwarePoeIfStatus_Object = MibTableColumn
hardwarePoeIfStatus = _HardwarePoeIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 5, 1, 2),
    _HardwarePoeIfStatus_Type()
)
hardwarePoeIfStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hardwarePoeIfStatus.setStatus("current")


class _HardwarePoeStatus_Type(String):
    """Custom type hardwarePoeStatus based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HardwarePoeStatus_Type.__name__ = "String"
_HardwarePoeStatus_Object = MibTableColumn
hardwarePoeStatus = _HardwarePoeStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 5, 1, 3),
    _HardwarePoeStatus_Type()
)
hardwarePoeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwarePoeStatus.setStatus("current")
_HardwarePoeMaxPower_Type = ConfdString
_HardwarePoeMaxPower_Object = MibTableColumn
hardwarePoeMaxPower = _HardwarePoeMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 5, 1, 4),
    _HardwarePoeMaxPower_Type()
)
hardwarePoeMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwarePoeMaxPower.setStatus("current")
_HardwarePoeUsedPower_Type = ConfdString
_HardwarePoeUsedPower_Object = MibTableColumn
hardwarePoeUsedPower = _HardwarePoeUsedPower_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 5, 1, 5),
    _HardwarePoeUsedPower_Type()
)
hardwarePoeUsedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwarePoeUsedPower.setStatus("current")
_HardwarePoePdClass_Type = HwPoeClassEnum
_HardwarePoePdClass_Object = MibTableColumn
hardwarePoePdClass = _HardwarePoePdClass_Object(
    (1, 3, 6, 1, 4, 1, 41916, 3, 1, 5, 1, 6),
    _HardwarePoePdClass_Type()
)
hardwarePoePdClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwarePoePdClass.setStatus("current")
_ViptelaDevices_ObjectIdentity = ObjectIdentity
viptelaDevices = _ViptelaDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2)
)
_Vsmart_ObjectIdentity = ObjectIdentity
vsmart = _Vsmart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 1)
)
_Vmanage_ObjectIdentity = ObjectIdentity
vmanage = _Vmanage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 2)
)
_VbondSoftware_ObjectIdentity = ObjectIdentity
vbondSoftware = _VbondSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 3)
)
_Vedge1000AC_ObjectIdentity = ObjectIdentity
vedge1000AC = _Vedge1000AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 4)
)
_Vedge2000AC_ObjectIdentity = ObjectIdentity
vedge2000AC = _Vedge2000AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 5)
)
_Vedge100AC_ObjectIdentity = ObjectIdentity
vedge100AC = _Vedge100AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 6)
)
_Vedge100W2AC_ObjectIdentity = ObjectIdentity
vedge100W2AC = _Vedge100W2AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 7)
)
_Vedge100WMAC_ObjectIdentity = ObjectIdentity
vedge100WMAC = _Vedge100WMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 8)
)
_Vedge100M2AC_ObjectIdentity = ObjectIdentity
vedge100M2AC = _Vedge100M2AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 9)
)
_Vedge100MAC_ObjectIdentity = ObjectIdentity
vedge100MAC = _Vedge100MAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 10)
)
_Vedge100BAC_ObjectIdentity = ObjectIdentity
vedge100BAC = _Vedge100BAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 11)
)
_VedgeCloud_ObjectIdentity = ObjectIdentity
vedgeCloud = _VedgeCloud_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 12)
)
_Vcontainer_ObjectIdentity = ObjectIdentity
vcontainer = _Vcontainer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 13)
)
_Vedge5000AC_ObjectIdentity = ObjectIdentity
vedge5000AC = _Vedge5000AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 14)
)
_Vedge101BAC_ObjectIdentity = ObjectIdentity
vedge101BAC = _Vedge101BAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 15)
)
_Vedge1001AC_ObjectIdentity = ObjectIdentity
vedge1001AC = _Vedge1001AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 16)
)
_Vedge101MAC_ObjectIdentity = ObjectIdentity
vedge101MAC = _Vedge101MAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 17)
)
_VedgeISR11004GAC_ObjectIdentity = ObjectIdentity
vedgeISR11004GAC = _VedgeISR11004GAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 18)
)
_VedgeISR11006GAC_ObjectIdentity = ObjectIdentity
vedgeISR11006GAC = _VedgeISR11006GAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 19)
)
_VedgeISR11004GLTEAC_ObjectIdentity = ObjectIdentity
vedgeISR11004GLTEAC = _VedgeISR11004GLTEAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 20)
)
_VedgeISR1100X4GAC_ObjectIdentity = ObjectIdentity
vedgeISR1100X4GAC = _VedgeISR1100X4GAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 21)
)
_VedgeISR1100X6GAC_ObjectIdentity = ObjectIdentity
vedgeISR1100X6GAC = _VedgeISR1100X6GAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 3, 2, 22)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIPTELA-HARDWARE",
    **{"ConfdString": ConfdString,
       "String": String,
       "HwSensorTypeEnum": HwSensorTypeEnum,
       "HwTypeEnum": HwTypeEnum,
       "ModuleStateEnum": ModuleStateEnum,
       "FailureStateEnum": FailureStateEnum,
       "HwPoeClassEnum": HwPoeClassEnum,
       "viptela-hardware": viptela_hardware,
       "hardware": hardware,
       "hardwareInventoryTable": hardwareInventoryTable,
       "hardwareInventoryEntry": hardwareInventoryEntry,
       "hardwareInventoryHwType": hardwareInventoryHwType,
       "hardwareInventoryHwDevIndex": hardwareInventoryHwDevIndex,
       "hardwareInventoryVersion": hardwareInventoryVersion,
       "hardwareInventoryPartNumber": hardwareInventoryPartNumber,
       "hardwareInventorySerialNumber": hardwareInventorySerialNumber,
       "hardwareInventoryHwDescription": hardwareInventoryHwDescription,
       "hardwareInventoryPartInfo": hardwareInventoryPartInfo,
       "hardwareEnvironmentTable": hardwareEnvironmentTable,
       "hardwareEnvironmentEntry": hardwareEnvironmentEntry,
       "hardwareEnvironmentHwClass": hardwareEnvironmentHwClass,
       "hardwareEnvironmentHwItem": hardwareEnvironmentHwItem,
       "hardwareEnvironmentHwDevIndex": hardwareEnvironmentHwDevIndex,
       "hardwareEnvironmentStatus": hardwareEnvironmentStatus,
       "hardwareEnvironmentMeasurement": hardwareEnvironmentMeasurement,
       "hardwareAlarmsTable": hardwareAlarmsTable,
       "hardwareAlarmsEntry": hardwareAlarmsEntry,
       "hardwareAlarmsAlarmId": hardwareAlarmsAlarmId,
       "hardwareAlarmsAlarmName": hardwareAlarmsAlarmName,
       "hardwareAlarmsAlarmInstance": hardwareAlarmsAlarmInstance,
       "hardwareAlarmsAlarmTime": hardwareAlarmsAlarmTime,
       "hardwareAlarmsAlarmCategory": hardwareAlarmsAlarmCategory,
       "hardwareAlarmsAlarmDescription": hardwareAlarmsAlarmDescription,
       "hardwareTemperatureThresholdsTable": hardwareTemperatureThresholdsTable,
       "hardwareTemperatureThresholdsEntry": hardwareTemperatureThresholdsEntry,
       "hardwareTemperatureThresholdsHwSensorType": hardwareTemperatureThresholdsHwSensorType,
       "hardwareTemperatureThresholdsHwDevIndex": hardwareTemperatureThresholdsHwDevIndex,
       "hardwareTemperatureThresholdsFanSpeedNormal": hardwareTemperatureThresholdsFanSpeedNormal,
       "hardwareTemperatureThresholdsYellowAlarmNormal": hardwareTemperatureThresholdsYellowAlarmNormal,
       "hardwareTemperatureThresholdsYellowAlarmBadFan": hardwareTemperatureThresholdsYellowAlarmBadFan,
       "hardwareTemperatureThresholdsRedAlarmNormal": hardwareTemperatureThresholdsRedAlarmNormal,
       "hardwareTemperatureThresholdsRedAlarmBadFan": hardwareTemperatureThresholdsRedAlarmBadFan,
       "hardwarePoeTable": hardwarePoeTable,
       "hardwarePoeEntry": hardwarePoeEntry,
       "hardwarePoeIfname": hardwarePoeIfname,
       "hardwarePoeIfStatus": hardwarePoeIfStatus,
       "hardwarePoeStatus": hardwarePoeStatus,
       "hardwarePoeMaxPower": hardwarePoeMaxPower,
       "hardwarePoeUsedPower": hardwarePoeUsedPower,
       "hardwarePoePdClass": hardwarePoePdClass,
       "viptelaDevices": viptelaDevices,
       "vsmart": vsmart,
       "vmanage": vmanage,
       "vbondSoftware": vbondSoftware,
       "vedge1000AC": vedge1000AC,
       "vedge2000AC": vedge2000AC,
       "vedge100AC": vedge100AC,
       "vedge100W2AC": vedge100W2AC,
       "vedge100WMAC": vedge100WMAC,
       "vedge100M2AC": vedge100M2AC,
       "vedge100MAC": vedge100MAC,
       "vedge100BAC": vedge100BAC,
       "vedgeCloud": vedgeCloud,
       "vcontainer": vcontainer,
       "vedge5000AC": vedge5000AC,
       "vedge101BAC": vedge101BAC,
       "vedge1001AC": vedge1001AC,
       "vedge101MAC": vedge101MAC,
       "vedgeISR11004GAC": vedgeISR11004GAC,
       "vedgeISR11006GAC": vedgeISR11006GAC,
       "vedgeISR11004GLTEAC": vedgeISR11004GLTEAC,
       "vedgeISR1100X4GAC": vedgeISR1100X4GAC,
       "vedgeISR1100X6GAC": vedgeISR1100X6GAC}
)
