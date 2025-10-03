# SNMP MIB module (JUNIPER-DOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-DOM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:03:05 2025
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

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(jnxDomLaneNotifications,
 jnxDomMibRoot,
 jnxDomNotifications) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxDomLaneNotifications",
    "jnxDomMibRoot",
    "jnxDomNotifications")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxDomMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1)
)
if mibBuilder.loadTexts:
    jnxDomMib.setRevisions(
        ("2014-03-20 00:00",
         "2009-12-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxDomAlarmId(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("domRxLossSignalAlarm", 0),
          ("domRxCDRLossLockAlarm", 1),
          ("domRxNotReadyAlarm", 2),
          ("domRxLaserPowerHighAlarm", 3),
          ("domRxLaserPowerLowAlarm", 4),
          ("domTxLaserBiasCurrentHighAlarm", 5),
          ("domTxLaserBiasCurrentLowAlarm", 6),
          ("domTxLaserOutputPowerHighAlarm", 7),
          ("domTxLaserOutputPowerLowAlarm", 8),
          ("domTxDataNotReadyAlarm", 9),
          ("domTxNotReadyAlarm", 10),
          ("domTxLaserFaultAlarm", 11),
          ("domTxCDRLossLockAlarm", 12),
          ("domModuleTemperatureHighAlarm", 13),
          ("domModuleTemperatureLowAlarm", 14),
          ("domModuleNotReadyAlarm", 15),
          ("domModulePowerDownAlarm", 16),
          ("domLinkDownAlarm", 17),
          ("domModuleRemovedAlarm", 18),
          ("domModuleVoltageHighAlarm", 19),
          ("domModuleVoltageLowAlarm", 20))
    )


class JnxDomWarningId(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("domRxLaserPowerHighWarning", 0),
          ("domRxLaserPowerLowWarning", 1),
          ("domTxLaserBiasCurrentHighWarning", 2),
          ("domTxLaserBiasCurrentLowWarning", 3),
          ("domTxLaserOutputPowerHighWarning", 4),
          ("domTxLaserOutputPowerLowWarning", 5),
          ("domModuleTemperatureHighWarning", 6),
          ("domModuleTemperatureLowWarning", 7),
          ("domModuleVoltageHighWarning", 8),
          ("domModuleVoltageLowWarning", 9))
    )


class JnxDomLaneAlarmId(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("domLaneRxLaserPowerHighAlarm", 0),
          ("domLaneRxLaserPowerLowAlarm", 1),
          ("domLaneTxLaserBiasCurrentHighAlarm", 2),
          ("domLaneTxLaserBiasCurrentLowAlarm", 3),
          ("domLaneTxLaserOutputPowerHighAlarm", 4),
          ("domLaneTxLaserOutputPowerLowAlarm", 5),
          ("domLaneLaserTemperatureHighAlarm", 6),
          ("domLaneLaserTemperatureLowAlarm", 7))
    )


class JnxDomLaneWarningId(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("domLaneRxLaserPowerHighWarning", 0),
          ("domLaneRxLaserPowerLowWarning", 1),
          ("domLaneTxLaserBiasCurrentHighWarning", 2),
          ("domLaneTxLaserBiasCurrentLowWarning", 3),
          ("domLaneTxLaserOutputPowerHighWarning", 4),
          ("domLaneTxLaserOutputPowerLowWarning", 5),
          ("domLaneLaserTemperatureHighWarning", 6),
          ("domLaneLaserTemperatureLowWarning", 7))
    )


# MIB Managed Objects in the order of their OIDs

_JnxDomDigitalMonitoring_ObjectIdentity = ObjectIdentity
jnxDomDigitalMonitoring = _JnxDomDigitalMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1)
)
_JnxDomCurrentTable_Object = MibTable
jnxDomCurrentTable = _JnxDomCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxDomCurrentTable.setStatus("current")
_JnxDomCurrentEntry_Object = MibTableRow
jnxDomCurrentEntry = _JnxDomCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1)
)
jnxDomCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxDomCurrentEntry.setStatus("current")
_JnxDomCurrentAlarms_Type = JnxDomAlarmId
_JnxDomCurrentAlarms_Object = MibTableColumn
jnxDomCurrentAlarms = _JnxDomCurrentAlarms_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 1),
    _JnxDomCurrentAlarms_Type()
)
jnxDomCurrentAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentAlarms.setStatus("current")
_JnxDomCurrentAlarmDate_Type = DateAndTime
_JnxDomCurrentAlarmDate_Object = MibTableColumn
jnxDomCurrentAlarmDate = _JnxDomCurrentAlarmDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 2),
    _JnxDomCurrentAlarmDate_Type()
)
jnxDomCurrentAlarmDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentAlarmDate.setStatus("current")
_JnxDomLastAlarms_Type = JnxDomAlarmId
_JnxDomLastAlarms_Object = MibTableColumn
jnxDomLastAlarms = _JnxDomLastAlarms_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 3),
    _JnxDomLastAlarms_Type()
)
jnxDomLastAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomLastAlarms.setStatus("current")
_JnxDomCurrentWarnings_Type = JnxDomWarningId
_JnxDomCurrentWarnings_Object = MibTableColumn
jnxDomCurrentWarnings = _JnxDomCurrentWarnings_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 4),
    _JnxDomCurrentWarnings_Type()
)
jnxDomCurrentWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentWarnings.setStatus("current")
_JnxDomCurrentRxLaserPower_Type = Integer32
_JnxDomCurrentRxLaserPower_Object = MibTableColumn
jnxDomCurrentRxLaserPower = _JnxDomCurrentRxLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 5),
    _JnxDomCurrentRxLaserPower_Type()
)
jnxDomCurrentRxLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentRxLaserPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentRxLaserPower.setUnits("0.01 dbm")
_JnxDomCurrentTxLaserBiasCurrent_Type = Integer32
_JnxDomCurrentTxLaserBiasCurrent_Object = MibTableColumn
jnxDomCurrentTxLaserBiasCurrent = _JnxDomCurrentTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 6),
    _JnxDomCurrentTxLaserBiasCurrent_Type()
)
jnxDomCurrentTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentTxLaserBiasCurrent.setUnits("0.001 mA")
_JnxDomCurrentTxLaserOutputPower_Type = Integer32
_JnxDomCurrentTxLaserOutputPower_Object = MibTableColumn
jnxDomCurrentTxLaserOutputPower = _JnxDomCurrentTxLaserOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 7),
    _JnxDomCurrentTxLaserOutputPower_Type()
)
jnxDomCurrentTxLaserOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentTxLaserOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentTxLaserOutputPower.setUnits("0.01 dbm")
_JnxDomCurrentModuleTemperature_Type = Integer32
_JnxDomCurrentModuleTemperature_Object = MibTableColumn
jnxDomCurrentModuleTemperature = _JnxDomCurrentModuleTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 8),
    _JnxDomCurrentModuleTemperature_Type()
)
jnxDomCurrentModuleTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentModuleTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentModuleTemperature.setUnits("Celsius (degrees C)")
_JnxDomCurrentRxLaserPowerHighAlarmThreshold_Type = Integer32
_JnxDomCurrentRxLaserPowerHighAlarmThreshold_Object = MibTableColumn
jnxDomCurrentRxLaserPowerHighAlarmThreshold = _JnxDomCurrentRxLaserPowerHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 9),
    _JnxDomCurrentRxLaserPowerHighAlarmThreshold_Type()
)
jnxDomCurrentRxLaserPowerHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentRxLaserPowerHighAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentRxLaserPowerHighAlarmThreshold.setUnits("0.01 dbm")
_JnxDomCurrentRxLaserPowerLowAlarmThreshold_Type = Integer32
_JnxDomCurrentRxLaserPowerLowAlarmThreshold_Object = MibTableColumn
jnxDomCurrentRxLaserPowerLowAlarmThreshold = _JnxDomCurrentRxLaserPowerLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 10),
    _JnxDomCurrentRxLaserPowerLowAlarmThreshold_Type()
)
jnxDomCurrentRxLaserPowerLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentRxLaserPowerLowAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentRxLaserPowerLowAlarmThreshold.setUnits("0.01 dbm")
_JnxDomCurrentRxLaserPowerHighWarningThreshold_Type = Integer32
_JnxDomCurrentRxLaserPowerHighWarningThreshold_Object = MibTableColumn
jnxDomCurrentRxLaserPowerHighWarningThreshold = _JnxDomCurrentRxLaserPowerHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 11),
    _JnxDomCurrentRxLaserPowerHighWarningThreshold_Type()
)
jnxDomCurrentRxLaserPowerHighWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentRxLaserPowerHighWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentRxLaserPowerHighWarningThreshold.setUnits("0.01 dbm")
_JnxDomCurrentRxLaserPowerLowWarningThreshold_Type = Integer32
_JnxDomCurrentRxLaserPowerLowWarningThreshold_Object = MibTableColumn
jnxDomCurrentRxLaserPowerLowWarningThreshold = _JnxDomCurrentRxLaserPowerLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 12),
    _JnxDomCurrentRxLaserPowerLowWarningThreshold_Type()
)
jnxDomCurrentRxLaserPowerLowWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentRxLaserPowerLowWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentRxLaserPowerLowWarningThreshold.setUnits("0.01 dbm")
_JnxDomCurrentTxLaserBiasCurrentHighAlarmThreshold_Type = Integer32
_JnxDomCurrentTxLaserBiasCurrentHighAlarmThreshold_Object = MibTableColumn
jnxDomCurrentTxLaserBiasCurrentHighAlarmThreshold = _JnxDomCurrentTxLaserBiasCurrentHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 13),
    _JnxDomCurrentTxLaserBiasCurrentHighAlarmThreshold_Type()
)
jnxDomCurrentTxLaserBiasCurrentHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentTxLaserBiasCurrentHighAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentTxLaserBiasCurrentHighAlarmThreshold.setUnits("0.001 mA")
_JnxDomCurrentTxLaserBiasCurrentLowAlarmThreshold_Type = Integer32
_JnxDomCurrentTxLaserBiasCurrentLowAlarmThreshold_Object = MibTableColumn
jnxDomCurrentTxLaserBiasCurrentLowAlarmThreshold = _JnxDomCurrentTxLaserBiasCurrentLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 14),
    _JnxDomCurrentTxLaserBiasCurrentLowAlarmThreshold_Type()
)
jnxDomCurrentTxLaserBiasCurrentLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentTxLaserBiasCurrentLowAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentTxLaserBiasCurrentLowAlarmThreshold.setUnits("0.001 mA")
_JnxDomCurrentTxLaserBiasCurrentHighWarningThreshold_Type = Integer32
_JnxDomCurrentTxLaserBiasCurrentHighWarningThreshold_Object = MibTableColumn
jnxDomCurrentTxLaserBiasCurrentHighWarningThreshold = _JnxDomCurrentTxLaserBiasCurrentHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 15),
    _JnxDomCurrentTxLaserBiasCurrentHighWarningThreshold_Type()
)
jnxDomCurrentTxLaserBiasCurrentHighWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentTxLaserBiasCurrentHighWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentTxLaserBiasCurrentHighWarningThreshold.setUnits("0.001 mA")
_JnxDomCurrentTxLaserBiasCurrentLowWarningThreshold_Type = Integer32
_JnxDomCurrentTxLaserBiasCurrentLowWarningThreshold_Object = MibTableColumn
jnxDomCurrentTxLaserBiasCurrentLowWarningThreshold = _JnxDomCurrentTxLaserBiasCurrentLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 16),
    _JnxDomCurrentTxLaserBiasCurrentLowWarningThreshold_Type()
)
jnxDomCurrentTxLaserBiasCurrentLowWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentTxLaserBiasCurrentLowWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentTxLaserBiasCurrentLowWarningThreshold.setUnits("0.001 mA")
_JnxDomCurrentTxLaserOutputPowerHighAlarmThreshold_Type = Integer32
_JnxDomCurrentTxLaserOutputPowerHighAlarmThreshold_Object = MibTableColumn
jnxDomCurrentTxLaserOutputPowerHighAlarmThreshold = _JnxDomCurrentTxLaserOutputPowerHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 17),
    _JnxDomCurrentTxLaserOutputPowerHighAlarmThreshold_Type()
)
jnxDomCurrentTxLaserOutputPowerHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentTxLaserOutputPowerHighAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentTxLaserOutputPowerHighAlarmThreshold.setUnits("0.01 dbm")
_JnxDomCurrentTxLaserOutputPowerLowAlarmThreshold_Type = Integer32
_JnxDomCurrentTxLaserOutputPowerLowAlarmThreshold_Object = MibTableColumn
jnxDomCurrentTxLaserOutputPowerLowAlarmThreshold = _JnxDomCurrentTxLaserOutputPowerLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 18),
    _JnxDomCurrentTxLaserOutputPowerLowAlarmThreshold_Type()
)
jnxDomCurrentTxLaserOutputPowerLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentTxLaserOutputPowerLowAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentTxLaserOutputPowerLowAlarmThreshold.setUnits("0.01 dbm")
_JnxDomCurrentTxLaserOutputPowerHighWarningThreshold_Type = Integer32
_JnxDomCurrentTxLaserOutputPowerHighWarningThreshold_Object = MibTableColumn
jnxDomCurrentTxLaserOutputPowerHighWarningThreshold = _JnxDomCurrentTxLaserOutputPowerHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 19),
    _JnxDomCurrentTxLaserOutputPowerHighWarningThreshold_Type()
)
jnxDomCurrentTxLaserOutputPowerHighWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentTxLaserOutputPowerHighWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentTxLaserOutputPowerHighWarningThreshold.setUnits("0.01 dbm")
_JnxDomCurrentTxLaserOutputPowerLowWarningThreshold_Type = Integer32
_JnxDomCurrentTxLaserOutputPowerLowWarningThreshold_Object = MibTableColumn
jnxDomCurrentTxLaserOutputPowerLowWarningThreshold = _JnxDomCurrentTxLaserOutputPowerLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 20),
    _JnxDomCurrentTxLaserOutputPowerLowWarningThreshold_Type()
)
jnxDomCurrentTxLaserOutputPowerLowWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentTxLaserOutputPowerLowWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentTxLaserOutputPowerLowWarningThreshold.setUnits("0.01 dbm")
_JnxDomCurrentModuleTemperatureHighAlarmThreshold_Type = Integer32
_JnxDomCurrentModuleTemperatureHighAlarmThreshold_Object = MibTableColumn
jnxDomCurrentModuleTemperatureHighAlarmThreshold = _JnxDomCurrentModuleTemperatureHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 21),
    _JnxDomCurrentModuleTemperatureHighAlarmThreshold_Type()
)
jnxDomCurrentModuleTemperatureHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentModuleTemperatureHighAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentModuleTemperatureHighAlarmThreshold.setUnits("Celsius (degrees C)")
_JnxDomCurrentModuleTemperatureLowAlarmThreshold_Type = Integer32
_JnxDomCurrentModuleTemperatureLowAlarmThreshold_Object = MibTableColumn
jnxDomCurrentModuleTemperatureLowAlarmThreshold = _JnxDomCurrentModuleTemperatureLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 22),
    _JnxDomCurrentModuleTemperatureLowAlarmThreshold_Type()
)
jnxDomCurrentModuleTemperatureLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentModuleTemperatureLowAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentModuleTemperatureLowAlarmThreshold.setUnits("Celsius (degrees C)")
_JnxDomCurrentModuleTemperatureHighWarningThreshold_Type = Integer32
_JnxDomCurrentModuleTemperatureHighWarningThreshold_Object = MibTableColumn
jnxDomCurrentModuleTemperatureHighWarningThreshold = _JnxDomCurrentModuleTemperatureHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 23),
    _JnxDomCurrentModuleTemperatureHighWarningThreshold_Type()
)
jnxDomCurrentModuleTemperatureHighWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentModuleTemperatureHighWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentModuleTemperatureHighWarningThreshold.setUnits("Celsius (degrees C)")
_JnxDomCurrentModuleTemperatureLowWarningThreshold_Type = Integer32
_JnxDomCurrentModuleTemperatureLowWarningThreshold_Object = MibTableColumn
jnxDomCurrentModuleTemperatureLowWarningThreshold = _JnxDomCurrentModuleTemperatureLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 24),
    _JnxDomCurrentModuleTemperatureLowWarningThreshold_Type()
)
jnxDomCurrentModuleTemperatureLowWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentModuleTemperatureLowWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentModuleTemperatureLowWarningThreshold.setUnits("Celsius (degrees C)")
_JnxDomCurrentModuleVoltage_Type = Integer32
_JnxDomCurrentModuleVoltage_Object = MibTableColumn
jnxDomCurrentModuleVoltage = _JnxDomCurrentModuleVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 25),
    _JnxDomCurrentModuleVoltage_Type()
)
jnxDomCurrentModuleVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentModuleVoltage.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentModuleVoltage.setUnits("0.001 V")
_JnxDomCurrentModuleVoltageHighAlarmThreshold_Type = Integer32
_JnxDomCurrentModuleVoltageHighAlarmThreshold_Object = MibTableColumn
jnxDomCurrentModuleVoltageHighAlarmThreshold = _JnxDomCurrentModuleVoltageHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 26),
    _JnxDomCurrentModuleVoltageHighAlarmThreshold_Type()
)
jnxDomCurrentModuleVoltageHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentModuleVoltageHighAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentModuleVoltageHighAlarmThreshold.setUnits("0.001 V")
_JnxDomCurrentModuleVoltageLowAlarmThreshold_Type = Integer32
_JnxDomCurrentModuleVoltageLowAlarmThreshold_Object = MibTableColumn
jnxDomCurrentModuleVoltageLowAlarmThreshold = _JnxDomCurrentModuleVoltageLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 27),
    _JnxDomCurrentModuleVoltageLowAlarmThreshold_Type()
)
jnxDomCurrentModuleVoltageLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentModuleVoltageLowAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentModuleVoltageLowAlarmThreshold.setUnits("0.001 V")
_JnxDomCurrentModuleVoltageHighWarningThreshold_Type = Integer32
_JnxDomCurrentModuleVoltageHighWarningThreshold_Object = MibTableColumn
jnxDomCurrentModuleVoltageHighWarningThreshold = _JnxDomCurrentModuleVoltageHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 28),
    _JnxDomCurrentModuleVoltageHighWarningThreshold_Type()
)
jnxDomCurrentModuleVoltageHighWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentModuleVoltageHighWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentModuleVoltageHighWarningThreshold.setUnits("0.001 V")
_JnxDomCurrentModuleVoltageLowWarningThreshold_Type = Integer32
_JnxDomCurrentModuleVoltageLowWarningThreshold_Object = MibTableColumn
jnxDomCurrentModuleVoltageLowWarningThreshold = _JnxDomCurrentModuleVoltageLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 29),
    _JnxDomCurrentModuleVoltageLowWarningThreshold_Type()
)
jnxDomCurrentModuleVoltageLowWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentModuleVoltageLowWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentModuleVoltageLowWarningThreshold.setUnits("0.001 V")
_JnxDomCurrentModuleLaneCount_Type = Integer32
_JnxDomCurrentModuleLaneCount_Object = MibTableColumn
jnxDomCurrentModuleLaneCount = _JnxDomCurrentModuleLaneCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 1, 1, 1, 30),
    _JnxDomCurrentModuleLaneCount_Type()
)
jnxDomCurrentModuleLaneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentModuleLaneCount.setStatus("current")
_JnxDomDigitalLaneMonitoring_ObjectIdentity = ObjectIdentity
jnxDomDigitalLaneMonitoring = _JnxDomDigitalLaneMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 2)
)
_JnxDomModuleLaneTable_Object = MibTable
jnxDomModuleLaneTable = _JnxDomModuleLaneTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxDomModuleLaneTable.setStatus("current")
_JnxDomCurrentLaneEntry_Object = MibTableRow
jnxDomCurrentLaneEntry = _JnxDomCurrentLaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 2, 1, 1)
)
jnxDomCurrentLaneEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-DOM-MIB", "jnxDomLaneIndex"),
)
if mibBuilder.loadTexts:
    jnxDomCurrentLaneEntry.setStatus("current")


class _JnxDomLaneIndex_Type(Integer32):
    """Custom type jnxDomLaneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_JnxDomLaneIndex_Type.__name__ = "Integer32"
_JnxDomLaneIndex_Object = MibTableColumn
jnxDomLaneIndex = _JnxDomLaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 2, 1, 1, 1),
    _JnxDomLaneIndex_Type()
)
jnxDomLaneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomLaneIndex.setStatus("current")
_JnxDomCurrentLaneAlarms_Type = JnxDomLaneAlarmId
_JnxDomCurrentLaneAlarms_Object = MibTableColumn
jnxDomCurrentLaneAlarms = _JnxDomCurrentLaneAlarms_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 2, 1, 1, 2),
    _JnxDomCurrentLaneAlarms_Type()
)
jnxDomCurrentLaneAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentLaneAlarms.setStatus("current")
_JnxDomCurrentLaneAlarmDate_Type = DateAndTime
_JnxDomCurrentLaneAlarmDate_Object = MibTableColumn
jnxDomCurrentLaneAlarmDate = _JnxDomCurrentLaneAlarmDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 2, 1, 1, 3),
    _JnxDomCurrentLaneAlarmDate_Type()
)
jnxDomCurrentLaneAlarmDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentLaneAlarmDate.setStatus("current")
_JnxDomLaneLastAlarms_Type = JnxDomLaneAlarmId
_JnxDomLaneLastAlarms_Object = MibTableColumn
jnxDomLaneLastAlarms = _JnxDomLaneLastAlarms_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 2, 1, 1, 4),
    _JnxDomLaneLastAlarms_Type()
)
jnxDomLaneLastAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomLaneLastAlarms.setStatus("current")
_JnxDomCurrentLaneWarnings_Type = JnxDomLaneWarningId
_JnxDomCurrentLaneWarnings_Object = MibTableColumn
jnxDomCurrentLaneWarnings = _JnxDomCurrentLaneWarnings_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 2, 1, 1, 5),
    _JnxDomCurrentLaneWarnings_Type()
)
jnxDomCurrentLaneWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentLaneWarnings.setStatus("current")
_JnxDomCurrentLaneRxLaserPower_Type = Integer32
_JnxDomCurrentLaneRxLaserPower_Object = MibTableColumn
jnxDomCurrentLaneRxLaserPower = _JnxDomCurrentLaneRxLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 2, 1, 1, 6),
    _JnxDomCurrentLaneRxLaserPower_Type()
)
jnxDomCurrentLaneRxLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentLaneRxLaserPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentLaneRxLaserPower.setUnits("0.01 dbm")
_JnxDomCurrentLaneTxLaserBiasCurrent_Type = Integer32
_JnxDomCurrentLaneTxLaserBiasCurrent_Object = MibTableColumn
jnxDomCurrentLaneTxLaserBiasCurrent = _JnxDomCurrentLaneTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 2, 1, 1, 7),
    _JnxDomCurrentLaneTxLaserBiasCurrent_Type()
)
jnxDomCurrentLaneTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentLaneTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentLaneTxLaserBiasCurrent.setUnits("0.001 mA")
_JnxDomCurrentLaneTxLaserOutputPower_Type = Integer32
_JnxDomCurrentLaneTxLaserOutputPower_Object = MibTableColumn
jnxDomCurrentLaneTxLaserOutputPower = _JnxDomCurrentLaneTxLaserOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 2, 1, 1, 8),
    _JnxDomCurrentLaneTxLaserOutputPower_Type()
)
jnxDomCurrentLaneTxLaserOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentLaneTxLaserOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentLaneTxLaserOutputPower.setUnits("0.01 dbm")
_JnxDomCurrentLaneLaserTemperature_Type = Integer32
_JnxDomCurrentLaneLaserTemperature_Object = MibTableColumn
jnxDomCurrentLaneLaserTemperature = _JnxDomCurrentLaneLaserTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60, 1, 2, 1, 1, 9),
    _JnxDomCurrentLaneLaserTemperature_Type()
)
jnxDomCurrentLaneLaserTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDomCurrentLaneLaserTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxDomCurrentLaneLaserTemperature.setUnits("Celsius (degrees C)")
_JnxDomNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxDomNotificationPrefix = _JnxDomNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 18, 0)
)
_JnxDomLaneNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxDomLaneNotificationPrefix = _JnxDomLaneNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 25, 0)
)

# Managed Objects groups


# Notification objects

jnxDomAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 18, 0, 1)
)
jnxDomAlarmSet.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-DOM-MIB", "jnxDomLastAlarms"),
        ("JUNIPER-DOM-MIB", "jnxDomCurrentAlarms"),
        ("JUNIPER-DOM-MIB", "jnxDomCurrentAlarmDate"))
)
if mibBuilder.loadTexts:
    jnxDomAlarmSet.setStatus(
        "current"
    )

jnxDomAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 18, 0, 2)
)
jnxDomAlarmCleared.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-DOM-MIB", "jnxDomLastAlarms"),
        ("JUNIPER-DOM-MIB", "jnxDomCurrentAlarms"),
        ("JUNIPER-DOM-MIB", "jnxDomCurrentAlarmDate"))
)
if mibBuilder.loadTexts:
    jnxDomAlarmCleared.setStatus(
        "current"
    )

jnxDomLaneAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 25, 0, 1)
)
jnxDomLaneAlarmSet.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-DOM-MIB", "jnxDomLaneIndex"),
        ("JUNIPER-DOM-MIB", "jnxDomLaneLastAlarms"),
        ("JUNIPER-DOM-MIB", "jnxDomCurrentLaneAlarms"),
        ("JUNIPER-DOM-MIB", "jnxDomCurrentLaneAlarmDate"))
)
if mibBuilder.loadTexts:
    jnxDomLaneAlarmSet.setStatus(
        "current"
    )

jnxDomLaneAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 25, 0, 2)
)
jnxDomLaneAlarmCleared.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-DOM-MIB", "jnxDomLaneIndex"),
        ("JUNIPER-DOM-MIB", "jnxDomLaneLastAlarms"),
        ("JUNIPER-DOM-MIB", "jnxDomCurrentLaneAlarms"),
        ("JUNIPER-DOM-MIB", "jnxDomCurrentLaneAlarmDate"))
)
if mibBuilder.loadTexts:
    jnxDomLaneAlarmCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-DOM-MIB",
    **{"JnxDomAlarmId": JnxDomAlarmId,
       "JnxDomWarningId": JnxDomWarningId,
       "JnxDomLaneAlarmId": JnxDomLaneAlarmId,
       "JnxDomLaneWarningId": JnxDomLaneWarningId,
       "jnxDomMib": jnxDomMib,
       "jnxDomDigitalMonitoring": jnxDomDigitalMonitoring,
       "jnxDomCurrentTable": jnxDomCurrentTable,
       "jnxDomCurrentEntry": jnxDomCurrentEntry,
       "jnxDomCurrentAlarms": jnxDomCurrentAlarms,
       "jnxDomCurrentAlarmDate": jnxDomCurrentAlarmDate,
       "jnxDomLastAlarms": jnxDomLastAlarms,
       "jnxDomCurrentWarnings": jnxDomCurrentWarnings,
       "jnxDomCurrentRxLaserPower": jnxDomCurrentRxLaserPower,
       "jnxDomCurrentTxLaserBiasCurrent": jnxDomCurrentTxLaserBiasCurrent,
       "jnxDomCurrentTxLaserOutputPower": jnxDomCurrentTxLaserOutputPower,
       "jnxDomCurrentModuleTemperature": jnxDomCurrentModuleTemperature,
       "jnxDomCurrentRxLaserPowerHighAlarmThreshold": jnxDomCurrentRxLaserPowerHighAlarmThreshold,
       "jnxDomCurrentRxLaserPowerLowAlarmThreshold": jnxDomCurrentRxLaserPowerLowAlarmThreshold,
       "jnxDomCurrentRxLaserPowerHighWarningThreshold": jnxDomCurrentRxLaserPowerHighWarningThreshold,
       "jnxDomCurrentRxLaserPowerLowWarningThreshold": jnxDomCurrentRxLaserPowerLowWarningThreshold,
       "jnxDomCurrentTxLaserBiasCurrentHighAlarmThreshold": jnxDomCurrentTxLaserBiasCurrentHighAlarmThreshold,
       "jnxDomCurrentTxLaserBiasCurrentLowAlarmThreshold": jnxDomCurrentTxLaserBiasCurrentLowAlarmThreshold,
       "jnxDomCurrentTxLaserBiasCurrentHighWarningThreshold": jnxDomCurrentTxLaserBiasCurrentHighWarningThreshold,
       "jnxDomCurrentTxLaserBiasCurrentLowWarningThreshold": jnxDomCurrentTxLaserBiasCurrentLowWarningThreshold,
       "jnxDomCurrentTxLaserOutputPowerHighAlarmThreshold": jnxDomCurrentTxLaserOutputPowerHighAlarmThreshold,
       "jnxDomCurrentTxLaserOutputPowerLowAlarmThreshold": jnxDomCurrentTxLaserOutputPowerLowAlarmThreshold,
       "jnxDomCurrentTxLaserOutputPowerHighWarningThreshold": jnxDomCurrentTxLaserOutputPowerHighWarningThreshold,
       "jnxDomCurrentTxLaserOutputPowerLowWarningThreshold": jnxDomCurrentTxLaserOutputPowerLowWarningThreshold,
       "jnxDomCurrentModuleTemperatureHighAlarmThreshold": jnxDomCurrentModuleTemperatureHighAlarmThreshold,
       "jnxDomCurrentModuleTemperatureLowAlarmThreshold": jnxDomCurrentModuleTemperatureLowAlarmThreshold,
       "jnxDomCurrentModuleTemperatureHighWarningThreshold": jnxDomCurrentModuleTemperatureHighWarningThreshold,
       "jnxDomCurrentModuleTemperatureLowWarningThreshold": jnxDomCurrentModuleTemperatureLowWarningThreshold,
       "jnxDomCurrentModuleVoltage": jnxDomCurrentModuleVoltage,
       "jnxDomCurrentModuleVoltageHighAlarmThreshold": jnxDomCurrentModuleVoltageHighAlarmThreshold,
       "jnxDomCurrentModuleVoltageLowAlarmThreshold": jnxDomCurrentModuleVoltageLowAlarmThreshold,
       "jnxDomCurrentModuleVoltageHighWarningThreshold": jnxDomCurrentModuleVoltageHighWarningThreshold,
       "jnxDomCurrentModuleVoltageLowWarningThreshold": jnxDomCurrentModuleVoltageLowWarningThreshold,
       "jnxDomCurrentModuleLaneCount": jnxDomCurrentModuleLaneCount,
       "jnxDomDigitalLaneMonitoring": jnxDomDigitalLaneMonitoring,
       "jnxDomModuleLaneTable": jnxDomModuleLaneTable,
       "jnxDomCurrentLaneEntry": jnxDomCurrentLaneEntry,
       "jnxDomLaneIndex": jnxDomLaneIndex,
       "jnxDomCurrentLaneAlarms": jnxDomCurrentLaneAlarms,
       "jnxDomCurrentLaneAlarmDate": jnxDomCurrentLaneAlarmDate,
       "jnxDomLaneLastAlarms": jnxDomLaneLastAlarms,
       "jnxDomCurrentLaneWarnings": jnxDomCurrentLaneWarnings,
       "jnxDomCurrentLaneRxLaserPower": jnxDomCurrentLaneRxLaserPower,
       "jnxDomCurrentLaneTxLaserBiasCurrent": jnxDomCurrentLaneTxLaserBiasCurrent,
       "jnxDomCurrentLaneTxLaserOutputPower": jnxDomCurrentLaneTxLaserOutputPower,
       "jnxDomCurrentLaneLaserTemperature": jnxDomCurrentLaneLaserTemperature,
       "jnxDomNotificationPrefix": jnxDomNotificationPrefix,
       "jnxDomAlarmSet": jnxDomAlarmSet,
       "jnxDomAlarmCleared": jnxDomAlarmCleared,
       "jnxDomLaneNotificationPrefix": jnxDomLaneNotificationPrefix,
       "jnxDomLaneAlarmSet": jnxDomLaneAlarmSet,
       "jnxDomLaneAlarmCleared": jnxDomLaneAlarmCleared}
)
