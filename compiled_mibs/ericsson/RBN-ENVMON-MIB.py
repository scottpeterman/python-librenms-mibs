# SNMP MIB module (RBN-ENVMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ericsson\RBN-ENVMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:42:43 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rbnEnvMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4)
)
if mibBuilder.loadTexts:
    rbnEnvMonMIB.setRevisions(
        ("2012-10-03 00:00",
         "2011-01-19 18:00",
         "2010-11-11 00:00",
         "2006-01-16 00:00",
         "2002-06-05 00:00",
         "2001-07-25 00:00",
         "2000-04-24 00:00",
         "1999-03-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RbnVoltage(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )



class RbnTemperature(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class RbnFanSpeed(TextualConvention, Unsigned32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_RbnEnvMonMIBNotifications_ObjectIdentity = ObjectIdentity
rbnEnvMonMIBNotifications = _RbnEnvMonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 0)
)
_RbnEnvMonMIBObjects_ObjectIdentity = ObjectIdentity
rbnEnvMonMIBObjects = _RbnEnvMonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1)
)
_RbnFanStatusTable_Object = MibTable
rbnFanStatusTable = _RbnFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rbnFanStatusTable.setStatus("current")
_RbnFanStatusEntry_Object = MibTableRow
rbnFanStatusEntry = _RbnFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1, 1)
)
rbnFanStatusEntry.setIndexNames(
    (0, "RBN-ENVMON-MIB", "rbnFanIndex"),
)
if mibBuilder.loadTexts:
    rbnFanStatusEntry.setStatus("current")


class _RbnFanIndex_Type(Integer32):
    """Custom type rbnFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RbnFanIndex_Type.__name__ = "Integer32"
_RbnFanIndex_Object = MibTableColumn
rbnFanIndex = _RbnFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1, 1, 1),
    _RbnFanIndex_Type()
)
rbnFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnFanIndex.setStatus("current")


class _RbnFanDescr_Type(DisplayString):
    """Custom type rbnFanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbnFanDescr_Type.__name__ = "DisplayString"
_RbnFanDescr_Object = MibTableColumn
rbnFanDescr = _RbnFanDescr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1, 1, 2),
    _RbnFanDescr_Type()
)
rbnFanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFanDescr.setStatus("current")
_RbnFanFail_Type = TruthValue
_RbnFanFail_Object = MibTableColumn
rbnFanFail = _RbnFanFail_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1, 1, 3),
    _RbnFanFail_Type()
)
rbnFanFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFanFail.setStatus("deprecated")


class _RbnFanStatus_Type(Integer32):
    """Custom type rbnFanStatus based on Integer32"""
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
        *(("normal", 1),
          ("failed", 2),
          ("absent", 3),
          ("unknown", 4))
    )


_RbnFanStatus_Type.__name__ = "Integer32"
_RbnFanStatus_Object = MibTableColumn
rbnFanStatus = _RbnFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1, 1, 4),
    _RbnFanStatus_Type()
)
rbnFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFanStatus.setStatus("current")
_RbnPowerStatusTable_Object = MibTable
rbnPowerStatusTable = _RbnPowerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    rbnPowerStatusTable.setStatus("current")
_RbnPowerStatusEntry_Object = MibTableRow
rbnPowerStatusEntry = _RbnPowerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2, 1)
)
rbnPowerStatusEntry.setIndexNames(
    (0, "RBN-ENVMON-MIB", "rbnPowerIndex"),
)
if mibBuilder.loadTexts:
    rbnPowerStatusEntry.setStatus("current")


class _RbnPowerIndex_Type(Integer32):
    """Custom type rbnPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RbnPowerIndex_Type.__name__ = "Integer32"
_RbnPowerIndex_Object = MibTableColumn
rbnPowerIndex = _RbnPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2, 1, 1),
    _RbnPowerIndex_Type()
)
rbnPowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnPowerIndex.setStatus("current")


class _RbnPowerDescr_Type(DisplayString):
    """Custom type rbnPowerDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbnPowerDescr_Type.__name__ = "DisplayString"
_RbnPowerDescr_Object = MibTableColumn
rbnPowerDescr = _RbnPowerDescr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2, 1, 2),
    _RbnPowerDescr_Type()
)
rbnPowerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnPowerDescr.setStatus("current")
_RbnPowerFail_Type = TruthValue
_RbnPowerFail_Object = MibTableColumn
rbnPowerFail = _RbnPowerFail_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2, 1, 3),
    _RbnPowerFail_Type()
)
rbnPowerFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnPowerFail.setStatus("deprecated")


class _RbnPowerStatus_Type(Integer32):
    """Custom type rbnPowerStatus based on Integer32"""
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
        *(("normal", 1),
          ("failed", 2),
          ("absent", 3),
          ("unknown", 4))
    )


_RbnPowerStatus_Type.__name__ = "Integer32"
_RbnPowerStatus_Object = MibTableColumn
rbnPowerStatus = _RbnPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2, 1, 4),
    _RbnPowerStatus_Type()
)
rbnPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnPowerStatus.setStatus("current")
_RbnVoltageSensorTable_Object = MibTable
rbnVoltageSensorTable = _RbnVoltageSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 3)
)
if mibBuilder.loadTexts:
    rbnVoltageSensorTable.setStatus("current")
_RbnVoltageSensorEntry_Object = MibTableRow
rbnVoltageSensorEntry = _RbnVoltageSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 3, 1)
)
rbnVoltageSensorEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "RBN-ENVMON-MIB", "rbnVoltageIndex"),
)
if mibBuilder.loadTexts:
    rbnVoltageSensorEntry.setStatus("current")


class _RbnVoltageIndex_Type(Integer32):
    """Custom type rbnVoltageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RbnVoltageIndex_Type.__name__ = "Integer32"
_RbnVoltageIndex_Object = MibTableColumn
rbnVoltageIndex = _RbnVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 3, 1, 1),
    _RbnVoltageIndex_Type()
)
rbnVoltageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnVoltageIndex.setStatus("current")


class _RbnVoltageDescr_Type(DisplayString):
    """Custom type rbnVoltageDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_RbnVoltageDescr_Type.__name__ = "DisplayString"
_RbnVoltageDescr_Object = MibTableColumn
rbnVoltageDescr = _RbnVoltageDescr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 3, 1, 2),
    _RbnVoltageDescr_Type()
)
rbnVoltageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnVoltageDescr.setStatus("current")
_RbnVoltageDesired_Type = RbnVoltage
_RbnVoltageDesired_Object = MibTableColumn
rbnVoltageDesired = _RbnVoltageDesired_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 3, 1, 3),
    _RbnVoltageDesired_Type()
)
rbnVoltageDesired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnVoltageDesired.setStatus("current")
if mibBuilder.loadTexts:
    rbnVoltageDesired.setUnits("millivolts")
_RbnVoltageCurrent_Type = RbnVoltage
_RbnVoltageCurrent_Object = MibTableColumn
rbnVoltageCurrent = _RbnVoltageCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 3, 1, 4),
    _RbnVoltageCurrent_Type()
)
rbnVoltageCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnVoltageCurrent.setStatus("current")
if mibBuilder.loadTexts:
    rbnVoltageCurrent.setUnits("millivolts")
_RbnCpuTempSensorTable_Object = MibTable
rbnCpuTempSensorTable = _RbnCpuTempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 4)
)
if mibBuilder.loadTexts:
    rbnCpuTempSensorTable.setStatus("deprecated")
_RbnCpuTempSensorEntry_Object = MibTableRow
rbnCpuTempSensorEntry = _RbnCpuTempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 4, 1)
)
rbnCpuTempSensorEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "RBN-ENVMON-MIB", "rbnCpuTempIndex"),
)
if mibBuilder.loadTexts:
    rbnCpuTempSensorEntry.setStatus("deprecated")


class _RbnCpuTempIndex_Type(Integer32):
    """Custom type rbnCpuTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RbnCpuTempIndex_Type.__name__ = "Integer32"
_RbnCpuTempIndex_Object = MibTableColumn
rbnCpuTempIndex = _RbnCpuTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 4, 1, 1),
    _RbnCpuTempIndex_Type()
)
rbnCpuTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnCpuTempIndex.setStatus("deprecated")


class _RbnCpuTempDescr_Type(DisplayString):
    """Custom type rbnCpuTempDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_RbnCpuTempDescr_Type.__name__ = "DisplayString"
_RbnCpuTempDescr_Object = MibTableColumn
rbnCpuTempDescr = _RbnCpuTempDescr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 4, 1, 2),
    _RbnCpuTempDescr_Type()
)
rbnCpuTempDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCpuTempDescr.setStatus("deprecated")
_RbnCpuTempCurrent_Type = RbnTemperature
_RbnCpuTempCurrent_Object = MibTableColumn
rbnCpuTempCurrent = _RbnCpuTempCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 4, 1, 3),
    _RbnCpuTempCurrent_Type()
)
rbnCpuTempCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCpuTempCurrent.setStatus("deprecated")
if mibBuilder.loadTexts:
    rbnCpuTempCurrent.setUnits("degrees")
_RbnFanSpeedTable_Object = MibTable
rbnFanSpeedTable = _RbnFanSpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 5)
)
if mibBuilder.loadTexts:
    rbnFanSpeedTable.setStatus("current")
_RbnFanSpeedEntry_Object = MibTableRow
rbnFanSpeedEntry = _RbnFanSpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 5, 1)
)
rbnFanSpeedEntry.setIndexNames(
    (0, "RBN-ENVMON-MIB", "rbnFanIndex"),
    (0, "RBN-ENVMON-MIB", "rbnFanUnitID"),
)
if mibBuilder.loadTexts:
    rbnFanSpeedEntry.setStatus("current")


class _RbnFanUnitID_Type(Integer32):
    """Custom type rbnFanUnitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RbnFanUnitID_Type.__name__ = "Integer32"
_RbnFanUnitID_Object = MibTableColumn
rbnFanUnitID = _RbnFanUnitID_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 5, 1, 1),
    _RbnFanUnitID_Type()
)
rbnFanUnitID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnFanUnitID.setStatus("current")


class _RbnFanUnitDescr_Type(DisplayString):
    """Custom type rbnFanUnitDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbnFanUnitDescr_Type.__name__ = "DisplayString"
_RbnFanUnitDescr_Object = MibTableColumn
rbnFanUnitDescr = _RbnFanUnitDescr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 5, 1, 2),
    _RbnFanUnitDescr_Type()
)
rbnFanUnitDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFanUnitDescr.setStatus("current")
_RbnFanSpeedCurrent_Type = RbnFanSpeed
_RbnFanSpeedCurrent_Object = MibTableColumn
rbnFanSpeedCurrent = _RbnFanSpeedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 5, 1, 3),
    _RbnFanSpeedCurrent_Type()
)
rbnFanSpeedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFanSpeedCurrent.setStatus("current")
_RbnEntityTempSensorTable_Object = MibTable
rbnEntityTempSensorTable = _RbnEntityTempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 6)
)
if mibBuilder.loadTexts:
    rbnEntityTempSensorTable.setStatus("current")
_RbnEntityTempSensorEntry_Object = MibTableRow
rbnEntityTempSensorEntry = _RbnEntityTempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 6, 1)
)
rbnEntityTempSensorEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "RBN-ENVMON-MIB", "rbnEntityTempIndex"),
)
if mibBuilder.loadTexts:
    rbnEntityTempSensorEntry.setStatus("current")


class _RbnEntityTempIndex_Type(Integer32):
    """Custom type rbnEntityTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RbnEntityTempIndex_Type.__name__ = "Integer32"
_RbnEntityTempIndex_Object = MibTableColumn
rbnEntityTempIndex = _RbnEntityTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 6, 1, 1),
    _RbnEntityTempIndex_Type()
)
rbnEntityTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnEntityTempIndex.setStatus("current")


class _RbnEntityTempDescr_Type(DisplayString):
    """Custom type rbnEntityTempDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_RbnEntityTempDescr_Type.__name__ = "DisplayString"
_RbnEntityTempDescr_Object = MibTableColumn
rbnEntityTempDescr = _RbnEntityTempDescr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 6, 1, 2),
    _RbnEntityTempDescr_Type()
)
rbnEntityTempDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEntityTempDescr.setStatus("current")
_RbnEntityTempCurrent_Type = RbnTemperature
_RbnEntityTempCurrent_Object = MibTableColumn
rbnEntityTempCurrent = _RbnEntityTempCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 6, 1, 3),
    _RbnEntityTempCurrent_Type()
)
rbnEntityTempCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEntityTempCurrent.setStatus("current")
if mibBuilder.loadTexts:
    rbnEntityTempCurrent.setUnits("degrees Celsius")
_RbnEnvMonMIBConformance_ObjectIdentity = ObjectIdentity
rbnEnvMonMIBConformance = _RbnEnvMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2)
)
_RbnEnvMonMIBGroups_ObjectIdentity = ObjectIdentity
rbnEnvMonMIBGroups = _RbnEnvMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1)
)
_RbnEnvMonMIBCompliances_ObjectIdentity = ObjectIdentity
rbnEnvMonMIBCompliances = _RbnEnvMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 2)
)

# Managed Objects groups

rbnEnvMonMIBObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1, 1)
)
rbnEnvMonMIBObjectGroup.setObjects(
      *(("RBN-ENVMON-MIB", "rbnFanDescr"),
        ("RBN-ENVMON-MIB", "rbnFanFail"),
        ("RBN-ENVMON-MIB", "rbnPowerDescr"),
        ("RBN-ENVMON-MIB", "rbnPowerFail"))
)
if mibBuilder.loadTexts:
    rbnEnvMonMIBObjectGroup.setStatus("deprecated")

rbnEnvMonVoltageObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1, 3)
)
rbnEnvMonVoltageObjectGroup.setObjects(
      *(("RBN-ENVMON-MIB", "rbnVoltageDescr"),
        ("RBN-ENVMON-MIB", "rbnVoltageDesired"),
        ("RBN-ENVMON-MIB", "rbnVoltageCurrent"))
)
if mibBuilder.loadTexts:
    rbnEnvMonVoltageObjectGroup.setStatus("current")

rbnEnvMonTempObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1, 4)
)
rbnEnvMonTempObjectGroup.setObjects(
      *(("RBN-ENVMON-MIB", "rbnCpuTempDescr"),
        ("RBN-ENVMON-MIB", "rbnCpuTempCurrent"))
)
if mibBuilder.loadTexts:
    rbnEnvMonTempObjectGroup.setStatus("deprecated")

rbnEnvMonMIBObjectGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1, 5)
)
rbnEnvMonMIBObjectGroupV2.setObjects(
      *(("RBN-ENVMON-MIB", "rbnFanDescr"),
        ("RBN-ENVMON-MIB", "rbnFanStatus"),
        ("RBN-ENVMON-MIB", "rbnPowerDescr"),
        ("RBN-ENVMON-MIB", "rbnPowerStatus"))
)
if mibBuilder.loadTexts:
    rbnEnvMonMIBObjectGroupV2.setStatus("current")

rbnEnvMonFanSpeedObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1, 7)
)
rbnEnvMonFanSpeedObjectGroup.setObjects(
      *(("RBN-ENVMON-MIB", "rbnFanUnitDescr"),
        ("RBN-ENVMON-MIB", "rbnFanSpeedCurrent"))
)
if mibBuilder.loadTexts:
    rbnEnvMonFanSpeedObjectGroup.setStatus("current")

rbnEnvMonEntityObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1, 8)
)
rbnEnvMonEntityObjectGroup.setObjects(
      *(("RBN-ENVMON-MIB", "rbnEntityTempDescr"),
        ("RBN-ENVMON-MIB", "rbnEntityTempCurrent"))
)
if mibBuilder.loadTexts:
    rbnEnvMonEntityObjectGroup.setStatus("current")


# Notification objects

rbnFanFailChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 0, 1)
)
rbnFanFailChange.setObjects(
    ("RBN-ENVMON-MIB", "rbnFanFail")
)
if mibBuilder.loadTexts:
    rbnFanFailChange.setStatus(
        "deprecated"
    )

rbnPowerFailChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 0, 2)
)
rbnPowerFailChange.setObjects(
    ("RBN-ENVMON-MIB", "rbnPowerFail")
)
if mibBuilder.loadTexts:
    rbnPowerFailChange.setStatus(
        "deprecated"
    )

rbnFanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 0, 3)
)
rbnFanStatusChange.setObjects(
    ("RBN-ENVMON-MIB", "rbnFanStatus")
)
if mibBuilder.loadTexts:
    rbnFanStatusChange.setStatus(
        "current"
    )

rbnPowerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 0, 4)
)
rbnPowerStatusChange.setObjects(
    ("RBN-ENVMON-MIB", "rbnPowerStatus")
)
if mibBuilder.loadTexts:
    rbnPowerStatusChange.setStatus(
        "current"
    )


# Notifications groups

rbnEnvMonMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1, 2)
)
rbnEnvMonMIBNotificationGroup.setObjects(
      *(("RBN-ENVMON-MIB", "rbnFanFailChange"),
        ("RBN-ENVMON-MIB", "rbnPowerFailChange"))
)
if mibBuilder.loadTexts:
    rbnEnvMonMIBNotificationGroup.setStatus(
        "deprecated"
    )

rbnEnvMonMIBNotificationGroupV2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1, 6)
)
rbnEnvMonMIBNotificationGroupV2.setObjects(
      *(("RBN-ENVMON-MIB", "rbnFanStatusChange"),
        ("RBN-ENVMON-MIB", "rbnPowerStatusChange"))
)
if mibBuilder.loadTexts:
    rbnEnvMonMIBNotificationGroupV2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnEnvMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 2, 1)
)
rbnEnvMonMIBCompliance.setObjects(
      *(("RBN-ENVMON-MIB", "rbnEnvMonMIBObjectGroup"),
        ("RBN-ENVMON-MIB", "rbnEnvMonMIBNotificationGroup"))
)
if mibBuilder.loadTexts:
    rbnEnvMonMIBCompliance.setStatus(
        "obsolete"
    )

rbnEnvMonMIBComplianceV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 2, 2)
)
rbnEnvMonMIBComplianceV2.setObjects(
      *(("RBN-ENVMON-MIB", "rbnEnvMonMIBObjectGroup"),
        ("RBN-ENVMON-MIB", "rbnEnvMonMIBNotificationGroup"),
        ("RBN-ENVMON-MIB", "rbnEnvMonVoltageObjectGroup"),
        ("RBN-ENVMON-MIB", "rbnEnvMonTempObjectGroup"))
)
if mibBuilder.loadTexts:
    rbnEnvMonMIBComplianceV2.setStatus(
        "deprecated"
    )

rbnEnvMonMIBComplianceV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 2, 3)
)
rbnEnvMonMIBComplianceV3.setObjects(
      *(("RBN-ENVMON-MIB", "rbnEnvMonMIBObjectGroupV2"),
        ("RBN-ENVMON-MIB", "rbnEnvMonMIBNotificationGroupV2"),
        ("RBN-ENVMON-MIB", "rbnEnvMonVoltageObjectGroup"),
        ("RBN-ENVMON-MIB", "rbnEnvMonTempObjectGroup"))
)
if mibBuilder.loadTexts:
    rbnEnvMonMIBComplianceV3.setStatus(
        "deprecated"
    )

rbnEnvMonMIBComplianceV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 2, 4)
)
rbnEnvMonMIBComplianceV4.setObjects(
      *(("RBN-ENVMON-MIB", "rbnEnvMonMIBObjectGroupV2"),
        ("RBN-ENVMON-MIB", "rbnEnvMonMIBNotificationGroupV2"),
        ("RBN-ENVMON-MIB", "rbnEnvMonVoltageObjectGroup"),
        ("RBN-ENVMON-MIB", "rbnEnvMonTempObjectGroup"),
        ("RBN-ENVMON-MIB", "rbnEnvMonFanSpeedObjectGroup"))
)
if mibBuilder.loadTexts:
    rbnEnvMonMIBComplianceV4.setStatus(
        "deprecated"
    )

rbnEnvMonMIBComplianceV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 2, 5)
)
rbnEnvMonMIBComplianceV5.setObjects(
      *(("RBN-ENVMON-MIB", "rbnEnvMonMIBObjectGroupV2"),
        ("RBN-ENVMON-MIB", "rbnEnvMonMIBNotificationGroupV2"),
        ("RBN-ENVMON-MIB", "rbnEnvMonVoltageObjectGroup"),
        ("RBN-ENVMON-MIB", "rbnEnvMonFanSpeedObjectGroup"),
        ("RBN-ENVMON-MIB", "rbnEnvMonEntityObjectGroup"))
)
if mibBuilder.loadTexts:
    rbnEnvMonMIBComplianceV5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-ENVMON-MIB",
    **{"RbnVoltage": RbnVoltage,
       "RbnTemperature": RbnTemperature,
       "RbnFanSpeed": RbnFanSpeed,
       "rbnEnvMonMIB": rbnEnvMonMIB,
       "rbnEnvMonMIBNotifications": rbnEnvMonMIBNotifications,
       "rbnFanFailChange": rbnFanFailChange,
       "rbnPowerFailChange": rbnPowerFailChange,
       "rbnFanStatusChange": rbnFanStatusChange,
       "rbnPowerStatusChange": rbnPowerStatusChange,
       "rbnEnvMonMIBObjects": rbnEnvMonMIBObjects,
       "rbnFanStatusTable": rbnFanStatusTable,
       "rbnFanStatusEntry": rbnFanStatusEntry,
       "rbnFanIndex": rbnFanIndex,
       "rbnFanDescr": rbnFanDescr,
       "rbnFanFail": rbnFanFail,
       "rbnFanStatus": rbnFanStatus,
       "rbnPowerStatusTable": rbnPowerStatusTable,
       "rbnPowerStatusEntry": rbnPowerStatusEntry,
       "rbnPowerIndex": rbnPowerIndex,
       "rbnPowerDescr": rbnPowerDescr,
       "rbnPowerFail": rbnPowerFail,
       "rbnPowerStatus": rbnPowerStatus,
       "rbnVoltageSensorTable": rbnVoltageSensorTable,
       "rbnVoltageSensorEntry": rbnVoltageSensorEntry,
       "rbnVoltageIndex": rbnVoltageIndex,
       "rbnVoltageDescr": rbnVoltageDescr,
       "rbnVoltageDesired": rbnVoltageDesired,
       "rbnVoltageCurrent": rbnVoltageCurrent,
       "rbnCpuTempSensorTable": rbnCpuTempSensorTable,
       "rbnCpuTempSensorEntry": rbnCpuTempSensorEntry,
       "rbnCpuTempIndex": rbnCpuTempIndex,
       "rbnCpuTempDescr": rbnCpuTempDescr,
       "rbnCpuTempCurrent": rbnCpuTempCurrent,
       "rbnFanSpeedTable": rbnFanSpeedTable,
       "rbnFanSpeedEntry": rbnFanSpeedEntry,
       "rbnFanUnitID": rbnFanUnitID,
       "rbnFanUnitDescr": rbnFanUnitDescr,
       "rbnFanSpeedCurrent": rbnFanSpeedCurrent,
       "rbnEntityTempSensorTable": rbnEntityTempSensorTable,
       "rbnEntityTempSensorEntry": rbnEntityTempSensorEntry,
       "rbnEntityTempIndex": rbnEntityTempIndex,
       "rbnEntityTempDescr": rbnEntityTempDescr,
       "rbnEntityTempCurrent": rbnEntityTempCurrent,
       "rbnEnvMonMIBConformance": rbnEnvMonMIBConformance,
       "rbnEnvMonMIBGroups": rbnEnvMonMIBGroups,
       "rbnEnvMonMIBObjectGroup": rbnEnvMonMIBObjectGroup,
       "rbnEnvMonMIBNotificationGroup": rbnEnvMonMIBNotificationGroup,
       "rbnEnvMonVoltageObjectGroup": rbnEnvMonVoltageObjectGroup,
       "rbnEnvMonTempObjectGroup": rbnEnvMonTempObjectGroup,
       "rbnEnvMonMIBObjectGroupV2": rbnEnvMonMIBObjectGroupV2,
       "rbnEnvMonMIBNotificationGroupV2": rbnEnvMonMIBNotificationGroupV2,
       "rbnEnvMonFanSpeedObjectGroup": rbnEnvMonFanSpeedObjectGroup,
       "rbnEnvMonEntityObjectGroup": rbnEnvMonEntityObjectGroup,
       "rbnEnvMonMIBCompliances": rbnEnvMonMIBCompliances,
       "rbnEnvMonMIBCompliance": rbnEnvMonMIBCompliance,
       "rbnEnvMonMIBComplianceV2": rbnEnvMonMIBComplianceV2,
       "rbnEnvMonMIBComplianceV3": rbnEnvMonMIBComplianceV3,
       "rbnEnvMonMIBComplianceV4": rbnEnvMonMIBComplianceV4,
       "rbnEnvMonMIBComplianceV5": rbnEnvMonMIBComplianceV5}
)
