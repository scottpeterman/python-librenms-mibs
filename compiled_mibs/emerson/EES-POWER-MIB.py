# SNMP MIB module (EES-POWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\emerson\EES-POWER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:53 2025
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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

powerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Status(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("normal", 2),
          ("warning", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6),
          ("unmanaged", 7),
          ("restricted", 8),
          ("testing", 9),
          ("disabled", 10))
    )



class StatusChange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("deactivated", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Ees_ObjectIdentity = ObjectIdentity
ees = _Ees_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302)
)
__pysmi_global_ObjectIdentity = ObjectIdentity
_pysmi_global = __pysmi_global_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2)
)
_Ident_ObjectIdentity = ObjectIdentity
ident = _Ident_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 1)
)
_IdentManufacturer_Type = DisplayString
_IdentManufacturer_Object = MibScalar
identManufacturer = _IdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 1, 1),
    _IdentManufacturer_Type()
)
identManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identManufacturer.setStatus("current")
_IdentModel_Type = DisplayString
_IdentModel_Object = MibScalar
identModel = _IdentModel_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 1, 2),
    _IdentModel_Type()
)
identModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identModel.setStatus("current")
_IdentControllerFirmwareVersion_Type = DisplayString
_IdentControllerFirmwareVersion_Object = MibScalar
identControllerFirmwareVersion = _IdentControllerFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 1, 3),
    _IdentControllerFirmwareVersion_Type()
)
identControllerFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identControllerFirmwareVersion.setStatus("current")
_IdentName_Type = DisplayString
_IdentName_Object = MibScalar
identName = _IdentName_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 1, 4),
    _IdentName_Type()
)
identName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identName.setStatus("current")
_IdentSNMPCfgVer_Type = DisplayString
_IdentSNMPCfgVer_Object = MibScalar
identSNMPCfgVer = _IdentSNMPCfgVer_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 1, 5),
    _IdentSNMPCfgVer_Type()
)
identSNMPCfgVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identSNMPCfgVer.setStatus("current")
_IdentControllerSerialNumber_Type = DisplayString
_IdentControllerSerialNumber_Object = MibScalar
identControllerSerialNumber = _IdentControllerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 1, 6),
    _IdentControllerSerialNumber_Type()
)
identControllerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identControllerSerialNumber.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2)
)
_SystemStatus_Type = Status
_SystemStatus_Object = MibScalar
systemStatus = _SystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 1),
    _SystemStatus_Type()
)
systemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatus.setStatus("current")
_SystemVoltage_Type = Integer32
_SystemVoltage_Object = MibScalar
systemVoltage = _SystemVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 2),
    _SystemVoltage_Type()
)
systemVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVoltage.setStatus("current")
_SystemCurrent_Type = Integer32
_SystemCurrent_Object = MibScalar
systemCurrent = _SystemCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 3),
    _SystemCurrent_Type()
)
systemCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCurrent.setStatus("current")
_SystemUsedCapacity_Type = Integer32
_SystemUsedCapacity_Object = MibScalar
systemUsedCapacity = _SystemUsedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 4),
    _SystemUsedCapacity_Type()
)
systemUsedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUsedCapacity.setStatus("current")
_PsBattery_ObjectIdentity = ObjectIdentity
psBattery = _PsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5)
)
_PsBatteryVoltage_Type = Integer32
_PsBatteryVoltage_Object = MibScalar
psBatteryVoltage = _PsBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5, 1),
    _PsBatteryVoltage_Type()
)
psBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryVoltage.setStatus("current")
_PsTotalBatteryCurrent_Type = Integer32
_PsTotalBatteryCurrent_Object = MibScalar
psTotalBatteryCurrent = _PsTotalBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5, 2),
    _PsTotalBatteryCurrent_Type()
)
psTotalBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTotalBatteryCurrent.setStatus("current")
_PsBatteryCapacity_Type = Integer32
_PsBatteryCapacity_Object = MibScalar
psBatteryCapacity = _PsBatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5, 3),
    _PsBatteryCapacity_Type()
)
psBatteryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryCapacity.setStatus("current")
_PsBatteryNominalCapacity_Type = Integer32
_PsBatteryNominalCapacity_Object = MibScalar
psBatteryNominalCapacity = _PsBatteryNominalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5, 4),
    _PsBatteryNominalCapacity_Type()
)
psBatteryNominalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryNominalCapacity.setStatus("current")
_PsBatteryTable_Object = MibTable
psBatteryTable = _PsBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5, 5)
)
if mibBuilder.loadTexts:
    psBatteryTable.setStatus("current")
_PsBatteryEntry_Object = MibTableRow
psBatteryEntry = _PsBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5, 5, 1)
)
psBatteryEntry.setIndexNames(
    (0, "EES-POWER-MIB", "psBatteryIndex"),
)
if mibBuilder.loadTexts:
    psBatteryEntry.setStatus("current")


class _PsBatteryIndex_Type(Integer32):
    """Custom type psBatteryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_PsBatteryIndex_Type.__name__ = "Integer32"
_PsBatteryIndex_Object = MibTableColumn
psBatteryIndex = _PsBatteryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5, 5, 1, 1),
    _PsBatteryIndex_Type()
)
psBatteryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryIndex.setStatus("current")
_PsBatteryCurrent_Type = Integer32
_PsBatteryCurrent_Object = MibTableColumn
psBatteryCurrent = _PsBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5, 5, 1, 2),
    _PsBatteryCurrent_Type()
)
psBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryCurrent.setStatus("current")
_PsBatteryName_Type = DisplayString
_PsBatteryName_Object = MibTableColumn
psBatteryName = _PsBatteryName_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5, 5, 1, 3),
    _PsBatteryName_Type()
)
psBatteryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryName.setStatus("current")
_PsInput_ObjectIdentity = ObjectIdentity
psInput = _PsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 6)
)
_PsInputLineAVoltage_Type = Integer32
_PsInputLineAVoltage_Object = MibScalar
psInputLineAVoltage = _PsInputLineAVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 6, 1),
    _PsInputLineAVoltage_Type()
)
psInputLineAVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psInputLineAVoltage.setStatus("current")
_PsInputLineBVoltage_Type = Integer32
_PsInputLineBVoltage_Object = MibScalar
psInputLineBVoltage = _PsInputLineBVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 6, 2),
    _PsInputLineBVoltage_Type()
)
psInputLineBVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psInputLineBVoltage.setStatus("current")
_PsInputLineCVoltage_Type = Integer32
_PsInputLineCVoltage_Object = MibScalar
psInputLineCVoltage = _PsInputLineCVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 6, 3),
    _PsInputLineCVoltage_Type()
)
psInputLineCVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psInputLineCVoltage.setStatus("current")
_PsTemperature_ObjectIdentity = ObjectIdentity
psTemperature = _PsTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7)
)
_PsTemperature1_Type = Integer32
_PsTemperature1_Object = MibScalar
psTemperature1 = _PsTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7, 1),
    _PsTemperature1_Type()
)
psTemperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTemperature1.setStatus("current")
_PsTemperature2_Type = Integer32
_PsTemperature2_Object = MibScalar
psTemperature2 = _PsTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7, 2),
    _PsTemperature2_Type()
)
psTemperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTemperature2.setStatus("current")
_PsTemperatureTable_Object = MibTable
psTemperatureTable = _PsTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7, 3)
)
if mibBuilder.loadTexts:
    psTemperatureTable.setStatus("current")
_PsTemperatureEntry_Object = MibTableRow
psTemperatureEntry = _PsTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7, 3, 1)
)
psTemperatureEntry.setIndexNames(
    (0, "EES-POWER-MIB", "psTemperatureIndex"),
)
if mibBuilder.loadTexts:
    psTemperatureEntry.setStatus("current")


class _PsTemperatureIndex_Type(Integer32):
    """Custom type psTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 71),
    )


_PsTemperatureIndex_Type.__name__ = "Integer32"
_PsTemperatureIndex_Object = MibTableColumn
psTemperatureIndex = _PsTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7, 3, 1, 1),
    _PsTemperatureIndex_Type()
)
psTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTemperatureIndex.setStatus("current")
_PsTemperatureMeasurement_Type = Integer32
_PsTemperatureMeasurement_Object = MibTableColumn
psTemperatureMeasurement = _PsTemperatureMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7, 3, 1, 2),
    _PsTemperatureMeasurement_Type()
)
psTemperatureMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTemperatureMeasurement.setStatus("current")
_PsTemperatureName_Type = DisplayString
_PsTemperatureName_Object = MibTableColumn
psTemperatureName = _PsTemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7, 3, 1, 3),
    _PsTemperatureName_Type()
)
psTemperatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTemperatureName.setStatus("current")


class _PsTemperatureType_Type(Integer32):
    """Custom type psTemperatureType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ambient", 1),
          ("battery", 2))
    )


_PsTemperatureType_Type.__name__ = "Integer32"
_PsTemperatureType_Object = MibTableColumn
psTemperatureType = _PsTemperatureType_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7, 3, 1, 4),
    _PsTemperatureType_Type()
)
psTemperatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTemperatureType.setStatus("current")


class _PsTemperatureAlarmStatus_Type(Integer32):
    """Custom type psTemperatureAlarmStatus based on Integer32"""
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
        *(("high", 0),
          ("low", 1),
          ("fail", 2),
          ("none", 3))
    )


_PsTemperatureAlarmStatus_Type.__name__ = "Integer32"
_PsTemperatureAlarmStatus_Object = MibTableColumn
psTemperatureAlarmStatus = _PsTemperatureAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7, 3, 1, 5),
    _PsTemperatureAlarmStatus_Type()
)
psTemperatureAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTemperatureAlarmStatus.setStatus("current")


class _PsStatusCommunication_Type(Integer32):
    """Custom type psStatusCommunication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("normal", 2),
          ("interrupt", 3))
    )


_PsStatusCommunication_Type.__name__ = "Integer32"
_PsStatusCommunication_Object = MibScalar
psStatusCommunication = _PsStatusCommunication_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 8),
    _PsStatusCommunication_Type()
)
psStatusCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psStatusCommunication.setStatus("current")


class _PsStatusBatteryMode_Type(Integer32):
    """Custom type psStatusBatteryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("floatCharging", 2),
          ("shortTest", 3),
          ("bcForTest", 4),
          ("manualTesting", 5),
          ("planTesting", 6),
          ("acFailTesting", 7),
          ("acFail", 8),
          ("manualBC", 9),
          ("autoBC", 10),
          ("cyclicBC", 11),
          ("masterBC", 12),
          ("masterBT", 13))
    )


_PsStatusBatteryMode_Type.__name__ = "Integer32"
_PsStatusBatteryMode_Object = MibScalar
psStatusBatteryMode = _PsStatusBatteryMode_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 9),
    _PsStatusBatteryMode_Type()
)
psStatusBatteryMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psStatusBatteryMode.setStatus("current")
_PsSMNumber_ObjectIdentity = ObjectIdentity
psSMNumber = _PsSMNumber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 10)
)
_PsSMACNumber_Type = Integer32
_PsSMACNumber_Object = MibScalar
psSMACNumber = _PsSMACNumber_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 10, 1),
    _PsSMACNumber_Type()
)
psSMACNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMACNumber.setStatus("current")
_PsSMBATNumber_Type = Integer32
_PsSMBATNumber_Object = MibScalar
psSMBATNumber = _PsSMBATNumber_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 10, 2),
    _PsSMBATNumber_Type()
)
psSMBATNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMBATNumber.setStatus("current")
_PsSMIONumber_Type = Integer32
_PsSMIONumber_Object = MibScalar
psSMIONumber = _PsSMIONumber_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 10, 3),
    _PsSMIONumber_Type()
)
psSMIONumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMIONumber.setStatus("current")
_PsRectifier_ObjectIdentity = ObjectIdentity
psRectifier = _PsRectifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11)
)
_NumberOfInstalledRectifiers_Type = Integer32
_NumberOfInstalledRectifiers_Object = MibScalar
numberOfInstalledRectifiers = _NumberOfInstalledRectifiers_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 1),
    _NumberOfInstalledRectifiers_Type()
)
numberOfInstalledRectifiers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfInstalledRectifiers.setStatus("current")
_NumberOfRectifiersCommunicating_Type = Integer32
_NumberOfRectifiersCommunicating_Object = MibScalar
numberOfRectifiersCommunicating = _NumberOfRectifiersCommunicating_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 2),
    _NumberOfRectifiersCommunicating_Type()
)
numberOfRectifiersCommunicating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfRectifiersCommunicating.setStatus("current")
_RectifiersUsedCapacity_Type = Integer32
_RectifiersUsedCapacity_Object = MibScalar
rectifiersUsedCapacity = _RectifiersUsedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 3),
    _RectifiersUsedCapacity_Type()
)
rectifiersUsedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersUsedCapacity.setStatus("current")
_PsRectifierTable_Object = MibTable
psRectifierTable = _PsRectifierTable_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    psRectifierTable.setStatus("current")
_PsRectifierEntry_Object = MibTableRow
psRectifierEntry = _PsRectifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 4, 1)
)
psRectifierEntry.setIndexNames(
    (0, "EES-POWER-MIB", "psRectifierIndex"),
)
if mibBuilder.loadTexts:
    psRectifierEntry.setStatus("current")


class _PsRectifierIndex_Type(Integer32):
    """Custom type psRectifierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_PsRectifierIndex_Type.__name__ = "Integer32"
_PsRectifierIndex_Object = MibTableColumn
psRectifierIndex = _PsRectifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 4, 1, 1),
    _PsRectifierIndex_Type()
)
psRectifierIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRectifierIndex.setStatus("current")
_PsRectifierProductNumber_Type = DisplayString
_PsRectifierProductNumber_Object = MibTableColumn
psRectifierProductNumber = _PsRectifierProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 4, 1, 2),
    _PsRectifierProductNumber_Type()
)
psRectifierProductNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRectifierProductNumber.setStatus("current")
_PsRectifierHWVersion_Type = DisplayString
_PsRectifierHWVersion_Object = MibTableColumn
psRectifierHWVersion = _PsRectifierHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 4, 1, 3),
    _PsRectifierHWVersion_Type()
)
psRectifierHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRectifierHWVersion.setStatus("current")
_PsRectifierSWVersion_Type = DisplayString
_PsRectifierSWVersion_Object = MibTableColumn
psRectifierSWVersion = _PsRectifierSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 4, 1, 4),
    _PsRectifierSWVersion_Type()
)
psRectifierSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRectifierSWVersion.setStatus("current")
_PsRectifierSerialNumber_Type = DisplayString
_PsRectifierSerialNumber_Object = MibTableColumn
psRectifierSerialNumber = _PsRectifierSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 4, 1, 5),
    _PsRectifierSerialNumber_Type()
)
psRectifierSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRectifierSerialNumber.setStatus("current")
_PsRectifierCurrent_Type = Integer32
_PsRectifierCurrent_Object = MibTableColumn
psRectifierCurrent = _PsRectifierCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 4, 1, 6),
    _PsRectifierCurrent_Type()
)
psRectifierCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRectifierCurrent.setStatus("current")
_PsRectifierIdent_Type = DisplayString
_PsRectifierIdent_Object = MibTableColumn
psRectifierIdent = _PsRectifierIdent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 4, 1, 7),
    _PsRectifierIdent_Type()
)
psRectifierIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRectifierIdent.setStatus("current")
_PsRectifierFail_Type = StatusChange
_PsRectifierFail_Object = MibTableColumn
psRectifierFail = _PsRectifierFail_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 4, 1, 8),
    _PsRectifierFail_Type()
)
psRectifierFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRectifierFail.setStatus("current")
_PsDistribution_ObjectIdentity = ObjectIdentity
psDistribution = _PsDistribution_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12)
)
_PsTotalLoadCurrent_Type = Integer32
_PsTotalLoadCurrent_Object = MibScalar
psTotalLoadCurrent = _PsTotalLoadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 1),
    _PsTotalLoadCurrent_Type()
)
psTotalLoadCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTotalLoadCurrent.setStatus("current")
_PsDistributionLoadTable_Object = MibTable
psDistributionLoadTable = _PsDistributionLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 2)
)
if mibBuilder.loadTexts:
    psDistributionLoadTable.setStatus("current")
_PsDistributionLoadEntry_Object = MibTableRow
psDistributionLoadEntry = _PsDistributionLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 2, 1)
)
psDistributionLoadEntry.setIndexNames(
    (0, "EES-POWER-MIB", "psDistributionLoadIndex"),
)
if mibBuilder.loadTexts:
    psDistributionLoadEntry.setStatus("current")


class _PsDistributionLoadIndex_Type(Integer32):
    """Custom type psDistributionLoadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268386303),
    )


_PsDistributionLoadIndex_Type.__name__ = "Integer32"
_PsDistributionLoadIndex_Object = MibTableColumn
psDistributionLoadIndex = _PsDistributionLoadIndex_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 2, 1, 1),
    _PsDistributionLoadIndex_Type()
)
psDistributionLoadIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    psDistributionLoadIndex.setStatus("current")
_PsDistributionLoadCurrent_Type = Integer32
_PsDistributionLoadCurrent_Object = MibTableColumn
psDistributionLoadCurrent = _PsDistributionLoadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 2, 1, 2),
    _PsDistributionLoadCurrent_Type()
)
psDistributionLoadCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDistributionLoadCurrent.setStatus("current")
_PsDistributionLoadName_Type = DisplayString
_PsDistributionLoadName_Object = MibTableColumn
psDistributionLoadName = _PsDistributionLoadName_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 2, 1, 3),
    _PsDistributionLoadName_Type()
)
psDistributionLoadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDistributionLoadName.setStatus("current")
_PsDistributionGeneralTable_Object = MibTable
psDistributionGeneralTable = _PsDistributionGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 3)
)
if mibBuilder.loadTexts:
    psDistributionGeneralTable.setStatus("current")
_PsDistributionGeneralEntry_Object = MibTableRow
psDistributionGeneralEntry = _PsDistributionGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 3, 1)
)
psDistributionGeneralEntry.setIndexNames(
    (0, "EES-POWER-MIB", "psDistributionGeneralIndex"),
)
if mibBuilder.loadTexts:
    psDistributionGeneralEntry.setStatus("current")


class _PsDistributionGeneralIndex_Type(Integer32):
    """Custom type psDistributionGeneralIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268386303),
    )


_PsDistributionGeneralIndex_Type.__name__ = "Integer32"
_PsDistributionGeneralIndex_Object = MibTableColumn
psDistributionGeneralIndex = _PsDistributionGeneralIndex_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 3, 1, 1),
    _PsDistributionGeneralIndex_Type()
)
psDistributionGeneralIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    psDistributionGeneralIndex.setStatus("current")
_PsDistributionGeneralCurrent_Type = Integer32
_PsDistributionGeneralCurrent_Object = MibTableColumn
psDistributionGeneralCurrent = _PsDistributionGeneralCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 3, 1, 2),
    _PsDistributionGeneralCurrent_Type()
)
psDistributionGeneralCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDistributionGeneralCurrent.setStatus("current")
_PsDistributionGeneralName_Type = DisplayString
_PsDistributionGeneralName_Object = MibTableColumn
psDistributionGeneralName = _PsDistributionGeneralName_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 3, 1, 3),
    _PsDistributionGeneralName_Type()
)
psDistributionGeneralName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDistributionGeneralName.setStatus("current")
_PsConverter_ObjectIdentity = ObjectIdentity
psConverter = _PsConverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13)
)
_NumberOfInstalledConverters_Type = Integer32
_NumberOfInstalledConverters_Object = MibScalar
numberOfInstalledConverters = _NumberOfInstalledConverters_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 1),
    _NumberOfInstalledConverters_Type()
)
numberOfInstalledConverters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfInstalledConverters.setStatus("current")
_NumberOfConvertersCommunicating_Type = Integer32
_NumberOfConvertersCommunicating_Object = MibScalar
numberOfConvertersCommunicating = _NumberOfConvertersCommunicating_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 2),
    _NumberOfConvertersCommunicating_Type()
)
numberOfConvertersCommunicating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfConvertersCommunicating.setStatus("current")
_ConvertersUsedCapacity_Type = Integer32
_ConvertersUsedCapacity_Object = MibScalar
convertersUsedCapacity = _ConvertersUsedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 3),
    _ConvertersUsedCapacity_Type()
)
convertersUsedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convertersUsedCapacity.setStatus("current")
_PsConverterVoltage_Type = Integer32
_PsConverterVoltage_Object = MibScalar
psConverterVoltage = _PsConverterVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 4),
    _PsConverterVoltage_Type()
)
psConverterVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psConverterVoltage.setStatus("current")
_PsTotalConverterCurrent_Type = Integer32
_PsTotalConverterCurrent_Object = MibScalar
psTotalConverterCurrent = _PsTotalConverterCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 5),
    _PsTotalConverterCurrent_Type()
)
psTotalConverterCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTotalConverterCurrent.setStatus("current")
_PsConverterTable_Object = MibTable
psConverterTable = _PsConverterTable_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 6)
)
if mibBuilder.loadTexts:
    psConverterTable.setStatus("current")
_PsConverterEntry_Object = MibTableRow
psConverterEntry = _PsConverterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 6, 1)
)
psConverterEntry.setIndexNames(
    (0, "EES-POWER-MIB", "psConverterIndex"),
)
if mibBuilder.loadTexts:
    psConverterEntry.setStatus("current")


class _PsConverterIndex_Type(Integer32):
    """Custom type psConverterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PsConverterIndex_Type.__name__ = "Integer32"
_PsConverterIndex_Object = MibTableColumn
psConverterIndex = _PsConverterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 6, 1, 1),
    _PsConverterIndex_Type()
)
psConverterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psConverterIndex.setStatus("current")
_PsConverterProductNumber_Type = DisplayString
_PsConverterProductNumber_Object = MibTableColumn
psConverterProductNumber = _PsConverterProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 6, 1, 2),
    _PsConverterProductNumber_Type()
)
psConverterProductNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psConverterProductNumber.setStatus("current")
_PsConverterHWVersion_Type = DisplayString
_PsConverterHWVersion_Object = MibTableColumn
psConverterHWVersion = _PsConverterHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 6, 1, 3),
    _PsConverterHWVersion_Type()
)
psConverterHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psConverterHWVersion.setStatus("current")
_PsConverterSWVersion_Type = DisplayString
_PsConverterSWVersion_Object = MibTableColumn
psConverterSWVersion = _PsConverterSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 6, 1, 4),
    _PsConverterSWVersion_Type()
)
psConverterSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psConverterSWVersion.setStatus("current")
_PsConverterSerialNumber_Type = DisplayString
_PsConverterSerialNumber_Object = MibTableColumn
psConverterSerialNumber = _PsConverterSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 6, 1, 5),
    _PsConverterSerialNumber_Type()
)
psConverterSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psConverterSerialNumber.setStatus("current")
_PsConverterCurrent_Type = Integer32
_PsConverterCurrent_Object = MibTableColumn
psConverterCurrent = _PsConverterCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 6, 1, 6),
    _PsConverterCurrent_Type()
)
psConverterCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psConverterCurrent.setStatus("current")
_PsConverterIdent_Type = DisplayString
_PsConverterIdent_Object = MibTableColumn
psConverterIdent = _PsConverterIdent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 6, 1, 7),
    _PsConverterIdent_Type()
)
psConverterIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psConverterIdent.setStatus("current")
_PsConverterFail_Type = StatusChange
_PsConverterFail_Object = MibTableColumn
psConverterFail = _PsConverterFail_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 6, 1, 8),
    _PsConverterFail_Type()
)
psConverterFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psConverterFail.setStatus("current")
_PsControl_ObjectIdentity = ObjectIdentity
psControl = _PsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 14)
)
_ControlBatteryTest_Type = Integer32
_ControlBatteryTest_Object = MibScalar
controlBatteryTest = _ControlBatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 14, 1),
    _ControlBatteryTest_Type()
)
controlBatteryTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlBatteryTest.setStatus("current")
_ControlRelay8_Type = Integer32
_ControlRelay8_Object = MibScalar
controlRelay8 = _ControlRelay8_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 14, 2),
    _ControlRelay8_Type()
)
controlRelay8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlRelay8.setStatus("current")
_ControlRelay7_Type = Integer32
_ControlRelay7_Object = MibScalar
controlRelay7 = _ControlRelay7_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 14, 3),
    _ControlRelay7_Type()
)
controlRelay7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlRelay7.setStatus("current")
_ControlRelay6_Type = Integer32
_ControlRelay6_Object = MibScalar
controlRelay6 = _ControlRelay6_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 14, 4),
    _ControlRelay6_Type()
)
controlRelay6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlRelay6.setStatus("current")
_ControlRelayTest_Type = Integer32
_ControlRelayTest_Object = MibScalar
controlRelayTest = _ControlRelayTest_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 14, 5),
    _ControlRelayTest_Type()
)
controlRelayTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlRelayTest.setStatus("current")
_PsEquipmentSignalTable_Object = MibTable
psEquipmentSignalTable = _PsEquipmentSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 15)
)
if mibBuilder.loadTexts:
    psEquipmentSignalTable.setStatus("current")
_EquipmentSignalTableEntry_Object = MibTableRow
equipmentSignalTableEntry = _EquipmentSignalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 15, 1)
)
equipmentSignalTableEntry.setIndexNames(
    (0, "EES-POWER-MIB", "psEquipmentSignalTableEntryIndex"),
)
if mibBuilder.loadTexts:
    equipmentSignalTableEntry.setStatus("current")


class _PsEquipmentSignalTableEntryIndex_Type(Integer32):
    """Custom type psEquipmentSignalTableEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268386303),
    )


_PsEquipmentSignalTableEntryIndex_Type.__name__ = "Integer32"
_PsEquipmentSignalTableEntryIndex_Object = MibTableColumn
psEquipmentSignalTableEntryIndex = _PsEquipmentSignalTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 15, 1, 1),
    _PsEquipmentSignalTableEntryIndex_Type()
)
psEquipmentSignalTableEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEquipmentSignalTableEntryIndex.setStatus("current")
_PsEquipmentSignalValue_Type = Integer32
_PsEquipmentSignalValue_Object = MibTableColumn
psEquipmentSignalValue = _PsEquipmentSignalValue_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 15, 1, 2),
    _PsEquipmentSignalValue_Type()
)
psEquipmentSignalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEquipmentSignalValue.setStatus("current")
_AlarmLastTrapNo_Type = Counter32
_AlarmLastTrapNo_Object = MibScalar
alarmLastTrapNo = _AlarmLastTrapNo_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 3),
    _AlarmLastTrapNo_Type()
)
alarmLastTrapNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLastTrapNo.setStatus("current")
_AlarmActiveAlarmTable_Object = MibTable
alarmActiveAlarmTable = _AlarmActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4)
)
if mibBuilder.loadTexts:
    alarmActiveAlarmTable.setStatus("current")
_ActiveAlarmEntry_Object = MibTableRow
activeAlarmEntry = _ActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4, 1)
)
activeAlarmEntry.setIndexNames(
    (0, "EES-POWER-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    activeAlarmEntry.setStatus("current")
_AlarmIndex_Type = Counter32
_AlarmIndex_Object = MibTableColumn
alarmIndex = _AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4, 1, 1),
    _AlarmIndex_Type()
)
alarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIndex.setStatus("current")
_AlarmTime_Type = DateAndTime
_AlarmTime_Object = MibTableColumn
alarmTime = _AlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4, 1, 2),
    _AlarmTime_Type()
)
alarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTime.setStatus("current")
_AlarmStatusChange_Type = StatusChange
_AlarmStatusChange_Object = MibTableColumn
alarmStatusChange = _AlarmStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4, 1, 3),
    _AlarmStatusChange_Type()
)
alarmStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatusChange.setStatus("current")
_AlarmSeverity_Type = Status
_AlarmSeverity_Object = MibTableColumn
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4, 1, 4),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")
_AlarmDescription_Type = DisplayString
_AlarmDescription_Object = MibTableColumn
alarmDescription = _AlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4, 1, 5),
    _AlarmDescription_Type()
)
alarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDescription.setStatus("current")
_AlarmType_Type = Integer32
_AlarmType_Object = MibTableColumn
alarmType = _AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4, 1, 6),
    _AlarmType_Type()
)
alarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmType.setStatus("current")
_PowerEvents_ObjectIdentity = ObjectIdentity
powerEvents = _PowerEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 5)
)

# Managed Objects groups


# Notification objects

alarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 5, 1)
)
alarmTrap.setObjects(
      *(("EES-POWER-MIB", "alarmIndex"),
        ("EES-POWER-MIB", "alarmTime"),
        ("EES-POWER-MIB", "alarmStatusChange"),
        ("EES-POWER-MIB", "alarmSeverity"),
        ("EES-POWER-MIB", "alarmDescription"),
        ("EES-POWER-MIB", "alarmType"))
)
if mibBuilder.loadTexts:
    alarmTrap.setStatus(
        "current"
    )

alarmActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 5, 2)
)
alarmActiveTrap.setObjects(
      *(("EES-POWER-MIB", "alarmTime"),
        ("EES-POWER-MIB", "alarmSeverity"),
        ("EES-POWER-MIB", "alarmDescription"),
        ("EES-POWER-MIB", "alarmType"))
)
if mibBuilder.loadTexts:
    alarmActiveTrap.setStatus(
        "current"
    )

alarmCeaseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 5, 3)
)
alarmCeaseTrap.setObjects(
      *(("EES-POWER-MIB", "alarmTime"),
        ("EES-POWER-MIB", "alarmSeverity"),
        ("EES-POWER-MIB", "alarmDescription"),
        ("EES-POWER-MIB", "alarmType"))
)
if mibBuilder.loadTexts:
    alarmCeaseTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EES-POWER-MIB",
    **{"Status": Status,
       "StatusChange": StatusChange,
       "ees": ees,
       "global": _pysmi_global,
       "powerMIB": powerMIB,
       "ident": ident,
       "identManufacturer": identManufacturer,
       "identModel": identModel,
       "identControllerFirmwareVersion": identControllerFirmwareVersion,
       "identName": identName,
       "identSNMPCfgVer": identSNMPCfgVer,
       "identControllerSerialNumber": identControllerSerialNumber,
       "system": system,
       "systemStatus": systemStatus,
       "systemVoltage": systemVoltage,
       "systemCurrent": systemCurrent,
       "systemUsedCapacity": systemUsedCapacity,
       "psBattery": psBattery,
       "psBatteryVoltage": psBatteryVoltage,
       "psTotalBatteryCurrent": psTotalBatteryCurrent,
       "psBatteryCapacity": psBatteryCapacity,
       "psBatteryNominalCapacity": psBatteryNominalCapacity,
       "psBatteryTable": psBatteryTable,
       "psBatteryEntry": psBatteryEntry,
       "psBatteryIndex": psBatteryIndex,
       "psBatteryCurrent": psBatteryCurrent,
       "psBatteryName": psBatteryName,
       "psInput": psInput,
       "psInputLineAVoltage": psInputLineAVoltage,
       "psInputLineBVoltage": psInputLineBVoltage,
       "psInputLineCVoltage": psInputLineCVoltage,
       "psTemperature": psTemperature,
       "psTemperature1": psTemperature1,
       "psTemperature2": psTemperature2,
       "psTemperatureTable": psTemperatureTable,
       "psTemperatureEntry": psTemperatureEntry,
       "psTemperatureIndex": psTemperatureIndex,
       "psTemperatureMeasurement": psTemperatureMeasurement,
       "psTemperatureName": psTemperatureName,
       "psTemperatureType": psTemperatureType,
       "psTemperatureAlarmStatus": psTemperatureAlarmStatus,
       "psStatusCommunication": psStatusCommunication,
       "psStatusBatteryMode": psStatusBatteryMode,
       "psSMNumber": psSMNumber,
       "psSMACNumber": psSMACNumber,
       "psSMBATNumber": psSMBATNumber,
       "psSMIONumber": psSMIONumber,
       "psRectifier": psRectifier,
       "numberOfInstalledRectifiers": numberOfInstalledRectifiers,
       "numberOfRectifiersCommunicating": numberOfRectifiersCommunicating,
       "rectifiersUsedCapacity": rectifiersUsedCapacity,
       "psRectifierTable": psRectifierTable,
       "psRectifierEntry": psRectifierEntry,
       "psRectifierIndex": psRectifierIndex,
       "psRectifierProductNumber": psRectifierProductNumber,
       "psRectifierHWVersion": psRectifierHWVersion,
       "psRectifierSWVersion": psRectifierSWVersion,
       "psRectifierSerialNumber": psRectifierSerialNumber,
       "psRectifierCurrent": psRectifierCurrent,
       "psRectifierIdent": psRectifierIdent,
       "psRectifierFail": psRectifierFail,
       "psDistribution": psDistribution,
       "psTotalLoadCurrent": psTotalLoadCurrent,
       "psDistributionLoadTable": psDistributionLoadTable,
       "psDistributionLoadEntry": psDistributionLoadEntry,
       "psDistributionLoadIndex": psDistributionLoadIndex,
       "psDistributionLoadCurrent": psDistributionLoadCurrent,
       "psDistributionLoadName": psDistributionLoadName,
       "psDistributionGeneralTable": psDistributionGeneralTable,
       "psDistributionGeneralEntry": psDistributionGeneralEntry,
       "psDistributionGeneralIndex": psDistributionGeneralIndex,
       "psDistributionGeneralCurrent": psDistributionGeneralCurrent,
       "psDistributionGeneralName": psDistributionGeneralName,
       "psConverter": psConverter,
       "numberOfInstalledConverters": numberOfInstalledConverters,
       "numberOfConvertersCommunicating": numberOfConvertersCommunicating,
       "convertersUsedCapacity": convertersUsedCapacity,
       "psConverterVoltage": psConverterVoltage,
       "psTotalConverterCurrent": psTotalConverterCurrent,
       "psConverterTable": psConverterTable,
       "psConverterEntry": psConverterEntry,
       "psConverterIndex": psConverterIndex,
       "psConverterProductNumber": psConverterProductNumber,
       "psConverterHWVersion": psConverterHWVersion,
       "psConverterSWVersion": psConverterSWVersion,
       "psConverterSerialNumber": psConverterSerialNumber,
       "psConverterCurrent": psConverterCurrent,
       "psConverterIdent": psConverterIdent,
       "psConverterFail": psConverterFail,
       "psControl": psControl,
       "controlBatteryTest": controlBatteryTest,
       "controlRelay8": controlRelay8,
       "controlRelay7": controlRelay7,
       "controlRelay6": controlRelay6,
       "controlRelayTest": controlRelayTest,
       "psEquipmentSignalTable": psEquipmentSignalTable,
       "equipmentSignalTableEntry": equipmentSignalTableEntry,
       "psEquipmentSignalTableEntryIndex": psEquipmentSignalTableEntryIndex,
       "psEquipmentSignalValue": psEquipmentSignalValue,
       "alarmLastTrapNo": alarmLastTrapNo,
       "alarmActiveAlarmTable": alarmActiveAlarmTable,
       "activeAlarmEntry": activeAlarmEntry,
       "alarmIndex": alarmIndex,
       "alarmTime": alarmTime,
       "alarmStatusChange": alarmStatusChange,
       "alarmSeverity": alarmSeverity,
       "alarmDescription": alarmDescription,
       "alarmType": alarmType,
       "powerEvents": powerEvents,
       "alarmTrap": alarmTrap,
       "alarmActiveTrap": alarmActiveTrap,
       "alarmCeaseTrap": alarmCeaseTrap}
)
