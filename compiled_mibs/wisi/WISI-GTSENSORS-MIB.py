# SNMP MIB module (WISI-GTSENSORS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\wisi\WISI-GTSENSORS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:18 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(gtModule,) = mibBuilder.importSymbols(
    "WISI-GTMODULES-MIB",
    "gtModule")

(gtUnit,) = mibBuilder.importSymbols(
    "WISI-TANGRAM-MIB",
    "gtUnit")


# MODULE-IDENTITY

gtSensorsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3)
)
if mibBuilder.loadTexts:
    gtSensorsMIB.setRevisions(
        ("2016-09-08 00:00",
         "2013-07-01 14:00",
         "2013-06-27 14:00",
         "2013-06-26 14:00",
         "2012-12-12 13:20",
         "2011-12-15 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GtSensorsNotifications_ObjectIdentity = ObjectIdentity
gtSensorsNotifications = _GtSensorsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0)
)
_GtSensorsObjects_ObjectIdentity = ObjectIdentity
gtSensorsObjects = _GtSensorsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1)
)


class _GtNumTemps_Type(Unsigned32):
    """Custom type gtNumTemps based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GtNumTemps_Type.__name__ = "Unsigned32"
_GtNumTemps_Object = MibScalar
gtNumTemps = _GtNumTemps_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 1),
    _GtNumTemps_Type()
)
gtNumTemps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtNumTemps.setStatus("current")
_GtTempsTable_Object = MibTable
gtTempsTable = _GtTempsTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gtTempsTable.setStatus("current")
_GtTempsEntry_Object = MibTableRow
gtTempsEntry = _GtTempsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 2, 1)
)
gtTempsEntry.setIndexNames(
    (0, "WISI-GTMODULES-MIB", "gtModule"),
    (0, "WISI-GTSENSORS-MIB", "gtTemp"),
)
if mibBuilder.loadTexts:
    gtTempsEntry.setStatus("current")


class _GtTemp_Type(Unsigned32):
    """Custom type gtTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_GtTemp_Type.__name__ = "Unsigned32"
_GtTemp_Object = MibTableColumn
gtTemp = _GtTemp_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 2, 1, 1),
    _GtTemp_Type()
)
gtTemp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtTemp.setStatus("current")


class _GtTempName_Type(DisplayString):
    """Custom type gtTempName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_GtTempName_Type.__name__ = "DisplayString"
_GtTempName_Object = MibTableColumn
gtTempName = _GtTempName_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 2, 1, 2),
    _GtTempName_Type()
)
gtTempName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtTempName.setStatus("current")


class _GtTempValue_Type(Integer32):
    """Custom type gtTempValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 195),
    )


_GtTempValue_Type.__name__ = "Integer32"
_GtTempValue_Object = MibTableColumn
gtTempValue = _GtTempValue_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 2, 1, 3),
    _GtTempValue_Type()
)
gtTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtTempValue.setStatus("current")
if mibBuilder.loadTexts:
    gtTempValue.setUnits("'C")


class _GtNumFans_Type(Unsigned32):
    """Custom type gtNumFans based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GtNumFans_Type.__name__ = "Unsigned32"
_GtNumFans_Object = MibScalar
gtNumFans = _GtNumFans_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 3),
    _GtNumFans_Type()
)
gtNumFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtNumFans.setStatus("current")
_GtFansTable_Object = MibTable
gtFansTable = _GtFansTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    gtFansTable.setStatus("current")
_GtFansEntry_Object = MibTableRow
gtFansEntry = _GtFansEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 4, 1)
)
gtFansEntry.setIndexNames(
    (0, "WISI-GTSENSORS-MIB", "gtFan"),
)
if mibBuilder.loadTexts:
    gtFansEntry.setStatus("current")


class _GtFan_Type(Unsigned32):
    """Custom type gtFan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_GtFan_Type.__name__ = "Unsigned32"
_GtFan_Object = MibTableColumn
gtFan = _GtFan_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 4, 1, 1),
    _GtFan_Type()
)
gtFan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtFan.setStatus("current")


class _GtFanName_Type(DisplayString):
    """Custom type gtFanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_GtFanName_Type.__name__ = "DisplayString"
_GtFanName_Object = MibTableColumn
gtFanName = _GtFanName_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 4, 1, 2),
    _GtFanName_Type()
)
gtFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtFanName.setStatus("current")


class _GtFanControl_Type(Unsigned32):
    """Custom type gtFanControl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_GtFanControl_Type.__name__ = "Unsigned32"
_GtFanControl_Object = MibTableColumn
gtFanControl = _GtFanControl_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 4, 1, 3),
    _GtFanControl_Type()
)
gtFanControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtFanControl.setStatus("current")
if mibBuilder.loadTexts:
    gtFanControl.setUnits("rpm")


class _GtFanSpeed_Type(Unsigned32):
    """Custom type gtFanSpeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_GtFanSpeed_Type.__name__ = "Unsigned32"
_GtFanSpeed_Object = MibTableColumn
gtFanSpeed = _GtFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 4, 1, 4),
    _GtFanSpeed_Type()
)
gtFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtFanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    gtFanSpeed.setUnits("rpm")
_GtFanUptime_Type = Counter32
_GtFanUptime_Object = MibTableColumn
gtFanUptime = _GtFanUptime_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 4, 1, 5),
    _GtFanUptime_Type()
)
gtFanUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtFanUptime.setStatus("current")
if mibBuilder.loadTexts:
    gtFanUptime.setUnits("s")
_GtFanLifetime_Type = Counter32
_GtFanLifetime_Object = MibTableColumn
gtFanLifetime = _GtFanLifetime_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 4, 1, 6),
    _GtFanLifetime_Type()
)
gtFanLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtFanLifetime.setStatus("current")
if mibBuilder.loadTexts:
    gtFanLifetime.setUnits("s")


class _GtNumPSUs_Type(Unsigned32):
    """Custom type gtNumPSUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GtNumPSUs_Type.__name__ = "Unsigned32"
_GtNumPSUs_Object = MibScalar
gtNumPSUs = _GtNumPSUs_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 5),
    _GtNumPSUs_Type()
)
gtNumPSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtNumPSUs.setStatus("current")
_GtPSUsTable_Object = MibTable
gtPSUsTable = _GtPSUsTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 6)
)
if mibBuilder.loadTexts:
    gtPSUsTable.setStatus("current")
_GtPSUsEntry_Object = MibTableRow
gtPSUsEntry = _GtPSUsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 6, 1)
)
gtPSUsEntry.setIndexNames(
    (0, "WISI-GTSENSORS-MIB", "gtPSU"),
)
if mibBuilder.loadTexts:
    gtPSUsEntry.setStatus("current")


class _GtPSU_Type(Unsigned32):
    """Custom type gtPSU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_GtPSU_Type.__name__ = "Unsigned32"
_GtPSU_Object = MibTableColumn
gtPSU = _GtPSU_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 6, 1, 1),
    _GtPSU_Type()
)
gtPSU.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtPSU.setStatus("current")


class _GtPSUName_Type(DisplayString):
    """Custom type gtPSUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_GtPSUName_Type.__name__ = "DisplayString"
_GtPSUName_Object = MibTableColumn
gtPSUName = _GtPSUName_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 6, 1, 2),
    _GtPSUName_Type()
)
gtPSUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtPSUName.setStatus("current")


class _GtPSUPower_Type(Unsigned32):
    """Custom type gtPSUPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300000),
    )


_GtPSUPower_Type.__name__ = "Unsigned32"
_GtPSUPower_Object = MibTableColumn
gtPSUPower = _GtPSUPower_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 6, 1, 3),
    _GtPSUPower_Type()
)
gtPSUPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtPSUPower.setStatus("current")
if mibBuilder.loadTexts:
    gtPSUPower.setUnits("mW")


class _GtPSUCurrent_Type(Unsigned32):
    """Custom type gtPSUCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25000),
    )


_GtPSUCurrent_Type.__name__ = "Unsigned32"
_GtPSUCurrent_Object = MibTableColumn
gtPSUCurrent = _GtPSUCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 6, 1, 4),
    _GtPSUCurrent_Type()
)
gtPSUCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtPSUCurrent.setStatus("current")
if mibBuilder.loadTexts:
    gtPSUCurrent.setUnits("mA")


class _GtPSUVoltageInt_Type(Unsigned32):
    """Custom type gtPSUVoltageInt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_GtPSUVoltageInt_Type.__name__ = "Unsigned32"
_GtPSUVoltageInt_Object = MibTableColumn
gtPSUVoltageInt = _GtPSUVoltageInt_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 6, 1, 5),
    _GtPSUVoltageInt_Type()
)
gtPSUVoltageInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtPSUVoltageInt.setStatus("current")
if mibBuilder.loadTexts:
    gtPSUVoltageInt.setUnits("mV")


class _GtPSUVoltageOR_Type(Unsigned32):
    """Custom type gtPSUVoltageOR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_GtPSUVoltageOR_Type.__name__ = "Unsigned32"
_GtPSUVoltageOR_Object = MibTableColumn
gtPSUVoltageOR = _GtPSUVoltageOR_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 6, 1, 6),
    _GtPSUVoltageOR_Type()
)
gtPSUVoltageOR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtPSUVoltageOR.setStatus("current")
if mibBuilder.loadTexts:
    gtPSUVoltageOR.setUnits("mV")


class _GtPSUVoltageExt_Type(Unsigned32):
    """Custom type gtPSUVoltageExt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_GtPSUVoltageExt_Type.__name__ = "Unsigned32"
_GtPSUVoltageExt_Object = MibTableColumn
gtPSUVoltageExt = _GtPSUVoltageExt_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 6, 1, 7),
    _GtPSUVoltageExt_Type()
)
gtPSUVoltageExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtPSUVoltageExt.setStatus("current")
if mibBuilder.loadTexts:
    gtPSUVoltageExt.setUnits("mV")


class _GtPSUTemperature_Type(Integer32):
    """Custom type gtPSUTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 195),
    )


_GtPSUTemperature_Type.__name__ = "Integer32"
_GtPSUTemperature_Object = MibTableColumn
gtPSUTemperature = _GtPSUTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 6, 1, 8),
    _GtPSUTemperature_Type()
)
gtPSUTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtPSUTemperature.setStatus("current")
if mibBuilder.loadTexts:
    gtPSUTemperature.setUnits("'C")
_GtSensorsConformance_ObjectIdentity = ObjectIdentity
gtSensorsConformance = _GtSensorsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 2)
)
_GtSensorsCompliances_ObjectIdentity = ObjectIdentity
gtSensorsCompliances = _GtSensorsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 2, 1)
)
_GtSensorsGroups_ObjectIdentity = ObjectIdentity
gtSensorsGroups = _GtSensorsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 2, 2)
)

# Managed Objects groups

gtSensorsV1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 2, 2, 1)
)
gtSensorsV1Group.setObjects(
      *(("WISI-GTSENSORS-MIB", "gtTempName"),
        ("WISI-GTSENSORS-MIB", "gtTempValue"),
        ("WISI-GTSENSORS-MIB", "gtFanName"),
        ("WISI-GTSENSORS-MIB", "gtFanControl"),
        ("WISI-GTSENSORS-MIB", "gtFanSpeed"),
        ("WISI-GTSENSORS-MIB", "gtPSUName"),
        ("WISI-GTSENSORS-MIB", "gtPSUPower"),
        ("WISI-GTSENSORS-MIB", "gtPSUCurrent"),
        ("WISI-GTSENSORS-MIB", "gtPSUVoltageInt"),
        ("WISI-GTSENSORS-MIB", "gtPSUVoltageOR"),
        ("WISI-GTSENSORS-MIB", "gtPSUVoltageExt"),
        ("WISI-GTSENSORS-MIB", "gtPSUTemperature"))
)
if mibBuilder.loadTexts:
    gtSensorsV1Group.setStatus("current")

gtSensorsSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 2, 2, 2)
)
gtSensorsSystemGroup.setObjects(
      *(("WISI-GTSENSORS-MIB", "gtTempName"),
        ("WISI-GTSENSORS-MIB", "gtTempValue"),
        ("WISI-GTSENSORS-MIB", "gtFanName"),
        ("WISI-GTSENSORS-MIB", "gtFanSpeed"),
        ("WISI-GTSENSORS-MIB", "gtPSUName"),
        ("WISI-GTSENSORS-MIB", "gtPSUPower"),
        ("WISI-GTSENSORS-MIB", "gtPSUCurrent"),
        ("WISI-GTSENSORS-MIB", "gtPSUVoltageInt"),
        ("WISI-GTSENSORS-MIB", "gtPSUVoltageOR"),
        ("WISI-GTSENSORS-MIB", "gtPSUVoltageExt"),
        ("WISI-GTSENSORS-MIB", "gtPSUTemperature"))
)
if mibBuilder.loadTexts:
    gtSensorsSystemGroup.setStatus("current")

gtSensorsStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 2, 2, 3)
)
gtSensorsStatsGroup.setObjects(
      *(("WISI-GTSENSORS-MIB", "gtNumTemps"),
        ("WISI-GTSENSORS-MIB", "gtNumFans"),
        ("WISI-GTSENSORS-MIB", "gtFanUptime"),
        ("WISI-GTSENSORS-MIB", "gtFanLifetime"),
        ("WISI-GTSENSORS-MIB", "gtNumPSUs"))
)
if mibBuilder.loadTexts:
    gtSensorsStatsGroup.setStatus("current")

gtSensorsTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 2, 2, 4)
)
gtSensorsTrapGroup.setObjects(
      *(("WISI-GTSENSORS-MIB", "gtTempValue"),
        ("WISI-GTSENSORS-MIB", "gtFanControl"),
        ("WISI-GTSENSORS-MIB", "gtFanSpeed"),
        ("WISI-GTSENSORS-MIB", "gtPSUCurrent"),
        ("WISI-GTSENSORS-MIB", "gtPSUVoltageInt"))
)
if mibBuilder.loadTexts:
    gtSensorsTrapGroup.setStatus("current")

gtSensorsSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 2, 2, 5)
)
gtSensorsSetGroup.setObjects(
    ("WISI-GTSENSORS-MIB", "gtFanControl")
)
if mibBuilder.loadTexts:
    gtSensorsSetGroup.setStatus("current")


# Notification objects

gtSensorsNotifyFanPlugin = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 1)
)
if mibBuilder.loadTexts:
    gtSensorsNotifyFanPlugin.setStatus(
        "current"
    )

gtSensorsNotifyFanPlugout = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 2)
)
if mibBuilder.loadTexts:
    gtSensorsNotifyFanPlugout.setStatus(
        "current"
    )

gtSensorsNotifyPSUPlugin = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 3)
)
if mibBuilder.loadTexts:
    gtSensorsNotifyPSUPlugin.setStatus(
        "current"
    )

gtSensorsNotifyPSUPlugout = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 4)
)
if mibBuilder.loadTexts:
    gtSensorsNotifyPSUPlugout.setStatus(
        "current"
    )

gtSensorsNotifyTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 5)
)
if mibBuilder.loadTexts:
    gtSensorsNotifyTemperature.setStatus(
        "current"
    )

gtSensorsNotifyFanSpeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 6)
)
if mibBuilder.loadTexts:
    gtSensorsNotifyFanSpeed.setStatus(
        "current"
    )

gtSensorsNotifyPSUCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 7)
)
if mibBuilder.loadTexts:
    gtSensorsNotifyPSUCurrent.setStatus(
        "current"
    )

gtSensorsNotifyPSUVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 8)
)
if mibBuilder.loadTexts:
    gtSensorsNotifyPSUVoltage.setStatus(
        "current"
    )

gtSensorsNotifyPSUTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 9)
)
if mibBuilder.loadTexts:
    gtSensorsNotifyPSUTemperature.setStatus(
        "current"
    )

gtSensorsNotifyPSUTemperatureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 10)
)
if mibBuilder.loadTexts:
    gtSensorsNotifyPSUTemperatureClear.setStatus(
        "current"
    )

gtSensorsNotifyBOARDTemperatureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 11)
)
if mibBuilder.loadTexts:
    gtSensorsNotifyBOARDTemperatureClear.setStatus(
        "current"
    )

gtSensorsNotifyPSUFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 12)
)
if mibBuilder.loadTexts:
    gtSensorsNotifyPSUFailure.setStatus(
        "current"
    )

gtSensorsNotifyPSUFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 13)
)
if mibBuilder.loadTexts:
    gtSensorsNotifyPSUFailureClear.setStatus(
        "current"
    )


# Notifications groups

gtSensorsBasicNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 2, 2, 6)
)
gtSensorsBasicNotificationsGroup.setObjects(
      *(("WISI-GTSENSORS-MIB", "gtSensorsNotifyFanPlugin"),
        ("WISI-GTSENSORS-MIB", "gtSensorsNotifyFanPlugout"),
        ("WISI-GTSENSORS-MIB", "gtSensorsNotifyPSUPlugin"),
        ("WISI-GTSENSORS-MIB", "gtSensorsNotifyPSUPlugout"),
        ("WISI-GTSENSORS-MIB", "gtSensorsNotifyTemperature"),
        ("WISI-GTSENSORS-MIB", "gtSensorsNotifyFanSpeed"),
        ("WISI-GTSENSORS-MIB", "gtSensorsNotifyPSUCurrent"),
        ("WISI-GTSENSORS-MIB", "gtSensorsNotifyPSUVoltage"),
        ("WISI-GTSENSORS-MIB", "gtSensorsNotifyPSUTemperature"))
)
if mibBuilder.loadTexts:
    gtSensorsBasicNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

gtSensorsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 2, 1, 1)
)
gtSensorsMIBCompliance.setObjects(
      *(("WISI-GTSENSORS-MIB", "gtSensorsV1Group"),
        ("WISI-GTSENSORS-MIB", "gtSensorsSystemGroup"),
        ("WISI-GTSENSORS-MIB", "gtSensorsStatsGroup"),
        ("WISI-GTSENSORS-MIB", "gtSensorsTrapGroup"),
        ("WISI-GTSENSORS-MIB", "gtSensorsSetGroup"),
        ("WISI-GTSENSORS-MIB", "gtSensorsBasicNotificationsGroup"))
)
if mibBuilder.loadTexts:
    gtSensorsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WISI-GTSENSORS-MIB",
    **{"gtSensorsMIB": gtSensorsMIB,
       "gtSensorsNotifications": gtSensorsNotifications,
       "gtSensorsNotifyFanPlugin": gtSensorsNotifyFanPlugin,
       "gtSensorsNotifyFanPlugout": gtSensorsNotifyFanPlugout,
       "gtSensorsNotifyPSUPlugin": gtSensorsNotifyPSUPlugin,
       "gtSensorsNotifyPSUPlugout": gtSensorsNotifyPSUPlugout,
       "gtSensorsNotifyTemperature": gtSensorsNotifyTemperature,
       "gtSensorsNotifyFanSpeed": gtSensorsNotifyFanSpeed,
       "gtSensorsNotifyPSUCurrent": gtSensorsNotifyPSUCurrent,
       "gtSensorsNotifyPSUVoltage": gtSensorsNotifyPSUVoltage,
       "gtSensorsNotifyPSUTemperature": gtSensorsNotifyPSUTemperature,
       "gtSensorsNotifyPSUTemperatureClear": gtSensorsNotifyPSUTemperatureClear,
       "gtSensorsNotifyBOARDTemperatureClear": gtSensorsNotifyBOARDTemperatureClear,
       "gtSensorsNotifyPSUFailure": gtSensorsNotifyPSUFailure,
       "gtSensorsNotifyPSUFailureClear": gtSensorsNotifyPSUFailureClear,
       "gtSensorsObjects": gtSensorsObjects,
       "gtNumTemps": gtNumTemps,
       "gtTempsTable": gtTempsTable,
       "gtTempsEntry": gtTempsEntry,
       "gtTemp": gtTemp,
       "gtTempName": gtTempName,
       "gtTempValue": gtTempValue,
       "gtNumFans": gtNumFans,
       "gtFansTable": gtFansTable,
       "gtFansEntry": gtFansEntry,
       "gtFan": gtFan,
       "gtFanName": gtFanName,
       "gtFanControl": gtFanControl,
       "gtFanSpeed": gtFanSpeed,
       "gtFanUptime": gtFanUptime,
       "gtFanLifetime": gtFanLifetime,
       "gtNumPSUs": gtNumPSUs,
       "gtPSUsTable": gtPSUsTable,
       "gtPSUsEntry": gtPSUsEntry,
       "gtPSU": gtPSU,
       "gtPSUName": gtPSUName,
       "gtPSUPower": gtPSUPower,
       "gtPSUCurrent": gtPSUCurrent,
       "gtPSUVoltageInt": gtPSUVoltageInt,
       "gtPSUVoltageOR": gtPSUVoltageOR,
       "gtPSUVoltageExt": gtPSUVoltageExt,
       "gtPSUTemperature": gtPSUTemperature,
       "gtSensorsConformance": gtSensorsConformance,
       "gtSensorsCompliances": gtSensorsCompliances,
       "gtSensorsMIBCompliance": gtSensorsMIBCompliance,
       "gtSensorsGroups": gtSensorsGroups,
       "gtSensorsV1Group": gtSensorsV1Group,
       "gtSensorsSystemGroup": gtSensorsSystemGroup,
       "gtSensorsStatsGroup": gtSensorsStatsGroup,
       "gtSensorsTrapGroup": gtSensorsTrapGroup,
       "gtSensorsSetGroup": gtSensorsSetGroup,
       "gtSensorsBasicNotificationsGroup": gtSensorsBasicNotificationsGroup}
)
