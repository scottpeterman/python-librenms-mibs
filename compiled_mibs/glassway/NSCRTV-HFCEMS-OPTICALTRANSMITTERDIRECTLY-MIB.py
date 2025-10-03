# SNMP MIB module (NSCRTV-HFCEMS-OPTICALTRANSMITTERDIRECTLY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\glassway\NSCRTV-HFCEMS-OPTICALTRANSMITTERDIRECTLY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:47:52 2025
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

(otdIdent,) = mibBuilder.importSymbols(
    "NSCRTV-ROOT",
    "otdIdent")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OtdVendorOID_Type = ObjectIdentifier
_OtdVendorOID_Object = MibScalar
otdVendorOID = _OtdVendorOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 1),
    _OtdVendorOID_Type()
)
otdVendorOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdVendorOID.setStatus("optional")


class _OtdSlotNumber_Type(Integer32):
    """Custom type otdSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_OtdSlotNumber_Type.__name__ = "Integer32"
_OtdSlotNumber_Object = MibScalar
otdSlotNumber = _OtdSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 2),
    _OtdSlotNumber_Type()
)
otdSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdSlotNumber.setStatus("mandatory")
_OtdOptDeviceTable_Object = MibTable
otdOptDeviceTable = _OtdOptDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 3)
)
if mibBuilder.loadTexts:
    otdOptDeviceTable.setStatus("mandatory")
_OtdOptDeviceEntry_Object = MibTableRow
otdOptDeviceEntry = _OtdOptDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 3, 1)
)
otdOptDeviceEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-OPTICALTRANSMITTERDIRECTLY-MIB", "otdIndex"),
)
if mibBuilder.loadTexts:
    otdOptDeviceEntry.setStatus("mandatory")


class _OtdIndex_Type(Integer32):
    """Custom type otdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_OtdIndex_Type.__name__ = "Integer32"
_OtdIndex_Object = MibTableColumn
otdIndex = _OtdIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 3, 1, 1),
    _OtdIndex_Type()
)
otdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdIndex.setStatus("mandatory")
_OtdLaserWavelength_Type = DisplayString
_OtdLaserWavelength_Object = MibTableColumn
otdLaserWavelength = _OtdLaserWavelength_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 3, 1, 2),
    _OtdLaserWavelength_Type()
)
otdLaserWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdLaserWavelength.setStatus("mandatory")
_OtdLaserType_Type = DisplayString
_OtdLaserType_Object = MibTableColumn
otdLaserType = _OtdLaserType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 3, 1, 3),
    _OtdLaserType_Type()
)
otdLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdLaserType.setStatus("optional")


class _OtdDriveLevel_Type(Integer32):
    """Custom type otdDriveLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_OtdDriveLevel_Type.__name__ = "Integer32"
_OtdDriveLevel_Object = MibTableColumn
otdDriveLevel = _OtdDriveLevel_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 3, 1, 4),
    _OtdDriveLevel_Type()
)
otdDriveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdDriveLevel.setStatus("optional")


class _OtdInputRFLevel_Type(Integer32):
    """Custom type otdInputRFLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_OtdInputRFLevel_Type.__name__ = "Integer32"
_OtdInputRFLevel_Object = MibTableColumn
otdInputRFLevel = _OtdInputRFLevel_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 3, 1, 5),
    _OtdInputRFLevel_Type()
)
otdInputRFLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdInputRFLevel.setStatus("optional")


class _OtdInputRFAttenuationRange_Type(Integer32):
    """Custom type otdInputRFAttenuationRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_OtdInputRFAttenuationRange_Type.__name__ = "Integer32"
_OtdInputRFAttenuationRange_Object = MibTableColumn
otdInputRFAttenuationRange = _OtdInputRFAttenuationRange_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 3, 1, 6),
    _OtdInputRFAttenuationRange_Type()
)
otdInputRFAttenuationRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdInputRFAttenuationRange.setStatus("optional")


class _OtdInputRFAttenuation_Type(Integer32):
    """Custom type otdInputRFAttenuation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_OtdInputRFAttenuation_Type.__name__ = "Integer32"
_OtdInputRFAttenuation_Object = MibTableColumn
otdInputRFAttenuation = _OtdInputRFAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 3, 1, 7),
    _OtdInputRFAttenuation_Type()
)
otdInputRFAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdInputRFAttenuation.setStatus("optional")


class _OtdLaserTemp_Type(Integer32):
    """Custom type otdLaserTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_OtdLaserTemp_Type.__name__ = "Integer32"
_OtdLaserTemp_Object = MibTableColumn
otdLaserTemp = _OtdLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 3, 1, 8),
    _OtdLaserTemp_Type()
)
otdLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdLaserTemp.setStatus("mandatory")


class _OtdLaserCurrent_Type(Integer32):
    """Custom type otdLaserCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_OtdLaserCurrent_Type.__name__ = "Integer32"
_OtdLaserCurrent_Object = MibTableColumn
otdLaserCurrent = _OtdLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 3, 1, 9),
    _OtdLaserCurrent_Type()
)
otdLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdLaserCurrent.setStatus("mandatory")


class _OtdOpicalOutputPower_Type(Integer32):
    """Custom type otdOpicalOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_OtdOpicalOutputPower_Type.__name__ = "Integer32"
_OtdOpicalOutputPower_Object = MibTableColumn
otdOpicalOutputPower = _OtdOpicalOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 3, 1, 10),
    _OtdOpicalOutputPower_Type()
)
otdOpicalOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdOpicalOutputPower.setStatus("mandatory")


class _OtdTecCurrent_Type(Integer32):
    """Custom type otdTecCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_OtdTecCurrent_Type.__name__ = "Integer32"
_OtdTecCurrent_Object = MibTableColumn
otdTecCurrent = _OtdTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 3, 1, 11),
    _OtdTecCurrent_Type()
)
otdTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdTecCurrent.setStatus("optional")


class _OtdAGCControl_Type(Integer32):
    """Custom type otdAGCControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_OtdAGCControl_Type.__name__ = "Integer32"
_OtdAGCControl_Object = MibTableColumn
otdAGCControl = _OtdAGCControl_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 3, 1, 12),
    _OtdAGCControl_Type()
)
otdAGCControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdAGCControl.setStatus("optional")
_OtdConfigurationDriveLevel_Type = Integer32
_OtdConfigurationDriveLevel_Object = MibTableColumn
otdConfigurationDriveLevel = _OtdConfigurationDriveLevel_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 3, 1, 13),
    _OtdConfigurationDriveLevel_Type()
)
otdConfigurationDriveLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdConfigurationDriveLevel.setStatus("optional")
_OtdConfigurationRFAttenuation_Type = Integer32
_OtdConfigurationRFAttenuation_Object = MibTableColumn
otdConfigurationRFAttenuation = _OtdConfigurationRFAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 3, 1, 14),
    _OtdConfigurationRFAttenuation_Type()
)
otdConfigurationRFAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdConfigurationRFAttenuation.setStatus("optional")
_OtdConfigurationRFChannels_Type = Integer32
_OtdConfigurationRFChannels_Object = MibTableColumn
otdConfigurationRFChannels = _OtdConfigurationRFChannels_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 3, 1, 15),
    _OtdConfigurationRFChannels_Type()
)
otdConfigurationRFChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdConfigurationRFChannels.setStatus("optional")
_OtdFansNumber_Type = Integer32
_OtdFansNumber_Object = MibScalar
otdFansNumber = _OtdFansNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 4),
    _OtdFansNumber_Type()
)
otdFansNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdFansNumber.setStatus("mandatory")
_OtdFansTable_Object = MibTable
otdFansTable = _OtdFansTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 5)
)
if mibBuilder.loadTexts:
    otdFansTable.setStatus("optional")
_OtdFansEntry_Object = MibTableRow
otdFansEntry = _OtdFansEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 5, 1)
)
otdFansEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-OPTICALTRANSMITTERDIRECTLY-MIB", "otdFansIndex"),
)
if mibBuilder.loadTexts:
    otdFansEntry.setStatus("optional")
_OtdFansIndex_Type = Integer32
_OtdFansIndex_Object = MibTableColumn
otdFansIndex = _OtdFansIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 5, 1, 1),
    _OtdFansIndex_Type()
)
otdFansIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdFansIndex.setStatus("optional")


class _OtdFansState_Type(Integer32):
    """Custom type otdFansState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("fault", 2),
          ("off", 3))
    )


_OtdFansState_Type.__name__ = "Integer32"
_OtdFansState_Object = MibTableColumn
otdFansState = _OtdFansState_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 5, 1, 2),
    _OtdFansState_Type()
)
otdFansState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdFansState.setStatus("optional")
_OtdFansSpeed_Type = Integer32
_OtdFansSpeed_Object = MibTableColumn
otdFansSpeed = _OtdFansSpeed_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 5, 1, 3),
    _OtdFansSpeed_Type()
)
otdFansSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdFansSpeed.setStatus("optional")


class _OtdFansControl_Type(Integer32):
    """Custom type otdFansControl based on Integer32"""
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


_OtdFansControl_Type.__name__ = "Integer32"
_OtdFansControl_Object = MibTableColumn
otdFansControl = _OtdFansControl_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 5, 1, 4),
    _OtdFansControl_Type()
)
otdFansControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdFansControl.setStatus("optional")
_OtdFansName_Type = DisplayString
_OtdFansName_Object = MibTableColumn
otdFansName = _OtdFansName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 5, 1, 5),
    _OtdFansName_Type()
)
otdFansName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdFansName.setStatus("optional")


class _OtdNumberDCPowerSupply_Type(Integer32):
    """Custom type otdNumberDCPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_OtdNumberDCPowerSupply_Type.__name__ = "Integer32"
_OtdNumberDCPowerSupply_Object = MibScalar
otdNumberDCPowerSupply = _OtdNumberDCPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 6),
    _OtdNumberDCPowerSupply_Type()
)
otdNumberDCPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdNumberDCPowerSupply.setStatus("mandatory")


class _OtdDCPowerSupplyMode_Type(Integer32):
    """Custom type otdDCPowerSupplyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loadsharing", 1),
          ("switchedredundant", 2),
          ("alonesupply", 3))
    )


_OtdDCPowerSupplyMode_Type.__name__ = "Integer32"
_OtdDCPowerSupplyMode_Object = MibScalar
otdDCPowerSupplyMode = _OtdDCPowerSupplyMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 7),
    _OtdDCPowerSupplyMode_Type()
)
otdDCPowerSupplyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdDCPowerSupplyMode.setStatus("optional")
_OtdDCPowerTable_Object = MibTable
otdDCPowerTable = _OtdDCPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 8)
)
if mibBuilder.loadTexts:
    otdDCPowerTable.setStatus("mandatory")
_OtdDCPowerEntry_Object = MibTableRow
otdDCPowerEntry = _OtdDCPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 8, 1)
)
otdDCPowerEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-OPTICALTRANSMITTERDIRECTLY-MIB", "otdDCPowerIndex"),
)
if mibBuilder.loadTexts:
    otdDCPowerEntry.setStatus("mandatory")
_OtdDCPowerIndex_Type = Integer32
_OtdDCPowerIndex_Object = MibTableColumn
otdDCPowerIndex = _OtdDCPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 8, 1, 1),
    _OtdDCPowerIndex_Type()
)
otdDCPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdDCPowerIndex.setStatus("mandatory")


class _OtdDCPowerVoltage_Type(Integer32):
    """Custom type otdDCPowerVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_OtdDCPowerVoltage_Type.__name__ = "Integer32"
_OtdDCPowerVoltage_Object = MibTableColumn
otdDCPowerVoltage = _OtdDCPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 8, 1, 2),
    _OtdDCPowerVoltage_Type()
)
otdDCPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdDCPowerVoltage.setStatus("mandatory")


class _OtdDCPowerCurrent_Type(Integer32):
    """Custom type otdDCPowerCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OtdDCPowerCurrent_Type.__name__ = "Integer32"
_OtdDCPowerCurrent_Object = MibTableColumn
otdDCPowerCurrent = _OtdDCPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 8, 1, 3),
    _OtdDCPowerCurrent_Type()
)
otdDCPowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdDCPowerCurrent.setStatus("optional")
_OtdDCPowerName_Type = DisplayString
_OtdDCPowerName_Object = MibTableColumn
otdDCPowerName = _OtdDCPowerName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 6, 8, 1, 4),
    _OtdDCPowerName_Type()
)
otdDCPowerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdDCPowerName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-HFCEMS-OPTICALTRANSMITTERDIRECTLY-MIB",
    **{"otdVendorOID": otdVendorOID,
       "otdSlotNumber": otdSlotNumber,
       "otdOptDeviceTable": otdOptDeviceTable,
       "otdOptDeviceEntry": otdOptDeviceEntry,
       "otdIndex": otdIndex,
       "otdLaserWavelength": otdLaserWavelength,
       "otdLaserType": otdLaserType,
       "otdDriveLevel": otdDriveLevel,
       "otdInputRFLevel": otdInputRFLevel,
       "otdInputRFAttenuationRange": otdInputRFAttenuationRange,
       "otdInputRFAttenuation": otdInputRFAttenuation,
       "otdLaserTemp": otdLaserTemp,
       "otdLaserCurrent": otdLaserCurrent,
       "otdOpicalOutputPower": otdOpicalOutputPower,
       "otdTecCurrent": otdTecCurrent,
       "otdAGCControl": otdAGCControl,
       "otdConfigurationDriveLevel": otdConfigurationDriveLevel,
       "otdConfigurationRFAttenuation": otdConfigurationRFAttenuation,
       "otdConfigurationRFChannels": otdConfigurationRFChannels,
       "otdFansNumber": otdFansNumber,
       "otdFansTable": otdFansTable,
       "otdFansEntry": otdFansEntry,
       "otdFansIndex": otdFansIndex,
       "otdFansState": otdFansState,
       "otdFansSpeed": otdFansSpeed,
       "otdFansControl": otdFansControl,
       "otdFansName": otdFansName,
       "otdNumberDCPowerSupply": otdNumberDCPowerSupply,
       "otdDCPowerSupplyMode": otdDCPowerSupplyMode,
       "otdDCPowerTable": otdDCPowerTable,
       "otdDCPowerEntry": otdDCPowerEntry,
       "otdDCPowerIndex": otdDCPowerIndex,
       "otdDCPowerVoltage": otdDCPowerVoltage,
       "otdDCPowerCurrent": otdDCPowerCurrent,
       "otdDCPowerName": otdDCPowerName}
)
