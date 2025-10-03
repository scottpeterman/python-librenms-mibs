# SNMP MIB module (EATON-SENSOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\eaton\EATON-SENSOR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:38 2025
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

(sensorAgent,) = mibBuilder.importSymbols(
    "EATON-OIDS",
    "sensorAgent")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

eatonSensor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1)
)
if mibBuilder.loadTexts:
    eatonSensor.setRevisions(
        ("2022-05-06 12:00",
         "2018-12-17 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnixTimeStamp(TextualConvention, Counter32):
    status = "current"
    displayHint = "dddddddddd"


class PositionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("other", 1),
          ("rackRear", 2),
          ("rackFront", 3),
          ("batteryRoom", 4))
    )



class ElevationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("other", 1),
          ("bottom", 2),
          ("middle", 3),
          ("top", 4))
    )



class CommunicationStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("communicationOK", 2),
          ("communicationLost", 3))
    )



class ProbeConnectionType(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("internal", 1),
          ("wired", 2),
          ("wireless", 3))
    )



class EnableType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



class AlarmType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("good", 0),
          ("lowWarning", 1),
          ("lowCritical", 2),
          ("highWarning", 3),
          ("highCritical", 4))
    )



class ResetCommandType(TextualConvention, Integer32):
    status = "current"
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



class PolarityType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normallyOpened", 0),
          ("normallyClosed", 1))
    )



class AlarmSeverityType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("informational", 1),
          ("warning", 2),
          ("critical", 3))
    )



class AlarmLevelType(TextualConvention, Integer32):
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
        *(("good", 0),
          ("informational", 1),
          ("warning", 2),
          ("critical", 3))
    )



class StateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )



class TemperatureUnitType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tenthOfDegKelvin", 0),
          ("tenthOfDegCelsius", 1),
          ("tenthOfDegFarhenheit", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Sensor_ObjectIdentity = ObjectIdentity
sensor = _Sensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1)
)
_SensorNotification_ObjectIdentity = ObjectIdentity
sensorNotification = _SensorNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 0)
)
_SensorCount_Type = Integer32
_SensorCount_Object = MibScalar
sensorCount = _SensorCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 1),
    _SensorCount_Type()
)
sensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorCount.setStatus("current")
_SensorIdentificationTable_Object = MibTable
sensorIdentificationTable = _SensorIdentificationTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sensorIdentificationTable.setStatus("current")
_SensorIdentificationEntry_Object = MibTableRow
sensorIdentificationEntry = _SensorIdentificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 2, 1)
)
sensorIdentificationEntry.setIndexNames(
    (0, "EATON-SENSOR-MIB", "sensorIndex"),
)
if mibBuilder.loadTexts:
    sensorIdentificationEntry.setStatus("current")


class _SensorIndex_Type(Integer32):
    """Custom type sensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SensorIndex_Type.__name__ = "Integer32"
_SensorIndex_Object = MibTableColumn
sensorIndex = _SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 2, 1, 1),
    _SensorIndex_Type()
)
sensorIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sensorIndex.setStatus("current")
_SensorUuid_Type = OctetString
_SensorUuid_Object = MibTableColumn
sensorUuid = _SensorUuid_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 2, 1, 2),
    _SensorUuid_Type()
)
sensorUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorUuid.setStatus("current")
_SensorConnectionType_Type = ProbeConnectionType
_SensorConnectionType_Object = MibTableColumn
sensorConnectionType = _SensorConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 2, 1, 3),
    _SensorConnectionType_Type()
)
sensorConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorConnectionType.setStatus("current")
_SensorAddress_Type = OctetString
_SensorAddress_Object = MibTableColumn
sensorAddress = _SensorAddress_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 2, 1, 4),
    _SensorAddress_Type()
)
sensorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorAddress.setStatus("current")
_SensorMonitoredBy_Type = ObjectIdentifier
_SensorMonitoredBy_Object = MibTableColumn
sensorMonitoredBy = _SensorMonitoredBy_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 2, 1, 5),
    _SensorMonitoredBy_Type()
)
sensorMonitoredBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorMonitoredBy.setStatus("current")


class _SensorManufacturer_Type(OctetString):
    """Custom type sensorManufacturer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SensorManufacturer_Type.__name__ = "OctetString"
_SensorManufacturer_Object = MibTableColumn
sensorManufacturer = _SensorManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 2, 1, 6),
    _SensorManufacturer_Type()
)
sensorManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorManufacturer.setStatus("current")


class _SensorModel_Type(OctetString):
    """Custom type sensorModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SensorModel_Type.__name__ = "OctetString"
_SensorModel_Object = MibTableColumn
sensorModel = _SensorModel_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 2, 1, 7),
    _SensorModel_Type()
)
sensorModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorModel.setStatus("current")


class _SensorPartNumber_Type(OctetString):
    """Custom type sensorPartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SensorPartNumber_Type.__name__ = "OctetString"
_SensorPartNumber_Object = MibTableColumn
sensorPartNumber = _SensorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 2, 1, 8),
    _SensorPartNumber_Type()
)
sensorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorPartNumber.setStatus("current")


class _SensorSerialNumber_Type(OctetString):
    """Custom type sensorSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SensorSerialNumber_Type.__name__ = "OctetString"
_SensorSerialNumber_Object = MibTableColumn
sensorSerialNumber = _SensorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 2, 1, 9),
    _SensorSerialNumber_Type()
)
sensorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorSerialNumber.setStatus("current")


class _SensorFirmwareVersion_Type(OctetString):
    """Custom type sensorFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SensorFirmwareVersion_Type.__name__ = "OctetString"
_SensorFirmwareVersion_Object = MibTableColumn
sensorFirmwareVersion = _SensorFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 2, 1, 10),
    _SensorFirmwareVersion_Type()
)
sensorFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorFirmwareVersion.setStatus("current")
_SensorConfigurationTable_Object = MibTable
sensorConfigurationTable = _SensorConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sensorConfigurationTable.setStatus("current")
_SensorConfigurationEntry_Object = MibTableRow
sensorConfigurationEntry = _SensorConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 3, 1)
)
sensorConfigurationEntry.setIndexNames(
    (0, "EATON-SENSOR-MIB", "sensorIndex"),
)
if mibBuilder.loadTexts:
    sensorConfigurationEntry.setStatus("current")


class _SensorName_Type(OctetString):
    """Custom type sensorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SensorName_Type.__name__ = "OctetString"
_SensorName_Object = MibTableColumn
sensorName = _SensorName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 3, 1, 1),
    _SensorName_Type()
)
sensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorName.setStatus("current")


class _SensorLocation_Type(OctetString):
    """Custom type sensorLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SensorLocation_Type.__name__ = "OctetString"
_SensorLocation_Object = MibTableColumn
sensorLocation = _SensorLocation_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 3, 1, 2),
    _SensorLocation_Type()
)
sensorLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorLocation.setStatus("current")
_SensorPosition_Type = PositionType
_SensorPosition_Object = MibTableColumn
sensorPosition = _SensorPosition_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 3, 1, 3),
    _SensorPosition_Type()
)
sensorPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorPosition.setStatus("current")
_SensorElevation_Type = ElevationType
_SensorElevation_Object = MibTableColumn
sensorElevation = _SensorElevation_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 3, 1, 4),
    _SensorElevation_Type()
)
sensorElevation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorElevation.setStatus("current")
_SensorUElevation_Type = Integer32
_SensorUElevation_Object = MibTableColumn
sensorUElevation = _SensorUElevation_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 3, 1, 5),
    _SensorUElevation_Type()
)
sensorUElevation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorUElevation.setStatus("current")
_SensorMonitoringTable_Object = MibTable
sensorMonitoringTable = _SensorMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 4)
)
if mibBuilder.loadTexts:
    sensorMonitoringTable.setStatus("current")
_SensorMonitoringEntry_Object = MibTableRow
sensorMonitoringEntry = _SensorMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 4, 1)
)
sensorMonitoringEntry.setIndexNames(
    (0, "EATON-SENSOR-MIB", "sensorIndex"),
)
if mibBuilder.loadTexts:
    sensorMonitoringEntry.setStatus("current")
_SensorStatus_Type = CommunicationStatus
_SensorStatus_Object = MibTableColumn
sensorStatus = _SensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 4, 1, 1),
    _SensorStatus_Type()
)
sensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorStatus.setStatus("current")
_SensorStatusSince_Type = UnixTimeStamp
_SensorStatusSince_Object = MibTableColumn
sensorStatusSince = _SensorStatusSince_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 4, 1, 2),
    _SensorStatusSince_Type()
)
sensorStatusSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorStatusSince.setStatus("current")
_SensorTemperatureCount_Type = Integer32
_SensorTemperatureCount_Object = MibTableColumn
sensorTemperatureCount = _SensorTemperatureCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 4, 1, 3),
    _SensorTemperatureCount_Type()
)
sensorTemperatureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTemperatureCount.setStatus("current")
_SensorHumidityCount_Type = Integer32
_SensorHumidityCount_Object = MibTableColumn
sensorHumidityCount = _SensorHumidityCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 4, 1, 4),
    _SensorHumidityCount_Type()
)
sensorHumidityCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorHumidityCount.setStatus("current")
_SensorDigitalInputCount_Type = Integer32
_SensorDigitalInputCount_Object = MibTableColumn
sensorDigitalInputCount = _SensorDigitalInputCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 4, 1, 5),
    _SensorDigitalInputCount_Type()
)
sensorDigitalInputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorDigitalInputCount.setStatus("current")
_SensorAnalogInputCount_Type = Integer32
_SensorAnalogInputCount_Object = MibTableColumn
sensorAnalogInputCount = _SensorAnalogInputCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 4, 1, 6),
    _SensorAnalogInputCount_Type()
)
sensorAnalogInputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorAnalogInputCount.setStatus("current")
_Temperature_ObjectIdentity = ObjectIdentity
temperature = _Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2)
)
_TemperatureNotification_ObjectIdentity = ObjectIdentity
temperatureNotification = _TemperatureNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 0)
)
_TemperatureIdentificationTable_Object = MibTable
temperatureIdentificationTable = _TemperatureIdentificationTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    temperatureIdentificationTable.setStatus("current")
_TemperatureIdentificationEntry_Object = MibTableRow
temperatureIdentificationEntry = _TemperatureIdentificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 1, 1)
)
temperatureIdentificationEntry.setIndexNames(
    (0, "EATON-SENSOR-MIB", "sensorIndex"),
    (0, "EATON-SENSOR-MIB", "temperatureIndex"),
)
if mibBuilder.loadTexts:
    temperatureIdentificationEntry.setStatus("current")


class _TemperatureIndex_Type(Integer32):
    """Custom type temperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TemperatureIndex_Type.__name__ = "Integer32"
_TemperatureIndex_Object = MibTableColumn
temperatureIndex = _TemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 1, 1, 1),
    _TemperatureIndex_Type()
)
temperatureIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    temperatureIndex.setStatus("current")
_TemperatureUuid_Type = OctetString
_TemperatureUuid_Object = MibTableColumn
temperatureUuid = _TemperatureUuid_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 1, 1, 2),
    _TemperatureUuid_Type()
)
temperatureUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureUuid.setStatus("current")
_TemperatureConnectionType_Type = ProbeConnectionType
_TemperatureConnectionType_Object = MibTableColumn
temperatureConnectionType = _TemperatureConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 1, 1, 3),
    _TemperatureConnectionType_Type()
)
temperatureConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureConnectionType.setStatus("current")
_TemperatureConfigurationTable_Object = MibTable
temperatureConfigurationTable = _TemperatureConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 2)
)
if mibBuilder.loadTexts:
    temperatureConfigurationTable.setStatus("current")
_TemperatureConfigurationEntry_Object = MibTableRow
temperatureConfigurationEntry = _TemperatureConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 2, 1)
)
temperatureConfigurationEntry.setIndexNames(
    (0, "EATON-SENSOR-MIB", "sensorIndex"),
    (0, "EATON-SENSOR-MIB", "temperatureIndex"),
)
if mibBuilder.loadTexts:
    temperatureConfigurationEntry.setStatus("current")


class _TemperatureName_Type(OctetString):
    """Custom type temperatureName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_TemperatureName_Type.__name__ = "OctetString"
_TemperatureName_Object = MibTableColumn
temperatureName = _TemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 2, 1, 1),
    _TemperatureName_Type()
)
temperatureName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureName.setStatus("current")
_TemperatureEnable_Type = EnableType
_TemperatureEnable_Object = MibTableColumn
temperatureEnable = _TemperatureEnable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 2, 1, 2),
    _TemperatureEnable_Type()
)
temperatureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureEnable.setStatus("current")
_TemperatureOffset_Type = Integer32
_TemperatureOffset_Object = MibTableColumn
temperatureOffset = _TemperatureOffset_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 2, 1, 3),
    _TemperatureOffset_Type()
)
temperatureOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureOffset.setStatus("current")
_TemperatureAlarmEnable_Type = EnableType
_TemperatureAlarmEnable_Object = MibTableColumn
temperatureAlarmEnable = _TemperatureAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 2, 1, 4),
    _TemperatureAlarmEnable_Type()
)
temperatureAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureAlarmEnable.setStatus("current")
_TemperatureThresholdLowWarning_Type = Integer32
_TemperatureThresholdLowWarning_Object = MibTableColumn
temperatureThresholdLowWarning = _TemperatureThresholdLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 2, 1, 5),
    _TemperatureThresholdLowWarning_Type()
)
temperatureThresholdLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureThresholdLowWarning.setStatus("current")
_TemperatureThresholdLowCritical_Type = Integer32
_TemperatureThresholdLowCritical_Object = MibTableColumn
temperatureThresholdLowCritical = _TemperatureThresholdLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 2, 1, 6),
    _TemperatureThresholdLowCritical_Type()
)
temperatureThresholdLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureThresholdLowCritical.setStatus("current")
_TemperatureThresholdHighWarning_Type = Integer32
_TemperatureThresholdHighWarning_Object = MibTableColumn
temperatureThresholdHighWarning = _TemperatureThresholdHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 2, 1, 7),
    _TemperatureThresholdHighWarning_Type()
)
temperatureThresholdHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureThresholdHighWarning.setStatus("current")
_TemperatureThresholdHighCritical_Type = Integer32
_TemperatureThresholdHighCritical_Object = MibTableColumn
temperatureThresholdHighCritical = _TemperatureThresholdHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 2, 1, 8),
    _TemperatureThresholdHighCritical_Type()
)
temperatureThresholdHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureThresholdHighCritical.setStatus("current")
_TemperatureThresholdHysteresis_Type = Integer32
_TemperatureThresholdHysteresis_Object = MibTableColumn
temperatureThresholdHysteresis = _TemperatureThresholdHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 2, 1, 9),
    _TemperatureThresholdHysteresis_Type()
)
temperatureThresholdHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureThresholdHysteresis.setStatus("current")


class _TemperatureAlarmGracePeriod_Type(Integer32):
    """Custom type temperatureAlarmGracePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TemperatureAlarmGracePeriod_Type.__name__ = "Integer32"
_TemperatureAlarmGracePeriod_Object = MibTableColumn
temperatureAlarmGracePeriod = _TemperatureAlarmGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 2, 1, 10),
    _TemperatureAlarmGracePeriod_Type()
)
temperatureAlarmGracePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureAlarmGracePeriod.setStatus("current")
_TemperatureMonitoringTable_Object = MibTable
temperatureMonitoringTable = _TemperatureMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 3)
)
if mibBuilder.loadTexts:
    temperatureMonitoringTable.setStatus("current")
_TemperatureMonitoringEntry_Object = MibTableRow
temperatureMonitoringEntry = _TemperatureMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 3, 1)
)
temperatureMonitoringEntry.setIndexNames(
    (0, "EATON-SENSOR-MIB", "sensorIndex"),
    (0, "EATON-SENSOR-MIB", "temperatureIndex"),
)
if mibBuilder.loadTexts:
    temperatureMonitoringEntry.setStatus("current")
_TemperatureAlarm_Type = AlarmType
_TemperatureAlarm_Object = MibTableColumn
temperatureAlarm = _TemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 3, 1, 1),
    _TemperatureAlarm_Type()
)
temperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureAlarm.setStatus("current")
_TemperatureAlarmChangeSince_Type = UnixTimeStamp
_TemperatureAlarmChangeSince_Object = MibTableColumn
temperatureAlarmChangeSince = _TemperatureAlarmChangeSince_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 3, 1, 2),
    _TemperatureAlarmChangeSince_Type()
)
temperatureAlarmChangeSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureAlarmChangeSince.setStatus("current")
_TemperatureValue_Type = Integer32
_TemperatureValue_Object = MibTableColumn
temperatureValue = _TemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 3, 1, 3),
    _TemperatureValue_Type()
)
temperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureValue.setStatus("current")
_TemperatureCommunicationStatus_Type = CommunicationStatus
_TemperatureCommunicationStatus_Object = MibTableColumn
temperatureCommunicationStatus = _TemperatureCommunicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 3, 1, 4),
    _TemperatureCommunicationStatus_Type()
)
temperatureCommunicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCommunicationStatus.setStatus("current")
_TemperatureCommunicationStatusSince_Type = UnixTimeStamp
_TemperatureCommunicationStatusSince_Object = MibTableColumn
temperatureCommunicationStatusSince = _TemperatureCommunicationStatusSince_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 3, 1, 5),
    _TemperatureCommunicationStatusSince_Type()
)
temperatureCommunicationStatusSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCommunicationStatusSince.setStatus("current")
_TemperatureMonitoringMinMaxTable_Object = MibTable
temperatureMonitoringMinMaxTable = _TemperatureMonitoringMinMaxTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 4)
)
if mibBuilder.loadTexts:
    temperatureMonitoringMinMaxTable.setStatus("current")
_TemperatureMonitoringMinMaxEntry_Object = MibTableRow
temperatureMonitoringMinMaxEntry = _TemperatureMonitoringMinMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 4, 1)
)
temperatureMonitoringMinMaxEntry.setIndexNames(
    (0, "EATON-SENSOR-MIB", "sensorIndex"),
    (0, "EATON-SENSOR-MIB", "temperatureIndex"),
)
if mibBuilder.loadTexts:
    temperatureMonitoringMinMaxEntry.setStatus("current")
_TemperatureMinValue_Type = Integer32
_TemperatureMinValue_Object = MibTableColumn
temperatureMinValue = _TemperatureMinValue_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 4, 1, 1),
    _TemperatureMinValue_Type()
)
temperatureMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureMinValue.setStatus("current")
_TemperatureMinValueSince_Type = UnixTimeStamp
_TemperatureMinValueSince_Object = MibTableColumn
temperatureMinValueSince = _TemperatureMinValueSince_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 4, 1, 2),
    _TemperatureMinValueSince_Type()
)
temperatureMinValueSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureMinValueSince.setStatus("current")
_TemperatureMaxValue_Type = Integer32
_TemperatureMaxValue_Object = MibTableColumn
temperatureMaxValue = _TemperatureMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 4, 1, 3),
    _TemperatureMaxValue_Type()
)
temperatureMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureMaxValue.setStatus("current")
_TemperatureMaxValueSince_Type = UnixTimeStamp
_TemperatureMaxValueSince_Object = MibTableColumn
temperatureMaxValueSince = _TemperatureMaxValueSince_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 4, 1, 4),
    _TemperatureMaxValueSince_Type()
)
temperatureMaxValueSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureMaxValueSince.setStatus("current")
_TemperatureResetMinMax_Type = ResetCommandType
_TemperatureResetMinMax_Object = MibTableColumn
temperatureResetMinMax = _TemperatureResetMinMax_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 4, 1, 5),
    _TemperatureResetMinMax_Type()
)
temperatureResetMinMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureResetMinMax.setStatus("current")
_TemperatureUnit_Type = TemperatureUnitType
_TemperatureUnit_Object = MibScalar
temperatureUnit = _TemperatureUnit_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 5),
    _TemperatureUnit_Type()
)
temperatureUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureUnit.setStatus("current")
_Humidity_ObjectIdentity = ObjectIdentity
humidity = _Humidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3)
)
_HumidityNotification_ObjectIdentity = ObjectIdentity
humidityNotification = _HumidityNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 0)
)
_HumidityIdentificationTable_Object = MibTable
humidityIdentificationTable = _HumidityIdentificationTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    humidityIdentificationTable.setStatus("current")
_HumidityIdentificationEntry_Object = MibTableRow
humidityIdentificationEntry = _HumidityIdentificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 1, 1)
)
humidityIdentificationEntry.setIndexNames(
    (0, "EATON-SENSOR-MIB", "sensorIndex"),
    (0, "EATON-SENSOR-MIB", "humidityIndex"),
)
if mibBuilder.loadTexts:
    humidityIdentificationEntry.setStatus("current")


class _HumidityIndex_Type(Integer32):
    """Custom type humidityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HumidityIndex_Type.__name__ = "Integer32"
_HumidityIndex_Object = MibTableColumn
humidityIndex = _HumidityIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 1, 1, 1),
    _HumidityIndex_Type()
)
humidityIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    humidityIndex.setStatus("current")
_HumidityUuid_Type = OctetString
_HumidityUuid_Object = MibTableColumn
humidityUuid = _HumidityUuid_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 1, 1, 2),
    _HumidityUuid_Type()
)
humidityUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityUuid.setStatus("current")
_HumidityConnectionType_Type = ProbeConnectionType
_HumidityConnectionType_Object = MibTableColumn
humidityConnectionType = _HumidityConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 1, 1, 3),
    _HumidityConnectionType_Type()
)
humidityConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityConnectionType.setStatus("current")
_HumidityConfigurationTable_Object = MibTable
humidityConfigurationTable = _HumidityConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 2)
)
if mibBuilder.loadTexts:
    humidityConfigurationTable.setStatus("current")
_HumidityConfigurationEntry_Object = MibTableRow
humidityConfigurationEntry = _HumidityConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 2, 1)
)
humidityConfigurationEntry.setIndexNames(
    (0, "EATON-SENSOR-MIB", "sensorIndex"),
    (0, "EATON-SENSOR-MIB", "humidityIndex"),
)
if mibBuilder.loadTexts:
    humidityConfigurationEntry.setStatus("current")


class _HumidityName_Type(OctetString):
    """Custom type humidityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HumidityName_Type.__name__ = "OctetString"
_HumidityName_Object = MibTableColumn
humidityName = _HumidityName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 2, 1, 1),
    _HumidityName_Type()
)
humidityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityName.setStatus("current")
_HumidityEnable_Type = EnableType
_HumidityEnable_Object = MibTableColumn
humidityEnable = _HumidityEnable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 2, 1, 2),
    _HumidityEnable_Type()
)
humidityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityEnable.setStatus("current")
_HumidityOffset_Type = Integer32
_HumidityOffset_Object = MibTableColumn
humidityOffset = _HumidityOffset_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 2, 1, 3),
    _HumidityOffset_Type()
)
humidityOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityOffset.setStatus("current")
_HumidityAlarmEnable_Type = EnableType
_HumidityAlarmEnable_Object = MibTableColumn
humidityAlarmEnable = _HumidityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 2, 1, 4),
    _HumidityAlarmEnable_Type()
)
humidityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityAlarmEnable.setStatus("current")
_HumidityThresholdLowWarning_Type = Integer32
_HumidityThresholdLowWarning_Object = MibTableColumn
humidityThresholdLowWarning = _HumidityThresholdLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 2, 1, 5),
    _HumidityThresholdLowWarning_Type()
)
humidityThresholdLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityThresholdLowWarning.setStatus("current")
_HumidityThresholdLowCritical_Type = Integer32
_HumidityThresholdLowCritical_Object = MibTableColumn
humidityThresholdLowCritical = _HumidityThresholdLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 2, 1, 6),
    _HumidityThresholdLowCritical_Type()
)
humidityThresholdLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityThresholdLowCritical.setStatus("current")
_HumidityThresholdHighWarning_Type = Integer32
_HumidityThresholdHighWarning_Object = MibTableColumn
humidityThresholdHighWarning = _HumidityThresholdHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 2, 1, 7),
    _HumidityThresholdHighWarning_Type()
)
humidityThresholdHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityThresholdHighWarning.setStatus("current")
_HumidityThresholdHighCritical_Type = Integer32
_HumidityThresholdHighCritical_Object = MibTableColumn
humidityThresholdHighCritical = _HumidityThresholdHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 2, 1, 8),
    _HumidityThresholdHighCritical_Type()
)
humidityThresholdHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityThresholdHighCritical.setStatus("current")
_HumidityThresholdHysteresis_Type = Integer32
_HumidityThresholdHysteresis_Object = MibTableColumn
humidityThresholdHysteresis = _HumidityThresholdHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 2, 1, 9),
    _HumidityThresholdHysteresis_Type()
)
humidityThresholdHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityThresholdHysteresis.setStatus("current")


class _HumidityAlarmGracePeriod_Type(Integer32):
    """Custom type humidityAlarmGracePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_HumidityAlarmGracePeriod_Type.__name__ = "Integer32"
_HumidityAlarmGracePeriod_Object = MibTableColumn
humidityAlarmGracePeriod = _HumidityAlarmGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 2, 1, 10),
    _HumidityAlarmGracePeriod_Type()
)
humidityAlarmGracePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityAlarmGracePeriod.setStatus("current")
_HumidityMonitoringTable_Object = MibTable
humidityMonitoringTable = _HumidityMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 3)
)
if mibBuilder.loadTexts:
    humidityMonitoringTable.setStatus("current")
_HumidityMonitoringEntry_Object = MibTableRow
humidityMonitoringEntry = _HumidityMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 3, 1)
)
humidityMonitoringEntry.setIndexNames(
    (0, "EATON-SENSOR-MIB", "sensorIndex"),
    (0, "EATON-SENSOR-MIB", "humidityIndex"),
)
if mibBuilder.loadTexts:
    humidityMonitoringEntry.setStatus("current")
_HumidityAlarm_Type = AlarmType
_HumidityAlarm_Object = MibTableColumn
humidityAlarm = _HumidityAlarm_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 3, 1, 1),
    _HumidityAlarm_Type()
)
humidityAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityAlarm.setStatus("current")
_HumidityAlarmChangeSince_Type = UnixTimeStamp
_HumidityAlarmChangeSince_Object = MibTableColumn
humidityAlarmChangeSince = _HumidityAlarmChangeSince_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 3, 1, 2),
    _HumidityAlarmChangeSince_Type()
)
humidityAlarmChangeSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityAlarmChangeSince.setStatus("current")
_HumidityValue_Type = Integer32
_HumidityValue_Object = MibTableColumn
humidityValue = _HumidityValue_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 3, 1, 3),
    _HumidityValue_Type()
)
humidityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityValue.setStatus("current")
_HumidityCommunicationStatus_Type = CommunicationStatus
_HumidityCommunicationStatus_Object = MibTableColumn
humidityCommunicationStatus = _HumidityCommunicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 3, 1, 4),
    _HumidityCommunicationStatus_Type()
)
humidityCommunicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityCommunicationStatus.setStatus("current")
_HumidityCommunicationStatusSince_Type = UnixTimeStamp
_HumidityCommunicationStatusSince_Object = MibTableColumn
humidityCommunicationStatusSince = _HumidityCommunicationStatusSince_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 3, 1, 5),
    _HumidityCommunicationStatusSince_Type()
)
humidityCommunicationStatusSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityCommunicationStatusSince.setStatus("current")
_HumidityMonitoringMinMaxTable_Object = MibTable
humidityMonitoringMinMaxTable = _HumidityMonitoringMinMaxTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 4)
)
if mibBuilder.loadTexts:
    humidityMonitoringMinMaxTable.setStatus("current")
_HumidityMonitoringMinMaxEntry_Object = MibTableRow
humidityMonitoringMinMaxEntry = _HumidityMonitoringMinMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 4, 1)
)
humidityMonitoringMinMaxEntry.setIndexNames(
    (0, "EATON-SENSOR-MIB", "sensorIndex"),
    (0, "EATON-SENSOR-MIB", "humidityIndex"),
)
if mibBuilder.loadTexts:
    humidityMonitoringMinMaxEntry.setStatus("current")
_HumidityMinValue_Type = Integer32
_HumidityMinValue_Object = MibTableColumn
humidityMinValue = _HumidityMinValue_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 4, 1, 1),
    _HumidityMinValue_Type()
)
humidityMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityMinValue.setStatus("current")
_HumidityMinValueSince_Type = UnixTimeStamp
_HumidityMinValueSince_Object = MibTableColumn
humidityMinValueSince = _HumidityMinValueSince_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 4, 1, 2),
    _HumidityMinValueSince_Type()
)
humidityMinValueSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityMinValueSince.setStatus("current")
_HumidityMaxValue_Type = Integer32
_HumidityMaxValue_Object = MibTableColumn
humidityMaxValue = _HumidityMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 4, 1, 3),
    _HumidityMaxValue_Type()
)
humidityMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityMaxValue.setStatus("current")
_HumidityMaxValueSince_Type = UnixTimeStamp
_HumidityMaxValueSince_Object = MibTableColumn
humidityMaxValueSince = _HumidityMaxValueSince_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 4, 1, 4),
    _HumidityMaxValueSince_Type()
)
humidityMaxValueSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityMaxValueSince.setStatus("current")
_HumidityResetMinMax_Type = ResetCommandType
_HumidityResetMinMax_Object = MibTableColumn
humidityResetMinMax = _HumidityResetMinMax_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 4, 1, 5),
    _HumidityResetMinMax_Type()
)
humidityResetMinMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityResetMinMax.setStatus("current")
_DigitalInput_ObjectIdentity = ObjectIdentity
digitalInput = _DigitalInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4)
)
_DigitalInputNotification_ObjectIdentity = ObjectIdentity
digitalInputNotification = _DigitalInputNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 0)
)
_DigitalInputIdentificationTable_Object = MibTable
digitalInputIdentificationTable = _DigitalInputIdentificationTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 1)
)
if mibBuilder.loadTexts:
    digitalInputIdentificationTable.setStatus("current")
_DigitalInputIdentificationEntry_Object = MibTableRow
digitalInputIdentificationEntry = _DigitalInputIdentificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 1, 1)
)
digitalInputIdentificationEntry.setIndexNames(
    (0, "EATON-SENSOR-MIB", "sensorIndex"),
    (0, "EATON-SENSOR-MIB", "digitalInputIndex"),
)
if mibBuilder.loadTexts:
    digitalInputIdentificationEntry.setStatus("current")


class _DigitalInputIndex_Type(Integer32):
    """Custom type digitalInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DigitalInputIndex_Type.__name__ = "Integer32"
_DigitalInputIndex_Object = MibTableColumn
digitalInputIndex = _DigitalInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 1, 1, 1),
    _DigitalInputIndex_Type()
)
digitalInputIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    digitalInputIndex.setStatus("current")
_DigitalInputUuid_Type = OctetString
_DigitalInputUuid_Object = MibTableColumn
digitalInputUuid = _DigitalInputUuid_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 1, 1, 2),
    _DigitalInputUuid_Type()
)
digitalInputUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInputUuid.setStatus("current")
_DigitalInputConnectionType_Type = ProbeConnectionType
_DigitalInputConnectionType_Object = MibTableColumn
digitalInputConnectionType = _DigitalInputConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 1, 1, 3),
    _DigitalInputConnectionType_Type()
)
digitalInputConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInputConnectionType.setStatus("current")
_DigitalInputConfigurationTable_Object = MibTable
digitalInputConfigurationTable = _DigitalInputConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 2)
)
if mibBuilder.loadTexts:
    digitalInputConfigurationTable.setStatus("current")
_DigitalInputConfigurationEntry_Object = MibTableRow
digitalInputConfigurationEntry = _DigitalInputConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 2, 1)
)
digitalInputConfigurationEntry.setIndexNames(
    (0, "EATON-SENSOR-MIB", "sensorIndex"),
    (0, "EATON-SENSOR-MIB", "digitalInputIndex"),
)
if mibBuilder.loadTexts:
    digitalInputConfigurationEntry.setStatus("current")


class _DigitalInputName_Type(OctetString):
    """Custom type digitalInputName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_DigitalInputName_Type.__name__ = "OctetString"
_DigitalInputName_Object = MibTableColumn
digitalInputName = _DigitalInputName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 2, 1, 1),
    _DigitalInputName_Type()
)
digitalInputName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInputName.setStatus("current")
_DigitalInputEnable_Type = EnableType
_DigitalInputEnable_Object = MibTableColumn
digitalInputEnable = _DigitalInputEnable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 2, 1, 2),
    _DigitalInputEnable_Type()
)
digitalInputEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInputEnable.setStatus("current")
_DigitalInputPolarity_Type = PolarityType
_DigitalInputPolarity_Object = MibTableColumn
digitalInputPolarity = _DigitalInputPolarity_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 2, 1, 3),
    _DigitalInputPolarity_Type()
)
digitalInputPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInputPolarity.setStatus("current")
_DigitalInputAlarmEnable_Type = EnableType
_DigitalInputAlarmEnable_Object = MibTableColumn
digitalInputAlarmEnable = _DigitalInputAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 2, 1, 4),
    _DigitalInputAlarmEnable_Type()
)
digitalInputAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInputAlarmEnable.setStatus("current")
_DigitalInputAlarmSeverity_Type = AlarmSeverityType
_DigitalInputAlarmSeverity_Object = MibTableColumn
digitalInputAlarmSeverity = _DigitalInputAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 2, 1, 5),
    _DigitalInputAlarmSeverity_Type()
)
digitalInputAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInputAlarmSeverity.setStatus("current")


class _DigitalInputAlarmGracePeriod_Type(Integer32):
    """Custom type digitalInputAlarmGracePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_DigitalInputAlarmGracePeriod_Type.__name__ = "Integer32"
_DigitalInputAlarmGracePeriod_Object = MibTableColumn
digitalInputAlarmGracePeriod = _DigitalInputAlarmGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 2, 1, 6),
    _DigitalInputAlarmGracePeriod_Type()
)
digitalInputAlarmGracePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInputAlarmGracePeriod.setStatus("current")
_DigitalInputMonitoringTable_Object = MibTable
digitalInputMonitoringTable = _DigitalInputMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 3)
)
if mibBuilder.loadTexts:
    digitalInputMonitoringTable.setStatus("current")
_DigitalInputMonitoringEntry_Object = MibTableRow
digitalInputMonitoringEntry = _DigitalInputMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 3, 1)
)
digitalInputMonitoringEntry.setIndexNames(
    (0, "EATON-SENSOR-MIB", "sensorIndex"),
    (0, "EATON-SENSOR-MIB", "digitalInputIndex"),
)
if mibBuilder.loadTexts:
    digitalInputMonitoringEntry.setStatus("current")
_DigitalInputAlarm_Type = AlarmLevelType
_DigitalInputAlarm_Object = MibTableColumn
digitalInputAlarm = _DigitalInputAlarm_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 3, 1, 1),
    _DigitalInputAlarm_Type()
)
digitalInputAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInputAlarm.setStatus("current")
_DigitalInputAlarmChangeSince_Type = UnixTimeStamp
_DigitalInputAlarmChangeSince_Object = MibTableColumn
digitalInputAlarmChangeSince = _DigitalInputAlarmChangeSince_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 3, 1, 2),
    _DigitalInputAlarmChangeSince_Type()
)
digitalInputAlarmChangeSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInputAlarmChangeSince.setStatus("current")
_DigitalInputState_Type = StateType
_DigitalInputState_Object = MibTableColumn
digitalInputState = _DigitalInputState_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 3, 1, 3),
    _DigitalInputState_Type()
)
digitalInputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInputState.setStatus("current")
_DigitalInputStateSince_Type = UnixTimeStamp
_DigitalInputStateSince_Object = MibTableColumn
digitalInputStateSince = _DigitalInputStateSince_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 3, 1, 4),
    _DigitalInputStateSince_Type()
)
digitalInputStateSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInputStateSince.setStatus("current")
_DigitalInputCommunicationStatus_Type = CommunicationStatus
_DigitalInputCommunicationStatus_Object = MibTableColumn
digitalInputCommunicationStatus = _DigitalInputCommunicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 3, 1, 5),
    _DigitalInputCommunicationStatus_Type()
)
digitalInputCommunicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInputCommunicationStatus.setStatus("current")
_DigitalInputCommunicationStatusSince_Type = UnixTimeStamp
_DigitalInputCommunicationStatusSince_Object = MibTableColumn
digitalInputCommunicationStatusSince = _DigitalInputCommunicationStatusSince_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 3, 1, 6),
    _DigitalInputCommunicationStatusSince_Type()
)
digitalInputCommunicationStatusSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInputCommunicationStatusSince.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 10)
)
_ObjectGroups_ObjectIdentity = ObjectIdentity
objectGroups = _ObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 10, 2)
)

# Managed Objects groups

sensorRequiredGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 10, 2, 1)
)
sensorRequiredGroup.setObjects(
      *(("EATON-SENSOR-MIB", "sensorCount"),
        ("EATON-SENSOR-MIB", "sensorIndex"),
        ("EATON-SENSOR-MIB", "sensorManufacturer"),
        ("EATON-SENSOR-MIB", "sensorModel"),
        ("EATON-SENSOR-MIB", "sensorPartNumber"),
        ("EATON-SENSOR-MIB", "sensorSerialNumber"),
        ("EATON-SENSOR-MIB", "sensorFirmwareVersion"),
        ("EATON-SENSOR-MIB", "sensorName"),
        ("EATON-SENSOR-MIB", "sensorStatus"),
        ("EATON-SENSOR-MIB", "sensorStatusSince"),
        ("EATON-SENSOR-MIB", "sensorTemperatureCount"),
        ("EATON-SENSOR-MIB", "sensorHumidityCount"),
        ("EATON-SENSOR-MIB", "sensorDigitalInputCount"),
        ("EATON-SENSOR-MIB", "temperatureIndex"),
        ("EATON-SENSOR-MIB", "temperatureName"),
        ("EATON-SENSOR-MIB", "temperatureValue"),
        ("EATON-SENSOR-MIB", "temperatureUnit"),
        ("EATON-SENSOR-MIB", "humidityIndex"),
        ("EATON-SENSOR-MIB", "humidityName"),
        ("EATON-SENSOR-MIB", "humidityValue"),
        ("EATON-SENSOR-MIB", "digitalInputIndex"),
        ("EATON-SENSOR-MIB", "digitalInputName"))
)
if mibBuilder.loadTexts:
    sensorRequiredGroup.setStatus("current")

sensorOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 10, 2, 2)
)
sensorOptionalGroup.setObjects(
      *(("EATON-SENSOR-MIB", "sensorUuid"),
        ("EATON-SENSOR-MIB", "sensorConnectionType"),
        ("EATON-SENSOR-MIB", "sensorAddress"),
        ("EATON-SENSOR-MIB", "sensorMonitoredBy"),
        ("EATON-SENSOR-MIB", "sensorLocation"),
        ("EATON-SENSOR-MIB", "sensorPosition"),
        ("EATON-SENSOR-MIB", "sensorElevation"),
        ("EATON-SENSOR-MIB", "sensorUElevation"),
        ("EATON-SENSOR-MIB", "sensorAnalogInputCount"),
        ("EATON-SENSOR-MIB", "temperatureUuid"),
        ("EATON-SENSOR-MIB", "temperatureConnectionType"),
        ("EATON-SENSOR-MIB", "temperatureEnable"),
        ("EATON-SENSOR-MIB", "temperatureOffset"),
        ("EATON-SENSOR-MIB", "temperatureAlarmEnable"),
        ("EATON-SENSOR-MIB", "temperatureThresholdLowWarning"),
        ("EATON-SENSOR-MIB", "temperatureThresholdLowCritical"),
        ("EATON-SENSOR-MIB", "temperatureThresholdHighWarning"),
        ("EATON-SENSOR-MIB", "temperatureThresholdHighCritical"),
        ("EATON-SENSOR-MIB", "temperatureThresholdHysteresis"),
        ("EATON-SENSOR-MIB", "temperatureAlarmGracePeriod"),
        ("EATON-SENSOR-MIB", "temperatureAlarm"),
        ("EATON-SENSOR-MIB", "temperatureAlarmChangeSince"),
        ("EATON-SENSOR-MIB", "temperatureCommunicationStatus"),
        ("EATON-SENSOR-MIB", "temperatureCommunicationStatusSince"),
        ("EATON-SENSOR-MIB", "temperatureMinValue"),
        ("EATON-SENSOR-MIB", "temperatureMinValueSince"),
        ("EATON-SENSOR-MIB", "temperatureMaxValue"),
        ("EATON-SENSOR-MIB", "temperatureMaxValueSince"),
        ("EATON-SENSOR-MIB", "temperatureResetMinMax"),
        ("EATON-SENSOR-MIB", "humidityUuid"),
        ("EATON-SENSOR-MIB", "humidityConnectionType"),
        ("EATON-SENSOR-MIB", "humidityEnable"),
        ("EATON-SENSOR-MIB", "humidityOffset"),
        ("EATON-SENSOR-MIB", "humidityAlarmEnable"),
        ("EATON-SENSOR-MIB", "humidityThresholdLowWarning"),
        ("EATON-SENSOR-MIB", "humidityThresholdLowCritical"),
        ("EATON-SENSOR-MIB", "humidityThresholdHighWarning"),
        ("EATON-SENSOR-MIB", "humidityThresholdHighCritical"),
        ("EATON-SENSOR-MIB", "humidityThresholdHysteresis"),
        ("EATON-SENSOR-MIB", "humidityAlarmGracePeriod"),
        ("EATON-SENSOR-MIB", "humidityAlarm"),
        ("EATON-SENSOR-MIB", "humidityAlarmChangeSince"),
        ("EATON-SENSOR-MIB", "humidityCommunicationStatus"),
        ("EATON-SENSOR-MIB", "humidityCommunicationStatusSince"),
        ("EATON-SENSOR-MIB", "humidityMinValue"),
        ("EATON-SENSOR-MIB", "humidityMinValueSince"),
        ("EATON-SENSOR-MIB", "humidityMaxValue"),
        ("EATON-SENSOR-MIB", "humidityMaxValueSince"),
        ("EATON-SENSOR-MIB", "humidityResetMinMax"),
        ("EATON-SENSOR-MIB", "digitalInputUuid"),
        ("EATON-SENSOR-MIB", "digitalInputConnectionType"),
        ("EATON-SENSOR-MIB", "digitalInputEnable"),
        ("EATON-SENSOR-MIB", "digitalInputPolarity"),
        ("EATON-SENSOR-MIB", "digitalInputAlarmEnable"),
        ("EATON-SENSOR-MIB", "digitalInputAlarmSeverity"),
        ("EATON-SENSOR-MIB", "digitalInputAlarmGracePeriod"),
        ("EATON-SENSOR-MIB", "digitalInputState"),
        ("EATON-SENSOR-MIB", "digitalInputStateSince"),
        ("EATON-SENSOR-MIB", "digitalInputAlarm"),
        ("EATON-SENSOR-MIB", "digitalInputAlarmChangeSince"),
        ("EATON-SENSOR-MIB", "digitalInputCommunicationStatus"),
        ("EATON-SENSOR-MIB", "digitalInputCommunicationStatusSince"))
)
if mibBuilder.loadTexts:
    sensorOptionalGroup.setStatus("current")


# Notification objects

notifySensorCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 0, 1)
)
notifySensorCount.setObjects(
    ("EATON-SENSOR-MIB", "sensorCount")
)
if mibBuilder.loadTexts:
    notifySensorCount.setStatus(
        "current"
    )

notifySensorStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 1, 0, 2)
)
notifySensorStatus.setObjects(
      *(("EATON-SENSOR-MIB", "sensorIndex"),
        ("EATON-SENSOR-MIB", "sensorUuid"),
        ("EATON-SENSOR-MIB", "sensorStatus"),
        ("EATON-SENSOR-MIB", "sensorStatusSince"))
)
if mibBuilder.loadTexts:
    notifySensorStatus.setStatus(
        "current"
    )

notifyTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 0, 1)
)
notifyTemperatureAlarm.setObjects(
      *(("EATON-SENSOR-MIB", "sensorIndex"),
        ("EATON-SENSOR-MIB", "temperatureIndex"),
        ("EATON-SENSOR-MIB", "temperatureUuid"),
        ("EATON-SENSOR-MIB", "temperatureAlarm"),
        ("EATON-SENSOR-MIB", "temperatureAlarmChangeSince"),
        ("EATON-SENSOR-MIB", "temperatureValue"))
)
if mibBuilder.loadTexts:
    notifyTemperatureAlarm.setStatus(
        "current"
    )

notifyTemperatureCommunicationStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 2, 0, 2)
)
notifyTemperatureCommunicationStatus.setObjects(
      *(("EATON-SENSOR-MIB", "sensorIndex"),
        ("EATON-SENSOR-MIB", "temperatureIndex"),
        ("EATON-SENSOR-MIB", "temperatureUuid"),
        ("EATON-SENSOR-MIB", "temperatureCommunicationStatus"),
        ("EATON-SENSOR-MIB", "temperatureCommunicationStatusSince"))
)
if mibBuilder.loadTexts:
    notifyTemperatureCommunicationStatus.setStatus(
        "current"
    )

notifyHumidityAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 0, 1)
)
notifyHumidityAlarm.setObjects(
      *(("EATON-SENSOR-MIB", "sensorIndex"),
        ("EATON-SENSOR-MIB", "humidityIndex"),
        ("EATON-SENSOR-MIB", "humidityUuid"),
        ("EATON-SENSOR-MIB", "humidityAlarm"),
        ("EATON-SENSOR-MIB", "humidityAlarmChangeSince"),
        ("EATON-SENSOR-MIB", "humidityValue"))
)
if mibBuilder.loadTexts:
    notifyHumidityAlarm.setStatus(
        "current"
    )

notifyHumidityCommunicationStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 3, 0, 2)
)
notifyHumidityCommunicationStatus.setObjects(
      *(("EATON-SENSOR-MIB", "sensorIndex"),
        ("EATON-SENSOR-MIB", "humidityIndex"),
        ("EATON-SENSOR-MIB", "humidityUuid"),
        ("EATON-SENSOR-MIB", "humidityCommunicationStatus"),
        ("EATON-SENSOR-MIB", "humidityCommunicationStatusSince"))
)
if mibBuilder.loadTexts:
    notifyHumidityCommunicationStatus.setStatus(
        "current"
    )

notifyDigitalInputAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 0, 1)
)
notifyDigitalInputAlarm.setObjects(
      *(("EATON-SENSOR-MIB", "sensorIndex"),
        ("EATON-SENSOR-MIB", "digitalInputIndex"),
        ("EATON-SENSOR-MIB", "digitalInputUuid"),
        ("EATON-SENSOR-MIB", "digitalInputAlarm"),
        ("EATON-SENSOR-MIB", "digitalInputAlarmChangeSince"),
        ("EATON-SENSOR-MIB", "digitalInputState"),
        ("EATON-SENSOR-MIB", "digitalInputStateSince"))
)
if mibBuilder.loadTexts:
    notifyDigitalInputAlarm.setStatus(
        "current"
    )

notifydigitalInputCommunicationStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 4, 0, 2)
)
notifydigitalInputCommunicationStatus.setObjects(
      *(("EATON-SENSOR-MIB", "sensorIndex"),
        ("EATON-SENSOR-MIB", "digitalInputIndex"),
        ("EATON-SENSOR-MIB", "digitalInputUuid"),
        ("EATON-SENSOR-MIB", "digitalInputCommunicationStatus"),
        ("EATON-SENSOR-MIB", "digitalInputCommunicationStatusSince"))
)
if mibBuilder.loadTexts:
    notifydigitalInputCommunicationStatus.setStatus(
        "current"
    )


# Notifications groups

sensorNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 10, 2, 3)
)
sensorNotifyGroup.setObjects(
      *(("EATON-SENSOR-MIB", "notifySensorStatus"),
        ("EATON-SENSOR-MIB", "notifySensorCount"),
        ("EATON-SENSOR-MIB", "notifyTemperatureAlarm"),
        ("EATON-SENSOR-MIB", "notifyTemperatureCommunicationStatus"),
        ("EATON-SENSOR-MIB", "notifyHumidityAlarm"),
        ("EATON-SENSOR-MIB", "notifyHumidityCommunicationStatus"),
        ("EATON-SENSOR-MIB", "notifyDigitalInputAlarm"),
        ("EATON-SENSOR-MIB", "notifydigitalInputCommunicationStatus"))
)
if mibBuilder.loadTexts:
    sensorNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

eatonSensorCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 534, 6, 8, 1, 10, 1)
)
eatonSensorCompliances.setObjects(
      *(("EATON-SENSOR-MIB", "sensorRequiredGroup"),
        ("EATON-SENSOR-MIB", "sensorOptionalGroup"),
        ("EATON-SENSOR-MIB", "sensorNotifyGroup"))
)
if mibBuilder.loadTexts:
    eatonSensorCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EATON-SENSOR-MIB",
    **{"UnixTimeStamp": UnixTimeStamp,
       "PositionType": PositionType,
       "ElevationType": ElevationType,
       "CommunicationStatus": CommunicationStatus,
       "ProbeConnectionType": ProbeConnectionType,
       "EnableType": EnableType,
       "AlarmType": AlarmType,
       "ResetCommandType": ResetCommandType,
       "PolarityType": PolarityType,
       "AlarmSeverityType": AlarmSeverityType,
       "AlarmLevelType": AlarmLevelType,
       "StateType": StateType,
       "TemperatureUnitType": TemperatureUnitType,
       "eatonSensor": eatonSensor,
       "sensor": sensor,
       "sensorNotification": sensorNotification,
       "notifySensorCount": notifySensorCount,
       "notifySensorStatus": notifySensorStatus,
       "sensorCount": sensorCount,
       "sensorIdentificationTable": sensorIdentificationTable,
       "sensorIdentificationEntry": sensorIdentificationEntry,
       "sensorIndex": sensorIndex,
       "sensorUuid": sensorUuid,
       "sensorConnectionType": sensorConnectionType,
       "sensorAddress": sensorAddress,
       "sensorMonitoredBy": sensorMonitoredBy,
       "sensorManufacturer": sensorManufacturer,
       "sensorModel": sensorModel,
       "sensorPartNumber": sensorPartNumber,
       "sensorSerialNumber": sensorSerialNumber,
       "sensorFirmwareVersion": sensorFirmwareVersion,
       "sensorConfigurationTable": sensorConfigurationTable,
       "sensorConfigurationEntry": sensorConfigurationEntry,
       "sensorName": sensorName,
       "sensorLocation": sensorLocation,
       "sensorPosition": sensorPosition,
       "sensorElevation": sensorElevation,
       "sensorUElevation": sensorUElevation,
       "sensorMonitoringTable": sensorMonitoringTable,
       "sensorMonitoringEntry": sensorMonitoringEntry,
       "sensorStatus": sensorStatus,
       "sensorStatusSince": sensorStatusSince,
       "sensorTemperatureCount": sensorTemperatureCount,
       "sensorHumidityCount": sensorHumidityCount,
       "sensorDigitalInputCount": sensorDigitalInputCount,
       "sensorAnalogInputCount": sensorAnalogInputCount,
       "temperature": temperature,
       "temperatureNotification": temperatureNotification,
       "notifyTemperatureAlarm": notifyTemperatureAlarm,
       "notifyTemperatureCommunicationStatus": notifyTemperatureCommunicationStatus,
       "temperatureIdentificationTable": temperatureIdentificationTable,
       "temperatureIdentificationEntry": temperatureIdentificationEntry,
       "temperatureIndex": temperatureIndex,
       "temperatureUuid": temperatureUuid,
       "temperatureConnectionType": temperatureConnectionType,
       "temperatureConfigurationTable": temperatureConfigurationTable,
       "temperatureConfigurationEntry": temperatureConfigurationEntry,
       "temperatureName": temperatureName,
       "temperatureEnable": temperatureEnable,
       "temperatureOffset": temperatureOffset,
       "temperatureAlarmEnable": temperatureAlarmEnable,
       "temperatureThresholdLowWarning": temperatureThresholdLowWarning,
       "temperatureThresholdLowCritical": temperatureThresholdLowCritical,
       "temperatureThresholdHighWarning": temperatureThresholdHighWarning,
       "temperatureThresholdHighCritical": temperatureThresholdHighCritical,
       "temperatureThresholdHysteresis": temperatureThresholdHysteresis,
       "temperatureAlarmGracePeriod": temperatureAlarmGracePeriod,
       "temperatureMonitoringTable": temperatureMonitoringTable,
       "temperatureMonitoringEntry": temperatureMonitoringEntry,
       "temperatureAlarm": temperatureAlarm,
       "temperatureAlarmChangeSince": temperatureAlarmChangeSince,
       "temperatureValue": temperatureValue,
       "temperatureCommunicationStatus": temperatureCommunicationStatus,
       "temperatureCommunicationStatusSince": temperatureCommunicationStatusSince,
       "temperatureMonitoringMinMaxTable": temperatureMonitoringMinMaxTable,
       "temperatureMonitoringMinMaxEntry": temperatureMonitoringMinMaxEntry,
       "temperatureMinValue": temperatureMinValue,
       "temperatureMinValueSince": temperatureMinValueSince,
       "temperatureMaxValue": temperatureMaxValue,
       "temperatureMaxValueSince": temperatureMaxValueSince,
       "temperatureResetMinMax": temperatureResetMinMax,
       "temperatureUnit": temperatureUnit,
       "humidity": humidity,
       "humidityNotification": humidityNotification,
       "notifyHumidityAlarm": notifyHumidityAlarm,
       "notifyHumidityCommunicationStatus": notifyHumidityCommunicationStatus,
       "humidityIdentificationTable": humidityIdentificationTable,
       "humidityIdentificationEntry": humidityIdentificationEntry,
       "humidityIndex": humidityIndex,
       "humidityUuid": humidityUuid,
       "humidityConnectionType": humidityConnectionType,
       "humidityConfigurationTable": humidityConfigurationTable,
       "humidityConfigurationEntry": humidityConfigurationEntry,
       "humidityName": humidityName,
       "humidityEnable": humidityEnable,
       "humidityOffset": humidityOffset,
       "humidityAlarmEnable": humidityAlarmEnable,
       "humidityThresholdLowWarning": humidityThresholdLowWarning,
       "humidityThresholdLowCritical": humidityThresholdLowCritical,
       "humidityThresholdHighWarning": humidityThresholdHighWarning,
       "humidityThresholdHighCritical": humidityThresholdHighCritical,
       "humidityThresholdHysteresis": humidityThresholdHysteresis,
       "humidityAlarmGracePeriod": humidityAlarmGracePeriod,
       "humidityMonitoringTable": humidityMonitoringTable,
       "humidityMonitoringEntry": humidityMonitoringEntry,
       "humidityAlarm": humidityAlarm,
       "humidityAlarmChangeSince": humidityAlarmChangeSince,
       "humidityValue": humidityValue,
       "humidityCommunicationStatus": humidityCommunicationStatus,
       "humidityCommunicationStatusSince": humidityCommunicationStatusSince,
       "humidityMonitoringMinMaxTable": humidityMonitoringMinMaxTable,
       "humidityMonitoringMinMaxEntry": humidityMonitoringMinMaxEntry,
       "humidityMinValue": humidityMinValue,
       "humidityMinValueSince": humidityMinValueSince,
       "humidityMaxValue": humidityMaxValue,
       "humidityMaxValueSince": humidityMaxValueSince,
       "humidityResetMinMax": humidityResetMinMax,
       "digitalInput": digitalInput,
       "digitalInputNotification": digitalInputNotification,
       "notifyDigitalInputAlarm": notifyDigitalInputAlarm,
       "notifydigitalInputCommunicationStatus": notifydigitalInputCommunicationStatus,
       "digitalInputIdentificationTable": digitalInputIdentificationTable,
       "digitalInputIdentificationEntry": digitalInputIdentificationEntry,
       "digitalInputIndex": digitalInputIndex,
       "digitalInputUuid": digitalInputUuid,
       "digitalInputConnectionType": digitalInputConnectionType,
       "digitalInputConfigurationTable": digitalInputConfigurationTable,
       "digitalInputConfigurationEntry": digitalInputConfigurationEntry,
       "digitalInputName": digitalInputName,
       "digitalInputEnable": digitalInputEnable,
       "digitalInputPolarity": digitalInputPolarity,
       "digitalInputAlarmEnable": digitalInputAlarmEnable,
       "digitalInputAlarmSeverity": digitalInputAlarmSeverity,
       "digitalInputAlarmGracePeriod": digitalInputAlarmGracePeriod,
       "digitalInputMonitoringTable": digitalInputMonitoringTable,
       "digitalInputMonitoringEntry": digitalInputMonitoringEntry,
       "digitalInputAlarm": digitalInputAlarm,
       "digitalInputAlarmChangeSince": digitalInputAlarmChangeSince,
       "digitalInputState": digitalInputState,
       "digitalInputStateSince": digitalInputStateSince,
       "digitalInputCommunicationStatus": digitalInputCommunicationStatus,
       "digitalInputCommunicationStatusSince": digitalInputCommunicationStatusSince,
       "conformance": conformance,
       "eatonSensorCompliances": eatonSensorCompliances,
       "objectGroups": objectGroups,
       "sensorRequiredGroup": sensorRequiredGroup,
       "sensorOptionalGroup": sensorOptionalGroup,
       "sensorNotifyGroup": sensorNotifyGroup}
)
