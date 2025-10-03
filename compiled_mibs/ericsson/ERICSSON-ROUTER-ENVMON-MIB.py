# SNMP MIB module (ERICSSON-ROUTER-ENVMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ericsson\ERICSSON-ROUTER-ENVMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:42:29 2025
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

(eriRouterMgmt,) = mibBuilder.importSymbols(
    "ERICSSON-ROUTER-SMI",
    "eriRouterMgmt")

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

eriRouterEnvMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4)
)
if mibBuilder.loadTexts:
    eriRouterEnvMonMIB.setRevisions(
        ("2015-01-14 18:00",
         "2012-10-03 00:00",
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



class EriRouterVoltage(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )



class EriRouterTemperature(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class EriRouterFanSpeed(TextualConvention, Unsigned32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_EriRouterEnvMonMIBNotifications_ObjectIdentity = ObjectIdentity
eriRouterEnvMonMIBNotifications = _EriRouterEnvMonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 0)
)
_EriRouterEnvMonMIBObjects_ObjectIdentity = ObjectIdentity
eriRouterEnvMonMIBObjects = _EriRouterEnvMonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1)
)
_EriRouterFanStatusTable_Object = MibTable
eriRouterFanStatusTable = _EriRouterFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    eriRouterFanStatusTable.setStatus("current")
_EriRouterFanStatusEntry_Object = MibTableRow
eriRouterFanStatusEntry = _EriRouterFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 1, 1)
)
eriRouterFanStatusEntry.setIndexNames(
    (0, "ERICSSON-ROUTER-ENVMON-MIB", "eriRouterFanIndex"),
)
if mibBuilder.loadTexts:
    eriRouterFanStatusEntry.setStatus("current")


class _EriRouterFanIndex_Type(Integer32):
    """Custom type eriRouterFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EriRouterFanIndex_Type.__name__ = "Integer32"
_EriRouterFanIndex_Object = MibTableColumn
eriRouterFanIndex = _EriRouterFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 1, 1, 1),
    _EriRouterFanIndex_Type()
)
eriRouterFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eriRouterFanIndex.setStatus("current")


class _EriRouterFanDescr_Type(DisplayString):
    """Custom type eriRouterFanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EriRouterFanDescr_Type.__name__ = "DisplayString"
_EriRouterFanDescr_Object = MibTableColumn
eriRouterFanDescr = _EriRouterFanDescr_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 1, 1, 2),
    _EriRouterFanDescr_Type()
)
eriRouterFanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterFanDescr.setStatus("current")
_EriRouterFanFail_Type = TruthValue
_EriRouterFanFail_Object = MibTableColumn
eriRouterFanFail = _EriRouterFanFail_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 1, 1, 3),
    _EriRouterFanFail_Type()
)
eriRouterFanFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterFanFail.setStatus("deprecated")


class _EriRouterFanStatus_Type(Integer32):
    """Custom type eriRouterFanStatus based on Integer32"""
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


_EriRouterFanStatus_Type.__name__ = "Integer32"
_EriRouterFanStatus_Object = MibTableColumn
eriRouterFanStatus = _EriRouterFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 1, 1, 4),
    _EriRouterFanStatus_Type()
)
eriRouterFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterFanStatus.setStatus("current")
_EriRouterPowerStatusTable_Object = MibTable
eriRouterPowerStatusTable = _EriRouterPowerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    eriRouterPowerStatusTable.setStatus("current")
_EriRouterPowerStatusEntry_Object = MibTableRow
eriRouterPowerStatusEntry = _EriRouterPowerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 2, 1)
)
eriRouterPowerStatusEntry.setIndexNames(
    (0, "ERICSSON-ROUTER-ENVMON-MIB", "eriRouterPowerIndex"),
)
if mibBuilder.loadTexts:
    eriRouterPowerStatusEntry.setStatus("current")


class _EriRouterPowerIndex_Type(Integer32):
    """Custom type eriRouterPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EriRouterPowerIndex_Type.__name__ = "Integer32"
_EriRouterPowerIndex_Object = MibTableColumn
eriRouterPowerIndex = _EriRouterPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 2, 1, 1),
    _EriRouterPowerIndex_Type()
)
eriRouterPowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eriRouterPowerIndex.setStatus("current")


class _EriRouterPowerDescr_Type(DisplayString):
    """Custom type eriRouterPowerDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EriRouterPowerDescr_Type.__name__ = "DisplayString"
_EriRouterPowerDescr_Object = MibTableColumn
eriRouterPowerDescr = _EriRouterPowerDescr_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 2, 1, 2),
    _EriRouterPowerDescr_Type()
)
eriRouterPowerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterPowerDescr.setStatus("current")
_EriRouterPowerFail_Type = TruthValue
_EriRouterPowerFail_Object = MibTableColumn
eriRouterPowerFail = _EriRouterPowerFail_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 2, 1, 3),
    _EriRouterPowerFail_Type()
)
eriRouterPowerFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterPowerFail.setStatus("deprecated")


class _EriRouterPowerStatus_Type(Integer32):
    """Custom type eriRouterPowerStatus based on Integer32"""
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


_EriRouterPowerStatus_Type.__name__ = "Integer32"
_EriRouterPowerStatus_Object = MibTableColumn
eriRouterPowerStatus = _EriRouterPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 2, 1, 4),
    _EriRouterPowerStatus_Type()
)
eriRouterPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterPowerStatus.setStatus("current")
_EriRouterVoltageSensorTable_Object = MibTable
eriRouterVoltageSensorTable = _EriRouterVoltageSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 3)
)
if mibBuilder.loadTexts:
    eriRouterVoltageSensorTable.setStatus("current")
_EriRouterVoltageSensorEntry_Object = MibTableRow
eriRouterVoltageSensorEntry = _EriRouterVoltageSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 3, 1)
)
eriRouterVoltageSensorEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "ERICSSON-ROUTER-ENVMON-MIB", "eriRouterVoltageIndex"),
)
if mibBuilder.loadTexts:
    eriRouterVoltageSensorEntry.setStatus("current")


class _EriRouterVoltageIndex_Type(Integer32):
    """Custom type eriRouterVoltageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EriRouterVoltageIndex_Type.__name__ = "Integer32"
_EriRouterVoltageIndex_Object = MibTableColumn
eriRouterVoltageIndex = _EriRouterVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 3, 1, 1),
    _EriRouterVoltageIndex_Type()
)
eriRouterVoltageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eriRouterVoltageIndex.setStatus("current")


class _EriRouterVoltageDescr_Type(DisplayString):
    """Custom type eriRouterVoltageDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_EriRouterVoltageDescr_Type.__name__ = "DisplayString"
_EriRouterVoltageDescr_Object = MibTableColumn
eriRouterVoltageDescr = _EriRouterVoltageDescr_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 3, 1, 2),
    _EriRouterVoltageDescr_Type()
)
eriRouterVoltageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterVoltageDescr.setStatus("current")
_EriRouterVoltageDesired_Type = EriRouterVoltage
_EriRouterVoltageDesired_Object = MibTableColumn
eriRouterVoltageDesired = _EriRouterVoltageDesired_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 3, 1, 3),
    _EriRouterVoltageDesired_Type()
)
eriRouterVoltageDesired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterVoltageDesired.setStatus("current")
if mibBuilder.loadTexts:
    eriRouterVoltageDesired.setUnits("millivolts")
_EriRouterVoltageCurrent_Type = EriRouterVoltage
_EriRouterVoltageCurrent_Object = MibTableColumn
eriRouterVoltageCurrent = _EriRouterVoltageCurrent_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 3, 1, 4),
    _EriRouterVoltageCurrent_Type()
)
eriRouterVoltageCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterVoltageCurrent.setStatus("current")
if mibBuilder.loadTexts:
    eriRouterVoltageCurrent.setUnits("millivolts")
_EriRouterCpuTempSensorTable_Object = MibTable
eriRouterCpuTempSensorTable = _EriRouterCpuTempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 4)
)
if mibBuilder.loadTexts:
    eriRouterCpuTempSensorTable.setStatus("deprecated")
_EriRouterCpuTempSensorEntry_Object = MibTableRow
eriRouterCpuTempSensorEntry = _EriRouterCpuTempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 4, 1)
)
eriRouterCpuTempSensorEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "ERICSSON-ROUTER-ENVMON-MIB", "eriRouterCpuTempIndex"),
)
if mibBuilder.loadTexts:
    eriRouterCpuTempSensorEntry.setStatus("deprecated")


class _EriRouterCpuTempIndex_Type(Integer32):
    """Custom type eriRouterCpuTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EriRouterCpuTempIndex_Type.__name__ = "Integer32"
_EriRouterCpuTempIndex_Object = MibTableColumn
eriRouterCpuTempIndex = _EriRouterCpuTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 4, 1, 1),
    _EriRouterCpuTempIndex_Type()
)
eriRouterCpuTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eriRouterCpuTempIndex.setStatus("deprecated")


class _EriRouterCpuTempDescr_Type(DisplayString):
    """Custom type eriRouterCpuTempDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_EriRouterCpuTempDescr_Type.__name__ = "DisplayString"
_EriRouterCpuTempDescr_Object = MibTableColumn
eriRouterCpuTempDescr = _EriRouterCpuTempDescr_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 4, 1, 2),
    _EriRouterCpuTempDescr_Type()
)
eriRouterCpuTempDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterCpuTempDescr.setStatus("deprecated")
_EriRouterCpuTempCurrent_Type = EriRouterTemperature
_EriRouterCpuTempCurrent_Object = MibTableColumn
eriRouterCpuTempCurrent = _EriRouterCpuTempCurrent_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 4, 1, 3),
    _EriRouterCpuTempCurrent_Type()
)
eriRouterCpuTempCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterCpuTempCurrent.setStatus("deprecated")
if mibBuilder.loadTexts:
    eriRouterCpuTempCurrent.setUnits("degrees")
_EriRouterFanSpeedTable_Object = MibTable
eriRouterFanSpeedTable = _EriRouterFanSpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 5)
)
if mibBuilder.loadTexts:
    eriRouterFanSpeedTable.setStatus("current")
_EriRouterFanSpeedEntry_Object = MibTableRow
eriRouterFanSpeedEntry = _EriRouterFanSpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 5, 1)
)
eriRouterFanSpeedEntry.setIndexNames(
    (0, "ERICSSON-ROUTER-ENVMON-MIB", "eriRouterFanIndex"),
    (0, "ERICSSON-ROUTER-ENVMON-MIB", "eriRouterFanUnitID"),
)
if mibBuilder.loadTexts:
    eriRouterFanSpeedEntry.setStatus("current")


class _EriRouterFanUnitID_Type(Integer32):
    """Custom type eriRouterFanUnitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EriRouterFanUnitID_Type.__name__ = "Integer32"
_EriRouterFanUnitID_Object = MibTableColumn
eriRouterFanUnitID = _EriRouterFanUnitID_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 5, 1, 1),
    _EriRouterFanUnitID_Type()
)
eriRouterFanUnitID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eriRouterFanUnitID.setStatus("current")


class _EriRouterFanUnitDescr_Type(DisplayString):
    """Custom type eriRouterFanUnitDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EriRouterFanUnitDescr_Type.__name__ = "DisplayString"
_EriRouterFanUnitDescr_Object = MibTableColumn
eriRouterFanUnitDescr = _EriRouterFanUnitDescr_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 5, 1, 2),
    _EriRouterFanUnitDescr_Type()
)
eriRouterFanUnitDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterFanUnitDescr.setStatus("current")
_EriRouterFanSpeedCurrent_Type = EriRouterFanSpeed
_EriRouterFanSpeedCurrent_Object = MibTableColumn
eriRouterFanSpeedCurrent = _EriRouterFanSpeedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 5, 1, 3),
    _EriRouterFanSpeedCurrent_Type()
)
eriRouterFanSpeedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterFanSpeedCurrent.setStatus("current")
_EriRouterEntityTempSensorTable_Object = MibTable
eriRouterEntityTempSensorTable = _EriRouterEntityTempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 6)
)
if mibBuilder.loadTexts:
    eriRouterEntityTempSensorTable.setStatus("current")
_EriRouterEntityTempSensorEntry_Object = MibTableRow
eriRouterEntityTempSensorEntry = _EriRouterEntityTempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 6, 1)
)
eriRouterEntityTempSensorEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEntityTempIndex"),
)
if mibBuilder.loadTexts:
    eriRouterEntityTempSensorEntry.setStatus("current")


class _EriRouterEntityTempIndex_Type(Integer32):
    """Custom type eriRouterEntityTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EriRouterEntityTempIndex_Type.__name__ = "Integer32"
_EriRouterEntityTempIndex_Object = MibTableColumn
eriRouterEntityTempIndex = _EriRouterEntityTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 6, 1, 1),
    _EriRouterEntityTempIndex_Type()
)
eriRouterEntityTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eriRouterEntityTempIndex.setStatus("current")


class _EriRouterEntityTempDescr_Type(DisplayString):
    """Custom type eriRouterEntityTempDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_EriRouterEntityTempDescr_Type.__name__ = "DisplayString"
_EriRouterEntityTempDescr_Object = MibTableColumn
eriRouterEntityTempDescr = _EriRouterEntityTempDescr_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 6, 1, 2),
    _EriRouterEntityTempDescr_Type()
)
eriRouterEntityTempDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterEntityTempDescr.setStatus("current")
_EriRouterEntityTempCurrent_Type = EriRouterTemperature
_EriRouterEntityTempCurrent_Object = MibTableColumn
eriRouterEntityTempCurrent = _EriRouterEntityTempCurrent_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 1, 6, 1, 3),
    _EriRouterEntityTempCurrent_Type()
)
eriRouterEntityTempCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterEntityTempCurrent.setStatus("current")
if mibBuilder.loadTexts:
    eriRouterEntityTempCurrent.setUnits("degrees Celsius")
_EriRouterEnvMonMIBConformance_ObjectIdentity = ObjectIdentity
eriRouterEnvMonMIBConformance = _EriRouterEnvMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 2)
)
_EriRouterEnvMonMIBGroups_ObjectIdentity = ObjectIdentity
eriRouterEnvMonMIBGroups = _EriRouterEnvMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 2, 1)
)
_EriRouterEnvMonMIBCompliances_ObjectIdentity = ObjectIdentity
eriRouterEnvMonMIBCompliances = _EriRouterEnvMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 2, 2)
)

# Managed Objects groups

eriRouterEnvMonMIBObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 2, 1, 1)
)
eriRouterEnvMonMIBObjectGroup.setObjects(
      *(("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterFanDescr"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterFanFail"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterPowerDescr"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterPowerFail"))
)
if mibBuilder.loadTexts:
    eriRouterEnvMonMIBObjectGroup.setStatus("deprecated")

eriRouterEnvMonVoltageObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 2, 1, 3)
)
eriRouterEnvMonVoltageObjectGroup.setObjects(
      *(("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterVoltageDescr"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterVoltageDesired"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterVoltageCurrent"))
)
if mibBuilder.loadTexts:
    eriRouterEnvMonVoltageObjectGroup.setStatus("current")

eriRouterEnvMonTempObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 2, 1, 4)
)
eriRouterEnvMonTempObjectGroup.setObjects(
      *(("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterCpuTempDescr"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterCpuTempCurrent"))
)
if mibBuilder.loadTexts:
    eriRouterEnvMonTempObjectGroup.setStatus("deprecated")

eriRouterEnvMonMIBObjectGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 2, 1, 5)
)
eriRouterEnvMonMIBObjectGroupV2.setObjects(
      *(("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterFanDescr"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterFanStatus"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterPowerDescr"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterPowerStatus"))
)
if mibBuilder.loadTexts:
    eriRouterEnvMonMIBObjectGroupV2.setStatus("current")

eriRouterEnvMonFanSpeedObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 2, 1, 7)
)
eriRouterEnvMonFanSpeedObjectGroup.setObjects(
      *(("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterFanUnitDescr"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterFanSpeedCurrent"))
)
if mibBuilder.loadTexts:
    eriRouterEnvMonFanSpeedObjectGroup.setStatus("current")

eriRouterEnvMonEntityObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 2, 1, 8)
)
eriRouterEnvMonEntityObjectGroup.setObjects(
      *(("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEntityTempDescr"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEntityTempCurrent"))
)
if mibBuilder.loadTexts:
    eriRouterEnvMonEntityObjectGroup.setStatus("current")


# Notification objects

eriRouterFanFailChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 0, 1)
)
eriRouterFanFailChange.setObjects(
    ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterFanFail")
)
if mibBuilder.loadTexts:
    eriRouterFanFailChange.setStatus(
        "deprecated"
    )

eriRouterPowerFailChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 0, 2)
)
eriRouterPowerFailChange.setObjects(
    ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterPowerFail")
)
if mibBuilder.loadTexts:
    eriRouterPowerFailChange.setStatus(
        "deprecated"
    )

eriRouterFanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 0, 3)
)
eriRouterFanStatusChange.setObjects(
    ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterFanStatus")
)
if mibBuilder.loadTexts:
    eriRouterFanStatusChange.setStatus(
        "current"
    )

eriRouterPowerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 0, 4)
)
eriRouterPowerStatusChange.setObjects(
    ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterPowerStatus")
)
if mibBuilder.loadTexts:
    eriRouterPowerStatusChange.setStatus(
        "current"
    )


# Notifications groups

eriRouterEnvMonMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 2, 1, 2)
)
eriRouterEnvMonMIBNotificationGroup.setObjects(
      *(("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterFanFailChange"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterPowerFailChange"))
)
if mibBuilder.loadTexts:
    eriRouterEnvMonMIBNotificationGroup.setStatus(
        "deprecated"
    )

eriRouterEnvMonMIBNotificationGroupV2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 2, 1, 6)
)
eriRouterEnvMonMIBNotificationGroupV2.setObjects(
      *(("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterFanStatusChange"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterPowerStatusChange"))
)
if mibBuilder.loadTexts:
    eriRouterEnvMonMIBNotificationGroupV2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

eriRouterEnvMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 2, 2, 1)
)
eriRouterEnvMonMIBCompliance.setObjects(
      *(("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEnvMonMIBObjectGroup"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEnvMonMIBNotificationGroup"))
)
if mibBuilder.loadTexts:
    eriRouterEnvMonMIBCompliance.setStatus(
        "obsolete"
    )

eriRouterEnvMonMIBComplianceV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 2, 2, 2)
)
eriRouterEnvMonMIBComplianceV2.setObjects(
      *(("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEnvMonMIBObjectGroup"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEnvMonMIBNotificationGroup"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEnvMonVoltageObjectGroup"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEnvMonTempObjectGroup"))
)
if mibBuilder.loadTexts:
    eriRouterEnvMonMIBComplianceV2.setStatus(
        "deprecated"
    )

eriRouterEnvMonMIBComplianceV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 2, 2, 3)
)
eriRouterEnvMonMIBComplianceV3.setObjects(
      *(("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEnvMonMIBObjectGroupV2"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEnvMonMIBNotificationGroupV2"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEnvMonVoltageObjectGroup"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEnvMonTempObjectGroup"))
)
if mibBuilder.loadTexts:
    eriRouterEnvMonMIBComplianceV3.setStatus(
        "deprecated"
    )

eriRouterEnvMonMIBComplianceV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 2, 2, 4)
)
eriRouterEnvMonMIBComplianceV4.setObjects(
      *(("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEnvMonMIBObjectGroupV2"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEnvMonMIBNotificationGroupV2"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEnvMonVoltageObjectGroup"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEnvMonTempObjectGroup"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEnvMonFanSpeedObjectGroup"))
)
if mibBuilder.loadTexts:
    eriRouterEnvMonMIBComplianceV4.setStatus(
        "deprecated"
    )

eriRouterEnvMonMIBComplianceV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 4, 2, 2, 5)
)
eriRouterEnvMonMIBComplianceV5.setObjects(
      *(("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEnvMonMIBObjectGroupV2"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEnvMonMIBNotificationGroupV2"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEnvMonVoltageObjectGroup"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEnvMonFanSpeedObjectGroup"),
        ("ERICSSON-ROUTER-ENVMON-MIB", "eriRouterEnvMonEntityObjectGroup"))
)
if mibBuilder.loadTexts:
    eriRouterEnvMonMIBComplianceV5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERICSSON-ROUTER-ENVMON-MIB",
    **{"EriRouterVoltage": EriRouterVoltage,
       "EriRouterTemperature": EriRouterTemperature,
       "EriRouterFanSpeed": EriRouterFanSpeed,
       "eriRouterEnvMonMIB": eriRouterEnvMonMIB,
       "eriRouterEnvMonMIBNotifications": eriRouterEnvMonMIBNotifications,
       "eriRouterFanFailChange": eriRouterFanFailChange,
       "eriRouterPowerFailChange": eriRouterPowerFailChange,
       "eriRouterFanStatusChange": eriRouterFanStatusChange,
       "eriRouterPowerStatusChange": eriRouterPowerStatusChange,
       "eriRouterEnvMonMIBObjects": eriRouterEnvMonMIBObjects,
       "eriRouterFanStatusTable": eriRouterFanStatusTable,
       "eriRouterFanStatusEntry": eriRouterFanStatusEntry,
       "eriRouterFanIndex": eriRouterFanIndex,
       "eriRouterFanDescr": eriRouterFanDescr,
       "eriRouterFanFail": eriRouterFanFail,
       "eriRouterFanStatus": eriRouterFanStatus,
       "eriRouterPowerStatusTable": eriRouterPowerStatusTable,
       "eriRouterPowerStatusEntry": eriRouterPowerStatusEntry,
       "eriRouterPowerIndex": eriRouterPowerIndex,
       "eriRouterPowerDescr": eriRouterPowerDescr,
       "eriRouterPowerFail": eriRouterPowerFail,
       "eriRouterPowerStatus": eriRouterPowerStatus,
       "eriRouterVoltageSensorTable": eriRouterVoltageSensorTable,
       "eriRouterVoltageSensorEntry": eriRouterVoltageSensorEntry,
       "eriRouterVoltageIndex": eriRouterVoltageIndex,
       "eriRouterVoltageDescr": eriRouterVoltageDescr,
       "eriRouterVoltageDesired": eriRouterVoltageDesired,
       "eriRouterVoltageCurrent": eriRouterVoltageCurrent,
       "eriRouterCpuTempSensorTable": eriRouterCpuTempSensorTable,
       "eriRouterCpuTempSensorEntry": eriRouterCpuTempSensorEntry,
       "eriRouterCpuTempIndex": eriRouterCpuTempIndex,
       "eriRouterCpuTempDescr": eriRouterCpuTempDescr,
       "eriRouterCpuTempCurrent": eriRouterCpuTempCurrent,
       "eriRouterFanSpeedTable": eriRouterFanSpeedTable,
       "eriRouterFanSpeedEntry": eriRouterFanSpeedEntry,
       "eriRouterFanUnitID": eriRouterFanUnitID,
       "eriRouterFanUnitDescr": eriRouterFanUnitDescr,
       "eriRouterFanSpeedCurrent": eriRouterFanSpeedCurrent,
       "eriRouterEntityTempSensorTable": eriRouterEntityTempSensorTable,
       "eriRouterEntityTempSensorEntry": eriRouterEntityTempSensorEntry,
       "eriRouterEntityTempIndex": eriRouterEntityTempIndex,
       "eriRouterEntityTempDescr": eriRouterEntityTempDescr,
       "eriRouterEntityTempCurrent": eriRouterEntityTempCurrent,
       "eriRouterEnvMonMIBConformance": eriRouterEnvMonMIBConformance,
       "eriRouterEnvMonMIBGroups": eriRouterEnvMonMIBGroups,
       "eriRouterEnvMonMIBObjectGroup": eriRouterEnvMonMIBObjectGroup,
       "eriRouterEnvMonMIBNotificationGroup": eriRouterEnvMonMIBNotificationGroup,
       "eriRouterEnvMonVoltageObjectGroup": eriRouterEnvMonVoltageObjectGroup,
       "eriRouterEnvMonTempObjectGroup": eriRouterEnvMonTempObjectGroup,
       "eriRouterEnvMonMIBObjectGroupV2": eriRouterEnvMonMIBObjectGroupV2,
       "eriRouterEnvMonMIBNotificationGroupV2": eriRouterEnvMonMIBNotificationGroupV2,
       "eriRouterEnvMonFanSpeedObjectGroup": eriRouterEnvMonFanSpeedObjectGroup,
       "eriRouterEnvMonEntityObjectGroup": eriRouterEnvMonEntityObjectGroup,
       "eriRouterEnvMonMIBCompliances": eriRouterEnvMonMIBCompliances,
       "eriRouterEnvMonMIBCompliance": eriRouterEnvMonMIBCompliance,
       "eriRouterEnvMonMIBComplianceV2": eriRouterEnvMonMIBComplianceV2,
       "eriRouterEnvMonMIBComplianceV3": eriRouterEnvMonMIBComplianceV3,
       "eriRouterEnvMonMIBComplianceV4": eriRouterEnvMonMIBComplianceV4,
       "eriRouterEnvMonMIBComplianceV5": eriRouterEnvMonMIBComplianceV5}
)
