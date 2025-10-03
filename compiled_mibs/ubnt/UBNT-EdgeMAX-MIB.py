# SNMP MIB module (UBNT-EdgeMAX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubnt\UBNT-EdgeMAX-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:39 2025
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

(ubntEdgeMaxGroups,
 ubntMIB) = mibBuilder.importSymbols(
    "UBNT-MIB",
    "ubntEdgeMaxGroups",
    "ubntMIB")


# MODULE-IDENTITY

ubntEdgeMax = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5)
)
if mibBuilder.loadTexts:
    ubntEdgeMax.setRevisions(
        ("2018-01-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UbntProductIdent_ObjectIdentity = ObjectIdentity
ubntProductIdent = _UbntProductIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 1)
)
_UbntModel_Type = DisplayString
_UbntModel_Object = MibScalar
ubntModel = _UbntModel_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 1, 1),
    _UbntModel_Type()
)
ubntModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntModel.setStatus("current")
_UbntSerialNumber_Type = DisplayString
_UbntSerialNumber_Object = MibScalar
ubntSerialNumber = _UbntSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 1, 2),
    _UbntSerialNumber_Type()
)
ubntSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntSerialNumber.setStatus("current")
_UbntVersion_Type = DisplayString
_UbntVersion_Object = MibScalar
ubntVersion = _UbntVersion_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 1, 3),
    _UbntVersion_Type()
)
ubntVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntVersion.setStatus("current")
_UbntPowerOuts_ObjectIdentity = ObjectIdentity
ubntPowerOuts = _UbntPowerOuts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 2)
)
_UbntPowerOutsCount_Type = Unsigned32
_UbntPowerOutsCount_Object = MibScalar
ubntPowerOutsCount = _UbntPowerOutsCount_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 2, 1),
    _UbntPowerOutsCount_Type()
)
ubntPowerOutsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntPowerOutsCount.setStatus("current")
_UbntPowerOutTable_Object = MibTable
ubntPowerOutTable = _UbntPowerOutTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    ubntPowerOutTable.setStatus("current")
_UbntPowerOutEntry_Object = MibTableRow
ubntPowerOutEntry = _UbntPowerOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 2, 2, 1)
)
ubntPowerOutEntry.setIndexNames(
    (0, "UBNT-EdgeMAX-MIB", "ubntPowerOutIndex"),
)
if mibBuilder.loadTexts:
    ubntPowerOutEntry.setStatus("current")


class _UbntPowerOutIndex_Type(Integer32):
    """Custom type ubntPowerOutIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbntPowerOutIndex_Type.__name__ = "Integer32"
_UbntPowerOutIndex_Object = MibTableColumn
ubntPowerOutIndex = _UbntPowerOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 2, 2, 1, 1),
    _UbntPowerOutIndex_Type()
)
ubntPowerOutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntPowerOutIndex.setStatus("current")
_UbntPowerOutVoltage_Type = Integer32
_UbntPowerOutVoltage_Object = MibTableColumn
ubntPowerOutVoltage = _UbntPowerOutVoltage_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 2, 2, 1, 2),
    _UbntPowerOutVoltage_Type()
)
ubntPowerOutVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntPowerOutVoltage.setStatus("current")
_UbntPowerOutCurrent_Type = Integer32
_UbntPowerOutCurrent_Object = MibTableColumn
ubntPowerOutCurrent = _UbntPowerOutCurrent_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 2, 2, 1, 3),
    _UbntPowerOutCurrent_Type()
)
ubntPowerOutCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntPowerOutCurrent.setStatus("current")
_UbntPowerOutPower_Type = Integer32
_UbntPowerOutPower_Object = MibTableColumn
ubntPowerOutPower = _UbntPowerOutPower_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 2, 2, 1, 4),
    _UbntPowerOutPower_Type()
)
ubntPowerOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntPowerOutPower.setStatus("current")
_UbntPowerSupplies_ObjectIdentity = ObjectIdentity
ubntPowerSupplies = _UbntPowerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 3)
)
_UbntPsuBaysNumber_Type = Unsigned32
_UbntPsuBaysNumber_Object = MibScalar
ubntPsuBaysNumber = _UbntPsuBaysNumber_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 3, 1),
    _UbntPsuBaysNumber_Type()
)
ubntPsuBaysNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntPsuBaysNumber.setStatus("current")
_UbntPsuTable_Object = MibTable
ubntPsuTable = _UbntPsuTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    ubntPsuTable.setStatus("current")
_UbntPsuEntry_Object = MibTableRow
ubntPsuEntry = _UbntPsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 3, 2, 1)
)
ubntPsuEntry.setIndexNames(
    (0, "UBNT-EdgeMAX-MIB", "ubntPsuIndex"),
)
if mibBuilder.loadTexts:
    ubntPsuEntry.setStatus("current")


class _UbntPsuIndex_Type(Integer32):
    """Custom type ubntPsuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbntPsuIndex_Type.__name__ = "Integer32"
_UbntPsuIndex_Object = MibTableColumn
ubntPsuIndex = _UbntPsuIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 3, 2, 1, 1),
    _UbntPsuIndex_Type()
)
ubntPsuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntPsuIndex.setStatus("current")


class _UbntPsuType_Type(Integer32):
    """Custom type ubntPsuType based on Integer32"""
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
        *(("unknown", 0),
          ("ac", 1),
          ("dc", 2),
          ("poe", 3))
    )


_UbntPsuType_Type.__name__ = "Integer32"
_UbntPsuType_Object = MibTableColumn
ubntPsuType = _UbntPsuType_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 3, 2, 1, 2),
    _UbntPsuType_Type()
)
ubntPsuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntPsuType.setStatus("current")


class _UbntPsuStatus_Type(Integer32):
    """Custom type ubntPsuStatus based on Integer32"""
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
        *(("unknown", 0),
          ("on", 1),
          ("off", 2),
          ("standby", 3))
    )


_UbntPsuStatus_Type.__name__ = "Integer32"
_UbntPsuStatus_Object = MibTableColumn
ubntPsuStatus = _UbntPsuStatus_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 3, 2, 1, 3),
    _UbntPsuStatus_Type()
)
ubntPsuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntPsuStatus.setStatus("current")


class _UbntPsuOperStatus_Type(Integer32):
    """Custom type ubntPsuOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_UbntPsuOperStatus_Type.__name__ = "Integer32"
_UbntPsuOperStatus_Object = MibTableColumn
ubntPsuOperStatus = _UbntPsuOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 3, 2, 1, 4),
    _UbntPsuOperStatus_Type()
)
ubntPsuOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntPsuOperStatus.setStatus("current")
_UbntPsuVoltage_Type = Integer32
_UbntPsuVoltage_Object = MibTableColumn
ubntPsuVoltage = _UbntPsuVoltage_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 3, 2, 1, 5),
    _UbntPsuVoltage_Type()
)
ubntPsuVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntPsuVoltage.setStatus("current")
_UbntPsuTemperature_Type = Integer32
_UbntPsuTemperature_Object = MibTableColumn
ubntPsuTemperature = _UbntPsuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 3, 2, 1, 6),
    _UbntPsuTemperature_Type()
)
ubntPsuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntPsuTemperature.setStatus("current")


class _UbntPsuCharging_Type(Integer32):
    """Custom type ubntPsuCharging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("on", 1),
          ("off", 2))
    )


_UbntPsuCharging_Type.__name__ = "Integer32"
_UbntPsuCharging_Object = MibTableColumn
ubntPsuCharging = _UbntPsuCharging_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 3, 2, 1, 7),
    _UbntPsuCharging_Type()
)
ubntPsuCharging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntPsuCharging.setStatus("current")
_UbntPsuBatteryQuantity_Type = Integer32
_UbntPsuBatteryQuantity_Object = MibTableColumn
ubntPsuBatteryQuantity = _UbntPsuBatteryQuantity_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 3, 2, 1, 8),
    _UbntPsuBatteryQuantity_Type()
)
ubntPsuBatteryQuantity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntPsuBatteryQuantity.setStatus("current")


class _UbntPsuBatteryChargeLevel_Type(Integer32):
    """Custom type ubntPsuBatteryChargeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UbntPsuBatteryChargeLevel_Type.__name__ = "Integer32"
_UbntPsuBatteryChargeLevel_Object = MibTableColumn
ubntPsuBatteryChargeLevel = _UbntPsuBatteryChargeLevel_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 3, 2, 1, 9),
    _UbntPsuBatteryChargeLevel_Type()
)
ubntPsuBatteryChargeLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntPsuBatteryChargeLevel.setStatus("current")
_UbntPsuBatteryTimeRemaining_Type = TimeTicks
_UbntPsuBatteryTimeRemaining_Object = MibTableColumn
ubntPsuBatteryTimeRemaining = _UbntPsuBatteryTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 3, 2, 1, 10),
    _UbntPsuBatteryTimeRemaining_Type()
)
ubntPsuBatteryTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntPsuBatteryTimeRemaining.setStatus("current")


class _UbntPsuBatteryReplaceIndicator_Type(Integer32):
    """Custom type ubntPsuBatteryReplaceIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("noBatteryNeedsReplacing", 1),
          ("batteryNeedsReplacing", 2))
    )


_UbntPsuBatteryReplaceIndicator_Type.__name__ = "Integer32"
_UbntPsuBatteryReplaceIndicator_Object = MibTableColumn
ubntPsuBatteryReplaceIndicator = _UbntPsuBatteryReplaceIndicator_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 3, 2, 1, 11),
    _UbntPsuBatteryReplaceIndicator_Type()
)
ubntPsuBatteryReplaceIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntPsuBatteryReplaceIndicator.setStatus("current")
_UbntPsuBatteryLastReplaceDate_Type = DisplayString
_UbntPsuBatteryLastReplaceDate_Object = MibTableColumn
ubntPsuBatteryLastReplaceDate = _UbntPsuBatteryLastReplaceDate_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 3, 2, 1, 12),
    _UbntPsuBatteryLastReplaceDate_Type()
)
ubntPsuBatteryLastReplaceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntPsuBatteryLastReplaceDate.setStatus("current")
_UbntThermometers_ObjectIdentity = ObjectIdentity
ubntThermometers = _UbntThermometers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 4)
)
_UbntThermometersCount_Type = Unsigned32
_UbntThermometersCount_Object = MibScalar
ubntThermometersCount = _UbntThermometersCount_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 4, 1),
    _UbntThermometersCount_Type()
)
ubntThermometersCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntThermometersCount.setStatus("current")
_UbntThermsTable_Object = MibTable
ubntThermsTable = _UbntThermsTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 4, 2)
)
if mibBuilder.loadTexts:
    ubntThermsTable.setStatus("current")
_UbntThermsEntry_Object = MibTableRow
ubntThermsEntry = _UbntThermsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 4, 2, 1)
)
ubntThermsEntry.setIndexNames(
    (0, "UBNT-EdgeMAX-MIB", "ubntThermIndex"),
)
if mibBuilder.loadTexts:
    ubntThermsEntry.setStatus("current")


class _UbntThermIndex_Type(Integer32):
    """Custom type ubntThermIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbntThermIndex_Type.__name__ = "Integer32"
_UbntThermIndex_Object = MibTableColumn
ubntThermIndex = _UbntThermIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 4, 2, 1, 1),
    _UbntThermIndex_Type()
)
ubntThermIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntThermIndex.setStatus("current")


class _UbntThermType_Type(Integer32):
    """Custom type ubntThermType based on Integer32"""
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
        *(("other", 0),
          ("board", 1),
          ("cpu", 2),
          ("power", 3))
    )


_UbntThermType_Type.__name__ = "Integer32"
_UbntThermType_Object = MibTableColumn
ubntThermType = _UbntThermType_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 4, 2, 1, 2),
    _UbntThermType_Type()
)
ubntThermType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntThermType.setStatus("current")
_UbntThermTemperature_Type = Integer32
_UbntThermTemperature_Object = MibTableColumn
ubntThermTemperature = _UbntThermTemperature_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 4, 2, 1, 3),
    _UbntThermTemperature_Type()
)
ubntThermTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntThermTemperature.setStatus("current")
_UbntFans_ObjectIdentity = ObjectIdentity
ubntFans = _UbntFans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 5)
)
_UbntFansCount_Type = Unsigned32
_UbntFansCount_Object = MibScalar
ubntFansCount = _UbntFansCount_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 5, 1),
    _UbntFansCount_Type()
)
ubntFansCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntFansCount.setStatus("current")
_UbntFansTable_Object = MibTable
ubntFansTable = _UbntFansTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 5, 2)
)
if mibBuilder.loadTexts:
    ubntFansTable.setStatus("current")
_UbntFanEntry_Object = MibTableRow
ubntFanEntry = _UbntFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 5, 2, 1)
)
ubntFanEntry.setIndexNames(
    (0, "UBNT-EdgeMAX-MIB", "ubntFanIndex"),
)
if mibBuilder.loadTexts:
    ubntFanEntry.setStatus("current")


class _UbntFanIndex_Type(Integer32):
    """Custom type ubntFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbntFanIndex_Type.__name__ = "Integer32"
_UbntFanIndex_Object = MibTableColumn
ubntFanIndex = _UbntFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 5, 2, 1, 1),
    _UbntFanIndex_Type()
)
ubntFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntFanIndex.setStatus("current")


class _UbntFanType_Type(Integer32):
    """Custom type ubntFanType based on Integer32"""
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
        *(("other", 0),
          ("board", 1),
          ("cpu", 2),
          ("power", 3))
    )


_UbntFanType_Type.__name__ = "Integer32"
_UbntFanType_Object = MibTableColumn
ubntFanType = _UbntFanType_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 5, 2, 1, 2),
    _UbntFanType_Type()
)
ubntFanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntFanType.setStatus("current")
_UbntFanRpm_Type = Integer32
_UbntFanRpm_Object = MibTableColumn
ubntFanRpm = _UbntFanRpm_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5, 5, 2, 1, 3),
    _UbntFanRpm_Type()
)
ubntFanRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntFanRpm.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBNT-EdgeMAX-MIB",
    **{"ubntEdgeMax": ubntEdgeMax,
       "ubntProductIdent": ubntProductIdent,
       "ubntModel": ubntModel,
       "ubntSerialNumber": ubntSerialNumber,
       "ubntVersion": ubntVersion,
       "ubntPowerOuts": ubntPowerOuts,
       "ubntPowerOutsCount": ubntPowerOutsCount,
       "ubntPowerOutTable": ubntPowerOutTable,
       "ubntPowerOutEntry": ubntPowerOutEntry,
       "ubntPowerOutIndex": ubntPowerOutIndex,
       "ubntPowerOutVoltage": ubntPowerOutVoltage,
       "ubntPowerOutCurrent": ubntPowerOutCurrent,
       "ubntPowerOutPower": ubntPowerOutPower,
       "ubntPowerSupplies": ubntPowerSupplies,
       "ubntPsuBaysNumber": ubntPsuBaysNumber,
       "ubntPsuTable": ubntPsuTable,
       "ubntPsuEntry": ubntPsuEntry,
       "ubntPsuIndex": ubntPsuIndex,
       "ubntPsuType": ubntPsuType,
       "ubntPsuStatus": ubntPsuStatus,
       "ubntPsuOperStatus": ubntPsuOperStatus,
       "ubntPsuVoltage": ubntPsuVoltage,
       "ubntPsuTemperature": ubntPsuTemperature,
       "ubntPsuCharging": ubntPsuCharging,
       "ubntPsuBatteryQuantity": ubntPsuBatteryQuantity,
       "ubntPsuBatteryChargeLevel": ubntPsuBatteryChargeLevel,
       "ubntPsuBatteryTimeRemaining": ubntPsuBatteryTimeRemaining,
       "ubntPsuBatteryReplaceIndicator": ubntPsuBatteryReplaceIndicator,
       "ubntPsuBatteryLastReplaceDate": ubntPsuBatteryLastReplaceDate,
       "ubntThermometers": ubntThermometers,
       "ubntThermometersCount": ubntThermometersCount,
       "ubntThermsTable": ubntThermsTable,
       "ubntThermsEntry": ubntThermsEntry,
       "ubntThermIndex": ubntThermIndex,
       "ubntThermType": ubntThermType,
       "ubntThermTemperature": ubntThermTemperature,
       "ubntFans": ubntFans,
       "ubntFansCount": ubntFansCount,
       "ubntFansTable": ubntFansTable,
       "ubntFanEntry": ubntFanEntry,
       "ubntFanIndex": ubntFanIndex,
       "ubntFanType": ubntFanType,
       "ubntFanRpm": ubntFanRpm}
)
