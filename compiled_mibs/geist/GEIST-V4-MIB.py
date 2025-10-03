# SNMP MIB module (GEIST-V4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\geist\GEIST-V4-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:47:18 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

geist = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21239)
)
if mibBuilder.loadTexts:
    geist.setRevisions(
        ("2012-09-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Blackbird_ObjectIdentity = ObjectIdentity
blackbird = _Blackbird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 5)
)
_Watchdog100_ObjectIdentity = ObjectIdentity
watchdog100 = _Watchdog100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1)
)
_DeviceInfo_ObjectIdentity = ObjectIdentity
deviceInfo = _DeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 1)
)
_ProductTitle_Type = DisplayString
_ProductTitle_Object = MibScalar
productTitle = _ProductTitle_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 1, 1),
    _ProductTitle_Type()
)
productTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productTitle.setStatus("current")
_ProductVersion_Type = DisplayString
_ProductVersion_Object = MibScalar
productVersion = _ProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 1, 2),
    _ProductVersion_Type()
)
productVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productVersion.setStatus("current")
_ProductFriendlyName_Type = DisplayString
_ProductFriendlyName_Object = MibScalar
productFriendlyName = _ProductFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 1, 3),
    _ProductFriendlyName_Type()
)
productFriendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productFriendlyName.setStatus("current")
_ProductMacAddress_Type = OctetString
_ProductMacAddress_Object = MibScalar
productMacAddress = _ProductMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 1, 4),
    _ProductMacAddress_Type()
)
productMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productMacAddress.setStatus("current")
_ProductUrl_Type = IpAddress
_ProductUrl_Object = MibScalar
productUrl = _ProductUrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 1, 5),
    _ProductUrl_Type()
)
productUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productUrl.setStatus("current")


class _DeviceCount_Type(Integer32):
    """Custom type deviceCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DeviceCount_Type.__name__ = "Integer32"
_DeviceCount_Object = MibScalar
deviceCount = _DeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 1, 6),
    _DeviceCount_Type()
)
deviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCount.setStatus("current")


class _TemperatureUnits_Type(Integer32):
    """Custom type temperatureUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TemperatureUnits_Type.__name__ = "Integer32"
_TemperatureUnits_Object = MibScalar
temperatureUnits = _TemperatureUnits_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 1, 7),
    _TemperatureUnits_Type()
)
temperatureUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureUnits.setStatus("current")
_InternalTable_Object = MibTable
internalTable = _InternalTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 2)
)
if mibBuilder.loadTexts:
    internalTable.setStatus("current")
_InternalEntry_Object = MibTableRow
internalEntry = _InternalEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 2, 1)
)
internalEntry.setIndexNames(
    (0, "GEIST-V4-MIB", "internalIndex"),
)
if mibBuilder.loadTexts:
    internalEntry.setStatus("current")


class _InternalIndex_Type(Integer32):
    """Custom type internalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_InternalIndex_Type.__name__ = "Integer32"
_InternalIndex_Object = MibTableColumn
internalIndex = _InternalIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 2, 1, 1),
    _InternalIndex_Type()
)
internalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalIndex.setStatus("current")
_InternalSerial_Type = DisplayString
_InternalSerial_Object = MibTableColumn
internalSerial = _InternalSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 2, 1, 2),
    _InternalSerial_Type()
)
internalSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalSerial.setStatus("current")
_InternalName_Type = DisplayString
_InternalName_Object = MibTableColumn
internalName = _InternalName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 2, 1, 3),
    _InternalName_Type()
)
internalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalName.setStatus("current")
_InternalAvail_Type = Gauge32
_InternalAvail_Object = MibTableColumn
internalAvail = _InternalAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 2, 1, 4),
    _InternalAvail_Type()
)
internalAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalAvail.setStatus("current")


class _InternalTemp_Type(Integer32):
    """Custom type internalTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 200),
    )


_InternalTemp_Type.__name__ = "Integer32"
_InternalTemp_Object = MibTableColumn
internalTemp = _InternalTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 2, 1, 5),
    _InternalTemp_Type()
)
internalTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalTemp.setStatus("current")
if mibBuilder.loadTexts:
    internalTemp.setUnits("0.1 Degrees")


class _InternalHumidity_Type(Integer32):
    """Custom type internalHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_InternalHumidity_Type.__name__ = "Integer32"
_InternalHumidity_Object = MibTableColumn
internalHumidity = _InternalHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 2, 1, 6),
    _InternalHumidity_Type()
)
internalHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalHumidity.setStatus("current")
if mibBuilder.loadTexts:
    internalHumidity.setUnits("%")


class _InternalDewPoint_Type(Integer32):
    """Custom type internalDewPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 200),
    )


_InternalDewPoint_Type.__name__ = "Integer32"
_InternalDewPoint_Object = MibTableColumn
internalDewPoint = _InternalDewPoint_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 2, 1, 7),
    _InternalDewPoint_Type()
)
internalDewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalDewPoint.setStatus("current")
if mibBuilder.loadTexts:
    internalDewPoint.setUnits("0.1 Degrees")
_TempSensorTable_Object = MibTable
tempSensorTable = _TempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 4)
)
if mibBuilder.loadTexts:
    tempSensorTable.setStatus("current")
_TempSensorEntry_Object = MibTableRow
tempSensorEntry = _TempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 4, 1)
)
tempSensorEntry.setIndexNames(
    (0, "GEIST-V4-MIB", "tempSensorIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 4, 1, 1),
    _TempSensorIndex_Type()
)
tempSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorIndex.setStatus("current")
_TempSensorSerial_Type = DisplayString
_TempSensorSerial_Object = MibTableColumn
tempSensorSerial = _TempSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 4, 1, 2),
    _TempSensorSerial_Type()
)
tempSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorSerial.setStatus("current")
_TempSensorName_Type = DisplayString
_TempSensorName_Object = MibTableColumn
tempSensorName = _TempSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 4, 1, 3),
    _TempSensorName_Type()
)
tempSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorName.setStatus("current")
_TempSensorAvail_Type = Gauge32
_TempSensorAvail_Object = MibTableColumn
tempSensorAvail = _TempSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 4, 1, 4),
    _TempSensorAvail_Type()
)
tempSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorAvail.setStatus("current")


class _TempSensorTemp_Type(Integer32):
    """Custom type tempSensorTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 200),
    )


_TempSensorTemp_Type.__name__ = "Integer32"
_TempSensorTemp_Object = MibTableColumn
tempSensorTemp = _TempSensorTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 4, 1, 5),
    _TempSensorTemp_Type()
)
tempSensorTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorTemp.setStatus("current")
if mibBuilder.loadTexts:
    tempSensorTemp.setUnits("0.1 Degrees")
_AirFlowSensorTable_Object = MibTable
airFlowSensorTable = _AirFlowSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 5)
)
if mibBuilder.loadTexts:
    airFlowSensorTable.setStatus("current")
_AirFlowSensorEntry_Object = MibTableRow
airFlowSensorEntry = _AirFlowSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 5, 1)
)
airFlowSensorEntry.setIndexNames(
    (0, "GEIST-V4-MIB", "airFlowSensorIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 5, 1, 1),
    _AirFlowSensorIndex_Type()
)
airFlowSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorIndex.setStatus("current")
_AirFlowSensorSerial_Type = DisplayString
_AirFlowSensorSerial_Object = MibTableColumn
airFlowSensorSerial = _AirFlowSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 5, 1, 2),
    _AirFlowSensorSerial_Type()
)
airFlowSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorSerial.setStatus("current")
_AirFlowSensorName_Type = DisplayString
_AirFlowSensorName_Object = MibTableColumn
airFlowSensorName = _AirFlowSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 5, 1, 3),
    _AirFlowSensorName_Type()
)
airFlowSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorName.setStatus("current")
_AirFlowSensorAvail_Type = Gauge32
_AirFlowSensorAvail_Object = MibTableColumn
airFlowSensorAvail = _AirFlowSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 5, 1, 4),
    _AirFlowSensorAvail_Type()
)
airFlowSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorAvail.setStatus("current")


class _AirFlowSensorTemp_Type(Integer32):
    """Custom type airFlowSensorTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 200),
    )


_AirFlowSensorTemp_Type.__name__ = "Integer32"
_AirFlowSensorTemp_Object = MibTableColumn
airFlowSensorTemp = _AirFlowSensorTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 5, 1, 5),
    _AirFlowSensorTemp_Type()
)
airFlowSensorTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorTemp.setStatus("current")
if mibBuilder.loadTexts:
    airFlowSensorTemp.setUnits("0.1 Degrees")


class _AirFlowSensorFlow_Type(Integer32):
    """Custom type airFlowSensorFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AirFlowSensorFlow_Type.__name__ = "Integer32"
_AirFlowSensorFlow_Object = MibTableColumn
airFlowSensorFlow = _AirFlowSensorFlow_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 5, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 5, 1, 7),
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
        ValueRangeConstraint(-40, 200),
    )


_AirFlowSensorDewPoint_Type.__name__ = "Integer32"
_AirFlowSensorDewPoint_Object = MibTableColumn
airFlowSensorDewPoint = _AirFlowSensorDewPoint_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 5, 1, 8),
    _AirFlowSensorDewPoint_Type()
)
airFlowSensorDewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorDewPoint.setStatus("current")
if mibBuilder.loadTexts:
    airFlowSensorDewPoint.setUnits("0.1 Degrees")
_DewPointSensorTable_Object = MibTable
dewPointSensorTable = _DewPointSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 6)
)
if mibBuilder.loadTexts:
    dewPointSensorTable.setStatus("current")
_DewPointSensorEntry_Object = MibTableRow
dewPointSensorEntry = _DewPointSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 6, 1)
)
dewPointSensorEntry.setIndexNames(
    (0, "GEIST-V4-MIB", "dewPointSensorIndex"),
)
if mibBuilder.loadTexts:
    dewPointSensorEntry.setStatus("current")


class _DewPointSensorIndex_Type(Integer32):
    """Custom type dewPointSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_DewPointSensorIndex_Type.__name__ = "Integer32"
_DewPointSensorIndex_Object = MibTableColumn
dewPointSensorIndex = _DewPointSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 6, 1, 1),
    _DewPointSensorIndex_Type()
)
dewPointSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorIndex.setStatus("current")
_DewPointSensorSerial_Type = DisplayString
_DewPointSensorSerial_Object = MibTableColumn
dewPointSensorSerial = _DewPointSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 6, 1, 2),
    _DewPointSensorSerial_Type()
)
dewPointSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorSerial.setStatus("current")
_DewPointSensorName_Type = DisplayString
_DewPointSensorName_Object = MibTableColumn
dewPointSensorName = _DewPointSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 6, 1, 3),
    _DewPointSensorName_Type()
)
dewPointSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorName.setStatus("current")
_DewPointSensorAvail_Type = Gauge32
_DewPointSensorAvail_Object = MibTableColumn
dewPointSensorAvail = _DewPointSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 6, 1, 4),
    _DewPointSensorAvail_Type()
)
dewPointSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorAvail.setStatus("current")


class _DewPointSensorTemp_Type(Integer32):
    """Custom type dewPointSensorTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 200),
    )


_DewPointSensorTemp_Type.__name__ = "Integer32"
_DewPointSensorTemp_Object = MibTableColumn
dewPointSensorTemp = _DewPointSensorTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 6, 1, 5),
    _DewPointSensorTemp_Type()
)
dewPointSensorTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorTemp.setStatus("current")
if mibBuilder.loadTexts:
    dewPointSensorTemp.setUnits("0.1 Degrees")


class _DewPointSensorHumidity_Type(Integer32):
    """Custom type dewPointSensorHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DewPointSensorHumidity_Type.__name__ = "Integer32"
_DewPointSensorHumidity_Object = MibTableColumn
dewPointSensorHumidity = _DewPointSensorHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 6, 1, 6),
    _DewPointSensorHumidity_Type()
)
dewPointSensorHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorHumidity.setStatus("current")
if mibBuilder.loadTexts:
    dewPointSensorHumidity.setUnits("%")


class _DewPointSensorDewPoint_Type(Integer32):
    """Custom type dewPointSensorDewPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 200),
    )


_DewPointSensorDewPoint_Type.__name__ = "Integer32"
_DewPointSensorDewPoint_Object = MibTableColumn
dewPointSensorDewPoint = _DewPointSensorDewPoint_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 6, 1, 7),
    _DewPointSensorDewPoint_Type()
)
dewPointSensorDewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorDewPoint.setStatus("current")
if mibBuilder.loadTexts:
    dewPointSensorDewPoint.setUnits("0.1 Degrees")
_CcatSensorTable_Object = MibTable
ccatSensorTable = _CcatSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 7)
)
if mibBuilder.loadTexts:
    ccatSensorTable.setStatus("current")
_CcatSensorEntry_Object = MibTableRow
ccatSensorEntry = _CcatSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 7, 1)
)
ccatSensorEntry.setIndexNames(
    (0, "GEIST-V4-MIB", "ccatSensorIndex"),
)
if mibBuilder.loadTexts:
    ccatSensorEntry.setStatus("current")


class _CcatSensorIndex_Type(Integer32):
    """Custom type ccatSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcatSensorIndex_Type.__name__ = "Integer32"
_CcatSensorIndex_Object = MibTableColumn
ccatSensorIndex = _CcatSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 7, 1, 1),
    _CcatSensorIndex_Type()
)
ccatSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccatSensorIndex.setStatus("current")
_CcatSensorSerial_Type = DisplayString
_CcatSensorSerial_Object = MibTableColumn
ccatSensorSerial = _CcatSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 7, 1, 2),
    _CcatSensorSerial_Type()
)
ccatSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccatSensorSerial.setStatus("current")
_CcatSensorName_Type = DisplayString
_CcatSensorName_Object = MibTableColumn
ccatSensorName = _CcatSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 7, 1, 3),
    _CcatSensorName_Type()
)
ccatSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccatSensorName.setStatus("current")
_CcatSensorAvail_Type = Gauge32
_CcatSensorAvail_Object = MibTableColumn
ccatSensorAvail = _CcatSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 7, 1, 4),
    _CcatSensorAvail_Type()
)
ccatSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccatSensorAvail.setStatus("current")


class _CcatSensorValue_Type(Integer32):
    """Custom type ccatSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 5000),
    )


_CcatSensorValue_Type.__name__ = "Integer32"
_CcatSensorValue_Object = MibTableColumn
ccatSensorValue = _CcatSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 7, 1, 5),
    _CcatSensorValue_Type()
)
ccatSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccatSensorValue.setStatus("current")
_CcatSensorType_Type = DisplayString
_CcatSensorType_Object = MibTableColumn
ccatSensorType = _CcatSensorType_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 7, 1, 6),
    _CcatSensorType_Type()
)
ccatSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccatSensorType.setStatus("current")
_CcatSensorDescription_Type = DisplayString
_CcatSensorDescription_Object = MibTableColumn
ccatSensorDescription = _CcatSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 7, 1, 7),
    _CcatSensorDescription_Type()
)
ccatSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccatSensorDescription.setStatus("current")
_T3hdSensorTable_Object = MibTable
t3hdSensorTable = _T3hdSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 8)
)
if mibBuilder.loadTexts:
    t3hdSensorTable.setStatus("current")
_T3hdSensorEntry_Object = MibTableRow
t3hdSensorEntry = _T3hdSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 8, 1)
)
t3hdSensorEntry.setIndexNames(
    (0, "GEIST-V4-MIB", "t3hdSensorIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 8, 1, 1),
    _T3hdSensorIndex_Type()
)
t3hdSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorIndex.setStatus("current")
_T3hdSensorSerial_Type = DisplayString
_T3hdSensorSerial_Object = MibTableColumn
t3hdSensorSerial = _T3hdSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 8, 1, 2),
    _T3hdSensorSerial_Type()
)
t3hdSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorSerial.setStatus("current")
_T3hdSensorName_Type = DisplayString
_T3hdSensorName_Object = MibTableColumn
t3hdSensorName = _T3hdSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 8, 1, 3),
    _T3hdSensorName_Type()
)
t3hdSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorName.setStatus("current")
_T3hdSensorAvail_Type = Gauge32
_T3hdSensorAvail_Object = MibTableColumn
t3hdSensorAvail = _T3hdSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 8, 1, 4),
    _T3hdSensorAvail_Type()
)
t3hdSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorAvail.setStatus("current")
_T3hdSensorIntName_Type = DisplayString
_T3hdSensorIntName_Object = MibTableColumn
t3hdSensorIntName = _T3hdSensorIntName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 8, 1, 5),
    _T3hdSensorIntName_Type()
)
t3hdSensorIntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorIntName.setStatus("current")


class _T3hdSensorIntTemp_Type(Integer32):
    """Custom type t3hdSensorIntTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 200),
    )


_T3hdSensorIntTemp_Type.__name__ = "Integer32"
_T3hdSensorIntTemp_Object = MibTableColumn
t3hdSensorIntTemp = _T3hdSensorIntTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 8, 1, 6),
    _T3hdSensorIntTemp_Type()
)
t3hdSensorIntTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorIntTemp.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorIntTemp.setUnits("0.1 Degrees")


class _T3hdSensorIntHumidity_Type(Integer32):
    """Custom type t3hdSensorIntHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_T3hdSensorIntHumidity_Type.__name__ = "Integer32"
_T3hdSensorIntHumidity_Object = MibTableColumn
t3hdSensorIntHumidity = _T3hdSensorIntHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 8, 1, 7),
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
        ValueRangeConstraint(-40, 200),
    )


_T3hdSensorIntDewPoint_Type.__name__ = "Integer32"
_T3hdSensorIntDewPoint_Object = MibTableColumn
t3hdSensorIntDewPoint = _T3hdSensorIntDewPoint_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 8, 1, 8),
    _T3hdSensorIntDewPoint_Type()
)
t3hdSensorIntDewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorIntDewPoint.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorIntDewPoint.setUnits("0.1 Degrees")
_T3hdSensorExtAAvail_Type = Gauge32
_T3hdSensorExtAAvail_Object = MibTableColumn
t3hdSensorExtAAvail = _T3hdSensorExtAAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 8, 1, 9),
    _T3hdSensorExtAAvail_Type()
)
t3hdSensorExtAAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExtAAvail.setStatus("current")
_T3hdSensorExtAName_Type = DisplayString
_T3hdSensorExtAName_Object = MibTableColumn
t3hdSensorExtAName = _T3hdSensorExtAName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 8, 1, 10),
    _T3hdSensorExtAName_Type()
)
t3hdSensorExtAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExtAName.setStatus("current")


class _T3hdSensorExtATemp_Type(Integer32):
    """Custom type t3hdSensorExtATemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 200),
    )


_T3hdSensorExtATemp_Type.__name__ = "Integer32"
_T3hdSensorExtATemp_Object = MibTableColumn
t3hdSensorExtATemp = _T3hdSensorExtATemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 8, 1, 11),
    _T3hdSensorExtATemp_Type()
)
t3hdSensorExtATemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExtATemp.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorExtATemp.setUnits("0.1 Degrees")
_T3hdSensorExtBAvail_Type = Gauge32
_T3hdSensorExtBAvail_Object = MibTableColumn
t3hdSensorExtBAvail = _T3hdSensorExtBAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 8, 1, 12),
    _T3hdSensorExtBAvail_Type()
)
t3hdSensorExtBAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExtBAvail.setStatus("current")
_T3hdSensorExtBName_Type = DisplayString
_T3hdSensorExtBName_Object = MibTableColumn
t3hdSensorExtBName = _T3hdSensorExtBName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 8, 1, 13),
    _T3hdSensorExtBName_Type()
)
t3hdSensorExtBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExtBName.setStatus("current")


class _T3hdSensorExtBTemp_Type(Integer32):
    """Custom type t3hdSensorExtBTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 200),
    )


_T3hdSensorExtBTemp_Type.__name__ = "Integer32"
_T3hdSensorExtBTemp_Object = MibTableColumn
t3hdSensorExtBTemp = _T3hdSensorExtBTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 8, 1, 14),
    _T3hdSensorExtBTemp_Type()
)
t3hdSensorExtBTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExtBTemp.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorExtBTemp.setUnits("0.1 Degrees")
_ThdSensorTable_Object = MibTable
thdSensorTable = _ThdSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 9)
)
if mibBuilder.loadTexts:
    thdSensorTable.setStatus("current")
_ThdSensorEntry_Object = MibTableRow
thdSensorEntry = _ThdSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 9, 1)
)
thdSensorEntry.setIndexNames(
    (0, "GEIST-V4-MIB", "thdSensorIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 9, 1, 1),
    _ThdSensorIndex_Type()
)
thdSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorIndex.setStatus("current")
_ThdSensorSerial_Type = DisplayString
_ThdSensorSerial_Object = MibTableColumn
thdSensorSerial = _ThdSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 9, 1, 2),
    _ThdSensorSerial_Type()
)
thdSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorSerial.setStatus("current")
_ThdSensorName_Type = DisplayString
_ThdSensorName_Object = MibTableColumn
thdSensorName = _ThdSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 9, 1, 3),
    _ThdSensorName_Type()
)
thdSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorName.setStatus("current")
_ThdSensorAvail_Type = Gauge32
_ThdSensorAvail_Object = MibTableColumn
thdSensorAvail = _ThdSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 9, 1, 4),
    _ThdSensorAvail_Type()
)
thdSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorAvail.setStatus("current")


class _ThdSensorTemp_Type(Integer32):
    """Custom type thdSensorTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 200),
    )


_ThdSensorTemp_Type.__name__ = "Integer32"
_ThdSensorTemp_Object = MibTableColumn
thdSensorTemp = _ThdSensorTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 9, 1, 5),
    _ThdSensorTemp_Type()
)
thdSensorTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorTemp.setStatus("current")
if mibBuilder.loadTexts:
    thdSensorTemp.setUnits("0.1 Degrees")


class _ThdSensorHumidity_Type(Integer32):
    """Custom type thdSensorHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ThdSensorHumidity_Type.__name__ = "Integer32"
_ThdSensorHumidity_Object = MibTableColumn
thdSensorHumidity = _ThdSensorHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 9, 1, 6),
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
        ValueRangeConstraint(-40, 200),
    )


_ThdSensorDewPoint_Type.__name__ = "Integer32"
_ThdSensorDewPoint_Object = MibTableColumn
thdSensorDewPoint = _ThdSensorDewPoint_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 9, 1, 7),
    _ThdSensorDewPoint_Type()
)
thdSensorDewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorDewPoint.setStatus("current")
if mibBuilder.loadTexts:
    thdSensorDewPoint.setUnits("0.1 Degrees")
_RpmSensorTable_Object = MibTable
rpmSensorTable = _RpmSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 10)
)
if mibBuilder.loadTexts:
    rpmSensorTable.setStatus("current")
_RpmSensorEntry_Object = MibTableRow
rpmSensorEntry = _RpmSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 10, 1)
)
rpmSensorEntry.setIndexNames(
    (0, "GEIST-V4-MIB", "rpmSensorIndex"),
)
if mibBuilder.loadTexts:
    rpmSensorEntry.setStatus("current")


class _RpmSensorIndex_Type(Integer32):
    """Custom type rpmSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RpmSensorIndex_Type.__name__ = "Integer32"
_RpmSensorIndex_Object = MibTableColumn
rpmSensorIndex = _RpmSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 10, 1, 1),
    _RpmSensorIndex_Type()
)
rpmSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorIndex.setStatus("current")
_RpmSensorSerial_Type = DisplayString
_RpmSensorSerial_Object = MibTableColumn
rpmSensorSerial = _RpmSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 10, 1, 2),
    _RpmSensorSerial_Type()
)
rpmSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorSerial.setStatus("current")
_RpmSensorName_Type = DisplayString
_RpmSensorName_Object = MibTableColumn
rpmSensorName = _RpmSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 10, 1, 3),
    _RpmSensorName_Type()
)
rpmSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorName.setStatus("current")
_RpmSensorAvail_Type = Gauge32
_RpmSensorAvail_Object = MibTableColumn
rpmSensorAvail = _RpmSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 10, 1, 4),
    _RpmSensorAvail_Type()
)
rpmSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorAvail.setStatus("current")
_RpmSensorEnergy_Type = Gauge32
_RpmSensorEnergy_Object = MibTableColumn
rpmSensorEnergy = _RpmSensorEnergy_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 10, 1, 5),
    _RpmSensorEnergy_Type()
)
rpmSensorEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorEnergy.setStatus("current")
if mibBuilder.loadTexts:
    rpmSensorEnergy.setUnits("kWh")
_RpmSensorVoltage_Type = Gauge32
_RpmSensorVoltage_Object = MibTableColumn
rpmSensorVoltage = _RpmSensorVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 10, 1, 6),
    _RpmSensorVoltage_Type()
)
rpmSensorVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorVoltage.setStatus("current")
if mibBuilder.loadTexts:
    rpmSensorVoltage.setUnits("Volts (rms)")
_RpmSensorVoltageMax_Type = Gauge32
_RpmSensorVoltageMax_Object = MibTableColumn
rpmSensorVoltageMax = _RpmSensorVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 10, 1, 7),
    _RpmSensorVoltageMax_Type()
)
rpmSensorVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorVoltageMax.setStatus("current")
if mibBuilder.loadTexts:
    rpmSensorVoltageMax.setUnits("Volts (rms)")
_RpmSensorVoltageMin_Type = Gauge32
_RpmSensorVoltageMin_Object = MibTableColumn
rpmSensorVoltageMin = _RpmSensorVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 10, 1, 8),
    _RpmSensorVoltageMin_Type()
)
rpmSensorVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorVoltageMin.setStatus("current")
if mibBuilder.loadTexts:
    rpmSensorVoltageMin.setUnits("Volts (rms)")
_RpmSensorVoltagePeak_Type = Gauge32
_RpmSensorVoltagePeak_Object = MibTableColumn
rpmSensorVoltagePeak = _RpmSensorVoltagePeak_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 10, 1, 9),
    _RpmSensorVoltagePeak_Type()
)
rpmSensorVoltagePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorVoltagePeak.setStatus("current")
if mibBuilder.loadTexts:
    rpmSensorVoltagePeak.setUnits("Volts")
_RpmSensorCurrent_Type = Gauge32
_RpmSensorCurrent_Object = MibTableColumn
rpmSensorCurrent = _RpmSensorCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 10, 1, 10),
    _RpmSensorCurrent_Type()
)
rpmSensorCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorCurrent.setStatus("current")
if mibBuilder.loadTexts:
    rpmSensorCurrent.setUnits("0.1 Amps (rms)")
_RpmSensorRealPower_Type = Gauge32
_RpmSensorRealPower_Object = MibTableColumn
rpmSensorRealPower = _RpmSensorRealPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 10, 1, 11),
    _RpmSensorRealPower_Type()
)
rpmSensorRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorRealPower.setStatus("current")
if mibBuilder.loadTexts:
    rpmSensorRealPower.setUnits("Watts")
_RpmSensorApparentPower_Type = Gauge32
_RpmSensorApparentPower_Object = MibTableColumn
rpmSensorApparentPower = _RpmSensorApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 10, 1, 12),
    _RpmSensorApparentPower_Type()
)
rpmSensorApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    rpmSensorApparentPower.setUnits("Volt-Amps")
_RpmSensorPowerFactor_Type = Gauge32
_RpmSensorPowerFactor_Object = MibTableColumn
rpmSensorPowerFactor = _RpmSensorPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 10, 1, 13),
    _RpmSensorPowerFactor_Type()
)
rpmSensorPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    rpmSensorPowerFactor.setUnits("%")
_RpmSensorOutlet1_Type = Gauge32
_RpmSensorOutlet1_Object = MibTableColumn
rpmSensorOutlet1 = _RpmSensorOutlet1_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 10, 1, 14),
    _RpmSensorOutlet1_Type()
)
rpmSensorOutlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorOutlet1.setStatus("current")
_RpmSensorOutlet2_Type = Gauge32
_RpmSensorOutlet2_Object = MibTableColumn
rpmSensorOutlet2 = _RpmSensorOutlet2_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 10, 1, 15),
    _RpmSensorOutlet2_Type()
)
rpmSensorOutlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorOutlet2.setStatus("current")
_A2dSensorTable_Object = MibTable
a2dSensorTable = _A2dSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 11)
)
if mibBuilder.loadTexts:
    a2dSensorTable.setStatus("current")
_A2DSensorEntry_Object = MibTableRow
a2DSensorEntry = _A2DSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 11, 1)
)
a2DSensorEntry.setIndexNames(
    (0, "GEIST-V4-MIB", "a2dSensorIndex"),
)
if mibBuilder.loadTexts:
    a2DSensorEntry.setStatus("current")


class _A2dSensorIndex_Type(Integer32):
    """Custom type a2dSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_A2dSensorIndex_Type.__name__ = "Integer32"
_A2dSensorIndex_Object = MibTableColumn
a2dSensorIndex = _A2dSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 11, 1, 1),
    _A2dSensorIndex_Type()
)
a2dSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2dSensorIndex.setStatus("current")
_A2dSensorSerial_Type = DisplayString
_A2dSensorSerial_Object = MibTableColumn
a2dSensorSerial = _A2dSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 11, 1, 2),
    _A2dSensorSerial_Type()
)
a2dSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2dSensorSerial.setStatus("current")
_A2dSensorName_Type = DisplayString
_A2dSensorName_Object = MibTableColumn
a2dSensorName = _A2dSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 11, 1, 3),
    _A2dSensorName_Type()
)
a2dSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2dSensorName.setStatus("current")
_A2dSensorAvail_Type = Gauge32
_A2dSensorAvail_Object = MibTableColumn
a2dSensorAvail = _A2dSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 11, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 11, 1, 5),
    _A2dSensorValue_Type()
)
a2dSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2dSensorValue.setStatus("current")
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767)
)
_TrapPrefix_ObjectIdentity = ObjectIdentity
trapPrefix = _TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0)
)

# Managed Objects groups


# Notification objects

internalTestNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10101)
)
if mibBuilder.loadTexts:
    internalTestNOTIFY.setStatus(
        "current"
    )

internalAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10204)
)
internalAvailNOTIFY.setObjects(
    ("GEIST-V4-MIB", "internalAvail")
)
if mibBuilder.loadTexts:
    internalAvailNOTIFY.setStatus(
        "current"
    )

internalTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10205)
)
internalTempNOTIFY.setObjects(
      *(("GEIST-V4-MIB", "internalTemp"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    internalTempNOTIFY.setStatus(
        "current"
    )

internalHumidityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10206)
)
internalHumidityNOTIFY.setObjects(
    ("GEIST-V4-MIB", "internalHumidity")
)
if mibBuilder.loadTexts:
    internalHumidityNOTIFY.setStatus(
        "current"
    )

internalDewPointNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10207)
)
internalDewPointNOTIFY.setObjects(
      *(("GEIST-V4-MIB", "internalDewPoint"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    internalDewPointNOTIFY.setStatus(
        "current"
    )

tempSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10404)
)
tempSensorAvailNOTIFY.setObjects(
    ("GEIST-V4-MIB", "tempSensorAvail")
)
if mibBuilder.loadTexts:
    tempSensorAvailNOTIFY.setStatus(
        "current"
    )

tempSensorTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10405)
)
tempSensorTempNOTIFY.setObjects(
      *(("GEIST-V4-MIB", "tempSensorTemp"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    tempSensorTempNOTIFY.setStatus(
        "current"
    )

airFlowSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10504)
)
airFlowSensorAvailNOTIFY.setObjects(
    ("GEIST-V4-MIB", "airFlowSensorAvail")
)
if mibBuilder.loadTexts:
    airFlowSensorAvailNOTIFY.setStatus(
        "current"
    )

airFlowSensorTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10505)
)
airFlowSensorTempNOTIFY.setObjects(
      *(("GEIST-V4-MIB", "airFlowSensorTemp"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    airFlowSensorTempNOTIFY.setStatus(
        "current"
    )

airFlowSensorFlowNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10506)
)
airFlowSensorFlowNOTIFY.setObjects(
    ("GEIST-V4-MIB", "airFlowSensorFlow")
)
if mibBuilder.loadTexts:
    airFlowSensorFlowNOTIFY.setStatus(
        "current"
    )

airFlowSensorHumidityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10507)
)
airFlowSensorHumidityNOTIFY.setObjects(
    ("GEIST-V4-MIB", "airFlowSensorHumidity")
)
if mibBuilder.loadTexts:
    airFlowSensorHumidityNOTIFY.setStatus(
        "current"
    )

airFlowSensorDewPointNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10508)
)
airFlowSensorDewPointNOTIFY.setObjects(
      *(("GEIST-V4-MIB", "airFlowSensorDewPoint"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    airFlowSensorDewPointNOTIFY.setStatus(
        "current"
    )

dewPointSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10604)
)
dewPointSensorAvailNOTIFY.setObjects(
    ("GEIST-V4-MIB", "dewPointSensorAvail")
)
if mibBuilder.loadTexts:
    dewPointSensorAvailNOTIFY.setStatus(
        "current"
    )

dewPointSensorTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10605)
)
dewPointSensorTempNOTIFY.setObjects(
      *(("GEIST-V4-MIB", "dewPointSensorTemp"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    dewPointSensorTempNOTIFY.setStatus(
        "current"
    )

dewPointSensorHumidityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10606)
)
dewPointSensorHumidityNOTIFY.setObjects(
    ("GEIST-V4-MIB", "dewPointSensorHumidity")
)
if mibBuilder.loadTexts:
    dewPointSensorHumidityNOTIFY.setStatus(
        "current"
    )

dewPointSensorDewPointNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10607)
)
dewPointSensorDewPointNOTIFY.setObjects(
      *(("GEIST-V4-MIB", "dewPointSensorDewPoint"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    dewPointSensorDewPointNOTIFY.setStatus(
        "current"
    )

ccatSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10704)
)
ccatSensorAvailNOTIFY.setObjects(
    ("GEIST-V4-MIB", "ccatSensorAvail")
)
if mibBuilder.loadTexts:
    ccatSensorAvailNOTIFY.setStatus(
        "current"
    )

ccatSensorValueNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10705)
)
ccatSensorValueNOTIFY.setObjects(
      *(("GEIST-V4-MIB", "ccatSensorValue"),
        ("GEIST-V4-MIB", "ccatSensorType"))
)
if mibBuilder.loadTexts:
    ccatSensorValueNOTIFY.setStatus(
        "current"
    )

t3hdSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10804)
)
t3hdSensorAvailNOTIFY.setObjects(
    ("GEIST-V4-MIB", "t3hdSensorAvail")
)
if mibBuilder.loadTexts:
    t3hdSensorAvailNOTIFY.setStatus(
        "current"
    )

t3hdSensorIntTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10806)
)
t3hdSensorIntTempNOTIFY.setObjects(
      *(("GEIST-V4-MIB", "t3hdSensorIntTemp"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    t3hdSensorIntTempNOTIFY.setStatus(
        "current"
    )

t3hdSensorIntHumidityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10807)
)
t3hdSensorIntHumidityNOTIFY.setObjects(
    ("GEIST-V4-MIB", "t3hdSensorIntHumidity")
)
if mibBuilder.loadTexts:
    t3hdSensorIntHumidityNOTIFY.setStatus(
        "current"
    )

t3hdSensorIntDewPointNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10808)
)
t3hdSensorIntDewPointNOTIFY.setObjects(
      *(("GEIST-V4-MIB", "t3hdSensorIntDewPoint"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    t3hdSensorIntDewPointNOTIFY.setStatus(
        "current"
    )

t3hdSensorExtATempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10811)
)
t3hdSensorExtATempNOTIFY.setObjects(
      *(("GEIST-V4-MIB", "t3hdSensorExtATemp"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    t3hdSensorExtATempNOTIFY.setStatus(
        "current"
    )

t3hdSensorExtBTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10814)
)
t3hdSensorExtBTempNOTIFY.setObjects(
      *(("GEIST-V4-MIB", "t3hdSensorExtBTemp"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    t3hdSensorExtBTempNOTIFY.setStatus(
        "current"
    )

thdSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10904)
)
thdSensorAvailNOTIFY.setObjects(
    ("GEIST-V4-MIB", "thdSensorAvail")
)
if mibBuilder.loadTexts:
    thdSensorAvailNOTIFY.setStatus(
        "current"
    )

thdSensorTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10905)
)
thdSensorTempNOTIFY.setObjects(
      *(("GEIST-V4-MIB", "thdSensorTemp"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    thdSensorTempNOTIFY.setStatus(
        "current"
    )

thdSensorHumidityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10906)
)
thdSensorHumidityNOTIFY.setObjects(
    ("GEIST-V4-MIB", "thdSensorHumidity")
)
if mibBuilder.loadTexts:
    thdSensorHumidityNOTIFY.setStatus(
        "current"
    )

thdSensorDewPointNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 10907)
)
thdSensorDewPointNOTIFY.setObjects(
      *(("GEIST-V4-MIB", "thdSensorDewPoint"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    thdSensorDewPointNOTIFY.setStatus(
        "current"
    )

rpmSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 11004)
)
rpmSensorAvailNOTIFY.setObjects(
    ("GEIST-V4-MIB", "rpmSensorAvail")
)
if mibBuilder.loadTexts:
    rpmSensorAvailNOTIFY.setStatus(
        "current"
    )

rpmSensorEnergyNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 11005)
)
rpmSensorEnergyNOTIFY.setObjects(
    ("GEIST-V4-MIB", "rpmSensorEnergy")
)
if mibBuilder.loadTexts:
    rpmSensorEnergyNOTIFY.setStatus(
        "current"
    )

rpmSensorVoltageNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 11006)
)
rpmSensorVoltageNOTIFY.setObjects(
    ("GEIST-V4-MIB", "rpmSensorVoltage")
)
if mibBuilder.loadTexts:
    rpmSensorVoltageNOTIFY.setStatus(
        "current"
    )

rpmSensorVoltageMaxNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 11007)
)
rpmSensorVoltageMaxNOTIFY.setObjects(
    ("GEIST-V4-MIB", "rpmSensorVoltageMax")
)
if mibBuilder.loadTexts:
    rpmSensorVoltageMaxNOTIFY.setStatus(
        "current"
    )

rpmSensorVoltageMinNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 11008)
)
rpmSensorVoltageMinNOTIFY.setObjects(
    ("GEIST-V4-MIB", "rpmSensorVoltageMin")
)
if mibBuilder.loadTexts:
    rpmSensorVoltageMinNOTIFY.setStatus(
        "current"
    )

rpmSensorVoltagePeakNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 11009)
)
rpmSensorVoltagePeakNOTIFY.setObjects(
    ("GEIST-V4-MIB", "rpmSensorVoltagePeak")
)
if mibBuilder.loadTexts:
    rpmSensorVoltagePeakNOTIFY.setStatus(
        "current"
    )

rpmSensorCurrentNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 11010)
)
rpmSensorCurrentNOTIFY.setObjects(
    ("GEIST-V4-MIB", "rpmSensorCurrent")
)
if mibBuilder.loadTexts:
    rpmSensorCurrentNOTIFY.setStatus(
        "current"
    )

rpmSensorRealPowerNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 11011)
)
rpmSensorRealPowerNOTIFY.setObjects(
    ("GEIST-V4-MIB", "rpmSensorRealPower")
)
if mibBuilder.loadTexts:
    rpmSensorRealPowerNOTIFY.setStatus(
        "current"
    )

rpmSensorApparentPowerNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 11012)
)
rpmSensorApparentPowerNOTIFY.setObjects(
    ("GEIST-V4-MIB", "rpmSensorApparentPower")
)
if mibBuilder.loadTexts:
    rpmSensorApparentPowerNOTIFY.setStatus(
        "current"
    )

rpmSensorPowerFactorNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 11013)
)
rpmSensorPowerFactorNOTIFY.setObjects(
    ("GEIST-V4-MIB", "rpmSensorPowerFactor")
)
if mibBuilder.loadTexts:
    rpmSensorPowerFactorNOTIFY.setStatus(
        "current"
    )

a2dSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 11104)
)
a2dSensorAvailNOTIFY.setObjects(
    ("GEIST-V4-MIB", "a2dSensorAvail")
)
if mibBuilder.loadTexts:
    a2dSensorAvailNOTIFY.setStatus(
        "current"
    )

a2dSensorValueNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 11105)
)
a2dSensorValueNOTIFY.setObjects(
    ("GEIST-V4-MIB", "a2dSensorValue")
)
if mibBuilder.loadTexts:
    a2dSensorValueNOTIFY.setStatus(
        "current"
    )

internalAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20204)
)
internalAvailCLEAR.setObjects(
    ("GEIST-V4-MIB", "internalAvail")
)
if mibBuilder.loadTexts:
    internalAvailCLEAR.setStatus(
        "current"
    )

internalTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20205)
)
internalTempCLEAR.setObjects(
      *(("GEIST-V4-MIB", "internalTemp"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    internalTempCLEAR.setStatus(
        "current"
    )

internalHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20206)
)
internalHumidityCLEAR.setObjects(
    ("GEIST-V4-MIB", "internalHumidity")
)
if mibBuilder.loadTexts:
    internalHumidityCLEAR.setStatus(
        "current"
    )

internalDewPointCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20207)
)
internalDewPointCLEAR.setObjects(
      *(("GEIST-V4-MIB", "internalDewPoint"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    internalDewPointCLEAR.setStatus(
        "current"
    )

tempSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20404)
)
tempSensorAvailCLEAR.setObjects(
    ("GEIST-V4-MIB", "tempSensorAvail")
)
if mibBuilder.loadTexts:
    tempSensorAvailCLEAR.setStatus(
        "current"
    )

tempSensorTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20405)
)
tempSensorTempCLEAR.setObjects(
      *(("GEIST-V4-MIB", "tempSensorTemp"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    tempSensorTempCLEAR.setStatus(
        "current"
    )

airFlowSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20504)
)
airFlowSensorAvailCLEAR.setObjects(
    ("GEIST-V4-MIB", "airFlowSensorAvail")
)
if mibBuilder.loadTexts:
    airFlowSensorAvailCLEAR.setStatus(
        "current"
    )

airFlowSensorTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20505)
)
airFlowSensorTempCLEAR.setObjects(
      *(("GEIST-V4-MIB", "airFlowSensorTemp"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    airFlowSensorTempCLEAR.setStatus(
        "current"
    )

airFlowSensorFlowCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20506)
)
airFlowSensorFlowCLEAR.setObjects(
    ("GEIST-V4-MIB", "airFlowSensorFlow")
)
if mibBuilder.loadTexts:
    airFlowSensorFlowCLEAR.setStatus(
        "current"
    )

airFlowSensorHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20507)
)
airFlowSensorHumidityCLEAR.setObjects(
    ("GEIST-V4-MIB", "airFlowSensorHumidity")
)
if mibBuilder.loadTexts:
    airFlowSensorHumidityCLEAR.setStatus(
        "current"
    )

airFlowSensorDewPointCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20508)
)
airFlowSensorDewPointCLEAR.setObjects(
      *(("GEIST-V4-MIB", "airFlowSensorDewPoint"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    airFlowSensorDewPointCLEAR.setStatus(
        "current"
    )

dewPointSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20604)
)
dewPointSensorAvailCLEAR.setObjects(
    ("GEIST-V4-MIB", "dewPointSensorAvail")
)
if mibBuilder.loadTexts:
    dewPointSensorAvailCLEAR.setStatus(
        "current"
    )

dewPointSensorTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20605)
)
dewPointSensorTempCLEAR.setObjects(
      *(("GEIST-V4-MIB", "dewPointSensorTemp"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    dewPointSensorTempCLEAR.setStatus(
        "current"
    )

dewPointSensorHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20606)
)
dewPointSensorHumidityCLEAR.setObjects(
    ("GEIST-V4-MIB", "dewPointSensorHumidity")
)
if mibBuilder.loadTexts:
    dewPointSensorHumidityCLEAR.setStatus(
        "current"
    )

dewPointSensorDewPointCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20607)
)
dewPointSensorDewPointCLEAR.setObjects(
      *(("GEIST-V4-MIB", "dewPointSensorDewPoint"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    dewPointSensorDewPointCLEAR.setStatus(
        "current"
    )

ccatSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20704)
)
ccatSensorAvailCLEAR.setObjects(
    ("GEIST-V4-MIB", "ccatSensorAvail")
)
if mibBuilder.loadTexts:
    ccatSensorAvailCLEAR.setStatus(
        "current"
    )

ccatSensorValueCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20705)
)
ccatSensorValueCLEAR.setObjects(
      *(("GEIST-V4-MIB", "ccatSensorValue"),
        ("GEIST-V4-MIB", "ccatSensorType"))
)
if mibBuilder.loadTexts:
    ccatSensorValueCLEAR.setStatus(
        "current"
    )

t3hdSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20804)
)
t3hdSensorAvailCLEAR.setObjects(
    ("GEIST-V4-MIB", "t3hdSensorAvail")
)
if mibBuilder.loadTexts:
    t3hdSensorAvailCLEAR.setStatus(
        "current"
    )

t3hdSensorIntTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20806)
)
t3hdSensorIntTempCLEAR.setObjects(
      *(("GEIST-V4-MIB", "t3hdSensorIntTemp"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    t3hdSensorIntTempCLEAR.setStatus(
        "current"
    )

t3hdSensorIntHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20807)
)
t3hdSensorIntHumidityCLEAR.setObjects(
    ("GEIST-V4-MIB", "t3hdSensorIntHumidity")
)
if mibBuilder.loadTexts:
    t3hdSensorIntHumidityCLEAR.setStatus(
        "current"
    )

t3hdSensorIntDewPointCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20808)
)
t3hdSensorIntDewPointCLEAR.setObjects(
      *(("GEIST-V4-MIB", "t3hdSensorIntDewPoint"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    t3hdSensorIntDewPointCLEAR.setStatus(
        "current"
    )

t3hdSensorExtATempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20811)
)
t3hdSensorExtATempCLEAR.setObjects(
      *(("GEIST-V4-MIB", "t3hdSensorExtATemp"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    t3hdSensorExtATempCLEAR.setStatus(
        "current"
    )

t3hdSensorExtBTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20814)
)
t3hdSensorExtBTempCLEAR.setObjects(
      *(("GEIST-V4-MIB", "t3hdSensorExtBTemp"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    t3hdSensorExtBTempCLEAR.setStatus(
        "current"
    )

thdSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20904)
)
thdSensorAvailCLEAR.setObjects(
    ("GEIST-V4-MIB", "thdSensorAvail")
)
if mibBuilder.loadTexts:
    thdSensorAvailCLEAR.setStatus(
        "current"
    )

thdSensorTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20905)
)
thdSensorTempCLEAR.setObjects(
      *(("GEIST-V4-MIB", "thdSensorTemp"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    thdSensorTempCLEAR.setStatus(
        "current"
    )

thdSensorHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20906)
)
thdSensorHumidityCLEAR.setObjects(
    ("GEIST-V4-MIB", "thdSensorHumidity")
)
if mibBuilder.loadTexts:
    thdSensorHumidityCLEAR.setStatus(
        "current"
    )

thdSensorDewPointCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 20907)
)
thdSensorDewPointCLEAR.setObjects(
      *(("GEIST-V4-MIB", "thdSensorDewPoint"),
        ("GEIST-V4-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    thdSensorDewPointCLEAR.setStatus(
        "current"
    )

rpmSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 21004)
)
rpmSensorAvailCLEAR.setObjects(
    ("GEIST-V4-MIB", "rpmSensorAvail")
)
if mibBuilder.loadTexts:
    rpmSensorAvailCLEAR.setStatus(
        "current"
    )

rpmSensorEnergyCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 21005)
)
rpmSensorEnergyCLEAR.setObjects(
    ("GEIST-V4-MIB", "rpmSensorEnergy")
)
if mibBuilder.loadTexts:
    rpmSensorEnergyCLEAR.setStatus(
        "current"
    )

rpmSensorVoltageCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 21006)
)
rpmSensorVoltageCLEAR.setObjects(
    ("GEIST-V4-MIB", "rpmSensorVoltage")
)
if mibBuilder.loadTexts:
    rpmSensorVoltageCLEAR.setStatus(
        "current"
    )

rpmSensorVoltageMaxCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 21007)
)
rpmSensorVoltageMaxCLEAR.setObjects(
    ("GEIST-V4-MIB", "rpmSensorVoltageMax")
)
if mibBuilder.loadTexts:
    rpmSensorVoltageMaxCLEAR.setStatus(
        "current"
    )

rpmSensorVoltageMinCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 21008)
)
rpmSensorVoltageMinCLEAR.setObjects(
    ("GEIST-V4-MIB", "rpmSensorVoltageMin")
)
if mibBuilder.loadTexts:
    rpmSensorVoltageMinCLEAR.setStatus(
        "current"
    )

rpmSensorVoltagePeakCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 21009)
)
rpmSensorVoltagePeakCLEAR.setObjects(
    ("GEIST-V4-MIB", "rpmSensorVoltagePeak")
)
if mibBuilder.loadTexts:
    rpmSensorVoltagePeakCLEAR.setStatus(
        "current"
    )

rpmSensorCurrentCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 21010)
)
rpmSensorCurrentCLEAR.setObjects(
    ("GEIST-V4-MIB", "rpmSensorCurrent")
)
if mibBuilder.loadTexts:
    rpmSensorCurrentCLEAR.setStatus(
        "current"
    )

rpmSensorRealPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 21011)
)
rpmSensorRealPowerCLEAR.setObjects(
    ("GEIST-V4-MIB", "rpmSensorRealPower")
)
if mibBuilder.loadTexts:
    rpmSensorRealPowerCLEAR.setStatus(
        "current"
    )

rpmSensorApparentPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 21012)
)
rpmSensorApparentPowerCLEAR.setObjects(
    ("GEIST-V4-MIB", "rpmSensorApparentPower")
)
if mibBuilder.loadTexts:
    rpmSensorApparentPowerCLEAR.setStatus(
        "current"
    )

rpmSensorPowerFactorCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 21013)
)
rpmSensorPowerFactorCLEAR.setObjects(
    ("GEIST-V4-MIB", "rpmSensorPowerFactor")
)
if mibBuilder.loadTexts:
    rpmSensorPowerFactorCLEAR.setStatus(
        "current"
    )

a2dSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 21104)
)
a2dSensorAvailCLEAR.setObjects(
    ("GEIST-V4-MIB", "a2dSensorAvail")
)
if mibBuilder.loadTexts:
    a2dSensorAvailCLEAR.setStatus(
        "current"
    )

a2dSensorValueCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 1, 32767, 0, 21105)
)
a2dSensorValueCLEAR.setObjects(
    ("GEIST-V4-MIB", "a2dSensorValue")
)
if mibBuilder.loadTexts:
    a2dSensorValueCLEAR.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GEIST-V4-MIB",
    **{"geist": geist,
       "blackbird": blackbird,
       "watchdog100": watchdog100,
       "deviceInfo": deviceInfo,
       "productTitle": productTitle,
       "productVersion": productVersion,
       "productFriendlyName": productFriendlyName,
       "productMacAddress": productMacAddress,
       "productUrl": productUrl,
       "deviceCount": deviceCount,
       "temperatureUnits": temperatureUnits,
       "internalTable": internalTable,
       "internalEntry": internalEntry,
       "internalIndex": internalIndex,
       "internalSerial": internalSerial,
       "internalName": internalName,
       "internalAvail": internalAvail,
       "internalTemp": internalTemp,
       "internalHumidity": internalHumidity,
       "internalDewPoint": internalDewPoint,
       "tempSensorTable": tempSensorTable,
       "tempSensorEntry": tempSensorEntry,
       "tempSensorIndex": tempSensorIndex,
       "tempSensorSerial": tempSensorSerial,
       "tempSensorName": tempSensorName,
       "tempSensorAvail": tempSensorAvail,
       "tempSensorTemp": tempSensorTemp,
       "airFlowSensorTable": airFlowSensorTable,
       "airFlowSensorEntry": airFlowSensorEntry,
       "airFlowSensorIndex": airFlowSensorIndex,
       "airFlowSensorSerial": airFlowSensorSerial,
       "airFlowSensorName": airFlowSensorName,
       "airFlowSensorAvail": airFlowSensorAvail,
       "airFlowSensorTemp": airFlowSensorTemp,
       "airFlowSensorFlow": airFlowSensorFlow,
       "airFlowSensorHumidity": airFlowSensorHumidity,
       "airFlowSensorDewPoint": airFlowSensorDewPoint,
       "dewPointSensorTable": dewPointSensorTable,
       "dewPointSensorEntry": dewPointSensorEntry,
       "dewPointSensorIndex": dewPointSensorIndex,
       "dewPointSensorSerial": dewPointSensorSerial,
       "dewPointSensorName": dewPointSensorName,
       "dewPointSensorAvail": dewPointSensorAvail,
       "dewPointSensorTemp": dewPointSensorTemp,
       "dewPointSensorHumidity": dewPointSensorHumidity,
       "dewPointSensorDewPoint": dewPointSensorDewPoint,
       "ccatSensorTable": ccatSensorTable,
       "ccatSensorEntry": ccatSensorEntry,
       "ccatSensorIndex": ccatSensorIndex,
       "ccatSensorSerial": ccatSensorSerial,
       "ccatSensorName": ccatSensorName,
       "ccatSensorAvail": ccatSensorAvail,
       "ccatSensorValue": ccatSensorValue,
       "ccatSensorType": ccatSensorType,
       "ccatSensorDescription": ccatSensorDescription,
       "t3hdSensorTable": t3hdSensorTable,
       "t3hdSensorEntry": t3hdSensorEntry,
       "t3hdSensorIndex": t3hdSensorIndex,
       "t3hdSensorSerial": t3hdSensorSerial,
       "t3hdSensorName": t3hdSensorName,
       "t3hdSensorAvail": t3hdSensorAvail,
       "t3hdSensorIntName": t3hdSensorIntName,
       "t3hdSensorIntTemp": t3hdSensorIntTemp,
       "t3hdSensorIntHumidity": t3hdSensorIntHumidity,
       "t3hdSensorIntDewPoint": t3hdSensorIntDewPoint,
       "t3hdSensorExtAAvail": t3hdSensorExtAAvail,
       "t3hdSensorExtAName": t3hdSensorExtAName,
       "t3hdSensorExtATemp": t3hdSensorExtATemp,
       "t3hdSensorExtBAvail": t3hdSensorExtBAvail,
       "t3hdSensorExtBName": t3hdSensorExtBName,
       "t3hdSensorExtBTemp": t3hdSensorExtBTemp,
       "thdSensorTable": thdSensorTable,
       "thdSensorEntry": thdSensorEntry,
       "thdSensorIndex": thdSensorIndex,
       "thdSensorSerial": thdSensorSerial,
       "thdSensorName": thdSensorName,
       "thdSensorAvail": thdSensorAvail,
       "thdSensorTemp": thdSensorTemp,
       "thdSensorHumidity": thdSensorHumidity,
       "thdSensorDewPoint": thdSensorDewPoint,
       "rpmSensorTable": rpmSensorTable,
       "rpmSensorEntry": rpmSensorEntry,
       "rpmSensorIndex": rpmSensorIndex,
       "rpmSensorSerial": rpmSensorSerial,
       "rpmSensorName": rpmSensorName,
       "rpmSensorAvail": rpmSensorAvail,
       "rpmSensorEnergy": rpmSensorEnergy,
       "rpmSensorVoltage": rpmSensorVoltage,
       "rpmSensorVoltageMax": rpmSensorVoltageMax,
       "rpmSensorVoltageMin": rpmSensorVoltageMin,
       "rpmSensorVoltagePeak": rpmSensorVoltagePeak,
       "rpmSensorCurrent": rpmSensorCurrent,
       "rpmSensorRealPower": rpmSensorRealPower,
       "rpmSensorApparentPower": rpmSensorApparentPower,
       "rpmSensorPowerFactor": rpmSensorPowerFactor,
       "rpmSensorOutlet1": rpmSensorOutlet1,
       "rpmSensorOutlet2": rpmSensorOutlet2,
       "a2dSensorTable": a2dSensorTable,
       "a2DSensorEntry": a2DSensorEntry,
       "a2dSensorIndex": a2dSensorIndex,
       "a2dSensorSerial": a2dSensorSerial,
       "a2dSensorName": a2dSensorName,
       "a2dSensorAvail": a2dSensorAvail,
       "a2dSensorValue": a2dSensorValue,
       "trap": trap,
       "trapPrefix": trapPrefix,
       "internalTestNOTIFY": internalTestNOTIFY,
       "internalAvailNOTIFY": internalAvailNOTIFY,
       "internalTempNOTIFY": internalTempNOTIFY,
       "internalHumidityNOTIFY": internalHumidityNOTIFY,
       "internalDewPointNOTIFY": internalDewPointNOTIFY,
       "tempSensorAvailNOTIFY": tempSensorAvailNOTIFY,
       "tempSensorTempNOTIFY": tempSensorTempNOTIFY,
       "airFlowSensorAvailNOTIFY": airFlowSensorAvailNOTIFY,
       "airFlowSensorTempNOTIFY": airFlowSensorTempNOTIFY,
       "airFlowSensorFlowNOTIFY": airFlowSensorFlowNOTIFY,
       "airFlowSensorHumidityNOTIFY": airFlowSensorHumidityNOTIFY,
       "airFlowSensorDewPointNOTIFY": airFlowSensorDewPointNOTIFY,
       "dewPointSensorAvailNOTIFY": dewPointSensorAvailNOTIFY,
       "dewPointSensorTempNOTIFY": dewPointSensorTempNOTIFY,
       "dewPointSensorHumidityNOTIFY": dewPointSensorHumidityNOTIFY,
       "dewPointSensorDewPointNOTIFY": dewPointSensorDewPointNOTIFY,
       "ccatSensorAvailNOTIFY": ccatSensorAvailNOTIFY,
       "ccatSensorValueNOTIFY": ccatSensorValueNOTIFY,
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
       "rpmSensorAvailNOTIFY": rpmSensorAvailNOTIFY,
       "rpmSensorEnergyNOTIFY": rpmSensorEnergyNOTIFY,
       "rpmSensorVoltageNOTIFY": rpmSensorVoltageNOTIFY,
       "rpmSensorVoltageMaxNOTIFY": rpmSensorVoltageMaxNOTIFY,
       "rpmSensorVoltageMinNOTIFY": rpmSensorVoltageMinNOTIFY,
       "rpmSensorVoltagePeakNOTIFY": rpmSensorVoltagePeakNOTIFY,
       "rpmSensorCurrentNOTIFY": rpmSensorCurrentNOTIFY,
       "rpmSensorRealPowerNOTIFY": rpmSensorRealPowerNOTIFY,
       "rpmSensorApparentPowerNOTIFY": rpmSensorApparentPowerNOTIFY,
       "rpmSensorPowerFactorNOTIFY": rpmSensorPowerFactorNOTIFY,
       "a2dSensorAvailNOTIFY": a2dSensorAvailNOTIFY,
       "a2dSensorValueNOTIFY": a2dSensorValueNOTIFY,
       "internalAvailCLEAR": internalAvailCLEAR,
       "internalTempCLEAR": internalTempCLEAR,
       "internalHumidityCLEAR": internalHumidityCLEAR,
       "internalDewPointCLEAR": internalDewPointCLEAR,
       "tempSensorAvailCLEAR": tempSensorAvailCLEAR,
       "tempSensorTempCLEAR": tempSensorTempCLEAR,
       "airFlowSensorAvailCLEAR": airFlowSensorAvailCLEAR,
       "airFlowSensorTempCLEAR": airFlowSensorTempCLEAR,
       "airFlowSensorFlowCLEAR": airFlowSensorFlowCLEAR,
       "airFlowSensorHumidityCLEAR": airFlowSensorHumidityCLEAR,
       "airFlowSensorDewPointCLEAR": airFlowSensorDewPointCLEAR,
       "dewPointSensorAvailCLEAR": dewPointSensorAvailCLEAR,
       "dewPointSensorTempCLEAR": dewPointSensorTempCLEAR,
       "dewPointSensorHumidityCLEAR": dewPointSensorHumidityCLEAR,
       "dewPointSensorDewPointCLEAR": dewPointSensorDewPointCLEAR,
       "ccatSensorAvailCLEAR": ccatSensorAvailCLEAR,
       "ccatSensorValueCLEAR": ccatSensorValueCLEAR,
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
       "rpmSensorAvailCLEAR": rpmSensorAvailCLEAR,
       "rpmSensorEnergyCLEAR": rpmSensorEnergyCLEAR,
       "rpmSensorVoltageCLEAR": rpmSensorVoltageCLEAR,
       "rpmSensorVoltageMaxCLEAR": rpmSensorVoltageMaxCLEAR,
       "rpmSensorVoltageMinCLEAR": rpmSensorVoltageMinCLEAR,
       "rpmSensorVoltagePeakCLEAR": rpmSensorVoltagePeakCLEAR,
       "rpmSensorCurrentCLEAR": rpmSensorCurrentCLEAR,
       "rpmSensorRealPowerCLEAR": rpmSensorRealPowerCLEAR,
       "rpmSensorApparentPowerCLEAR": rpmSensorApparentPowerCLEAR,
       "rpmSensorPowerFactorCLEAR": rpmSensorPowerFactorCLEAR,
       "a2dSensorAvailCLEAR": a2dSensorAvailCLEAR,
       "a2dSensorValueCLEAR": a2dSensorValueCLEAR}
)
