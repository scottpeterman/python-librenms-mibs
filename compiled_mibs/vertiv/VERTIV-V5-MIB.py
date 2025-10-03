# SNMP MIB module (VERTIV-V5-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\vertiv\VERTIV-V5-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:54 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

vertiv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21239)
)
if mibBuilder.loadTexts:
    vertiv.setRevisions(
        ("2020-01-07 00:00",
         "2019-09-30 00:00",
         "2019-09-12 00:00",
         "2019-08-30 00:00",
         "2019-06-06 00:00",
         "2019-05-07 00:00",
         "2019-04-30 00:00",
         "2019-03-07 00:00",
         "2018-01-19 00:00",
         "2017-09-19 00:00",
         "2017-08-10 00:00",
         "2017-05-10 00:00",
         "2017-04-05 00:00",
         "2016-06-30 00:00",
         "2012-09-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_V5_ObjectIdentity = ObjectIdentity
v5 = _V5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 5)
)
_Imd_ObjectIdentity = ObjectIdentity
imd = _Imd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2)
)
_DeviceInfo_ObjectIdentity = ObjectIdentity
deviceInfo = _DeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1)
)
_ProductTitle_Type = SnmpAdminString
_ProductTitle_Object = MibScalar
productTitle = _ProductTitle_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1, 1),
    _ProductTitle_Type()
)
productTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productTitle.setStatus("current")
_ProductVersion_Type = SnmpAdminString
_ProductVersion_Object = MibScalar
productVersion = _ProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1, 2),
    _ProductVersion_Type()
)
productVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productVersion.setStatus("current")
_ProductFriendlyName_Type = SnmpAdminString
_ProductFriendlyName_Object = MibScalar
productFriendlyName = _ProductFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1, 3),
    _ProductFriendlyName_Type()
)
productFriendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productFriendlyName.setStatus("current")
_ProductMacAddress_Type = MacAddress
_ProductMacAddress_Object = MibScalar
productMacAddress = _ProductMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1, 4),
    _ProductMacAddress_Type()
)
productMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productMacAddress.setStatus("current")


class _DeviceCount_Type(Integer32):
    """Custom type deviceCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DeviceCount_Type.__name__ = "Integer32"
_DeviceCount_Object = MibScalar
deviceCount = _DeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1, 6),
    _DeviceCount_Type()
)
deviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCount.setStatus("current")


class _TemperatureUnits_Type(Integer32):
    """Custom type temperatureUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fahrenheit", 0),
          ("celsius", 1))
    )


_TemperatureUnits_Type.__name__ = "Integer32"
_TemperatureUnits_Object = MibScalar
temperatureUnits = _TemperatureUnits_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1, 7),
    _TemperatureUnits_Type()
)
temperatureUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureUnits.setStatus("current")
_ProductModelNumber_Type = SnmpAdminString
_ProductModelNumber_Object = MibScalar
productModelNumber = _ProductModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1, 8),
    _ProductModelNumber_Type()
)
productModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productModelNumber.setStatus("current")
_ProductPartNumber_Type = SnmpAdminString
_ProductPartNumber_Object = MibScalar
productPartNumber = _ProductPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1, 9),
    _ProductPartNumber_Type()
)
productPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productPartNumber.setStatus("current")
_ProductSerialNumber_Type = SnmpAdminString
_ProductSerialNumber_Object = MibScalar
productSerialNumber = _ProductSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1, 10),
    _ProductSerialNumber_Type()
)
productSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productSerialNumber.setStatus("current")
_ProductPlatform_Type = SnmpAdminString
_ProductPlatform_Object = MibScalar
productPlatform = _ProductPlatform_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1, 11),
    _ProductPlatform_Type()
)
productPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productPlatform.setStatus("current")
_ProductHostname_Type = SnmpAdminString
_ProductHostname_Object = MibScalar
productHostname = _ProductHostname_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1, 12),
    _ProductHostname_Type()
)
productHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productHostname.setStatus("current")
_ProductAlarmCount_Type = Integer32
_ProductAlarmCount_Object = MibScalar
productAlarmCount = _ProductAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1, 13),
    _ProductAlarmCount_Type()
)
productAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productAlarmCount.setStatus("current")
_ProductWarnCount_Type = Integer32
_ProductWarnCount_Object = MibScalar
productWarnCount = _ProductWarnCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1, 14),
    _ProductWarnCount_Type()
)
productWarnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productWarnCount.setStatus("current")
_ProductManufacturer_Type = SnmpAdminString
_ProductManufacturer_Object = MibScalar
productManufacturer = _ProductManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1, 15),
    _ProductManufacturer_Type()
)
productManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productManufacturer.setStatus("current")
_Pdu_ObjectIdentity = ObjectIdentity
pdu = _Pdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3)
)
_PduMainTable_Object = MibTable
pduMainTable = _PduMainTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1)
)
if mibBuilder.loadTexts:
    pduMainTable.setStatus("current")
_PduMainEntry_Object = MibTableRow
pduMainEntry = _PduMainEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1)
)
pduMainEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "pduMainIndex"),
)
if mibBuilder.loadTexts:
    pduMainEntry.setStatus("current")


class _PduMainIndex_Type(Integer32):
    """Custom type pduMainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PduMainIndex_Type.__name__ = "Integer32"
_PduMainIndex_Object = MibTableColumn
pduMainIndex = _PduMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 1),
    _PduMainIndex_Type()
)
pduMainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduMainIndex.setStatus("current")
_PduMainSerial_Type = DisplayString
_PduMainSerial_Object = MibTableColumn
pduMainSerial = _PduMainSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 2),
    _PduMainSerial_Type()
)
pduMainSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMainSerial.setStatus("current")


class _PduMainName_Type(SnmpAdminString):
    """Custom type pduMainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_PduMainName_Type.__name__ = "SnmpAdminString"
_PduMainName_Object = MibTableColumn
pduMainName = _PduMainName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 3),
    _PduMainName_Type()
)
pduMainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMainName.setStatus("current")


class _PduMainLabel_Type(SnmpAdminString):
    """Custom type pduMainLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_PduMainLabel_Type.__name__ = "SnmpAdminString"
_PduMainLabel_Object = MibTableColumn
pduMainLabel = _PduMainLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 4),
    _PduMainLabel_Type()
)
pduMainLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMainLabel.setStatus("current")
_PduMainAvail_Type = Gauge32
_PduMainAvail_Object = MibTableColumn
pduMainAvail = _PduMainAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 5),
    _PduMainAvail_Type()
)
pduMainAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMainAvail.setStatus("current")


class _PduMeterType_Type(Integer32):
    """Custom type pduMeterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wye", 0),
          ("delta", 1))
    )


_PduMeterType_Type.__name__ = "Integer32"
_PduMeterType_Object = MibTableColumn
pduMeterType = _PduMeterType_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 6),
    _PduMeterType_Type()
)
pduMeterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMeterType.setStatus("current")


class _PduTotalName_Type(SnmpAdminString):
    """Custom type pduTotalName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_PduTotalName_Type.__name__ = "SnmpAdminString"
_PduTotalName_Object = MibTableColumn
pduTotalName = _PduTotalName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 7),
    _PduTotalName_Type()
)
pduTotalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTotalName.setStatus("current")


class _PduTotalLabel_Type(SnmpAdminString):
    """Custom type pduTotalLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_PduTotalLabel_Type.__name__ = "SnmpAdminString"
_PduTotalLabel_Object = MibTableColumn
pduTotalLabel = _PduTotalLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 8),
    _PduTotalLabel_Type()
)
pduTotalLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduTotalLabel.setStatus("current")


class _PduTotalRealPower_Type(Gauge32):
    """Custom type pduTotalRealPower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_PduTotalRealPower_Type.__name__ = "Gauge32"
_PduTotalRealPower_Object = MibTableColumn
pduTotalRealPower = _PduTotalRealPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 9),
    _PduTotalRealPower_Type()
)
pduTotalRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTotalRealPower.setStatus("current")
if mibBuilder.loadTexts:
    pduTotalRealPower.setUnits("watts")


class _PduTotalApparentPower_Type(Gauge32):
    """Custom type pduTotalApparentPower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_PduTotalApparentPower_Type.__name__ = "Gauge32"
_PduTotalApparentPower_Object = MibTableColumn
pduTotalApparentPower = _PduTotalApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 10),
    _PduTotalApparentPower_Type()
)
pduTotalApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTotalApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    pduTotalApparentPower.setUnits("volt-amps")


class _PduTotalPowerFactor_Type(Gauge32):
    """Custom type pduTotalPowerFactor based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PduTotalPowerFactor_Type.__name__ = "Gauge32"
_PduTotalPowerFactor_Object = MibTableColumn
pduTotalPowerFactor = _PduTotalPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 11),
    _PduTotalPowerFactor_Type()
)
pduTotalPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTotalPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    pduTotalPowerFactor.setUnits("%")


class _PduTotalEnergy_Type(Gauge32):
    """Custom type pduTotalEnergy based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999000),
    )


_PduTotalEnergy_Type.__name__ = "Gauge32"
_PduTotalEnergy_Object = MibTableColumn
pduTotalEnergy = _PduTotalEnergy_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 12),
    _PduTotalEnergy_Type()
)
pduTotalEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTotalEnergy.setStatus("current")
if mibBuilder.loadTexts:
    pduTotalEnergy.setUnits("watt-hours")
_PduPhaseTable_Object = MibTable
pduPhaseTable = _PduPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2)
)
if mibBuilder.loadTexts:
    pduPhaseTable.setStatus("current")
_PduPhaseEntry_Object = MibTableRow
pduPhaseEntry = _PduPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1)
)
pduPhaseEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "pduPhaseIndex"),
)
if mibBuilder.loadTexts:
    pduPhaseEntry.setStatus("current")


class _PduPhaseIndex_Type(Integer32):
    """Custom type pduPhaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PduPhaseIndex_Type.__name__ = "Integer32"
_PduPhaseIndex_Object = MibTableColumn
pduPhaseIndex = _PduPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 1),
    _PduPhaseIndex_Type()
)
pduPhaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduPhaseIndex.setStatus("current")


class _PduPhaseName_Type(SnmpAdminString):
    """Custom type pduPhaseName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_PduPhaseName_Type.__name__ = "SnmpAdminString"
_PduPhaseName_Object = MibTableColumn
pduPhaseName = _PduPhaseName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 2),
    _PduPhaseName_Type()
)
pduPhaseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseName.setStatus("current")


class _PduPhaseLabel_Type(SnmpAdminString):
    """Custom type pduPhaseLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_PduPhaseLabel_Type.__name__ = "SnmpAdminString"
_PduPhaseLabel_Object = MibTableColumn
pduPhaseLabel = _PduPhaseLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 3),
    _PduPhaseLabel_Type()
)
pduPhaseLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduPhaseLabel.setStatus("current")


class _PduPhaseVoltage_Type(Gauge32):
    """Custom type pduPhaseVoltage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3100),
    )


_PduPhaseVoltage_Type.__name__ = "Gauge32"
_PduPhaseVoltage_Object = MibTableColumn
pduPhaseVoltage = _PduPhaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 4),
    _PduPhaseVoltage_Type()
)
pduPhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    pduPhaseVoltage.setUnits("decivolts (rms)")


class _PduPhaseCurrent_Type(Gauge32):
    """Custom type pduPhaseCurrent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9900),
    )


_PduPhaseCurrent_Type.__name__ = "Gauge32"
_PduPhaseCurrent_Object = MibTableColumn
pduPhaseCurrent = _PduPhaseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 8),
    _PduPhaseCurrent_Type()
)
pduPhaseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pduPhaseCurrent.setUnits("centiamps (rms)")


class _PduPhaseRealPower_Type(Gauge32):
    """Custom type pduPhaseRealPower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_PduPhaseRealPower_Type.__name__ = "Gauge32"
_PduPhaseRealPower_Object = MibTableColumn
pduPhaseRealPower = _PduPhaseRealPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 12),
    _PduPhaseRealPower_Type()
)
pduPhaseRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseRealPower.setStatus("current")
if mibBuilder.loadTexts:
    pduPhaseRealPower.setUnits("watts")


class _PduPhaseApparentPower_Type(Gauge32):
    """Custom type pduPhaseApparentPower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_PduPhaseApparentPower_Type.__name__ = "Gauge32"
_PduPhaseApparentPower_Object = MibTableColumn
pduPhaseApparentPower = _PduPhaseApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 13),
    _PduPhaseApparentPower_Type()
)
pduPhaseApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    pduPhaseApparentPower.setUnits("volt-amps")


class _PduPhasePowerFactor_Type(Gauge32):
    """Custom type pduPhasePowerFactor based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PduPhasePowerFactor_Type.__name__ = "Gauge32"
_PduPhasePowerFactor_Object = MibTableColumn
pduPhasePowerFactor = _PduPhasePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 14),
    _PduPhasePowerFactor_Type()
)
pduPhasePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhasePowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    pduPhasePowerFactor.setUnits("%")


class _PduPhaseEnergy_Type(Gauge32):
    """Custom type pduPhaseEnergy based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999000),
    )


_PduPhaseEnergy_Type.__name__ = "Gauge32"
_PduPhaseEnergy_Object = MibTableColumn
pduPhaseEnergy = _PduPhaseEnergy_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 15),
    _PduPhaseEnergy_Type()
)
pduPhaseEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseEnergy.setStatus("current")
if mibBuilder.loadTexts:
    pduPhaseEnergy.setUnits("watt-hours")


class _PduPhaseBalance_Type(Gauge32):
    """Custom type pduPhaseBalance based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PduPhaseBalance_Type.__name__ = "Gauge32"
_PduPhaseBalance_Object = MibTableColumn
pduPhaseBalance = _PduPhaseBalance_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 17),
    _PduPhaseBalance_Type()
)
pduPhaseBalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseBalance.setStatus("current")
if mibBuilder.loadTexts:
    pduPhaseBalance.setUnits("%")


class _PduPhaseCurrentCrestFactor_Type(Gauge32):
    """Custom type pduPhaseCurrentCrestFactor based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_PduPhaseCurrentCrestFactor_Type.__name__ = "Gauge32"
_PduPhaseCurrentCrestFactor_Object = MibTableColumn
pduPhaseCurrentCrestFactor = _PduPhaseCurrentCrestFactor_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 19),
    _PduPhaseCurrentCrestFactor_Type()
)
pduPhaseCurrentCrestFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseCurrentCrestFactor.setStatus("current")
_PduBreakerTable_Object = MibTable
pduBreakerTable = _PduBreakerTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 3)
)
if mibBuilder.loadTexts:
    pduBreakerTable.setStatus("current")
_PduBreakerEntry_Object = MibTableRow
pduBreakerEntry = _PduBreakerEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 3, 1)
)
pduBreakerEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "pduBreakerIndex"),
)
if mibBuilder.loadTexts:
    pduBreakerEntry.setStatus("current")


class _PduBreakerIndex_Type(Integer32):
    """Custom type pduBreakerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PduBreakerIndex_Type.__name__ = "Integer32"
_PduBreakerIndex_Object = MibTableColumn
pduBreakerIndex = _PduBreakerIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 3, 1, 1),
    _PduBreakerIndex_Type()
)
pduBreakerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduBreakerIndex.setStatus("current")


class _PduBreakerName_Type(SnmpAdminString):
    """Custom type pduBreakerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_PduBreakerName_Type.__name__ = "SnmpAdminString"
_PduBreakerName_Object = MibTableColumn
pduBreakerName = _PduBreakerName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 3, 1, 2),
    _PduBreakerName_Type()
)
pduBreakerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBreakerName.setStatus("current")


class _PduBreakerLabel_Type(SnmpAdminString):
    """Custom type pduBreakerLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_PduBreakerLabel_Type.__name__ = "SnmpAdminString"
_PduBreakerLabel_Object = MibTableColumn
pduBreakerLabel = _PduBreakerLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 3, 1, 3),
    _PduBreakerLabel_Type()
)
pduBreakerLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduBreakerLabel.setStatus("current")


class _PduBreakerCurrent_Type(Gauge32):
    """Custom type pduBreakerCurrent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9900),
    )


_PduBreakerCurrent_Type.__name__ = "Gauge32"
_PduBreakerCurrent_Object = MibTableColumn
pduBreakerCurrent = _PduBreakerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 3, 1, 4),
    _PduBreakerCurrent_Type()
)
pduBreakerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBreakerCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pduBreakerCurrent.setUnits("centiamps (rms)")


class _PduBreakerVoltage_Type(Gauge32):
    """Custom type pduBreakerVoltage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3100),
    )


_PduBreakerVoltage_Type.__name__ = "Gauge32"
_PduBreakerVoltage_Object = MibTableColumn
pduBreakerVoltage = _PduBreakerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 3, 1, 8),
    _PduBreakerVoltage_Type()
)
pduBreakerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBreakerVoltage.setStatus("current")
if mibBuilder.loadTexts:
    pduBreakerVoltage.setUnits("decivolts (rms)")


class _PduBreakerRealPower_Type(Gauge32):
    """Custom type pduBreakerRealPower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_PduBreakerRealPower_Type.__name__ = "Gauge32"
_PduBreakerRealPower_Object = MibTableColumn
pduBreakerRealPower = _PduBreakerRealPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 3, 1, 12),
    _PduBreakerRealPower_Type()
)
pduBreakerRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBreakerRealPower.setStatus("current")
if mibBuilder.loadTexts:
    pduBreakerRealPower.setUnits("watts")


class _PduBreakerApparentPower_Type(Gauge32):
    """Custom type pduBreakerApparentPower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_PduBreakerApparentPower_Type.__name__ = "Gauge32"
_PduBreakerApparentPower_Object = MibTableColumn
pduBreakerApparentPower = _PduBreakerApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 3, 1, 13),
    _PduBreakerApparentPower_Type()
)
pduBreakerApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBreakerApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    pduBreakerApparentPower.setUnits("volt-amps")


class _PduBreakerPowerFactor_Type(Gauge32):
    """Custom type pduBreakerPowerFactor based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PduBreakerPowerFactor_Type.__name__ = "Gauge32"
_PduBreakerPowerFactor_Object = MibTableColumn
pduBreakerPowerFactor = _PduBreakerPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 3, 1, 14),
    _PduBreakerPowerFactor_Type()
)
pduBreakerPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBreakerPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    pduBreakerPowerFactor.setUnits("%")


class _PduBreakerEnergy_Type(Gauge32):
    """Custom type pduBreakerEnergy based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999000),
    )


_PduBreakerEnergy_Type.__name__ = "Gauge32"
_PduBreakerEnergy_Object = MibTableColumn
pduBreakerEnergy = _PduBreakerEnergy_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 3, 1, 15),
    _PduBreakerEnergy_Type()
)
pduBreakerEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBreakerEnergy.setStatus("current")
if mibBuilder.loadTexts:
    pduBreakerEnergy.setUnits("watt-hours")
_PduLineTable_Object = MibTable
pduLineTable = _PduLineTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 4)
)
if mibBuilder.loadTexts:
    pduLineTable.setStatus("current")
_PduLineEntry_Object = MibTableRow
pduLineEntry = _PduLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 4, 1)
)
pduLineEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "pduLineIndex"),
)
if mibBuilder.loadTexts:
    pduLineEntry.setStatus("current")


class _PduLineIndex_Type(Integer32):
    """Custom type pduLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PduLineIndex_Type.__name__ = "Integer32"
_PduLineIndex_Object = MibTableColumn
pduLineIndex = _PduLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 4, 1, 1),
    _PduLineIndex_Type()
)
pduLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduLineIndex.setStatus("current")


class _PduLineName_Type(SnmpAdminString):
    """Custom type pduLineName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_PduLineName_Type.__name__ = "SnmpAdminString"
_PduLineName_Object = MibTableColumn
pduLineName = _PduLineName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 4, 1, 2),
    _PduLineName_Type()
)
pduLineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduLineName.setStatus("current")


class _PduLineLabel_Type(SnmpAdminString):
    """Custom type pduLineLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_PduLineLabel_Type.__name__ = "SnmpAdminString"
_PduLineLabel_Object = MibTableColumn
pduLineLabel = _PduLineLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 4, 1, 3),
    _PduLineLabel_Type()
)
pduLineLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduLineLabel.setStatus("current")


class _PduLineCurrent_Type(Gauge32):
    """Custom type pduLineCurrent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9900),
    )


_PduLineCurrent_Type.__name__ = "Gauge32"
_PduLineCurrent_Object = MibTableColumn
pduLineCurrent = _PduLineCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 4, 1, 4),
    _PduLineCurrent_Type()
)
pduLineCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduLineCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pduLineCurrent.setUnits("centiamps (rms)")
_PduOutletSwitchTable_Object = MibTable
pduOutletSwitchTable = _PduOutletSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 5)
)
if mibBuilder.loadTexts:
    pduOutletSwitchTable.setStatus("current")
_PduOutletSwitchEntry_Object = MibTableRow
pduOutletSwitchEntry = _PduOutletSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 5, 1)
)
pduOutletSwitchEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "pduOutletSwitchIndex"),
)
if mibBuilder.loadTexts:
    pduOutletSwitchEntry.setStatus("current")


class _PduOutletSwitchIndex_Type(Integer32):
    """Custom type pduOutletSwitchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PduOutletSwitchIndex_Type.__name__ = "Integer32"
_PduOutletSwitchIndex_Object = MibTableColumn
pduOutletSwitchIndex = _PduOutletSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 5, 1, 1),
    _PduOutletSwitchIndex_Type()
)
pduOutletSwitchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduOutletSwitchIndex.setStatus("current")


class _PduOutletSwitchName_Type(SnmpAdminString):
    """Custom type pduOutletSwitchName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_PduOutletSwitchName_Type.__name__ = "SnmpAdminString"
_PduOutletSwitchName_Object = MibTableColumn
pduOutletSwitchName = _PduOutletSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 5, 1, 2),
    _PduOutletSwitchName_Type()
)
pduOutletSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchName.setStatus("current")


class _PduOutletSwitchLabel_Type(SnmpAdminString):
    """Custom type pduOutletSwitchLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_PduOutletSwitchLabel_Type.__name__ = "SnmpAdminString"
_PduOutletSwitchLabel_Object = MibTableColumn
pduOutletSwitchLabel = _PduOutletSwitchLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 5, 1, 3),
    _PduOutletSwitchLabel_Type()
)
pduOutletSwitchLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchLabel.setStatus("current")


class _PduOutletSwitchState_Type(Integer32):
    """Custom type pduOutletSwitchState based on Integer32"""
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
        *(("on", 1),
          ("off", 2),
          ("on2off", 3),
          ("off2on", 4),
          ("rebootOn", 5),
          ("rebootOff", 6),
          ("unavailable", 7))
    )


_PduOutletSwitchState_Type.__name__ = "Integer32"
_PduOutletSwitchState_Object = MibTableColumn
pduOutletSwitchState = _PduOutletSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 5, 1, 4),
    _PduOutletSwitchState_Type()
)
pduOutletSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchState.setStatus("current")
_PduOutletSwitchRelayFailure_Type = TruthValue
_PduOutletSwitchRelayFailure_Object = MibTableColumn
pduOutletSwitchRelayFailure = _PduOutletSwitchRelayFailure_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 5, 1, 5),
    _PduOutletSwitchRelayFailure_Type()
)
pduOutletSwitchRelayFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchRelayFailure.setStatus("current")


class _PduOutletSwitchControl_Type(Integer32):
    """Custom type pduOutletSwitchControl based on Integer32"""
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
        *(("cancel", 1),
          ("on", 2),
          ("onAfterDelay", 3),
          ("off", 4),
          ("offAfterDelay", 5),
          ("reboot", 6),
          ("rebootAfterDelay", 7),
          ("none", 8))
    )


_PduOutletSwitchControl_Type.__name__ = "Integer32"
_PduOutletSwitchControl_Object = MibTableColumn
pduOutletSwitchControl = _PduOutletSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 5, 1, 6),
    _PduOutletSwitchControl_Type()
)
pduOutletSwitchControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchControl.setStatus("current")


class _PduOutletSwitchTimeToAction_Type(Integer32):
    """Custom type pduOutletSwitchTimeToAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_PduOutletSwitchTimeToAction_Type.__name__ = "Integer32"
_PduOutletSwitchTimeToAction_Object = MibTableColumn
pduOutletSwitchTimeToAction = _PduOutletSwitchTimeToAction_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 5, 1, 7),
    _PduOutletSwitchTimeToAction_Type()
)
pduOutletSwitchTimeToAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchTimeToAction.setStatus("current")


class _PduOutletSwitchOnDelay_Type(Integer32):
    """Custom type pduOutletSwitchOnDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_PduOutletSwitchOnDelay_Type.__name__ = "Integer32"
_PduOutletSwitchOnDelay_Object = MibTableColumn
pduOutletSwitchOnDelay = _PduOutletSwitchOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 5, 1, 8),
    _PduOutletSwitchOnDelay_Type()
)
pduOutletSwitchOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchOnDelay.setStatus("current")


class _PduOutletSwitchOffDelay_Type(Integer32):
    """Custom type pduOutletSwitchOffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_PduOutletSwitchOffDelay_Type.__name__ = "Integer32"
_PduOutletSwitchOffDelay_Object = MibTableColumn
pduOutletSwitchOffDelay = _PduOutletSwitchOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 5, 1, 9),
    _PduOutletSwitchOffDelay_Type()
)
pduOutletSwitchOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchOffDelay.setStatus("current")


class _PduOutletSwitchRebootDelay_Type(Integer32):
    """Custom type pduOutletSwitchRebootDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_PduOutletSwitchRebootDelay_Type.__name__ = "Integer32"
_PduOutletSwitchRebootDelay_Object = MibTableColumn
pduOutletSwitchRebootDelay = _PduOutletSwitchRebootDelay_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 5, 1, 10),
    _PduOutletSwitchRebootDelay_Type()
)
pduOutletSwitchRebootDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchRebootDelay.setStatus("current")


class _PduOutletSwitchRebootHoldDelay_Type(Integer32):
    """Custom type pduOutletSwitchRebootHoldDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_PduOutletSwitchRebootHoldDelay_Type.__name__ = "Integer32"
_PduOutletSwitchRebootHoldDelay_Object = MibTableColumn
pduOutletSwitchRebootHoldDelay = _PduOutletSwitchRebootHoldDelay_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 5, 1, 11),
    _PduOutletSwitchRebootHoldDelay_Type()
)
pduOutletSwitchRebootHoldDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchRebootHoldDelay.setStatus("current")


class _PduOutletSwitchPoaAction_Type(Integer32):
    """Custom type pduOutletSwitchPoaAction based on Integer32"""
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
          ("off", 2),
          ("last", 3))
    )


_PduOutletSwitchPoaAction_Type.__name__ = "Integer32"
_PduOutletSwitchPoaAction_Object = MibTableColumn
pduOutletSwitchPoaAction = _PduOutletSwitchPoaAction_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 5, 1, 12),
    _PduOutletSwitchPoaAction_Type()
)
pduOutletSwitchPoaAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchPoaAction.setStatus("current")


class _PduOutletSwitchPoaDelay_Type(Integer32):
    """Custom type pduOutletSwitchPoaDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_PduOutletSwitchPoaDelay_Type.__name__ = "Integer32"
_PduOutletSwitchPoaDelay_Object = MibTableColumn
pduOutletSwitchPoaDelay = _PduOutletSwitchPoaDelay_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 5, 1, 13),
    _PduOutletSwitchPoaDelay_Type()
)
pduOutletSwitchPoaDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchPoaDelay.setStatus("current")
_PduOutletMeterTable_Object = MibTable
pduOutletMeterTable = _PduOutletMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 6)
)
if mibBuilder.loadTexts:
    pduOutletMeterTable.setStatus("current")
_PduOutletMeterEntry_Object = MibTableRow
pduOutletMeterEntry = _PduOutletMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 6, 1)
)
pduOutletMeterEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "pduOutletMeterIndex"),
)
if mibBuilder.loadTexts:
    pduOutletMeterEntry.setStatus("current")


class _PduOutletMeterIndex_Type(Integer32):
    """Custom type pduOutletMeterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PduOutletMeterIndex_Type.__name__ = "Integer32"
_PduOutletMeterIndex_Object = MibTableColumn
pduOutletMeterIndex = _PduOutletMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 6, 1, 1),
    _PduOutletMeterIndex_Type()
)
pduOutletMeterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduOutletMeterIndex.setStatus("current")


class _PduOutletMeterName_Type(SnmpAdminString):
    """Custom type pduOutletMeterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_PduOutletMeterName_Type.__name__ = "SnmpAdminString"
_PduOutletMeterName_Object = MibTableColumn
pduOutletMeterName = _PduOutletMeterName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 6, 1, 2),
    _PduOutletMeterName_Type()
)
pduOutletMeterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeterName.setStatus("current")


class _PduOutletMeterLabel_Type(SnmpAdminString):
    """Custom type pduOutletMeterLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_PduOutletMeterLabel_Type.__name__ = "SnmpAdminString"
_PduOutletMeterLabel_Object = MibTableColumn
pduOutletMeterLabel = _PduOutletMeterLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 6, 1, 3),
    _PduOutletMeterLabel_Type()
)
pduOutletMeterLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletMeterLabel.setStatus("current")


class _PduOutletMeterVoltage_Type(Gauge32):
    """Custom type pduOutletMeterVoltage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3100),
    )


_PduOutletMeterVoltage_Type.__name__ = "Gauge32"
_PduOutletMeterVoltage_Object = MibTableColumn
pduOutletMeterVoltage = _PduOutletMeterVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 6, 1, 4),
    _PduOutletMeterVoltage_Type()
)
pduOutletMeterVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeterVoltage.setStatus("current")
if mibBuilder.loadTexts:
    pduOutletMeterVoltage.setUnits("decivolts (rms)")


class _PduOutletMeterCurrent_Type(Gauge32):
    """Custom type pduOutletMeterCurrent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9900),
    )


_PduOutletMeterCurrent_Type.__name__ = "Gauge32"
_PduOutletMeterCurrent_Object = MibTableColumn
pduOutletMeterCurrent = _PduOutletMeterCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 6, 1, 8),
    _PduOutletMeterCurrent_Type()
)
pduOutletMeterCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeterCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pduOutletMeterCurrent.setUnits("centiamps (rms)")


class _PduOutletMeterRealPower_Type(Gauge32):
    """Custom type pduOutletMeterRealPower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_PduOutletMeterRealPower_Type.__name__ = "Gauge32"
_PduOutletMeterRealPower_Object = MibTableColumn
pduOutletMeterRealPower = _PduOutletMeterRealPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 6, 1, 12),
    _PduOutletMeterRealPower_Type()
)
pduOutletMeterRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeterRealPower.setStatus("current")
if mibBuilder.loadTexts:
    pduOutletMeterRealPower.setUnits("watts")


class _PduOutletMeterApparentPower_Type(Gauge32):
    """Custom type pduOutletMeterApparentPower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_PduOutletMeterApparentPower_Type.__name__ = "Gauge32"
_PduOutletMeterApparentPower_Object = MibTableColumn
pduOutletMeterApparentPower = _PduOutletMeterApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 6, 1, 13),
    _PduOutletMeterApparentPower_Type()
)
pduOutletMeterApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeterApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    pduOutletMeterApparentPower.setUnits("volt-amps")


class _PduOutletMeterPowerFactor_Type(Gauge32):
    """Custom type pduOutletMeterPowerFactor based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PduOutletMeterPowerFactor_Type.__name__ = "Gauge32"
_PduOutletMeterPowerFactor_Object = MibTableColumn
pduOutletMeterPowerFactor = _PduOutletMeterPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 6, 1, 14),
    _PduOutletMeterPowerFactor_Type()
)
pduOutletMeterPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeterPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    pduOutletMeterPowerFactor.setUnits("%")


class _PduOutletMeterEnergy_Type(Gauge32):
    """Custom type pduOutletMeterEnergy based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999000),
    )


_PduOutletMeterEnergy_Type.__name__ = "Gauge32"
_PduOutletMeterEnergy_Object = MibTableColumn
pduOutletMeterEnergy = _PduOutletMeterEnergy_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 6, 1, 15),
    _PduOutletMeterEnergy_Type()
)
pduOutletMeterEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeterEnergy.setStatus("current")
if mibBuilder.loadTexts:
    pduOutletMeterEnergy.setUnits("watt-hours")


class _PduOutletMeterReset_Type(Integer32):
    """Custom type pduOutletMeterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8)
        )
    )
    namedValues = NamedValues(
        *(("resetEnergy", 1),
          ("none", 8))
    )


_PduOutletMeterReset_Type.__name__ = "Integer32"
_PduOutletMeterReset_Object = MibTableColumn
pduOutletMeterReset = _PduOutletMeterReset_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 6, 1, 16),
    _PduOutletMeterReset_Type()
)
pduOutletMeterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletMeterReset.setStatus("current")


class _PduOutletCurrentCrestFactor_Type(Gauge32):
    """Custom type pduOutletCurrentCrestFactor based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_PduOutletCurrentCrestFactor_Type.__name__ = "Gauge32"
_PduOutletCurrentCrestFactor_Object = MibTableColumn
pduOutletCurrentCrestFactor = _PduOutletCurrentCrestFactor_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 6, 1, 19),
    _PduOutletCurrentCrestFactor_Type()
)
pduOutletCurrentCrestFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletCurrentCrestFactor.setStatus("current")
_TempSensorTable_Object = MibTable
tempSensorTable = _TempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 4)
)
if mibBuilder.loadTexts:
    tempSensorTable.setStatus("current")
_TempSensorEntry_Object = MibTableRow
tempSensorEntry = _TempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 4, 1)
)
tempSensorEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "tempSensorIndex"),
)
if mibBuilder.loadTexts:
    tempSensorEntry.setStatus("current")


class _TempSensorIndex_Type(Integer32):
    """Custom type tempSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TempSensorIndex_Type.__name__ = "Integer32"
_TempSensorIndex_Object = MibTableColumn
tempSensorIndex = _TempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 4, 1, 1),
    _TempSensorIndex_Type()
)
tempSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tempSensorIndex.setStatus("current")
_TempSensorSerial_Type = DisplayString
_TempSensorSerial_Object = MibTableColumn
tempSensorSerial = _TempSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 4, 1, 2),
    _TempSensorSerial_Type()
)
tempSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorSerial.setStatus("current")


class _TempSensorLabel_Type(SnmpAdminString):
    """Custom type tempSensorLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_TempSensorLabel_Type.__name__ = "SnmpAdminString"
_TempSensorLabel_Object = MibTableColumn
tempSensorLabel = _TempSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 4, 1, 3),
    _TempSensorLabel_Type()
)
tempSensorLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensorLabel.setStatus("current")
_TempSensorAvail_Type = Gauge32
_TempSensorAvail_Object = MibTableColumn
tempSensorAvail = _TempSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 4, 1, 4),
    _TempSensorAvail_Type()
)
tempSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorAvail.setStatus("current")


class _TempSensorTemp_Type(Integer32):
    """Custom type tempSensorTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 2540),
    )


_TempSensorTemp_Type.__name__ = "Integer32"
_TempSensorTemp_Object = MibTableColumn
tempSensorTemp = _TempSensorTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 4, 1, 5),
    _TempSensorTemp_Type()
)
tempSensorTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorTemp.setStatus("current")
if mibBuilder.loadTexts:
    tempSensorTemp.setUnits("decidegrees")
_AirFlowSensorTable_Object = MibTable
airFlowSensorTable = _AirFlowSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 5)
)
if mibBuilder.loadTexts:
    airFlowSensorTable.setStatus("current")
_AirFlowSensorEntry_Object = MibTableRow
airFlowSensorEntry = _AirFlowSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 5, 1)
)
airFlowSensorEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "airFlowSensorIndex"),
)
if mibBuilder.loadTexts:
    airFlowSensorEntry.setStatus("current")


class _AirFlowSensorIndex_Type(Integer32):
    """Custom type airFlowSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AirFlowSensorIndex_Type.__name__ = "Integer32"
_AirFlowSensorIndex_Object = MibTableColumn
airFlowSensorIndex = _AirFlowSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 5, 1, 1),
    _AirFlowSensorIndex_Type()
)
airFlowSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    airFlowSensorIndex.setStatus("current")
_AirFlowSensorSerial_Type = DisplayString
_AirFlowSensorSerial_Object = MibTableColumn
airFlowSensorSerial = _AirFlowSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 5, 1, 2),
    _AirFlowSensorSerial_Type()
)
airFlowSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorSerial.setStatus("current")


class _AirFlowSensorLabel_Type(SnmpAdminString):
    """Custom type airFlowSensorLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_AirFlowSensorLabel_Type.__name__ = "SnmpAdminString"
_AirFlowSensorLabel_Object = MibTableColumn
airFlowSensorLabel = _AirFlowSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 5, 1, 3),
    _AirFlowSensorLabel_Type()
)
airFlowSensorLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    airFlowSensorLabel.setStatus("current")
_AirFlowSensorAvail_Type = Gauge32
_AirFlowSensorAvail_Object = MibTableColumn
airFlowSensorAvail = _AirFlowSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 5, 1, 4),
    _AirFlowSensorAvail_Type()
)
airFlowSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorAvail.setStatus("current")


class _AirFlowSensorTemp_Type(Integer32):
    """Custom type airFlowSensorTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 2540),
    )


_AirFlowSensorTemp_Type.__name__ = "Integer32"
_AirFlowSensorTemp_Object = MibTableColumn
airFlowSensorTemp = _AirFlowSensorTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 5, 1, 5),
    _AirFlowSensorTemp_Type()
)
airFlowSensorTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorTemp.setStatus("current")
if mibBuilder.loadTexts:
    airFlowSensorTemp.setUnits("decidegrees")


class _AirFlowSensorFlow_Type(Integer32):
    """Custom type airFlowSensorFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AirFlowSensorFlow_Type.__name__ = "Integer32"
_AirFlowSensorFlow_Object = MibTableColumn
airFlowSensorFlow = _AirFlowSensorFlow_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 5, 1, 6),
    _AirFlowSensorFlow_Type()
)
airFlowSensorFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorFlow.setStatus("current")


class _AirFlowSensorHumidity_Type(Integer32):
    """Custom type airFlowSensorHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AirFlowSensorHumidity_Type.__name__ = "Integer32"
_AirFlowSensorHumidity_Object = MibTableColumn
airFlowSensorHumidity = _AirFlowSensorHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 5, 1, 7),
    _AirFlowSensorHumidity_Type()
)
airFlowSensorHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorHumidity.setStatus("current")
if mibBuilder.loadTexts:
    airFlowSensorHumidity.setUnits("%")


class _AirFlowSensorDewPoint_Type(Integer32):
    """Custom type airFlowSensorDewPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 2540),
    )


_AirFlowSensorDewPoint_Type.__name__ = "Integer32"
_AirFlowSensorDewPoint_Object = MibTableColumn
airFlowSensorDewPoint = _AirFlowSensorDewPoint_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 5, 1, 8),
    _AirFlowSensorDewPoint_Type()
)
airFlowSensorDewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorDewPoint.setStatus("current")
if mibBuilder.loadTexts:
    airFlowSensorDewPoint.setUnits("decidegrees")
_T3hdSensorTable_Object = MibTable
t3hdSensorTable = _T3hdSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8)
)
if mibBuilder.loadTexts:
    t3hdSensorTable.setStatus("current")
_T3hdSensorEntry_Object = MibTableRow
t3hdSensorEntry = _T3hdSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1)
)
t3hdSensorEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "t3hdSensorIndex"),
)
if mibBuilder.loadTexts:
    t3hdSensorEntry.setStatus("current")


class _T3hdSensorIndex_Type(Integer32):
    """Custom type t3hdSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_T3hdSensorIndex_Type.__name__ = "Integer32"
_T3hdSensorIndex_Object = MibTableColumn
t3hdSensorIndex = _T3hdSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 1),
    _T3hdSensorIndex_Type()
)
t3hdSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t3hdSensorIndex.setStatus("current")
_T3hdSensorSerial_Type = DisplayString
_T3hdSensorSerial_Object = MibTableColumn
t3hdSensorSerial = _T3hdSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 2),
    _T3hdSensorSerial_Type()
)
t3hdSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorSerial.setStatus("current")


class _T3hdSensorLabel_Type(SnmpAdminString):
    """Custom type t3hdSensorLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_T3hdSensorLabel_Type.__name__ = "SnmpAdminString"
_T3hdSensorLabel_Object = MibTableColumn
t3hdSensorLabel = _T3hdSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 3),
    _T3hdSensorLabel_Type()
)
t3hdSensorLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3hdSensorLabel.setStatus("current")
_T3hdSensorAvail_Type = Gauge32
_T3hdSensorAvail_Object = MibTableColumn
t3hdSensorAvail = _T3hdSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 4),
    _T3hdSensorAvail_Type()
)
t3hdSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorAvail.setStatus("current")


class _T3hdSensorIntLabel_Type(SnmpAdminString):
    """Custom type t3hdSensorIntLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_T3hdSensorIntLabel_Type.__name__ = "SnmpAdminString"
_T3hdSensorIntLabel_Object = MibTableColumn
t3hdSensorIntLabel = _T3hdSensorIntLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 5),
    _T3hdSensorIntLabel_Type()
)
t3hdSensorIntLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3hdSensorIntLabel.setStatus("current")


class _T3hdSensorIntTemp_Type(Integer32):
    """Custom type t3hdSensorIntTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 2540),
    )


_T3hdSensorIntTemp_Type.__name__ = "Integer32"
_T3hdSensorIntTemp_Object = MibTableColumn
t3hdSensorIntTemp = _T3hdSensorIntTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 6),
    _T3hdSensorIntTemp_Type()
)
t3hdSensorIntTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorIntTemp.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorIntTemp.setUnits("decidegrees")


class _T3hdSensorIntHumidity_Type(Integer32):
    """Custom type t3hdSensorIntHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_T3hdSensorIntHumidity_Type.__name__ = "Integer32"
_T3hdSensorIntHumidity_Object = MibTableColumn
t3hdSensorIntHumidity = _T3hdSensorIntHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 7),
    _T3hdSensorIntHumidity_Type()
)
t3hdSensorIntHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorIntHumidity.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorIntHumidity.setUnits("%")


class _T3hdSensorIntDewPoint_Type(Integer32):
    """Custom type t3hdSensorIntDewPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 2540),
    )


_T3hdSensorIntDewPoint_Type.__name__ = "Integer32"
_T3hdSensorIntDewPoint_Object = MibTableColumn
t3hdSensorIntDewPoint = _T3hdSensorIntDewPoint_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 8),
    _T3hdSensorIntDewPoint_Type()
)
t3hdSensorIntDewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorIntDewPoint.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorIntDewPoint.setUnits("decidegrees")
_T3hdSensorExtAAvail_Type = Gauge32
_T3hdSensorExtAAvail_Object = MibTableColumn
t3hdSensorExtAAvail = _T3hdSensorExtAAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 9),
    _T3hdSensorExtAAvail_Type()
)
t3hdSensorExtAAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExtAAvail.setStatus("current")


class _T3hdSensorExtALabel_Type(SnmpAdminString):
    """Custom type t3hdSensorExtALabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_T3hdSensorExtALabel_Type.__name__ = "SnmpAdminString"
_T3hdSensorExtALabel_Object = MibTableColumn
t3hdSensorExtALabel = _T3hdSensorExtALabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 10),
    _T3hdSensorExtALabel_Type()
)
t3hdSensorExtALabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3hdSensorExtALabel.setStatus("current")


class _T3hdSensorExtATemp_Type(Integer32):
    """Custom type t3hdSensorExtATemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 2540),
    )


_T3hdSensorExtATemp_Type.__name__ = "Integer32"
_T3hdSensorExtATemp_Object = MibTableColumn
t3hdSensorExtATemp = _T3hdSensorExtATemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 11),
    _T3hdSensorExtATemp_Type()
)
t3hdSensorExtATemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExtATemp.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorExtATemp.setUnits("decidegrees")
_T3hdSensorExtBAvail_Type = Gauge32
_T3hdSensorExtBAvail_Object = MibTableColumn
t3hdSensorExtBAvail = _T3hdSensorExtBAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 12),
    _T3hdSensorExtBAvail_Type()
)
t3hdSensorExtBAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExtBAvail.setStatus("current")


class _T3hdSensorExtBLabel_Type(SnmpAdminString):
    """Custom type t3hdSensorExtBLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_T3hdSensorExtBLabel_Type.__name__ = "SnmpAdminString"
_T3hdSensorExtBLabel_Object = MibTableColumn
t3hdSensorExtBLabel = _T3hdSensorExtBLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 13),
    _T3hdSensorExtBLabel_Type()
)
t3hdSensorExtBLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3hdSensorExtBLabel.setStatus("current")


class _T3hdSensorExtBTemp_Type(Integer32):
    """Custom type t3hdSensorExtBTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 2540),
    )


_T3hdSensorExtBTemp_Type.__name__ = "Integer32"
_T3hdSensorExtBTemp_Object = MibTableColumn
t3hdSensorExtBTemp = _T3hdSensorExtBTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 14),
    _T3hdSensorExtBTemp_Type()
)
t3hdSensorExtBTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExtBTemp.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorExtBTemp.setUnits("decidegrees")
_ThdSensorTable_Object = MibTable
thdSensorTable = _ThdSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 9)
)
if mibBuilder.loadTexts:
    thdSensorTable.setStatus("current")
_ThdSensorEntry_Object = MibTableRow
thdSensorEntry = _ThdSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 9, 1)
)
thdSensorEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "thdSensorIndex"),
)
if mibBuilder.loadTexts:
    thdSensorEntry.setStatus("current")


class _ThdSensorIndex_Type(Integer32):
    """Custom type thdSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ThdSensorIndex_Type.__name__ = "Integer32"
_ThdSensorIndex_Object = MibTableColumn
thdSensorIndex = _ThdSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 9, 1, 1),
    _ThdSensorIndex_Type()
)
thdSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    thdSensorIndex.setStatus("current")
_ThdSensorSerial_Type = DisplayString
_ThdSensorSerial_Object = MibTableColumn
thdSensorSerial = _ThdSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 9, 1, 2),
    _ThdSensorSerial_Type()
)
thdSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorSerial.setStatus("current")


class _ThdSensorLabel_Type(SnmpAdminString):
    """Custom type thdSensorLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_ThdSensorLabel_Type.__name__ = "SnmpAdminString"
_ThdSensorLabel_Object = MibTableColumn
thdSensorLabel = _ThdSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 9, 1, 3),
    _ThdSensorLabel_Type()
)
thdSensorLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thdSensorLabel.setStatus("current")
_ThdSensorAvail_Type = Gauge32
_ThdSensorAvail_Object = MibTableColumn
thdSensorAvail = _ThdSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 9, 1, 4),
    _ThdSensorAvail_Type()
)
thdSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorAvail.setStatus("current")


class _ThdSensorTemp_Type(Integer32):
    """Custom type thdSensorTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 2540),
    )


_ThdSensorTemp_Type.__name__ = "Integer32"
_ThdSensorTemp_Object = MibTableColumn
thdSensorTemp = _ThdSensorTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 9, 1, 5),
    _ThdSensorTemp_Type()
)
thdSensorTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorTemp.setStatus("current")
if mibBuilder.loadTexts:
    thdSensorTemp.setUnits("decidegrees")


class _ThdSensorHumidity_Type(Integer32):
    """Custom type thdSensorHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ThdSensorHumidity_Type.__name__ = "Integer32"
_ThdSensorHumidity_Object = MibTableColumn
thdSensorHumidity = _ThdSensorHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 9, 1, 6),
    _ThdSensorHumidity_Type()
)
thdSensorHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorHumidity.setStatus("current")
if mibBuilder.loadTexts:
    thdSensorHumidity.setUnits("%")


class _ThdSensorDewPoint_Type(Integer32):
    """Custom type thdSensorDewPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 2540),
    )


_ThdSensorDewPoint_Type.__name__ = "Integer32"
_ThdSensorDewPoint_Object = MibTableColumn
thdSensorDewPoint = _ThdSensorDewPoint_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 9, 1, 7),
    _ThdSensorDewPoint_Type()
)
thdSensorDewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorDewPoint.setStatus("current")
if mibBuilder.loadTexts:
    thdSensorDewPoint.setUnits("decidegrees")
_A2dSensorTable_Object = MibTable
a2dSensorTable = _A2dSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11)
)
if mibBuilder.loadTexts:
    a2dSensorTable.setStatus("current")
_A2dSensorEntry_Object = MibTableRow
a2dSensorEntry = _A2dSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11, 1)
)
a2dSensorEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "a2dSensorIndex"),
)
if mibBuilder.loadTexts:
    a2dSensorEntry.setStatus("current")


class _A2dSensorIndex_Type(Integer32):
    """Custom type a2dSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_A2dSensorIndex_Type.__name__ = "Integer32"
_A2dSensorIndex_Object = MibTableColumn
a2dSensorIndex = _A2dSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11, 1, 1),
    _A2dSensorIndex_Type()
)
a2dSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a2dSensorIndex.setStatus("current")
_A2dSensorSerial_Type = DisplayString
_A2dSensorSerial_Object = MibTableColumn
a2dSensorSerial = _A2dSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11, 1, 2),
    _A2dSensorSerial_Type()
)
a2dSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2dSensorSerial.setStatus("current")


class _A2dSensorLabel_Type(SnmpAdminString):
    """Custom type a2dSensorLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_A2dSensorLabel_Type.__name__ = "SnmpAdminString"
_A2dSensorLabel_Object = MibTableColumn
a2dSensorLabel = _A2dSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11, 1, 3),
    _A2dSensorLabel_Type()
)
a2dSensorLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2dSensorLabel.setStatus("current")
_A2dSensorAvail_Type = Gauge32
_A2dSensorAvail_Object = MibTableColumn
a2dSensorAvail = _A2dSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11, 1, 4),
    _A2dSensorAvail_Type()
)
a2dSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2dSensorAvail.setStatus("current")


class _A2dSensorValue_Type(Integer32):
    """Custom type a2dSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000, 1000000),
    )


_A2dSensorValue_Type.__name__ = "Integer32"
_A2dSensorValue_Object = MibTableColumn
a2dSensorValue = _A2dSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11, 1, 5),
    _A2dSensorValue_Type()
)
a2dSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2dSensorValue.setStatus("current")


class _A2dSensorDisplayValue_Type(SnmpAdminString):
    """Custom type a2dSensorDisplayValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_A2dSensorDisplayValue_Type.__name__ = "SnmpAdminString"
_A2dSensorDisplayValue_Object = MibTableColumn
a2dSensorDisplayValue = _A2dSensorDisplayValue_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11, 1, 6),
    _A2dSensorDisplayValue_Type()
)
a2dSensorDisplayValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2dSensorDisplayValue.setStatus("current")


class _A2dSensorMode_Type(Integer32):
    """Custom type a2dSensorMode based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("door", 1),
          ("powerFailure", 2),
          ("flood", 3),
          ("wscLeak", 4),
          ("wscFault", 5),
          ("smoke", 6),
          ("ivsNegGnd", 7),
          ("ivsPosGnd", 8),
          ("customVoltage", 9),
          ("customBinary", 10),
          ("customCurrent", 11))
    )


_A2dSensorMode_Type.__name__ = "Integer32"
_A2dSensorMode_Object = MibTableColumn
a2dSensorMode = _A2dSensorMode_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11, 1, 7),
    _A2dSensorMode_Type()
)
a2dSensorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2dSensorMode.setStatus("current")


class _A2dSensorUnits_Type(SnmpAdminString):
    """Custom type a2dSensorUnits based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_A2dSensorUnits_Type.__name__ = "SnmpAdminString"
_A2dSensorUnits_Object = MibTableColumn
a2dSensorUnits = _A2dSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11, 1, 8),
    _A2dSensorUnits_Type()
)
a2dSensorUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2dSensorUnits.setStatus("current")


class _A2dSensorMin_Type(Integer32):
    """Custom type a2dSensorMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000, 1000000),
    )


_A2dSensorMin_Type.__name__ = "Integer32"
_A2dSensorMin_Object = MibTableColumn
a2dSensorMin = _A2dSensorMin_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11, 1, 9),
    _A2dSensorMin_Type()
)
a2dSensorMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2dSensorMin.setStatus("current")


class _A2dSensorMax_Type(Integer32):
    """Custom type a2dSensorMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000, 1000000),
    )


_A2dSensorMax_Type.__name__ = "Integer32"
_A2dSensorMax_Object = MibTableColumn
a2dSensorMax = _A2dSensorMax_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11, 1, 10),
    _A2dSensorMax_Type()
)
a2dSensorMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2dSensorMax.setStatus("current")


class _A2dSensorLowLabel_Type(SnmpAdminString):
    """Custom type a2dSensorLowLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_A2dSensorLowLabel_Type.__name__ = "SnmpAdminString"
_A2dSensorLowLabel_Object = MibTableColumn
a2dSensorLowLabel = _A2dSensorLowLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11, 1, 11),
    _A2dSensorLowLabel_Type()
)
a2dSensorLowLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2dSensorLowLabel.setStatus("current")


class _A2dSensorHighLabel_Type(SnmpAdminString):
    """Custom type a2dSensorHighLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_A2dSensorHighLabel_Type.__name__ = "SnmpAdminString"
_A2dSensorHighLabel_Object = MibTableColumn
a2dSensorHighLabel = _A2dSensorHighLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11, 1, 12),
    _A2dSensorHighLabel_Type()
)
a2dSensorHighLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2dSensorHighLabel.setStatus("current")


class _A2dSensorAnalogLabel_Type(SnmpAdminString):
    """Custom type a2dSensorAnalogLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_A2dSensorAnalogLabel_Type.__name__ = "SnmpAdminString"
_A2dSensorAnalogLabel_Object = MibTableColumn
a2dSensorAnalogLabel = _A2dSensorAnalogLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11, 1, 13),
    _A2dSensorAnalogLabel_Type()
)
a2dSensorAnalogLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2dSensorAnalogLabel.setStatus("current")
_HumiditySensorTable_Object = MibTable
humiditySensorTable = _HumiditySensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 12)
)
if mibBuilder.loadTexts:
    humiditySensorTable.setStatus("current")
_HumiditySensorEntry_Object = MibTableRow
humiditySensorEntry = _HumiditySensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 12, 1)
)
humiditySensorEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "humiditySensorIndex"),
)
if mibBuilder.loadTexts:
    humiditySensorEntry.setStatus("current")


class _HumiditySensorIndex_Type(Integer32):
    """Custom type humiditySensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HumiditySensorIndex_Type.__name__ = "Integer32"
_HumiditySensorIndex_Object = MibTableColumn
humiditySensorIndex = _HumiditySensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 12, 1, 1),
    _HumiditySensorIndex_Type()
)
humiditySensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    humiditySensorIndex.setStatus("current")
_HumiditySensorSerial_Type = DisplayString
_HumiditySensorSerial_Object = MibTableColumn
humiditySensorSerial = _HumiditySensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 12, 1, 2),
    _HumiditySensorSerial_Type()
)
humiditySensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiditySensorSerial.setStatus("current")


class _HumiditySensorLabel_Type(SnmpAdminString):
    """Custom type humiditySensorLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_HumiditySensorLabel_Type.__name__ = "SnmpAdminString"
_HumiditySensorLabel_Object = MibTableColumn
humiditySensorLabel = _HumiditySensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 12, 1, 3),
    _HumiditySensorLabel_Type()
)
humiditySensorLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humiditySensorLabel.setStatus("current")
_HumiditySensorAvail_Type = Gauge32
_HumiditySensorAvail_Object = MibTableColumn
humiditySensorAvail = _HumiditySensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 12, 1, 4),
    _HumiditySensorAvail_Type()
)
humiditySensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiditySensorAvail.setStatus("current")


class _HumiditySensorValue_Type(Integer32):
    """Custom type humiditySensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HumiditySensorValue_Type.__name__ = "Integer32"
_HumiditySensorValue_Object = MibTableColumn
humiditySensorValue = _HumiditySensorValue_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 12, 1, 5),
    _HumiditySensorValue_Type()
)
humiditySensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiditySensorValue.setStatus("current")
_Sn2dSensorTable_Object = MibTable
sn2dSensorTable = _Sn2dSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 13)
)
if mibBuilder.loadTexts:
    sn2dSensorTable.setStatus("current")
_Sn2dSensorEntry_Object = MibTableRow
sn2dSensorEntry = _Sn2dSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 13, 1)
)
sn2dSensorEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "sn2dSensorIndex"),
)
if mibBuilder.loadTexts:
    sn2dSensorEntry.setStatus("current")


class _Sn2dSensorIndex_Type(Integer32):
    """Custom type sn2dSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Sn2dSensorIndex_Type.__name__ = "Integer32"
_Sn2dSensorIndex_Object = MibTableColumn
sn2dSensorIndex = _Sn2dSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 13, 1, 1),
    _Sn2dSensorIndex_Type()
)
sn2dSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sn2dSensorIndex.setStatus("current")
_Sn2dSensorSerial_Type = DisplayString
_Sn2dSensorSerial_Object = MibTableColumn
sn2dSensorSerial = _Sn2dSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 13, 1, 2),
    _Sn2dSensorSerial_Type()
)
sn2dSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sn2dSensorSerial.setStatus("current")


class _Sn2dSensorLabel_Type(SnmpAdminString):
    """Custom type sn2dSensorLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_Sn2dSensorLabel_Type.__name__ = "SnmpAdminString"
_Sn2dSensorLabel_Object = MibTableColumn
sn2dSensorLabel = _Sn2dSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 13, 1, 3),
    _Sn2dSensorLabel_Type()
)
sn2dSensorLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sn2dSensorLabel.setStatus("current")
_Sn2dSensorAvail_Type = Gauge32
_Sn2dSensorAvail_Object = MibTableColumn
sn2dSensorAvail = _Sn2dSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 13, 1, 4),
    _Sn2dSensorAvail_Type()
)
sn2dSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sn2dSensorAvail.setStatus("current")


class _Sn2dSensorDoor1Label_Type(SnmpAdminString):
    """Custom type sn2dSensorDoor1Label based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_Sn2dSensorDoor1Label_Type.__name__ = "SnmpAdminString"
_Sn2dSensorDoor1Label_Object = MibTableColumn
sn2dSensorDoor1Label = _Sn2dSensorDoor1Label_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 13, 1, 5),
    _Sn2dSensorDoor1Label_Type()
)
sn2dSensorDoor1Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sn2dSensorDoor1Label.setStatus("current")


class _Sn2dSensorDoor1State_Type(Integer32):
    """Custom type sn2dSensorDoor1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2))
    )


_Sn2dSensorDoor1State_Type.__name__ = "Integer32"
_Sn2dSensorDoor1State_Object = MibTableColumn
sn2dSensorDoor1State = _Sn2dSensorDoor1State_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 13, 1, 6),
    _Sn2dSensorDoor1State_Type()
)
sn2dSensorDoor1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sn2dSensorDoor1State.setStatus("current")


class _Sn2dSensorDoor1DisplayState_Type(SnmpAdminString):
    """Custom type sn2dSensorDoor1DisplayState based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_Sn2dSensorDoor1DisplayState_Type.__name__ = "SnmpAdminString"
_Sn2dSensorDoor1DisplayState_Object = MibTableColumn
sn2dSensorDoor1DisplayState = _Sn2dSensorDoor1DisplayState_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 13, 1, 7),
    _Sn2dSensorDoor1DisplayState_Type()
)
sn2dSensorDoor1DisplayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sn2dSensorDoor1DisplayState.setStatus("current")


class _Sn2dSensorDoor2Label_Type(SnmpAdminString):
    """Custom type sn2dSensorDoor2Label based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_Sn2dSensorDoor2Label_Type.__name__ = "SnmpAdminString"
_Sn2dSensorDoor2Label_Object = MibTableColumn
sn2dSensorDoor2Label = _Sn2dSensorDoor2Label_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 13, 1, 8),
    _Sn2dSensorDoor2Label_Type()
)
sn2dSensorDoor2Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sn2dSensorDoor2Label.setStatus("current")


class _Sn2dSensorDoor2State_Type(Integer32):
    """Custom type sn2dSensorDoor2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2))
    )


_Sn2dSensorDoor2State_Type.__name__ = "Integer32"
_Sn2dSensorDoor2State_Object = MibTableColumn
sn2dSensorDoor2State = _Sn2dSensorDoor2State_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 13, 1, 9),
    _Sn2dSensorDoor2State_Type()
)
sn2dSensorDoor2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sn2dSensorDoor2State.setStatus("current")


class _Sn2dSensorDoor2DisplayState_Type(SnmpAdminString):
    """Custom type sn2dSensorDoor2DisplayState based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_Sn2dSensorDoor2DisplayState_Type.__name__ = "SnmpAdminString"
_Sn2dSensorDoor2DisplayState_Object = MibTableColumn
sn2dSensorDoor2DisplayState = _Sn2dSensorDoor2DisplayState_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 13, 1, 10),
    _Sn2dSensorDoor2DisplayState_Type()
)
sn2dSensorDoor2DisplayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sn2dSensorDoor2DisplayState.setStatus("current")
_Cooling_ObjectIdentity = ObjectIdentity
cooling = _Cooling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30)
)
_Vrc_ObjectIdentity = ObjectIdentity
vrc = _Vrc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1)
)
_VrcMainTable_Object = MibTable
vrcMainTable = _VrcMainTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 1)
)
if mibBuilder.loadTexts:
    vrcMainTable.setStatus("current")
_VrcMainEntry_Object = MibTableRow
vrcMainEntry = _VrcMainEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 1, 1)
)
vrcMainEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "vrcMainIndex"),
)
if mibBuilder.loadTexts:
    vrcMainEntry.setStatus("current")


class _VrcMainIndex_Type(Integer32):
    """Custom type vrcMainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrcMainIndex_Type.__name__ = "Integer32"
_VrcMainIndex_Object = MibTableColumn
vrcMainIndex = _VrcMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 1, 1, 1),
    _VrcMainIndex_Type()
)
vrcMainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrcMainIndex.setStatus("current")
_VrcMainSerial_Type = DisplayString
_VrcMainSerial_Object = MibTableColumn
vrcMainSerial = _VrcMainSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 1, 1, 2),
    _VrcMainSerial_Type()
)
vrcMainSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainSerial.setStatus("current")


class _VrcMainName_Type(SnmpAdminString):
    """Custom type vrcMainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_VrcMainName_Type.__name__ = "SnmpAdminString"
_VrcMainName_Object = MibTableColumn
vrcMainName = _VrcMainName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 1, 1, 3),
    _VrcMainName_Type()
)
vrcMainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainName.setStatus("current")


class _VrcMainLabel_Type(SnmpAdminString):
    """Custom type vrcMainLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_VrcMainLabel_Type.__name__ = "SnmpAdminString"
_VrcMainLabel_Object = MibTableColumn
vrcMainLabel = _VrcMainLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 1, 1, 4),
    _VrcMainLabel_Type()
)
vrcMainLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainLabel.setStatus("current")
_VrcMainAvail_Type = Gauge32
_VrcMainAvail_Object = MibTableColumn
vrcMainAvail = _VrcMainAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 1, 1, 5),
    _VrcMainAvail_Type()
)
vrcMainAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainAvail.setStatus("current")
_VrcMainPtTable_Object = MibTable
vrcMainPtTable = _VrcMainPtTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2)
)
if mibBuilder.loadTexts:
    vrcMainPtTable.setStatus("current")
_VrcMainPtEntry_Object = MibTableRow
vrcMainPtEntry = _VrcMainPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1)
)
vrcMainPtEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "vrcMainPtIndex"),
)
if mibBuilder.loadTexts:
    vrcMainPtEntry.setStatus("current")


class _VrcMainPtIndex_Type(Integer32):
    """Custom type vrcMainPtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrcMainPtIndex_Type.__name__ = "Integer32"
_VrcMainPtIndex_Object = MibTableColumn
vrcMainPtIndex = _VrcMainPtIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 1),
    _VrcMainPtIndex_Type()
)
vrcMainPtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrcMainPtIndex.setStatus("current")


class _VrcMainPtRunState_Type(Integer32):
    """Custom type vrcMainPtRunState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_VrcMainPtRunState_Type.__name__ = "Integer32"
_VrcMainPtRunState_Object = MibTableColumn
vrcMainPtRunState = _VrcMainPtRunState_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 2),
    _VrcMainPtRunState_Type()
)
vrcMainPtRunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtRunState.setStatus("current")


class _VrcMainPtEevOpened_Type(Integer32):
    """Custom type vrcMainPtEevOpened based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrcMainPtEevOpened_Type.__name__ = "Integer32"
_VrcMainPtEevOpened_Object = MibTableColumn
vrcMainPtEevOpened = _VrcMainPtEevOpened_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 3),
    _VrcMainPtEevOpened_Type()
)
vrcMainPtEevOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtEevOpened.setStatus("current")
if mibBuilder.loadTexts:
    vrcMainPtEevOpened.setUnits("%")


class _VrcMainPtAlarmNumbers_Type(Integer32):
    """Custom type vrcMainPtAlarmNumbers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_VrcMainPtAlarmNumbers_Type.__name__ = "Integer32"
_VrcMainPtAlarmNumbers_Object = MibTableColumn
vrcMainPtAlarmNumbers = _VrcMainPtAlarmNumbers_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 4),
    _VrcMainPtAlarmNumbers_Type()
)
vrcMainPtAlarmNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtAlarmNumbers.setStatus("current")


class _VrcMainPtHistoryAlarmNumbers_Type(Integer32):
    """Custom type vrcMainPtHistoryAlarmNumbers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_VrcMainPtHistoryAlarmNumbers_Type.__name__ = "Integer32"
_VrcMainPtHistoryAlarmNumbers_Object = MibTableColumn
vrcMainPtHistoryAlarmNumbers = _VrcMainPtHistoryAlarmNumbers_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 5),
    _VrcMainPtHistoryAlarmNumbers_Type()
)
vrcMainPtHistoryAlarmNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtHistoryAlarmNumbers.setStatus("current")


class _VrcMainPtHpAbnRecordCnt_Type(Integer32):
    """Custom type vrcMainPtHpAbnRecordCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_VrcMainPtHpAbnRecordCnt_Type.__name__ = "Integer32"
_VrcMainPtHpAbnRecordCnt_Object = MibTableColumn
vrcMainPtHpAbnRecordCnt = _VrcMainPtHpAbnRecordCnt_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 6),
    _VrcMainPtHpAbnRecordCnt_Type()
)
vrcMainPtHpAbnRecordCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtHpAbnRecordCnt.setStatus("current")


class _VrcMainPtMonitorBaudrate_Type(Integer32):
    """Custom type vrcMainPtMonitorBaudrate based on Integer32"""
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
        *(("error", 1),
          ("baud1200", 2),
          ("baud2400", 3),
          ("baud4800", 4),
          ("baud9600", 5),
          ("baud19200", 6))
    )


_VrcMainPtMonitorBaudrate_Type.__name__ = "Integer32"
_VrcMainPtMonitorBaudrate_Object = MibTableColumn
vrcMainPtMonitorBaudrate = _VrcMainPtMonitorBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 7),
    _VrcMainPtMonitorBaudrate_Type()
)
vrcMainPtMonitorBaudrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtMonitorBaudrate.setStatus("current")


class _VrcMainPtMonitorAddress_Type(Integer32):
    """Custom type vrcMainPtMonitorAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 247),
    )


_VrcMainPtMonitorAddress_Type.__name__ = "Integer32"
_VrcMainPtMonitorAddress_Object = MibTableColumn
vrcMainPtMonitorAddress = _VrcMainPtMonitorAddress_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 8),
    _VrcMainPtMonitorAddress_Type()
)
vrcMainPtMonitorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtMonitorAddress.setStatus("current")
_VrcMainPtLp_Type = TruthValue
_VrcMainPtLp_Object = MibTableColumn
vrcMainPtLp = _VrcMainPtLp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 9),
    _VrcMainPtLp_Type()
)
vrcMainPtLp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtLp.setStatus("current")
_VrcMainPtFilterMaintRemind_Type = TruthValue
_VrcMainPtFilterMaintRemind_Object = MibTableColumn
vrcMainPtFilterMaintRemind = _VrcMainPtFilterMaintRemind_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 10),
    _VrcMainPtFilterMaintRemind_Type()
)
vrcMainPtFilterMaintRemind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtFilterMaintRemind.setStatus("current")
_VrcMainPtCoolingFlag_Type = TruthValue
_VrcMainPtCoolingFlag_Object = MibTableColumn
vrcMainPtCoolingFlag = _VrcMainPtCoolingFlag_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 11),
    _VrcMainPtCoolingFlag_Type()
)
vrcMainPtCoolingFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtCoolingFlag.setStatus("current")
_VrcMainPtFirstOnFlag_Type = TruthValue
_VrcMainPtFirstOnFlag_Object = MibTableColumn
vrcMainPtFirstOnFlag = _VrcMainPtFirstOnFlag_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 12),
    _VrcMainPtFirstOnFlag_Type()
)
vrcMainPtFirstOnFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtFirstOnFlag.setStatus("current")
_VrcMainPtNewAlarmFlag_Type = TruthValue
_VrcMainPtNewAlarmFlag_Object = MibTableColumn
vrcMainPtNewAlarmFlag = _VrcMainPtNewAlarmFlag_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 13),
    _VrcMainPtNewAlarmFlag_Type()
)
vrcMainPtNewAlarmFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtNewAlarmFlag.setStatus("current")
_VrcMainPtComAlarmOutState_Type = TruthValue
_VrcMainPtComAlarmOutState_Object = MibTableColumn
vrcMainPtComAlarmOutState = _VrcMainPtComAlarmOutState_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 14),
    _VrcMainPtComAlarmOutState_Type()
)
vrcMainPtComAlarmOutState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtComAlarmOutState.setStatus("current")
_VrcMainPtHighWaterInput_Type = TruthValue
_VrcMainPtHighWaterInput_Object = MibTableColumn
vrcMainPtHighWaterInput = _VrcMainPtHighWaterInput_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 15),
    _VrcMainPtHighWaterInput_Type()
)
vrcMainPtHighWaterInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtHighWaterInput.setStatus("current")
_VrcMainPtHighWaterAlarm_Type = TruthValue
_VrcMainPtHighWaterAlarm_Object = MibTableColumn
vrcMainPtHighWaterAlarm = _VrcMainPtHighWaterAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 16),
    _VrcMainPtHighWaterAlarm_Type()
)
vrcMainPtHighWaterAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtHighWaterAlarm.setStatus("current")
_VrcMainPtWaterUnderFloorAlarm_Type = TruthValue
_VrcMainPtWaterUnderFloorAlarm_Object = MibTableColumn
vrcMainPtWaterUnderFloorAlarm = _VrcMainPtWaterUnderFloorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 17),
    _VrcMainPtWaterUnderFloorAlarm_Type()
)
vrcMainPtWaterUnderFloorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtWaterUnderFloorAlarm.setStatus("current")
_VrcMainPtSwShutDownStatus_Type = TruthValue
_VrcMainPtSwShutDownStatus_Object = MibTableColumn
vrcMainPtSwShutDownStatus = _VrcMainPtSwShutDownStatus_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 18),
    _VrcMainPtSwShutDownStatus_Type()
)
vrcMainPtSwShutDownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtSwShutDownStatus.setStatus("current")
_VrcMainPtRemoteShutdown_Type = TruthValue
_VrcMainPtRemoteShutdown_Object = MibTableColumn
vrcMainPtRemoteShutdown = _VrcMainPtRemoteShutdown_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 19),
    _VrcMainPtRemoteShutdown_Type()
)
vrcMainPtRemoteShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtRemoteShutdown.setStatus("current")
_VrcMainPtRemoteShutDownFlag_Type = TruthValue
_VrcMainPtRemoteShutDownFlag_Object = MibTableColumn
vrcMainPtRemoteShutDownFlag = _VrcMainPtRemoteShutDownFlag_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 20),
    _VrcMainPtRemoteShutDownFlag_Type()
)
vrcMainPtRemoteShutDownFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtRemoteShutDownFlag.setStatus("current")
_VrcMainPtRemoteShutDownAlarm_Type = TruthValue
_VrcMainPtRemoteShutDownAlarm_Object = MibTableColumn
vrcMainPtRemoteShutDownAlarm = _VrcMainPtRemoteShutDownAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 21),
    _VrcMainPtRemoteShutDownAlarm_Type()
)
vrcMainPtRemoteShutDownAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtRemoteShutDownAlarm.setStatus("current")
_VrcMainPtHmiShutDownFlag_Type = TruthValue
_VrcMainPtHmiShutDownFlag_Object = MibTableColumn
vrcMainPtHmiShutDownFlag = _VrcMainPtHmiShutDownFlag_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 22),
    _VrcMainPtHmiShutDownFlag_Type()
)
vrcMainPtHmiShutDownFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtHmiShutDownFlag.setStatus("current")
_VrcMainPtLpAlarm_Type = TruthValue
_VrcMainPtLpAlarm_Object = MibTableColumn
vrcMainPtLpAlarm = _VrcMainPtLpAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 23),
    _VrcMainPtLpAlarm_Type()
)
vrcMainPtLpAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtLpAlarm.setStatus("current")
_VrcMainPtHpAlarm_Type = TruthValue
_VrcMainPtHpAlarm_Object = MibTableColumn
vrcMainPtHpAlarm = _VrcMainPtHpAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 24),
    _VrcMainPtHpAlarm_Type()
)
vrcMainPtHpAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtHpAlarm.setStatus("current")
_VrcMainPtLpFreqAlarm_Type = TruthValue
_VrcMainPtLpFreqAlarm_Object = MibTableColumn
vrcMainPtLpFreqAlarm = _VrcMainPtLpFreqAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 25),
    _VrcMainPtLpFreqAlarm_Type()
)
vrcMainPtLpFreqAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtLpFreqAlarm.setStatus("current")
_VrcMainPtHpFreqAlarm_Type = TruthValue
_VrcMainPtHpFreqAlarm_Object = MibTableColumn
vrcMainPtHpFreqAlarm = _VrcMainPtHpFreqAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 26),
    _VrcMainPtHpFreqAlarm_Type()
)
vrcMainPtHpFreqAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtHpFreqAlarm.setStatus("current")
_VrcMainPtLpSensorFailAlarm_Type = TruthValue
_VrcMainPtLpSensorFailAlarm_Object = MibTableColumn
vrcMainPtLpSensorFailAlarm = _VrcMainPtLpSensorFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 27),
    _VrcMainPtLpSensorFailAlarm_Type()
)
vrcMainPtLpSensorFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtLpSensorFailAlarm.setStatus("current")
_VrcMainPtHpSensorFailAlarm_Type = TruthValue
_VrcMainPtHpSensorFailAlarm_Object = MibTableColumn
vrcMainPtHpSensorFailAlarm = _VrcMainPtHpSensorFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 28),
    _VrcMainPtHpSensorFailAlarm_Type()
)
vrcMainPtHpSensorFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtHpSensorFailAlarm.setStatus("current")
_VrcMainPtEevCommFailAlarm_Type = TruthValue
_VrcMainPtEevCommFailAlarm_Object = MibTableColumn
vrcMainPtEevCommFailAlarm = _VrcMainPtEevCommFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 2, 1, 29),
    _VrcMainPtEevCommFailAlarm_Type()
)
vrcMainPtEevCommFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcMainPtEevCommFailAlarm.setStatus("current")
_VrcMainCfgTable_Object = MibTable
vrcMainCfgTable = _VrcMainCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3)
)
if mibBuilder.loadTexts:
    vrcMainCfgTable.setStatus("current")
_VrcMainCfgEntry_Object = MibTableRow
vrcMainCfgEntry = _VrcMainCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1)
)
vrcMainCfgEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "vrcMainCfgIndex"),
)
if mibBuilder.loadTexts:
    vrcMainCfgEntry.setStatus("current")


class _VrcMainCfgIndex_Type(Integer32):
    """Custom type vrcMainCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrcMainCfgIndex_Type.__name__ = "Integer32"
_VrcMainCfgIndex_Object = MibTableColumn
vrcMainCfgIndex = _VrcMainCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 1),
    _VrcMainCfgIndex_Type()
)
vrcMainCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrcMainCfgIndex.setStatus("current")


class _VrcMainCfgModelSelect_Type(Integer32):
    """Custom type vrcMainCfgModelSelect based on Integer32"""
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
        *(("tmLoc", 1),
          ("r035Ap", 2),
          ("r035Ak", 3),
          ("scLoc", 4),
          ("zeroULoc", 5),
          ("r035Ep", 6),
          ("r035Ek", 7))
    )


_VrcMainCfgModelSelect_Type.__name__ = "Integer32"
_VrcMainCfgModelSelect_Object = MibTableColumn
vrcMainCfgModelSelect = _VrcMainCfgModelSelect_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 2),
    _VrcMainCfgModelSelect_Type()
)
vrcMainCfgModelSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgModelSelect.setStatus("current")


class _VrcMainCfgSystemTimeYear_Type(Integer32):
    """Custom type vrcMainCfgSystemTimeYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 2099),
    )


_VrcMainCfgSystemTimeYear_Type.__name__ = "Integer32"
_VrcMainCfgSystemTimeYear_Object = MibTableColumn
vrcMainCfgSystemTimeYear = _VrcMainCfgSystemTimeYear_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 3),
    _VrcMainCfgSystemTimeYear_Type()
)
vrcMainCfgSystemTimeYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgSystemTimeYear.setStatus("current")


class _VrcMainCfgSystemTimeMonth_Type(Integer32):
    """Custom type vrcMainCfgSystemTimeMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_VrcMainCfgSystemTimeMonth_Type.__name__ = "Integer32"
_VrcMainCfgSystemTimeMonth_Object = MibTableColumn
vrcMainCfgSystemTimeMonth = _VrcMainCfgSystemTimeMonth_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 4),
    _VrcMainCfgSystemTimeMonth_Type()
)
vrcMainCfgSystemTimeMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgSystemTimeMonth.setStatus("current")


class _VrcMainCfgSystemTimeDay_Type(Integer32):
    """Custom type vrcMainCfgSystemTimeDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_VrcMainCfgSystemTimeDay_Type.__name__ = "Integer32"
_VrcMainCfgSystemTimeDay_Object = MibTableColumn
vrcMainCfgSystemTimeDay = _VrcMainCfgSystemTimeDay_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 5),
    _VrcMainCfgSystemTimeDay_Type()
)
vrcMainCfgSystemTimeDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgSystemTimeDay.setStatus("current")


class _VrcMainCfgSystemTimeHour_Type(Integer32):
    """Custom type vrcMainCfgSystemTimeHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_VrcMainCfgSystemTimeHour_Type.__name__ = "Integer32"
_VrcMainCfgSystemTimeHour_Object = MibTableColumn
vrcMainCfgSystemTimeHour = _VrcMainCfgSystemTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 6),
    _VrcMainCfgSystemTimeHour_Type()
)
vrcMainCfgSystemTimeHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgSystemTimeHour.setStatus("current")


class _VrcMainCfgSystemTimeMin_Type(Integer32):
    """Custom type vrcMainCfgSystemTimeMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_VrcMainCfgSystemTimeMin_Type.__name__ = "Integer32"
_VrcMainCfgSystemTimeMin_Object = MibTableColumn
vrcMainCfgSystemTimeMin = _VrcMainCfgSystemTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 7),
    _VrcMainCfgSystemTimeMin_Type()
)
vrcMainCfgSystemTimeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgSystemTimeMin.setStatus("current")


class _VrcMainCfgSystemTimeSec_Type(Integer32):
    """Custom type vrcMainCfgSystemTimeSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_VrcMainCfgSystemTimeSec_Type.__name__ = "Integer32"
_VrcMainCfgSystemTimeSec_Object = MibTableColumn
vrcMainCfgSystemTimeSec = _VrcMainCfgSystemTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 8),
    _VrcMainCfgSystemTimeSec_Type()
)
vrcMainCfgSystemTimeSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgSystemTimeSec.setStatus("current")
_VrcMainCfgEevShtSettingMin_Type = Integer32
_VrcMainCfgEevShtSettingMin_Object = MibTableColumn
vrcMainCfgEevShtSettingMin = _VrcMainCfgEevShtSettingMin_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 9),
    _VrcMainCfgEevShtSettingMin_Type()
)
vrcMainCfgEevShtSettingMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgEevShtSettingMin.setStatus("current")
if mibBuilder.loadTexts:
    vrcMainCfgEevShtSettingMin.setUnits("decidegrees")
_VrcMainCfgEevShtSettingMax_Type = Integer32
_VrcMainCfgEevShtSettingMax_Object = MibTableColumn
vrcMainCfgEevShtSettingMax = _VrcMainCfgEevShtSettingMax_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 10),
    _VrcMainCfgEevShtSettingMax_Type()
)
vrcMainCfgEevShtSettingMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgEevShtSettingMax.setStatus("current")
if mibBuilder.loadTexts:
    vrcMainCfgEevShtSettingMax.setUnits("decidegrees")
_VrcMainCfgEevValveCloseSht_Type = Integer32
_VrcMainCfgEevValveCloseSht_Object = MibTableColumn
vrcMainCfgEevValveCloseSht = _VrcMainCfgEevValveCloseSht_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 11),
    _VrcMainCfgEevValveCloseSht_Type()
)
vrcMainCfgEevValveCloseSht.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgEevValveCloseSht.setStatus("current")
if mibBuilder.loadTexts:
    vrcMainCfgEevValveCloseSht.setUnits("decidegrees")


class _VrcMainCfgEevMopPressSetting_Type(Integer32):
    """Custom type vrcMainCfgEevMopPressSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_VrcMainCfgEevMopPressSetting_Type.__name__ = "Integer32"
_VrcMainCfgEevMopPressSetting_Object = MibTableColumn
vrcMainCfgEevMopPressSetting = _VrcMainCfgEevMopPressSetting_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 12),
    _VrcMainCfgEevMopPressSetting_Type()
)
vrcMainCfgEevMopPressSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgEevMopPressSetting.setStatus("current")
if mibBuilder.loadTexts:
    vrcMainCfgEevMopPressSetting.setUnits("decibars")


class _VrcMainCfgLpdt_Type(Integer32):
    """Custom type vrcMainCfgLpdt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 600),
    )


_VrcMainCfgLpdt_Type.__name__ = "Integer32"
_VrcMainCfgLpdt_Object = MibTableColumn
vrcMainCfgLpdt = _VrcMainCfgLpdt_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 13),
    _VrcMainCfgLpdt_Type()
)
vrcMainCfgLpdt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgLpdt.setStatus("current")
if mibBuilder.loadTexts:
    vrcMainCfgLpdt.setUnits("seconds")
_VrcMainCfgDeadBand_Type = Integer32
_VrcMainCfgDeadBand_Object = MibTableColumn
vrcMainCfgDeadBand = _VrcMainCfgDeadBand_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 14),
    _VrcMainCfgDeadBand_Type()
)
vrcMainCfgDeadBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgDeadBand.setStatus("current")
if mibBuilder.loadTexts:
    vrcMainCfgDeadBand.setUnits("decidegrees")
_VrcMainCfgOnOffSwitch_Type = TruthValue
_VrcMainCfgOnOffSwitch_Object = MibTableColumn
vrcMainCfgOnOffSwitch = _VrcMainCfgOnOffSwitch_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 15),
    _VrcMainCfgOnOffSwitch_Type()
)
vrcMainCfgOnOffSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgOnOffSwitch.setStatus("current")
_VrcMainCfgVacuumState_Type = TruthValue
_VrcMainCfgVacuumState_Object = MibTableColumn
vrcMainCfgVacuumState = _VrcMainCfgVacuumState_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 16),
    _VrcMainCfgVacuumState_Type()
)
vrcMainCfgVacuumState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgVacuumState.setStatus("current")


class _VrcMainCfgControlMode_Type(Integer32):
    """Custom type vrcMainCfgControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supply", 1),
          ("return", 2))
    )


_VrcMainCfgControlMode_Type.__name__ = "Integer32"
_VrcMainCfgControlMode_Object = MibTableColumn
vrcMainCfgControlMode = _VrcMainCfgControlMode_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 17),
    _VrcMainCfgControlMode_Type()
)
vrcMainCfgControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgControlMode.setStatus("current")
_VrcMainCfgManualRunEnable_Type = TruthValue
_VrcMainCfgManualRunEnable_Object = MibTableColumn
vrcMainCfgManualRunEnable = _VrcMainCfgManualRunEnable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 18),
    _VrcMainCfgManualRunEnable_Type()
)
vrcMainCfgManualRunEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgManualRunEnable.setStatus("current")
_VrcMainCfgRemShutdownInput_Type = TruthValue
_VrcMainCfgRemShutdownInput_Object = MibTableColumn
vrcMainCfgRemShutdownInput = _VrcMainCfgRemShutdownInput_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 19),
    _VrcMainCfgRemShutdownInput_Type()
)
vrcMainCfgRemShutdownInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgRemShutdownInput.setStatus("current")
_VrcMainCfgMonitorShutDownFlag_Type = TruthValue
_VrcMainCfgMonitorShutDownFlag_Object = MibTableColumn
vrcMainCfgMonitorShutDownFlag = _VrcMainCfgMonitorShutDownFlag_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 20),
    _VrcMainCfgMonitorShutDownFlag_Type()
)
vrcMainCfgMonitorShutDownFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgMonitorShutDownFlag.setStatus("current")


class _VrcMainCfgFirstOnPassword_Type(Integer32):
    """Custom type vrcMainCfgFirstOnPassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_VrcMainCfgFirstOnPassword_Type.__name__ = "Integer32"
_VrcMainCfgFirstOnPassword_Object = MibTableColumn
vrcMainCfgFirstOnPassword = _VrcMainCfgFirstOnPassword_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 21),
    _VrcMainCfgFirstOnPassword_Type()
)
vrcMainCfgFirstOnPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgFirstOnPassword.setStatus("current")
_VrcMainCfgFilterMaintSetting_Type = TruthValue
_VrcMainCfgFilterMaintSetting_Object = MibTableColumn
vrcMainCfgFilterMaintSetting = _VrcMainCfgFilterMaintSetting_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 22),
    _VrcMainCfgFilterMaintSetting_Type()
)
vrcMainCfgFilterMaintSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgFilterMaintSetting.setStatus("current")


class _VrcMainCfgFilterMaintRemindTime_Type(Integer32):
    """Custom type vrcMainCfgFilterMaintRemindTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 360),
    )


_VrcMainCfgFilterMaintRemindTime_Type.__name__ = "Integer32"
_VrcMainCfgFilterMaintRemindTime_Object = MibTableColumn
vrcMainCfgFilterMaintRemindTime = _VrcMainCfgFilterMaintRemindTime_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 23),
    _VrcMainCfgFilterMaintRemindTime_Type()
)
vrcMainCfgFilterMaintRemindTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgFilterMaintRemindTime.setStatus("current")
if mibBuilder.loadTexts:
    vrcMainCfgFilterMaintRemindTime.setUnits("days")


class _VrcMainCfgFilterMaintRemindCtrl_Type(Integer32):
    """Custom type vrcMainCfgFilterMaintRemindCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("close", 1),
          ("suspend", 2),
          ("open", 3))
    )


_VrcMainCfgFilterMaintRemindCtrl_Type.__name__ = "Integer32"
_VrcMainCfgFilterMaintRemindCtrl_Object = MibTableColumn
vrcMainCfgFilterMaintRemindCtrl = _VrcMainCfgFilterMaintRemindCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 24),
    _VrcMainCfgFilterMaintRemindCtrl_Type()
)
vrcMainCfgFilterMaintRemindCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgFilterMaintRemindCtrl.setStatus("current")
_VrcMainCfgCommonAlarmOutputDir_Type = TruthValue
_VrcMainCfgCommonAlarmOutputDir_Object = MibTableColumn
vrcMainCfgCommonAlarmOutputDir = _VrcMainCfgCommonAlarmOutputDir_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 25),
    _VrcMainCfgCommonAlarmOutputDir_Type()
)
vrcMainCfgCommonAlarmOutputDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgCommonAlarmOutputDir.setStatus("current")


class _VrcMainCfgHpAbnAlarmSetting_Type(Integer32):
    """Custom type vrcMainCfgHpAbnAlarmSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 360),
    )


_VrcMainCfgHpAbnAlarmSetting_Type.__name__ = "Integer32"
_VrcMainCfgHpAbnAlarmSetting_Object = MibTableColumn
vrcMainCfgHpAbnAlarmSetting = _VrcMainCfgHpAbnAlarmSetting_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 26),
    _VrcMainCfgHpAbnAlarmSetting_Type()
)
vrcMainCfgHpAbnAlarmSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgHpAbnAlarmSetting.setStatus("current")
if mibBuilder.loadTexts:
    vrcMainCfgHpAbnAlarmSetting.setUnits("decibars")


class _VrcMainCfgLpAlarmCtrl_Type(Integer32):
    """Custom type vrcMainCfgLpAlarmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("suspend", 2),
          ("open", 3))
    )


_VrcMainCfgLpAlarmCtrl_Type.__name__ = "Integer32"
_VrcMainCfgLpAlarmCtrl_Object = MibTableColumn
vrcMainCfgLpAlarmCtrl = _VrcMainCfgLpAlarmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 27),
    _VrcMainCfgLpAlarmCtrl_Type()
)
vrcMainCfgLpAlarmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgLpAlarmCtrl.setStatus("current")


class _VrcMainCfgHpAlarmCtrl_Type(Integer32):
    """Custom type vrcMainCfgHpAlarmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("suspend", 2),
          ("open", 3))
    )


_VrcMainCfgHpAlarmCtrl_Type.__name__ = "Integer32"
_VrcMainCfgHpAlarmCtrl_Object = MibTableColumn
vrcMainCfgHpAlarmCtrl = _VrcMainCfgHpAlarmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 28),
    _VrcMainCfgHpAlarmCtrl_Type()
)
vrcMainCfgHpAlarmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgHpAlarmCtrl.setStatus("current")


class _VrcMainCfgLpFreqAlarmCtrl_Type(Integer32):
    """Custom type vrcMainCfgLpFreqAlarmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("suspend", 2),
          ("open", 3))
    )


_VrcMainCfgLpFreqAlarmCtrl_Type.__name__ = "Integer32"
_VrcMainCfgLpFreqAlarmCtrl_Object = MibTableColumn
vrcMainCfgLpFreqAlarmCtrl = _VrcMainCfgLpFreqAlarmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 29),
    _VrcMainCfgLpFreqAlarmCtrl_Type()
)
vrcMainCfgLpFreqAlarmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgLpFreqAlarmCtrl.setStatus("current")


class _VrcMainCfgHpFreqAlarmCtrl_Type(Integer32):
    """Custom type vrcMainCfgHpFreqAlarmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("suspend", 2),
          ("open", 3))
    )


_VrcMainCfgHpFreqAlarmCtrl_Type.__name__ = "Integer32"
_VrcMainCfgHpFreqAlarmCtrl_Object = MibTableColumn
vrcMainCfgHpFreqAlarmCtrl = _VrcMainCfgHpFreqAlarmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 30),
    _VrcMainCfgHpFreqAlarmCtrl_Type()
)
vrcMainCfgHpFreqAlarmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgHpFreqAlarmCtrl.setStatus("current")


class _VrcMainCfgLpSensorFailAlarmCtrl_Type(Integer32):
    """Custom type vrcMainCfgLpSensorFailAlarmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("suspend", 2),
          ("open", 3))
    )


_VrcMainCfgLpSensorFailAlarmCtrl_Type.__name__ = "Integer32"
_VrcMainCfgLpSensorFailAlarmCtrl_Object = MibTableColumn
vrcMainCfgLpSensorFailAlarmCtrl = _VrcMainCfgLpSensorFailAlarmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 31),
    _VrcMainCfgLpSensorFailAlarmCtrl_Type()
)
vrcMainCfgLpSensorFailAlarmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgLpSensorFailAlarmCtrl.setStatus("current")


class _VrcMainCfgHpSensorFailAlarmCtrl_Type(Integer32):
    """Custom type vrcMainCfgHpSensorFailAlarmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("suspend", 2),
          ("open", 3))
    )


_VrcMainCfgHpSensorFailAlarmCtrl_Type.__name__ = "Integer32"
_VrcMainCfgHpSensorFailAlarmCtrl_Object = MibTableColumn
vrcMainCfgHpSensorFailAlarmCtrl = _VrcMainCfgHpSensorFailAlarmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 32),
    _VrcMainCfgHpSensorFailAlarmCtrl_Type()
)
vrcMainCfgHpSensorFailAlarmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgHpSensorFailAlarmCtrl.setStatus("current")


class _VrcMainCfgHighWaterAlarmCtrl_Type(Integer32):
    """Custom type vrcMainCfgHighWaterAlarmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("close", 1),
          ("suspend", 2),
          ("open", 3))
    )


_VrcMainCfgHighWaterAlarmCtrl_Type.__name__ = "Integer32"
_VrcMainCfgHighWaterAlarmCtrl_Object = MibTableColumn
vrcMainCfgHighWaterAlarmCtrl = _VrcMainCfgHighWaterAlarmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 33),
    _VrcMainCfgHighWaterAlarmCtrl_Type()
)
vrcMainCfgHighWaterAlarmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgHighWaterAlarmCtrl.setStatus("current")


class _VrcMainCfgRemShutdownAlarmCtrl_Type(Integer32):
    """Custom type vrcMainCfgRemShutdownAlarmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("suspend", 2),
          ("open", 3))
    )


_VrcMainCfgRemShutdownAlarmCtrl_Type.__name__ = "Integer32"
_VrcMainCfgRemShutdownAlarmCtrl_Object = MibTableColumn
vrcMainCfgRemShutdownAlarmCtrl = _VrcMainCfgRemShutdownAlarmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 34),
    _VrcMainCfgRemShutdownAlarmCtrl_Type()
)
vrcMainCfgRemShutdownAlarmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgRemShutdownAlarmCtrl.setStatus("current")


class _VrcMainCfgEevCommFailAlarmCtrl_Type(Integer32):
    """Custom type vrcMainCfgEevCommFailAlarmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("suspend", 2),
          ("open", 3))
    )


_VrcMainCfgEevCommFailAlarmCtrl_Type.__name__ = "Integer32"
_VrcMainCfgEevCommFailAlarmCtrl_Object = MibTableColumn
vrcMainCfgEevCommFailAlarmCtrl = _VrcMainCfgEevCommFailAlarmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 3, 1, 35),
    _VrcMainCfgEevCommFailAlarmCtrl_Type()
)
vrcMainCfgEevCommFailAlarmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcMainCfgEevCommFailAlarmCtrl.setStatus("current")
_VrcOutFanPtTable_Object = MibTable
vrcOutFanPtTable = _VrcOutFanPtTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 4)
)
if mibBuilder.loadTexts:
    vrcOutFanPtTable.setStatus("current")
_VrcOutFanPtEntry_Object = MibTableRow
vrcOutFanPtEntry = _VrcOutFanPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 4, 1)
)
vrcOutFanPtEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "vrcOutFanPtIndex"),
)
if mibBuilder.loadTexts:
    vrcOutFanPtEntry.setStatus("current")


class _VrcOutFanPtIndex_Type(Integer32):
    """Custom type vrcOutFanPtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrcOutFanPtIndex_Type.__name__ = "Integer32"
_VrcOutFanPtIndex_Object = MibTableColumn
vrcOutFanPtIndex = _VrcOutFanPtIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 4, 1, 1),
    _VrcOutFanPtIndex_Type()
)
vrcOutFanPtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrcOutFanPtIndex.setStatus("current")


class _VrcOutFanPtName_Type(SnmpAdminString):
    """Custom type vrcOutFanPtName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_VrcOutFanPtName_Type.__name__ = "SnmpAdminString"
_VrcOutFanPtName_Object = MibTableColumn
vrcOutFanPtName = _VrcOutFanPtName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 4, 1, 2),
    _VrcOutFanPtName_Type()
)
vrcOutFanPtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcOutFanPtName.setStatus("current")


class _VrcOutFanPtSpeed_Type(Integer32):
    """Custom type vrcOutFanPtSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrcOutFanPtSpeed_Type.__name__ = "Integer32"
_VrcOutFanPtSpeed_Object = MibTableColumn
vrcOutFanPtSpeed = _VrcOutFanPtSpeed_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 4, 1, 3),
    _VrcOutFanPtSpeed_Type()
)
vrcOutFanPtSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcOutFanPtSpeed.setStatus("current")
if mibBuilder.loadTexts:
    vrcOutFanPtSpeed.setUnits("%")
_VrcOutFanCfgTable_Object = MibTable
vrcOutFanCfgTable = _VrcOutFanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 5)
)
if mibBuilder.loadTexts:
    vrcOutFanCfgTable.setStatus("current")
_VrcOutFanCfgEntry_Object = MibTableRow
vrcOutFanCfgEntry = _VrcOutFanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 5, 1)
)
vrcOutFanCfgEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "vrcOutFanCfgIndex"),
)
if mibBuilder.loadTexts:
    vrcOutFanCfgEntry.setStatus("current")


class _VrcOutFanCfgIndex_Type(Integer32):
    """Custom type vrcOutFanCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrcOutFanCfgIndex_Type.__name__ = "Integer32"
_VrcOutFanCfgIndex_Object = MibTableColumn
vrcOutFanCfgIndex = _VrcOutFanCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 5, 1, 1),
    _VrcOutFanCfgIndex_Type()
)
vrcOutFanCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrcOutFanCfgIndex.setStatus("current")


class _VrcOutFanCfgStartPress_Type(Integer32):
    """Custom type vrcOutFanCfgStartPress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(190, 250),
    )


_VrcOutFanCfgStartPress_Type.__name__ = "Integer32"
_VrcOutFanCfgStartPress_Object = MibTableColumn
vrcOutFanCfgStartPress = _VrcOutFanCfgStartPress_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 5, 1, 2),
    _VrcOutFanCfgStartPress_Type()
)
vrcOutFanCfgStartPress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcOutFanCfgStartPress.setStatus("current")
if mibBuilder.loadTexts:
    vrcOutFanCfgStartPress.setUnits("decibars")


class _VrcOutFanCfgPressSetting_Type(Integer32):
    """Custom type vrcOutFanCfgPressSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 80),
    )


_VrcOutFanCfgPressSetting_Type.__name__ = "Integer32"
_VrcOutFanCfgPressSetting_Object = MibTableColumn
vrcOutFanCfgPressSetting = _VrcOutFanCfgPressSetting_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 5, 1, 3),
    _VrcOutFanCfgPressSetting_Type()
)
vrcOutFanCfgPressSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcOutFanCfgPressSetting.setStatus("current")
if mibBuilder.loadTexts:
    vrcOutFanCfgPressSetting.setUnits("decibars")


class _VrcOutFanCfgMinPowerVoltage_Type(Integer32):
    """Custom type vrcOutFanCfgMinPowerVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 50),
    )


_VrcOutFanCfgMinPowerVoltage_Type.__name__ = "Integer32"
_VrcOutFanCfgMinPowerVoltage_Object = MibTableColumn
vrcOutFanCfgMinPowerVoltage = _VrcOutFanCfgMinPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 5, 1, 4),
    _VrcOutFanCfgMinPowerVoltage_Type()
)
vrcOutFanCfgMinPowerVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcOutFanCfgMinPowerVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vrcOutFanCfgMinPowerVoltage.setUnits("%")


class _VrcOutFanCfgMaxPowerVoltage_Type(Integer32):
    """Custom type vrcOutFanCfgMaxPowerVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 100),
    )


_VrcOutFanCfgMaxPowerVoltage_Type.__name__ = "Integer32"
_VrcOutFanCfgMaxPowerVoltage_Object = MibTableColumn
vrcOutFanCfgMaxPowerVoltage = _VrcOutFanCfgMaxPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 5, 1, 5),
    _VrcOutFanCfgMaxPowerVoltage_Type()
)
vrcOutFanCfgMaxPowerVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcOutFanCfgMaxPowerVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vrcOutFanCfgMaxPowerVoltage.setUnits("%")


class _VrcOutFanCfgSpeed_Type(Integer32):
    """Custom type vrcOutFanCfgSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrcOutFanCfgSpeed_Type.__name__ = "Integer32"
_VrcOutFanCfgSpeed_Object = MibTableColumn
vrcOutFanCfgSpeed = _VrcOutFanCfgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 5, 1, 6),
    _VrcOutFanCfgSpeed_Type()
)
vrcOutFanCfgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcOutFanCfgSpeed.setStatus("current")
if mibBuilder.loadTexts:
    vrcOutFanCfgSpeed.setUnits("%")
_VrcInFanPtTable_Object = MibTable
vrcInFanPtTable = _VrcInFanPtTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 6)
)
if mibBuilder.loadTexts:
    vrcInFanPtTable.setStatus("current")
_VrcInFanPtEntry_Object = MibTableRow
vrcInFanPtEntry = _VrcInFanPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 6, 1)
)
vrcInFanPtEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "vrcInFanPtIndex"),
)
if mibBuilder.loadTexts:
    vrcInFanPtEntry.setStatus("current")


class _VrcInFanPtIndex_Type(Integer32):
    """Custom type vrcInFanPtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrcInFanPtIndex_Type.__name__ = "Integer32"
_VrcInFanPtIndex_Object = MibTableColumn
vrcInFanPtIndex = _VrcInFanPtIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 6, 1, 1),
    _VrcInFanPtIndex_Type()
)
vrcInFanPtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrcInFanPtIndex.setStatus("current")


class _VrcInFanPtName_Type(SnmpAdminString):
    """Custom type vrcInFanPtName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_VrcInFanPtName_Type.__name__ = "SnmpAdminString"
_VrcInFanPtName_Object = MibTableColumn
vrcInFanPtName = _VrcInFanPtName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 6, 1, 2),
    _VrcInFanPtName_Type()
)
vrcInFanPtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcInFanPtName.setStatus("current")


class _VrcInFanPtRunTimeHours_Type(Integer32):
    """Custom type vrcInFanPtRunTimeHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_VrcInFanPtRunTimeHours_Type.__name__ = "Integer32"
_VrcInFanPtRunTimeHours_Object = MibTableColumn
vrcInFanPtRunTimeHours = _VrcInFanPtRunTimeHours_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 6, 1, 3),
    _VrcInFanPtRunTimeHours_Type()
)
vrcInFanPtRunTimeHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcInFanPtRunTimeHours.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanPtRunTimeHours.setUnits("hours")


class _VrcInFanPtStartStopCount_Type(Integer32):
    """Custom type vrcInFanPtStartStopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_VrcInFanPtStartStopCount_Type.__name__ = "Integer32"
_VrcInFanPtStartStopCount_Object = MibTableColumn
vrcInFanPtStartStopCount = _VrcInFanPtStartStopCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 6, 1, 4),
    _VrcInFanPtStartStopCount_Type()
)
vrcInFanPtStartStopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcInFanPtStartStopCount.setStatus("current")
_VrcInFanCfgTable_Object = MibTable
vrcInFanCfgTable = _VrcInFanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7)
)
if mibBuilder.loadTexts:
    vrcInFanCfgTable.setStatus("current")
_VrcInFanCfgEntry_Object = MibTableRow
vrcInFanCfgEntry = _VrcInFanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1)
)
vrcInFanCfgEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "vrcInFanCfgIndex"),
)
if mibBuilder.loadTexts:
    vrcInFanCfgEntry.setStatus("current")


class _VrcInFanCfgIndex_Type(Integer32):
    """Custom type vrcInFanCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrcInFanCfgIndex_Type.__name__ = "Integer32"
_VrcInFanCfgIndex_Object = MibTableColumn
vrcInFanCfgIndex = _VrcInFanCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 1),
    _VrcInFanCfgIndex_Type()
)
vrcInFanCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrcInFanCfgIndex.setStatus("current")
_VrcInFanCfgOutputStatus_Type = TruthValue
_VrcInFanCfgOutputStatus_Object = MibTableColumn
vrcInFanCfgOutputStatus = _VrcInFanCfgOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 2),
    _VrcInFanCfgOutputStatus_Type()
)
vrcInFanCfgOutputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgOutputStatus.setStatus("current")


class _VrcInFanCfgLowSpeedStep_Type(Integer32):
    """Custom type vrcInFanCfgLowSpeedStep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_VrcInFanCfgLowSpeedStep_Type.__name__ = "Integer32"
_VrcInFanCfgLowSpeedStep_Object = MibTableColumn
vrcInFanCfgLowSpeedStep = _VrcInFanCfgLowSpeedStep_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 3),
    _VrcInFanCfgLowSpeedStep_Type()
)
vrcInFanCfgLowSpeedStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgLowSpeedStep.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgLowSpeedStep.setUnits("0.1%/s")


class _VrcInFanCfgHighSpeedStep_Type(Integer32):
    """Custom type vrcInFanCfgHighSpeedStep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_VrcInFanCfgHighSpeedStep_Type.__name__ = "Integer32"
_VrcInFanCfgHighSpeedStep_Object = MibTableColumn
vrcInFanCfgHighSpeedStep = _VrcInFanCfgHighSpeedStep_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 4),
    _VrcInFanCfgHighSpeedStep_Type()
)
vrcInFanCfgHighSpeedStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgHighSpeedStep.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgHighSpeedStep.setUnits("0.1%/s")


class _VrcInFanCfgMinSpeed_Type(Integer32):
    """Custom type vrcInFanCfgMinSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 80),
    )


_VrcInFanCfgMinSpeed_Type.__name__ = "Integer32"
_VrcInFanCfgMinSpeed_Object = MibTableColumn
vrcInFanCfgMinSpeed = _VrcInFanCfgMinSpeed_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 5),
    _VrcInFanCfgMinSpeed_Type()
)
vrcInFanCfgMinSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgMinSpeed.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgMinSpeed.setUnits("%")


class _VrcInFanCfgStandardSpeed_Type(Integer32):
    """Custom type vrcInFanCfgStandardSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 100),
    )


_VrcInFanCfgStandardSpeed_Type.__name__ = "Integer32"
_VrcInFanCfgStandardSpeed_Object = MibTableColumn
vrcInFanCfgStandardSpeed = _VrcInFanCfgStandardSpeed_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 6),
    _VrcInFanCfgStandardSpeed_Type()
)
vrcInFanCfgStandardSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgStandardSpeed.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgStandardSpeed.setUnits("%")


class _VrcInFanCfgMinCfc_Type(Integer32):
    """Custom type vrcInFanCfgMinCfc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_VrcInFanCfgMinCfc_Type.__name__ = "Integer32"
_VrcInFanCfgMinCfc_Object = MibTableColumn
vrcInFanCfgMinCfc = _VrcInFanCfgMinCfc_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 7),
    _VrcInFanCfgMinCfc_Type()
)
vrcInFanCfgMinCfc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgMinCfc.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgMinCfc.setUnits("%")


class _VrcInFanCfgStandardCfc_Type(Integer32):
    """Custom type vrcInFanCfgStandardCfc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(85, 100),
    )


_VrcInFanCfgStandardCfc_Type.__name__ = "Integer32"
_VrcInFanCfgStandardCfc_Object = MibTableColumn
vrcInFanCfgStandardCfc = _VrcInFanCfgStandardCfc_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 8),
    _VrcInFanCfgStandardCfc_Type()
)
vrcInFanCfgStandardCfc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgStandardCfc.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgStandardCfc.setUnits("%")


class _VrcInFanCfgStartDelay_Type(Integer32):
    """Custom type vrcInFanCfgStartDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_VrcInFanCfgStartDelay_Type.__name__ = "Integer32"
_VrcInFanCfgStartDelay_Object = MibTableColumn
vrcInFanCfgStartDelay = _VrcInFanCfgStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 9),
    _VrcInFanCfgStartDelay_Type()
)
vrcInFanCfgStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgStartDelay.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgStartDelay.setUnits("seconds")


class _VrcInFanCfgStopDelay_Type(Integer32):
    """Custom type vrcInFanCfgStopDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_VrcInFanCfgStopDelay_Type.__name__ = "Integer32"
_VrcInFanCfgStopDelay_Object = MibTableColumn
vrcInFanCfgStopDelay = _VrcInFanCfgStopDelay_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 10),
    _VrcInFanCfgStopDelay_Type()
)
vrcInFanCfgStopDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgStopDelay.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgStopDelay.setUnits("seconds")


class _VrcInFanCfgReduceSpeedDelay_Type(Integer32):
    """Custom type vrcInFanCfgReduceSpeedDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_VrcInFanCfgReduceSpeedDelay_Type.__name__ = "Integer32"
_VrcInFanCfgReduceSpeedDelay_Object = MibTableColumn
vrcInFanCfgReduceSpeedDelay = _VrcInFanCfgReduceSpeedDelay_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 11),
    _VrcInFanCfgReduceSpeedDelay_Type()
)
vrcInFanCfgReduceSpeedDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgReduceSpeedDelay.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgReduceSpeedDelay.setUnits("seconds")


class _VrcInFanCfgJumpBand1_Type(Integer32):
    """Custom type vrcInFanCfgJumpBand1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrcInFanCfgJumpBand1_Type.__name__ = "Integer32"
_VrcInFanCfgJumpBand1_Object = MibTableColumn
vrcInFanCfgJumpBand1 = _VrcInFanCfgJumpBand1_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 12),
    _VrcInFanCfgJumpBand1_Type()
)
vrcInFanCfgJumpBand1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgJumpBand1.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgJumpBand1.setUnits("0.1%")


class _VrcInFanCfgJumpBand2_Type(Integer32):
    """Custom type vrcInFanCfgJumpBand2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrcInFanCfgJumpBand2_Type.__name__ = "Integer32"
_VrcInFanCfgJumpBand2_Object = MibTableColumn
vrcInFanCfgJumpBand2 = _VrcInFanCfgJumpBand2_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 13),
    _VrcInFanCfgJumpBand2_Type()
)
vrcInFanCfgJumpBand2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgJumpBand2.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgJumpBand2.setUnits("0.1%")


class _VrcInFanCfgJumpBand3_Type(Integer32):
    """Custom type vrcInFanCfgJumpBand3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrcInFanCfgJumpBand3_Type.__name__ = "Integer32"
_VrcInFanCfgJumpBand3_Object = MibTableColumn
vrcInFanCfgJumpBand3 = _VrcInFanCfgJumpBand3_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 14),
    _VrcInFanCfgJumpBand3_Type()
)
vrcInFanCfgJumpBand3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgJumpBand3.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgJumpBand3.setUnits("0.1%")


class _VrcInFanCfgJumpBand4_Type(Integer32):
    """Custom type vrcInFanCfgJumpBand4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrcInFanCfgJumpBand4_Type.__name__ = "Integer32"
_VrcInFanCfgJumpBand4_Object = MibTableColumn
vrcInFanCfgJumpBand4 = _VrcInFanCfgJumpBand4_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 15),
    _VrcInFanCfgJumpBand4_Type()
)
vrcInFanCfgJumpBand4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgJumpBand4.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgJumpBand4.setUnits("0.1%")


class _VrcInFanCfgJumpBand5_Type(Integer32):
    """Custom type vrcInFanCfgJumpBand5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrcInFanCfgJumpBand5_Type.__name__ = "Integer32"
_VrcInFanCfgJumpBand5_Object = MibTableColumn
vrcInFanCfgJumpBand5 = _VrcInFanCfgJumpBand5_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 16),
    _VrcInFanCfgJumpBand5_Type()
)
vrcInFanCfgJumpBand5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgJumpBand5.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgJumpBand5.setUnits("0.1%")


class _VrcInFanCfgJumpFreq1_Type(Integer32):
    """Custom type vrcInFanCfgJumpFreq1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_VrcInFanCfgJumpFreq1_Type.__name__ = "Integer32"
_VrcInFanCfgJumpFreq1_Object = MibTableColumn
vrcInFanCfgJumpFreq1 = _VrcInFanCfgJumpFreq1_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 17),
    _VrcInFanCfgJumpFreq1_Type()
)
vrcInFanCfgJumpFreq1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgJumpFreq1.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgJumpFreq1.setUnits("0.1%")


class _VrcInFanCfgJumpFreq2_Type(Integer32):
    """Custom type vrcInFanCfgJumpFreq2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_VrcInFanCfgJumpFreq2_Type.__name__ = "Integer32"
_VrcInFanCfgJumpFreq2_Object = MibTableColumn
vrcInFanCfgJumpFreq2 = _VrcInFanCfgJumpFreq2_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 18),
    _VrcInFanCfgJumpFreq2_Type()
)
vrcInFanCfgJumpFreq2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgJumpFreq2.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgJumpFreq2.setUnits("0.1%")


class _VrcInFanCfgJumpFreq3_Type(Integer32):
    """Custom type vrcInFanCfgJumpFreq3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_VrcInFanCfgJumpFreq3_Type.__name__ = "Integer32"
_VrcInFanCfgJumpFreq3_Object = MibTableColumn
vrcInFanCfgJumpFreq3 = _VrcInFanCfgJumpFreq3_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 19),
    _VrcInFanCfgJumpFreq3_Type()
)
vrcInFanCfgJumpFreq3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgJumpFreq3.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgJumpFreq3.setUnits("0.1%")


class _VrcInFanCfgJumpFreq4_Type(Integer32):
    """Custom type vrcInFanCfgJumpFreq4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_VrcInFanCfgJumpFreq4_Type.__name__ = "Integer32"
_VrcInFanCfgJumpFreq4_Object = MibTableColumn
vrcInFanCfgJumpFreq4 = _VrcInFanCfgJumpFreq4_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 20),
    _VrcInFanCfgJumpFreq4_Type()
)
vrcInFanCfgJumpFreq4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgJumpFreq4.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgJumpFreq4.setUnits("0.1%")


class _VrcInFanCfgJumpFreq5_Type(Integer32):
    """Custom type vrcInFanCfgJumpFreq5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_VrcInFanCfgJumpFreq5_Type.__name__ = "Integer32"
_VrcInFanCfgJumpFreq5_Object = MibTableColumn
vrcInFanCfgJumpFreq5 = _VrcInFanCfgJumpFreq5_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 21),
    _VrcInFanCfgJumpFreq5_Type()
)
vrcInFanCfgJumpFreq5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgJumpFreq5.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgJumpFreq5.setUnits("0.1%")


class _VrcInFanCfgTempP_Type(Integer32):
    """Custom type vrcInFanCfgTempP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 150),
    )


_VrcInFanCfgTempP_Type.__name__ = "Integer32"
_VrcInFanCfgTempP_Object = MibTableColumn
vrcInFanCfgTempP = _VrcInFanCfgTempP_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 22),
    _VrcInFanCfgTempP_Type()
)
vrcInFanCfgTempP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgTempP.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgTempP.setUnits("decidegrees")


class _VrcInFanCfgTempI_Type(Integer32):
    """Custom type vrcInFanCfgTempI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_VrcInFanCfgTempI_Type.__name__ = "Integer32"
_VrcInFanCfgTempI_Object = MibTableColumn
vrcInFanCfgTempI = _VrcInFanCfgTempI_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 23),
    _VrcInFanCfgTempI_Type()
)
vrcInFanCfgTempI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgTempI.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgTempI.setUnits("seconds")


class _VrcInFanCfgTempD_Type(Integer32):
    """Custom type vrcInFanCfgTempD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_VrcInFanCfgTempD_Type.__name__ = "Integer32"
_VrcInFanCfgTempD_Object = MibTableColumn
vrcInFanCfgTempD = _VrcInFanCfgTempD_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 7, 1, 24),
    _VrcInFanCfgTempD_Type()
)
vrcInFanCfgTempD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcInFanCfgTempD.setStatus("current")
if mibBuilder.loadTexts:
    vrcInFanCfgTempD.setUnits("seconds")
_VrcCompPtTable_Object = MibTable
vrcCompPtTable = _VrcCompPtTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8)
)
if mibBuilder.loadTexts:
    vrcCompPtTable.setStatus("current")
_VrcCompPtEntry_Object = MibTableRow
vrcCompPtEntry = _VrcCompPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1)
)
vrcCompPtEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "vrcCompPtIndex"),
)
if mibBuilder.loadTexts:
    vrcCompPtEntry.setStatus("current")


class _VrcCompPtIndex_Type(Integer32):
    """Custom type vrcCompPtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrcCompPtIndex_Type.__name__ = "Integer32"
_VrcCompPtIndex_Object = MibTableColumn
vrcCompPtIndex = _VrcCompPtIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 1),
    _VrcCompPtIndex_Type()
)
vrcCompPtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrcCompPtIndex.setStatus("current")


class _VrcCompPtName_Type(SnmpAdminString):
    """Custom type vrcCompPtName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_VrcCompPtName_Type.__name__ = "SnmpAdminString"
_VrcCompPtName_Object = MibTableColumn
vrcCompPtName = _VrcCompPtName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 2),
    _VrcCompPtName_Type()
)
vrcCompPtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtName.setStatus("current")


class _VrcCompPtCapacity_Type(Integer32):
    """Custom type vrcCompPtCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrcCompPtCapacity_Type.__name__ = "Integer32"
_VrcCompPtCapacity_Object = MibTableColumn
vrcCompPtCapacity = _VrcCompPtCapacity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 3),
    _VrcCompPtCapacity_Type()
)
vrcCompPtCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtCapacity.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompPtCapacity.setUnits("%")


class _VrcCompPtRunTimeHours_Type(Integer32):
    """Custom type vrcCompPtRunTimeHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_VrcCompPtRunTimeHours_Type.__name__ = "Integer32"
_VrcCompPtRunTimeHours_Object = MibTableColumn
vrcCompPtRunTimeHours = _VrcCompPtRunTimeHours_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 4),
    _VrcCompPtRunTimeHours_Type()
)
vrcCompPtRunTimeHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtRunTimeHours.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompPtRunTimeHours.setUnits("hours")


class _VrcCompPtStartStopCount_Type(Integer32):
    """Custom type vrcCompPtStartStopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_VrcCompPtStartStopCount_Type.__name__ = "Integer32"
_VrcCompPtStartStopCount_Object = MibTableColumn
vrcCompPtStartStopCount = _VrcCompPtStartStopCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 5),
    _VrcCompPtStartStopCount_Type()
)
vrcCompPtStartStopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtStartStopCount.setStatus("current")
_VrcCompPtDriverFaultU00_Type = TruthValue
_VrcCompPtDriverFaultU00_Object = MibTableColumn
vrcCompPtDriverFaultU00 = _VrcCompPtDriverFaultU00_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 6),
    _VrcCompPtDriverFaultU00_Type()
)
vrcCompPtDriverFaultU00.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtDriverFaultU00.setStatus("current")
_VrcCompPtDriverFaultU01_Type = TruthValue
_VrcCompPtDriverFaultU01_Object = MibTableColumn
vrcCompPtDriverFaultU01 = _VrcCompPtDriverFaultU01_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 7),
    _VrcCompPtDriverFaultU01_Type()
)
vrcCompPtDriverFaultU01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtDriverFaultU01.setStatus("current")
_VrcCompPtDriverFaultU02_Type = TruthValue
_VrcCompPtDriverFaultU02_Object = MibTableColumn
vrcCompPtDriverFaultU02 = _VrcCompPtDriverFaultU02_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 8),
    _VrcCompPtDriverFaultU02_Type()
)
vrcCompPtDriverFaultU02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtDriverFaultU02.setStatus("current")
_VrcCompPtDriverFaultU03_Type = TruthValue
_VrcCompPtDriverFaultU03_Object = MibTableColumn
vrcCompPtDriverFaultU03 = _VrcCompPtDriverFaultU03_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 9),
    _VrcCompPtDriverFaultU03_Type()
)
vrcCompPtDriverFaultU03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtDriverFaultU03.setStatus("current")
_VrcCompPtDriverFaultU04_Type = TruthValue
_VrcCompPtDriverFaultU04_Object = MibTableColumn
vrcCompPtDriverFaultU04 = _VrcCompPtDriverFaultU04_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 10),
    _VrcCompPtDriverFaultU04_Type()
)
vrcCompPtDriverFaultU04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtDriverFaultU04.setStatus("current")
_VrcCompPtDriverFaultU05_Type = TruthValue
_VrcCompPtDriverFaultU05_Object = MibTableColumn
vrcCompPtDriverFaultU05 = _VrcCompPtDriverFaultU05_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 11),
    _VrcCompPtDriverFaultU05_Type()
)
vrcCompPtDriverFaultU05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtDriverFaultU05.setStatus("current")
_VrcCompPtDriverFaultU06_Type = TruthValue
_VrcCompPtDriverFaultU06_Object = MibTableColumn
vrcCompPtDriverFaultU06 = _VrcCompPtDriverFaultU06_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 12),
    _VrcCompPtDriverFaultU06_Type()
)
vrcCompPtDriverFaultU06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtDriverFaultU06.setStatus("current")
_VrcCompPtDriverFaultU07_Type = TruthValue
_VrcCompPtDriverFaultU07_Object = MibTableColumn
vrcCompPtDriverFaultU07 = _VrcCompPtDriverFaultU07_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 13),
    _VrcCompPtDriverFaultU07_Type()
)
vrcCompPtDriverFaultU07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtDriverFaultU07.setStatus("current")
_VrcCompPtDriverFaultU08_Type = TruthValue
_VrcCompPtDriverFaultU08_Object = MibTableColumn
vrcCompPtDriverFaultU08 = _VrcCompPtDriverFaultU08_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 14),
    _VrcCompPtDriverFaultU08_Type()
)
vrcCompPtDriverFaultU08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtDriverFaultU08.setStatus("current")
_VrcCompPtDriverFaultU09_Type = TruthValue
_VrcCompPtDriverFaultU09_Object = MibTableColumn
vrcCompPtDriverFaultU09 = _VrcCompPtDriverFaultU09_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 15),
    _VrcCompPtDriverFaultU09_Type()
)
vrcCompPtDriverFaultU09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtDriverFaultU09.setStatus("current")
_VrcCompPtDriverFaultU10_Type = TruthValue
_VrcCompPtDriverFaultU10_Object = MibTableColumn
vrcCompPtDriverFaultU10 = _VrcCompPtDriverFaultU10_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 16),
    _VrcCompPtDriverFaultU10_Type()
)
vrcCompPtDriverFaultU10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtDriverFaultU10.setStatus("current")
_VrcCompPtDriverFaultU11_Type = TruthValue
_VrcCompPtDriverFaultU11_Object = MibTableColumn
vrcCompPtDriverFaultU11 = _VrcCompPtDriverFaultU11_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 17),
    _VrcCompPtDriverFaultU11_Type()
)
vrcCompPtDriverFaultU11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtDriverFaultU11.setStatus("current")
_VrcCompPtDriverFaultU12_Type = TruthValue
_VrcCompPtDriverFaultU12_Object = MibTableColumn
vrcCompPtDriverFaultU12 = _VrcCompPtDriverFaultU12_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 18),
    _VrcCompPtDriverFaultU12_Type()
)
vrcCompPtDriverFaultU12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtDriverFaultU12.setStatus("current")
_VrcCompPtDriverFaultU13_Type = TruthValue
_VrcCompPtDriverFaultU13_Object = MibTableColumn
vrcCompPtDriverFaultU13 = _VrcCompPtDriverFaultU13_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 19),
    _VrcCompPtDriverFaultU13_Type()
)
vrcCompPtDriverFaultU13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtDriverFaultU13.setStatus("current")
_VrcCompPtDriverFaultU14_Type = TruthValue
_VrcCompPtDriverFaultU14_Object = MibTableColumn
vrcCompPtDriverFaultU14 = _VrcCompPtDriverFaultU14_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 20),
    _VrcCompPtDriverFaultU14_Type()
)
vrcCompPtDriverFaultU14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtDriverFaultU14.setStatus("current")
_VrcCompPtDriverFaultU15_Type = TruthValue
_VrcCompPtDriverFaultU15_Object = MibTableColumn
vrcCompPtDriverFaultU15 = _VrcCompPtDriverFaultU15_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 21),
    _VrcCompPtDriverFaultU15_Type()
)
vrcCompPtDriverFaultU15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtDriverFaultU15.setStatus("current")
_VrcCompPtDriverCommFailAlarm_Type = TruthValue
_VrcCompPtDriverCommFailAlarm_Object = MibTableColumn
vrcCompPtDriverCommFailAlarm = _VrcCompPtDriverCommFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 22),
    _VrcCompPtDriverCommFailAlarm_Type()
)
vrcCompPtDriverCommFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtDriverCommFailAlarm.setStatus("current")
_VrcCompPtFaultLockAlarm_Type = TruthValue
_VrcCompPtFaultLockAlarm_Object = MibTableColumn
vrcCompPtFaultLockAlarm = _VrcCompPtFaultLockAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 8, 1, 23),
    _VrcCompPtFaultLockAlarm_Type()
)
vrcCompPtFaultLockAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcCompPtFaultLockAlarm.setStatus("current")
_VrcCompCfgTable_Object = MibTable
vrcCompCfgTable = _VrcCompCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9)
)
if mibBuilder.loadTexts:
    vrcCompCfgTable.setStatus("current")
_VrcCompCfgEntry_Object = MibTableRow
vrcCompCfgEntry = _VrcCompCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1)
)
vrcCompCfgEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "vrcCompCfgIndex"),
)
if mibBuilder.loadTexts:
    vrcCompCfgEntry.setStatus("current")


class _VrcCompCfgIndex_Type(Integer32):
    """Custom type vrcCompCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrcCompCfgIndex_Type.__name__ = "Integer32"
_VrcCompCfgIndex_Object = MibTableColumn
vrcCompCfgIndex = _VrcCompCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 1),
    _VrcCompCfgIndex_Type()
)
vrcCompCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrcCompCfgIndex.setStatus("current")
_VrcCompCfgOutputStatus_Type = TruthValue
_VrcCompCfgOutputStatus_Object = MibTableColumn
vrcCompCfgOutputStatus = _VrcCompCfgOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 2),
    _VrcCompCfgOutputStatus_Type()
)
vrcCompCfgOutputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgOutputStatus.setStatus("current")


class _VrcCompCfgOutputDeadBand_Type(Integer32):
    """Custom type vrcCompCfgOutputDeadBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_VrcCompCfgOutputDeadBand_Type.__name__ = "Integer32"
_VrcCompCfgOutputDeadBand_Object = MibTableColumn
vrcCompCfgOutputDeadBand = _VrcCompCfgOutputDeadBand_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 3),
    _VrcCompCfgOutputDeadBand_Type()
)
vrcCompCfgOutputDeadBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgOutputDeadBand.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgOutputDeadBand.setUnits("0.1%")


class _VrcCompCfgCapacityOutputValue_Type(Integer32):
    """Custom type vrcCompCfgCapacityOutputValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrcCompCfgCapacityOutputValue_Type.__name__ = "Integer32"
_VrcCompCfgCapacityOutputValue_Object = MibTableColumn
vrcCompCfgCapacityOutputValue = _VrcCompCfgCapacityOutputValue_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 4),
    _VrcCompCfgCapacityOutputValue_Type()
)
vrcCompCfgCapacityOutputValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgCapacityOutputValue.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgCapacityOutputValue.setUnits("%")


class _VrcCompCfgMinCapacity_Type(Integer32):
    """Custom type vrcCompCfgMinCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 50),
    )


_VrcCompCfgMinCapacity_Type.__name__ = "Integer32"
_VrcCompCfgMinCapacity_Object = MibTableColumn
vrcCompCfgMinCapacity = _VrcCompCfgMinCapacity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 5),
    _VrcCompCfgMinCapacity_Type()
)
vrcCompCfgMinCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgMinCapacity.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgMinCapacity.setUnits("%")


class _VrcCompCfgStartCapacity_Type(Integer32):
    """Custom type vrcCompCfgStartCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 100),
    )


_VrcCompCfgStartCapacity_Type.__name__ = "Integer32"
_VrcCompCfgStartCapacity_Object = MibTableColumn
vrcCompCfgStartCapacity = _VrcCompCfgStartCapacity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 6),
    _VrcCompCfgStartCapacity_Type()
)
vrcCompCfgStartCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgStartCapacity.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgStartCapacity.setUnits("%")


class _VrcCompCfgStandardCapacity_Type(Integer32):
    """Custom type vrcCompCfgStandardCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 100),
    )


_VrcCompCfgStandardCapacity_Type.__name__ = "Integer32"
_VrcCompCfgStandardCapacity_Object = MibTableColumn
vrcCompCfgStandardCapacity = _VrcCompCfgStandardCapacity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 7),
    _VrcCompCfgStandardCapacity_Type()
)
vrcCompCfgStandardCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgStandardCapacity.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgStandardCapacity.setUnits("%")


class _VrcCompCfgStartCfc_Type(Integer32):
    """Custom type vrcCompCfgStartCfc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrcCompCfgStartCfc_Type.__name__ = "Integer32"
_VrcCompCfgStartCfc_Object = MibTableColumn
vrcCompCfgStartCfc = _VrcCompCfgStartCfc_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 8),
    _VrcCompCfgStartCfc_Type()
)
vrcCompCfgStartCfc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgStartCfc.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgStartCfc.setUnits("%")


class _VrcCompCfgStopCfc_Type(Integer32):
    """Custom type vrcCompCfgStopCfc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, -50),
    )


_VrcCompCfgStopCfc_Type.__name__ = "Integer32"
_VrcCompCfgStopCfc_Object = MibTableColumn
vrcCompCfgStopCfc = _VrcCompCfgStopCfc_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 9),
    _VrcCompCfgStopCfc_Type()
)
vrcCompCfgStopCfc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgStopCfc.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgStopCfc.setUnits("%")


class _VrcCompCfgMinRunTime_Type(Integer32):
    """Custom type vrcCompCfgMinRunTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_VrcCompCfgMinRunTime_Type.__name__ = "Integer32"
_VrcCompCfgMinRunTime_Object = MibTableColumn
vrcCompCfgMinRunTime = _VrcCompCfgMinRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 10),
    _VrcCompCfgMinRunTime_Type()
)
vrcCompCfgMinRunTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgMinRunTime.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgMinRunTime.setUnits("minutes")


class _VrcCompCfgMinStopTime_Type(Integer32):
    """Custom type vrcCompCfgMinStopTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VrcCompCfgMinStopTime_Type.__name__ = "Integer32"
_VrcCompCfgMinStopTime_Object = MibTableColumn
vrcCompCfgMinStopTime = _VrcCompCfgMinStopTime_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 11),
    _VrcCompCfgMinStopTime_Type()
)
vrcCompCfgMinStopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgMinStopTime.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgMinStopTime.setUnits("minutes")


class _VrcCompCfgJumpBand1_Type(Integer32):
    """Custom type vrcCompCfgJumpBand1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrcCompCfgJumpBand1_Type.__name__ = "Integer32"
_VrcCompCfgJumpBand1_Object = MibTableColumn
vrcCompCfgJumpBand1 = _VrcCompCfgJumpBand1_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 12),
    _VrcCompCfgJumpBand1_Type()
)
vrcCompCfgJumpBand1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgJumpBand1.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgJumpBand1.setUnits("0.1%")


class _VrcCompCfgJumpBand2_Type(Integer32):
    """Custom type vrcCompCfgJumpBand2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrcCompCfgJumpBand2_Type.__name__ = "Integer32"
_VrcCompCfgJumpBand2_Object = MibTableColumn
vrcCompCfgJumpBand2 = _VrcCompCfgJumpBand2_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 13),
    _VrcCompCfgJumpBand2_Type()
)
vrcCompCfgJumpBand2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgJumpBand2.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgJumpBand2.setUnits("0.1%")


class _VrcCompCfgJumpBand3_Type(Integer32):
    """Custom type vrcCompCfgJumpBand3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrcCompCfgJumpBand3_Type.__name__ = "Integer32"
_VrcCompCfgJumpBand3_Object = MibTableColumn
vrcCompCfgJumpBand3 = _VrcCompCfgJumpBand3_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 14),
    _VrcCompCfgJumpBand3_Type()
)
vrcCompCfgJumpBand3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgJumpBand3.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgJumpBand3.setUnits("0.1%")


class _VrcCompCfgJumpBand4_Type(Integer32):
    """Custom type vrcCompCfgJumpBand4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrcCompCfgJumpBand4_Type.__name__ = "Integer32"
_VrcCompCfgJumpBand4_Object = MibTableColumn
vrcCompCfgJumpBand4 = _VrcCompCfgJumpBand4_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 15),
    _VrcCompCfgJumpBand4_Type()
)
vrcCompCfgJumpBand4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgJumpBand4.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgJumpBand4.setUnits("0.1%")


class _VrcCompCfgJumpBand5_Type(Integer32):
    """Custom type vrcCompCfgJumpBand5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrcCompCfgJumpBand5_Type.__name__ = "Integer32"
_VrcCompCfgJumpBand5_Object = MibTableColumn
vrcCompCfgJumpBand5 = _VrcCompCfgJumpBand5_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 16),
    _VrcCompCfgJumpBand5_Type()
)
vrcCompCfgJumpBand5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgJumpBand5.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgJumpBand5.setUnits("0.1%")


class _VrcCompCfgJumpFreq1_Type(Integer32):
    """Custom type vrcCompCfgJumpFreq1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_VrcCompCfgJumpFreq1_Type.__name__ = "Integer32"
_VrcCompCfgJumpFreq1_Object = MibTableColumn
vrcCompCfgJumpFreq1 = _VrcCompCfgJumpFreq1_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 17),
    _VrcCompCfgJumpFreq1_Type()
)
vrcCompCfgJumpFreq1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgJumpFreq1.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgJumpFreq1.setUnits("0.1%")


class _VrcCompCfgJumpFreq2_Type(Integer32):
    """Custom type vrcCompCfgJumpFreq2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_VrcCompCfgJumpFreq2_Type.__name__ = "Integer32"
_VrcCompCfgJumpFreq2_Object = MibTableColumn
vrcCompCfgJumpFreq2 = _VrcCompCfgJumpFreq2_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 18),
    _VrcCompCfgJumpFreq2_Type()
)
vrcCompCfgJumpFreq2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgJumpFreq2.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgJumpFreq2.setUnits("0.1%")


class _VrcCompCfgJumpFreq3_Type(Integer32):
    """Custom type vrcCompCfgJumpFreq3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_VrcCompCfgJumpFreq3_Type.__name__ = "Integer32"
_VrcCompCfgJumpFreq3_Object = MibTableColumn
vrcCompCfgJumpFreq3 = _VrcCompCfgJumpFreq3_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 19),
    _VrcCompCfgJumpFreq3_Type()
)
vrcCompCfgJumpFreq3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgJumpFreq3.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgJumpFreq3.setUnits("0.1%")


class _VrcCompCfgJumpFreq4_Type(Integer32):
    """Custom type vrcCompCfgJumpFreq4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_VrcCompCfgJumpFreq4_Type.__name__ = "Integer32"
_VrcCompCfgJumpFreq4_Object = MibTableColumn
vrcCompCfgJumpFreq4 = _VrcCompCfgJumpFreq4_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 20),
    _VrcCompCfgJumpFreq4_Type()
)
vrcCompCfgJumpFreq4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgJumpFreq4.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgJumpFreq4.setUnits("0.1%")


class _VrcCompCfgJumpFreq5_Type(Integer32):
    """Custom type vrcCompCfgJumpFreq5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_VrcCompCfgJumpFreq5_Type.__name__ = "Integer32"
_VrcCompCfgJumpFreq5_Object = MibTableColumn
vrcCompCfgJumpFreq5 = _VrcCompCfgJumpFreq5_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 21),
    _VrcCompCfgJumpFreq5_Type()
)
vrcCompCfgJumpFreq5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgJumpFreq5.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgJumpFreq5.setUnits("0.1%")
_VrcCompCfgTempP_Type = Integer32
_VrcCompCfgTempP_Object = MibTableColumn
vrcCompCfgTempP = _VrcCompCfgTempP_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 22),
    _VrcCompCfgTempP_Type()
)
vrcCompCfgTempP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgTempP.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgTempP.setUnits("decidegrees")


class _VrcCompCfgTempI_Type(Integer32):
    """Custom type vrcCompCfgTempI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_VrcCompCfgTempI_Type.__name__ = "Integer32"
_VrcCompCfgTempI_Object = MibTableColumn
vrcCompCfgTempI = _VrcCompCfgTempI_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 23),
    _VrcCompCfgTempI_Type()
)
vrcCompCfgTempI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgTempI.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgTempI.setUnits("seconds")


class _VrcCompCfgTempD_Type(Integer32):
    """Custom type vrcCompCfgTempD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_VrcCompCfgTempD_Type.__name__ = "Integer32"
_VrcCompCfgTempD_Object = MibTableColumn
vrcCompCfgTempD = _VrcCompCfgTempD_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 24),
    _VrcCompCfgTempD_Type()
)
vrcCompCfgTempD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgTempD.setStatus("current")
if mibBuilder.loadTexts:
    vrcCompCfgTempD.setUnits("seconds")


class _VrcCompCfgDriverFaultAlmCtrl_Type(Integer32):
    """Custom type vrcCompCfgDriverFaultAlmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("suspend", 2),
          ("open", 3))
    )


_VrcCompCfgDriverFaultAlmCtrl_Type.__name__ = "Integer32"
_VrcCompCfgDriverFaultAlmCtrl_Object = MibTableColumn
vrcCompCfgDriverFaultAlmCtrl = _VrcCompCfgDriverFaultAlmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 25),
    _VrcCompCfgDriverFaultAlmCtrl_Type()
)
vrcCompCfgDriverFaultAlmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgDriverFaultAlmCtrl.setStatus("current")


class _VrcCompCfgDriverCommFailAlmCtrl_Type(Integer32):
    """Custom type vrcCompCfgDriverCommFailAlmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("suspend", 2),
          ("open", 3))
    )


_VrcCompCfgDriverCommFailAlmCtrl_Type.__name__ = "Integer32"
_VrcCompCfgDriverCommFailAlmCtrl_Object = MibTableColumn
vrcCompCfgDriverCommFailAlmCtrl = _VrcCompCfgDriverCommFailAlmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 26),
    _VrcCompCfgDriverCommFailAlmCtrl_Type()
)
vrcCompCfgDriverCommFailAlmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgDriverCommFailAlmCtrl.setStatus("current")


class _VrcCompCfgFaultLockAlmCtrl_Type(Integer32):
    """Custom type vrcCompCfgFaultLockAlmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("suspend", 2),
          ("open", 3))
    )


_VrcCompCfgFaultLockAlmCtrl_Type.__name__ = "Integer32"
_VrcCompCfgFaultLockAlmCtrl_Object = MibTableColumn
vrcCompCfgFaultLockAlmCtrl = _VrcCompCfgFaultLockAlmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 9, 1, 27),
    _VrcCompCfgFaultLockAlmCtrl_Type()
)
vrcCompCfgFaultLockAlmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcCompCfgFaultLockAlmCtrl.setStatus("current")
_VrcReturnPtTable_Object = MibTable
vrcReturnPtTable = _VrcReturnPtTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 10)
)
if mibBuilder.loadTexts:
    vrcReturnPtTable.setStatus("current")
_VrcReturnPtEntry_Object = MibTableRow
vrcReturnPtEntry = _VrcReturnPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 10, 1)
)
vrcReturnPtEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "vrcReturnPtIndex"),
)
if mibBuilder.loadTexts:
    vrcReturnPtEntry.setStatus("current")


class _VrcReturnPtIndex_Type(Integer32):
    """Custom type vrcReturnPtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrcReturnPtIndex_Type.__name__ = "Integer32"
_VrcReturnPtIndex_Object = MibTableColumn
vrcReturnPtIndex = _VrcReturnPtIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 10, 1, 1),
    _VrcReturnPtIndex_Type()
)
vrcReturnPtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrcReturnPtIndex.setStatus("current")


class _VrcReturnPtName_Type(SnmpAdminString):
    """Custom type vrcReturnPtName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_VrcReturnPtName_Type.__name__ = "SnmpAdminString"
_VrcReturnPtName_Object = MibTableColumn
vrcReturnPtName = _VrcReturnPtName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 10, 1, 2),
    _VrcReturnPtName_Type()
)
vrcReturnPtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcReturnPtName.setStatus("current")
_VrcReturnPtTemp_Type = Integer32
_VrcReturnPtTemp_Object = MibTableColumn
vrcReturnPtTemp = _VrcReturnPtTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 10, 1, 3),
    _VrcReturnPtTemp_Type()
)
vrcReturnPtTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcReturnPtTemp.setStatus("current")
if mibBuilder.loadTexts:
    vrcReturnPtTemp.setUnits("decidegrees")
_VrcReturnPtHighTempAlarm_Type = TruthValue
_VrcReturnPtHighTempAlarm_Object = MibTableColumn
vrcReturnPtHighTempAlarm = _VrcReturnPtHighTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 10, 1, 4),
    _VrcReturnPtHighTempAlarm_Type()
)
vrcReturnPtHighTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcReturnPtHighTempAlarm.setStatus("current")
_VrcReturnPtTempSensorFailAlarm_Type = TruthValue
_VrcReturnPtTempSensorFailAlarm_Object = MibTableColumn
vrcReturnPtTempSensorFailAlarm = _VrcReturnPtTempSensorFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 10, 1, 5),
    _VrcReturnPtTempSensorFailAlarm_Type()
)
vrcReturnPtTempSensorFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcReturnPtTempSensorFailAlarm.setStatus("current")
_VrcReturnCfgTable_Object = MibTable
vrcReturnCfgTable = _VrcReturnCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 11)
)
if mibBuilder.loadTexts:
    vrcReturnCfgTable.setStatus("current")
_VrcReturnCfgEntry_Object = MibTableRow
vrcReturnCfgEntry = _VrcReturnCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 11, 1)
)
vrcReturnCfgEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "vrcReturnCfgIndex"),
)
if mibBuilder.loadTexts:
    vrcReturnCfgEntry.setStatus("current")


class _VrcReturnCfgIndex_Type(Integer32):
    """Custom type vrcReturnCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrcReturnCfgIndex_Type.__name__ = "Integer32"
_VrcReturnCfgIndex_Object = MibTableColumn
vrcReturnCfgIndex = _VrcReturnCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 11, 1, 1),
    _VrcReturnCfgIndex_Type()
)
vrcReturnCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrcReturnCfgIndex.setStatus("current")


class _VrcReturnCfgOilCycle_Type(Integer32):
    """Custom type vrcReturnCfgOilCycle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 50),
    )


_VrcReturnCfgOilCycle_Type.__name__ = "Integer32"
_VrcReturnCfgOilCycle_Object = MibTableColumn
vrcReturnCfgOilCycle = _VrcReturnCfgOilCycle_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 11, 1, 2),
    _VrcReturnCfgOilCycle_Type()
)
vrcReturnCfgOilCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcReturnCfgOilCycle.setStatus("current")
if mibBuilder.loadTexts:
    vrcReturnCfgOilCycle.setUnits("decihours")


class _VrcReturnCfgOilRunCapacity_Type(Integer32):
    """Custom type vrcReturnCfgOilRunCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 100),
    )


_VrcReturnCfgOilRunCapacity_Type.__name__ = "Integer32"
_VrcReturnCfgOilRunCapacity_Object = MibTableColumn
vrcReturnCfgOilRunCapacity = _VrcReturnCfgOilRunCapacity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 11, 1, 3),
    _VrcReturnCfgOilRunCapacity_Type()
)
vrcReturnCfgOilRunCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcReturnCfgOilRunCapacity.setStatus("current")
if mibBuilder.loadTexts:
    vrcReturnCfgOilRunCapacity.setUnits("%")


class _VrcReturnCfgOilRunTime_Type(Integer32):
    """Custom type vrcReturnCfgOilRunTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VrcReturnCfgOilRunTime_Type.__name__ = "Integer32"
_VrcReturnCfgOilRunTime_Object = MibTableColumn
vrcReturnCfgOilRunTime = _VrcReturnCfgOilRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 11, 1, 4),
    _VrcReturnCfgOilRunTime_Type()
)
vrcReturnCfgOilRunTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcReturnCfgOilRunTime.setStatus("current")
if mibBuilder.loadTexts:
    vrcReturnCfgOilRunTime.setUnits("minutes")
_VrcReturnCfgTempCalValue_Type = Integer32
_VrcReturnCfgTempCalValue_Object = MibTableColumn
vrcReturnCfgTempCalValue = _VrcReturnCfgTempCalValue_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 11, 1, 5),
    _VrcReturnCfgTempCalValue_Type()
)
vrcReturnCfgTempCalValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcReturnCfgTempCalValue.setStatus("current")
if mibBuilder.loadTexts:
    vrcReturnCfgTempCalValue.setUnits("decidegrees")
_VrcReturnCfgTempSetting_Type = Integer32
_VrcReturnCfgTempSetting_Object = MibTableColumn
vrcReturnCfgTempSetting = _VrcReturnCfgTempSetting_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 11, 1, 6),
    _VrcReturnCfgTempSetting_Type()
)
vrcReturnCfgTempSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcReturnCfgTempSetting.setStatus("current")
if mibBuilder.loadTexts:
    vrcReturnCfgTempSetting.setUnits("decidegrees")
_VrcReturnCfgHighTempAlarmValue_Type = Integer32
_VrcReturnCfgHighTempAlarmValue_Object = MibTableColumn
vrcReturnCfgHighTempAlarmValue = _VrcReturnCfgHighTempAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 11, 1, 7),
    _VrcReturnCfgHighTempAlarmValue_Type()
)
vrcReturnCfgHighTempAlarmValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcReturnCfgHighTempAlarmValue.setStatus("current")
if mibBuilder.loadTexts:
    vrcReturnCfgHighTempAlarmValue.setUnits("decidegrees")


class _VrcReturnCfgHighTempAlarmCtrl_Type(Integer32):
    """Custom type vrcReturnCfgHighTempAlarmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("close", 1),
          ("suspend", 2),
          ("open", 3))
    )


_VrcReturnCfgHighTempAlarmCtrl_Type.__name__ = "Integer32"
_VrcReturnCfgHighTempAlarmCtrl_Object = MibTableColumn
vrcReturnCfgHighTempAlarmCtrl = _VrcReturnCfgHighTempAlarmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 11, 1, 8),
    _VrcReturnCfgHighTempAlarmCtrl_Type()
)
vrcReturnCfgHighTempAlarmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcReturnCfgHighTempAlarmCtrl.setStatus("current")


class _VrcReturnCfgTempSensFailAlmCtrl_Type(Integer32):
    """Custom type vrcReturnCfgTempSensFailAlmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("close", 1),
          ("suspend", 2),
          ("open", 3))
    )


_VrcReturnCfgTempSensFailAlmCtrl_Type.__name__ = "Integer32"
_VrcReturnCfgTempSensFailAlmCtrl_Object = MibTableColumn
vrcReturnCfgTempSensFailAlmCtrl = _VrcReturnCfgTempSensFailAlmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 11, 1, 9),
    _VrcReturnCfgTempSensFailAlmCtrl_Type()
)
vrcReturnCfgTempSensFailAlmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcReturnCfgTempSensFailAlmCtrl.setStatus("current")
_VrcSupplyPtTable_Object = MibTable
vrcSupplyPtTable = _VrcSupplyPtTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 12)
)
if mibBuilder.loadTexts:
    vrcSupplyPtTable.setStatus("current")
_VrcSupplyPtEntry_Object = MibTableRow
vrcSupplyPtEntry = _VrcSupplyPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 12, 1)
)
vrcSupplyPtEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "vrcSupplyPtIndex"),
)
if mibBuilder.loadTexts:
    vrcSupplyPtEntry.setStatus("current")


class _VrcSupplyPtIndex_Type(Integer32):
    """Custom type vrcSupplyPtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrcSupplyPtIndex_Type.__name__ = "Integer32"
_VrcSupplyPtIndex_Object = MibTableColumn
vrcSupplyPtIndex = _VrcSupplyPtIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 12, 1, 1),
    _VrcSupplyPtIndex_Type()
)
vrcSupplyPtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrcSupplyPtIndex.setStatus("current")


class _VrcSupplyPtName_Type(SnmpAdminString):
    """Custom type vrcSupplyPtName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_VrcSupplyPtName_Type.__name__ = "SnmpAdminString"
_VrcSupplyPtName_Object = MibTableColumn
vrcSupplyPtName = _VrcSupplyPtName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 12, 1, 2),
    _VrcSupplyPtName_Type()
)
vrcSupplyPtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcSupplyPtName.setStatus("current")
_VrcSupplyPtTemp_Type = Integer32
_VrcSupplyPtTemp_Object = MibTableColumn
vrcSupplyPtTemp = _VrcSupplyPtTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 12, 1, 3),
    _VrcSupplyPtTemp_Type()
)
vrcSupplyPtTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcSupplyPtTemp.setStatus("current")
if mibBuilder.loadTexts:
    vrcSupplyPtTemp.setUnits("decidegrees")
_VrcSupplyPtLowTempAlarm_Type = TruthValue
_VrcSupplyPtLowTempAlarm_Object = MibTableColumn
vrcSupplyPtLowTempAlarm = _VrcSupplyPtLowTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 12, 1, 4),
    _VrcSupplyPtLowTempAlarm_Type()
)
vrcSupplyPtLowTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcSupplyPtLowTempAlarm.setStatus("current")
_VrcSupplyPtHighTempAlarm_Type = TruthValue
_VrcSupplyPtHighTempAlarm_Object = MibTableColumn
vrcSupplyPtHighTempAlarm = _VrcSupplyPtHighTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 12, 1, 5),
    _VrcSupplyPtHighTempAlarm_Type()
)
vrcSupplyPtHighTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcSupplyPtHighTempAlarm.setStatus("current")
_VrcSupplyPtTempSensorFailAlarm_Type = TruthValue
_VrcSupplyPtTempSensorFailAlarm_Object = MibTableColumn
vrcSupplyPtTempSensorFailAlarm = _VrcSupplyPtTempSensorFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 12, 1, 6),
    _VrcSupplyPtTempSensorFailAlarm_Type()
)
vrcSupplyPtTempSensorFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcSupplyPtTempSensorFailAlarm.setStatus("current")
_VrcSupplyCfgTable_Object = MibTable
vrcSupplyCfgTable = _VrcSupplyCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 13)
)
if mibBuilder.loadTexts:
    vrcSupplyCfgTable.setStatus("current")
_VrcSupplyCfgEntry_Object = MibTableRow
vrcSupplyCfgEntry = _VrcSupplyCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 13, 1)
)
vrcSupplyCfgEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "vrcSupplyCfgIndex"),
)
if mibBuilder.loadTexts:
    vrcSupplyCfgEntry.setStatus("current")


class _VrcSupplyCfgIndex_Type(Integer32):
    """Custom type vrcSupplyCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrcSupplyCfgIndex_Type.__name__ = "Integer32"
_VrcSupplyCfgIndex_Object = MibTableColumn
vrcSupplyCfgIndex = _VrcSupplyCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 13, 1, 1),
    _VrcSupplyCfgIndex_Type()
)
vrcSupplyCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrcSupplyCfgIndex.setStatus("current")
_VrcSupplyCfgTempCalValue_Type = Integer32
_VrcSupplyCfgTempCalValue_Object = MibTableColumn
vrcSupplyCfgTempCalValue = _VrcSupplyCfgTempCalValue_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 13, 1, 2),
    _VrcSupplyCfgTempCalValue_Type()
)
vrcSupplyCfgTempCalValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcSupplyCfgTempCalValue.setStatus("current")
if mibBuilder.loadTexts:
    vrcSupplyCfgTempCalValue.setUnits("decidegrees")
_VrcSupplyCfgTempSetting_Type = Integer32
_VrcSupplyCfgTempSetting_Object = MibTableColumn
vrcSupplyCfgTempSetting = _VrcSupplyCfgTempSetting_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 13, 1, 3),
    _VrcSupplyCfgTempSetting_Type()
)
vrcSupplyCfgTempSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcSupplyCfgTempSetting.setStatus("current")
if mibBuilder.loadTexts:
    vrcSupplyCfgTempSetting.setUnits("decidegrees")
_VrcSupplyCfgLowTempAlarmValue_Type = Integer32
_VrcSupplyCfgLowTempAlarmValue_Object = MibTableColumn
vrcSupplyCfgLowTempAlarmValue = _VrcSupplyCfgLowTempAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 13, 1, 4),
    _VrcSupplyCfgLowTempAlarmValue_Type()
)
vrcSupplyCfgLowTempAlarmValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcSupplyCfgLowTempAlarmValue.setStatus("current")
if mibBuilder.loadTexts:
    vrcSupplyCfgLowTempAlarmValue.setUnits("decidegrees")
_VrcSupplyCfgHighTempAlarmValue_Type = Integer32
_VrcSupplyCfgHighTempAlarmValue_Object = MibTableColumn
vrcSupplyCfgHighTempAlarmValue = _VrcSupplyCfgHighTempAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 13, 1, 5),
    _VrcSupplyCfgHighTempAlarmValue_Type()
)
vrcSupplyCfgHighTempAlarmValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcSupplyCfgHighTempAlarmValue.setStatus("current")
if mibBuilder.loadTexts:
    vrcSupplyCfgHighTempAlarmValue.setUnits("decidegrees")


class _VrcSupplyCfgLowTempAlmCtrl_Type(Integer32):
    """Custom type vrcSupplyCfgLowTempAlmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("close", 1),
          ("suspend", 2),
          ("open", 3))
    )


_VrcSupplyCfgLowTempAlmCtrl_Type.__name__ = "Integer32"
_VrcSupplyCfgLowTempAlmCtrl_Object = MibTableColumn
vrcSupplyCfgLowTempAlmCtrl = _VrcSupplyCfgLowTempAlmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 13, 1, 6),
    _VrcSupplyCfgLowTempAlmCtrl_Type()
)
vrcSupplyCfgLowTempAlmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcSupplyCfgLowTempAlmCtrl.setStatus("current")


class _VrcSupplyCfgHighTempAlmCtrl_Type(Integer32):
    """Custom type vrcSupplyCfgHighTempAlmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("close", 1),
          ("suspend", 2),
          ("open", 3))
    )


_VrcSupplyCfgHighTempAlmCtrl_Type.__name__ = "Integer32"
_VrcSupplyCfgHighTempAlmCtrl_Object = MibTableColumn
vrcSupplyCfgHighTempAlmCtrl = _VrcSupplyCfgHighTempAlmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 13, 1, 7),
    _VrcSupplyCfgHighTempAlmCtrl_Type()
)
vrcSupplyCfgHighTempAlmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcSupplyCfgHighTempAlmCtrl.setStatus("current")


class _VrcSupplyCfgTempSensFailAlmCtrl_Type(Integer32):
    """Custom type vrcSupplyCfgTempSensFailAlmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("close", 1),
          ("suspend", 2),
          ("open", 3))
    )


_VrcSupplyCfgTempSensFailAlmCtrl_Type.__name__ = "Integer32"
_VrcSupplyCfgTempSensFailAlmCtrl_Object = MibTableColumn
vrcSupplyCfgTempSensFailAlmCtrl = _VrcSupplyCfgTempSensFailAlmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 13, 1, 8),
    _VrcSupplyCfgTempSensFailAlmCtrl_Type()
)
vrcSupplyCfgTempSensFailAlmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcSupplyCfgTempSensFailAlmCtrl.setStatus("current")
_VrcPowerPtTable_Object = MibTable
vrcPowerPtTable = _VrcPowerPtTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 14)
)
if mibBuilder.loadTexts:
    vrcPowerPtTable.setStatus("current")
_VrcPowerPtEntry_Object = MibTableRow
vrcPowerPtEntry = _VrcPowerPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 14, 1)
)
vrcPowerPtEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "vrcPowerPtIndex"),
)
if mibBuilder.loadTexts:
    vrcPowerPtEntry.setStatus("current")


class _VrcPowerPtIndex_Type(Integer32):
    """Custom type vrcPowerPtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrcPowerPtIndex_Type.__name__ = "Integer32"
_VrcPowerPtIndex_Object = MibTableColumn
vrcPowerPtIndex = _VrcPowerPtIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 14, 1, 1),
    _VrcPowerPtIndex_Type()
)
vrcPowerPtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrcPowerPtIndex.setStatus("current")


class _VrcPowerPtName_Type(SnmpAdminString):
    """Custom type vrcPowerPtName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_VrcPowerPtName_Type.__name__ = "SnmpAdminString"
_VrcPowerPtName_Object = MibTableColumn
vrcPowerPtName = _VrcPowerPtName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 14, 1, 2),
    _VrcPowerPtName_Type()
)
vrcPowerPtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcPowerPtName.setStatus("current")


class _VrcPowerPtVoltage_Type(Integer32):
    """Custom type vrcPowerPtVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_VrcPowerPtVoltage_Type.__name__ = "Integer32"
_VrcPowerPtVoltage_Object = MibTableColumn
vrcPowerPtVoltage = _VrcPowerPtVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 14, 1, 3),
    _VrcPowerPtVoltage_Type()
)
vrcPowerPtVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcPowerPtVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vrcPowerPtVoltage.setUnits("decivolts")


class _VrcPowerPtFrequency_Type(Integer32):
    """Custom type vrcPowerPtFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_VrcPowerPtFrequency_Type.__name__ = "Integer32"
_VrcPowerPtFrequency_Object = MibTableColumn
vrcPowerPtFrequency = _VrcPowerPtFrequency_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 14, 1, 4),
    _VrcPowerPtFrequency_Type()
)
vrcPowerPtFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcPowerPtFrequency.setStatus("current")
if mibBuilder.loadTexts:
    vrcPowerPtFrequency.setUnits("decihertz")
_VrcPowerPtLowVoltageAlarm_Type = TruthValue
_VrcPowerPtLowVoltageAlarm_Object = MibTableColumn
vrcPowerPtLowVoltageAlarm = _VrcPowerPtLowVoltageAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 14, 1, 5),
    _VrcPowerPtLowVoltageAlarm_Type()
)
vrcPowerPtLowVoltageAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcPowerPtLowVoltageAlarm.setStatus("current")
_VrcPowerPtHighVoltageAlarm_Type = TruthValue
_VrcPowerPtHighVoltageAlarm_Object = MibTableColumn
vrcPowerPtHighVoltageAlarm = _VrcPowerPtHighVoltageAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 14, 1, 6),
    _VrcPowerPtHighVoltageAlarm_Type()
)
vrcPowerPtHighVoltageAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcPowerPtHighVoltageAlarm.setStatus("current")
_VrcPowerPtLossOfPhasePowerAlarm_Type = TruthValue
_VrcPowerPtLossOfPhasePowerAlarm_Object = MibTableColumn
vrcPowerPtLossOfPhasePowerAlarm = _VrcPowerPtLossOfPhasePowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 14, 1, 7),
    _VrcPowerPtLossOfPhasePowerAlarm_Type()
)
vrcPowerPtLossOfPhasePowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcPowerPtLossOfPhasePowerAlarm.setStatus("current")
_VrcPowerPtLossOfPowerAlarm_Type = TruthValue
_VrcPowerPtLossOfPowerAlarm_Object = MibTableColumn
vrcPowerPtLossOfPowerAlarm = _VrcPowerPtLossOfPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 14, 1, 8),
    _VrcPowerPtLossOfPowerAlarm_Type()
)
vrcPowerPtLossOfPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcPowerPtLossOfPowerAlarm.setStatus("current")
_VrcPowerPtFrequencyErrorAlarm_Type = TruthValue
_VrcPowerPtFrequencyErrorAlarm_Object = MibTableColumn
vrcPowerPtFrequencyErrorAlarm = _VrcPowerPtFrequencyErrorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 14, 1, 9),
    _VrcPowerPtFrequencyErrorAlarm_Type()
)
vrcPowerPtFrequencyErrorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcPowerPtFrequencyErrorAlarm.setStatus("current")
_VrcPowerCfgTable_Object = MibTable
vrcPowerCfgTable = _VrcPowerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 15)
)
if mibBuilder.loadTexts:
    vrcPowerCfgTable.setStatus("current")
_VrcPowerCfgEntry_Object = MibTableRow
vrcPowerCfgEntry = _VrcPowerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 15, 1)
)
vrcPowerCfgEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "vrcPowerCfgIndex"),
)
if mibBuilder.loadTexts:
    vrcPowerCfgEntry.setStatus("current")


class _VrcPowerCfgIndex_Type(Integer32):
    """Custom type vrcPowerCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrcPowerCfgIndex_Type.__name__ = "Integer32"
_VrcPowerCfgIndex_Object = MibTableColumn
vrcPowerCfgIndex = _VrcPowerCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 15, 1, 1),
    _VrcPowerCfgIndex_Type()
)
vrcPowerCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrcPowerCfgIndex.setStatus("current")


class _VrcPowerCfgLowVoltageSetting_Type(Integer32):
    """Custom type vrcPowerCfgLowVoltageSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 230),
    )


_VrcPowerCfgLowVoltageSetting_Type.__name__ = "Integer32"
_VrcPowerCfgLowVoltageSetting_Object = MibTableColumn
vrcPowerCfgLowVoltageSetting = _VrcPowerCfgLowVoltageSetting_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 15, 1, 2),
    _VrcPowerCfgLowVoltageSetting_Type()
)
vrcPowerCfgLowVoltageSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcPowerCfgLowVoltageSetting.setStatus("current")
if mibBuilder.loadTexts:
    vrcPowerCfgLowVoltageSetting.setUnits("volts")


class _VrcPowerCfgHighVoltageSetting_Type(Integer32):
    """Custom type vrcPowerCfgHighVoltageSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 300),
    )


_VrcPowerCfgHighVoltageSetting_Type.__name__ = "Integer32"
_VrcPowerCfgHighVoltageSetting_Object = MibTableColumn
vrcPowerCfgHighVoltageSetting = _VrcPowerCfgHighVoltageSetting_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 15, 1, 3),
    _VrcPowerCfgHighVoltageSetting_Type()
)
vrcPowerCfgHighVoltageSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcPowerCfgHighVoltageSetting.setStatus("current")
if mibBuilder.loadTexts:
    vrcPowerCfgHighVoltageSetting.setUnits("volts")


class _VrcPowerCfgLowVoltageAlarmCtrl_Type(Integer32):
    """Custom type vrcPowerCfgLowVoltageAlarmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("close", 1),
          ("suspend", 2),
          ("open", 3))
    )


_VrcPowerCfgLowVoltageAlarmCtrl_Type.__name__ = "Integer32"
_VrcPowerCfgLowVoltageAlarmCtrl_Object = MibTableColumn
vrcPowerCfgLowVoltageAlarmCtrl = _VrcPowerCfgLowVoltageAlarmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 15, 1, 4),
    _VrcPowerCfgLowVoltageAlarmCtrl_Type()
)
vrcPowerCfgLowVoltageAlarmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcPowerCfgLowVoltageAlarmCtrl.setStatus("current")


class _VrcPowerCfgHighVoltageAlarmCtrl_Type(Integer32):
    """Custom type vrcPowerCfgHighVoltageAlarmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("close", 1),
          ("suspend", 2),
          ("open", 3))
    )


_VrcPowerCfgHighVoltageAlarmCtrl_Type.__name__ = "Integer32"
_VrcPowerCfgHighVoltageAlarmCtrl_Object = MibTableColumn
vrcPowerCfgHighVoltageAlarmCtrl = _VrcPowerCfgHighVoltageAlarmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 15, 1, 5),
    _VrcPowerCfgHighVoltageAlarmCtrl_Type()
)
vrcPowerCfgHighVoltageAlarmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcPowerCfgHighVoltageAlarmCtrl.setStatus("current")


class _VrcPowerCfgLossOfPowerAlarmCtrl_Type(Integer32):
    """Custom type vrcPowerCfgLossOfPowerAlarmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("close", 1),
          ("suspend", 2),
          ("open", 3))
    )


_VrcPowerCfgLossOfPowerAlarmCtrl_Type.__name__ = "Integer32"
_VrcPowerCfgLossOfPowerAlarmCtrl_Object = MibTableColumn
vrcPowerCfgLossOfPowerAlarmCtrl = _VrcPowerCfgLossOfPowerAlarmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 15, 1, 6),
    _VrcPowerCfgLossOfPowerAlarmCtrl_Type()
)
vrcPowerCfgLossOfPowerAlarmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcPowerCfgLossOfPowerAlarmCtrl.setStatus("current")


class _VrcPowerCfgFreqErrorAlarmCtrl_Type(Integer32):
    """Custom type vrcPowerCfgFreqErrorAlarmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("close", 1),
          ("suspend", 2),
          ("open", 3))
    )


_VrcPowerCfgFreqErrorAlarmCtrl_Type.__name__ = "Integer32"
_VrcPowerCfgFreqErrorAlarmCtrl_Object = MibTableColumn
vrcPowerCfgFreqErrorAlarmCtrl = _VrcPowerCfgFreqErrorAlarmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 15, 1, 7),
    _VrcPowerCfgFreqErrorAlarmCtrl_Type()
)
vrcPowerCfgFreqErrorAlarmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcPowerCfgFreqErrorAlarmCtrl.setStatus("current")
_VrcOutdoorPtTable_Object = MibTable
vrcOutdoorPtTable = _VrcOutdoorPtTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 16)
)
if mibBuilder.loadTexts:
    vrcOutdoorPtTable.setStatus("current")
_VrcOutdoorPtEntry_Object = MibTableRow
vrcOutdoorPtEntry = _VrcOutdoorPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 16, 1)
)
vrcOutdoorPtEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "vrcOutdoorPtIndex"),
)
if mibBuilder.loadTexts:
    vrcOutdoorPtEntry.setStatus("current")


class _VrcOutdoorPtIndex_Type(Integer32):
    """Custom type vrcOutdoorPtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrcOutdoorPtIndex_Type.__name__ = "Integer32"
_VrcOutdoorPtIndex_Object = MibTableColumn
vrcOutdoorPtIndex = _VrcOutdoorPtIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 16, 1, 1),
    _VrcOutdoorPtIndex_Type()
)
vrcOutdoorPtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrcOutdoorPtIndex.setStatus("current")


class _VrcOutdoorPtName_Type(SnmpAdminString):
    """Custom type vrcOutdoorPtName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_VrcOutdoorPtName_Type.__name__ = "SnmpAdminString"
_VrcOutdoorPtName_Object = MibTableColumn
vrcOutdoorPtName = _VrcOutdoorPtName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 16, 1, 2),
    _VrcOutdoorPtName_Type()
)
vrcOutdoorPtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcOutdoorPtName.setStatus("current")
_VrcOutdoorPtTemp_Type = Integer32
_VrcOutdoorPtTemp_Object = MibTableColumn
vrcOutdoorPtTemp = _VrcOutdoorPtTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 16, 1, 3),
    _VrcOutdoorPtTemp_Type()
)
vrcOutdoorPtTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcOutdoorPtTemp.setStatus("current")
if mibBuilder.loadTexts:
    vrcOutdoorPtTemp.setUnits("decidegrees")
_VrcDischPtTable_Object = MibTable
vrcDischPtTable = _VrcDischPtTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 18)
)
if mibBuilder.loadTexts:
    vrcDischPtTable.setStatus("current")
_VrcDischPtEntry_Object = MibTableRow
vrcDischPtEntry = _VrcDischPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 18, 1)
)
vrcDischPtEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "vrcDischPtIndex"),
)
if mibBuilder.loadTexts:
    vrcDischPtEntry.setStatus("current")


class _VrcDischPtIndex_Type(Integer32):
    """Custom type vrcDischPtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrcDischPtIndex_Type.__name__ = "Integer32"
_VrcDischPtIndex_Object = MibTableColumn
vrcDischPtIndex = _VrcDischPtIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 18, 1, 1),
    _VrcDischPtIndex_Type()
)
vrcDischPtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrcDischPtIndex.setStatus("current")


class _VrcDischPtName_Type(SnmpAdminString):
    """Custom type vrcDischPtName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_VrcDischPtName_Type.__name__ = "SnmpAdminString"
_VrcDischPtName_Object = MibTableColumn
vrcDischPtName = _VrcDischPtName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 18, 1, 2),
    _VrcDischPtName_Type()
)
vrcDischPtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcDischPtName.setStatus("current")
_VrcDischPtTemp_Type = Integer32
_VrcDischPtTemp_Object = MibTableColumn
vrcDischPtTemp = _VrcDischPtTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 18, 1, 3),
    _VrcDischPtTemp_Type()
)
vrcDischPtTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcDischPtTemp.setStatus("current")
if mibBuilder.loadTexts:
    vrcDischPtTemp.setUnits("decidegrees")


class _VrcDischPtPressure_Type(Integer32):
    """Custom type vrcDischPtPressure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 460),
    )


_VrcDischPtPressure_Type.__name__ = "Integer32"
_VrcDischPtPressure_Object = MibTableColumn
vrcDischPtPressure = _VrcDischPtPressure_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 18, 1, 4),
    _VrcDischPtPressure_Type()
)
vrcDischPtPressure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcDischPtPressure.setStatus("current")
if mibBuilder.loadTexts:
    vrcDischPtPressure.setUnits("decibars")
_VrcDischPtHighTempAlarm_Type = TruthValue
_VrcDischPtHighTempAlarm_Object = MibTableColumn
vrcDischPtHighTempAlarm = _VrcDischPtHighTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 18, 1, 5),
    _VrcDischPtHighTempAlarm_Type()
)
vrcDischPtHighTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcDischPtHighTempAlarm.setStatus("current")
_VrcDischPtHighTempFreqAlarm_Type = TruthValue
_VrcDischPtHighTempFreqAlarm_Object = MibTableColumn
vrcDischPtHighTempFreqAlarm = _VrcDischPtHighTempFreqAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 18, 1, 6),
    _VrcDischPtHighTempFreqAlarm_Type()
)
vrcDischPtHighTempFreqAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcDischPtHighTempFreqAlarm.setStatus("current")
_VrcDischPtTempSensorFailAlarm_Type = TruthValue
_VrcDischPtTempSensorFailAlarm_Object = MibTableColumn
vrcDischPtTempSensorFailAlarm = _VrcDischPtTempSensorFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 18, 1, 7),
    _VrcDischPtTempSensorFailAlarm_Type()
)
vrcDischPtTempSensorFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcDischPtTempSensorFailAlarm.setStatus("current")
_VrcDischCfgTable_Object = MibTable
vrcDischCfgTable = _VrcDischCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 19)
)
if mibBuilder.loadTexts:
    vrcDischCfgTable.setStatus("current")
_VrcDischCfgEntry_Object = MibTableRow
vrcDischCfgEntry = _VrcDischCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 19, 1)
)
vrcDischCfgEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "vrcDischCfgIndex"),
)
if mibBuilder.loadTexts:
    vrcDischCfgEntry.setStatus("current")


class _VrcDischCfgIndex_Type(Integer32):
    """Custom type vrcDischCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrcDischCfgIndex_Type.__name__ = "Integer32"
_VrcDischCfgIndex_Object = MibTableColumn
vrcDischCfgIndex = _VrcDischCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 19, 1, 1),
    _VrcDischCfgIndex_Type()
)
vrcDischCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrcDischCfgIndex.setStatus("current")
_VrcDischCfgTempCalValue_Type = Integer32
_VrcDischCfgTempCalValue_Object = MibTableColumn
vrcDischCfgTempCalValue = _VrcDischCfgTempCalValue_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 19, 1, 2),
    _VrcDischCfgTempCalValue_Type()
)
vrcDischCfgTempCalValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcDischCfgTempCalValue.setStatus("current")
if mibBuilder.loadTexts:
    vrcDischCfgTempCalValue.setUnits("decidegrees")


class _VrcDischCfgPressCalValue_Type(Integer32):
    """Custom type vrcDischCfgPressCalValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_VrcDischCfgPressCalValue_Type.__name__ = "Integer32"
_VrcDischCfgPressCalValue_Object = MibTableColumn
vrcDischCfgPressCalValue = _VrcDischCfgPressCalValue_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 19, 1, 3),
    _VrcDischCfgPressCalValue_Type()
)
vrcDischCfgPressCalValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcDischCfgPressCalValue.setStatus("current")
if mibBuilder.loadTexts:
    vrcDischCfgPressCalValue.setUnits("decibars")


class _VrcDischCfgHighTempAlmCtrl_Type(Integer32):
    """Custom type vrcDischCfgHighTempAlmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("suspend", 2),
          ("open", 3))
    )


_VrcDischCfgHighTempAlmCtrl_Type.__name__ = "Integer32"
_VrcDischCfgHighTempAlmCtrl_Object = MibTableColumn
vrcDischCfgHighTempAlmCtrl = _VrcDischCfgHighTempAlmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 19, 1, 4),
    _VrcDischCfgHighTempAlmCtrl_Type()
)
vrcDischCfgHighTempAlmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcDischCfgHighTempAlmCtrl.setStatus("current")


class _VrcDischCfgHighTempFreqAlmCtrl_Type(Integer32):
    """Custom type vrcDischCfgHighTempFreqAlmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("suspend", 2),
          ("open", 3))
    )


_VrcDischCfgHighTempFreqAlmCtrl_Type.__name__ = "Integer32"
_VrcDischCfgHighTempFreqAlmCtrl_Object = MibTableColumn
vrcDischCfgHighTempFreqAlmCtrl = _VrcDischCfgHighTempFreqAlmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 19, 1, 5),
    _VrcDischCfgHighTempFreqAlmCtrl_Type()
)
vrcDischCfgHighTempFreqAlmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcDischCfgHighTempFreqAlmCtrl.setStatus("current")


class _VrcDischCfgTempSensFailAlmCtrl_Type(Integer32):
    """Custom type vrcDischCfgTempSensFailAlmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("suspend", 2),
          ("open", 3))
    )


_VrcDischCfgTempSensFailAlmCtrl_Type.__name__ = "Integer32"
_VrcDischCfgTempSensFailAlmCtrl_Object = MibTableColumn
vrcDischCfgTempSensFailAlmCtrl = _VrcDischCfgTempSensFailAlmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 19, 1, 6),
    _VrcDischCfgTempSensFailAlmCtrl_Type()
)
vrcDischCfgTempSensFailAlmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcDischCfgTempSensFailAlmCtrl.setStatus("current")
_VrcSuctPtTable_Object = MibTable
vrcSuctPtTable = _VrcSuctPtTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 20)
)
if mibBuilder.loadTexts:
    vrcSuctPtTable.setStatus("current")
_VrcSuctPtEntry_Object = MibTableRow
vrcSuctPtEntry = _VrcSuctPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 20, 1)
)
vrcSuctPtEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "vrcSuctPtIndex"),
)
if mibBuilder.loadTexts:
    vrcSuctPtEntry.setStatus("current")


class _VrcSuctPtIndex_Type(Integer32):
    """Custom type vrcSuctPtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrcSuctPtIndex_Type.__name__ = "Integer32"
_VrcSuctPtIndex_Object = MibTableColumn
vrcSuctPtIndex = _VrcSuctPtIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 20, 1, 1),
    _VrcSuctPtIndex_Type()
)
vrcSuctPtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrcSuctPtIndex.setStatus("current")


class _VrcSuctPtName_Type(SnmpAdminString):
    """Custom type vrcSuctPtName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_VrcSuctPtName_Type.__name__ = "SnmpAdminString"
_VrcSuctPtName_Object = MibTableColumn
vrcSuctPtName = _VrcSuctPtName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 20, 1, 2),
    _VrcSuctPtName_Type()
)
vrcSuctPtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcSuctPtName.setStatus("current")
_VrcSuctPtTemp_Type = Integer32
_VrcSuctPtTemp_Object = MibTableColumn
vrcSuctPtTemp = _VrcSuctPtTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 20, 1, 3),
    _VrcSuctPtTemp_Type()
)
vrcSuctPtTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcSuctPtTemp.setStatus("current")
if mibBuilder.loadTexts:
    vrcSuctPtTemp.setUnits("decidegrees")


class _VrcSuctPtPressure_Type(Integer32):
    """Custom type vrcSuctPtPressure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 173),
    )


_VrcSuctPtPressure_Type.__name__ = "Integer32"
_VrcSuctPtPressure_Object = MibTableColumn
vrcSuctPtPressure = _VrcSuctPtPressure_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 20, 1, 4),
    _VrcSuctPtPressure_Type()
)
vrcSuctPtPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcSuctPtPressure.setStatus("current")
if mibBuilder.loadTexts:
    vrcSuctPtPressure.setUnits("decibars")
_VrcSuctPtSuperHeatTemp_Type = Integer32
_VrcSuctPtSuperHeatTemp_Object = MibTableColumn
vrcSuctPtSuperHeatTemp = _VrcSuctPtSuperHeatTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 20, 1, 5),
    _VrcSuctPtSuperHeatTemp_Type()
)
vrcSuctPtSuperHeatTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcSuctPtSuperHeatTemp.setStatus("current")
if mibBuilder.loadTexts:
    vrcSuctPtSuperHeatTemp.setUnits("decidegrees")
_VrcSuctPtTempSensorFailAlarm_Type = TruthValue
_VrcSuctPtTempSensorFailAlarm_Object = MibTableColumn
vrcSuctPtTempSensorFailAlarm = _VrcSuctPtTempSensorFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 20, 1, 6),
    _VrcSuctPtTempSensorFailAlarm_Type()
)
vrcSuctPtTempSensorFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrcSuctPtTempSensorFailAlarm.setStatus("current")
_VrcSuctCfgTable_Object = MibTable
vrcSuctCfgTable = _VrcSuctCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 21)
)
if mibBuilder.loadTexts:
    vrcSuctCfgTable.setStatus("current")
_VrcSuctCfgEntry_Object = MibTableRow
vrcSuctCfgEntry = _VrcSuctCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 21, 1)
)
vrcSuctCfgEntry.setIndexNames(
    (0, "VERTIV-V5-MIB", "vrcSuctCfgIndex"),
)
if mibBuilder.loadTexts:
    vrcSuctCfgEntry.setStatus("current")


class _VrcSuctCfgIndex_Type(Integer32):
    """Custom type vrcSuctCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrcSuctCfgIndex_Type.__name__ = "Integer32"
_VrcSuctCfgIndex_Object = MibTableColumn
vrcSuctCfgIndex = _VrcSuctCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 21, 1, 1),
    _VrcSuctCfgIndex_Type()
)
vrcSuctCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrcSuctCfgIndex.setStatus("current")


class _VrcSuctCfgPressCalValue_Type(Integer32):
    """Custom type vrcSuctCfgPressCalValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_VrcSuctCfgPressCalValue_Type.__name__ = "Integer32"
_VrcSuctCfgPressCalValue_Object = MibTableColumn
vrcSuctCfgPressCalValue = _VrcSuctCfgPressCalValue_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 21, 1, 2),
    _VrcSuctCfgPressCalValue_Type()
)
vrcSuctCfgPressCalValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcSuctCfgPressCalValue.setStatus("current")
if mibBuilder.loadTexts:
    vrcSuctCfgPressCalValue.setUnits("decibars")


class _VrcSuctCfgTempSensFailAlmCtrl_Type(Integer32):
    """Custom type vrcSuctCfgTempSensFailAlmCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("suspend", 2),
          ("open", 3))
    )


_VrcSuctCfgTempSensFailAlmCtrl_Type.__name__ = "Integer32"
_VrcSuctCfgTempSensFailAlmCtrl_Object = MibTableColumn
vrcSuctCfgTempSensFailAlmCtrl = _VrcSuctCfgTempSensFailAlmCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 30, 1, 21, 1, 3),
    _VrcSuctCfgTempSensFailAlmCtrl_Type()
)
vrcSuctCfgTempSensFailAlmCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrcSuctCfgTempSensFailAlmCtrl.setStatus("current")
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767)
)
_TrapPrefix_ObjectIdentity = ObjectIdentity
trapPrefix = _TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0)
)
_TrapObj_ObjectIdentity = ObjectIdentity
trapObj = _TrapObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 1)
)


class _TrapSeverity_Type(Integer32):
    """Custom type trapSeverity based on Integer32"""
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
          ("warning", 1),
          ("alarm", 2))
    )


_TrapSeverity_Type.__name__ = "Integer32"
_TrapSeverity_Object = MibScalar
trapSeverity = _TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 1, 1),
    _TrapSeverity_Type()
)
trapSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapSeverity.setStatus("current")


class _TrapThreshType_Type(Integer32):
    """Custom type trapThreshType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_TrapThreshType_Type.__name__ = "Integer32"
_TrapThreshType_Object = MibScalar
trapThreshType = _TrapThreshType_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 1, 2),
    _TrapThreshType_Type()
)
trapThreshType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapThreshType.setStatus("current")
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 42)
)
_Identity_ObjectIdentity = ObjectIdentity
identity = _Identity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 42, 1)
)
_R05_ObjectIdentity = ObjectIdentity
r05 = _R05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 42, 1, 15)
)
if mibBuilder.loadTexts:
    r05.setStatus("current")
_I03_ObjectIdentity = ObjectIdentity
i03 = _I03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 42, 1, 53)
)
if mibBuilder.loadTexts:
    i03.setStatus("current")

# Managed Objects groups


# Notification objects

internalTestNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10101)
)
if mibBuilder.loadTexts:
    internalTestNOTIFY.setStatus(
        "current"
    )

pduMainAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10305)
)
pduMainAvailNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduMainAvail"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"))
)
if mibBuilder.loadTexts:
    pduMainAvailNOTIFY.setStatus(
        "current"
    )

pduTotalRealPowerNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10309)
)
pduTotalRealPowerNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduTotalRealPower"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduTotalLabel"))
)
if mibBuilder.loadTexts:
    pduTotalRealPowerNOTIFY.setStatus(
        "current"
    )

pduTotalApparentPowerNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10310)
)
pduTotalApparentPowerNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduTotalApparentPower"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduTotalLabel"))
)
if mibBuilder.loadTexts:
    pduTotalApparentPowerNOTIFY.setStatus(
        "current"
    )

pduTotalPowerFactorNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10311)
)
pduTotalPowerFactorNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduTotalPowerFactor"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduTotalLabel"))
)
if mibBuilder.loadTexts:
    pduTotalPowerFactorNOTIFY.setStatus(
        "current"
    )

pduTotalEnergyNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10312)
)
pduTotalEnergyNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduTotalEnergy"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduTotalLabel"))
)
if mibBuilder.loadTexts:
    pduTotalEnergyNOTIFY.setStatus(
        "current"
    )

pduPhaseVoltageNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10324)
)
pduPhaseVoltageNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduPhaseVoltage"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduPhaseLabel"))
)
if mibBuilder.loadTexts:
    pduPhaseVoltageNOTIFY.setStatus(
        "current"
    )

pduPhaseCurrentNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10328)
)
pduPhaseCurrentNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduPhaseCurrent"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduPhaseLabel"))
)
if mibBuilder.loadTexts:
    pduPhaseCurrentNOTIFY.setStatus(
        "current"
    )

pduPhaseRealPowerNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10332)
)
pduPhaseRealPowerNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduPhaseRealPower"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduPhaseLabel"))
)
if mibBuilder.loadTexts:
    pduPhaseRealPowerNOTIFY.setStatus(
        "current"
    )

pduPhaseApparentPowerNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10333)
)
pduPhaseApparentPowerNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduPhaseApparentPower"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduPhaseLabel"))
)
if mibBuilder.loadTexts:
    pduPhaseApparentPowerNOTIFY.setStatus(
        "current"
    )

pduPhasePowerFactorNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10334)
)
pduPhasePowerFactorNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduPhasePowerFactor"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduPhaseLabel"))
)
if mibBuilder.loadTexts:
    pduPhasePowerFactorNOTIFY.setStatus(
        "current"
    )

pduPhaseEnergyNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10335)
)
pduPhaseEnergyNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduPhaseEnergy"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduPhaseLabel"))
)
if mibBuilder.loadTexts:
    pduPhaseEnergyNOTIFY.setStatus(
        "current"
    )

pduPhaseBalanceNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10337)
)
pduPhaseBalanceNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduPhaseBalance"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduPhaseLabel"))
)
if mibBuilder.loadTexts:
    pduPhaseBalanceNOTIFY.setStatus(
        "current"
    )

pduPhaseCurrentCrestFactorNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10339)
)
pduPhaseCurrentCrestFactorNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduPhaseCurrentCrestFactor"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduPhaseLabel"))
)
if mibBuilder.loadTexts:
    pduPhaseCurrentCrestFactorNOTIFY.setStatus(
        "current"
    )

pduBreakerCurrentNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10354)
)
pduBreakerCurrentNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduBreakerCurrent"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduBreakerLabel"))
)
if mibBuilder.loadTexts:
    pduBreakerCurrentNOTIFY.setStatus(
        "current"
    )

pduBreakerVoltageNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10358)
)
pduBreakerVoltageNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduBreakerVoltage"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduBreakerLabel"))
)
if mibBuilder.loadTexts:
    pduBreakerVoltageNOTIFY.setStatus(
        "current"
    )

pduBreakerRealPowerNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10362)
)
pduBreakerRealPowerNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduBreakerRealPower"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduBreakerLabel"))
)
if mibBuilder.loadTexts:
    pduBreakerRealPowerNOTIFY.setStatus(
        "current"
    )

pduBreakerApparentPowerNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10363)
)
pduBreakerApparentPowerNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduBreakerApparentPower"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduBreakerLabel"))
)
if mibBuilder.loadTexts:
    pduBreakerApparentPowerNOTIFY.setStatus(
        "current"
    )

pduBreakerPowerFactorNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10364)
)
pduBreakerPowerFactorNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduBreakerPowerFactor"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduBreakerLabel"))
)
if mibBuilder.loadTexts:
    pduBreakerPowerFactorNOTIFY.setStatus(
        "current"
    )

pduBreakerEnergyNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10365)
)
pduBreakerEnergyNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduBreakerEnergy"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduBreakerLabel"))
)
if mibBuilder.loadTexts:
    pduBreakerEnergyNOTIFY.setStatus(
        "current"
    )

pduLineCurrentNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10374)
)
pduLineCurrentNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduLineCurrent"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduLineLabel"))
)
if mibBuilder.loadTexts:
    pduLineCurrentNOTIFY.setStatus(
        "current"
    )

pduOutletMeterVoltageNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10385)
)
pduOutletMeterVoltageNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduOutletMeterVoltage"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduOutletMeterLabel"))
)
if mibBuilder.loadTexts:
    pduOutletMeterVoltageNOTIFY.setStatus(
        "current"
    )

pduOutletMeterCurrentNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10389)
)
pduOutletMeterCurrentNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduOutletMeterCurrent"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduOutletMeterLabel"))
)
if mibBuilder.loadTexts:
    pduOutletMeterCurrentNOTIFY.setStatus(
        "current"
    )

pduOutletMeterRealPowerNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10393)
)
pduOutletMeterRealPowerNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduOutletMeterRealPower"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduOutletMeterLabel"))
)
if mibBuilder.loadTexts:
    pduOutletMeterRealPowerNOTIFY.setStatus(
        "current"
    )

pduOutletMeterApparentPowerNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10394)
)
pduOutletMeterApparentPowerNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduOutletMeterApparentPower"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduOutletMeterLabel"))
)
if mibBuilder.loadTexts:
    pduOutletMeterApparentPowerNOTIFY.setStatus(
        "current"
    )

pduOutletMeterPowerFactorNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10395)
)
pduOutletMeterPowerFactorNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduOutletMeterPowerFactor"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduOutletMeterLabel"))
)
if mibBuilder.loadTexts:
    pduOutletMeterPowerFactorNOTIFY.setStatus(
        "current"
    )

pduOutletMeterEnergyNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10396)
)
pduOutletMeterEnergyNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduOutletMeterEnergy"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduOutletMeterLabel"))
)
if mibBuilder.loadTexts:
    pduOutletMeterEnergyNOTIFY.setStatus(
        "current"
    )

pduOutletCurrentCrestFactorNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10400)
)
pduOutletCurrentCrestFactorNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "pduOutletCurrentCrestFactor"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduOutletMeterLabel"))
)
if mibBuilder.loadTexts:
    pduOutletCurrentCrestFactorNOTIFY.setStatus(
        "current"
    )

tempSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10404)
)
tempSensorAvailNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "tempSensorAvail"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "tempSensorLabel"))
)
if mibBuilder.loadTexts:
    tempSensorAvailNOTIFY.setStatus(
        "current"
    )

tempSensorTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10405)
)
tempSensorTempNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "tempSensorTemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "tempSensorLabel"))
)
if mibBuilder.loadTexts:
    tempSensorTempNOTIFY.setStatus(
        "current"
    )

airFlowSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10504)
)
airFlowSensorAvailNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "airFlowSensorAvail"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "airFlowSensorLabel"))
)
if mibBuilder.loadTexts:
    airFlowSensorAvailNOTIFY.setStatus(
        "current"
    )

airFlowSensorTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10505)
)
airFlowSensorTempNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "airFlowSensorTemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "airFlowSensorLabel"))
)
if mibBuilder.loadTexts:
    airFlowSensorTempNOTIFY.setStatus(
        "current"
    )

airFlowSensorFlowNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10506)
)
airFlowSensorFlowNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "airFlowSensorFlow"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "airFlowSensorLabel"))
)
if mibBuilder.loadTexts:
    airFlowSensorFlowNOTIFY.setStatus(
        "current"
    )

airFlowSensorHumidityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10507)
)
airFlowSensorHumidityNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "airFlowSensorHumidity"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "airFlowSensorLabel"))
)
if mibBuilder.loadTexts:
    airFlowSensorHumidityNOTIFY.setStatus(
        "current"
    )

airFlowSensorDewPointNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10508)
)
airFlowSensorDewPointNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "airFlowSensorDewPoint"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "airFlowSensorLabel"))
)
if mibBuilder.loadTexts:
    airFlowSensorDewPointNOTIFY.setStatus(
        "current"
    )

t3hdSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10804)
)
t3hdSensorAvailNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "t3hdSensorAvail"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "t3hdSensorLabel"))
)
if mibBuilder.loadTexts:
    t3hdSensorAvailNOTIFY.setStatus(
        "current"
    )

t3hdSensorIntTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10806)
)
t3hdSensorIntTempNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "t3hdSensorIntTemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "t3hdSensorLabel"),
        ("VERTIV-V5-MIB", "t3hdSensorIntLabel"))
)
if mibBuilder.loadTexts:
    t3hdSensorIntTempNOTIFY.setStatus(
        "current"
    )

t3hdSensorIntHumidityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10807)
)
t3hdSensorIntHumidityNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "t3hdSensorIntHumidity"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "t3hdSensorLabel"),
        ("VERTIV-V5-MIB", "t3hdSensorIntLabel"))
)
if mibBuilder.loadTexts:
    t3hdSensorIntHumidityNOTIFY.setStatus(
        "current"
    )

t3hdSensorIntDewPointNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10808)
)
t3hdSensorIntDewPointNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "t3hdSensorIntDewPoint"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "t3hdSensorLabel"),
        ("VERTIV-V5-MIB", "t3hdSensorIntLabel"))
)
if mibBuilder.loadTexts:
    t3hdSensorIntDewPointNOTIFY.setStatus(
        "current"
    )

t3hdSensorExtATempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10811)
)
t3hdSensorExtATempNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "t3hdSensorExtATemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "t3hdSensorLabel"),
        ("VERTIV-V5-MIB", "t3hdSensorExtALabel"))
)
if mibBuilder.loadTexts:
    t3hdSensorExtATempNOTIFY.setStatus(
        "current"
    )

t3hdSensorExtBTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10814)
)
t3hdSensorExtBTempNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "t3hdSensorExtBTemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "t3hdSensorLabel"),
        ("VERTIV-V5-MIB", "t3hdSensorExtBLabel"))
)
if mibBuilder.loadTexts:
    t3hdSensorExtBTempNOTIFY.setStatus(
        "current"
    )

thdSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10904)
)
thdSensorAvailNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "thdSensorAvail"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "thdSensorLabel"))
)
if mibBuilder.loadTexts:
    thdSensorAvailNOTIFY.setStatus(
        "current"
    )

thdSensorTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10905)
)
thdSensorTempNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "thdSensorTemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "thdSensorLabel"))
)
if mibBuilder.loadTexts:
    thdSensorTempNOTIFY.setStatus(
        "current"
    )

thdSensorHumidityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10906)
)
thdSensorHumidityNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "thdSensorHumidity"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "thdSensorLabel"))
)
if mibBuilder.loadTexts:
    thdSensorHumidityNOTIFY.setStatus(
        "current"
    )

thdSensorDewPointNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10907)
)
thdSensorDewPointNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "thdSensorDewPoint"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "thdSensorLabel"))
)
if mibBuilder.loadTexts:
    thdSensorDewPointNOTIFY.setStatus(
        "current"
    )

a2dSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 11104)
)
a2dSensorAvailNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "a2dSensorAvail"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "a2dSensorLabel"))
)
if mibBuilder.loadTexts:
    a2dSensorAvailNOTIFY.setStatus(
        "current"
    )

a2dSensorValueNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 11105)
)
a2dSensorValueNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "a2dSensorValue"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "a2dSensorLabel"),
        ("VERTIV-V5-MIB", "a2dSensorAnalogLabel"),
        ("VERTIV-V5-MIB", "a2dSensorDisplayValue"))
)
if mibBuilder.loadTexts:
    a2dSensorValueNOTIFY.setStatus(
        "current"
    )

humiditySensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 11204)
)
humiditySensorAvailNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "humiditySensorAvail"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "humiditySensorLabel"))
)
if mibBuilder.loadTexts:
    humiditySensorAvailNOTIFY.setStatus(
        "current"
    )

humiditySensorValueNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 11205)
)
humiditySensorValueNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "humiditySensorValue"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "humiditySensorLabel"))
)
if mibBuilder.loadTexts:
    humiditySensorValueNOTIFY.setStatus(
        "current"
    )

sn2dSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 11304)
)
sn2dSensorAvailNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "sn2dSensorAvail"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "sn2dSensorLabel"))
)
if mibBuilder.loadTexts:
    sn2dSensorAvailNOTIFY.setStatus(
        "current"
    )

sn2dSensorDoor1StateNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 11306)
)
sn2dSensorDoor1StateNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "sn2dSensorDoor1State"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "sn2dSensorLabel"),
        ("VERTIV-V5-MIB", "sn2dSensorDoor1Label"),
        ("VERTIV-V5-MIB", "sn2dSensorDoor1DisplayState"))
)
if mibBuilder.loadTexts:
    sn2dSensorDoor1StateNOTIFY.setStatus(
        "current"
    )

sn2dSensorDoor2StateNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 11309)
)
sn2dSensorDoor2StateNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "sn2dSensorDoor2State"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "sn2dSensorLabel"),
        ("VERTIV-V5-MIB", "sn2dSensorDoor2Label"),
        ("VERTIV-V5-MIB", "sn2dSensorDoor2DisplayState"))
)
if mibBuilder.loadTexts:
    sn2dSensorDoor2StateNOTIFY.setStatus(
        "current"
    )

vrcMainAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 13001)
)
vrcMainAvailNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "vrcMainAvail"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcMainAvailNOTIFY.setStatus(
        "current"
    )

vrcOutFanPtSpeedNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 13002)
)
vrcOutFanPtSpeedNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "vrcOutFanPtSpeed"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcOutFanPtSpeedNOTIFY.setStatus(
        "current"
    )

vrcCompPtCapacityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 13003)
)
vrcCompPtCapacityNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "vrcCompPtCapacity"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcCompPtCapacityNOTIFY.setStatus(
        "current"
    )

vrcReturnPtTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 13004)
)
vrcReturnPtTempNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "vrcReturnPtTemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcReturnPtTempNOTIFY.setStatus(
        "current"
    )

vrcSupplyPtTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 13005)
)
vrcSupplyPtTempNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "vrcSupplyPtTemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcSupplyPtTempNOTIFY.setStatus(
        "current"
    )

vrcPowerPtVoltageNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 13006)
)
vrcPowerPtVoltageNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "vrcPowerPtVoltage"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcPowerPtVoltageNOTIFY.setStatus(
        "current"
    )

vrcPowerPtFrequencyNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 13007)
)
vrcPowerPtFrequencyNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "vrcPowerPtFrequency"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcPowerPtFrequencyNOTIFY.setStatus(
        "current"
    )

vrcOutdoorPtTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 13008)
)
vrcOutdoorPtTempNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "vrcOutdoorPtTemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcOutdoorPtTempNOTIFY.setStatus(
        "current"
    )

vrcDischPtTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 13009)
)
vrcDischPtTempNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "vrcDischPtTemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcDischPtTempNOTIFY.setStatus(
        "current"
    )

vrcDischPtPressureNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 13010)
)
vrcDischPtPressureNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "vrcDischPtPressure"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcDischPtPressureNOTIFY.setStatus(
        "current"
    )

vrcSuctPtTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 13011)
)
vrcSuctPtTempNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "vrcSuctPtTemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcSuctPtTempNOTIFY.setStatus(
        "current"
    )

vrcSuctPtPressureNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 13012)
)
vrcSuctPtPressureNOTIFY.setObjects(
      *(("VERTIV-V5-MIB", "vrcSuctPtPressure"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcSuctPtPressureNOTIFY.setStatus(
        "current"
    )

pduMainAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20305)
)
pduMainAvailCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduMainAvail"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"))
)
if mibBuilder.loadTexts:
    pduMainAvailCLEAR.setStatus(
        "current"
    )

pduTotalRealPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20309)
)
pduTotalRealPowerCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduTotalRealPower"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduTotalLabel"))
)
if mibBuilder.loadTexts:
    pduTotalRealPowerCLEAR.setStatus(
        "current"
    )

pduTotalApparentPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20310)
)
pduTotalApparentPowerCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduTotalApparentPower"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduTotalLabel"))
)
if mibBuilder.loadTexts:
    pduTotalApparentPowerCLEAR.setStatus(
        "current"
    )

pduTotalPowerFactorCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20311)
)
pduTotalPowerFactorCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduTotalPowerFactor"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduTotalLabel"))
)
if mibBuilder.loadTexts:
    pduTotalPowerFactorCLEAR.setStatus(
        "current"
    )

pduTotalEnergyCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20312)
)
pduTotalEnergyCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduTotalEnergy"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduTotalLabel"))
)
if mibBuilder.loadTexts:
    pduTotalEnergyCLEAR.setStatus(
        "current"
    )

pduPhaseVoltageCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20324)
)
pduPhaseVoltageCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduPhaseVoltage"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduPhaseLabel"))
)
if mibBuilder.loadTexts:
    pduPhaseVoltageCLEAR.setStatus(
        "current"
    )

pduPhaseCurrentCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20328)
)
pduPhaseCurrentCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduPhaseCurrent"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduPhaseLabel"))
)
if mibBuilder.loadTexts:
    pduPhaseCurrentCLEAR.setStatus(
        "current"
    )

pduPhaseRealPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20332)
)
pduPhaseRealPowerCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduPhaseRealPower"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduPhaseLabel"))
)
if mibBuilder.loadTexts:
    pduPhaseRealPowerCLEAR.setStatus(
        "current"
    )

pduPhaseApparentPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20333)
)
pduPhaseApparentPowerCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduPhaseApparentPower"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduPhaseLabel"))
)
if mibBuilder.loadTexts:
    pduPhaseApparentPowerCLEAR.setStatus(
        "current"
    )

pduPhasePowerFactorCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20334)
)
pduPhasePowerFactorCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduPhasePowerFactor"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduPhaseLabel"))
)
if mibBuilder.loadTexts:
    pduPhasePowerFactorCLEAR.setStatus(
        "current"
    )

pduPhaseEnergyCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20335)
)
pduPhaseEnergyCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduPhaseEnergy"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduPhaseLabel"))
)
if mibBuilder.loadTexts:
    pduPhaseEnergyCLEAR.setStatus(
        "current"
    )

pduPhaseBalanceCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20337)
)
pduPhaseBalanceCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduPhaseBalance"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduPhaseLabel"))
)
if mibBuilder.loadTexts:
    pduPhaseBalanceCLEAR.setStatus(
        "current"
    )

pduPhaseCurrentCrestFactorCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20339)
)
pduPhaseCurrentCrestFactorCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduPhaseCurrentCrestFactor"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduPhaseLabel"))
)
if mibBuilder.loadTexts:
    pduPhaseCurrentCrestFactorCLEAR.setStatus(
        "current"
    )

pduBreakerCurrentCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20354)
)
pduBreakerCurrentCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduBreakerCurrent"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduBreakerLabel"))
)
if mibBuilder.loadTexts:
    pduBreakerCurrentCLEAR.setStatus(
        "current"
    )

pduBreakerVoltageCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20358)
)
pduBreakerVoltageCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduBreakerVoltage"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduBreakerLabel"))
)
if mibBuilder.loadTexts:
    pduBreakerVoltageCLEAR.setStatus(
        "current"
    )

pduBreakerRealPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20362)
)
pduBreakerRealPowerCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduBreakerRealPower"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduBreakerLabel"))
)
if mibBuilder.loadTexts:
    pduBreakerRealPowerCLEAR.setStatus(
        "current"
    )

pduBreakerApparentPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20363)
)
pduBreakerApparentPowerCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduBreakerApparentPower"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduBreakerLabel"))
)
if mibBuilder.loadTexts:
    pduBreakerApparentPowerCLEAR.setStatus(
        "current"
    )

pduBreakerPowerFactorCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20364)
)
pduBreakerPowerFactorCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduBreakerPowerFactor"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduBreakerLabel"))
)
if mibBuilder.loadTexts:
    pduBreakerPowerFactorCLEAR.setStatus(
        "current"
    )

pduBreakerEnergyCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20365)
)
pduBreakerEnergyCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduBreakerEnergy"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduBreakerLabel"))
)
if mibBuilder.loadTexts:
    pduBreakerEnergyCLEAR.setStatus(
        "current"
    )

pduLineCurrentCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20374)
)
pduLineCurrentCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduLineCurrent"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduLineLabel"))
)
if mibBuilder.loadTexts:
    pduLineCurrentCLEAR.setStatus(
        "current"
    )

pduOutletMeterVoltageCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20385)
)
pduOutletMeterVoltageCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduOutletMeterVoltage"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduOutletMeterLabel"))
)
if mibBuilder.loadTexts:
    pduOutletMeterVoltageCLEAR.setStatus(
        "current"
    )

pduOutletMeterCurrentCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20389)
)
pduOutletMeterCurrentCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduOutletMeterCurrent"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduOutletMeterLabel"))
)
if mibBuilder.loadTexts:
    pduOutletMeterCurrentCLEAR.setStatus(
        "current"
    )

pduOutletMeterRealPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20393)
)
pduOutletMeterRealPowerCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduOutletMeterRealPower"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduOutletMeterLabel"))
)
if mibBuilder.loadTexts:
    pduOutletMeterRealPowerCLEAR.setStatus(
        "current"
    )

pduOutletMeterApparentPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20394)
)
pduOutletMeterApparentPowerCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduOutletMeterApparentPower"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduOutletMeterLabel"))
)
if mibBuilder.loadTexts:
    pduOutletMeterApparentPowerCLEAR.setStatus(
        "current"
    )

pduOutletMeterPowerFactorCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20395)
)
pduOutletMeterPowerFactorCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduOutletMeterPowerFactor"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduOutletMeterLabel"))
)
if mibBuilder.loadTexts:
    pduOutletMeterPowerFactorCLEAR.setStatus(
        "current"
    )

pduOutletMeterEnergyCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20396)
)
pduOutletMeterEnergyCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduOutletMeterEnergy"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduOutletMeterLabel"))
)
if mibBuilder.loadTexts:
    pduOutletMeterEnergyCLEAR.setStatus(
        "current"
    )

pduOutletCurrentCrestFactorCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20400)
)
pduOutletCurrentCrestFactorCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "pduOutletCurrentCrestFactor"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "pduMainLabel"),
        ("VERTIV-V5-MIB", "pduOutletMeterLabel"))
)
if mibBuilder.loadTexts:
    pduOutletCurrentCrestFactorCLEAR.setStatus(
        "current"
    )

tempSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20404)
)
tempSensorAvailCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "tempSensorAvail"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "tempSensorLabel"))
)
if mibBuilder.loadTexts:
    tempSensorAvailCLEAR.setStatus(
        "current"
    )

tempSensorTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20405)
)
tempSensorTempCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "tempSensorTemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "tempSensorLabel"))
)
if mibBuilder.loadTexts:
    tempSensorTempCLEAR.setStatus(
        "current"
    )

airFlowSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20504)
)
airFlowSensorAvailCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "airFlowSensorAvail"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "airFlowSensorLabel"))
)
if mibBuilder.loadTexts:
    airFlowSensorAvailCLEAR.setStatus(
        "current"
    )

airFlowSensorTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20505)
)
airFlowSensorTempCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "airFlowSensorTemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "airFlowSensorLabel"))
)
if mibBuilder.loadTexts:
    airFlowSensorTempCLEAR.setStatus(
        "current"
    )

airFlowSensorFlowCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20506)
)
airFlowSensorFlowCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "airFlowSensorFlow"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "airFlowSensorLabel"))
)
if mibBuilder.loadTexts:
    airFlowSensorFlowCLEAR.setStatus(
        "current"
    )

airFlowSensorHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20507)
)
airFlowSensorHumidityCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "airFlowSensorHumidity"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "airFlowSensorLabel"))
)
if mibBuilder.loadTexts:
    airFlowSensorHumidityCLEAR.setStatus(
        "current"
    )

airFlowSensorDewPointCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20508)
)
airFlowSensorDewPointCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "airFlowSensorDewPoint"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "airFlowSensorLabel"))
)
if mibBuilder.loadTexts:
    airFlowSensorDewPointCLEAR.setStatus(
        "current"
    )

t3hdSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20804)
)
t3hdSensorAvailCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "t3hdSensorAvail"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "t3hdSensorLabel"))
)
if mibBuilder.loadTexts:
    t3hdSensorAvailCLEAR.setStatus(
        "current"
    )

t3hdSensorIntTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20806)
)
t3hdSensorIntTempCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "t3hdSensorIntTemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "t3hdSensorLabel"),
        ("VERTIV-V5-MIB", "t3hdSensorIntLabel"))
)
if mibBuilder.loadTexts:
    t3hdSensorIntTempCLEAR.setStatus(
        "current"
    )

t3hdSensorIntHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20807)
)
t3hdSensorIntHumidityCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "t3hdSensorIntHumidity"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "t3hdSensorLabel"),
        ("VERTIV-V5-MIB", "t3hdSensorIntLabel"))
)
if mibBuilder.loadTexts:
    t3hdSensorIntHumidityCLEAR.setStatus(
        "current"
    )

t3hdSensorIntDewPointCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20808)
)
t3hdSensorIntDewPointCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "t3hdSensorIntDewPoint"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "t3hdSensorLabel"),
        ("VERTIV-V5-MIB", "t3hdSensorIntLabel"))
)
if mibBuilder.loadTexts:
    t3hdSensorIntDewPointCLEAR.setStatus(
        "current"
    )

t3hdSensorExtATempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20811)
)
t3hdSensorExtATempCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "t3hdSensorExtATemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "t3hdSensorLabel"),
        ("VERTIV-V5-MIB", "t3hdSensorExtALabel"))
)
if mibBuilder.loadTexts:
    t3hdSensorExtATempCLEAR.setStatus(
        "current"
    )

t3hdSensorExtBTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20814)
)
t3hdSensorExtBTempCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "t3hdSensorExtBTemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "t3hdSensorLabel"),
        ("VERTIV-V5-MIB", "t3hdSensorExtBLabel"))
)
if mibBuilder.loadTexts:
    t3hdSensorExtBTempCLEAR.setStatus(
        "current"
    )

thdSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20904)
)
thdSensorAvailCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "thdSensorAvail"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "thdSensorLabel"))
)
if mibBuilder.loadTexts:
    thdSensorAvailCLEAR.setStatus(
        "current"
    )

thdSensorTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20905)
)
thdSensorTempCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "thdSensorTemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "thdSensorLabel"))
)
if mibBuilder.loadTexts:
    thdSensorTempCLEAR.setStatus(
        "current"
    )

thdSensorHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20906)
)
thdSensorHumidityCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "thdSensorHumidity"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "thdSensorLabel"))
)
if mibBuilder.loadTexts:
    thdSensorHumidityCLEAR.setStatus(
        "current"
    )

thdSensorDewPointCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20907)
)
thdSensorDewPointCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "thdSensorDewPoint"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "thdSensorLabel"))
)
if mibBuilder.loadTexts:
    thdSensorDewPointCLEAR.setStatus(
        "current"
    )

a2dSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 21104)
)
a2dSensorAvailCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "a2dSensorAvail"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "a2dSensorLabel"))
)
if mibBuilder.loadTexts:
    a2dSensorAvailCLEAR.setStatus(
        "current"
    )

a2dSensorValueCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 21105)
)
a2dSensorValueCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "a2dSensorValue"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "a2dSensorLabel"),
        ("VERTIV-V5-MIB", "a2dSensorAnalogLabel"),
        ("VERTIV-V5-MIB", "a2dSensorDisplayValue"))
)
if mibBuilder.loadTexts:
    a2dSensorValueCLEAR.setStatus(
        "current"
    )

humiditySensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 21204)
)
humiditySensorAvailCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "humiditySensorAvail"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "humiditySensorLabel"))
)
if mibBuilder.loadTexts:
    humiditySensorAvailCLEAR.setStatus(
        "current"
    )

humiditySensorValueCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 21205)
)
humiditySensorValueCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "humiditySensorValue"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "humiditySensorLabel"))
)
if mibBuilder.loadTexts:
    humiditySensorValueCLEAR.setStatus(
        "current"
    )

sn2dSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 21304)
)
sn2dSensorAvailCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "sn2dSensorAvail"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "sn2dSensorLabel"))
)
if mibBuilder.loadTexts:
    sn2dSensorAvailCLEAR.setStatus(
        "current"
    )

sn2dSensorDoor1StateCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 21306)
)
sn2dSensorDoor1StateCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "sn2dSensorDoor1State"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "sn2dSensorLabel"),
        ("VERTIV-V5-MIB", "sn2dSensorDoor1Label"),
        ("VERTIV-V5-MIB", "sn2dSensorDoor1DisplayState"))
)
if mibBuilder.loadTexts:
    sn2dSensorDoor1StateCLEAR.setStatus(
        "current"
    )

sn2dSensorDoor2StateCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 21309)
)
sn2dSensorDoor2StateCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "sn2dSensorDoor2State"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "sn2dSensorLabel"),
        ("VERTIV-V5-MIB", "sn2dSensorDoor2Label"),
        ("VERTIV-V5-MIB", "sn2dSensorDoor2DisplayState"))
)
if mibBuilder.loadTexts:
    sn2dSensorDoor2StateCLEAR.setStatus(
        "current"
    )

vrcMainAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 23001)
)
vrcMainAvailCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "vrcMainAvail"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcMainAvailCLEAR.setStatus(
        "current"
    )

vrcOutFanPtSpeedCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 23002)
)
vrcOutFanPtSpeedCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "vrcOutFanPtSpeed"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcOutFanPtSpeedCLEAR.setStatus(
        "current"
    )

vrcCompPtCapacityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 23003)
)
vrcCompPtCapacityCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "vrcCompPtCapacity"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcCompPtCapacityCLEAR.setStatus(
        "current"
    )

vrcReturnPtTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 23004)
)
vrcReturnPtTempCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "vrcReturnPtTemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcReturnPtTempCLEAR.setStatus(
        "current"
    )

vrcSupplyPtTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 23005)
)
vrcSupplyPtTempCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "vrcSupplyPtTemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcSupplyPtTempCLEAR.setStatus(
        "current"
    )

vrcPowerPtVoltageCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 23006)
)
vrcPowerPtVoltageCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "vrcPowerPtVoltage"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcPowerPtVoltageCLEAR.setStatus(
        "current"
    )

vrcPowerPtFrequencyCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 23007)
)
vrcPowerPtFrequencyCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "vrcPowerPtFrequency"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcPowerPtFrequencyCLEAR.setStatus(
        "current"
    )

vrcOutdoorPtTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 23008)
)
vrcOutdoorPtTempCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "vrcOutdoorPtTemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcOutdoorPtTempCLEAR.setStatus(
        "current"
    )

vrcDischPtTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 23009)
)
vrcDischPtTempCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "vrcDischPtTemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcDischPtTempCLEAR.setStatus(
        "current"
    )

vrcDischPtPressureCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 23010)
)
vrcDischPtPressureCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "vrcDischPtPressure"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcDischPtPressureCLEAR.setStatus(
        "current"
    )

vrcSuctPtTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 23011)
)
vrcSuctPtTempCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "vrcSuctPtTemp"),
        ("VERTIV-V5-MIB", "temperatureUnits"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcSuctPtTempCLEAR.setStatus(
        "current"
    )

vrcSuctPtPressureCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 23012)
)
vrcSuctPtPressureCLEAR.setObjects(
      *(("VERTIV-V5-MIB", "vrcSuctPtPressure"),
        ("VERTIV-V5-MIB", "trapThreshType"),
        ("VERTIV-V5-MIB", "trapSeverity"),
        ("SNMPv2-MIB", "sysName"),
        ("VERTIV-V5-MIB", "vrcMainLabel"))
)
if mibBuilder.loadTexts:
    vrcSuctPtPressureCLEAR.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERTIV-V5-MIB",
    **{"vertiv": vertiv,
       "v5": v5,
       "imd": imd,
       "deviceInfo": deviceInfo,
       "productTitle": productTitle,
       "productVersion": productVersion,
       "productFriendlyName": productFriendlyName,
       "productMacAddress": productMacAddress,
       "deviceCount": deviceCount,
       "temperatureUnits": temperatureUnits,
       "productModelNumber": productModelNumber,
       "productPartNumber": productPartNumber,
       "productSerialNumber": productSerialNumber,
       "productPlatform": productPlatform,
       "productHostname": productHostname,
       "productAlarmCount": productAlarmCount,
       "productWarnCount": productWarnCount,
       "productManufacturer": productManufacturer,
       "pdu": pdu,
       "pduMainTable": pduMainTable,
       "pduMainEntry": pduMainEntry,
       "pduMainIndex": pduMainIndex,
       "pduMainSerial": pduMainSerial,
       "pduMainName": pduMainName,
       "pduMainLabel": pduMainLabel,
       "pduMainAvail": pduMainAvail,
       "pduMeterType": pduMeterType,
       "pduTotalName": pduTotalName,
       "pduTotalLabel": pduTotalLabel,
       "pduTotalRealPower": pduTotalRealPower,
       "pduTotalApparentPower": pduTotalApparentPower,
       "pduTotalPowerFactor": pduTotalPowerFactor,
       "pduTotalEnergy": pduTotalEnergy,
       "pduPhaseTable": pduPhaseTable,
       "pduPhaseEntry": pduPhaseEntry,
       "pduPhaseIndex": pduPhaseIndex,
       "pduPhaseName": pduPhaseName,
       "pduPhaseLabel": pduPhaseLabel,
       "pduPhaseVoltage": pduPhaseVoltage,
       "pduPhaseCurrent": pduPhaseCurrent,
       "pduPhaseRealPower": pduPhaseRealPower,
       "pduPhaseApparentPower": pduPhaseApparentPower,
       "pduPhasePowerFactor": pduPhasePowerFactor,
       "pduPhaseEnergy": pduPhaseEnergy,
       "pduPhaseBalance": pduPhaseBalance,
       "pduPhaseCurrentCrestFactor": pduPhaseCurrentCrestFactor,
       "pduBreakerTable": pduBreakerTable,
       "pduBreakerEntry": pduBreakerEntry,
       "pduBreakerIndex": pduBreakerIndex,
       "pduBreakerName": pduBreakerName,
       "pduBreakerLabel": pduBreakerLabel,
       "pduBreakerCurrent": pduBreakerCurrent,
       "pduBreakerVoltage": pduBreakerVoltage,
       "pduBreakerRealPower": pduBreakerRealPower,
       "pduBreakerApparentPower": pduBreakerApparentPower,
       "pduBreakerPowerFactor": pduBreakerPowerFactor,
       "pduBreakerEnergy": pduBreakerEnergy,
       "pduLineTable": pduLineTable,
       "pduLineEntry": pduLineEntry,
       "pduLineIndex": pduLineIndex,
       "pduLineName": pduLineName,
       "pduLineLabel": pduLineLabel,
       "pduLineCurrent": pduLineCurrent,
       "pduOutletSwitchTable": pduOutletSwitchTable,
       "pduOutletSwitchEntry": pduOutletSwitchEntry,
       "pduOutletSwitchIndex": pduOutletSwitchIndex,
       "pduOutletSwitchName": pduOutletSwitchName,
       "pduOutletSwitchLabel": pduOutletSwitchLabel,
       "pduOutletSwitchState": pduOutletSwitchState,
       "pduOutletSwitchRelayFailure": pduOutletSwitchRelayFailure,
       "pduOutletSwitchControl": pduOutletSwitchControl,
       "pduOutletSwitchTimeToAction": pduOutletSwitchTimeToAction,
       "pduOutletSwitchOnDelay": pduOutletSwitchOnDelay,
       "pduOutletSwitchOffDelay": pduOutletSwitchOffDelay,
       "pduOutletSwitchRebootDelay": pduOutletSwitchRebootDelay,
       "pduOutletSwitchRebootHoldDelay": pduOutletSwitchRebootHoldDelay,
       "pduOutletSwitchPoaAction": pduOutletSwitchPoaAction,
       "pduOutletSwitchPoaDelay": pduOutletSwitchPoaDelay,
       "pduOutletMeterTable": pduOutletMeterTable,
       "pduOutletMeterEntry": pduOutletMeterEntry,
       "pduOutletMeterIndex": pduOutletMeterIndex,
       "pduOutletMeterName": pduOutletMeterName,
       "pduOutletMeterLabel": pduOutletMeterLabel,
       "pduOutletMeterVoltage": pduOutletMeterVoltage,
       "pduOutletMeterCurrent": pduOutletMeterCurrent,
       "pduOutletMeterRealPower": pduOutletMeterRealPower,
       "pduOutletMeterApparentPower": pduOutletMeterApparentPower,
       "pduOutletMeterPowerFactor": pduOutletMeterPowerFactor,
       "pduOutletMeterEnergy": pduOutletMeterEnergy,
       "pduOutletMeterReset": pduOutletMeterReset,
       "pduOutletCurrentCrestFactor": pduOutletCurrentCrestFactor,
       "tempSensorTable": tempSensorTable,
       "tempSensorEntry": tempSensorEntry,
       "tempSensorIndex": tempSensorIndex,
       "tempSensorSerial": tempSensorSerial,
       "tempSensorLabel": tempSensorLabel,
       "tempSensorAvail": tempSensorAvail,
       "tempSensorTemp": tempSensorTemp,
       "airFlowSensorTable": airFlowSensorTable,
       "airFlowSensorEntry": airFlowSensorEntry,
       "airFlowSensorIndex": airFlowSensorIndex,
       "airFlowSensorSerial": airFlowSensorSerial,
       "airFlowSensorLabel": airFlowSensorLabel,
       "airFlowSensorAvail": airFlowSensorAvail,
       "airFlowSensorTemp": airFlowSensorTemp,
       "airFlowSensorFlow": airFlowSensorFlow,
       "airFlowSensorHumidity": airFlowSensorHumidity,
       "airFlowSensorDewPoint": airFlowSensorDewPoint,
       "t3hdSensorTable": t3hdSensorTable,
       "t3hdSensorEntry": t3hdSensorEntry,
       "t3hdSensorIndex": t3hdSensorIndex,
       "t3hdSensorSerial": t3hdSensorSerial,
       "t3hdSensorLabel": t3hdSensorLabel,
       "t3hdSensorAvail": t3hdSensorAvail,
       "t3hdSensorIntLabel": t3hdSensorIntLabel,
       "t3hdSensorIntTemp": t3hdSensorIntTemp,
       "t3hdSensorIntHumidity": t3hdSensorIntHumidity,
       "t3hdSensorIntDewPoint": t3hdSensorIntDewPoint,
       "t3hdSensorExtAAvail": t3hdSensorExtAAvail,
       "t3hdSensorExtALabel": t3hdSensorExtALabel,
       "t3hdSensorExtATemp": t3hdSensorExtATemp,
       "t3hdSensorExtBAvail": t3hdSensorExtBAvail,
       "t3hdSensorExtBLabel": t3hdSensorExtBLabel,
       "t3hdSensorExtBTemp": t3hdSensorExtBTemp,
       "thdSensorTable": thdSensorTable,
       "thdSensorEntry": thdSensorEntry,
       "thdSensorIndex": thdSensorIndex,
       "thdSensorSerial": thdSensorSerial,
       "thdSensorLabel": thdSensorLabel,
       "thdSensorAvail": thdSensorAvail,
       "thdSensorTemp": thdSensorTemp,
       "thdSensorHumidity": thdSensorHumidity,
       "thdSensorDewPoint": thdSensorDewPoint,
       "a2dSensorTable": a2dSensorTable,
       "a2dSensorEntry": a2dSensorEntry,
       "a2dSensorIndex": a2dSensorIndex,
       "a2dSensorSerial": a2dSensorSerial,
       "a2dSensorLabel": a2dSensorLabel,
       "a2dSensorAvail": a2dSensorAvail,
       "a2dSensorValue": a2dSensorValue,
       "a2dSensorDisplayValue": a2dSensorDisplayValue,
       "a2dSensorMode": a2dSensorMode,
       "a2dSensorUnits": a2dSensorUnits,
       "a2dSensorMin": a2dSensorMin,
       "a2dSensorMax": a2dSensorMax,
       "a2dSensorLowLabel": a2dSensorLowLabel,
       "a2dSensorHighLabel": a2dSensorHighLabel,
       "a2dSensorAnalogLabel": a2dSensorAnalogLabel,
       "humiditySensorTable": humiditySensorTable,
       "humiditySensorEntry": humiditySensorEntry,
       "humiditySensorIndex": humiditySensorIndex,
       "humiditySensorSerial": humiditySensorSerial,
       "humiditySensorLabel": humiditySensorLabel,
       "humiditySensorAvail": humiditySensorAvail,
       "humiditySensorValue": humiditySensorValue,
       "sn2dSensorTable": sn2dSensorTable,
       "sn2dSensorEntry": sn2dSensorEntry,
       "sn2dSensorIndex": sn2dSensorIndex,
       "sn2dSensorSerial": sn2dSensorSerial,
       "sn2dSensorLabel": sn2dSensorLabel,
       "sn2dSensorAvail": sn2dSensorAvail,
       "sn2dSensorDoor1Label": sn2dSensorDoor1Label,
       "sn2dSensorDoor1State": sn2dSensorDoor1State,
       "sn2dSensorDoor1DisplayState": sn2dSensorDoor1DisplayState,
       "sn2dSensorDoor2Label": sn2dSensorDoor2Label,
       "sn2dSensorDoor2State": sn2dSensorDoor2State,
       "sn2dSensorDoor2DisplayState": sn2dSensorDoor2DisplayState,
       "cooling": cooling,
       "vrc": vrc,
       "vrcMainTable": vrcMainTable,
       "vrcMainEntry": vrcMainEntry,
       "vrcMainIndex": vrcMainIndex,
       "vrcMainSerial": vrcMainSerial,
       "vrcMainName": vrcMainName,
       "vrcMainLabel": vrcMainLabel,
       "vrcMainAvail": vrcMainAvail,
       "vrcMainPtTable": vrcMainPtTable,
       "vrcMainPtEntry": vrcMainPtEntry,
       "vrcMainPtIndex": vrcMainPtIndex,
       "vrcMainPtRunState": vrcMainPtRunState,
       "vrcMainPtEevOpened": vrcMainPtEevOpened,
       "vrcMainPtAlarmNumbers": vrcMainPtAlarmNumbers,
       "vrcMainPtHistoryAlarmNumbers": vrcMainPtHistoryAlarmNumbers,
       "vrcMainPtHpAbnRecordCnt": vrcMainPtHpAbnRecordCnt,
       "vrcMainPtMonitorBaudrate": vrcMainPtMonitorBaudrate,
       "vrcMainPtMonitorAddress": vrcMainPtMonitorAddress,
       "vrcMainPtLp": vrcMainPtLp,
       "vrcMainPtFilterMaintRemind": vrcMainPtFilterMaintRemind,
       "vrcMainPtCoolingFlag": vrcMainPtCoolingFlag,
       "vrcMainPtFirstOnFlag": vrcMainPtFirstOnFlag,
       "vrcMainPtNewAlarmFlag": vrcMainPtNewAlarmFlag,
       "vrcMainPtComAlarmOutState": vrcMainPtComAlarmOutState,
       "vrcMainPtHighWaterInput": vrcMainPtHighWaterInput,
       "vrcMainPtHighWaterAlarm": vrcMainPtHighWaterAlarm,
       "vrcMainPtWaterUnderFloorAlarm": vrcMainPtWaterUnderFloorAlarm,
       "vrcMainPtSwShutDownStatus": vrcMainPtSwShutDownStatus,
       "vrcMainPtRemoteShutdown": vrcMainPtRemoteShutdown,
       "vrcMainPtRemoteShutDownFlag": vrcMainPtRemoteShutDownFlag,
       "vrcMainPtRemoteShutDownAlarm": vrcMainPtRemoteShutDownAlarm,
       "vrcMainPtHmiShutDownFlag": vrcMainPtHmiShutDownFlag,
       "vrcMainPtLpAlarm": vrcMainPtLpAlarm,
       "vrcMainPtHpAlarm": vrcMainPtHpAlarm,
       "vrcMainPtLpFreqAlarm": vrcMainPtLpFreqAlarm,
       "vrcMainPtHpFreqAlarm": vrcMainPtHpFreqAlarm,
       "vrcMainPtLpSensorFailAlarm": vrcMainPtLpSensorFailAlarm,
       "vrcMainPtHpSensorFailAlarm": vrcMainPtHpSensorFailAlarm,
       "vrcMainPtEevCommFailAlarm": vrcMainPtEevCommFailAlarm,
       "vrcMainCfgTable": vrcMainCfgTable,
       "vrcMainCfgEntry": vrcMainCfgEntry,
       "vrcMainCfgIndex": vrcMainCfgIndex,
       "vrcMainCfgModelSelect": vrcMainCfgModelSelect,
       "vrcMainCfgSystemTimeYear": vrcMainCfgSystemTimeYear,
       "vrcMainCfgSystemTimeMonth": vrcMainCfgSystemTimeMonth,
       "vrcMainCfgSystemTimeDay": vrcMainCfgSystemTimeDay,
       "vrcMainCfgSystemTimeHour": vrcMainCfgSystemTimeHour,
       "vrcMainCfgSystemTimeMin": vrcMainCfgSystemTimeMin,
       "vrcMainCfgSystemTimeSec": vrcMainCfgSystemTimeSec,
       "vrcMainCfgEevShtSettingMin": vrcMainCfgEevShtSettingMin,
       "vrcMainCfgEevShtSettingMax": vrcMainCfgEevShtSettingMax,
       "vrcMainCfgEevValveCloseSht": vrcMainCfgEevValveCloseSht,
       "vrcMainCfgEevMopPressSetting": vrcMainCfgEevMopPressSetting,
       "vrcMainCfgLpdt": vrcMainCfgLpdt,
       "vrcMainCfgDeadBand": vrcMainCfgDeadBand,
       "vrcMainCfgOnOffSwitch": vrcMainCfgOnOffSwitch,
       "vrcMainCfgVacuumState": vrcMainCfgVacuumState,
       "vrcMainCfgControlMode": vrcMainCfgControlMode,
       "vrcMainCfgManualRunEnable": vrcMainCfgManualRunEnable,
       "vrcMainCfgRemShutdownInput": vrcMainCfgRemShutdownInput,
       "vrcMainCfgMonitorShutDownFlag": vrcMainCfgMonitorShutDownFlag,
       "vrcMainCfgFirstOnPassword": vrcMainCfgFirstOnPassword,
       "vrcMainCfgFilterMaintSetting": vrcMainCfgFilterMaintSetting,
       "vrcMainCfgFilterMaintRemindTime": vrcMainCfgFilterMaintRemindTime,
       "vrcMainCfgFilterMaintRemindCtrl": vrcMainCfgFilterMaintRemindCtrl,
       "vrcMainCfgCommonAlarmOutputDir": vrcMainCfgCommonAlarmOutputDir,
       "vrcMainCfgHpAbnAlarmSetting": vrcMainCfgHpAbnAlarmSetting,
       "vrcMainCfgLpAlarmCtrl": vrcMainCfgLpAlarmCtrl,
       "vrcMainCfgHpAlarmCtrl": vrcMainCfgHpAlarmCtrl,
       "vrcMainCfgLpFreqAlarmCtrl": vrcMainCfgLpFreqAlarmCtrl,
       "vrcMainCfgHpFreqAlarmCtrl": vrcMainCfgHpFreqAlarmCtrl,
       "vrcMainCfgLpSensorFailAlarmCtrl": vrcMainCfgLpSensorFailAlarmCtrl,
       "vrcMainCfgHpSensorFailAlarmCtrl": vrcMainCfgHpSensorFailAlarmCtrl,
       "vrcMainCfgHighWaterAlarmCtrl": vrcMainCfgHighWaterAlarmCtrl,
       "vrcMainCfgRemShutdownAlarmCtrl": vrcMainCfgRemShutdownAlarmCtrl,
       "vrcMainCfgEevCommFailAlarmCtrl": vrcMainCfgEevCommFailAlarmCtrl,
       "vrcOutFanPtTable": vrcOutFanPtTable,
       "vrcOutFanPtEntry": vrcOutFanPtEntry,
       "vrcOutFanPtIndex": vrcOutFanPtIndex,
       "vrcOutFanPtName": vrcOutFanPtName,
       "vrcOutFanPtSpeed": vrcOutFanPtSpeed,
       "vrcOutFanCfgTable": vrcOutFanCfgTable,
       "vrcOutFanCfgEntry": vrcOutFanCfgEntry,
       "vrcOutFanCfgIndex": vrcOutFanCfgIndex,
       "vrcOutFanCfgStartPress": vrcOutFanCfgStartPress,
       "vrcOutFanCfgPressSetting": vrcOutFanCfgPressSetting,
       "vrcOutFanCfgMinPowerVoltage": vrcOutFanCfgMinPowerVoltage,
       "vrcOutFanCfgMaxPowerVoltage": vrcOutFanCfgMaxPowerVoltage,
       "vrcOutFanCfgSpeed": vrcOutFanCfgSpeed,
       "vrcInFanPtTable": vrcInFanPtTable,
       "vrcInFanPtEntry": vrcInFanPtEntry,
       "vrcInFanPtIndex": vrcInFanPtIndex,
       "vrcInFanPtName": vrcInFanPtName,
       "vrcInFanPtRunTimeHours": vrcInFanPtRunTimeHours,
       "vrcInFanPtStartStopCount": vrcInFanPtStartStopCount,
       "vrcInFanCfgTable": vrcInFanCfgTable,
       "vrcInFanCfgEntry": vrcInFanCfgEntry,
       "vrcInFanCfgIndex": vrcInFanCfgIndex,
       "vrcInFanCfgOutputStatus": vrcInFanCfgOutputStatus,
       "vrcInFanCfgLowSpeedStep": vrcInFanCfgLowSpeedStep,
       "vrcInFanCfgHighSpeedStep": vrcInFanCfgHighSpeedStep,
       "vrcInFanCfgMinSpeed": vrcInFanCfgMinSpeed,
       "vrcInFanCfgStandardSpeed": vrcInFanCfgStandardSpeed,
       "vrcInFanCfgMinCfc": vrcInFanCfgMinCfc,
       "vrcInFanCfgStandardCfc": vrcInFanCfgStandardCfc,
       "vrcInFanCfgStartDelay": vrcInFanCfgStartDelay,
       "vrcInFanCfgStopDelay": vrcInFanCfgStopDelay,
       "vrcInFanCfgReduceSpeedDelay": vrcInFanCfgReduceSpeedDelay,
       "vrcInFanCfgJumpBand1": vrcInFanCfgJumpBand1,
       "vrcInFanCfgJumpBand2": vrcInFanCfgJumpBand2,
       "vrcInFanCfgJumpBand3": vrcInFanCfgJumpBand3,
       "vrcInFanCfgJumpBand4": vrcInFanCfgJumpBand4,
       "vrcInFanCfgJumpBand5": vrcInFanCfgJumpBand5,
       "vrcInFanCfgJumpFreq1": vrcInFanCfgJumpFreq1,
       "vrcInFanCfgJumpFreq2": vrcInFanCfgJumpFreq2,
       "vrcInFanCfgJumpFreq3": vrcInFanCfgJumpFreq3,
       "vrcInFanCfgJumpFreq4": vrcInFanCfgJumpFreq4,
       "vrcInFanCfgJumpFreq5": vrcInFanCfgJumpFreq5,
       "vrcInFanCfgTempP": vrcInFanCfgTempP,
       "vrcInFanCfgTempI": vrcInFanCfgTempI,
       "vrcInFanCfgTempD": vrcInFanCfgTempD,
       "vrcCompPtTable": vrcCompPtTable,
       "vrcCompPtEntry": vrcCompPtEntry,
       "vrcCompPtIndex": vrcCompPtIndex,
       "vrcCompPtName": vrcCompPtName,
       "vrcCompPtCapacity": vrcCompPtCapacity,
       "vrcCompPtRunTimeHours": vrcCompPtRunTimeHours,
       "vrcCompPtStartStopCount": vrcCompPtStartStopCount,
       "vrcCompPtDriverFaultU00": vrcCompPtDriverFaultU00,
       "vrcCompPtDriverFaultU01": vrcCompPtDriverFaultU01,
       "vrcCompPtDriverFaultU02": vrcCompPtDriverFaultU02,
       "vrcCompPtDriverFaultU03": vrcCompPtDriverFaultU03,
       "vrcCompPtDriverFaultU04": vrcCompPtDriverFaultU04,
       "vrcCompPtDriverFaultU05": vrcCompPtDriverFaultU05,
       "vrcCompPtDriverFaultU06": vrcCompPtDriverFaultU06,
       "vrcCompPtDriverFaultU07": vrcCompPtDriverFaultU07,
       "vrcCompPtDriverFaultU08": vrcCompPtDriverFaultU08,
       "vrcCompPtDriverFaultU09": vrcCompPtDriverFaultU09,
       "vrcCompPtDriverFaultU10": vrcCompPtDriverFaultU10,
       "vrcCompPtDriverFaultU11": vrcCompPtDriverFaultU11,
       "vrcCompPtDriverFaultU12": vrcCompPtDriverFaultU12,
       "vrcCompPtDriverFaultU13": vrcCompPtDriverFaultU13,
       "vrcCompPtDriverFaultU14": vrcCompPtDriverFaultU14,
       "vrcCompPtDriverFaultU15": vrcCompPtDriverFaultU15,
       "vrcCompPtDriverCommFailAlarm": vrcCompPtDriverCommFailAlarm,
       "vrcCompPtFaultLockAlarm": vrcCompPtFaultLockAlarm,
       "vrcCompCfgTable": vrcCompCfgTable,
       "vrcCompCfgEntry": vrcCompCfgEntry,
       "vrcCompCfgIndex": vrcCompCfgIndex,
       "vrcCompCfgOutputStatus": vrcCompCfgOutputStatus,
       "vrcCompCfgOutputDeadBand": vrcCompCfgOutputDeadBand,
       "vrcCompCfgCapacityOutputValue": vrcCompCfgCapacityOutputValue,
       "vrcCompCfgMinCapacity": vrcCompCfgMinCapacity,
       "vrcCompCfgStartCapacity": vrcCompCfgStartCapacity,
       "vrcCompCfgStandardCapacity": vrcCompCfgStandardCapacity,
       "vrcCompCfgStartCfc": vrcCompCfgStartCfc,
       "vrcCompCfgStopCfc": vrcCompCfgStopCfc,
       "vrcCompCfgMinRunTime": vrcCompCfgMinRunTime,
       "vrcCompCfgMinStopTime": vrcCompCfgMinStopTime,
       "vrcCompCfgJumpBand1": vrcCompCfgJumpBand1,
       "vrcCompCfgJumpBand2": vrcCompCfgJumpBand2,
       "vrcCompCfgJumpBand3": vrcCompCfgJumpBand3,
       "vrcCompCfgJumpBand4": vrcCompCfgJumpBand4,
       "vrcCompCfgJumpBand5": vrcCompCfgJumpBand5,
       "vrcCompCfgJumpFreq1": vrcCompCfgJumpFreq1,
       "vrcCompCfgJumpFreq2": vrcCompCfgJumpFreq2,
       "vrcCompCfgJumpFreq3": vrcCompCfgJumpFreq3,
       "vrcCompCfgJumpFreq4": vrcCompCfgJumpFreq4,
       "vrcCompCfgJumpFreq5": vrcCompCfgJumpFreq5,
       "vrcCompCfgTempP": vrcCompCfgTempP,
       "vrcCompCfgTempI": vrcCompCfgTempI,
       "vrcCompCfgTempD": vrcCompCfgTempD,
       "vrcCompCfgDriverFaultAlmCtrl": vrcCompCfgDriverFaultAlmCtrl,
       "vrcCompCfgDriverCommFailAlmCtrl": vrcCompCfgDriverCommFailAlmCtrl,
       "vrcCompCfgFaultLockAlmCtrl": vrcCompCfgFaultLockAlmCtrl,
       "vrcReturnPtTable": vrcReturnPtTable,
       "vrcReturnPtEntry": vrcReturnPtEntry,
       "vrcReturnPtIndex": vrcReturnPtIndex,
       "vrcReturnPtName": vrcReturnPtName,
       "vrcReturnPtTemp": vrcReturnPtTemp,
       "vrcReturnPtHighTempAlarm": vrcReturnPtHighTempAlarm,
       "vrcReturnPtTempSensorFailAlarm": vrcReturnPtTempSensorFailAlarm,
       "vrcReturnCfgTable": vrcReturnCfgTable,
       "vrcReturnCfgEntry": vrcReturnCfgEntry,
       "vrcReturnCfgIndex": vrcReturnCfgIndex,
       "vrcReturnCfgOilCycle": vrcReturnCfgOilCycle,
       "vrcReturnCfgOilRunCapacity": vrcReturnCfgOilRunCapacity,
       "vrcReturnCfgOilRunTime": vrcReturnCfgOilRunTime,
       "vrcReturnCfgTempCalValue": vrcReturnCfgTempCalValue,
       "vrcReturnCfgTempSetting": vrcReturnCfgTempSetting,
       "vrcReturnCfgHighTempAlarmValue": vrcReturnCfgHighTempAlarmValue,
       "vrcReturnCfgHighTempAlarmCtrl": vrcReturnCfgHighTempAlarmCtrl,
       "vrcReturnCfgTempSensFailAlmCtrl": vrcReturnCfgTempSensFailAlmCtrl,
       "vrcSupplyPtTable": vrcSupplyPtTable,
       "vrcSupplyPtEntry": vrcSupplyPtEntry,
       "vrcSupplyPtIndex": vrcSupplyPtIndex,
       "vrcSupplyPtName": vrcSupplyPtName,
       "vrcSupplyPtTemp": vrcSupplyPtTemp,
       "vrcSupplyPtLowTempAlarm": vrcSupplyPtLowTempAlarm,
       "vrcSupplyPtHighTempAlarm": vrcSupplyPtHighTempAlarm,
       "vrcSupplyPtTempSensorFailAlarm": vrcSupplyPtTempSensorFailAlarm,
       "vrcSupplyCfgTable": vrcSupplyCfgTable,
       "vrcSupplyCfgEntry": vrcSupplyCfgEntry,
       "vrcSupplyCfgIndex": vrcSupplyCfgIndex,
       "vrcSupplyCfgTempCalValue": vrcSupplyCfgTempCalValue,
       "vrcSupplyCfgTempSetting": vrcSupplyCfgTempSetting,
       "vrcSupplyCfgLowTempAlarmValue": vrcSupplyCfgLowTempAlarmValue,
       "vrcSupplyCfgHighTempAlarmValue": vrcSupplyCfgHighTempAlarmValue,
       "vrcSupplyCfgLowTempAlmCtrl": vrcSupplyCfgLowTempAlmCtrl,
       "vrcSupplyCfgHighTempAlmCtrl": vrcSupplyCfgHighTempAlmCtrl,
       "vrcSupplyCfgTempSensFailAlmCtrl": vrcSupplyCfgTempSensFailAlmCtrl,
       "vrcPowerPtTable": vrcPowerPtTable,
       "vrcPowerPtEntry": vrcPowerPtEntry,
       "vrcPowerPtIndex": vrcPowerPtIndex,
       "vrcPowerPtName": vrcPowerPtName,
       "vrcPowerPtVoltage": vrcPowerPtVoltage,
       "vrcPowerPtFrequency": vrcPowerPtFrequency,
       "vrcPowerPtLowVoltageAlarm": vrcPowerPtLowVoltageAlarm,
       "vrcPowerPtHighVoltageAlarm": vrcPowerPtHighVoltageAlarm,
       "vrcPowerPtLossOfPhasePowerAlarm": vrcPowerPtLossOfPhasePowerAlarm,
       "vrcPowerPtLossOfPowerAlarm": vrcPowerPtLossOfPowerAlarm,
       "vrcPowerPtFrequencyErrorAlarm": vrcPowerPtFrequencyErrorAlarm,
       "vrcPowerCfgTable": vrcPowerCfgTable,
       "vrcPowerCfgEntry": vrcPowerCfgEntry,
       "vrcPowerCfgIndex": vrcPowerCfgIndex,
       "vrcPowerCfgLowVoltageSetting": vrcPowerCfgLowVoltageSetting,
       "vrcPowerCfgHighVoltageSetting": vrcPowerCfgHighVoltageSetting,
       "vrcPowerCfgLowVoltageAlarmCtrl": vrcPowerCfgLowVoltageAlarmCtrl,
       "vrcPowerCfgHighVoltageAlarmCtrl": vrcPowerCfgHighVoltageAlarmCtrl,
       "vrcPowerCfgLossOfPowerAlarmCtrl": vrcPowerCfgLossOfPowerAlarmCtrl,
       "vrcPowerCfgFreqErrorAlarmCtrl": vrcPowerCfgFreqErrorAlarmCtrl,
       "vrcOutdoorPtTable": vrcOutdoorPtTable,
       "vrcOutdoorPtEntry": vrcOutdoorPtEntry,
       "vrcOutdoorPtIndex": vrcOutdoorPtIndex,
       "vrcOutdoorPtName": vrcOutdoorPtName,
       "vrcOutdoorPtTemp": vrcOutdoorPtTemp,
       "vrcDischPtTable": vrcDischPtTable,
       "vrcDischPtEntry": vrcDischPtEntry,
       "vrcDischPtIndex": vrcDischPtIndex,
       "vrcDischPtName": vrcDischPtName,
       "vrcDischPtTemp": vrcDischPtTemp,
       "vrcDischPtPressure": vrcDischPtPressure,
       "vrcDischPtHighTempAlarm": vrcDischPtHighTempAlarm,
       "vrcDischPtHighTempFreqAlarm": vrcDischPtHighTempFreqAlarm,
       "vrcDischPtTempSensorFailAlarm": vrcDischPtTempSensorFailAlarm,
       "vrcDischCfgTable": vrcDischCfgTable,
       "vrcDischCfgEntry": vrcDischCfgEntry,
       "vrcDischCfgIndex": vrcDischCfgIndex,
       "vrcDischCfgTempCalValue": vrcDischCfgTempCalValue,
       "vrcDischCfgPressCalValue": vrcDischCfgPressCalValue,
       "vrcDischCfgHighTempAlmCtrl": vrcDischCfgHighTempAlmCtrl,
       "vrcDischCfgHighTempFreqAlmCtrl": vrcDischCfgHighTempFreqAlmCtrl,
       "vrcDischCfgTempSensFailAlmCtrl": vrcDischCfgTempSensFailAlmCtrl,
       "vrcSuctPtTable": vrcSuctPtTable,
       "vrcSuctPtEntry": vrcSuctPtEntry,
       "vrcSuctPtIndex": vrcSuctPtIndex,
       "vrcSuctPtName": vrcSuctPtName,
       "vrcSuctPtTemp": vrcSuctPtTemp,
       "vrcSuctPtPressure": vrcSuctPtPressure,
       "vrcSuctPtSuperHeatTemp": vrcSuctPtSuperHeatTemp,
       "vrcSuctPtTempSensorFailAlarm": vrcSuctPtTempSensorFailAlarm,
       "vrcSuctCfgTable": vrcSuctCfgTable,
       "vrcSuctCfgEntry": vrcSuctCfgEntry,
       "vrcSuctCfgIndex": vrcSuctCfgIndex,
       "vrcSuctCfgPressCalValue": vrcSuctCfgPressCalValue,
       "vrcSuctCfgTempSensFailAlmCtrl": vrcSuctCfgTempSensFailAlmCtrl,
       "trap": trap,
       "trapPrefix": trapPrefix,
       "internalTestNOTIFY": internalTestNOTIFY,
       "pduMainAvailNOTIFY": pduMainAvailNOTIFY,
       "pduTotalRealPowerNOTIFY": pduTotalRealPowerNOTIFY,
       "pduTotalApparentPowerNOTIFY": pduTotalApparentPowerNOTIFY,
       "pduTotalPowerFactorNOTIFY": pduTotalPowerFactorNOTIFY,
       "pduTotalEnergyNOTIFY": pduTotalEnergyNOTIFY,
       "pduPhaseVoltageNOTIFY": pduPhaseVoltageNOTIFY,
       "pduPhaseCurrentNOTIFY": pduPhaseCurrentNOTIFY,
       "pduPhaseRealPowerNOTIFY": pduPhaseRealPowerNOTIFY,
       "pduPhaseApparentPowerNOTIFY": pduPhaseApparentPowerNOTIFY,
       "pduPhasePowerFactorNOTIFY": pduPhasePowerFactorNOTIFY,
       "pduPhaseEnergyNOTIFY": pduPhaseEnergyNOTIFY,
       "pduPhaseBalanceNOTIFY": pduPhaseBalanceNOTIFY,
       "pduPhaseCurrentCrestFactorNOTIFY": pduPhaseCurrentCrestFactorNOTIFY,
       "pduBreakerCurrentNOTIFY": pduBreakerCurrentNOTIFY,
       "pduBreakerVoltageNOTIFY": pduBreakerVoltageNOTIFY,
       "pduBreakerRealPowerNOTIFY": pduBreakerRealPowerNOTIFY,
       "pduBreakerApparentPowerNOTIFY": pduBreakerApparentPowerNOTIFY,
       "pduBreakerPowerFactorNOTIFY": pduBreakerPowerFactorNOTIFY,
       "pduBreakerEnergyNOTIFY": pduBreakerEnergyNOTIFY,
       "pduLineCurrentNOTIFY": pduLineCurrentNOTIFY,
       "pduOutletMeterVoltageNOTIFY": pduOutletMeterVoltageNOTIFY,
       "pduOutletMeterCurrentNOTIFY": pduOutletMeterCurrentNOTIFY,
       "pduOutletMeterRealPowerNOTIFY": pduOutletMeterRealPowerNOTIFY,
       "pduOutletMeterApparentPowerNOTIFY": pduOutletMeterApparentPowerNOTIFY,
       "pduOutletMeterPowerFactorNOTIFY": pduOutletMeterPowerFactorNOTIFY,
       "pduOutletMeterEnergyNOTIFY": pduOutletMeterEnergyNOTIFY,
       "pduOutletCurrentCrestFactorNOTIFY": pduOutletCurrentCrestFactorNOTIFY,
       "tempSensorAvailNOTIFY": tempSensorAvailNOTIFY,
       "tempSensorTempNOTIFY": tempSensorTempNOTIFY,
       "airFlowSensorAvailNOTIFY": airFlowSensorAvailNOTIFY,
       "airFlowSensorTempNOTIFY": airFlowSensorTempNOTIFY,
       "airFlowSensorFlowNOTIFY": airFlowSensorFlowNOTIFY,
       "airFlowSensorHumidityNOTIFY": airFlowSensorHumidityNOTIFY,
       "airFlowSensorDewPointNOTIFY": airFlowSensorDewPointNOTIFY,
       "t3hdSensorAvailNOTIFY": t3hdSensorAvailNOTIFY,
       "t3hdSensorIntTempNOTIFY": t3hdSensorIntTempNOTIFY,
       "t3hdSensorIntHumidityNOTIFY": t3hdSensorIntHumidityNOTIFY,
       "t3hdSensorIntDewPointNOTIFY": t3hdSensorIntDewPointNOTIFY,
       "t3hdSensorExtATempNOTIFY": t3hdSensorExtATempNOTIFY,
       "t3hdSensorExtBTempNOTIFY": t3hdSensorExtBTempNOTIFY,
       "thdSensorAvailNOTIFY": thdSensorAvailNOTIFY,
       "thdSensorTempNOTIFY": thdSensorTempNOTIFY,
       "thdSensorHumidityNOTIFY": thdSensorHumidityNOTIFY,
       "thdSensorDewPointNOTIFY": thdSensorDewPointNOTIFY,
       "a2dSensorAvailNOTIFY": a2dSensorAvailNOTIFY,
       "a2dSensorValueNOTIFY": a2dSensorValueNOTIFY,
       "humiditySensorAvailNOTIFY": humiditySensorAvailNOTIFY,
       "humiditySensorValueNOTIFY": humiditySensorValueNOTIFY,
       "sn2dSensorAvailNOTIFY": sn2dSensorAvailNOTIFY,
       "sn2dSensorDoor1StateNOTIFY": sn2dSensorDoor1StateNOTIFY,
       "sn2dSensorDoor2StateNOTIFY": sn2dSensorDoor2StateNOTIFY,
       "vrcMainAvailNOTIFY": vrcMainAvailNOTIFY,
       "vrcOutFanPtSpeedNOTIFY": vrcOutFanPtSpeedNOTIFY,
       "vrcCompPtCapacityNOTIFY": vrcCompPtCapacityNOTIFY,
       "vrcReturnPtTempNOTIFY": vrcReturnPtTempNOTIFY,
       "vrcSupplyPtTempNOTIFY": vrcSupplyPtTempNOTIFY,
       "vrcPowerPtVoltageNOTIFY": vrcPowerPtVoltageNOTIFY,
       "vrcPowerPtFrequencyNOTIFY": vrcPowerPtFrequencyNOTIFY,
       "vrcOutdoorPtTempNOTIFY": vrcOutdoorPtTempNOTIFY,
       "vrcDischPtTempNOTIFY": vrcDischPtTempNOTIFY,
       "vrcDischPtPressureNOTIFY": vrcDischPtPressureNOTIFY,
       "vrcSuctPtTempNOTIFY": vrcSuctPtTempNOTIFY,
       "vrcSuctPtPressureNOTIFY": vrcSuctPtPressureNOTIFY,
       "pduMainAvailCLEAR": pduMainAvailCLEAR,
       "pduTotalRealPowerCLEAR": pduTotalRealPowerCLEAR,
       "pduTotalApparentPowerCLEAR": pduTotalApparentPowerCLEAR,
       "pduTotalPowerFactorCLEAR": pduTotalPowerFactorCLEAR,
       "pduTotalEnergyCLEAR": pduTotalEnergyCLEAR,
       "pduPhaseVoltageCLEAR": pduPhaseVoltageCLEAR,
       "pduPhaseCurrentCLEAR": pduPhaseCurrentCLEAR,
       "pduPhaseRealPowerCLEAR": pduPhaseRealPowerCLEAR,
       "pduPhaseApparentPowerCLEAR": pduPhaseApparentPowerCLEAR,
       "pduPhasePowerFactorCLEAR": pduPhasePowerFactorCLEAR,
       "pduPhaseEnergyCLEAR": pduPhaseEnergyCLEAR,
       "pduPhaseBalanceCLEAR": pduPhaseBalanceCLEAR,
       "pduPhaseCurrentCrestFactorCLEAR": pduPhaseCurrentCrestFactorCLEAR,
       "pduBreakerCurrentCLEAR": pduBreakerCurrentCLEAR,
       "pduBreakerVoltageCLEAR": pduBreakerVoltageCLEAR,
       "pduBreakerRealPowerCLEAR": pduBreakerRealPowerCLEAR,
       "pduBreakerApparentPowerCLEAR": pduBreakerApparentPowerCLEAR,
       "pduBreakerPowerFactorCLEAR": pduBreakerPowerFactorCLEAR,
       "pduBreakerEnergyCLEAR": pduBreakerEnergyCLEAR,
       "pduLineCurrentCLEAR": pduLineCurrentCLEAR,
       "pduOutletMeterVoltageCLEAR": pduOutletMeterVoltageCLEAR,
       "pduOutletMeterCurrentCLEAR": pduOutletMeterCurrentCLEAR,
       "pduOutletMeterRealPowerCLEAR": pduOutletMeterRealPowerCLEAR,
       "pduOutletMeterApparentPowerCLEAR": pduOutletMeterApparentPowerCLEAR,
       "pduOutletMeterPowerFactorCLEAR": pduOutletMeterPowerFactorCLEAR,
       "pduOutletMeterEnergyCLEAR": pduOutletMeterEnergyCLEAR,
       "pduOutletCurrentCrestFactorCLEAR": pduOutletCurrentCrestFactorCLEAR,
       "tempSensorAvailCLEAR": tempSensorAvailCLEAR,
       "tempSensorTempCLEAR": tempSensorTempCLEAR,
       "airFlowSensorAvailCLEAR": airFlowSensorAvailCLEAR,
       "airFlowSensorTempCLEAR": airFlowSensorTempCLEAR,
       "airFlowSensorFlowCLEAR": airFlowSensorFlowCLEAR,
       "airFlowSensorHumidityCLEAR": airFlowSensorHumidityCLEAR,
       "airFlowSensorDewPointCLEAR": airFlowSensorDewPointCLEAR,
       "t3hdSensorAvailCLEAR": t3hdSensorAvailCLEAR,
       "t3hdSensorIntTempCLEAR": t3hdSensorIntTempCLEAR,
       "t3hdSensorIntHumidityCLEAR": t3hdSensorIntHumidityCLEAR,
       "t3hdSensorIntDewPointCLEAR": t3hdSensorIntDewPointCLEAR,
       "t3hdSensorExtATempCLEAR": t3hdSensorExtATempCLEAR,
       "t3hdSensorExtBTempCLEAR": t3hdSensorExtBTempCLEAR,
       "thdSensorAvailCLEAR": thdSensorAvailCLEAR,
       "thdSensorTempCLEAR": thdSensorTempCLEAR,
       "thdSensorHumidityCLEAR": thdSensorHumidityCLEAR,
       "thdSensorDewPointCLEAR": thdSensorDewPointCLEAR,
       "a2dSensorAvailCLEAR": a2dSensorAvailCLEAR,
       "a2dSensorValueCLEAR": a2dSensorValueCLEAR,
       "humiditySensorAvailCLEAR": humiditySensorAvailCLEAR,
       "humiditySensorValueCLEAR": humiditySensorValueCLEAR,
       "sn2dSensorAvailCLEAR": sn2dSensorAvailCLEAR,
       "sn2dSensorDoor1StateCLEAR": sn2dSensorDoor1StateCLEAR,
       "sn2dSensorDoor2StateCLEAR": sn2dSensorDoor2StateCLEAR,
       "vrcMainAvailCLEAR": vrcMainAvailCLEAR,
       "vrcOutFanPtSpeedCLEAR": vrcOutFanPtSpeedCLEAR,
       "vrcCompPtCapacityCLEAR": vrcCompPtCapacityCLEAR,
       "vrcReturnPtTempCLEAR": vrcReturnPtTempCLEAR,
       "vrcSupplyPtTempCLEAR": vrcSupplyPtTempCLEAR,
       "vrcPowerPtVoltageCLEAR": vrcPowerPtVoltageCLEAR,
       "vrcPowerPtFrequencyCLEAR": vrcPowerPtFrequencyCLEAR,
       "vrcOutdoorPtTempCLEAR": vrcOutdoorPtTempCLEAR,
       "vrcDischPtTempCLEAR": vrcDischPtTempCLEAR,
       "vrcDischPtPressureCLEAR": vrcDischPtPressureCLEAR,
       "vrcSuctPtTempCLEAR": vrcSuctPtTempCLEAR,
       "vrcSuctPtPressureCLEAR": vrcSuctPtPressureCLEAR,
       "trapObj": trapObj,
       "trapSeverity": trapSeverity,
       "trapThreshType": trapThreshType,
       "common": common,
       "identity": identity,
       "r05": r05,
       "i03": i03}
)
