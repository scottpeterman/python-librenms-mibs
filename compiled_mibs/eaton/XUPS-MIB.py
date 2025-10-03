# SNMP MIB module (XUPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\eaton\XUPS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:41 2025
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

(xupsContactDescr,
 xupsContactIndex,
 xupsContactState,
 xupsContactType,
 xupsEnvRemoteHumidity,
 xupsEnvRemoteHumidityLowerLimit,
 xupsEnvRemoteHumidityUpperLimit,
 xupsEnvRemoteTemp,
 xupsEnvRemoteTempLowerLimit,
 xupsEnvRemoteTempUpperLimit) = mibBuilder.importSymbols(
    "EATON-EMP-MIB",
    "xupsContactDescr",
    "xupsContactIndex",
    "xupsContactState",
    "xupsContactType",
    "xupsEnvRemoteHumidity",
    "xupsEnvRemoteHumidityLowerLimit",
    "xupsEnvRemoteHumidityUpperLimit",
    "xupsEnvRemoteTemp",
    "xupsEnvRemoteTempLowerLimit",
    "xupsEnvRemoteTempUpperLimit")

(eaton,
 xupsEnvironment) = mibBuilder.importSymbols(
    "EATON-OIDS",
    "eaton",
    "xupsEnvironment")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

xupsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1)
)
if mibBuilder.loadTexts:
    xupsMIB.setRevisions(
        ("2019-09-27 00:00",
         "2019-09-12 00:00",
         "2019-09-10 00:00",
         "2019-04-12 00:00",
         "2019-03-05 00:00",
         "2019-02-19 00:00",
         "2018-09-12 00:00",
         "2018-04-23 00:00",
         "2012-11-26 15:13",
         "2012-04-03 00:00",
         "2011-02-25 00:00",
         "2008-10-02 00:00",
         "2007-05-03 00:00",
         "2007-03-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XupsIdent_ObjectIdentity = ObjectIdentity
xupsIdent = _XupsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 1)
)


class _XupsIdentManufacturer_Type(DisplayString):
    """Custom type xupsIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XupsIdentManufacturer_Type.__name__ = "DisplayString"
_XupsIdentManufacturer_Object = MibScalar
xupsIdentManufacturer = _XupsIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 1, 1),
    _XupsIdentManufacturer_Type()
)
xupsIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsIdentManufacturer.setStatus("current")


class _XupsIdentModel_Type(DisplayString):
    """Custom type xupsIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_XupsIdentModel_Type.__name__ = "DisplayString"
_XupsIdentModel_Object = MibScalar
xupsIdentModel = _XupsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 1, 2),
    _XupsIdentModel_Type()
)
xupsIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsIdentModel.setStatus("current")


class _XupsIdentSoftwareVersion_Type(DisplayString):
    """Custom type xupsIdentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_XupsIdentSoftwareVersion_Type.__name__ = "DisplayString"
_XupsIdentSoftwareVersion_Object = MibScalar
xupsIdentSoftwareVersion = _XupsIdentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 1, 3),
    _XupsIdentSoftwareVersion_Type()
)
xupsIdentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsIdentSoftwareVersion.setStatus("current")


class _XupsIdentOemCode_Type(Integer32):
    """Custom type xupsIdentOemCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_XupsIdentOemCode_Type.__name__ = "Integer32"
_XupsIdentOemCode_Object = MibScalar
xupsIdentOemCode = _XupsIdentOemCode_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 1, 4),
    _XupsIdentOemCode_Type()
)
xupsIdentOemCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsIdentOemCode.setStatus("current")


class _XupsIdentPartNumber_Type(OctetString):
    """Custom type xupsIdentPartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_XupsIdentPartNumber_Type.__name__ = "OctetString"
_XupsIdentPartNumber_Object = MibScalar
xupsIdentPartNumber = _XupsIdentPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 1, 5),
    _XupsIdentPartNumber_Type()
)
xupsIdentPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsIdentPartNumber.setStatus("current")


class _XupsIdentSerialNumber_Type(OctetString):
    """Custom type xupsIdentSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_XupsIdentSerialNumber_Type.__name__ = "OctetString"
_XupsIdentSerialNumber_Object = MibScalar
xupsIdentSerialNumber = _XupsIdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 1, 6),
    _XupsIdentSerialNumber_Type()
)
xupsIdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsIdentSerialNumber.setStatus("current")
_XupsBattery_ObjectIdentity = ObjectIdentity
xupsBattery = _XupsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 2)
)


class _XupsBatTimeRemaining_Type(Integer32):
    """Custom type xupsBatTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsBatTimeRemaining_Type.__name__ = "Integer32"
_XupsBatTimeRemaining_Object = MibScalar
xupsBatTimeRemaining = _XupsBatTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 2, 1),
    _XupsBatTimeRemaining_Type()
)
xupsBatTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBatTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    xupsBatTimeRemaining.setUnits("seconds")


class _XupsBatVoltage_Type(Integer32):
    """Custom type xupsBatVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsBatVoltage_Type.__name__ = "Integer32"
_XupsBatVoltage_Object = MibScalar
xupsBatVoltage = _XupsBatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 2, 2),
    _XupsBatVoltage_Type()
)
xupsBatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBatVoltage.setStatus("current")
if mibBuilder.loadTexts:
    xupsBatVoltage.setUnits("Volts DC")


class _XupsBatCurrent_Type(Integer32):
    """Custom type xupsBatCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_XupsBatCurrent_Type.__name__ = "Integer32"
_XupsBatCurrent_Object = MibScalar
xupsBatCurrent = _XupsBatCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 2, 3),
    _XupsBatCurrent_Type()
)
xupsBatCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBatCurrent.setStatus("current")
if mibBuilder.loadTexts:
    xupsBatCurrent.setUnits("Amps DC")


class _XupsBatCapacity_Type(Integer32):
    """Custom type xupsBatCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XupsBatCapacity_Type.__name__ = "Integer32"
_XupsBatCapacity_Object = MibScalar
xupsBatCapacity = _XupsBatCapacity_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 2, 4),
    _XupsBatCapacity_Type()
)
xupsBatCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBatCapacity.setStatus("current")
if mibBuilder.loadTexts:
    xupsBatCapacity.setUnits("percent")


class _XupsBatteryAbmStatus_Type(Integer32):
    """Custom type xupsBatteryAbmStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("batteryCharging", 1),
          ("batteryDischarging", 2),
          ("batteryFloating", 3),
          ("batteryResting", 4),
          ("unknown", 5),
          ("batteryDisconnected", 6),
          ("batteryUnderTest", 7),
          ("checkBattery", 8))
    )


_XupsBatteryAbmStatus_Type.__name__ = "Integer32"
_XupsBatteryAbmStatus_Object = MibScalar
xupsBatteryAbmStatus = _XupsBatteryAbmStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 2, 5),
    _XupsBatteryAbmStatus_Type()
)
xupsBatteryAbmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBatteryAbmStatus.setStatus("current")


class _XupsBatteryLastReplacedDate_Type(DisplayString):
    """Custom type xupsBatteryLastReplacedDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_XupsBatteryLastReplacedDate_Type.__name__ = "DisplayString"
_XupsBatteryLastReplacedDate_Object = MibScalar
xupsBatteryLastReplacedDate = _XupsBatteryLastReplacedDate_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 2, 6),
    _XupsBatteryLastReplacedDate_Type()
)
xupsBatteryLastReplacedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBatteryLastReplacedDate.setStatus("current")


class _XupsBatteryFailure_Type(Integer32):
    """Custom type xupsBatteryFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_XupsBatteryFailure_Type.__name__ = "Integer32"
_XupsBatteryFailure_Object = MibScalar
xupsBatteryFailure = _XupsBatteryFailure_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 2, 7),
    _XupsBatteryFailure_Type()
)
xupsBatteryFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBatteryFailure.setStatus("current")


class _XupsBatteryNotPresent_Type(Integer32):
    """Custom type xupsBatteryNotPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_XupsBatteryNotPresent_Type.__name__ = "Integer32"
_XupsBatteryNotPresent_Object = MibScalar
xupsBatteryNotPresent = _XupsBatteryNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 2, 8),
    _XupsBatteryNotPresent_Type()
)
xupsBatteryNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBatteryNotPresent.setStatus("current")


class _XupsBatteryAged_Type(Integer32):
    """Custom type xupsBatteryAged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_XupsBatteryAged_Type.__name__ = "Integer32"
_XupsBatteryAged_Object = MibScalar
xupsBatteryAged = _XupsBatteryAged_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 2, 9),
    _XupsBatteryAged_Type()
)
xupsBatteryAged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBatteryAged.setStatus("current")


class _XupsBatteryLowCapacity_Type(Integer32):
    """Custom type xupsBatteryLowCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_XupsBatteryLowCapacity_Type.__name__ = "Integer32"
_XupsBatteryLowCapacity_Object = MibScalar
xupsBatteryLowCapacity = _XupsBatteryLowCapacity_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 2, 10),
    _XupsBatteryLowCapacity_Type()
)
xupsBatteryLowCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBatteryLowCapacity.setStatus("current")
_XupsInput_ObjectIdentity = ObjectIdentity
xupsInput = _XupsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 3)
)


class _XupsInputFrequency_Type(Integer32):
    """Custom type xupsInputFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsInputFrequency_Type.__name__ = "Integer32"
_XupsInputFrequency_Object = MibScalar
xupsInputFrequency = _XupsInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 1),
    _XupsInputFrequency_Type()
)
xupsInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    xupsInputFrequency.setUnits("0.1 Hertz")
_XupsInputLineBads_Type = Counter32
_XupsInputLineBads_Object = MibScalar
xupsInputLineBads = _XupsInputLineBads_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 2),
    _XupsInputLineBads_Type()
)
xupsInputLineBads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputLineBads.setStatus("current")


class _XupsInputNumPhases_Type(Integer32):
    """Custom type xupsInputNumPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_XupsInputNumPhases_Type.__name__ = "Integer32"
_XupsInputNumPhases_Object = MibScalar
xupsInputNumPhases = _XupsInputNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 3),
    _XupsInputNumPhases_Type()
)
xupsInputNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputNumPhases.setStatus("current")
_XupsInputTable_Object = MibTable
xupsInputTable = _XupsInputTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 4)
)
if mibBuilder.loadTexts:
    xupsInputTable.setStatus("current")
_XupsInputEntry_Object = MibTableRow
xupsInputEntry = _XupsInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 4, 1)
)
xupsInputEntry.setIndexNames(
    (0, "XUPS-MIB", "xupsInputPhase"),
)
if mibBuilder.loadTexts:
    xupsInputEntry.setStatus("current")


class _XupsInputPhase_Type(Integer32):
    """Custom type xupsInputPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_XupsInputPhase_Type.__name__ = "Integer32"
_XupsInputPhase_Object = MibTableColumn
xupsInputPhase = _XupsInputPhase_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 4, 1, 1),
    _XupsInputPhase_Type()
)
xupsInputPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputPhase.setStatus("current")


class _XupsInputVoltage_Type(Integer32):
    """Custom type xupsInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsInputVoltage_Type.__name__ = "Integer32"
_XupsInputVoltage_Object = MibTableColumn
xupsInputVoltage = _XupsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 4, 1, 2),
    _XupsInputVoltage_Type()
)
xupsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    xupsInputVoltage.setUnits("RMS Volts")


class _XupsInputCurrent_Type(Integer32):
    """Custom type xupsInputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsInputCurrent_Type.__name__ = "Integer32"
_XupsInputCurrent_Object = MibTableColumn
xupsInputCurrent = _XupsInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 4, 1, 3),
    _XupsInputCurrent_Type()
)
xupsInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    xupsInputCurrent.setUnits("RMS Amps")


class _XupsInputWatts_Type(Integer32):
    """Custom type xupsInputWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsInputWatts_Type.__name__ = "Integer32"
_XupsInputWatts_Object = MibTableColumn
xupsInputWatts = _XupsInputWatts_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 4, 1, 4),
    _XupsInputWatts_Type()
)
xupsInputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputWatts.setStatus("current")
if mibBuilder.loadTexts:
    xupsInputWatts.setUnits("Watts")


class _XupsInputId_Type(Integer32):
    """Custom type xupsInputId based on Integer32"""
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
        *(("phase1toN", 1),
          ("phase2toN", 2),
          ("phase3toN", 3),
          ("phase1to2", 4),
          ("phase2to3", 5),
          ("phase3to1", 6))
    )


_XupsInputId_Type.__name__ = "Integer32"
_XupsInputId_Object = MibTableColumn
xupsInputId = _XupsInputId_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 4, 1, 5),
    _XupsInputId_Type()
)
xupsInputId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputId.setStatus("current")


class _XupsInputName_Type(OctetString):
    """Custom type xupsInputName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_XupsInputName_Type.__name__ = "OctetString"
_XupsInputName_Object = MibTableColumn
xupsInputName = _XupsInputName_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 4, 1, 6),
    _XupsInputName_Type()
)
xupsInputName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputName.setStatus("current")


class _XupsInputCurrentHighPrecision_Type(Integer32):
    """Custom type xupsInputCurrentHighPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsInputCurrentHighPrecision_Type.__name__ = "Integer32"
_XupsInputCurrentHighPrecision_Object = MibTableColumn
xupsInputCurrentHighPrecision = _XupsInputCurrentHighPrecision_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 4, 1, 7),
    _XupsInputCurrentHighPrecision_Type()
)
xupsInputCurrentHighPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputCurrentHighPrecision.setStatus("current")
if mibBuilder.loadTexts:
    xupsInputCurrentHighPrecision.setUnits("RMS tenth of Amps")


class _XupsInputSource_Type(Integer32):
    """Custom type xupsInputSource based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("none", 2),
          ("primaryUtility", 3),
          ("bypassFeed", 4),
          ("secondaryUtility", 5),
          ("generator", 6),
          ("flywheel", 7),
          ("fuelcell", 8))
    )


_XupsInputSource_Type.__name__ = "Integer32"
_XupsInputSource_Object = MibScalar
xupsInputSource = _XupsInputSource_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 5),
    _XupsInputSource_Type()
)
xupsInputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputSource.setStatus("current")


class _XupsDualInputStatus_Type(Integer32):
    """Custom type xupsDualInputStatus based on Integer32"""
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
        *(("bothSourcesBad", 1),
          ("primarySourceGood", 2),
          ("secondarySourceGood", 3),
          ("bothSourcesGood", 4))
    )


_XupsDualInputStatus_Type.__name__ = "Integer32"
_XupsDualInputStatus_Object = MibScalar
xupsDualInputStatus = _XupsDualInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 6),
    _XupsDualInputStatus_Type()
)
xupsDualInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsDualInputStatus.setStatus("current")


class _XupsSecondaryInputWatch_Type(Integer32):
    """Custom type xupsSecondaryInputWatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_XupsSecondaryInputWatch_Type.__name__ = "Integer32"
_XupsSecondaryInputWatch_Object = MibScalar
xupsSecondaryInputWatch = _XupsSecondaryInputWatch_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 7),
    _XupsSecondaryInputWatch_Type()
)
xupsSecondaryInputWatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsSecondaryInputWatch.setStatus("current")
_XupsInputTotal_ObjectIdentity = ObjectIdentity
xupsInputTotal = _XupsInputTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 8)
)


class _XupsInputAverageVoltage_Type(Integer32):
    """Custom type xupsInputAverageVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsInputAverageVoltage_Type.__name__ = "Integer32"
_XupsInputAverageVoltage_Object = MibScalar
xupsInputAverageVoltage = _XupsInputAverageVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 8, 1),
    _XupsInputAverageVoltage_Type()
)
xupsInputAverageVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputAverageVoltage.setStatus("current")
if mibBuilder.loadTexts:
    xupsInputAverageVoltage.setUnits("RMS Volts")


class _XupsInputTotalCurrent_Type(Integer32):
    """Custom type xupsInputTotalCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsInputTotalCurrent_Type.__name__ = "Integer32"
_XupsInputTotalCurrent_Object = MibScalar
xupsInputTotalCurrent = _XupsInputTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 8, 2),
    _XupsInputTotalCurrent_Type()
)
xupsInputTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputTotalCurrent.setStatus("current")
if mibBuilder.loadTexts:
    xupsInputTotalCurrent.setUnits("RMS tenth of Amps")


class _XupsInputTotalWatts_Type(Integer32):
    """Custom type xupsInputTotalWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsInputTotalWatts_Type.__name__ = "Integer32"
_XupsInputTotalWatts_Object = MibScalar
xupsInputTotalWatts = _XupsInputTotalWatts_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 8, 3),
    _XupsInputTotalWatts_Type()
)
xupsInputTotalWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputTotalWatts.setStatus("current")
if mibBuilder.loadTexts:
    xupsInputTotalWatts.setUnits("Watts")


class _XupsInputTotalVA_Type(Integer32):
    """Custom type xupsInputTotalVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsInputTotalVA_Type.__name__ = "Integer32"
_XupsInputTotalVA_Object = MibScalar
xupsInputTotalVA = _XupsInputTotalVA_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 8, 4),
    _XupsInputTotalVA_Type()
)
xupsInputTotalVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputTotalVA.setStatus("current")
if mibBuilder.loadTexts:
    xupsInputTotalVA.setUnits("VA")
_XupsInputAveragePowerFactor_Type = Integer32
_XupsInputAveragePowerFactor_Object = MibScalar
xupsInputAveragePowerFactor = _XupsInputAveragePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 8, 5),
    _XupsInputAveragePowerFactor_Type()
)
xupsInputAveragePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputAveragePowerFactor.setStatus("current")


class _XupsInputStatus_Type(Integer32):
    """Custom type xupsInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inputBad", 1),
          ("inputGood", 2))
    )


_XupsInputStatus_Type.__name__ = "Integer32"
_XupsInputStatus_Object = MibScalar
xupsInputStatus = _XupsInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 9),
    _XupsInputStatus_Type()
)
xupsInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputStatus.setStatus("current")
_XupsOutput_ObjectIdentity = ObjectIdentity
xupsOutput = _XupsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 4)
)


class _XupsOutputLoad_Type(Integer32):
    """Custom type xupsOutputLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_XupsOutputLoad_Type.__name__ = "Integer32"
_XupsOutputLoad_Object = MibScalar
xupsOutputLoad = _XupsOutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 1),
    _XupsOutputLoad_Type()
)
xupsOutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputLoad.setStatus("current")
if mibBuilder.loadTexts:
    xupsOutputLoad.setUnits("percent")


class _XupsOutputFrequency_Type(Integer32):
    """Custom type xupsOutputFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsOutputFrequency_Type.__name__ = "Integer32"
_XupsOutputFrequency_Object = MibScalar
xupsOutputFrequency = _XupsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 2),
    _XupsOutputFrequency_Type()
)
xupsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    xupsOutputFrequency.setUnits("0.1 Hertz")


class _XupsOutputNumPhases_Type(Integer32):
    """Custom type xupsOutputNumPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_XupsOutputNumPhases_Type.__name__ = "Integer32"
_XupsOutputNumPhases_Object = MibScalar
xupsOutputNumPhases = _XupsOutputNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 3),
    _XupsOutputNumPhases_Type()
)
xupsOutputNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputNumPhases.setStatus("current")
_XupsOutputTable_Object = MibTable
xupsOutputTable = _XupsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 4)
)
if mibBuilder.loadTexts:
    xupsOutputTable.setStatus("current")
_XupsOutputEntry_Object = MibTableRow
xupsOutputEntry = _XupsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 4, 1)
)
xupsOutputEntry.setIndexNames(
    (0, "XUPS-MIB", "xupsOutputPhase"),
)
if mibBuilder.loadTexts:
    xupsOutputEntry.setStatus("current")


class _XupsOutputPhase_Type(Integer32):
    """Custom type xupsOutputPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_XupsOutputPhase_Type.__name__ = "Integer32"
_XupsOutputPhase_Object = MibTableColumn
xupsOutputPhase = _XupsOutputPhase_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 4, 1, 1),
    _XupsOutputPhase_Type()
)
xupsOutputPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputPhase.setStatus("current")


class _XupsOutputVoltage_Type(Integer32):
    """Custom type xupsOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsOutputVoltage_Type.__name__ = "Integer32"
_XupsOutputVoltage_Object = MibTableColumn
xupsOutputVoltage = _XupsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 4, 1, 2),
    _XupsOutputVoltage_Type()
)
xupsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    xupsOutputVoltage.setUnits("RMS Volts")


class _XupsOutputCurrent_Type(Integer32):
    """Custom type xupsOutputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsOutputCurrent_Type.__name__ = "Integer32"
_XupsOutputCurrent_Object = MibTableColumn
xupsOutputCurrent = _XupsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 4, 1, 3),
    _XupsOutputCurrent_Type()
)
xupsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    xupsOutputCurrent.setUnits("RMS Amps")


class _XupsOutputWatts_Type(Integer32):
    """Custom type xupsOutputWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsOutputWatts_Type.__name__ = "Integer32"
_XupsOutputWatts_Object = MibTableColumn
xupsOutputWatts = _XupsOutputWatts_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 4, 1, 4),
    _XupsOutputWatts_Type()
)
xupsOutputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputWatts.setStatus("current")
if mibBuilder.loadTexts:
    xupsOutputWatts.setUnits("Watts")


class _XupsOutputId_Type(Integer32):
    """Custom type xupsOutputId based on Integer32"""
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
        *(("phase1toN", 1),
          ("phase2toN", 2),
          ("phase3toN", 3),
          ("phase1to2", 4),
          ("phase2to3", 5),
          ("phase3to1", 6))
    )


_XupsOutputId_Type.__name__ = "Integer32"
_XupsOutputId_Object = MibTableColumn
xupsOutputId = _XupsOutputId_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 4, 1, 5),
    _XupsOutputId_Type()
)
xupsOutputId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputId.setStatus("current")


class _XupsOutputName_Type(OctetString):
    """Custom type xupsOutputName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_XupsOutputName_Type.__name__ = "OctetString"
_XupsOutputName_Object = MibTableColumn
xupsOutputName = _XupsOutputName_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 4, 1, 6),
    _XupsOutputName_Type()
)
xupsOutputName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputName.setStatus("current")


class _XupsOutputCurrentHighPrecision_Type(Integer32):
    """Custom type xupsOutputCurrentHighPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsOutputCurrentHighPrecision_Type.__name__ = "Integer32"
_XupsOutputCurrentHighPrecision_Object = MibTableColumn
xupsOutputCurrentHighPrecision = _XupsOutputCurrentHighPrecision_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 4, 1, 7),
    _XupsOutputCurrentHighPrecision_Type()
)
xupsOutputCurrentHighPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputCurrentHighPrecision.setStatus("current")
if mibBuilder.loadTexts:
    xupsOutputCurrentHighPrecision.setUnits("RMS tenth of Amps")


class _XupsOutputPercentLoad_Type(Integer32):
    """Custom type xupsOutputPercentLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_XupsOutputPercentLoad_Type.__name__ = "Integer32"
_XupsOutputPercentLoad_Object = MibTableColumn
xupsOutputPercentLoad = _XupsOutputPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 4, 1, 8),
    _XupsOutputPercentLoad_Type()
)
xupsOutputPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputPercentLoad.setStatus("current")
if mibBuilder.loadTexts:
    xupsOutputPercentLoad.setUnits("percent")


class _XupsOutputVA_Type(Integer32):
    """Custom type xupsOutputVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsOutputVA_Type.__name__ = "Integer32"
_XupsOutputVA_Object = MibTableColumn
xupsOutputVA = _XupsOutputVA_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 4, 1, 9),
    _XupsOutputVA_Type()
)
xupsOutputVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputVA.setStatus("current")
if mibBuilder.loadTexts:
    xupsOutputVA.setUnits("VA")


class _XupsOutputSource_Type(Integer32):
    """Custom type xupsOutputSource based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("none", 2),
          ("normal", 3),
          ("bypass", 4),
          ("battery", 5),
          ("booster", 6),
          ("reducer", 7),
          ("parallelCapacity", 8),
          ("parallelRedundant", 9),
          ("highEfficiencyMode", 10),
          ("maintenanceBypass", 11),
          ("essMode", 12))
    )


_XupsOutputSource_Type.__name__ = "Integer32"
_XupsOutputSource_Object = MibScalar
xupsOutputSource = _XupsOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 5),
    _XupsOutputSource_Type()
)
xupsOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputSource.setStatus("current")


class _XupsOutputHourlyPowerUsage_Type(Integer32):
    """Custom type xupsOutputHourlyPowerUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsOutputHourlyPowerUsage_Type.__name__ = "Integer32"
_XupsOutputHourlyPowerUsage_Object = MibScalar
xupsOutputHourlyPowerUsage = _XupsOutputHourlyPowerUsage_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 6),
    _XupsOutputHourlyPowerUsage_Type()
)
xupsOutputHourlyPowerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputHourlyPowerUsage.setStatus("current")
if mibBuilder.loadTexts:
    xupsOutputHourlyPowerUsage.setUnits("Wh")


class _XupsOutputCumulativePowerUsage_Type(Integer32):
    """Custom type xupsOutputCumulativePowerUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsOutputCumulativePowerUsage_Type.__name__ = "Integer32"
_XupsOutputCumulativePowerUsage_Object = MibScalar
xupsOutputCumulativePowerUsage = _XupsOutputCumulativePowerUsage_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 7),
    _XupsOutputCumulativePowerUsage_Type()
)
xupsOutputCumulativePowerUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsOutputCumulativePowerUsage.setStatus("current")
if mibBuilder.loadTexts:
    xupsOutputCumulativePowerUsage.setUnits("Wh")
_XupsOutputCumulativePowerUsageTimer_Type = Counter32
_XupsOutputCumulativePowerUsageTimer_Object = MibScalar
xupsOutputCumulativePowerUsageTimer = _XupsOutputCumulativePowerUsageTimer_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 8),
    _XupsOutputCumulativePowerUsageTimer_Type()
)
xupsOutputCumulativePowerUsageTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputCumulativePowerUsageTimer.setStatus("current")
if mibBuilder.loadTexts:
    xupsOutputCumulativePowerUsageTimer.setUnits("Seconds")
_XupsOutputTotal_ObjectIdentity = ObjectIdentity
xupsOutputTotal = _XupsOutputTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 9)
)


class _XupsOutputAverageVoltage_Type(Integer32):
    """Custom type xupsOutputAverageVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsOutputAverageVoltage_Type.__name__ = "Integer32"
_XupsOutputAverageVoltage_Object = MibScalar
xupsOutputAverageVoltage = _XupsOutputAverageVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 9, 1),
    _XupsOutputAverageVoltage_Type()
)
xupsOutputAverageVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputAverageVoltage.setStatus("current")
if mibBuilder.loadTexts:
    xupsOutputAverageVoltage.setUnits("RMS Volts")


class _XupsOutputTotalCurrent_Type(Integer32):
    """Custom type xupsOutputTotalCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsOutputTotalCurrent_Type.__name__ = "Integer32"
_XupsOutputTotalCurrent_Object = MibScalar
xupsOutputTotalCurrent = _XupsOutputTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 9, 2),
    _XupsOutputTotalCurrent_Type()
)
xupsOutputTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputTotalCurrent.setStatus("current")
if mibBuilder.loadTexts:
    xupsOutputTotalCurrent.setUnits("RMS tenth of Amps")


class _XupsOutputTotalWatts_Type(Integer32):
    """Custom type xupsOutputTotalWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsOutputTotalWatts_Type.__name__ = "Integer32"
_XupsOutputTotalWatts_Object = MibScalar
xupsOutputTotalWatts = _XupsOutputTotalWatts_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 9, 3),
    _XupsOutputTotalWatts_Type()
)
xupsOutputTotalWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputTotalWatts.setStatus("current")
if mibBuilder.loadTexts:
    xupsOutputTotalWatts.setUnits("Watts")


class _XupsOutputTotalVA_Type(Integer32):
    """Custom type xupsOutputTotalVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsOutputTotalVA_Type.__name__ = "Integer32"
_XupsOutputTotalVA_Object = MibScalar
xupsOutputTotalVA = _XupsOutputTotalVA_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 9, 4),
    _XupsOutputTotalVA_Type()
)
xupsOutputTotalVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputTotalVA.setStatus("current")
if mibBuilder.loadTexts:
    xupsOutputTotalVA.setUnits("VA")
_XupsOutputAveragePowerFactor_Type = Integer32
_XupsOutputAveragePowerFactor_Object = MibScalar
xupsOutputAveragePowerFactor = _XupsOutputAveragePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 9, 5),
    _XupsOutputAveragePowerFactor_Type()
)
xupsOutputAveragePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputAveragePowerFactor.setStatus("current")


class _XupsOutputStatus_Type(Integer32):
    """Custom type xupsOutputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("outputNotPowered", 1),
          ("outputNotProtected", 2),
          ("outputProtected", 3))
    )


_XupsOutputStatus_Type.__name__ = "Integer32"
_XupsOutputStatus_Object = MibScalar
xupsOutputStatus = _XupsOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 10),
    _XupsOutputStatus_Type()
)
xupsOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputStatus.setStatus("current")
_XupsBypass_ObjectIdentity = ObjectIdentity
xupsBypass = _XupsBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 5)
)


class _XupsBypassFrequency_Type(Integer32):
    """Custom type xupsBypassFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsBypassFrequency_Type.__name__ = "Integer32"
_XupsBypassFrequency_Object = MibScalar
xupsBypassFrequency = _XupsBypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 1),
    _XupsBypassFrequency_Type()
)
xupsBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBypassFrequency.setStatus("current")
if mibBuilder.loadTexts:
    xupsBypassFrequency.setUnits("0.1 Hertz")


class _XupsBypassNumPhases_Type(Integer32):
    """Custom type xupsBypassNumPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_XupsBypassNumPhases_Type.__name__ = "Integer32"
_XupsBypassNumPhases_Object = MibScalar
xupsBypassNumPhases = _XupsBypassNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 2),
    _XupsBypassNumPhases_Type()
)
xupsBypassNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBypassNumPhases.setStatus("current")
_XupsBypassTable_Object = MibTable
xupsBypassTable = _XupsBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 3)
)
if mibBuilder.loadTexts:
    xupsBypassTable.setStatus("current")
_XupsBypassEntry_Object = MibTableRow
xupsBypassEntry = _XupsBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 3, 1)
)
xupsBypassEntry.setIndexNames(
    (0, "XUPS-MIB", "xupsBypassPhase"),
)
if mibBuilder.loadTexts:
    xupsBypassEntry.setStatus("current")


class _XupsBypassPhase_Type(Integer32):
    """Custom type xupsBypassPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_XupsBypassPhase_Type.__name__ = "Integer32"
_XupsBypassPhase_Object = MibTableColumn
xupsBypassPhase = _XupsBypassPhase_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 3, 1, 1),
    _XupsBypassPhase_Type()
)
xupsBypassPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBypassPhase.setStatus("current")


class _XupsBypassVoltage_Type(Integer32):
    """Custom type xupsBypassVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsBypassVoltage_Type.__name__ = "Integer32"
_XupsBypassVoltage_Object = MibTableColumn
xupsBypassVoltage = _XupsBypassVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 3, 1, 2),
    _XupsBypassVoltage_Type()
)
xupsBypassVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBypassVoltage.setStatus("current")
if mibBuilder.loadTexts:
    xupsBypassVoltage.setUnits("RMS Volts")


class _XupsBypassId_Type(Integer32):
    """Custom type xupsBypassId based on Integer32"""
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
        *(("phase1toN", 1),
          ("phase2toN", 2),
          ("phase3toN", 3),
          ("phase1to2", 4),
          ("phase2to3", 5),
          ("phase3to1", 6))
    )


_XupsBypassId_Type.__name__ = "Integer32"
_XupsBypassId_Object = MibTableColumn
xupsBypassId = _XupsBypassId_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 3, 1, 3),
    _XupsBypassId_Type()
)
xupsBypassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBypassId.setStatus("current")


class _XupsBypassName_Type(OctetString):
    """Custom type xupsBypassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_XupsBypassName_Type.__name__ = "OctetString"
_XupsBypassName_Object = MibTableColumn
xupsBypassName = _XupsBypassName_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 3, 1, 4),
    _XupsBypassName_Type()
)
xupsBypassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBypassName.setStatus("current")


class _XupsBypassCurrentHighPrecision_Type(Integer32):
    """Custom type xupsBypassCurrentHighPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsBypassCurrentHighPrecision_Type.__name__ = "Integer32"
_XupsBypassCurrentHighPrecision_Object = MibTableColumn
xupsBypassCurrentHighPrecision = _XupsBypassCurrentHighPrecision_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 3, 1, 5),
    _XupsBypassCurrentHighPrecision_Type()
)
xupsBypassCurrentHighPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBypassCurrentHighPrecision.setStatus("current")
if mibBuilder.loadTexts:
    xupsBypassCurrentHighPrecision.setUnits("RMS tenth of Amps")


class _XupsBypassWatts_Type(Integer32):
    """Custom type xupsBypassWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsBypassWatts_Type.__name__ = "Integer32"
_XupsBypassWatts_Object = MibTableColumn
xupsBypassWatts = _XupsBypassWatts_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 3, 1, 6),
    _XupsBypassWatts_Type()
)
xupsBypassWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBypassWatts.setStatus("current")
if mibBuilder.loadTexts:
    xupsBypassWatts.setUnits("Watts")
_XupsBypassTotal_ObjectIdentity = ObjectIdentity
xupsBypassTotal = _XupsBypassTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 4)
)


class _XupsBypassAverageVoltage_Type(Integer32):
    """Custom type xupsBypassAverageVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsBypassAverageVoltage_Type.__name__ = "Integer32"
_XupsBypassAverageVoltage_Object = MibScalar
xupsBypassAverageVoltage = _XupsBypassAverageVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 4, 1),
    _XupsBypassAverageVoltage_Type()
)
xupsBypassAverageVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBypassAverageVoltage.setStatus("current")
if mibBuilder.loadTexts:
    xupsBypassAverageVoltage.setUnits("RMS Volts")


class _XupsBypassTotalCurrent_Type(Integer32):
    """Custom type xupsBypassTotalCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsBypassTotalCurrent_Type.__name__ = "Integer32"
_XupsBypassTotalCurrent_Object = MibScalar
xupsBypassTotalCurrent = _XupsBypassTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 4, 2),
    _XupsBypassTotalCurrent_Type()
)
xupsBypassTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBypassTotalCurrent.setStatus("current")
if mibBuilder.loadTexts:
    xupsBypassTotalCurrent.setUnits("RMS tenth of Amps")


class _XupsBypassTotalWatts_Type(Integer32):
    """Custom type xupsBypassTotalWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsBypassTotalWatts_Type.__name__ = "Integer32"
_XupsBypassTotalWatts_Object = MibScalar
xupsBypassTotalWatts = _XupsBypassTotalWatts_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 4, 3),
    _XupsBypassTotalWatts_Type()
)
xupsBypassTotalWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBypassTotalWatts.setStatus("current")
if mibBuilder.loadTexts:
    xupsBypassTotalWatts.setUnits("Watts")


class _XupsBypassTotalVA_Type(Integer32):
    """Custom type xupsBypassTotalVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsBypassTotalVA_Type.__name__ = "Integer32"
_XupsBypassTotalVA_Object = MibScalar
xupsBypassTotalVA = _XupsBypassTotalVA_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 4, 4),
    _XupsBypassTotalVA_Type()
)
xupsBypassTotalVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBypassTotalVA.setStatus("current")
if mibBuilder.loadTexts:
    xupsBypassTotalVA.setUnits("VA")
_XupsBypassAveragePowerFactor_Type = Integer32
_XupsBypassAveragePowerFactor_Object = MibScalar
xupsBypassAveragePowerFactor = _XupsBypassAveragePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 4, 5),
    _XupsBypassAveragePowerFactor_Type()
)
xupsBypassAveragePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBypassAveragePowerFactor.setStatus("current")


class _XupsEnvAmbientTemp_Type(Integer32):
    """Custom type xupsEnvAmbientTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_XupsEnvAmbientTemp_Type.__name__ = "Integer32"
_XupsEnvAmbientTemp_Object = MibScalar
xupsEnvAmbientTemp = _XupsEnvAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 1),
    _XupsEnvAmbientTemp_Type()
)
xupsEnvAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsEnvAmbientTemp.setStatus("current")
if mibBuilder.loadTexts:
    xupsEnvAmbientTemp.setUnits("degrees Centigrade")


class _XupsEnvAmbientLowerLimit_Type(Integer32):
    """Custom type xupsEnvAmbientLowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_XupsEnvAmbientLowerLimit_Type.__name__ = "Integer32"
_XupsEnvAmbientLowerLimit_Object = MibScalar
xupsEnvAmbientLowerLimit = _XupsEnvAmbientLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 2),
    _XupsEnvAmbientLowerLimit_Type()
)
xupsEnvAmbientLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsEnvAmbientLowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    xupsEnvAmbientLowerLimit.setUnits("degrees Centigrade")


class _XupsEnvAmbientUpperLimit_Type(Integer32):
    """Custom type xupsEnvAmbientUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_XupsEnvAmbientUpperLimit_Type.__name__ = "Integer32"
_XupsEnvAmbientUpperLimit_Object = MibScalar
xupsEnvAmbientUpperLimit = _XupsEnvAmbientUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 3),
    _XupsEnvAmbientUpperLimit_Type()
)
xupsEnvAmbientUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsEnvAmbientUpperLimit.setStatus("current")
if mibBuilder.loadTexts:
    xupsEnvAmbientUpperLimit.setUnits("degrees Centigrade")


class _XupsEnvAmbientHumidity_Type(Integer32):
    """Custom type xupsEnvAmbientHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XupsEnvAmbientHumidity_Type.__name__ = "Integer32"
_XupsEnvAmbientHumidity_Object = MibScalar
xupsEnvAmbientHumidity = _XupsEnvAmbientHumidity_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 4),
    _XupsEnvAmbientHumidity_Type()
)
xupsEnvAmbientHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsEnvAmbientHumidity.setStatus("current")
if mibBuilder.loadTexts:
    xupsEnvAmbientHumidity.setUnits("percent")
_XupsAlarm_ObjectIdentity = ObjectIdentity
xupsAlarm = _XupsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7)
)
_XupsAlarms_Type = Gauge32
_XupsAlarms_Object = MibScalar
xupsAlarms = _XupsAlarms_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 1),
    _XupsAlarms_Type()
)
xupsAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAlarms.setStatus("current")
_XupsAlarmTable_Object = MibTable
xupsAlarmTable = _XupsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 2)
)
if mibBuilder.loadTexts:
    xupsAlarmTable.setStatus("current")
_XupsAlarmEntry_Object = MibTableRow
xupsAlarmEntry = _XupsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 2, 1)
)
xupsAlarmEntry.setIndexNames(
    (0, "XUPS-MIB", "xupsAlarmID"),
)
if mibBuilder.loadTexts:
    xupsAlarmEntry.setStatus("current")


class _XupsAlarmID_Type(Integer32):
    """Custom type xupsAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_XupsAlarmID_Type.__name__ = "Integer32"
_XupsAlarmID_Object = MibTableColumn
xupsAlarmID = _XupsAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 2, 1, 1),
    _XupsAlarmID_Type()
)
xupsAlarmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAlarmID.setStatus("current")
_XupsAlarmDescr_Type = ObjectIdentifier
_XupsAlarmDescr_Object = MibTableColumn
xupsAlarmDescr = _XupsAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 2, 1, 2),
    _XupsAlarmDescr_Type()
)
xupsAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAlarmDescr.setStatus("current")
_XupsAlarmTime_Type = TimeTicks
_XupsAlarmTime_Object = MibTableColumn
xupsAlarmTime = _XupsAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 2, 1, 3),
    _XupsAlarmTime_Type()
)
xupsAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAlarmTime.setStatus("current")
_XupsOnBattery_ObjectIdentity = ObjectIdentity
xupsOnBattery = _XupsOnBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 3)
)
_XupsLowBattery_ObjectIdentity = ObjectIdentity
xupsLowBattery = _XupsLowBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 4)
)
_XupsUtilityPowerRestored_ObjectIdentity = ObjectIdentity
xupsUtilityPowerRestored = _XupsUtilityPowerRestored_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 5)
)
_XupsReturnFromLowBattery_ObjectIdentity = ObjectIdentity
xupsReturnFromLowBattery = _XupsReturnFromLowBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 6)
)
_XupsOutputOverload_ObjectIdentity = ObjectIdentity
xupsOutputOverload = _XupsOutputOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 7)
)
_XupsInternalFailure_ObjectIdentity = ObjectIdentity
xupsInternalFailure = _XupsInternalFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 8)
)
_XupsBatteryDischarged_ObjectIdentity = ObjectIdentity
xupsBatteryDischarged = _XupsBatteryDischarged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 9)
)
_XupsInverterFailure_ObjectIdentity = ObjectIdentity
xupsInverterFailure = _XupsInverterFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 10)
)
_XupsOnBypass_ObjectIdentity = ObjectIdentity
xupsOnBypass = _XupsOnBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 11)
)
_XupsBypassNotAvailable_ObjectIdentity = ObjectIdentity
xupsBypassNotAvailable = _XupsBypassNotAvailable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 12)
)
_XupsOutputOff_ObjectIdentity = ObjectIdentity
xupsOutputOff = _XupsOutputOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 13)
)
_XupsInputFailure_ObjectIdentity = ObjectIdentity
xupsInputFailure = _XupsInputFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 14)
)
_XupsBuildingAlarm_ObjectIdentity = ObjectIdentity
xupsBuildingAlarm = _XupsBuildingAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 15)
)
_XupsShutdownImminent_ObjectIdentity = ObjectIdentity
xupsShutdownImminent = _XupsShutdownImminent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 16)
)
_XupsOnInverter_ObjectIdentity = ObjectIdentity
xupsOnInverter = _XupsOnInverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 17)
)
_XupsAlarmNumEvents_Type = Gauge32
_XupsAlarmNumEvents_Object = MibScalar
xupsAlarmNumEvents = _XupsAlarmNumEvents_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 18),
    _XupsAlarmNumEvents_Type()
)
xupsAlarmNumEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAlarmNumEvents.setStatus("current")
_XupsAlarmEventTable_Object = MibTable
xupsAlarmEventTable = _XupsAlarmEventTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 19)
)
if mibBuilder.loadTexts:
    xupsAlarmEventTable.setStatus("current")
_XupsAlarmEventEntry_Object = MibTableRow
xupsAlarmEventEntry = _XupsAlarmEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 19, 1)
)
xupsAlarmEventEntry.setIndexNames(
    (0, "XUPS-MIB", "xupsAlarmEventID"),
)
if mibBuilder.loadTexts:
    xupsAlarmEventEntry.setStatus("current")


class _XupsAlarmEventID_Type(Integer32):
    """Custom type xupsAlarmEventID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_XupsAlarmEventID_Type.__name__ = "Integer32"
_XupsAlarmEventID_Object = MibTableColumn
xupsAlarmEventID = _XupsAlarmEventID_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 19, 1, 1),
    _XupsAlarmEventID_Type()
)
xupsAlarmEventID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xupsAlarmEventID.setStatus("current")


class _XupsAlarmEventDateAndTime_Type(DisplayString):
    """Custom type xupsAlarmEventDateAndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_XupsAlarmEventDateAndTime_Type.__name__ = "DisplayString"
_XupsAlarmEventDateAndTime_Object = MibTableColumn
xupsAlarmEventDateAndTime = _XupsAlarmEventDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 19, 1, 2),
    _XupsAlarmEventDateAndTime_Type()
)
xupsAlarmEventDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAlarmEventDateAndTime.setStatus("deprecated")


class _XupsAlarmEventKind_Type(Integer32):
    """Custom type xupsAlarmEventKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("occurred", 1),
          ("cleared", 2),
          ("unknown", 3))
    )


_XupsAlarmEventKind_Type.__name__ = "Integer32"
_XupsAlarmEventKind_Object = MibTableColumn
xupsAlarmEventKind = _XupsAlarmEventKind_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 19, 1, 3),
    _XupsAlarmEventKind_Type()
)
xupsAlarmEventKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAlarmEventKind.setStatus("deprecated")


class _XupsAlarmEventDescr_Type(Integer32):
    """Custom type xupsAlarmEventDescr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsAlarmEventDescr_Type.__name__ = "Integer32"
_XupsAlarmEventDescr_Object = MibTableColumn
xupsAlarmEventDescr = _XupsAlarmEventDescr_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 19, 1, 4),
    _XupsAlarmEventDescr_Type()
)
xupsAlarmEventDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAlarmEventDescr.setStatus("deprecated")


class _XupsAlarmEventMsg_Type(DisplayString):
    """Custom type xupsAlarmEventMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_XupsAlarmEventMsg_Type.__name__ = "DisplayString"
_XupsAlarmEventMsg_Object = MibTableColumn
xupsAlarmEventMsg = _XupsAlarmEventMsg_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 19, 1, 5),
    _XupsAlarmEventMsg_Type()
)
xupsAlarmEventMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAlarmEventMsg.setStatus("current")
_XupsBreakerOpen_ObjectIdentity = ObjectIdentity
xupsBreakerOpen = _XupsBreakerOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 20)
)
_XupsAlarmEntryAdded_ObjectIdentity = ObjectIdentity
xupsAlarmEntryAdded = _XupsAlarmEntryAdded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 21)
)
_XupsAlarmEntryRemoved_ObjectIdentity = ObjectIdentity
xupsAlarmEntryRemoved = _XupsAlarmEntryRemoved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 22)
)
_XupsAlarmBatteryBad_ObjectIdentity = ObjectIdentity
xupsAlarmBatteryBad = _XupsAlarmBatteryBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 23)
)
_XupsOutputOffAsRequested_ObjectIdentity = ObjectIdentity
xupsOutputOffAsRequested = _XupsOutputOffAsRequested_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 24)
)
_XupsDiagnosticTestFailed_ObjectIdentity = ObjectIdentity
xupsDiagnosticTestFailed = _XupsDiagnosticTestFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 25)
)
_XupsCommunicationsLost_ObjectIdentity = ObjectIdentity
xupsCommunicationsLost = _XupsCommunicationsLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 26)
)
_XupsUpsShutdownPending_ObjectIdentity = ObjectIdentity
xupsUpsShutdownPending = _XupsUpsShutdownPending_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 27)
)
_XupsAlarmTestInProgress_ObjectIdentity = ObjectIdentity
xupsAlarmTestInProgress = _XupsAlarmTestInProgress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 28)
)
_XupsAmbientTempBad_ObjectIdentity = ObjectIdentity
xupsAmbientTempBad = _XupsAmbientTempBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 29)
)
_XupsLossOfRedundancy_ObjectIdentity = ObjectIdentity
xupsLossOfRedundancy = _XupsLossOfRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 30)
)
_XupsAlarmTempBad_ObjectIdentity = ObjectIdentity
xupsAlarmTempBad = _XupsAlarmTempBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 31)
)
_XupsAlarmChargerFailed_ObjectIdentity = ObjectIdentity
xupsAlarmChargerFailed = _XupsAlarmChargerFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 32)
)
_XupsAlarmFanFailure_ObjectIdentity = ObjectIdentity
xupsAlarmFanFailure = _XupsAlarmFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 33)
)
_XupsAlarmFuseFailure_ObjectIdentity = ObjectIdentity
xupsAlarmFuseFailure = _XupsAlarmFuseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 34)
)
_XupsPowerSwitchBad_ObjectIdentity = ObjectIdentity
xupsPowerSwitchBad = _XupsPowerSwitchBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 35)
)
_XupsModuleFailure_ObjectIdentity = ObjectIdentity
xupsModuleFailure = _XupsModuleFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 36)
)
_XupsOnAlternatePowerSource_ObjectIdentity = ObjectIdentity
xupsOnAlternatePowerSource = _XupsOnAlternatePowerSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 37)
)
_XupsAltPowerNotAvailable_ObjectIdentity = ObjectIdentity
xupsAltPowerNotAvailable = _XupsAltPowerNotAvailable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 38)
)
_XupsNoticeCondition_ObjectIdentity = ObjectIdentity
xupsNoticeCondition = _XupsNoticeCondition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 39)
)
_XupsRemoteTempBad_ObjectIdentity = ObjectIdentity
xupsRemoteTempBad = _XupsRemoteTempBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 40)
)
_XupsRemoteHumidityBad_ObjectIdentity = ObjectIdentity
xupsRemoteHumidityBad = _XupsRemoteHumidityBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 41)
)
_XupsAlarmOutputBad_ObjectIdentity = ObjectIdentity
xupsAlarmOutputBad = _XupsAlarmOutputBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 42)
)
_XupsAlarmAwaitingPower_ObjectIdentity = ObjectIdentity
xupsAlarmAwaitingPower = _XupsAlarmAwaitingPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 43)
)
_XupsOnMaintenanceBypass_ObjectIdentity = ObjectIdentity
xupsOnMaintenanceBypass = _XupsOnMaintenanceBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 44)
)
_XupsOutputNotProtected_ObjectIdentity = ObjectIdentity
xupsOutputNotProtected = _XupsOutputNotProtected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 51)
)
_XupsTest_ObjectIdentity = ObjectIdentity
xupsTest = _XupsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 8)
)


class _XupsTestStart_Type(Integer32):
    """Custom type xupsTestStart based on Integer32"""
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
        *(("testBattery", 1),
          ("noTestStarted", 2),
          ("testSystem", 3),
          ("testSecondarySource", 4),
          ("flashLightsTest", 5),
          ("cancelTest", 6))
    )


_XupsTestStart_Type.__name__ = "Integer32"
_XupsTestStart_Object = MibScalar
xupsTestStart = _XupsTestStart_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 8, 1),
    _XupsTestStart_Type()
)
xupsTestStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsTestStart.setStatus("current")


class _XupsTestBatteryStatus_Type(Integer32):
    """Custom type xupsTestBatteryStatus based on Integer32"""
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
        *(("unknown", 1),
          ("passed", 2),
          ("failed", 3),
          ("inProgress", 4),
          ("notSupported", 5),
          ("inhibited", 6),
          ("scheduled", 7))
    )


_XupsTestBatteryStatus_Type.__name__ = "Integer32"
_XupsTestBatteryStatus_Object = MibScalar
xupsTestBatteryStatus = _XupsTestBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 8, 2),
    _XupsTestBatteryStatus_Type()
)
xupsTestBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsTestBatteryStatus.setStatus("current")


class _XupsLastGeneralTest_Type(Integer32):
    """Custom type xupsLastGeneralTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noTestStarted", 2),
          ("testSystem", 3),
          ("testSecondarySource", 4),
          ("flashLightsTest", 5))
    )


_XupsLastGeneralTest_Type.__name__ = "Integer32"
_XupsLastGeneralTest_Object = MibScalar
xupsLastGeneralTest = _XupsLastGeneralTest_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 8, 3),
    _XupsLastGeneralTest_Type()
)
xupsLastGeneralTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsLastGeneralTest.setStatus("current")


class _XupsLastGeneralTestResult_Type(Integer32):
    """Custom type xupsLastGeneralTestResult based on Integer32"""
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
        *(("unknown", 1),
          ("passed", 2),
          ("failed", 3),
          ("inProgress", 4),
          ("notSupported", 5),
          ("inhibited", 6),
          ("scheduled", 7))
    )


_XupsLastGeneralTestResult_Type.__name__ = "Integer32"
_XupsLastGeneralTestResult_Object = MibScalar
xupsLastGeneralTestResult = _XupsLastGeneralTestResult_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 8, 4),
    _XupsLastGeneralTestResult_Type()
)
xupsLastGeneralTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsLastGeneralTestResult.setStatus("current")


class _XupsTestTrap_Type(Integer32):
    """Custom type xupsTestTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("startTestTrap", 1)
    )


_XupsTestTrap_Type.__name__ = "Integer32"
_XupsTestTrap_Object = MibScalar
xupsTestTrap = _XupsTestTrap_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 8, 5),
    _XupsTestTrap_Type()
)
xupsTestTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsTestTrap.setStatus("current")
_XupsControl_ObjectIdentity = ObjectIdentity
xupsControl = _XupsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 9)
)


class _XupsControlOutputOffDelay_Type(Integer32):
    """Custom type xupsControlOutputOffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsControlOutputOffDelay_Type.__name__ = "Integer32"
_XupsControlOutputOffDelay_Object = MibScalar
xupsControlOutputOffDelay = _XupsControlOutputOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 9, 1),
    _XupsControlOutputOffDelay_Type()
)
xupsControlOutputOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsControlOutputOffDelay.setStatus("current")
if mibBuilder.loadTexts:
    xupsControlOutputOffDelay.setUnits("seconds")


class _XupsControlOutputOnDelay_Type(Integer32):
    """Custom type xupsControlOutputOnDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsControlOutputOnDelay_Type.__name__ = "Integer32"
_XupsControlOutputOnDelay_Object = MibScalar
xupsControlOutputOnDelay = _XupsControlOutputOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 9, 2),
    _XupsControlOutputOnDelay_Type()
)
xupsControlOutputOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsControlOutputOnDelay.setStatus("current")
if mibBuilder.loadTexts:
    xupsControlOutputOnDelay.setUnits("seconds")


class _XupsControlOutputOffTrapDelay_Type(Integer32):
    """Custom type xupsControlOutputOffTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsControlOutputOffTrapDelay_Type.__name__ = "Integer32"
_XupsControlOutputOffTrapDelay_Object = MibScalar
xupsControlOutputOffTrapDelay = _XupsControlOutputOffTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 9, 3),
    _XupsControlOutputOffTrapDelay_Type()
)
xupsControlOutputOffTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsControlOutputOffTrapDelay.setStatus("current")
if mibBuilder.loadTexts:
    xupsControlOutputOffTrapDelay.setUnits("seconds")


class _XupsControlOutputOnTrapDelay_Type(Integer32):
    """Custom type xupsControlOutputOnTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsControlOutputOnTrapDelay_Type.__name__ = "Integer32"
_XupsControlOutputOnTrapDelay_Object = MibScalar
xupsControlOutputOnTrapDelay = _XupsControlOutputOnTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 9, 4),
    _XupsControlOutputOnTrapDelay_Type()
)
xupsControlOutputOnTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsControlOutputOnTrapDelay.setStatus("deprecated")
if mibBuilder.loadTexts:
    xupsControlOutputOnTrapDelay.setUnits("seconds")


class _XupsControlToBypassDelay_Type(Integer32):
    """Custom type xupsControlToBypassDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsControlToBypassDelay_Type.__name__ = "Integer32"
_XupsControlToBypassDelay_Object = MibScalar
xupsControlToBypassDelay = _XupsControlToBypassDelay_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 9, 5),
    _XupsControlToBypassDelay_Type()
)
xupsControlToBypassDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsControlToBypassDelay.setStatus("current")
if mibBuilder.loadTexts:
    xupsControlToBypassDelay.setUnits("seconds")


class _XupsLoadShedSecsWithRestart_Type(Integer32):
    """Custom type xupsLoadShedSecsWithRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsLoadShedSecsWithRestart_Type.__name__ = "Integer32"
_XupsLoadShedSecsWithRestart_Object = MibScalar
xupsLoadShedSecsWithRestart = _XupsLoadShedSecsWithRestart_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 9, 6),
    _XupsLoadShedSecsWithRestart_Type()
)
xupsLoadShedSecsWithRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsLoadShedSecsWithRestart.setStatus("current")
if mibBuilder.loadTexts:
    xupsLoadShedSecsWithRestart.setUnits("seconds")


class _XupsSwitchable_Type(Integer32):
    """Custom type xupsSwitchable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switchable", 1),
          ("notSwitchable", 2))
    )


_XupsSwitchable_Type.__name__ = "Integer32"
_XupsSwitchable_Object = MibScalar
xupsSwitchable = _XupsSwitchable_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 9, 7),
    _XupsSwitchable_Type()
)
xupsSwitchable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsSwitchable.setStatus("current")
_XupsConfig_ObjectIdentity = ObjectIdentity
xupsConfig = _XupsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 10)
)


class _XupsConfigOutputVoltage_Type(Integer32):
    """Custom type xupsConfigOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsConfigOutputVoltage_Type.__name__ = "Integer32"
_XupsConfigOutputVoltage_Object = MibScalar
xupsConfigOutputVoltage = _XupsConfigOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 10, 1),
    _XupsConfigOutputVoltage_Type()
)
xupsConfigOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsConfigOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    xupsConfigOutputVoltage.setUnits("RMS Volts")


class _XupsConfigInputVoltage_Type(Integer32):
    """Custom type xupsConfigInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsConfigInputVoltage_Type.__name__ = "Integer32"
_XupsConfigInputVoltage_Object = MibScalar
xupsConfigInputVoltage = _XupsConfigInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 10, 2),
    _XupsConfigInputVoltage_Type()
)
xupsConfigInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsConfigInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    xupsConfigInputVoltage.setUnits("RMS Volts")


class _XupsConfigOutputWatts_Type(Integer32):
    """Custom type xupsConfigOutputWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsConfigOutputWatts_Type.__name__ = "Integer32"
_XupsConfigOutputWatts_Object = MibScalar
xupsConfigOutputWatts = _XupsConfigOutputWatts_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 10, 3),
    _XupsConfigOutputWatts_Type()
)
xupsConfigOutputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsConfigOutputWatts.setStatus("current")
if mibBuilder.loadTexts:
    xupsConfigOutputWatts.setUnits("Watts")


class _XupsConfigOutputFreq_Type(Integer32):
    """Custom type xupsConfigOutputFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsConfigOutputFreq_Type.__name__ = "Integer32"
_XupsConfigOutputFreq_Object = MibScalar
xupsConfigOutputFreq = _XupsConfigOutputFreq_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 10, 4),
    _XupsConfigOutputFreq_Type()
)
xupsConfigOutputFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsConfigOutputFreq.setStatus("current")
if mibBuilder.loadTexts:
    xupsConfigOutputFreq.setUnits("0.1 Hertz")


class _XupsConfigDateAndTime_Type(DisplayString):
    """Custom type xupsConfigDateAndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_XupsConfigDateAndTime_Type.__name__ = "DisplayString"
_XupsConfigDateAndTime_Object = MibScalar
xupsConfigDateAndTime = _XupsConfigDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 10, 5),
    _XupsConfigDateAndTime_Type()
)
xupsConfigDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsConfigDateAndTime.setStatus("current")


class _XupsConfigLowOutputVoltageLimit_Type(Integer32):
    """Custom type xupsConfigLowOutputVoltageLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsConfigLowOutputVoltageLimit_Type.__name__ = "Integer32"
_XupsConfigLowOutputVoltageLimit_Object = MibScalar
xupsConfigLowOutputVoltageLimit = _XupsConfigLowOutputVoltageLimit_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 10, 6),
    _XupsConfigLowOutputVoltageLimit_Type()
)
xupsConfigLowOutputVoltageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsConfigLowOutputVoltageLimit.setStatus("current")
if mibBuilder.loadTexts:
    xupsConfigLowOutputVoltageLimit.setUnits("RMS Volts")


class _XupsConfigHighOutputVoltageLimit_Type(Integer32):
    """Custom type xupsConfigHighOutputVoltageLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsConfigHighOutputVoltageLimit_Type.__name__ = "Integer32"
_XupsConfigHighOutputVoltageLimit_Object = MibScalar
xupsConfigHighOutputVoltageLimit = _XupsConfigHighOutputVoltageLimit_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 10, 7),
    _XupsConfigHighOutputVoltageLimit_Type()
)
xupsConfigHighOutputVoltageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsConfigHighOutputVoltageLimit.setStatus("current")
if mibBuilder.loadTexts:
    xupsConfigHighOutputVoltageLimit.setUnits("RMS Volts")


class _XupsConfigInstallDate_Type(DisplayString):
    """Custom type xupsConfigInstallDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_XupsConfigInstallDate_Type.__name__ = "DisplayString"
_XupsConfigInstallDate_Object = MibScalar
xupsConfigInstallDate = _XupsConfigInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 10, 8),
    _XupsConfigInstallDate_Type()
)
xupsConfigInstallDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsConfigInstallDate.setStatus("current")
_XupsTrapControl_ObjectIdentity = ObjectIdentity
xupsTrapControl = _XupsTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 11)
)


class _XupsMaxTrapLevel_Type(Integer32):
    """Custom type xupsMaxTrapLevel based on Integer32"""
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
        *(("none", 1),
          ("critical", 2),
          ("major", 3),
          ("minor", 4),
          ("allTraps", 5))
    )


_XupsMaxTrapLevel_Type.__name__ = "Integer32"
_XupsMaxTrapLevel_Object = MibScalar
xupsMaxTrapLevel = _XupsMaxTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 1),
    _XupsMaxTrapLevel_Type()
)
xupsMaxTrapLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsMaxTrapLevel.setStatus("current")


class _XupsSendTrapType_Type(Integer32):
    """Custom type xupsSendTrapType based on Integer32"""
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
        *(("stnd", 1),
          ("xups", 2),
          ("stndPlus", 3),
          ("xupsPlus", 4),
          ("pxg", 5))
    )


_XupsSendTrapType_Type.__name__ = "Integer32"
_XupsSendTrapType_Object = MibScalar
xupsSendTrapType = _XupsSendTrapType_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 2),
    _XupsSendTrapType_Type()
)
xupsSendTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsSendTrapType.setStatus("current")


class _XupsTrapMessage_Type(DisplayString):
    """Custom type xupsTrapMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_XupsTrapMessage_Type.__name__ = "DisplayString"
_XupsTrapMessage_Object = MibScalar
xupsTrapMessage = _XupsTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 3),
    _XupsTrapMessage_Type()
)
xupsTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsTrapMessage.setStatus("current")
_XupsTrapSource_ObjectIdentity = ObjectIdentity
xupsTrapSource = _XupsTrapSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4)
)
_XupsTrapDefined_ObjectIdentity = ObjectIdentity
xupsTrapDefined = _XupsTrapDefined_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1)
)
_XupsTrapOidDefined_ObjectIdentity = ObjectIdentity
xupsTrapOidDefined = _XupsTrapOidDefined_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0)
)


class _XupsHeartbeatMinsInterval_Type(Integer32):
    """Custom type xupsHeartbeatMinsInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsHeartbeatMinsInterval_Type.__name__ = "Integer32"
_XupsHeartbeatMinsInterval_Object = MibScalar
xupsHeartbeatMinsInterval = _XupsHeartbeatMinsInterval_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 5),
    _XupsHeartbeatMinsInterval_Type()
)
xupsHeartbeatMinsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsHeartbeatMinsInterval.setStatus("current")
if mibBuilder.loadTexts:
    xupsHeartbeatMinsInterval.setUnits("Minutes")
_XupsRecep_ObjectIdentity = ObjectIdentity
xupsRecep = _XupsRecep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 12)
)


class _XupsNumReceptacles_Type(Integer32):
    """Custom type xupsNumReceptacles based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_XupsNumReceptacles_Type.__name__ = "Integer32"
_XupsNumReceptacles_Object = MibScalar
xupsNumReceptacles = _XupsNumReceptacles_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 1),
    _XupsNumReceptacles_Type()
)
xupsNumReceptacles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsNumReceptacles.setStatus("current")
_XupsRecepTable_Object = MibTable
xupsRecepTable = _XupsRecepTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 2)
)
if mibBuilder.loadTexts:
    xupsRecepTable.setStatus("current")
_XupsRecepEntry_Object = MibTableRow
xupsRecepEntry = _XupsRecepEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 2, 1)
)
xupsRecepEntry.setIndexNames(
    (0, "XUPS-MIB", "xupsRecepIndex"),
)
if mibBuilder.loadTexts:
    xupsRecepEntry.setStatus("current")


class _XupsRecepIndex_Type(Integer32):
    """Custom type xupsRecepIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_XupsRecepIndex_Type.__name__ = "Integer32"
_XupsRecepIndex_Object = MibTableColumn
xupsRecepIndex = _XupsRecepIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 2, 1, 1),
    _XupsRecepIndex_Type()
)
xupsRecepIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsRecepIndex.setStatus("current")


class _XupsRecepStatus_Type(Integer32):
    """Custom type xupsRecepStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("pendingOff", 3),
          ("pendingOn", 4),
          ("unknown", 5),
          ("reserved", 6),
          ("failedClosed", 7),
          ("failedOpen", 8))
    )


_XupsRecepStatus_Type.__name__ = "Integer32"
_XupsRecepStatus_Object = MibTableColumn
xupsRecepStatus = _XupsRecepStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 2, 1, 2),
    _XupsRecepStatus_Type()
)
xupsRecepStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsRecepStatus.setStatus("current")


class _XupsRecepOffDelaySecs_Type(Integer32):
    """Custom type xupsRecepOffDelaySecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_XupsRecepOffDelaySecs_Type.__name__ = "Integer32"
_XupsRecepOffDelaySecs_Object = MibTableColumn
xupsRecepOffDelaySecs = _XupsRecepOffDelaySecs_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 2, 1, 3),
    _XupsRecepOffDelaySecs_Type()
)
xupsRecepOffDelaySecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsRecepOffDelaySecs.setStatus("current")
if mibBuilder.loadTexts:
    xupsRecepOffDelaySecs.setUnits("seconds")


class _XupsRecepOnDelaySecs_Type(Integer32):
    """Custom type xupsRecepOnDelaySecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_XupsRecepOnDelaySecs_Type.__name__ = "Integer32"
_XupsRecepOnDelaySecs_Object = MibTableColumn
xupsRecepOnDelaySecs = _XupsRecepOnDelaySecs_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 2, 1, 4),
    _XupsRecepOnDelaySecs_Type()
)
xupsRecepOnDelaySecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsRecepOnDelaySecs.setStatus("current")
if mibBuilder.loadTexts:
    xupsRecepOnDelaySecs.setUnits("seconds")


class _XupsRecepAutoOffDelay_Type(Integer32):
    """Custom type xupsRecepAutoOffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_XupsRecepAutoOffDelay_Type.__name__ = "Integer32"
_XupsRecepAutoOffDelay_Object = MibTableColumn
xupsRecepAutoOffDelay = _XupsRecepAutoOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 2, 1, 5),
    _XupsRecepAutoOffDelay_Type()
)
xupsRecepAutoOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsRecepAutoOffDelay.setStatus("current")
if mibBuilder.loadTexts:
    xupsRecepAutoOffDelay.setUnits("seconds")


class _XupsRecepAutoOnDelay_Type(Integer32):
    """Custom type xupsRecepAutoOnDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_XupsRecepAutoOnDelay_Type.__name__ = "Integer32"
_XupsRecepAutoOnDelay_Object = MibTableColumn
xupsRecepAutoOnDelay = _XupsRecepAutoOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 2, 1, 6),
    _XupsRecepAutoOnDelay_Type()
)
xupsRecepAutoOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsRecepAutoOnDelay.setStatus("current")
if mibBuilder.loadTexts:
    xupsRecepAutoOnDelay.setUnits("seconds")


class _XupsRecepShedSecsWithRestart_Type(Integer32):
    """Custom type xupsRecepShedSecsWithRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsRecepShedSecsWithRestart_Type.__name__ = "Integer32"
_XupsRecepShedSecsWithRestart_Object = MibTableColumn
xupsRecepShedSecsWithRestart = _XupsRecepShedSecsWithRestart_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 2, 1, 7),
    _XupsRecepShedSecsWithRestart_Type()
)
xupsRecepShedSecsWithRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsRecepShedSecsWithRestart.setStatus("current")
if mibBuilder.loadTexts:
    xupsRecepShedSecsWithRestart.setUnits("seconds")


class _XupsRecepHourlyPowerUsage_Type(Integer32):
    """Custom type xupsRecepHourlyPowerUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsRecepHourlyPowerUsage_Type.__name__ = "Integer32"
_XupsRecepHourlyPowerUsage_Object = MibTableColumn
xupsRecepHourlyPowerUsage = _XupsRecepHourlyPowerUsage_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 2, 1, 8),
    _XupsRecepHourlyPowerUsage_Type()
)
xupsRecepHourlyPowerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsRecepHourlyPowerUsage.setStatus("current")
if mibBuilder.loadTexts:
    xupsRecepHourlyPowerUsage.setUnits("Wh")


class _XupsRecepCumulativePowerUsage_Type(Integer32):
    """Custom type xupsRecepCumulativePowerUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsRecepCumulativePowerUsage_Type.__name__ = "Integer32"
_XupsRecepCumulativePowerUsage_Object = MibTableColumn
xupsRecepCumulativePowerUsage = _XupsRecepCumulativePowerUsage_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 2, 1, 9),
    _XupsRecepCumulativePowerUsage_Type()
)
xupsRecepCumulativePowerUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsRecepCumulativePowerUsage.setStatus("current")
if mibBuilder.loadTexts:
    xupsRecepCumulativePowerUsage.setUnits("Wh")
_XupsRecepCumulativePowerUsageTimer_Type = Counter32
_XupsRecepCumulativePowerUsageTimer_Object = MibTableColumn
xupsRecepCumulativePowerUsageTimer = _XupsRecepCumulativePowerUsageTimer_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 2, 1, 10),
    _XupsRecepCumulativePowerUsageTimer_Type()
)
xupsRecepCumulativePowerUsageTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsRecepCumulativePowerUsageTimer.setStatus("current")
if mibBuilder.loadTexts:
    xupsRecepCumulativePowerUsageTimer.setUnits("Seconds")
_XupsTopology_ObjectIdentity = ObjectIdentity
xupsTopology = _XupsTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 13)
)


class _XupsTopologyType_Type(Integer32):
    """Custom type xupsTopologyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_XupsTopologyType_Type.__name__ = "Integer32"
_XupsTopologyType_Object = MibScalar
xupsTopologyType = _XupsTopologyType_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 13, 1),
    _XupsTopologyType_Type()
)
xupsTopologyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsTopologyType.setStatus("current")


class _XupsTopoMachineCode_Type(Integer32):
    """Custom type xupsTopoMachineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_XupsTopoMachineCode_Type.__name__ = "Integer32"
_XupsTopoMachineCode_Object = MibScalar
xupsTopoMachineCode = _XupsTopoMachineCode_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 13, 2),
    _XupsTopoMachineCode_Type()
)
xupsTopoMachineCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsTopoMachineCode.setStatus("current")


class _XupsTopoUnitNumber_Type(Integer32):
    """Custom type xupsTopoUnitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_XupsTopoUnitNumber_Type.__name__ = "Integer32"
_XupsTopoUnitNumber_Object = MibScalar
xupsTopoUnitNumber = _XupsTopoUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 13, 3),
    _XupsTopoUnitNumber_Type()
)
xupsTopoUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsTopoUnitNumber.setStatus("current")


class _XupsTopoPowerStrategy_Type(Integer32):
    """Custom type xupsTopoPowerStrategy based on Integer32"""
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
        *(("highAlert", 1),
          ("standard", 2),
          ("enableHighEfficiency", 3),
          ("immediateHighEfficiency", 4))
    )


_XupsTopoPowerStrategy_Type.__name__ = "Integer32"
_XupsTopoPowerStrategy_Object = MibScalar
xupsTopoPowerStrategy = _XupsTopoPowerStrategy_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 13, 4),
    _XupsTopoPowerStrategy_Type()
)
xupsTopoPowerStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsTopoPowerStrategy.setStatus("current")
_XupsAgent_ObjectIdentity = ObjectIdentity
xupsAgent = _XupsAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 14)
)


class _XupsAgentManufacturer_Type(DisplayString):
    """Custom type xupsAgentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XupsAgentManufacturer_Type.__name__ = "DisplayString"
_XupsAgentManufacturer_Object = MibScalar
xupsAgentManufacturer = _XupsAgentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 14, 1),
    _XupsAgentManufacturer_Type()
)
xupsAgentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAgentManufacturer.setStatus("current")


class _XupsAgentModel_Type(DisplayString):
    """Custom type xupsAgentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_XupsAgentModel_Type.__name__ = "DisplayString"
_XupsAgentModel_Object = MibScalar
xupsAgentModel = _XupsAgentModel_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 14, 2),
    _XupsAgentModel_Type()
)
xupsAgentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAgentModel.setStatus("current")


class _XupsAgentSoftwareVersion_Type(DisplayString):
    """Custom type xupsAgentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_XupsAgentSoftwareVersion_Type.__name__ = "DisplayString"
_XupsAgentSoftwareVersion_Object = MibScalar
xupsAgentSoftwareVersion = _XupsAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 14, 3),
    _XupsAgentSoftwareVersion_Type()
)
xupsAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAgentSoftwareVersion.setStatus("current")


class _XupsAgentPartNumber_Type(OctetString):
    """Custom type xupsAgentPartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_XupsAgentPartNumber_Type.__name__ = "OctetString"
_XupsAgentPartNumber_Object = MibScalar
xupsAgentPartNumber = _XupsAgentPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 14, 4),
    _XupsAgentPartNumber_Type()
)
xupsAgentPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAgentPartNumber.setStatus("current")


class _XupsAgentSerialNumber_Type(OctetString):
    """Custom type xupsAgentSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_XupsAgentSerialNumber_Type.__name__ = "OctetString"
_XupsAgentSerialNumber_Object = MibScalar
xupsAgentSerialNumber = _XupsAgentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 14, 5),
    _XupsAgentSerialNumber_Type()
)
xupsAgentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAgentSerialNumber.setStatus("current")
_XupsConformance_ObjectIdentity = ObjectIdentity
xupsConformance = _XupsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 100)
)

# Managed Objects groups

xupsIdentFullGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 2)
)
xupsIdentFullGroup.setObjects(
      *(("XUPS-MIB", "xupsIdentManufacturer"),
        ("XUPS-MIB", "xupsIdentModel"),
        ("XUPS-MIB", "xupsIdentSoftwareVersion"),
        ("XUPS-MIB", "xupsIdentOemCode"),
        ("XUPS-MIB", "xupsIdentPartNumber"),
        ("XUPS-MIB", "xupsIdentSerialNumber"))
)
if mibBuilder.loadTexts:
    xupsIdentFullGroup.setStatus("current")

xupsBatteryFullGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 3)
)
xupsBatteryFullGroup.setObjects(
      *(("XUPS-MIB", "xupsBatTimeRemaining"),
        ("XUPS-MIB", "xupsBatVoltage"),
        ("XUPS-MIB", "xupsBatCurrent"),
        ("XUPS-MIB", "xupsBatCapacity"),
        ("XUPS-MIB", "xupsBatteryAbmStatus"),
        ("XUPS-MIB", "xupsBatteryLastReplacedDate"),
        ("XUPS-MIB", "xupsBatteryFailure"),
        ("XUPS-MIB", "xupsBatteryNotPresent"),
        ("XUPS-MIB", "xupsBatteryAged"),
        ("XUPS-MIB", "xupsBatteryLowCapacity"))
)
if mibBuilder.loadTexts:
    xupsBatteryFullGroup.setStatus("current")

xupsInputFullGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 4)
)
xupsInputFullGroup.setObjects(
      *(("XUPS-MIB", "xupsInputFrequency"),
        ("XUPS-MIB", "xupsInputLineBads"),
        ("XUPS-MIB", "xupsInputNumPhases"),
        ("XUPS-MIB", "xupsInputSource"),
        ("XUPS-MIB", "xupsDualInputStatus"),
        ("XUPS-MIB", "xupsSecondaryInputWatch"),
        ("XUPS-MIB", "xupsInputStatus"))
)
if mibBuilder.loadTexts:
    xupsInputFullGroup.setStatus("current")

xupsInputTableFullGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 5)
)
xupsInputTableFullGroup.setObjects(
      *(("XUPS-MIB", "xupsInputPhase"),
        ("XUPS-MIB", "xupsInputVoltage"),
        ("XUPS-MIB", "xupsInputCurrent"),
        ("XUPS-MIB", "xupsInputWatts"),
        ("XUPS-MIB", "xupsInputId"),
        ("XUPS-MIB", "xupsInputName"),
        ("XUPS-MIB", "xupsInputCurrentHighPrecision"))
)
if mibBuilder.loadTexts:
    xupsInputTableFullGroup.setStatus("current")

xupsOutputFullGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 6)
)
xupsOutputFullGroup.setObjects(
      *(("XUPS-MIB", "xupsOutputLoad"),
        ("XUPS-MIB", "xupsOutputFrequency"),
        ("XUPS-MIB", "xupsOutputNumPhases"),
        ("XUPS-MIB", "xupsOutputSource"),
        ("XUPS-MIB", "xupsOutputHourlyPowerUsage"),
        ("XUPS-MIB", "xupsOutputCumulativePowerUsage"),
        ("XUPS-MIB", "xupsOutputCumulativePowerUsageTimer"),
        ("XUPS-MIB", "xupsOutputStatus"))
)
if mibBuilder.loadTexts:
    xupsOutputFullGroup.setStatus("current")

xupsOutputTableFullGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 7)
)
xupsOutputTableFullGroup.setObjects(
      *(("XUPS-MIB", "xupsOutputPhase"),
        ("XUPS-MIB", "xupsOutputVoltage"),
        ("XUPS-MIB", "xupsOutputCurrent"),
        ("XUPS-MIB", "xupsOutputWatts"),
        ("XUPS-MIB", "xupsOutputId"),
        ("XUPS-MIB", "xupsOutputName"),
        ("XUPS-MIB", "xupsOutputCurrentHighPrecision"),
        ("XUPS-MIB", "xupsOutputPercentLoad"),
        ("XUPS-MIB", "xupsOutputVA"))
)
if mibBuilder.loadTexts:
    xupsOutputTableFullGroup.setStatus("current")

xupsBypassFullGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 8)
)
xupsBypassFullGroup.setObjects(
      *(("XUPS-MIB", "xupsBypassFrequency"),
        ("XUPS-MIB", "xupsBypassNumPhases"),
        ("XUPS-MIB", "xupsBypassPhase"),
        ("XUPS-MIB", "xupsBypassVoltage"))
)
if mibBuilder.loadTexts:
    xupsBypassFullGroup.setStatus("current")

xupsEnvironmentFullGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 9)
)
xupsEnvironmentFullGroup.setObjects(
      *(("XUPS-MIB", "xupsEnvAmbientTemp"),
        ("XUPS-MIB", "xupsEnvAmbientLowerLimit"),
        ("XUPS-MIB", "xupsEnvAmbientUpperLimit"),
        ("XUPS-MIB", "xupsEnvAmbientHumidity"))
)
if mibBuilder.loadTexts:
    xupsEnvironmentFullGroup.setStatus("current")

xupsAlarmFullGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 10)
)
xupsAlarmFullGroup.setObjects(
      *(("XUPS-MIB", "xupsAlarms"),
        ("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsAlarmTime"))
)
if mibBuilder.loadTexts:
    xupsAlarmFullGroup.setStatus("current")

xupsAlarmEventsFullGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 11)
)
xupsAlarmEventsFullGroup.setObjects(
      *(("XUPS-MIB", "xupsAlarmNumEvents"),
        ("XUPS-MIB", "xupsAlarmEventMsg"))
)
if mibBuilder.loadTexts:
    xupsAlarmEventsFullGroup.setStatus("current")

xupsTestFullGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 12)
)
xupsTestFullGroup.setObjects(
      *(("XUPS-MIB", "xupsTestStart"),
        ("XUPS-MIB", "xupsTestBatteryStatus"),
        ("XUPS-MIB", "xupsLastGeneralTest"),
        ("XUPS-MIB", "xupsLastGeneralTestResult"),
        ("XUPS-MIB", "xupsTestTrap"))
)
if mibBuilder.loadTexts:
    xupsTestFullGroup.setStatus("current")

xupsControlFullGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 13)
)
xupsControlFullGroup.setObjects(
      *(("XUPS-MIB", "xupsControlOutputOffDelay"),
        ("XUPS-MIB", "xupsControlOutputOnDelay"),
        ("XUPS-MIB", "xupsControlOutputOffTrapDelay"),
        ("XUPS-MIB", "xupsControlToBypassDelay"),
        ("XUPS-MIB", "xupsLoadShedSecsWithRestart"),
        ("XUPS-MIB", "xupsSwitchable"))
)
if mibBuilder.loadTexts:
    xupsControlFullGroup.setStatus("current")

xupsConfigFullGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 14)
)
xupsConfigFullGroup.setObjects(
      *(("XUPS-MIB", "xupsConfigOutputVoltage"),
        ("XUPS-MIB", "xupsConfigInputVoltage"),
        ("XUPS-MIB", "xupsConfigOutputWatts"),
        ("XUPS-MIB", "xupsConfigOutputFreq"),
        ("XUPS-MIB", "xupsConfigDateAndTime"),
        ("XUPS-MIB", "xupsConfigLowOutputVoltageLimit"),
        ("XUPS-MIB", "xupsConfigHighOutputVoltageLimit"),
        ("XUPS-MIB", "xupsConfigInstallDate"))
)
if mibBuilder.loadTexts:
    xupsConfigFullGroup.setStatus("current")

xupsTrapControlFullGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 15)
)
xupsTrapControlFullGroup.setObjects(
      *(("XUPS-MIB", "xupsMaxTrapLevel"),
        ("XUPS-MIB", "xupsSendTrapType"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("XUPS-MIB", "xupsHeartbeatMinsInterval"))
)
if mibBuilder.loadTexts:
    xupsTrapControlFullGroup.setStatus("current")

xupsRecepFullGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 16)
)
xupsRecepFullGroup.setObjects(
      *(("XUPS-MIB", "xupsNumReceptacles"),
        ("XUPS-MIB", "xupsRecepIndex"),
        ("XUPS-MIB", "xupsRecepStatus"),
        ("XUPS-MIB", "xupsRecepOffDelaySecs"),
        ("XUPS-MIB", "xupsRecepOnDelaySecs"),
        ("XUPS-MIB", "xupsRecepAutoOffDelay"),
        ("XUPS-MIB", "xupsRecepAutoOnDelay"),
        ("XUPS-MIB", "xupsRecepShedSecsWithRestart"),
        ("XUPS-MIB", "xupsRecepHourlyPowerUsage"),
        ("XUPS-MIB", "xupsRecepCumulativePowerUsage"),
        ("XUPS-MIB", "xupsRecepCumulativePowerUsageTimer"))
)
if mibBuilder.loadTexts:
    xupsRecepFullGroup.setStatus("current")

xupsTopologyFullGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 17)
)
xupsTopologyFullGroup.setObjects(
      *(("XUPS-MIB", "xupsTopologyType"),
        ("XUPS-MIB", "xupsTopoMachineCode"),
        ("XUPS-MIB", "xupsTopoUnitNumber"),
        ("XUPS-MIB", "xupsTopoPowerStrategy"))
)
if mibBuilder.loadTexts:
    xupsTopologyFullGroup.setStatus("current")

xupsDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 21)
)
xupsDeprecatedGroup.setObjects(
      *(("XUPS-MIB", "xupsAlarmEventDateAndTime"),
        ("XUPS-MIB", "xupsAlarmEventKind"),
        ("XUPS-MIB", "xupsAlarmEventDescr"),
        ("XUPS-MIB", "xupsControlOutputOnTrapDelay"))
)
if mibBuilder.loadTexts:
    xupsDeprecatedGroup.setStatus("deprecated")

xupsBypassTableFullGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 22)
)
xupsBypassTableFullGroup.setObjects(
      *(("XUPS-MIB", "xupsBypassId"),
        ("XUPS-MIB", "xupsBypassName"),
        ("XUPS-MIB", "xupsBypassCurrentHighPrecision"),
        ("XUPS-MIB", "xupsBypassWatts"))
)
if mibBuilder.loadTexts:
    xupsBypassTableFullGroup.setStatus("current")

xupsInputTotalFullGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 23)
)
xupsInputTotalFullGroup.setObjects(
      *(("XUPS-MIB", "xupsInputAverageVoltage"),
        ("XUPS-MIB", "xupsInputTotalCurrent"),
        ("XUPS-MIB", "xupsInputTotalWatts"),
        ("XUPS-MIB", "xupsInputTotalVA"),
        ("XUPS-MIB", "xupsInputAveragePowerFactor"))
)
if mibBuilder.loadTexts:
    xupsInputTotalFullGroup.setStatus("current")

xupsOutputTotalFullGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 24)
)
xupsOutputTotalFullGroup.setObjects(
      *(("XUPS-MIB", "xupsOutputAverageVoltage"),
        ("XUPS-MIB", "xupsOutputTotalCurrent"),
        ("XUPS-MIB", "xupsOutputTotalWatts"),
        ("XUPS-MIB", "xupsOutputTotalVA"),
        ("XUPS-MIB", "xupsOutputAveragePowerFactor"))
)
if mibBuilder.loadTexts:
    xupsOutputTotalFullGroup.setStatus("current")

xupsBypassTotalFullGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 25)
)
xupsBypassTotalFullGroup.setObjects(
      *(("XUPS-MIB", "xupsBypassAverageVoltage"),
        ("XUPS-MIB", "xupsBypassTotalCurrent"),
        ("XUPS-MIB", "xupsBypassTotalWatts"),
        ("XUPS-MIB", "xupsBypassTotalVA"),
        ("XUPS-MIB", "xupsBypassAveragePowerFactor"))
)
if mibBuilder.loadTexts:
    xupsBypassTotalFullGroup.setStatus("current")

xupsAgentFullGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 26)
)
xupsAgentFullGroup.setObjects(
      *(("XUPS-MIB", "xupsAgentManufacturer"),
        ("XUPS-MIB", "xupsAgentModel"),
        ("XUPS-MIB", "xupsAgentSoftwareVersion"),
        ("XUPS-MIB", "xupsAgentPartNumber"),
        ("XUPS-MIB", "xupsAgentSerialNumber"))
)
if mibBuilder.loadTexts:
    xupsAgentFullGroup.setStatus("current")


# Notification objects

xupstdControlOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 1)
)
xupstdControlOff.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdControlOff.setStatus(
        "current"
    )

xupstdControlOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 2)
)
xupstdControlOn.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdControlOn.setStatus(
        "current"
    )

xupstdOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 3)
)
xupstdOnBattery.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdOnBattery.setStatus(
        "current"
    )

xupstdLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 4)
)
xupstdLowBattery.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdLowBattery.setStatus(
        "current"
    )

xupstdUtilityPowerRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 5)
)
xupstdUtilityPowerRestored.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdUtilityPowerRestored.setStatus(
        "current"
    )

xupstdReturnFromLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 6)
)
xupstdReturnFromLowBattery.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdReturnFromLowBattery.setStatus(
        "current"
    )

xupstdOutputOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 7)
)
xupstdOutputOverload.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdOutputOverload.setStatus(
        "current"
    )

xupstdInternalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 8)
)
xupstdInternalFailure.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdInternalFailure.setStatus(
        "current"
    )

xupstdBatteryDischarged = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 9)
)
xupstdBatteryDischarged.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdBatteryDischarged.setStatus(
        "current"
    )

xupstdInverterFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 10)
)
xupstdInverterFailure.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdInverterFailure.setStatus(
        "current"
    )

xupstdOnBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 11)
)
xupstdOnBypass.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdOnBypass.setStatus(
        "current"
    )

xupstdBypassNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 12)
)
xupstdBypassNotAvailable.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdBypassNotAvailable.setStatus(
        "current"
    )

xupstdOutputOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 13)
)
xupstdOutputOff.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdOutputOff.setStatus(
        "current"
    )

xupstdInputFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 14)
)
xupstdInputFailure.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdInputFailure.setStatus(
        "current"
    )

xupstdBuildingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 15)
)
xupstdBuildingAlarm.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdBuildingAlarm.setStatus(
        "current"
    )

xupstdShutdownImminent = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 16)
)
xupstdShutdownImminent.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdShutdownImminent.setStatus(
        "current"
    )

xupstdOnInverter = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 17)
)
xupstdOnInverter.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdOnInverter.setStatus(
        "current"
    )

xupstdBreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 20)
)
xupstdBreakerOpen.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdBreakerOpen.setStatus(
        "current"
    )

xupstdAlarmEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 21)
)
xupstdAlarmEntryAdded.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdAlarmEntryAdded.setStatus(
        "current"
    )

xupstdAlarmEntryRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 22)
)
xupstdAlarmEntryRemoved.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdAlarmEntryRemoved.setStatus(
        "current"
    )

xupstdAlarmBatteryBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 23)
)
xupstdAlarmBatteryBad.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdAlarmBatteryBad.setStatus(
        "current"
    )

xupstdOutputOffAsRequested = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 24)
)
xupstdOutputOffAsRequested.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdOutputOffAsRequested.setStatus(
        "current"
    )

xupstdDiagnosticTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 25)
)
xupstdDiagnosticTestFailed.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdDiagnosticTestFailed.setStatus(
        "current"
    )

xupstdCommunicationsLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 26)
)
xupstdCommunicationsLost.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdCommunicationsLost.setStatus(
        "current"
    )

xupstdUpsShutdownPending = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 27)
)
xupstdUpsShutdownPending.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdUpsShutdownPending.setStatus(
        "current"
    )

xupstdAlarmTestInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 28)
)
xupstdAlarmTestInProgress.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdAlarmTestInProgress.setStatus(
        "current"
    )

xupstdAmbientTempBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 29)
)
xupstdAmbientTempBad.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("XUPS-MIB", "xupsEnvAmbientTemp"),
        ("XUPS-MIB", "xupsEnvAmbientLowerLimit"),
        ("XUPS-MIB", "xupsEnvAmbientUpperLimit"))
)
if mibBuilder.loadTexts:
    xupstdAmbientTempBad.setStatus(
        "current"
    )

xupstdContactActiveNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 30)
)
xupstdContactActiveNotice.setObjects(
      *(("EATON-EMP-MIB", "xupsContactIndex"),
        ("EATON-EMP-MIB", "xupsContactType"),
        ("EATON-EMP-MIB", "xupsContactState"),
        ("EATON-EMP-MIB", "xupsContactDescr"))
)
if mibBuilder.loadTexts:
    xupstdContactActiveNotice.setStatus(
        "current"
    )

xupstdContactInactiveNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 31)
)
xupstdContactInactiveNotice.setObjects(
      *(("EATON-EMP-MIB", "xupsContactIndex"),
        ("EATON-EMP-MIB", "xupsContactType"),
        ("EATON-EMP-MIB", "xupsContactState"),
        ("EATON-EMP-MIB", "xupsContactDescr"))
)
if mibBuilder.loadTexts:
    xupstdContactInactiveNotice.setStatus(
        "current"
    )

xupstdLossOfRedundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 32)
)
xupstdLossOfRedundancy.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdLossOfRedundancy.setStatus(
        "current"
    )

xupstdAlarmTempBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 33)
)
xupstdAlarmTempBad.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdAlarmTempBad.setStatus(
        "current"
    )

xupstdAlarmChargerFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 34)
)
xupstdAlarmChargerFailed.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdAlarmChargerFailed.setStatus(
        "current"
    )

xupstdAlarmFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 35)
)
xupstdAlarmFanFailure.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdAlarmFanFailure.setStatus(
        "current"
    )

xupstdAlarmFuseFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 36)
)
xupstdAlarmFuseFailure.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdAlarmFuseFailure.setStatus(
        "current"
    )

xupstdPowerSwitchBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 37)
)
xupstdPowerSwitchBad.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdPowerSwitchBad.setStatus(
        "current"
    )

xupstdModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 38)
)
xupstdModuleFailure.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdModuleFailure.setStatus(
        "current"
    )

xupstdOnAlternatePowerSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 39)
)
xupstdOnAlternatePowerSource.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("XUPS-MIB", "xupsInputSource"))
)
if mibBuilder.loadTexts:
    xupstdOnAlternatePowerSource.setStatus(
        "current"
    )

xupstdAltPowerNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 40)
)
xupstdAltPowerNotAvailable.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdAltPowerNotAvailable.setStatus(
        "current"
    )

xupstdNoticeCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 41)
)
xupstdNoticeCondition.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdNoticeCondition.setStatus(
        "current"
    )

xupstdRemoteTempBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 42)
)
xupstdRemoteTempBad.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("EATON-EMP-MIB", "xupsEnvRemoteTemp"),
        ("EATON-EMP-MIB", "xupsEnvRemoteTempLowerLimit"),
        ("EATON-EMP-MIB", "xupsEnvRemoteTempUpperLimit"))
)
if mibBuilder.loadTexts:
    xupstdRemoteTempBad.setStatus(
        "current"
    )

xupstdRemoteHumidityBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 43)
)
xupstdRemoteHumidityBad.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("EATON-EMP-MIB", "xupsEnvRemoteHumidity"),
        ("EATON-EMP-MIB", "xupsEnvRemoteHumidityLowerLimit"),
        ("EATON-EMP-MIB", "xupsEnvRemoteHumidityUpperLimit"))
)
if mibBuilder.loadTexts:
    xupstdRemoteHumidityBad.setStatus(
        "current"
    )

xupstdHeartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 44)
)
xupstdHeartbeat.setObjects(
      *(("XUPS-MIB", "xupsInputSource"),
        ("XUPS-MIB", "xupsOutputSource"),
        ("XUPS-MIB", "xupsAlarms"))
)
if mibBuilder.loadTexts:
    xupstdHeartbeat.setStatus(
        "current"
    )

xupstdDiagnosticTestPassed = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 45)
)
xupstdDiagnosticTestPassed.setObjects(
      *(("XUPS-MIB", "xupsTestBatteryStatus"),
        ("XUPS-MIB", "xupsLastGeneralTest"),
        ("XUPS-MIB", "xupsLastGeneralTestResult"))
)
if mibBuilder.loadTexts:
    xupstdDiagnosticTestPassed.setStatus(
        "current"
    )

xupstdOutputBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 46)
)
xupstdOutputBad.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdOutputBad.setStatus(
        "current"
    )

xupstdAwaitingPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 47)
)
xupstdAwaitingPower.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdAwaitingPower.setStatus(
        "current"
    )

xupstdOnMaintenanceBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 48)
)
xupstdOnMaintenanceBypass.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdOnMaintenanceBypass.setStatus(
        "current"
    )

xupstdCommEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 49)
)
xupstdCommEstablished.setObjects(
      *(("XUPS-MIB", "xupsIdentModel"),
        ("XUPS-MIB", "xupsOutputSource"))
)
if mibBuilder.loadTexts:
    xupstdCommEstablished.setStatus(
        "current"
    )

xupstdAgentDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 50)
)
if mibBuilder.loadTexts:
    xupstdAgentDown.setStatus(
        "current"
    )

xupstdOutputNotProtected = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 51)
)
xupstdOutputNotProtected.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdOutputNotProtected.setStatus(
        "current"
    )

xupstdTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 100)
)
xupstdTestTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdTestTrap.setStatus(
        "current"
    )


# Notifications groups

xupstdNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 18)
)
xupstdNotifyGroup.setObjects(
      *(("XUPS-MIB", "xupstdControlOff"),
        ("XUPS-MIB", "xupstdControlOn"),
        ("XUPS-MIB", "xupstdOnBattery"),
        ("XUPS-MIB", "xupstdLowBattery"),
        ("XUPS-MIB", "xupstdUtilityPowerRestored"),
        ("XUPS-MIB", "xupstdReturnFromLowBattery"),
        ("XUPS-MIB", "xupstdOutputOverload"),
        ("XUPS-MIB", "xupstdInternalFailure"),
        ("XUPS-MIB", "xupstdBatteryDischarged"),
        ("XUPS-MIB", "xupstdInverterFailure"),
        ("XUPS-MIB", "xupstdOnBypass"),
        ("XUPS-MIB", "xupstdBypassNotAvailable"),
        ("XUPS-MIB", "xupstdOutputOff"),
        ("XUPS-MIB", "xupstdInputFailure"),
        ("XUPS-MIB", "xupstdBuildingAlarm"),
        ("XUPS-MIB", "xupstdShutdownImminent"),
        ("XUPS-MIB", "xupstdOnInverter"),
        ("XUPS-MIB", "xupstdBreakerOpen"),
        ("XUPS-MIB", "xupstdAlarmEntryAdded"),
        ("XUPS-MIB", "xupstdAlarmEntryRemoved"),
        ("XUPS-MIB", "xupstdAlarmBatteryBad"),
        ("XUPS-MIB", "xupstdOutputOffAsRequested"),
        ("XUPS-MIB", "xupstdDiagnosticTestFailed"),
        ("XUPS-MIB", "xupstdCommunicationsLost"),
        ("XUPS-MIB", "xupstdUpsShutdownPending"),
        ("XUPS-MIB", "xupstdAlarmTempBad"),
        ("XUPS-MIB", "xupstdAlarmTestInProgress"),
        ("XUPS-MIB", "xupstdAmbientTempBad"),
        ("XUPS-MIB", "xupstdLossOfRedundancy"),
        ("XUPS-MIB", "xupstdAlarmChargerFailed"),
        ("XUPS-MIB", "xupstdAlarmFanFailure"),
        ("XUPS-MIB", "xupstdAlarmFuseFailure"),
        ("XUPS-MIB", "xupstdPowerSwitchBad"),
        ("XUPS-MIB", "xupstdModuleFailure"),
        ("XUPS-MIB", "xupstdOnAlternatePowerSource"),
        ("XUPS-MIB", "xupstdAltPowerNotAvailable"),
        ("XUPS-MIB", "xupstdNoticeCondition"),
        ("XUPS-MIB", "xupstdHeartbeat"),
        ("XUPS-MIB", "xupstdDiagnosticTestPassed"),
        ("XUPS-MIB", "xupstdOutputBad"),
        ("XUPS-MIB", "xupstdAwaitingPower"),
        ("XUPS-MIB", "xupstdOnMaintenanceBypass"),
        ("XUPS-MIB", "xupstdCommEstablished"),
        ("XUPS-MIB", "xupstdAgentDown"),
        ("XUPS-MIB", "xupstdOutputNotProtected"),
        ("XUPS-MIB", "xupstdTestTrap"))
)
if mibBuilder.loadTexts:
    xupstdNotifyGroup.setStatus(
        "current"
    )

xupstdEMPNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 19)
)
xupstdEMPNotifyGroup.setObjects(
      *(("XUPS-MIB", "xupstdContactActiveNotice"),
        ("XUPS-MIB", "xupstdContactInactiveNotice"),
        ("XUPS-MIB", "xupstdRemoteTempBad"),
        ("XUPS-MIB", "xupstdRemoteHumidityBad"))
)
if mibBuilder.loadTexts:
    xupstdEMPNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

xupsMibFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 534, 1, 100, 20)
)
xupsMibFullCompliance.setObjects(
      *(("XUPS-MIB", "xupsIdentFullGroup"),
        ("XUPS-MIB", "xupsBatteryFullGroup"),
        ("XUPS-MIB", "xupsInputFullGroup"),
        ("XUPS-MIB", "xupsInputTableFullGroup"),
        ("XUPS-MIB", "xupsOutputFullGroup"),
        ("XUPS-MIB", "xupsOutputTableFullGroup"),
        ("XUPS-MIB", "xupsBypassFullGroup"),
        ("XUPS-MIB", "xupsEnvironmentFullGroup"),
        ("XUPS-MIB", "xupsAlarmFullGroup"),
        ("XUPS-MIB", "xupsAlarmEventsFullGroup"),
        ("XUPS-MIB", "xupsTestFullGroup"),
        ("XUPS-MIB", "xupsControlFullGroup"),
        ("XUPS-MIB", "xupsConfigFullGroup"),
        ("XUPS-MIB", "xupsTrapControlFullGroup"),
        ("XUPS-MIB", "xupsRecepFullGroup"),
        ("XUPS-MIB", "xupsTopologyFullGroup"),
        ("XUPS-MIB", "xupstdNotifyGroup"),
        ("XUPS-MIB", "xupstdEMPNotifyGroup"),
        ("XUPS-MIB", "xupsBypassTableFullGroup"),
        ("XUPS-MIB", "xupsInputTotalFullGroup"),
        ("XUPS-MIB", "xupsOutputTotalFullGroup"),
        ("XUPS-MIB", "xupsBypassTotalFullGroup"))
)
if mibBuilder.loadTexts:
    xupsMibFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XUPS-MIB",
    **{"xupsMIB": xupsMIB,
       "xupsIdent": xupsIdent,
       "xupsIdentManufacturer": xupsIdentManufacturer,
       "xupsIdentModel": xupsIdentModel,
       "xupsIdentSoftwareVersion": xupsIdentSoftwareVersion,
       "xupsIdentOemCode": xupsIdentOemCode,
       "xupsIdentPartNumber": xupsIdentPartNumber,
       "xupsIdentSerialNumber": xupsIdentSerialNumber,
       "xupsBattery": xupsBattery,
       "xupsBatTimeRemaining": xupsBatTimeRemaining,
       "xupsBatVoltage": xupsBatVoltage,
       "xupsBatCurrent": xupsBatCurrent,
       "xupsBatCapacity": xupsBatCapacity,
       "xupsBatteryAbmStatus": xupsBatteryAbmStatus,
       "xupsBatteryLastReplacedDate": xupsBatteryLastReplacedDate,
       "xupsBatteryFailure": xupsBatteryFailure,
       "xupsBatteryNotPresent": xupsBatteryNotPresent,
       "xupsBatteryAged": xupsBatteryAged,
       "xupsBatteryLowCapacity": xupsBatteryLowCapacity,
       "xupsInput": xupsInput,
       "xupsInputFrequency": xupsInputFrequency,
       "xupsInputLineBads": xupsInputLineBads,
       "xupsInputNumPhases": xupsInputNumPhases,
       "xupsInputTable": xupsInputTable,
       "xupsInputEntry": xupsInputEntry,
       "xupsInputPhase": xupsInputPhase,
       "xupsInputVoltage": xupsInputVoltage,
       "xupsInputCurrent": xupsInputCurrent,
       "xupsInputWatts": xupsInputWatts,
       "xupsInputId": xupsInputId,
       "xupsInputName": xupsInputName,
       "xupsInputCurrentHighPrecision": xupsInputCurrentHighPrecision,
       "xupsInputSource": xupsInputSource,
       "xupsDualInputStatus": xupsDualInputStatus,
       "xupsSecondaryInputWatch": xupsSecondaryInputWatch,
       "xupsInputTotal": xupsInputTotal,
       "xupsInputAverageVoltage": xupsInputAverageVoltage,
       "xupsInputTotalCurrent": xupsInputTotalCurrent,
       "xupsInputTotalWatts": xupsInputTotalWatts,
       "xupsInputTotalVA": xupsInputTotalVA,
       "xupsInputAveragePowerFactor": xupsInputAveragePowerFactor,
       "xupsInputStatus": xupsInputStatus,
       "xupsOutput": xupsOutput,
       "xupsOutputLoad": xupsOutputLoad,
       "xupsOutputFrequency": xupsOutputFrequency,
       "xupsOutputNumPhases": xupsOutputNumPhases,
       "xupsOutputTable": xupsOutputTable,
       "xupsOutputEntry": xupsOutputEntry,
       "xupsOutputPhase": xupsOutputPhase,
       "xupsOutputVoltage": xupsOutputVoltage,
       "xupsOutputCurrent": xupsOutputCurrent,
       "xupsOutputWatts": xupsOutputWatts,
       "xupsOutputId": xupsOutputId,
       "xupsOutputName": xupsOutputName,
       "xupsOutputCurrentHighPrecision": xupsOutputCurrentHighPrecision,
       "xupsOutputPercentLoad": xupsOutputPercentLoad,
       "xupsOutputVA": xupsOutputVA,
       "xupsOutputSource": xupsOutputSource,
       "xupsOutputHourlyPowerUsage": xupsOutputHourlyPowerUsage,
       "xupsOutputCumulativePowerUsage": xupsOutputCumulativePowerUsage,
       "xupsOutputCumulativePowerUsageTimer": xupsOutputCumulativePowerUsageTimer,
       "xupsOutputTotal": xupsOutputTotal,
       "xupsOutputAverageVoltage": xupsOutputAverageVoltage,
       "xupsOutputTotalCurrent": xupsOutputTotalCurrent,
       "xupsOutputTotalWatts": xupsOutputTotalWatts,
       "xupsOutputTotalVA": xupsOutputTotalVA,
       "xupsOutputAveragePowerFactor": xupsOutputAveragePowerFactor,
       "xupsOutputStatus": xupsOutputStatus,
       "xupsBypass": xupsBypass,
       "xupsBypassFrequency": xupsBypassFrequency,
       "xupsBypassNumPhases": xupsBypassNumPhases,
       "xupsBypassTable": xupsBypassTable,
       "xupsBypassEntry": xupsBypassEntry,
       "xupsBypassPhase": xupsBypassPhase,
       "xupsBypassVoltage": xupsBypassVoltage,
       "xupsBypassId": xupsBypassId,
       "xupsBypassName": xupsBypassName,
       "xupsBypassCurrentHighPrecision": xupsBypassCurrentHighPrecision,
       "xupsBypassWatts": xupsBypassWatts,
       "xupsBypassTotal": xupsBypassTotal,
       "xupsBypassAverageVoltage": xupsBypassAverageVoltage,
       "xupsBypassTotalCurrent": xupsBypassTotalCurrent,
       "xupsBypassTotalWatts": xupsBypassTotalWatts,
       "xupsBypassTotalVA": xupsBypassTotalVA,
       "xupsBypassAveragePowerFactor": xupsBypassAveragePowerFactor,
       "xupsEnvAmbientTemp": xupsEnvAmbientTemp,
       "xupsEnvAmbientLowerLimit": xupsEnvAmbientLowerLimit,
       "xupsEnvAmbientUpperLimit": xupsEnvAmbientUpperLimit,
       "xupsEnvAmbientHumidity": xupsEnvAmbientHumidity,
       "xupsAlarm": xupsAlarm,
       "xupsAlarms": xupsAlarms,
       "xupsAlarmTable": xupsAlarmTable,
       "xupsAlarmEntry": xupsAlarmEntry,
       "xupsAlarmID": xupsAlarmID,
       "xupsAlarmDescr": xupsAlarmDescr,
       "xupsAlarmTime": xupsAlarmTime,
       "xupsOnBattery": xupsOnBattery,
       "xupsLowBattery": xupsLowBattery,
       "xupsUtilityPowerRestored": xupsUtilityPowerRestored,
       "xupsReturnFromLowBattery": xupsReturnFromLowBattery,
       "xupsOutputOverload": xupsOutputOverload,
       "xupsInternalFailure": xupsInternalFailure,
       "xupsBatteryDischarged": xupsBatteryDischarged,
       "xupsInverterFailure": xupsInverterFailure,
       "xupsOnBypass": xupsOnBypass,
       "xupsBypassNotAvailable": xupsBypassNotAvailable,
       "xupsOutputOff": xupsOutputOff,
       "xupsInputFailure": xupsInputFailure,
       "xupsBuildingAlarm": xupsBuildingAlarm,
       "xupsShutdownImminent": xupsShutdownImminent,
       "xupsOnInverter": xupsOnInverter,
       "xupsAlarmNumEvents": xupsAlarmNumEvents,
       "xupsAlarmEventTable": xupsAlarmEventTable,
       "xupsAlarmEventEntry": xupsAlarmEventEntry,
       "xupsAlarmEventID": xupsAlarmEventID,
       "xupsAlarmEventDateAndTime": xupsAlarmEventDateAndTime,
       "xupsAlarmEventKind": xupsAlarmEventKind,
       "xupsAlarmEventDescr": xupsAlarmEventDescr,
       "xupsAlarmEventMsg": xupsAlarmEventMsg,
       "xupsBreakerOpen": xupsBreakerOpen,
       "xupsAlarmEntryAdded": xupsAlarmEntryAdded,
       "xupsAlarmEntryRemoved": xupsAlarmEntryRemoved,
       "xupsAlarmBatteryBad": xupsAlarmBatteryBad,
       "xupsOutputOffAsRequested": xupsOutputOffAsRequested,
       "xupsDiagnosticTestFailed": xupsDiagnosticTestFailed,
       "xupsCommunicationsLost": xupsCommunicationsLost,
       "xupsUpsShutdownPending": xupsUpsShutdownPending,
       "xupsAlarmTestInProgress": xupsAlarmTestInProgress,
       "xupsAmbientTempBad": xupsAmbientTempBad,
       "xupsLossOfRedundancy": xupsLossOfRedundancy,
       "xupsAlarmTempBad": xupsAlarmTempBad,
       "xupsAlarmChargerFailed": xupsAlarmChargerFailed,
       "xupsAlarmFanFailure": xupsAlarmFanFailure,
       "xupsAlarmFuseFailure": xupsAlarmFuseFailure,
       "xupsPowerSwitchBad": xupsPowerSwitchBad,
       "xupsModuleFailure": xupsModuleFailure,
       "xupsOnAlternatePowerSource": xupsOnAlternatePowerSource,
       "xupsAltPowerNotAvailable": xupsAltPowerNotAvailable,
       "xupsNoticeCondition": xupsNoticeCondition,
       "xupsRemoteTempBad": xupsRemoteTempBad,
       "xupsRemoteHumidityBad": xupsRemoteHumidityBad,
       "xupsAlarmOutputBad": xupsAlarmOutputBad,
       "xupsAlarmAwaitingPower": xupsAlarmAwaitingPower,
       "xupsOnMaintenanceBypass": xupsOnMaintenanceBypass,
       "xupsOutputNotProtected": xupsOutputNotProtected,
       "xupsTest": xupsTest,
       "xupsTestStart": xupsTestStart,
       "xupsTestBatteryStatus": xupsTestBatteryStatus,
       "xupsLastGeneralTest": xupsLastGeneralTest,
       "xupsLastGeneralTestResult": xupsLastGeneralTestResult,
       "xupsTestTrap": xupsTestTrap,
       "xupsControl": xupsControl,
       "xupsControlOutputOffDelay": xupsControlOutputOffDelay,
       "xupsControlOutputOnDelay": xupsControlOutputOnDelay,
       "xupsControlOutputOffTrapDelay": xupsControlOutputOffTrapDelay,
       "xupsControlOutputOnTrapDelay": xupsControlOutputOnTrapDelay,
       "xupsControlToBypassDelay": xupsControlToBypassDelay,
       "xupsLoadShedSecsWithRestart": xupsLoadShedSecsWithRestart,
       "xupsSwitchable": xupsSwitchable,
       "xupsConfig": xupsConfig,
       "xupsConfigOutputVoltage": xupsConfigOutputVoltage,
       "xupsConfigInputVoltage": xupsConfigInputVoltage,
       "xupsConfigOutputWatts": xupsConfigOutputWatts,
       "xupsConfigOutputFreq": xupsConfigOutputFreq,
       "xupsConfigDateAndTime": xupsConfigDateAndTime,
       "xupsConfigLowOutputVoltageLimit": xupsConfigLowOutputVoltageLimit,
       "xupsConfigHighOutputVoltageLimit": xupsConfigHighOutputVoltageLimit,
       "xupsConfigInstallDate": xupsConfigInstallDate,
       "xupsTrapControl": xupsTrapControl,
       "xupsMaxTrapLevel": xupsMaxTrapLevel,
       "xupsSendTrapType": xupsSendTrapType,
       "xupsTrapMessage": xupsTrapMessage,
       "xupsTrapSource": xupsTrapSource,
       "xupsTrapDefined": xupsTrapDefined,
       "xupsTrapOidDefined": xupsTrapOidDefined,
       "xupstdControlOff": xupstdControlOff,
       "xupstdControlOn": xupstdControlOn,
       "xupstdOnBattery": xupstdOnBattery,
       "xupstdLowBattery": xupstdLowBattery,
       "xupstdUtilityPowerRestored": xupstdUtilityPowerRestored,
       "xupstdReturnFromLowBattery": xupstdReturnFromLowBattery,
       "xupstdOutputOverload": xupstdOutputOverload,
       "xupstdInternalFailure": xupstdInternalFailure,
       "xupstdBatteryDischarged": xupstdBatteryDischarged,
       "xupstdInverterFailure": xupstdInverterFailure,
       "xupstdOnBypass": xupstdOnBypass,
       "xupstdBypassNotAvailable": xupstdBypassNotAvailable,
       "xupstdOutputOff": xupstdOutputOff,
       "xupstdInputFailure": xupstdInputFailure,
       "xupstdBuildingAlarm": xupstdBuildingAlarm,
       "xupstdShutdownImminent": xupstdShutdownImminent,
       "xupstdOnInverter": xupstdOnInverter,
       "xupstdBreakerOpen": xupstdBreakerOpen,
       "xupstdAlarmEntryAdded": xupstdAlarmEntryAdded,
       "xupstdAlarmEntryRemoved": xupstdAlarmEntryRemoved,
       "xupstdAlarmBatteryBad": xupstdAlarmBatteryBad,
       "xupstdOutputOffAsRequested": xupstdOutputOffAsRequested,
       "xupstdDiagnosticTestFailed": xupstdDiagnosticTestFailed,
       "xupstdCommunicationsLost": xupstdCommunicationsLost,
       "xupstdUpsShutdownPending": xupstdUpsShutdownPending,
       "xupstdAlarmTestInProgress": xupstdAlarmTestInProgress,
       "xupstdAmbientTempBad": xupstdAmbientTempBad,
       "xupstdContactActiveNotice": xupstdContactActiveNotice,
       "xupstdContactInactiveNotice": xupstdContactInactiveNotice,
       "xupstdLossOfRedundancy": xupstdLossOfRedundancy,
       "xupstdAlarmTempBad": xupstdAlarmTempBad,
       "xupstdAlarmChargerFailed": xupstdAlarmChargerFailed,
       "xupstdAlarmFanFailure": xupstdAlarmFanFailure,
       "xupstdAlarmFuseFailure": xupstdAlarmFuseFailure,
       "xupstdPowerSwitchBad": xupstdPowerSwitchBad,
       "xupstdModuleFailure": xupstdModuleFailure,
       "xupstdOnAlternatePowerSource": xupstdOnAlternatePowerSource,
       "xupstdAltPowerNotAvailable": xupstdAltPowerNotAvailable,
       "xupstdNoticeCondition": xupstdNoticeCondition,
       "xupstdRemoteTempBad": xupstdRemoteTempBad,
       "xupstdRemoteHumidityBad": xupstdRemoteHumidityBad,
       "xupstdHeartbeat": xupstdHeartbeat,
       "xupstdDiagnosticTestPassed": xupstdDiagnosticTestPassed,
       "xupstdOutputBad": xupstdOutputBad,
       "xupstdAwaitingPower": xupstdAwaitingPower,
       "xupstdOnMaintenanceBypass": xupstdOnMaintenanceBypass,
       "xupstdCommEstablished": xupstdCommEstablished,
       "xupstdAgentDown": xupstdAgentDown,
       "xupstdOutputNotProtected": xupstdOutputNotProtected,
       "xupstdTestTrap": xupstdTestTrap,
       "xupsHeartbeatMinsInterval": xupsHeartbeatMinsInterval,
       "xupsRecep": xupsRecep,
       "xupsNumReceptacles": xupsNumReceptacles,
       "xupsRecepTable": xupsRecepTable,
       "xupsRecepEntry": xupsRecepEntry,
       "xupsRecepIndex": xupsRecepIndex,
       "xupsRecepStatus": xupsRecepStatus,
       "xupsRecepOffDelaySecs": xupsRecepOffDelaySecs,
       "xupsRecepOnDelaySecs": xupsRecepOnDelaySecs,
       "xupsRecepAutoOffDelay": xupsRecepAutoOffDelay,
       "xupsRecepAutoOnDelay": xupsRecepAutoOnDelay,
       "xupsRecepShedSecsWithRestart": xupsRecepShedSecsWithRestart,
       "xupsRecepHourlyPowerUsage": xupsRecepHourlyPowerUsage,
       "xupsRecepCumulativePowerUsage": xupsRecepCumulativePowerUsage,
       "xupsRecepCumulativePowerUsageTimer": xupsRecepCumulativePowerUsageTimer,
       "xupsTopology": xupsTopology,
       "xupsTopologyType": xupsTopologyType,
       "xupsTopoMachineCode": xupsTopoMachineCode,
       "xupsTopoUnitNumber": xupsTopoUnitNumber,
       "xupsTopoPowerStrategy": xupsTopoPowerStrategy,
       "xupsAgent": xupsAgent,
       "xupsAgentManufacturer": xupsAgentManufacturer,
       "xupsAgentModel": xupsAgentModel,
       "xupsAgentSoftwareVersion": xupsAgentSoftwareVersion,
       "xupsAgentPartNumber": xupsAgentPartNumber,
       "xupsAgentSerialNumber": xupsAgentSerialNumber,
       "xupsConformance": xupsConformance,
       "xupsIdentFullGroup": xupsIdentFullGroup,
       "xupsBatteryFullGroup": xupsBatteryFullGroup,
       "xupsInputFullGroup": xupsInputFullGroup,
       "xupsInputTableFullGroup": xupsInputTableFullGroup,
       "xupsOutputFullGroup": xupsOutputFullGroup,
       "xupsOutputTableFullGroup": xupsOutputTableFullGroup,
       "xupsBypassFullGroup": xupsBypassFullGroup,
       "xupsEnvironmentFullGroup": xupsEnvironmentFullGroup,
       "xupsAlarmFullGroup": xupsAlarmFullGroup,
       "xupsAlarmEventsFullGroup": xupsAlarmEventsFullGroup,
       "xupsTestFullGroup": xupsTestFullGroup,
       "xupsControlFullGroup": xupsControlFullGroup,
       "xupsConfigFullGroup": xupsConfigFullGroup,
       "xupsTrapControlFullGroup": xupsTrapControlFullGroup,
       "xupsRecepFullGroup": xupsRecepFullGroup,
       "xupsTopologyFullGroup": xupsTopologyFullGroup,
       "xupstdNotifyGroup": xupstdNotifyGroup,
       "xupstdEMPNotifyGroup": xupstdEMPNotifyGroup,
       "xupsMibFullCompliance": xupsMibFullCompliance,
       "xupsDeprecatedGroup": xupsDeprecatedGroup,
       "xupsBypassTableFullGroup": xupsBypassTableFullGroup,
       "xupsInputTotalFullGroup": xupsInputTotalFullGroup,
       "xupsOutputTotalFullGroup": xupsOutputTotalFullGroup,
       "xupsBypassTotalFullGroup": xupsBypassTotalFullGroup,
       "xupsAgentFullGroup": xupsAgentFullGroup}
)
