# SNMP MIB module (DIGIPDU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\planet\DIGIPDU-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:48 2025
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

smart = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10456, 3)
)
if mibBuilder.loadTexts:
    smart.setRevisions(
        ("2009-04-16 16:27",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Digipdu_ObjectIdentity = ObjectIdentity
digipdu = _Digipdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10456)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10456, 3, 1)
)


class _ProductModel_Type(DisplayString):
    """Custom type productModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_ProductModel_Type.__name__ = "DisplayString"
_ProductModel_Object = MibScalar
productModel = _ProductModel_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 1, 1),
    _ProductModel_Type()
)
productModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productModel.setStatus("current")


class _ProductPartNumber_Type(DisplayString):
    """Custom type productPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProductPartNumber_Type.__name__ = "DisplayString"
_ProductPartNumber_Object = MibScalar
productPartNumber = _ProductPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 1, 2),
    _ProductPartNumber_Type()
)
productPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productPartNumber.setStatus("current")


class _ProductSerialNumber_Type(DisplayString):
    """Custom type productSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProductSerialNumber_Type.__name__ = "DisplayString"
_ProductSerialNumber_Object = MibScalar
productSerialNumber = _ProductSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 1, 3),
    _ProductSerialNumber_Type()
)
productSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productSerialNumber.setStatus("current")


class _ProductFirmwareVersion_Type(DisplayString):
    """Custom type productFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProductFirmwareVersion_Type.__name__ = "DisplayString"
_ProductFirmwareVersion_Object = MibScalar
productFirmwareVersion = _ProductFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 1, 4),
    _ProductFirmwareVersion_Type()
)
productFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productFirmwareVersion.setStatus("current")


class _ProductTemperatureKind_Type(Integer32):
    """Custom type productTemperatureKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ProductTemperatureKind_Type.__name__ = "Integer32"
_ProductTemperatureKind_Object = MibScalar
productTemperatureKind = _ProductTemperatureKind_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 1, 11),
    _ProductTemperatureKind_Type()
)
productTemperatureKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productTemperatureKind.setStatus("current")
_ProductResetDetector_Type = DisplayString
_ProductResetDetector_Object = MibScalar
productResetDetector = _ProductResetDetector_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 1, 21),
    _ProductResetDetector_Type()
)
productResetDetector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productResetDetector.setStatus("current")
_DeviceTable_ObjectIdentity = ObjectIdentity
deviceTable = _DeviceTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10456, 3, 2)
)


class _DeviceATSKind_Type(Integer32):
    """Custom type deviceATSKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_DeviceATSKind_Type.__name__ = "Integer32"
_DeviceATSKind_Object = MibScalar
deviceATSKind = _DeviceATSKind_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 2, 1),
    _DeviceATSKind_Type()
)
deviceATSKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceATSKind.setStatus("current")


class _DeviceInFeedTotal_Type(Integer32):
    """Custom type deviceInFeedTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_DeviceInFeedTotal_Type.__name__ = "Integer32"
_DeviceInFeedTotal_Object = MibScalar
deviceInFeedTotal = _DeviceInFeedTotal_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 2, 2),
    _DeviceInFeedTotal_Type()
)
deviceInFeedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInFeedTotal.setStatus("current")


class _DeviceInFeedKind_Type(Integer32):
    """Custom type deviceInFeedKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DeviceInFeedKind_Type.__name__ = "Integer32"
_DeviceInFeedKind_Object = MibScalar
deviceInFeedKind = _DeviceInFeedKind_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 2, 3),
    _DeviceInFeedKind_Type()
)
deviceInFeedKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInFeedKind.setStatus("current")


class _DeviceInFeedBranch_Type(Integer32):
    """Custom type deviceInFeedBranch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DeviceInFeedBranch_Type.__name__ = "Integer32"
_DeviceInFeedBranch_Object = MibScalar
deviceInFeedBranch = _DeviceInFeedBranch_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 2, 4),
    _DeviceInFeedBranch_Type()
)
deviceInFeedBranch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInFeedBranch.setStatus("current")


class _DeviceOutTotal_Type(Integer32):
    """Custom type deviceOutTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_DeviceOutTotal_Type.__name__ = "Integer32"
_DeviceOutTotal_Object = MibScalar
deviceOutTotal = _DeviceOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 2, 5),
    _DeviceOutTotal_Type()
)
deviceOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOutTotal.setStatus("current")


class _DeviceOutKind_Type(Integer32):
    """Custom type deviceOutKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DeviceOutKind_Type.__name__ = "Integer32"
_DeviceOutKind_Object = MibScalar
deviceOutKind = _DeviceOutKind_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 2, 6),
    _DeviceOutKind_Type()
)
deviceOutKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOutKind.setStatus("current")


class _DeviceInbuiltTempTotal_Type(Integer32):
    """Custom type deviceInbuiltTempTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DeviceInbuiltTempTotal_Type.__name__ = "Integer32"
_DeviceInbuiltTempTotal_Object = MibScalar
deviceInbuiltTempTotal = _DeviceInbuiltTempTotal_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 2, 7),
    _DeviceInbuiltTempTotal_Type()
)
deviceInbuiltTempTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInbuiltTempTotal.setStatus("current")


class _DeviceExtendTemperatureTotal_Type(Integer32):
    """Custom type deviceExtendTemperatureTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_DeviceExtendTemperatureTotal_Type.__name__ = "Integer32"
_DeviceExtendTemperatureTotal_Object = MibScalar
deviceExtendTemperatureTotal = _DeviceExtendTemperatureTotal_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 2, 8),
    _DeviceExtendTemperatureTotal_Type()
)
deviceExtendTemperatureTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceExtendTemperatureTotal.setStatus("current")


class _DeviceExtendRHTotal_Type(Integer32):
    """Custom type deviceExtendRHTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_DeviceExtendRHTotal_Type.__name__ = "Integer32"
_DeviceExtendRHTotal_Object = MibScalar
deviceExtendRHTotal = _DeviceExtendRHTotal_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 2, 9),
    _DeviceExtendRHTotal_Type()
)
deviceExtendRHTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceExtendRHTotal.setStatus("current")


class _DevicePDUTotal_Type(Integer32):
    """Custom type devicePDUTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DevicePDUTotal_Type.__name__ = "Integer32"
_DevicePDUTotal_Object = MibScalar
devicePDUTotal = _DevicePDUTotal_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 2, 10),
    _DevicePDUTotal_Type()
)
devicePDUTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePDUTotal.setStatus("current")


class _DeviceInputTotal_Type(Integer32):
    """Custom type deviceInputTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DeviceInputTotal_Type.__name__ = "Integer32"
_DeviceInputTotal_Object = MibScalar
deviceInputTotal = _DeviceInputTotal_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 2, 11),
    _DeviceInputTotal_Type()
)
deviceInputTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInputTotal.setStatus("current")


class _DeviceUPS_Type(Integer32):
    """Custom type deviceUPS based on Integer32"""
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


_DeviceUPS_Type.__name__ = "Integer32"
_DeviceUPS_Object = MibScalar
deviceUPS = _DeviceUPS_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 2, 12),
    _DeviceUPS_Type()
)
deviceUPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUPS.setStatus("current")


class _DeviceDaisyChain_Type(Integer32):
    """Custom type deviceDaisyChain based on Integer32"""
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


_DeviceDaisyChain_Type.__name__ = "Integer32"
_DeviceDaisyChain_Object = MibScalar
deviceDaisyChain = _DeviceDaisyChain_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 2, 13),
    _DeviceDaisyChain_Type()
)
deviceDaisyChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDaisyChain.setStatus("current")


class _DeviceUnitTotal_Type(Integer32):
    """Custom type deviceUnitTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DeviceUnitTotal_Type.__name__ = "Integer32"
_DeviceUnitTotal_Object = MibScalar
deviceUnitTotal = _DeviceUnitTotal_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 2, 20),
    _DeviceUnitTotal_Type()
)
deviceUnitTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUnitTotal.setStatus("current")
_DeviceUnitTable_Object = MibTable
deviceUnitTable = _DeviceUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 2, 21)
)
if mibBuilder.loadTexts:
    deviceUnitTable.setStatus("current")
_DeviceUnitEntry_Object = MibTableRow
deviceUnitEntry = _DeviceUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 2, 21, 1)
)
deviceUnitEntry.setIndexNames(
    (0, "DIGIPDU-MIB", "deviceUnitIndex"),
)
if mibBuilder.loadTexts:
    deviceUnitEntry.setStatus("current")


class _DeviceUnitIndex_Type(Integer32):
    """Custom type deviceUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DeviceUnitIndex_Type.__name__ = "Integer32"
_DeviceUnitIndex_Object = MibTableColumn
deviceUnitIndex = _DeviceUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 2, 21, 1, 1),
    _DeviceUnitIndex_Type()
)
deviceUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUnitIndex.setStatus("current")
_DeviceUnitStatus_Type = Integer32
_DeviceUnitStatus_Object = MibTableColumn
deviceUnitStatus = _DeviceUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 2, 21, 1, 2),
    _DeviceUnitStatus_Type()
)
deviceUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUnitStatus.setStatus("current")
_DeviceUnitInfeedTotal_Type = Integer32
_DeviceUnitInfeedTotal_Object = MibTableColumn
deviceUnitInfeedTotal = _DeviceUnitInfeedTotal_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 2, 21, 1, 3),
    _DeviceUnitInfeedTotal_Type()
)
deviceUnitInfeedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUnitInfeedTotal.setStatus("current")
_DeviceUnitOutTotal_Type = Integer32
_DeviceUnitOutTotal_Object = MibTableColumn
deviceUnitOutTotal = _DeviceUnitOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 2, 21, 1, 4),
    _DeviceUnitOutTotal_Type()
)
deviceUnitOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUnitOutTotal.setStatus("current")
_PeripheralTables_ObjectIdentity = ObjectIdentity
peripheralTables = _PeripheralTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3)
)
_ATSTable_Object = MibTable
aTSTable = _ATSTable_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 1)
)
if mibBuilder.loadTexts:
    aTSTable.setStatus("current")
_ATSEntry_Object = MibTableRow
aTSEntry = _ATSEntry_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 1, 1)
)
aTSEntry.setIndexNames(
    (0, "DIGIPDU-MIB", "aTSIndex"),
)
if mibBuilder.loadTexts:
    aTSEntry.setStatus("current")


class _ATSIndex_Type(Integer32):
    """Custom type aTSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ATSIndex_Type.__name__ = "Integer32"
_ATSIndex_Object = MibTableColumn
aTSIndex = _ATSIndex_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 1, 1, 1),
    _ATSIndex_Type()
)
aTSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aTSIndex.setStatus("current")
_ATSStatus_Type = Integer32
_ATSStatus_Object = MibTableColumn
aTSStatus = _ATSStatus_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 1, 1, 2),
    _ATSStatus_Type()
)
aTSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aTSStatus.setStatus("current")
_ATSVoltage_Type = Integer32
_ATSVoltage_Object = MibTableColumn
aTSVoltage = _ATSVoltage_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 1, 1, 3),
    _ATSVoltage_Type()
)
aTSVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aTSVoltage.setStatus("current")
_ATSFrequency_Type = Integer32
_ATSFrequency_Object = MibTableColumn
aTSFrequency = _ATSFrequency_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 1, 1, 4),
    _ATSFrequency_Type()
)
aTSFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aTSFrequency.setStatus("current")
_InFeedTable_Object = MibTable
inFeedTable = _InFeedTable_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2)
)
if mibBuilder.loadTexts:
    inFeedTable.setStatus("current")
_InFeedEntry_Object = MibTableRow
inFeedEntry = _InFeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1)
)
inFeedEntry.setIndexNames(
    (0, "DIGIPDU-MIB", "inFeedIndex"),
)
if mibBuilder.loadTexts:
    inFeedEntry.setStatus("current")


class _InFeedIndex_Type(Integer32):
    """Custom type inFeedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_InFeedIndex_Type.__name__ = "Integer32"
_InFeedIndex_Object = MibTableColumn
inFeedIndex = _InFeedIndex_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 1),
    _InFeedIndex_Type()
)
inFeedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inFeedIndex.setStatus("current")
_InFeedStatus_Type = Integer32
_InFeedStatus_Object = MibTableColumn
inFeedStatus = _InFeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 2),
    _InFeedStatus_Type()
)
inFeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inFeedStatus.setStatus("current")
_InFeedVoltage_Type = Integer32
_InFeedVoltage_Object = MibTableColumn
inFeedVoltage = _InFeedVoltage_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 3),
    _InFeedVoltage_Type()
)
inFeedVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inFeedVoltage.setStatus("current")
_InFeedFrequency_Type = Integer32
_InFeedFrequency_Object = MibTableColumn
inFeedFrequency = _InFeedFrequency_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 4),
    _InFeedFrequency_Type()
)
inFeedFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inFeedFrequency.setStatus("current")
_InFeedCurrent_Type = Integer32
_InFeedCurrent_Object = MibTableColumn
inFeedCurrent = _InFeedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 5),
    _InFeedCurrent_Type()
)
inFeedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inFeedCurrent.setStatus("current")
_InFeedPowerLoad_Type = Integer32
_InFeedPowerLoad_Object = MibTableColumn
inFeedPowerLoad = _InFeedPowerLoad_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 6),
    _InFeedPowerLoad_Type()
)
inFeedPowerLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inFeedPowerLoad.setStatus("current")
_InFeedPowerFactor_Type = Integer32
_InFeedPowerFactor_Object = MibTableColumn
inFeedPowerFactor = _InFeedPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 7),
    _InFeedPowerFactor_Type()
)
inFeedPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inFeedPowerFactor.setStatus("current")
_InFeedPowerEnergy_Type = Integer32
_InFeedPowerEnergy_Object = MibTableColumn
inFeedPowerEnergy = _InFeedPowerEnergy_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 8),
    _InFeedPowerEnergy_Type()
)
inFeedPowerEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inFeedPowerEnergy.setStatus("current")
_InFeedOverLoad_Type = Integer32
_InFeedOverLoad_Object = MibTableColumn
inFeedOverLoad = _InFeedOverLoad_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 9),
    _InFeedOverLoad_Type()
)
inFeedOverLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inFeedOverLoad.setStatus("current")
_InFeedHighWarning_Type = Integer32
_InFeedHighWarning_Object = MibTableColumn
inFeedHighWarning = _InFeedHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 10),
    _InFeedHighWarning_Type()
)
inFeedHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inFeedHighWarning.setStatus("current")
_InFeedLowWarning_Type = Integer32
_InFeedLowWarning_Object = MibTableColumn
inFeedLowWarning = _InFeedLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 11),
    _InFeedLowWarning_Type()
)
inFeedLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inFeedLowWarning.setStatus("current")
_InFeedBranch_Type = Integer32
_InFeedBranch_Object = MibTableColumn
inFeedBranch = _InFeedBranch_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 12),
    _InFeedBranch_Type()
)
inFeedBranch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inFeedBranch.setStatus("current")
_InFeedBranch1Current_Type = Integer32
_InFeedBranch1Current_Object = MibTableColumn
inFeedBranch1Current = _InFeedBranch1Current_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 13),
    _InFeedBranch1Current_Type()
)
inFeedBranch1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inFeedBranch1Current.setStatus("current")
_InFeedBranch1PowerLoad_Type = Integer32
_InFeedBranch1PowerLoad_Object = MibTableColumn
inFeedBranch1PowerLoad = _InFeedBranch1PowerLoad_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 14),
    _InFeedBranch1PowerLoad_Type()
)
inFeedBranch1PowerLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inFeedBranch1PowerLoad.setStatus("current")
_InFeedBranch1PowerFactor_Type = Integer32
_InFeedBranch1PowerFactor_Object = MibTableColumn
inFeedBranch1PowerFactor = _InFeedBranch1PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 15),
    _InFeedBranch1PowerFactor_Type()
)
inFeedBranch1PowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inFeedBranch1PowerFactor.setStatus("current")
_InFeedBranch1OverLoad_Type = Integer32
_InFeedBranch1OverLoad_Object = MibTableColumn
inFeedBranch1OverLoad = _InFeedBranch1OverLoad_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 16),
    _InFeedBranch1OverLoad_Type()
)
inFeedBranch1OverLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inFeedBranch1OverLoad.setStatus("current")
_InFeedBranch1HighWarning_Type = Integer32
_InFeedBranch1HighWarning_Object = MibTableColumn
inFeedBranch1HighWarning = _InFeedBranch1HighWarning_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 17),
    _InFeedBranch1HighWarning_Type()
)
inFeedBranch1HighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inFeedBranch1HighWarning.setStatus("current")
_InFeedBranch1LowWarning_Type = Integer32
_InFeedBranch1LowWarning_Object = MibTableColumn
inFeedBranch1LowWarning = _InFeedBranch1LowWarning_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 18),
    _InFeedBranch1LowWarning_Type()
)
inFeedBranch1LowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inFeedBranch1LowWarning.setStatus("current")
_InFeedBranch2Current_Type = Integer32
_InFeedBranch2Current_Object = MibTableColumn
inFeedBranch2Current = _InFeedBranch2Current_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 19),
    _InFeedBranch2Current_Type()
)
inFeedBranch2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inFeedBranch2Current.setStatus("current")
_InFeedBranch2PowerLoad_Type = Integer32
_InFeedBranch2PowerLoad_Object = MibTableColumn
inFeedBranch2PowerLoad = _InFeedBranch2PowerLoad_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 20),
    _InFeedBranch2PowerLoad_Type()
)
inFeedBranch2PowerLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inFeedBranch2PowerLoad.setStatus("current")
_InFeedBranch2PowerFactor_Type = Integer32
_InFeedBranch2PowerFactor_Object = MibTableColumn
inFeedBranch2PowerFactor = _InFeedBranch2PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 21),
    _InFeedBranch2PowerFactor_Type()
)
inFeedBranch2PowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inFeedBranch2PowerFactor.setStatus("current")
_InFeedBranch2OverLoad_Type = Integer32
_InFeedBranch2OverLoad_Object = MibTableColumn
inFeedBranch2OverLoad = _InFeedBranch2OverLoad_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 22),
    _InFeedBranch2OverLoad_Type()
)
inFeedBranch2OverLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inFeedBranch2OverLoad.setStatus("current")
_InFeedBranch2HighWarning_Type = Integer32
_InFeedBranch2HighWarning_Object = MibTableColumn
inFeedBranch2HighWarning = _InFeedBranch2HighWarning_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 23),
    _InFeedBranch2HighWarning_Type()
)
inFeedBranch2HighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inFeedBranch2HighWarning.setStatus("current")
_InFeedBranch2LowWarning_Type = Integer32
_InFeedBranch2LowWarning_Object = MibTableColumn
inFeedBranch2LowWarning = _InFeedBranch2LowWarning_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 2, 1, 24),
    _InFeedBranch2LowWarning_Type()
)
inFeedBranch2LowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inFeedBranch2LowWarning.setStatus("current")
_OutTable_Object = MibTable
outTable = _OutTable_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 3)
)
if mibBuilder.loadTexts:
    outTable.setStatus("current")
_OutEntry_Object = MibTableRow
outEntry = _OutEntry_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 3, 1)
)
outEntry.setIndexNames(
    (0, "DIGIPDU-MIB", "outIndex"),
)
if mibBuilder.loadTexts:
    outEntry.setStatus("current")


class _OutIndex_Type(Integer32):
    """Custom type outIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_OutIndex_Type.__name__ = "Integer32"
_OutIndex_Object = MibTableColumn
outIndex = _OutIndex_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 3, 1, 1),
    _OutIndex_Type()
)
outIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outIndex.setStatus("current")
_OutComputerStatus_Type = Integer32
_OutComputerStatus_Object = MibTableColumn
outComputerStatus = _OutComputerStatus_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 3, 1, 2),
    _OutComputerStatus_Type()
)
outComputerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outComputerStatus.setStatus("current")
_OutCurrentStatus_Type = Integer32
_OutCurrentStatus_Object = MibTableColumn
outCurrentStatus = _OutCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 3, 1, 3),
    _OutCurrentStatus_Type()
)
outCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outCurrentStatus.setStatus("current")


class _OutSwitchStatus_Type(Integer32):
    """Custom type outSwitchStatus based on Integer32"""
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
        *(("off", 0),
          ("on", 1),
          ("off-act", 2),
          ("on-act", 3))
    )


_OutSwitchStatus_Type.__name__ = "Integer32"
_OutSwitchStatus_Object = MibTableColumn
outSwitchStatus = _OutSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 3, 1, 4),
    _OutSwitchStatus_Type()
)
outSwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outSwitchStatus.setStatus("current")


class _OutSwitchCtrl_Type(Integer32):
    """Custom type outSwitchCtrl based on Integer32"""
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
        *(("none", 0),
          ("ctrl-on", 1),
          ("ctrl-off", 2),
          ("ctrl-reboot", 3),
          ("ctrl-on-off", 4))
    )


_OutSwitchCtrl_Type.__name__ = "Integer32"
_OutSwitchCtrl_Object = MibTableColumn
outSwitchCtrl = _OutSwitchCtrl_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 3, 1, 5),
    _OutSwitchCtrl_Type()
)
outSwitchCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outSwitchCtrl.setStatus("current")
_OutVoltage_Type = Integer32
_OutVoltage_Object = MibTableColumn
outVoltage = _OutVoltage_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 3, 1, 6),
    _OutVoltage_Type()
)
outVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outVoltage.setStatus("current")
_OutCurrent_Type = Integer32
_OutCurrent_Object = MibTableColumn
outCurrent = _OutCurrent_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 3, 1, 7),
    _OutCurrent_Type()
)
outCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outCurrent.setStatus("current")
_OutPowerFactor_Type = Integer32
_OutPowerFactor_Object = MibTableColumn
outPowerFactor = _OutPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 3, 1, 8),
    _OutPowerFactor_Type()
)
outPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outPowerFactor.setStatus("current")
_OutPowerLoad_Type = Integer32
_OutPowerLoad_Object = MibTableColumn
outPowerLoad = _OutPowerLoad_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 3, 1, 9),
    _OutPowerLoad_Type()
)
outPowerLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outPowerLoad.setStatus("current")
_OutOverload_Type = Integer32
_OutOverload_Object = MibTableColumn
outOverload = _OutOverload_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 3, 1, 10),
    _OutOverload_Type()
)
outOverload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outOverload.setStatus("current")
_OutHighWarning_Type = Integer32
_OutHighWarning_Object = MibTableColumn
outHighWarning = _OutHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 3, 1, 11),
    _OutHighWarning_Type()
)
outHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outHighWarning.setStatus("current")
_OutLowWarning_Type = Integer32
_OutLowWarning_Object = MibTableColumn
outLowWarning = _OutLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 3, 1, 12),
    _OutLowWarning_Type()
)
outLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outLowWarning.setStatus("current")
_PduTables_Object = MibTable
pduTables = _PduTables_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4)
)
if mibBuilder.loadTexts:
    pduTables.setStatus("current")
_PduEntry_Object = MibTableRow
pduEntry = _PduEntry_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1)
)
pduEntry.setIndexNames(
    (0, "DIGIPDU-MIB", "pduIndex"),
)
if mibBuilder.loadTexts:
    pduEntry.setStatus("current")


class _PduIndex_Type(Integer32):
    """Custom type pduIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PduIndex_Type.__name__ = "Integer32"
_PduIndex_Object = MibTableColumn
pduIndex = _PduIndex_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 1),
    _PduIndex_Type()
)
pduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduIndex.setStatus("current")
_PduModel_Type = DisplayString
_PduModel_Object = MibTableColumn
pduModel = _PduModel_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 2),
    _PduModel_Type()
)
pduModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduModel.setStatus("current")


class _PduMonitor_Type(Integer32):
    """Custom type pduMonitor based on Integer32"""
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


_PduMonitor_Type.__name__ = "Integer32"
_PduMonitor_Object = MibTableColumn
pduMonitor = _PduMonitor_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 3),
    _PduMonitor_Type()
)
pduMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduMonitor.setStatus("current")


class _PduStatus_Type(Integer32):
    """Custom type pduStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1),
          ("warning", 2))
    )


_PduStatus_Type.__name__ = "Integer32"
_PduStatus_Object = MibTableColumn
pduStatus = _PduStatus_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 4),
    _PduStatus_Type()
)
pduStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatus.setStatus("current")
_PduVoltage_Type = Integer32
_PduVoltage_Object = MibTableColumn
pduVoltage = _PduVoltage_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 5),
    _PduVoltage_Type()
)
pduVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduVoltage.setStatus("current")
_PduFrequency_Type = Integer32
_PduFrequency_Object = MibTableColumn
pduFrequency = _PduFrequency_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 6),
    _PduFrequency_Type()
)
pduFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduFrequency.setStatus("current")
_PduCurrent_Type = Integer32
_PduCurrent_Object = MibTableColumn
pduCurrent = _PduCurrent_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 7),
    _PduCurrent_Type()
)
pduCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCurrent.setStatus("current")
_PduPowerLoad_Type = Integer32
_PduPowerLoad_Object = MibTableColumn
pduPowerLoad = _PduPowerLoad_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 8),
    _PduPowerLoad_Type()
)
pduPowerLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPowerLoad.setStatus("current")
_PduPowerFactor_Type = Integer32
_PduPowerFactor_Object = MibTableColumn
pduPowerFactor = _PduPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 9),
    _PduPowerFactor_Type()
)
pduPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPowerFactor.setStatus("current")
_PduPowerEnergy_Type = Integer32
_PduPowerEnergy_Object = MibTableColumn
pduPowerEnergy = _PduPowerEnergy_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 10),
    _PduPowerEnergy_Type()
)
pduPowerEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPowerEnergy.setStatus("current")
_PduOverload_Type = Integer32
_PduOverload_Object = MibTableColumn
pduOverload = _PduOverload_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 11),
    _PduOverload_Type()
)
pduOverload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOverload.setStatus("current")
_PduHighWarning_Type = Integer32
_PduHighWarning_Object = MibTableColumn
pduHighWarning = _PduHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 12),
    _PduHighWarning_Type()
)
pduHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduHighWarning.setStatus("current")
_PduLowWarning_Type = Integer32
_PduLowWarning_Object = MibTableColumn
pduLowWarning = _PduLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 13),
    _PduLowWarning_Type()
)
pduLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduLowWarning.setStatus("current")
_PduBranch_Type = Integer32
_PduBranch_Object = MibTableColumn
pduBranch = _PduBranch_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 14),
    _PduBranch_Type()
)
pduBranch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBranch.setStatus("current")
_PduBranch1Current_Type = Integer32
_PduBranch1Current_Object = MibTableColumn
pduBranch1Current = _PduBranch1Current_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 15),
    _PduBranch1Current_Type()
)
pduBranch1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBranch1Current.setStatus("current")
_PduBranch1Overload_Type = Integer32
_PduBranch1Overload_Object = MibTableColumn
pduBranch1Overload = _PduBranch1Overload_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 16),
    _PduBranch1Overload_Type()
)
pduBranch1Overload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduBranch1Overload.setStatus("current")
_PduBranch1HighWarning_Type = Integer32
_PduBranch1HighWarning_Object = MibTableColumn
pduBranch1HighWarning = _PduBranch1HighWarning_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 17),
    _PduBranch1HighWarning_Type()
)
pduBranch1HighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduBranch1HighWarning.setStatus("current")
_PduBranch1LowWarning_Type = Integer32
_PduBranch1LowWarning_Object = MibTableColumn
pduBranch1LowWarning = _PduBranch1LowWarning_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 18),
    _PduBranch1LowWarning_Type()
)
pduBranch1LowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduBranch1LowWarning.setStatus("current")
_PduBranch2Current_Type = Integer32
_PduBranch2Current_Object = MibTableColumn
pduBranch2Current = _PduBranch2Current_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 19),
    _PduBranch2Current_Type()
)
pduBranch2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBranch2Current.setStatus("current")
_PduBranch2Overload_Type = Integer32
_PduBranch2Overload_Object = MibTableColumn
pduBranch2Overload = _PduBranch2Overload_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 20),
    _PduBranch2Overload_Type()
)
pduBranch2Overload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduBranch2Overload.setStatus("current")
_PduBranch2HighWarning_Type = Integer32
_PduBranch2HighWarning_Object = MibTableColumn
pduBranch2HighWarning = _PduBranch2HighWarning_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 21),
    _PduBranch2HighWarning_Type()
)
pduBranch2HighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduBranch2HighWarning.setStatus("current")
_PduBranch2LowWarning_Type = Integer32
_PduBranch2LowWarning_Object = MibTableColumn
pduBranch2LowWarning = _PduBranch2LowWarning_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 4, 1, 22),
    _PduBranch2LowWarning_Type()
)
pduBranch2LowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduBranch2LowWarning.setStatus("current")
_InbuiltTemperatureTable_Object = MibTable
inbuiltTemperatureTable = _InbuiltTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 5)
)
if mibBuilder.loadTexts:
    inbuiltTemperatureTable.setStatus("current")
_InbuiltTemperatureEntry_Object = MibTableRow
inbuiltTemperatureEntry = _InbuiltTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 5, 1)
)
inbuiltTemperatureEntry.setIndexNames(
    (0, "DIGIPDU-MIB", "inbuiltTemperatureIndex"),
)
if mibBuilder.loadTexts:
    inbuiltTemperatureEntry.setStatus("current")


class _InbuiltTemperatureIndex_Type(Integer32):
    """Custom type inbuiltTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_InbuiltTemperatureIndex_Type.__name__ = "Integer32"
_InbuiltTemperatureIndex_Object = MibTableColumn
inbuiltTemperatureIndex = _InbuiltTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 5, 1, 1),
    _InbuiltTemperatureIndex_Type()
)
inbuiltTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbuiltTemperatureIndex.setStatus("current")


class _InbuiltTemperatureStatus_Type(Integer32):
    """Custom type inbuiltTemperatureStatus based on Integer32"""
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


_InbuiltTemperatureStatus_Type.__name__ = "Integer32"
_InbuiltTemperatureStatus_Object = MibTableColumn
inbuiltTemperatureStatus = _InbuiltTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 5, 1, 2),
    _InbuiltTemperatureStatus_Type()
)
inbuiltTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbuiltTemperatureStatus.setStatus("current")
_InbuiltTemperature_Type = Integer32
_InbuiltTemperature_Object = MibTableColumn
inbuiltTemperature = _InbuiltTemperature_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 5, 1, 3),
    _InbuiltTemperature_Type()
)
inbuiltTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbuiltTemperature.setStatus("current")
_InbuiltTemperatureHighWarning_Type = Integer32
_InbuiltTemperatureHighWarning_Object = MibTableColumn
inbuiltTemperatureHighWarning = _InbuiltTemperatureHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 5, 1, 4),
    _InbuiltTemperatureHighWarning_Type()
)
inbuiltTemperatureHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbuiltTemperatureHighWarning.setStatus("current")
_InbuiltTemperatureLowWarning_Type = Integer32
_InbuiltTemperatureLowWarning_Object = MibTableColumn
inbuiltTemperatureLowWarning = _InbuiltTemperatureLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 5, 1, 5),
    _InbuiltTemperatureLowWarning_Type()
)
inbuiltTemperatureLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbuiltTemperatureLowWarning.setStatus("current")
_ExtendTemperatureTable_Object = MibTable
extendTemperatureTable = _ExtendTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 6)
)
if mibBuilder.loadTexts:
    extendTemperatureTable.setStatus("current")
_ExtendTemperatureEntry_Object = MibTableRow
extendTemperatureEntry = _ExtendTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 6, 1)
)
extendTemperatureEntry.setIndexNames(
    (0, "DIGIPDU-MIB", "extendTemperatureIndex"),
)
if mibBuilder.loadTexts:
    extendTemperatureEntry.setStatus("current")


class _ExtendTemperatureIndex_Type(Integer32):
    """Custom type extendTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ExtendTemperatureIndex_Type.__name__ = "Integer32"
_ExtendTemperatureIndex_Object = MibTableColumn
extendTemperatureIndex = _ExtendTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 6, 1, 1),
    _ExtendTemperatureIndex_Type()
)
extendTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendTemperatureIndex.setStatus("current")
_ExtendTemperatureDeviceId_Type = Integer32
_ExtendTemperatureDeviceId_Object = MibTableColumn
extendTemperatureDeviceId = _ExtendTemperatureDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 6, 1, 2),
    _ExtendTemperatureDeviceId_Type()
)
extendTemperatureDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendTemperatureDeviceId.setStatus("current")
_ExtendTemperaturePort_Type = Integer32
_ExtendTemperaturePort_Object = MibTableColumn
extendTemperaturePort = _ExtendTemperaturePort_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 6, 1, 3),
    _ExtendTemperaturePort_Type()
)
extendTemperaturePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendTemperaturePort.setStatus("current")


class _ExtendTemperatureMonitor_Type(Integer32):
    """Custom type extendTemperatureMonitor based on Integer32"""
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


_ExtendTemperatureMonitor_Type.__name__ = "Integer32"
_ExtendTemperatureMonitor_Object = MibTableColumn
extendTemperatureMonitor = _ExtendTemperatureMonitor_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 6, 1, 4),
    _ExtendTemperatureMonitor_Type()
)
extendTemperatureMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendTemperatureMonitor.setStatus("current")


class _ExtendTemperatureStatus_Type(Integer32):
    """Custom type extendTemperatureStatus based on Integer32"""
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


_ExtendTemperatureStatus_Type.__name__ = "Integer32"
_ExtendTemperatureStatus_Object = MibTableColumn
extendTemperatureStatus = _ExtendTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 6, 1, 5),
    _ExtendTemperatureStatus_Type()
)
extendTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendTemperatureStatus.setStatus("current")
_ExtendTemperature_Type = Integer32
_ExtendTemperature_Object = MibTableColumn
extendTemperature = _ExtendTemperature_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 6, 1, 6),
    _ExtendTemperature_Type()
)
extendTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendTemperature.setStatus("current")
_ExtendTemperatureHighWarning_Type = Integer32
_ExtendTemperatureHighWarning_Object = MibTableColumn
extendTemperatureHighWarning = _ExtendTemperatureHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 6, 1, 7),
    _ExtendTemperatureHighWarning_Type()
)
extendTemperatureHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendTemperatureHighWarning.setStatus("current")
_ExtendTemperatureLowWarning_Type = Integer32
_ExtendTemperatureLowWarning_Object = MibTableColumn
extendTemperatureLowWarning = _ExtendTemperatureLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 6, 1, 8),
    _ExtendTemperatureLowWarning_Type()
)
extendTemperatureLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendTemperatureLowWarning.setStatus("current")
_ExtendRHTable_Object = MibTable
extendRHTable = _ExtendRHTable_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 7)
)
if mibBuilder.loadTexts:
    extendRHTable.setStatus("current")
_ExtendRHEntry_Object = MibTableRow
extendRHEntry = _ExtendRHEntry_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 7, 1)
)
extendRHEntry.setIndexNames(
    (0, "DIGIPDU-MIB", "extendRHIndex"),
)
if mibBuilder.loadTexts:
    extendRHEntry.setStatus("current")


class _ExtendRHIndex_Type(Integer32):
    """Custom type extendRHIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ExtendRHIndex_Type.__name__ = "Integer32"
_ExtendRHIndex_Object = MibTableColumn
extendRHIndex = _ExtendRHIndex_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 7, 1, 1),
    _ExtendRHIndex_Type()
)
extendRHIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendRHIndex.setStatus("current")


class _ExtendRHDeviceId_Type(Integer32):
    """Custom type extendRHDeviceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ExtendRHDeviceId_Type.__name__ = "Integer32"
_ExtendRHDeviceId_Object = MibTableColumn
extendRHDeviceId = _ExtendRHDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 7, 1, 2),
    _ExtendRHDeviceId_Type()
)
extendRHDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendRHDeviceId.setStatus("current")


class _ExtendRHPort_Type(Integer32):
    """Custom type extendRHPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ExtendRHPort_Type.__name__ = "Integer32"
_ExtendRHPort_Object = MibTableColumn
extendRHPort = _ExtendRHPort_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 7, 1, 3),
    _ExtendRHPort_Type()
)
extendRHPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendRHPort.setStatus("current")


class _ExtendRHMonitor_Type(Integer32):
    """Custom type extendRHMonitor based on Integer32"""
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


_ExtendRHMonitor_Type.__name__ = "Integer32"
_ExtendRHMonitor_Object = MibTableColumn
extendRHMonitor = _ExtendRHMonitor_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 7, 1, 4),
    _ExtendRHMonitor_Type()
)
extendRHMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendRHMonitor.setStatus("current")


class _ExtendRHStatus_Type(Integer32):
    """Custom type extendRHStatus based on Integer32"""
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


_ExtendRHStatus_Type.__name__ = "Integer32"
_ExtendRHStatus_Object = MibTableColumn
extendRHStatus = _ExtendRHStatus_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 7, 1, 5),
    _ExtendRHStatus_Type()
)
extendRHStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendRHStatus.setStatus("current")
_ExtendRH_Type = Integer32
_ExtendRH_Object = MibTableColumn
extendRH = _ExtendRH_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 7, 1, 6),
    _ExtendRH_Type()
)
extendRH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendRH.setStatus("current")
_ExtendRHHighWarning_Type = Integer32
_ExtendRHHighWarning_Object = MibTableColumn
extendRHHighWarning = _ExtendRHHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 7, 1, 7),
    _ExtendRHHighWarning_Type()
)
extendRHHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendRHHighWarning.setStatus("current")
_ExtendRHLowWarning_Type = Integer32
_ExtendRHLowWarning_Object = MibTableColumn
extendRHLowWarning = _ExtendRHLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 7, 1, 8),
    _ExtendRHLowWarning_Type()
)
extendRHLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendRHLowWarning.setStatus("current")
_InputTable_Object = MibTable
inputTable = _InputTable_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 8)
)
if mibBuilder.loadTexts:
    inputTable.setStatus("current")
_InputEntry_Object = MibTableRow
inputEntry = _InputEntry_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 8, 1)
)
inputEntry.setIndexNames(
    (0, "DIGIPDU-MIB", "inputIndex"),
)
if mibBuilder.loadTexts:
    inputEntry.setStatus("current")


class _InputIndex_Type(Integer32):
    """Custom type inputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_InputIndex_Type.__name__ = "Integer32"
_InputIndex_Object = MibTableColumn
inputIndex = _InputIndex_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 8, 1, 1),
    _InputIndex_Type()
)
inputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputIndex.setStatus("current")
_InputStatus_Type = Integer32
_InputStatus_Object = MibTableColumn
inputStatus = _InputStatus_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 8, 1, 2),
    _InputStatus_Type()
)
inputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatus.setStatus("current")
_InputState_Type = Integer32
_InputState_Object = MibTableColumn
inputState = _InputState_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 8, 1, 3),
    _InputState_Type()
)
inputState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputState.setStatus("current")
_InputTimeout_Type = Integer32
_InputTimeout_Object = MibTableColumn
inputTimeout = _InputTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 8, 1, 4),
    _InputTimeout_Type()
)
inputTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputTimeout.setStatus("current")
_InputDefault_Type = Integer32
_InputDefault_Object = MibTableColumn
inputDefault = _InputDefault_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 8, 1, 5),
    _InputDefault_Type()
)
inputDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputDefault.setStatus("current")
_InputDetectTime_Type = DisplayString
_InputDetectTime_Object = MibTableColumn
inputDetectTime = _InputDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 8, 1, 6),
    _InputDetectTime_Type()
)
inputDetectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputDetectTime.setStatus("current")
_RfidReader_ObjectIdentity = ObjectIdentity
rfidReader = _RfidReader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 9)
)
_RfidCardNum_Type = DisplayString
_RfidCardNum_Object = MibScalar
rfidCardNum = _RfidCardNum_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 9, 1),
    _RfidCardNum_Type()
)
rfidCardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfidCardNum.setStatus("current")
_RfidDetectTime_Type = DisplayString
_RfidDetectTime_Object = MibScalar
rfidDetectTime = _RfidDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 9, 2),
    _RfidDetectTime_Type()
)
rfidDetectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfidDetectTime.setStatus("current")
_UPS_ObjectIdentity = ObjectIdentity
uPS = _UPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 10)
)
_UPSModel_Type = DisplayString
_UPSModel_Object = MibScalar
uPSModel = _UPSModel_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 10, 1),
    _UPSModel_Type()
)
uPSModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSModel.setStatus("current")
_UPSConnectStatus_Type = Integer32
_UPSConnectStatus_Object = MibScalar
uPSConnectStatus = _UPSConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 10, 2),
    _UPSConnectStatus_Type()
)
uPSConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSConnectStatus.setStatus("current")
_UPSFirmware_Type = DisplayString
_UPSFirmware_Object = MibScalar
uPSFirmware = _UPSFirmware_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 10, 3),
    _UPSFirmware_Type()
)
uPSFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSFirmware.setStatus("current")
_UPSSerial_Type = DisplayString
_UPSSerial_Object = MibScalar
uPSSerial = _UPSSerial_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 10, 4),
    _UPSSerial_Type()
)
uPSSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSSerial.setStatus("current")
_UPSTemperature_Type = Integer32
_UPSTemperature_Object = MibScalar
uPSTemperature = _UPSTemperature_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 10, 5),
    _UPSTemperature_Type()
)
uPSTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSTemperature.setStatus("current")
_UPSInputVoltage_Type = Integer32
_UPSInputVoltage_Object = MibScalar
uPSInputVoltage = _UPSInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 10, 6),
    _UPSInputVoltage_Type()
)
uPSInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSInputVoltage.setStatus("current")
_UPSOutputOnBattery_Type = Integer32
_UPSOutputOnBattery_Object = MibScalar
uPSOutputOnBattery = _UPSOutputOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 10, 7),
    _UPSOutputOnBattery_Type()
)
uPSOutputOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSOutputOnBattery.setStatus("current")
_UPSOutputVoltage_Type = Integer32
_UPSOutputVoltage_Object = MibScalar
uPSOutputVoltage = _UPSOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 10, 8),
    _UPSOutputVoltage_Type()
)
uPSOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSOutputVoltage.setStatus("current")
_UPSOutputFrequency_Type = Integer32
_UPSOutputFrequency_Object = MibScalar
uPSOutputFrequency = _UPSOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 10, 9),
    _UPSOutputFrequency_Type()
)
uPSOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSOutputFrequency.setStatus("current")
_UPSOutputCurrent_Type = Integer32
_UPSOutputCurrent_Object = MibScalar
uPSOutputCurrent = _UPSOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 10, 10),
    _UPSOutputCurrent_Type()
)
uPSOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSOutputCurrent.setStatus("current")
_UPSOutputLoad_Type = Integer32
_UPSOutputLoad_Object = MibScalar
uPSOutputLoad = _UPSOutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 10, 11),
    _UPSOutputLoad_Type()
)
uPSOutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSOutputLoad.setStatus("current")
_UPSOutputOverload_Type = Integer32
_UPSOutputOverload_Object = MibScalar
uPSOutputOverload = _UPSOutputOverload_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 10, 12),
    _UPSOutputOverload_Type()
)
uPSOutputOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSOutputOverload.setStatus("current")
_UPSBatteryDate_Type = DisplayString
_UPSBatteryDate_Object = MibScalar
uPSBatteryDate = _UPSBatteryDate_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 10, 13),
    _UPSBatteryDate_Type()
)
uPSBatteryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSBatteryDate.setStatus("current")
_UPSBatteryVoltage_Type = Integer32
_UPSBatteryVoltage_Object = MibScalar
uPSBatteryVoltage = _UPSBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 10, 14),
    _UPSBatteryVoltage_Type()
)
uPSBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSBatteryVoltage.setStatus("current")
_UPSBatteryLevel_Type = Integer32
_UPSBatteryLevel_Object = MibScalar
uPSBatteryLevel = _UPSBatteryLevel_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 10, 15),
    _UPSBatteryLevel_Type()
)
uPSBatteryLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSBatteryLevel.setStatus("current")
_UPSBatteryRunTime_Type = Integer32
_UPSBatteryRunTime_Object = MibScalar
uPSBatteryRunTime = _UPSBatteryRunTime_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 10, 16),
    _UPSBatteryRunTime_Type()
)
uPSBatteryRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSBatteryRunTime.setStatus("current")
_UPSBatteryLow_Type = Integer32
_UPSBatteryLow_Object = MibScalar
uPSBatteryLow = _UPSBatteryLow_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 10, 17),
    _UPSBatteryLow_Type()
)
uPSBatteryLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSBatteryLow.setStatus("current")
_UPSBatteryReplace_Type = Integer32
_UPSBatteryReplace_Object = MibScalar
uPSBatteryReplace = _UPSBatteryReplace_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 10, 18),
    _UPSBatteryReplace_Type()
)
uPSBatteryReplace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSBatteryReplace.setStatus("current")
_UPSUARTId_Type = Integer32
_UPSUARTId_Object = MibScalar
uPSUARTId = _UPSUARTId_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 10, 19),
    _UPSUARTId_Type()
)
uPSUARTId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSUARTId.setStatus("current")
_MicDetec_ObjectIdentity = ObjectIdentity
micDetec = _MicDetec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 11)
)
_MicDetectTimes_Type = Integer32
_MicDetectTimes_Object = MibScalar
micDetectTimes = _MicDetectTimes_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 11, 1),
    _MicDetectTimes_Type()
)
micDetectTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    micDetectTimes.setStatus("current")
_MicDetectPeriod_Type = Integer32
_MicDetectPeriod_Object = MibScalar
micDetectPeriod = _MicDetectPeriod_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 11, 2),
    _MicDetectPeriod_Type()
)
micDetectPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    micDetectPeriod.setStatus("current")
_MicLastDetectTime_Type = DisplayString
_MicLastDetectTime_Object = MibScalar
micLastDetectTime = _MicLastDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 11, 3),
    _MicLastDetectTime_Type()
)
micLastDetectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    micLastDetectTime.setStatus("current")
_VibrationDetec_ObjectIdentity = ObjectIdentity
vibrationDetec = _VibrationDetec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 12)
)
_VibrationDetectTimes_Type = Integer32
_VibrationDetectTimes_Object = MibScalar
vibrationDetectTimes = _VibrationDetectTimes_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 12, 1),
    _VibrationDetectTimes_Type()
)
vibrationDetectTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vibrationDetectTimes.setStatus("current")
_VibrationDetectPeriod_Type = Integer32
_VibrationDetectPeriod_Object = MibScalar
vibrationDetectPeriod = _VibrationDetectPeriod_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 12, 2),
    _VibrationDetectPeriod_Type()
)
vibrationDetectPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vibrationDetectPeriod.setStatus("current")
_VibrationLastDetectTime_Type = DisplayString
_VibrationLastDetectTime_Object = MibScalar
vibrationLastDetectTime = _VibrationLastDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 3, 12, 3),
    _VibrationLastDetectTime_Type()
)
vibrationLastDetectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vibrationLastDetectTime.setStatus("current")
_DataLogTable_ObjectIdentity = ObjectIdentity
dataLogTable = _DataLogTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10456, 3, 4)
)
_InFeedDataList_Type = DisplayString
_InFeedDataList_Object = MibScalar
inFeedDataList = _InFeedDataList_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 4, 1),
    _InFeedDataList_Type()
)
inFeedDataList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inFeedDataList.setStatus("current")
_OutDataList_Type = DisplayString
_OutDataList_Object = MibScalar
outDataList = _OutDataList_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 4, 2),
    _OutDataList_Type()
)
outDataList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outDataList.setStatus("current")
_PduDataList_Type = DisplayString
_PduDataList_Object = MibScalar
pduDataList = _PduDataList_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 4, 3),
    _PduDataList_Type()
)
pduDataList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduDataList.setStatus("current")
_SmartTraps_ObjectIdentity = ObjectIdentity
smartTraps = _SmartTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100)
)
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1)
)
_Arg_ObjectIdentity = ObjectIdentity
arg = _Arg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 2)
)
_TrapArg1_Type = Integer32
_TrapArg1_Object = MibScalar
trapArg1 = _TrapArg1_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 2, 1),
    _TrapArg1_Type()
)
trapArg1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapArg1.setStatus("current")
_TrapArg2_Type = Integer32
_TrapArg2_Object = MibScalar
trapArg2 = _TrapArg2_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 2, 2),
    _TrapArg2_Type()
)
trapArg2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapArg2.setStatus("current")
_TrapArg3_Type = Integer32
_TrapArg3_Object = MibScalar
trapArg3 = _TrapArg3_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 2, 3),
    _TrapArg3_Type()
)
trapArg3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapArg3.setStatus("current")
_TrapArg4_Type = Integer32
_TrapArg4_Object = MibScalar
trapArg4 = _TrapArg4_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 2, 4),
    _TrapArg4_Type()
)
trapArg4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapArg4.setStatus("current")
_TrapArg5_Type = Integer32
_TrapArg5_Object = MibScalar
trapArg5 = _TrapArg5_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 2, 5),
    _TrapArg5_Type()
)
trapArg5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapArg5.setStatus("current")
_TrapArg6_Type = Integer32
_TrapArg6_Object = MibScalar
trapArg6 = _TrapArg6_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 2, 6),
    _TrapArg6_Type()
)
trapArg6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapArg6.setStatus("current")
_TrapArg7_Type = Integer32
_TrapArg7_Object = MibScalar
trapArg7 = _TrapArg7_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 2, 7),
    _TrapArg7_Type()
)
trapArg7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapArg7.setStatus("current")
_TrapArg8_Type = Integer32
_TrapArg8_Object = MibScalar
trapArg8 = _TrapArg8_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 2, 8),
    _TrapArg8_Type()
)
trapArg8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapArg8.setStatus("current")
_TrapArg9_Type = Integer32
_TrapArg9_Object = MibScalar
trapArg9 = _TrapArg9_Object(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 2, 9),
    _TrapArg9_Type()
)
trapArg9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapArg9.setStatus("current")

# Managed Objects groups


# Notification objects

testTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 1)
)
testTrap.setObjects(
    ("DIGIPDU-MIB", "trapArg1")
)
if mibBuilder.loadTexts:
    testTrap.setStatus(
        "current"
    )

inFeedOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 101)
)
inFeedOverloadTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"))
)
if mibBuilder.loadTexts:
    inFeedOverloadTrap.setStatus(
        "current"
    )

inFeedHighCurrentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 102)
)
inFeedHighCurrentTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"))
)
if mibBuilder.loadTexts:
    inFeedHighCurrentTrap.setStatus(
        "current"
    )

inFeedLowCurrentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 103)
)
inFeedLowCurrentTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"))
)
if mibBuilder.loadTexts:
    inFeedLowCurrentTrap.setStatus(
        "current"
    )

inFeedBranchOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 104)
)
inFeedBranchOverloadTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"))
)
if mibBuilder.loadTexts:
    inFeedBranchOverloadTrap.setStatus(
        "current"
    )

inFeedBranchHighCurrentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 105)
)
inFeedBranchHighCurrentTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"))
)
if mibBuilder.loadTexts:
    inFeedBranchHighCurrentTrap.setStatus(
        "current"
    )

inFeedBranchLowCurrentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 106)
)
inFeedBranchLowCurrentTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"))
)
if mibBuilder.loadTexts:
    inFeedBranchLowCurrentTrap.setStatus(
        "current"
    )

outWebOperationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 201)
)
outWebOperationTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"))
)
if mibBuilder.loadTexts:
    outWebOperationTrap.setStatus(
        "current"
    )

outPanelOperationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 202)
)
outPanelOperationTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"))
)
if mibBuilder.loadTexts:
    outPanelOperationTrap.setStatus(
        "current"
    )

outAPIOperationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 203)
)
outAPIOperationTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"))
)
if mibBuilder.loadTexts:
    outAPIOperationTrap.setStatus(
        "current"
    )

outScheduleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 211)
)
outScheduleTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"),
        ("DIGIPDU-MIB", "trapArg6"),
        ("DIGIPDU-MIB", "trapArg7"),
        ("DIGIPDU-MIB", "trapArg8"),
        ("DIGIPDU-MIB", "trapArg9"))
)
if mibBuilder.loadTexts:
    outScheduleTrap.setStatus(
        "current"
    )

outScheduleErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 212)
)
outScheduleErrorTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"),
        ("DIGIPDU-MIB", "trapArg6"),
        ("DIGIPDU-MIB", "trapArg7"))
)
if mibBuilder.loadTexts:
    outScheduleErrorTrap.setStatus(
        "current"
    )

outPingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 221)
)
outPingTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"))
)
if mibBuilder.loadTexts:
    outPingTrap.setStatus(
        "current"
    )

outPingRebootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 222)
)
outPingRebootTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"))
)
if mibBuilder.loadTexts:
    outPingRebootTrap.setStatus(
        "current"
    )

outOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 231)
)
outOverloadTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"))
)
if mibBuilder.loadTexts:
    outOverloadTrap.setStatus(
        "current"
    )

outHighCurrentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 232)
)
outHighCurrentTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"))
)
if mibBuilder.loadTexts:
    outHighCurrentTrap.setStatus(
        "current"
    )

outLowCurrentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 233)
)
outLowCurrentTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"))
)
if mibBuilder.loadTexts:
    outLowCurrentTrap.setStatus(
        "current"
    )

outConditionCtrlTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 241)
)
outConditionCtrlTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"))
)
if mibBuilder.loadTexts:
    outConditionCtrlTrap.setStatus(
        "current"
    )

outUPSACFaultOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 311)
)
outUPSACFaultOffTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"))
)
if mibBuilder.loadTexts:
    outUPSACFaultOffTrap.setStatus(
        "current"
    )

outUPSBatteryLevelOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 312)
)
outUPSBatteryLevelOffTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"))
)
if mibBuilder.loadTexts:
    outUPSBatteryLevelOffTrap.setStatus(
        "current"
    )

outUPSBatteryLowOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 313)
)
outUPSBatteryLowOffTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"))
)
if mibBuilder.loadTexts:
    outUPSBatteryLowOffTrap.setStatus(
        "current"
    )

outUPSACRecoveryOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 314)
)
outUPSACRecoveryOnTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"))
)
if mibBuilder.loadTexts:
    outUPSACRecoveryOnTrap.setStatus(
        "current"
    )

outUPSBatteryLevelOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 315)
)
outUPSBatteryLevelOnTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"))
)
if mibBuilder.loadTexts:
    outUPSBatteryLevelOnTrap.setStatus(
        "current"
    )

outUPSBatteryLowRecoveryOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 316)
)
outUPSBatteryLowRecoveryOnTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"))
)
if mibBuilder.loadTexts:
    outUPSBatteryLowRecoveryOnTrap.setStatus(
        "current"
    )

pduConnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 401)
)
pduConnectTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"))
)
if mibBuilder.loadTexts:
    pduConnectTrap.setStatus(
        "current"
    )

pduOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 402)
)
pduOverloadTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"))
)
if mibBuilder.loadTexts:
    pduOverloadTrap.setStatus(
        "current"
    )

pduHighCurrentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 403)
)
pduHighCurrentTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"))
)
if mibBuilder.loadTexts:
    pduHighCurrentTrap.setStatus(
        "current"
    )

pduLowCurrentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 404)
)
pduLowCurrentTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"))
)
if mibBuilder.loadTexts:
    pduLowCurrentTrap.setStatus(
        "current"
    )

pduBranchOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 405)
)
pduBranchOverloadTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"))
)
if mibBuilder.loadTexts:
    pduBranchOverloadTrap.setStatus(
        "current"
    )

pduBranchHighCurrentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 406)
)
pduBranchHighCurrentTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"))
)
if mibBuilder.loadTexts:
    pduBranchHighCurrentTrap.setStatus(
        "current"
    )

pduBranchLowCurrentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 407)
)
pduBranchLowCurrentTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"))
)
if mibBuilder.loadTexts:
    pduBranchLowCurrentTrap.setStatus(
        "current"
    )

inbuiltTemperatureHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 501)
)
inbuiltTemperatureHighTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"))
)
if mibBuilder.loadTexts:
    inbuiltTemperatureHighTrap.setStatus(
        "current"
    )

inbuiltTemperatureLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 502)
)
inbuiltTemperatureLowTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"))
)
if mibBuilder.loadTexts:
    inbuiltTemperatureLowTrap.setStatus(
        "current"
    )

envConnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 511)
)
envConnectTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"))
)
if mibBuilder.loadTexts:
    envConnectTrap.setStatus(
        "current"
    )

envTemperatureConnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 512)
)
envTemperatureConnectTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"))
)
if mibBuilder.loadTexts:
    envTemperatureConnectTrap.setStatus(
        "current"
    )

envTemperatureHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 513)
)
envTemperatureHighTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"),
        ("DIGIPDU-MIB", "trapArg6"))
)
if mibBuilder.loadTexts:
    envTemperatureHighTrap.setStatus(
        "current"
    )

envTemperatureLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 514)
)
envTemperatureLowTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"),
        ("DIGIPDU-MIB", "trapArg6"))
)
if mibBuilder.loadTexts:
    envTemperatureLowTrap.setStatus(
        "current"
    )

envRHConnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 515)
)
envRHConnectTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"))
)
if mibBuilder.loadTexts:
    envRHConnectTrap.setStatus(
        "current"
    )

envRHHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 516)
)
envRHHighTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"))
)
if mibBuilder.loadTexts:
    envRHHighTrap.setStatus(
        "current"
    )

envRHLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 517)
)
envRHLowTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"),
        ("DIGIPDU-MIB", "trapArg5"))
)
if mibBuilder.loadTexts:
    envRHLowTrap.setStatus(
        "current"
    )

inputTimeOutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 601)
)
inputTimeOutTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"))
)
if mibBuilder.loadTexts:
    inputTimeOutTrap.setStatus(
        "current"
    )

inputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 602)
)
inputTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"),
        ("DIGIPDU-MIB", "trapArg3"),
        ("DIGIPDU-MIB", "trapArg4"))
)
if mibBuilder.loadTexts:
    inputTrap.setStatus(
        "current"
    )

upsConnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 701)
)
upsConnectTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"))
)
if mibBuilder.loadTexts:
    upsConnectTrap.setStatus(
        "current"
    )

upsOnBatteryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 702)
)
upsOnBatteryTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"))
)
if mibBuilder.loadTexts:
    upsOnBatteryTrap.setStatus(
        "current"
    )

upsOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 703)
)
upsOverloadTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"))
)
if mibBuilder.loadTexts:
    upsOverloadTrap.setStatus(
        "current"
    )

upsBatteryLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 704)
)
upsBatteryLowTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"))
)
if mibBuilder.loadTexts:
    upsBatteryLowTrap.setStatus(
        "current"
    )

upsBatteryReplace = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 705)
)
upsBatteryReplace.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"))
)
if mibBuilder.loadTexts:
    upsBatteryReplace.setStatus(
        "current"
    )

daisyChainConnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 801)
)
daisyChainConnectTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"))
)
if mibBuilder.loadTexts:
    daisyChainConnectTrap.setStatus(
        "current"
    )

micDetectOccurTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 901)
)
micDetectOccurTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"))
)
if mibBuilder.loadTexts:
    micDetectOccurTrap.setStatus(
        "current"
    )

vibrationDetectOccurTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10456, 3, 100, 1, 902)
)
vibrationDetectOccurTrap.setObjects(
      *(("DIGIPDU-MIB", "trapArg1"),
        ("DIGIPDU-MIB", "trapArg2"))
)
if mibBuilder.loadTexts:
    vibrationDetectOccurTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGIPDU-MIB",
    **{"digipdu": digipdu,
       "smart": smart,
       "product": product,
       "productModel": productModel,
       "productPartNumber": productPartNumber,
       "productSerialNumber": productSerialNumber,
       "productFirmwareVersion": productFirmwareVersion,
       "productTemperatureKind": productTemperatureKind,
       "productResetDetector": productResetDetector,
       "deviceTable": deviceTable,
       "deviceATSKind": deviceATSKind,
       "deviceInFeedTotal": deviceInFeedTotal,
       "deviceInFeedKind": deviceInFeedKind,
       "deviceInFeedBranch": deviceInFeedBranch,
       "deviceOutTotal": deviceOutTotal,
       "deviceOutKind": deviceOutKind,
       "deviceInbuiltTempTotal": deviceInbuiltTempTotal,
       "deviceExtendTemperatureTotal": deviceExtendTemperatureTotal,
       "deviceExtendRHTotal": deviceExtendRHTotal,
       "devicePDUTotal": devicePDUTotal,
       "deviceInputTotal": deviceInputTotal,
       "deviceUPS": deviceUPS,
       "deviceDaisyChain": deviceDaisyChain,
       "deviceUnitTotal": deviceUnitTotal,
       "deviceUnitTable": deviceUnitTable,
       "deviceUnitEntry": deviceUnitEntry,
       "deviceUnitIndex": deviceUnitIndex,
       "deviceUnitStatus": deviceUnitStatus,
       "deviceUnitInfeedTotal": deviceUnitInfeedTotal,
       "deviceUnitOutTotal": deviceUnitOutTotal,
       "peripheralTables": peripheralTables,
       "aTSTable": aTSTable,
       "aTSEntry": aTSEntry,
       "aTSIndex": aTSIndex,
       "aTSStatus": aTSStatus,
       "aTSVoltage": aTSVoltage,
       "aTSFrequency": aTSFrequency,
       "inFeedTable": inFeedTable,
       "inFeedEntry": inFeedEntry,
       "inFeedIndex": inFeedIndex,
       "inFeedStatus": inFeedStatus,
       "inFeedVoltage": inFeedVoltage,
       "inFeedFrequency": inFeedFrequency,
       "inFeedCurrent": inFeedCurrent,
       "inFeedPowerLoad": inFeedPowerLoad,
       "inFeedPowerFactor": inFeedPowerFactor,
       "inFeedPowerEnergy": inFeedPowerEnergy,
       "inFeedOverLoad": inFeedOverLoad,
       "inFeedHighWarning": inFeedHighWarning,
       "inFeedLowWarning": inFeedLowWarning,
       "inFeedBranch": inFeedBranch,
       "inFeedBranch1Current": inFeedBranch1Current,
       "inFeedBranch1PowerLoad": inFeedBranch1PowerLoad,
       "inFeedBranch1PowerFactor": inFeedBranch1PowerFactor,
       "inFeedBranch1OverLoad": inFeedBranch1OverLoad,
       "inFeedBranch1HighWarning": inFeedBranch1HighWarning,
       "inFeedBranch1LowWarning": inFeedBranch1LowWarning,
       "inFeedBranch2Current": inFeedBranch2Current,
       "inFeedBranch2PowerLoad": inFeedBranch2PowerLoad,
       "inFeedBranch2PowerFactor": inFeedBranch2PowerFactor,
       "inFeedBranch2OverLoad": inFeedBranch2OverLoad,
       "inFeedBranch2HighWarning": inFeedBranch2HighWarning,
       "inFeedBranch2LowWarning": inFeedBranch2LowWarning,
       "outTable": outTable,
       "outEntry": outEntry,
       "outIndex": outIndex,
       "outComputerStatus": outComputerStatus,
       "outCurrentStatus": outCurrentStatus,
       "outSwitchStatus": outSwitchStatus,
       "outSwitchCtrl": outSwitchCtrl,
       "outVoltage": outVoltage,
       "outCurrent": outCurrent,
       "outPowerFactor": outPowerFactor,
       "outPowerLoad": outPowerLoad,
       "outOverload": outOverload,
       "outHighWarning": outHighWarning,
       "outLowWarning": outLowWarning,
       "pduTables": pduTables,
       "pduEntry": pduEntry,
       "pduIndex": pduIndex,
       "pduModel": pduModel,
       "pduMonitor": pduMonitor,
       "pduStatus": pduStatus,
       "pduVoltage": pduVoltage,
       "pduFrequency": pduFrequency,
       "pduCurrent": pduCurrent,
       "pduPowerLoad": pduPowerLoad,
       "pduPowerFactor": pduPowerFactor,
       "pduPowerEnergy": pduPowerEnergy,
       "pduOverload": pduOverload,
       "pduHighWarning": pduHighWarning,
       "pduLowWarning": pduLowWarning,
       "pduBranch": pduBranch,
       "pduBranch1Current": pduBranch1Current,
       "pduBranch1Overload": pduBranch1Overload,
       "pduBranch1HighWarning": pduBranch1HighWarning,
       "pduBranch1LowWarning": pduBranch1LowWarning,
       "pduBranch2Current": pduBranch2Current,
       "pduBranch2Overload": pduBranch2Overload,
       "pduBranch2HighWarning": pduBranch2HighWarning,
       "pduBranch2LowWarning": pduBranch2LowWarning,
       "inbuiltTemperatureTable": inbuiltTemperatureTable,
       "inbuiltTemperatureEntry": inbuiltTemperatureEntry,
       "inbuiltTemperatureIndex": inbuiltTemperatureIndex,
       "inbuiltTemperatureStatus": inbuiltTemperatureStatus,
       "inbuiltTemperature": inbuiltTemperature,
       "inbuiltTemperatureHighWarning": inbuiltTemperatureHighWarning,
       "inbuiltTemperatureLowWarning": inbuiltTemperatureLowWarning,
       "extendTemperatureTable": extendTemperatureTable,
       "extendTemperatureEntry": extendTemperatureEntry,
       "extendTemperatureIndex": extendTemperatureIndex,
       "extendTemperatureDeviceId": extendTemperatureDeviceId,
       "extendTemperaturePort": extendTemperaturePort,
       "extendTemperatureMonitor": extendTemperatureMonitor,
       "extendTemperatureStatus": extendTemperatureStatus,
       "extendTemperature": extendTemperature,
       "extendTemperatureHighWarning": extendTemperatureHighWarning,
       "extendTemperatureLowWarning": extendTemperatureLowWarning,
       "extendRHTable": extendRHTable,
       "extendRHEntry": extendRHEntry,
       "extendRHIndex": extendRHIndex,
       "extendRHDeviceId": extendRHDeviceId,
       "extendRHPort": extendRHPort,
       "extendRHMonitor": extendRHMonitor,
       "extendRHStatus": extendRHStatus,
       "extendRH": extendRH,
       "extendRHHighWarning": extendRHHighWarning,
       "extendRHLowWarning": extendRHLowWarning,
       "inputTable": inputTable,
       "inputEntry": inputEntry,
       "inputIndex": inputIndex,
       "inputStatus": inputStatus,
       "inputState": inputState,
       "inputTimeout": inputTimeout,
       "inputDefault": inputDefault,
       "inputDetectTime": inputDetectTime,
       "rfidReader": rfidReader,
       "rfidCardNum": rfidCardNum,
       "rfidDetectTime": rfidDetectTime,
       "uPS": uPS,
       "uPSModel": uPSModel,
       "uPSConnectStatus": uPSConnectStatus,
       "uPSFirmware": uPSFirmware,
       "uPSSerial": uPSSerial,
       "uPSTemperature": uPSTemperature,
       "uPSInputVoltage": uPSInputVoltage,
       "uPSOutputOnBattery": uPSOutputOnBattery,
       "uPSOutputVoltage": uPSOutputVoltage,
       "uPSOutputFrequency": uPSOutputFrequency,
       "uPSOutputCurrent": uPSOutputCurrent,
       "uPSOutputLoad": uPSOutputLoad,
       "uPSOutputOverload": uPSOutputOverload,
       "uPSBatteryDate": uPSBatteryDate,
       "uPSBatteryVoltage": uPSBatteryVoltage,
       "uPSBatteryLevel": uPSBatteryLevel,
       "uPSBatteryRunTime": uPSBatteryRunTime,
       "uPSBatteryLow": uPSBatteryLow,
       "uPSBatteryReplace": uPSBatteryReplace,
       "uPSUARTId": uPSUARTId,
       "micDetec": micDetec,
       "micDetectTimes": micDetectTimes,
       "micDetectPeriod": micDetectPeriod,
       "micLastDetectTime": micLastDetectTime,
       "vibrationDetec": vibrationDetec,
       "vibrationDetectTimes": vibrationDetectTimes,
       "vibrationDetectPeriod": vibrationDetectPeriod,
       "vibrationLastDetectTime": vibrationLastDetectTime,
       "dataLogTable": dataLogTable,
       "inFeedDataList": inFeedDataList,
       "outDataList": outDataList,
       "pduDataList": pduDataList,
       "smartTraps": smartTraps,
       "trap": trap,
       "testTrap": testTrap,
       "inFeedOverloadTrap": inFeedOverloadTrap,
       "inFeedHighCurrentTrap": inFeedHighCurrentTrap,
       "inFeedLowCurrentTrap": inFeedLowCurrentTrap,
       "inFeedBranchOverloadTrap": inFeedBranchOverloadTrap,
       "inFeedBranchHighCurrentTrap": inFeedBranchHighCurrentTrap,
       "inFeedBranchLowCurrentTrap": inFeedBranchLowCurrentTrap,
       "outWebOperationTrap": outWebOperationTrap,
       "outPanelOperationTrap": outPanelOperationTrap,
       "outAPIOperationTrap": outAPIOperationTrap,
       "outScheduleTrap": outScheduleTrap,
       "outScheduleErrorTrap": outScheduleErrorTrap,
       "outPingTrap": outPingTrap,
       "outPingRebootTrap": outPingRebootTrap,
       "outOverloadTrap": outOverloadTrap,
       "outHighCurrentTrap": outHighCurrentTrap,
       "outLowCurrentTrap": outLowCurrentTrap,
       "outConditionCtrlTrap": outConditionCtrlTrap,
       "outUPSACFaultOffTrap": outUPSACFaultOffTrap,
       "outUPSBatteryLevelOffTrap": outUPSBatteryLevelOffTrap,
       "outUPSBatteryLowOffTrap": outUPSBatteryLowOffTrap,
       "outUPSACRecoveryOnTrap": outUPSACRecoveryOnTrap,
       "outUPSBatteryLevelOnTrap": outUPSBatteryLevelOnTrap,
       "outUPSBatteryLowRecoveryOnTrap": outUPSBatteryLowRecoveryOnTrap,
       "pduConnectTrap": pduConnectTrap,
       "pduOverloadTrap": pduOverloadTrap,
       "pduHighCurrentTrap": pduHighCurrentTrap,
       "pduLowCurrentTrap": pduLowCurrentTrap,
       "pduBranchOverloadTrap": pduBranchOverloadTrap,
       "pduBranchHighCurrentTrap": pduBranchHighCurrentTrap,
       "pduBranchLowCurrentTrap": pduBranchLowCurrentTrap,
       "inbuiltTemperatureHighTrap": inbuiltTemperatureHighTrap,
       "inbuiltTemperatureLowTrap": inbuiltTemperatureLowTrap,
       "envConnectTrap": envConnectTrap,
       "envTemperatureConnectTrap": envTemperatureConnectTrap,
       "envTemperatureHighTrap": envTemperatureHighTrap,
       "envTemperatureLowTrap": envTemperatureLowTrap,
       "envRHConnectTrap": envRHConnectTrap,
       "envRHHighTrap": envRHHighTrap,
       "envRHLowTrap": envRHLowTrap,
       "inputTimeOutTrap": inputTimeOutTrap,
       "inputTrap": inputTrap,
       "upsConnectTrap": upsConnectTrap,
       "upsOnBatteryTrap": upsOnBatteryTrap,
       "upsOverloadTrap": upsOverloadTrap,
       "upsBatteryLowTrap": upsBatteryLowTrap,
       "upsBatteryReplace": upsBatteryReplace,
       "daisyChainConnectTrap": daisyChainConnectTrap,
       "micDetectOccurTrap": micDetectOccurTrap,
       "vibrationDetectOccurTrap": vibrationDetectOccurTrap,
       "arg": arg,
       "trapArg1": trapArg1,
       "trapArg2": trapArg2,
       "trapArg3": trapArg3,
       "trapArg4": trapArg4,
       "trapArg5": trapArg5,
       "trapArg6": trapArg6,
       "trapArg7": trapArg7,
       "trapArg8": trapArg8,
       "trapArg9": trapArg9}
)
