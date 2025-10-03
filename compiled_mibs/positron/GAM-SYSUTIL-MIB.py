# SNMP MIB module (GAM-SYSUTIL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\positron\GAM-SYSUTIL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:52 2025
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

(GAMDisplayString,) = mibBuilder.importSymbols(
    "GAM-TC",
    "GAMDisplayString")

(gamMgmt,) = mibBuilder.importSymbols(
    "POSITRON-SMI",
    "gamMgmt")

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


# MODULE-IDENTITY

gamSysutilMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24)
)
if mibBuilder.loadTexts:
    gamSysutilMib.setRevisions(
        ("2016-02-17 00:00",
         "2016-02-15 00:00",
         "2015-11-02 00:00",
         "2015-10-30 00:00",
         "2015-10-20 00:00",
         "2015-10-15 00:00",
         "2014-11-11 00:00",
         "2014-10-10 00:00",
         "2014-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class GAMSysutilPowerSupplyStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("standby", 1),
          ("notPresent", 2))
    )



class GAMSysutilRebootType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReboot", 0),
          ("coldReboot", 1),
          ("warmReboot", 2))
    )



class GAMSysutilTemperatureMonitorSensorType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("board", 0),
          ("junction", 1))
    )



# MIB Managed Objects in the order of their OIDs

_GamSysutilMibObjects_ObjectIdentity = ObjectIdentity
gamSysutilMibObjects = _GamSysutilMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1)
)
_GamSysutilCapabilities_ObjectIdentity = ObjectIdentity
gamSysutilCapabilities = _GamSysutilCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 1)
)
_GamSysutilCapabilitiesWarmRebootSupported_Type = TruthValue
_GamSysutilCapabilitiesWarmRebootSupported_Object = MibScalar
gamSysutilCapabilitiesWarmRebootSupported = _GamSysutilCapabilitiesWarmRebootSupported_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 1, 1),
    _GamSysutilCapabilitiesWarmRebootSupported_Type()
)
gamSysutilCapabilitiesWarmRebootSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilCapabilitiesWarmRebootSupported.setStatus("current")
_GamSysutilCapabilitiesPostSupported_Type = TruthValue
_GamSysutilCapabilitiesPostSupported_Object = MibScalar
gamSysutilCapabilitiesPostSupported = _GamSysutilCapabilitiesPostSupported_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 1, 2),
    _GamSysutilCapabilitiesPostSupported_Type()
)
gamSysutilCapabilitiesPostSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilCapabilitiesPostSupported.setStatus("current")
_GamSysutilCapabilitiesZtpSupported_Type = TruthValue
_GamSysutilCapabilitiesZtpSupported_Object = MibScalar
gamSysutilCapabilitiesZtpSupported = _GamSysutilCapabilitiesZtpSupported_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 1, 3),
    _GamSysutilCapabilitiesZtpSupported_Type()
)
gamSysutilCapabilitiesZtpSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilCapabilitiesZtpSupported.setStatus("current")
_GamSysutilCapabilitiesStackFwChkSupported_Type = TruthValue
_GamSysutilCapabilitiesStackFwChkSupported_Object = MibScalar
gamSysutilCapabilitiesStackFwChkSupported = _GamSysutilCapabilitiesStackFwChkSupported_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 1, 4),
    _GamSysutilCapabilitiesStackFwChkSupported_Type()
)
gamSysutilCapabilitiesStackFwChkSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilCapabilitiesStackFwChkSupported.setStatus("current")
_GamSysutilConfig_ObjectIdentity = ObjectIdentity
gamSysutilConfig = _GamSysutilConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 2)
)
_GamSysutilConfigSystemInfo_ObjectIdentity = ObjectIdentity
gamSysutilConfigSystemInfo = _GamSysutilConfigSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 2, 1)
)


class _GamSysutilConfigSystemInfoHostname_Type(GAMDisplayString):
    """Custom type gamSysutilConfigSystemInfoHostname based on GAMDisplayString"""
    subtypeSpec = GAMDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GamSysutilConfigSystemInfoHostname_Type.__name__ = "GAMDisplayString"
_GamSysutilConfigSystemInfoHostname_Object = MibScalar
gamSysutilConfigSystemInfoHostname = _GamSysutilConfigSystemInfoHostname_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 2, 1, 1),
    _GamSysutilConfigSystemInfoHostname_Type()
)
gamSysutilConfigSystemInfoHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gamSysutilConfigSystemInfoHostname.setStatus("current")


class _GamSysutilConfigSystemInfoContact_Type(GAMDisplayString):
    """Custom type gamSysutilConfigSystemInfoContact based on GAMDisplayString"""
    subtypeSpec = GAMDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GamSysutilConfigSystemInfoContact_Type.__name__ = "GAMDisplayString"
_GamSysutilConfigSystemInfoContact_Object = MibScalar
gamSysutilConfigSystemInfoContact = _GamSysutilConfigSystemInfoContact_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 2, 1, 2),
    _GamSysutilConfigSystemInfoContact_Type()
)
gamSysutilConfigSystemInfoContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gamSysutilConfigSystemInfoContact.setStatus("current")


class _GamSysutilConfigSystemInfoLocation_Type(GAMDisplayString):
    """Custom type gamSysutilConfigSystemInfoLocation based on GAMDisplayString"""
    subtypeSpec = GAMDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GamSysutilConfigSystemInfoLocation_Type.__name__ = "GAMDisplayString"
_GamSysutilConfigSystemInfoLocation_Object = MibScalar
gamSysutilConfigSystemInfoLocation = _GamSysutilConfigSystemInfoLocation_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 2, 1, 3),
    _GamSysutilConfigSystemInfoLocation_Type()
)
gamSysutilConfigSystemInfoLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gamSysutilConfigSystemInfoLocation.setStatus("current")
_GamSysutilConfigSystemTime_ObjectIdentity = ObjectIdentity
gamSysutilConfigSystemTime = _GamSysutilConfigSystemTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 2, 2)
)


class _GamSysutilConfigSystemTimeSystemCurTime_Type(GAMDisplayString):
    """Custom type gamSysutilConfigSystemTimeSystemCurTime based on GAMDisplayString"""
    subtypeSpec = GAMDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_GamSysutilConfigSystemTimeSystemCurTime_Type.__name__ = "GAMDisplayString"
_GamSysutilConfigSystemTimeSystemCurTime_Object = MibScalar
gamSysutilConfigSystemTimeSystemCurTime = _GamSysutilConfigSystemTimeSystemCurTime_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 2, 2, 1),
    _GamSysutilConfigSystemTimeSystemCurTime_Type()
)
gamSysutilConfigSystemTimeSystemCurTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gamSysutilConfigSystemTimeSystemCurTime.setStatus("current")


class _GamSysutilConfigSystemTimeSystemCurTimeFormat_Type(GAMDisplayString):
    """Custom type gamSysutilConfigSystemTimeSystemCurTimeFormat based on GAMDisplayString"""
    subtypeSpec = GAMDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_GamSysutilConfigSystemTimeSystemCurTimeFormat_Type.__name__ = "GAMDisplayString"
_GamSysutilConfigSystemTimeSystemCurTimeFormat_Object = MibScalar
gamSysutilConfigSystemTimeSystemCurTimeFormat = _GamSysutilConfigSystemTimeSystemCurTimeFormat_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 2, 2, 2),
    _GamSysutilConfigSystemTimeSystemCurTimeFormat_Type()
)
gamSysutilConfigSystemTimeSystemCurTimeFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gamSysutilConfigSystemTimeSystemCurTimeFormat.setStatus("current")
_GamSysutilConfigTemperatureMonitorTable_Object = MibTable
gamSysutilConfigTemperatureMonitorTable = _GamSysutilConfigTemperatureMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 2, 3)
)
if mibBuilder.loadTexts:
    gamSysutilConfigTemperatureMonitorTable.setStatus("current")
_GamSysutilConfigTemperatureMonitorEntry_Object = MibTableRow
gamSysutilConfigTemperatureMonitorEntry = _GamSysutilConfigTemperatureMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 2, 3, 1)
)
gamSysutilConfigTemperatureMonitorEntry.setIndexNames(
    (0, "GAM-SYSUTIL-MIB", "gamSysutilConfigTemperatureMonitorSensorId"),
)
if mibBuilder.loadTexts:
    gamSysutilConfigTemperatureMonitorEntry.setStatus("current")
_GamSysutilConfigTemperatureMonitorSensorId_Type = GAMSysutilTemperatureMonitorSensorType
_GamSysutilConfigTemperatureMonitorSensorId_Object = MibTableColumn
gamSysutilConfigTemperatureMonitorSensorId = _GamSysutilConfigTemperatureMonitorSensorId_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 2, 3, 1, 1),
    _GamSysutilConfigTemperatureMonitorSensorId_Type()
)
gamSysutilConfigTemperatureMonitorSensorId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gamSysutilConfigTemperatureMonitorSensorId.setStatus("current")


class _GamSysutilConfigTemperatureMonitorLowThreshold_Type(Integer32):
    """Custom type gamSysutilConfigTemperatureMonitorLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 125),
    )


_GamSysutilConfigTemperatureMonitorLowThreshold_Type.__name__ = "Integer32"
_GamSysutilConfigTemperatureMonitorLowThreshold_Object = MibTableColumn
gamSysutilConfigTemperatureMonitorLowThreshold = _GamSysutilConfigTemperatureMonitorLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 2, 3, 1, 2),
    _GamSysutilConfigTemperatureMonitorLowThreshold_Type()
)
gamSysutilConfigTemperatureMonitorLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gamSysutilConfigTemperatureMonitorLowThreshold.setStatus("current")


class _GamSysutilConfigTemperatureMonitorHighThreshold_Type(Integer32):
    """Custom type gamSysutilConfigTemperatureMonitorHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 125),
    )


_GamSysutilConfigTemperatureMonitorHighThreshold_Type.__name__ = "Integer32"
_GamSysutilConfigTemperatureMonitorHighThreshold_Object = MibTableColumn
gamSysutilConfigTemperatureMonitorHighThreshold = _GamSysutilConfigTemperatureMonitorHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 2, 3, 1, 3),
    _GamSysutilConfigTemperatureMonitorHighThreshold_Type()
)
gamSysutilConfigTemperatureMonitorHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gamSysutilConfigTemperatureMonitorHighThreshold.setStatus("current")


class _GamSysutilConfigTemperatureMonitorCriticalThreshold_Type(Integer32):
    """Custom type gamSysutilConfigTemperatureMonitorCriticalThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 150),
    )


_GamSysutilConfigTemperatureMonitorCriticalThreshold_Type.__name__ = "Integer32"
_GamSysutilConfigTemperatureMonitorCriticalThreshold_Object = MibTableColumn
gamSysutilConfigTemperatureMonitorCriticalThreshold = _GamSysutilConfigTemperatureMonitorCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 2, 3, 1, 4),
    _GamSysutilConfigTemperatureMonitorCriticalThreshold_Type()
)
gamSysutilConfigTemperatureMonitorCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gamSysutilConfigTemperatureMonitorCriticalThreshold.setStatus("current")


class _GamSysutilConfigTemperatureMonitorHysteresis_Type(Integer32):
    """Custom type gamSysutilConfigTemperatureMonitorHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_GamSysutilConfigTemperatureMonitorHysteresis_Type.__name__ = "Integer32"
_GamSysutilConfigTemperatureMonitorHysteresis_Object = MibTableColumn
gamSysutilConfigTemperatureMonitorHysteresis = _GamSysutilConfigTemperatureMonitorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 2, 3, 1, 5),
    _GamSysutilConfigTemperatureMonitorHysteresis_Type()
)
gamSysutilConfigTemperatureMonitorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gamSysutilConfigTemperatureMonitorHysteresis.setStatus("current")
_GamSysutilStatus_ObjectIdentity = ObjectIdentity
gamSysutilStatus = _GamSysutilStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3)
)
_GamSysutilStatusCpuLoad_ObjectIdentity = ObjectIdentity
gamSysutilStatusCpuLoad = _GamSysutilStatusCpuLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 1)
)
_GamSysutilStatusCpuLoadAverage100msec_Type = Unsigned32
_GamSysutilStatusCpuLoadAverage100msec_Object = MibScalar
gamSysutilStatusCpuLoadAverage100msec = _GamSysutilStatusCpuLoadAverage100msec_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 1, 1),
    _GamSysutilStatusCpuLoadAverage100msec_Type()
)
gamSysutilStatusCpuLoadAverage100msec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusCpuLoadAverage100msec.setStatus("current")
_GamSysutilStatusCpuLoadAverage1sec_Type = Unsigned32
_GamSysutilStatusCpuLoadAverage1sec_Object = MibScalar
gamSysutilStatusCpuLoadAverage1sec = _GamSysutilStatusCpuLoadAverage1sec_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 1, 2),
    _GamSysutilStatusCpuLoadAverage1sec_Type()
)
gamSysutilStatusCpuLoadAverage1sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusCpuLoadAverage1sec.setStatus("current")
_GamSysutilStatusCpuLoadAverage10sec_Type = Unsigned32
_GamSysutilStatusCpuLoadAverage10sec_Object = MibScalar
gamSysutilStatusCpuLoadAverage10sec = _GamSysutilStatusCpuLoadAverage10sec_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 1, 3),
    _GamSysutilStatusCpuLoadAverage10sec_Type()
)
gamSysutilStatusCpuLoadAverage10sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusCpuLoadAverage10sec.setStatus("current")
_GamSysutilStatusPowerSupplyTable_Object = MibTable
gamSysutilStatusPowerSupplyTable = _GamSysutilStatusPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 2)
)
if mibBuilder.loadTexts:
    gamSysutilStatusPowerSupplyTable.setStatus("current")
_GamSysutilStatusPowerSupplyEntry_Object = MibTableRow
gamSysutilStatusPowerSupplyEntry = _GamSysutilStatusPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 2, 1)
)
gamSysutilStatusPowerSupplyEntry.setIndexNames(
    (0, "GAM-SYSUTIL-MIB", "gamSysutilStatusPowerSupplySwitchId"),
    (0, "GAM-SYSUTIL-MIB", "gamSysutilStatusPowerSupplyPsuId"),
)
if mibBuilder.loadTexts:
    gamSysutilStatusPowerSupplyEntry.setStatus("current")


class _GamSysutilStatusPowerSupplySwitchId_Type(Integer32):
    """Custom type gamSysutilStatusPowerSupplySwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_GamSysutilStatusPowerSupplySwitchId_Type.__name__ = "Integer32"
_GamSysutilStatusPowerSupplySwitchId_Object = MibTableColumn
gamSysutilStatusPowerSupplySwitchId = _GamSysutilStatusPowerSupplySwitchId_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 2, 1, 1),
    _GamSysutilStatusPowerSupplySwitchId_Type()
)
gamSysutilStatusPowerSupplySwitchId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gamSysutilStatusPowerSupplySwitchId.setStatus("current")


class _GamSysutilStatusPowerSupplyPsuId_Type(Integer32):
    """Custom type gamSysutilStatusPowerSupplyPsuId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GamSysutilStatusPowerSupplyPsuId_Type.__name__ = "Integer32"
_GamSysutilStatusPowerSupplyPsuId_Object = MibTableColumn
gamSysutilStatusPowerSupplyPsuId = _GamSysutilStatusPowerSupplyPsuId_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 2, 1, 2),
    _GamSysutilStatusPowerSupplyPsuId_Type()
)
gamSysutilStatusPowerSupplyPsuId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gamSysutilStatusPowerSupplyPsuId.setStatus("current")
_GamSysutilStatusPowerSupplyState_Type = GAMSysutilPowerSupplyStateType
_GamSysutilStatusPowerSupplyState_Object = MibTableColumn
gamSysutilStatusPowerSupplyState = _GamSysutilStatusPowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 2, 1, 3),
    _GamSysutilStatusPowerSupplyState_Type()
)
gamSysutilStatusPowerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusPowerSupplyState.setStatus("current")


class _GamSysutilStatusPowerSupplyDescription_Type(GAMDisplayString):
    """Custom type gamSysutilStatusPowerSupplyDescription based on GAMDisplayString"""
    subtypeSpec = GAMDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_GamSysutilStatusPowerSupplyDescription_Type.__name__ = "GAMDisplayString"
_GamSysutilStatusPowerSupplyDescription_Object = MibTableColumn
gamSysutilStatusPowerSupplyDescription = _GamSysutilStatusPowerSupplyDescription_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 2, 1, 4),
    _GamSysutilStatusPowerSupplyDescription_Type()
)
gamSysutilStatusPowerSupplyDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusPowerSupplyDescription.setStatus("current")
_GamSysutilStatusSystemLedTable_Object = MibTable
gamSysutilStatusSystemLedTable = _GamSysutilStatusSystemLedTable_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 3)
)
if mibBuilder.loadTexts:
    gamSysutilStatusSystemLedTable.setStatus("current")
_GamSysutilStatusSystemLedEntry_Object = MibTableRow
gamSysutilStatusSystemLedEntry = _GamSysutilStatusSystemLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 3, 1)
)
gamSysutilStatusSystemLedEntry.setIndexNames(
    (0, "GAM-SYSUTIL-MIB", "gamSysutilStatusSystemLedSwitchId"),
)
if mibBuilder.loadTexts:
    gamSysutilStatusSystemLedEntry.setStatus("current")


class _GamSysutilStatusSystemLedSwitchId_Type(Integer32):
    """Custom type gamSysutilStatusSystemLedSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_GamSysutilStatusSystemLedSwitchId_Type.__name__ = "Integer32"
_GamSysutilStatusSystemLedSwitchId_Object = MibTableColumn
gamSysutilStatusSystemLedSwitchId = _GamSysutilStatusSystemLedSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 3, 1, 1),
    _GamSysutilStatusSystemLedSwitchId_Type()
)
gamSysutilStatusSystemLedSwitchId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gamSysutilStatusSystemLedSwitchId.setStatus("current")


class _GamSysutilStatusSystemLedDescription_Type(GAMDisplayString):
    """Custom type gamSysutilStatusSystemLedDescription based on GAMDisplayString"""
    subtypeSpec = GAMDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_GamSysutilStatusSystemLedDescription_Type.__name__ = "GAMDisplayString"
_GamSysutilStatusSystemLedDescription_Object = MibTableColumn
gamSysutilStatusSystemLedDescription = _GamSysutilStatusSystemLedDescription_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 3, 1, 2),
    _GamSysutilStatusSystemLedDescription_Type()
)
gamSysutilStatusSystemLedDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusSystemLedDescription.setStatus("current")
_GamSysutilStatusSystemUptime_ObjectIdentity = ObjectIdentity
gamSysutilStatusSystemUptime = _GamSysutilStatusSystemUptime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 4)
)


class _GamSysutilStatusSystemUptimeSystemUptime_Type(GAMDisplayString):
    """Custom type gamSysutilStatusSystemUptimeSystemUptime based on GAMDisplayString"""
    subtypeSpec = GAMDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_GamSysutilStatusSystemUptimeSystemUptime_Type.__name__ = "GAMDisplayString"
_GamSysutilStatusSystemUptimeSystemUptime_Object = MibScalar
gamSysutilStatusSystemUptimeSystemUptime = _GamSysutilStatusSystemUptimeSystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 4, 1),
    _GamSysutilStatusSystemUptimeSystemUptime_Type()
)
gamSysutilStatusSystemUptimeSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusSystemUptimeSystemUptime.setStatus("current")
_GamSysutilStatusBoardInfo_ObjectIdentity = ObjectIdentity
gamSysutilStatusBoardInfo = _GamSysutilStatusBoardInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 5)
)
_GamSysutilStatusBoardInfoBoardMacAddress_Type = MacAddress
_GamSysutilStatusBoardInfoBoardMacAddress_Object = MibScalar
gamSysutilStatusBoardInfoBoardMacAddress = _GamSysutilStatusBoardInfoBoardMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 5, 1),
    _GamSysutilStatusBoardInfoBoardMacAddress_Type()
)
gamSysutilStatusBoardInfoBoardMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusBoardInfoBoardMacAddress.setStatus("current")
_GamSysutilStatusBoardInfoBoardID_Type = Unsigned32
_GamSysutilStatusBoardInfoBoardID_Object = MibScalar
gamSysutilStatusBoardInfoBoardID = _GamSysutilStatusBoardInfoBoardID_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 5, 2),
    _GamSysutilStatusBoardInfoBoardID_Type()
)
gamSysutilStatusBoardInfoBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusBoardInfoBoardID.setStatus("current")


class _GamSysutilStatusBoardInfoBoardSerial_Type(GAMDisplayString):
    """Custom type gamSysutilStatusBoardInfoBoardSerial based on GAMDisplayString"""
    subtypeSpec = GAMDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_GamSysutilStatusBoardInfoBoardSerial_Type.__name__ = "GAMDisplayString"
_GamSysutilStatusBoardInfoBoardSerial_Object = MibScalar
gamSysutilStatusBoardInfoBoardSerial = _GamSysutilStatusBoardInfoBoardSerial_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 5, 3),
    _GamSysutilStatusBoardInfoBoardSerial_Type()
)
gamSysutilStatusBoardInfoBoardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusBoardInfoBoardSerial.setStatus("current")


class _GamSysutilStatusBoardInfoBoardType_Type(GAMDisplayString):
    """Custom type gamSysutilStatusBoardInfoBoardType based on GAMDisplayString"""
    subtypeSpec = GAMDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_GamSysutilStatusBoardInfoBoardType_Type.__name__ = "GAMDisplayString"
_GamSysutilStatusBoardInfoBoardType_Object = MibScalar
gamSysutilStatusBoardInfoBoardType = _GamSysutilStatusBoardInfoBoardType_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 5, 4),
    _GamSysutilStatusBoardInfoBoardType_Type()
)
gamSysutilStatusBoardInfoBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusBoardInfoBoardType.setStatus("current")


class _GamSysutilStatusBoardInfoBoardHwVersion_Type(GAMDisplayString):
    """Custom type gamSysutilStatusBoardInfoBoardHwVersion based on GAMDisplayString"""
    subtypeSpec = GAMDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_GamSysutilStatusBoardInfoBoardHwVersion_Type.__name__ = "GAMDisplayString"
_GamSysutilStatusBoardInfoBoardHwVersion_Object = MibScalar
gamSysutilStatusBoardInfoBoardHwVersion = _GamSysutilStatusBoardInfoBoardHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 5, 5),
    _GamSysutilStatusBoardInfoBoardHwVersion_Type()
)
gamSysutilStatusBoardInfoBoardHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusBoardInfoBoardHwVersion.setStatus("current")
_GamSysutilStatusBoardInfoBoardFPGA1Version_Type = Integer32
_GamSysutilStatusBoardInfoBoardFPGA1Version_Object = MibScalar
gamSysutilStatusBoardInfoBoardFPGA1Version = _GamSysutilStatusBoardInfoBoardFPGA1Version_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 5, 6),
    _GamSysutilStatusBoardInfoBoardFPGA1Version_Type()
)
gamSysutilStatusBoardInfoBoardFPGA1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusBoardInfoBoardFPGA1Version.setStatus("current")
_GamSysutilStatusBoardInfoBoardFPGA2Version_Type = Integer32
_GamSysutilStatusBoardInfoBoardFPGA2Version_Object = MibScalar
gamSysutilStatusBoardInfoBoardFPGA2Version = _GamSysutilStatusBoardInfoBoardFPGA2Version_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 5, 7),
    _GamSysutilStatusBoardInfoBoardFPGA2Version_Type()
)
gamSysutilStatusBoardInfoBoardFPGA2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusBoardInfoBoardFPGA2Version.setStatus("current")


class _GamSysutilStatusBoardInfoBoardNorFlashModel_Type(GAMDisplayString):
    """Custom type gamSysutilStatusBoardInfoBoardNorFlashModel based on GAMDisplayString"""
    subtypeSpec = GAMDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_GamSysutilStatusBoardInfoBoardNorFlashModel_Type.__name__ = "GAMDisplayString"
_GamSysutilStatusBoardInfoBoardNorFlashModel_Object = MibScalar
gamSysutilStatusBoardInfoBoardNorFlashModel = _GamSysutilStatusBoardInfoBoardNorFlashModel_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 5, 8),
    _GamSysutilStatusBoardInfoBoardNorFlashModel_Type()
)
gamSysutilStatusBoardInfoBoardNorFlashModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusBoardInfoBoardNorFlashModel.setStatus("current")


class _GamSysutilStatusBoardInfoBoardMgmtPhyModel_Type(GAMDisplayString):
    """Custom type gamSysutilStatusBoardInfoBoardMgmtPhyModel based on GAMDisplayString"""
    subtypeSpec = GAMDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_GamSysutilStatusBoardInfoBoardMgmtPhyModel_Type.__name__ = "GAMDisplayString"
_GamSysutilStatusBoardInfoBoardMgmtPhyModel_Object = MibScalar
gamSysutilStatusBoardInfoBoardMgmtPhyModel = _GamSysutilStatusBoardInfoBoardMgmtPhyModel_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 5, 9),
    _GamSysutilStatusBoardInfoBoardMgmtPhyModel_Type()
)
gamSysutilStatusBoardInfoBoardMgmtPhyModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusBoardInfoBoardMgmtPhyModel.setStatus("current")
_GamSysutilStatusTemperatureMonitorTable_Object = MibTable
gamSysutilStatusTemperatureMonitorTable = _GamSysutilStatusTemperatureMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 6)
)
if mibBuilder.loadTexts:
    gamSysutilStatusTemperatureMonitorTable.setStatus("current")
_GamSysutilStatusTemperatureMonitorEntry_Object = MibTableRow
gamSysutilStatusTemperatureMonitorEntry = _GamSysutilStatusTemperatureMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 6, 1)
)
gamSysutilStatusTemperatureMonitorEntry.setIndexNames(
    (0, "GAM-SYSUTIL-MIB", "gamSysutilStatusTemperatureMonitorSensorId"),
)
if mibBuilder.loadTexts:
    gamSysutilStatusTemperatureMonitorEntry.setStatus("current")
_GamSysutilStatusTemperatureMonitorSensorId_Type = GAMSysutilTemperatureMonitorSensorType
_GamSysutilStatusTemperatureMonitorSensorId_Object = MibTableColumn
gamSysutilStatusTemperatureMonitorSensorId = _GamSysutilStatusTemperatureMonitorSensorId_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 6, 1, 1),
    _GamSysutilStatusTemperatureMonitorSensorId_Type()
)
gamSysutilStatusTemperatureMonitorSensorId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gamSysutilStatusTemperatureMonitorSensorId.setStatus("current")
_GamSysutilStatusTemperatureMonitorLowAlarm_Type = TruthValue
_GamSysutilStatusTemperatureMonitorLowAlarm_Object = MibTableColumn
gamSysutilStatusTemperatureMonitorLowAlarm = _GamSysutilStatusTemperatureMonitorLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 6, 1, 2),
    _GamSysutilStatusTemperatureMonitorLowAlarm_Type()
)
gamSysutilStatusTemperatureMonitorLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusTemperatureMonitorLowAlarm.setStatus("current")
_GamSysutilStatusTemperatureMonitorHighAlarm_Type = TruthValue
_GamSysutilStatusTemperatureMonitorHighAlarm_Object = MibTableColumn
gamSysutilStatusTemperatureMonitorHighAlarm = _GamSysutilStatusTemperatureMonitorHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 6, 1, 3),
    _GamSysutilStatusTemperatureMonitorHighAlarm_Type()
)
gamSysutilStatusTemperatureMonitorHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusTemperatureMonitorHighAlarm.setStatus("current")
_GamSysutilStatusTemperatureMonitorCriticalAlarm_Type = TruthValue
_GamSysutilStatusTemperatureMonitorCriticalAlarm_Object = MibTableColumn
gamSysutilStatusTemperatureMonitorCriticalAlarm = _GamSysutilStatusTemperatureMonitorCriticalAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 6, 1, 4),
    _GamSysutilStatusTemperatureMonitorCriticalAlarm_Type()
)
gamSysutilStatusTemperatureMonitorCriticalAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusTemperatureMonitorCriticalAlarm.setStatus("current")
_GamSysutilStatusTemperatureMonitorTemperature_Type = Integer32
_GamSysutilStatusTemperatureMonitorTemperature_Object = MibTableColumn
gamSysutilStatusTemperatureMonitorTemperature = _GamSysutilStatusTemperatureMonitorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 6, 1, 5),
    _GamSysutilStatusTemperatureMonitorTemperature_Type()
)
gamSysutilStatusTemperatureMonitorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusTemperatureMonitorTemperature.setStatus("current")
_GamSysutilStatusTemperatureSensorsTable_Object = MibTable
gamSysutilStatusTemperatureSensorsTable = _GamSysutilStatusTemperatureSensorsTable_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 7)
)
if mibBuilder.loadTexts:
    gamSysutilStatusTemperatureSensorsTable.setStatus("current")
_GamSysutilStatusTemperatureSensorsEntry_Object = MibTableRow
gamSysutilStatusTemperatureSensorsEntry = _GamSysutilStatusTemperatureSensorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 7, 1)
)
gamSysutilStatusTemperatureSensorsEntry.setIndexNames(
    (0, "GAM-SYSUTIL-MIB", "gamSysutilStatusTemperatureSensorsSensorId"),
)
if mibBuilder.loadTexts:
    gamSysutilStatusTemperatureSensorsEntry.setStatus("current")
_GamSysutilStatusTemperatureSensorsSensorId_Type = Unsigned32
_GamSysutilStatusTemperatureSensorsSensorId_Object = MibTableColumn
gamSysutilStatusTemperatureSensorsSensorId = _GamSysutilStatusTemperatureSensorsSensorId_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 7, 1, 1),
    _GamSysutilStatusTemperatureSensorsSensorId_Type()
)
gamSysutilStatusTemperatureSensorsSensorId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gamSysutilStatusTemperatureSensorsSensorId.setStatus("current")


class _GamSysutilStatusTemperatureSensorsName_Type(GAMDisplayString):
    """Custom type gamSysutilStatusTemperatureSensorsName based on GAMDisplayString"""
    subtypeSpec = GAMDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GamSysutilStatusTemperatureSensorsName_Type.__name__ = "GAMDisplayString"
_GamSysutilStatusTemperatureSensorsName_Object = MibTableColumn
gamSysutilStatusTemperatureSensorsName = _GamSysutilStatusTemperatureSensorsName_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 7, 1, 2),
    _GamSysutilStatusTemperatureSensorsName_Type()
)
gamSysutilStatusTemperatureSensorsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusTemperatureSensorsName.setStatus("current")
_GamSysutilStatusTemperatureSensorsTemperatureX10_Type = Integer32
_GamSysutilStatusTemperatureSensorsTemperatureX10_Object = MibTableColumn
gamSysutilStatusTemperatureSensorsTemperatureX10 = _GamSysutilStatusTemperatureSensorsTemperatureX10_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 7, 1, 3),
    _GamSysutilStatusTemperatureSensorsTemperatureX10_Type()
)
gamSysutilStatusTemperatureSensorsTemperatureX10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusTemperatureSensorsTemperatureX10.setStatus("current")
_GamSysutilStatusFanTable_Object = MibTable
gamSysutilStatusFanTable = _GamSysutilStatusFanTable_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 8)
)
if mibBuilder.loadTexts:
    gamSysutilStatusFanTable.setStatus("current")
_GamSysutilStatusFanEntry_Object = MibTableRow
gamSysutilStatusFanEntry = _GamSysutilStatusFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 8, 1)
)
gamSysutilStatusFanEntry.setIndexNames(
    (0, "GAM-SYSUTIL-MIB", "gamSysutilStatusFanFanId"),
)
if mibBuilder.loadTexts:
    gamSysutilStatusFanEntry.setStatus("current")
_GamSysutilStatusFanFanId_Type = Unsigned32
_GamSysutilStatusFanFanId_Object = MibTableColumn
gamSysutilStatusFanFanId = _GamSysutilStatusFanFanId_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 8, 1, 1),
    _GamSysutilStatusFanFanId_Type()
)
gamSysutilStatusFanFanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gamSysutilStatusFanFanId.setStatus("current")
_GamSysutilStatusFanRPM_Type = Integer32
_GamSysutilStatusFanRPM_Object = MibTableColumn
gamSysutilStatusFanRPM = _GamSysutilStatusFanRPM_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 3, 8, 1, 2),
    _GamSysutilStatusFanRPM_Type()
)
gamSysutilStatusFanRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamSysutilStatusFanRPM.setStatus("current")
_GamSysutilControl_ObjectIdentity = ObjectIdentity
gamSysutilControl = _GamSysutilControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 4)
)
_GamSysutilControlRebootTable_Object = MibTable
gamSysutilControlRebootTable = _GamSysutilControlRebootTable_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 4, 1)
)
if mibBuilder.loadTexts:
    gamSysutilControlRebootTable.setStatus("current")
_GamSysutilControlRebootEntry_Object = MibTableRow
gamSysutilControlRebootEntry = _GamSysutilControlRebootEntry_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 4, 1, 1)
)
gamSysutilControlRebootEntry.setIndexNames(
    (0, "GAM-SYSUTIL-MIB", "gamSysutilControlRebootSwitchId"),
)
if mibBuilder.loadTexts:
    gamSysutilControlRebootEntry.setStatus("current")


class _GamSysutilControlRebootSwitchId_Type(Integer32):
    """Custom type gamSysutilControlRebootSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_GamSysutilControlRebootSwitchId_Type.__name__ = "Integer32"
_GamSysutilControlRebootSwitchId_Object = MibTableColumn
gamSysutilControlRebootSwitchId = _GamSysutilControlRebootSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 4, 1, 1, 1),
    _GamSysutilControlRebootSwitchId_Type()
)
gamSysutilControlRebootSwitchId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gamSysutilControlRebootSwitchId.setStatus("current")
_GamSysutilControlRebootType_Type = GAMSysutilRebootType
_GamSysutilControlRebootType_Object = MibTableColumn
gamSysutilControlRebootType = _GamSysutilControlRebootType_Object(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 1, 4, 1, 1, 2),
    _GamSysutilControlRebootType_Type()
)
gamSysutilControlRebootType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gamSysutilControlRebootType.setStatus("current")
_GamSysutilMibConformance_ObjectIdentity = ObjectIdentity
gamSysutilMibConformance = _GamSysutilMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 2)
)
_GamSysutilMibCompliances_ObjectIdentity = ObjectIdentity
gamSysutilMibCompliances = _GamSysutilMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 2, 1)
)
_GamSysutilMibGroups_ObjectIdentity = ObjectIdentity
gamSysutilMibGroups = _GamSysutilMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 2, 2)
)

# Managed Objects groups

gamSysutilCapabilitiesInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 2, 2, 1)
)
gamSysutilCapabilitiesInfoGroup.setObjects(
      *(("GAM-SYSUTIL-MIB", "gamSysutilCapabilitiesWarmRebootSupported"),
        ("GAM-SYSUTIL-MIB", "gamSysutilCapabilitiesPostSupported"),
        ("GAM-SYSUTIL-MIB", "gamSysutilCapabilitiesZtpSupported"),
        ("GAM-SYSUTIL-MIB", "gamSysutilCapabilitiesStackFwChkSupported"))
)
if mibBuilder.loadTexts:
    gamSysutilCapabilitiesInfoGroup.setStatus("current")

gamSysutilConfigSystemInfoInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 2, 2, 2)
)
gamSysutilConfigSystemInfoInfoGroup.setObjects(
      *(("GAM-SYSUTIL-MIB", "gamSysutilConfigSystemInfoHostname"),
        ("GAM-SYSUTIL-MIB", "gamSysutilConfigSystemInfoContact"),
        ("GAM-SYSUTIL-MIB", "gamSysutilConfigSystemInfoLocation"))
)
if mibBuilder.loadTexts:
    gamSysutilConfigSystemInfoInfoGroup.setStatus("current")

gamSysutilConfigSystemTimeInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 2, 2, 3)
)
gamSysutilConfigSystemTimeInfoGroup.setObjects(
      *(("GAM-SYSUTIL-MIB", "gamSysutilConfigSystemTimeSystemCurTime"),
        ("GAM-SYSUTIL-MIB", "gamSysutilConfigSystemTimeSystemCurTimeFormat"))
)
if mibBuilder.loadTexts:
    gamSysutilConfigSystemTimeInfoGroup.setStatus("current")

gamSysutilConfigTemperatureMonitorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 2, 2, 4)
)
gamSysutilConfigTemperatureMonitorInfoGroup.setObjects(
      *(("GAM-SYSUTIL-MIB", "gamSysutilConfigTemperatureMonitorSensorId"),
        ("GAM-SYSUTIL-MIB", "gamSysutilConfigTemperatureMonitorLowThreshold"),
        ("GAM-SYSUTIL-MIB", "gamSysutilConfigTemperatureMonitorHighThreshold"),
        ("GAM-SYSUTIL-MIB", "gamSysutilConfigTemperatureMonitorCriticalThreshold"),
        ("GAM-SYSUTIL-MIB", "gamSysutilConfigTemperatureMonitorHysteresis"))
)
if mibBuilder.loadTexts:
    gamSysutilConfigTemperatureMonitorInfoGroup.setStatus("current")

gamSysutilStatusCpuLoadInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 2, 2, 5)
)
gamSysutilStatusCpuLoadInfoGroup.setObjects(
      *(("GAM-SYSUTIL-MIB", "gamSysutilStatusCpuLoadAverage100msec"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusCpuLoadAverage1sec"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusCpuLoadAverage10sec"))
)
if mibBuilder.loadTexts:
    gamSysutilStatusCpuLoadInfoGroup.setStatus("current")

gamSysutilStatusPowerSupplyInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 2, 2, 6)
)
gamSysutilStatusPowerSupplyInfoGroup.setObjects(
      *(("GAM-SYSUTIL-MIB", "gamSysutilStatusPowerSupplySwitchId"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusPowerSupplyPsuId"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusPowerSupplyState"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusPowerSupplyDescription"))
)
if mibBuilder.loadTexts:
    gamSysutilStatusPowerSupplyInfoGroup.setStatus("current")

gamSysutilStatusSystemLedInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 2, 2, 7)
)
gamSysutilStatusSystemLedInfoGroup.setObjects(
      *(("GAM-SYSUTIL-MIB", "gamSysutilStatusSystemLedSwitchId"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusSystemLedDescription"))
)
if mibBuilder.loadTexts:
    gamSysutilStatusSystemLedInfoGroup.setStatus("current")

gamSysutilStatusSystemUptimeInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 2, 2, 8)
)
gamSysutilStatusSystemUptimeInfoGroup.setObjects(
    ("GAM-SYSUTIL-MIB", "gamSysutilStatusSystemUptimeSystemUptime")
)
if mibBuilder.loadTexts:
    gamSysutilStatusSystemUptimeInfoGroup.setStatus("current")

gamSysutilStatusBoardInfoInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 2, 2, 9)
)
gamSysutilStatusBoardInfoInfoGroup.setObjects(
      *(("GAM-SYSUTIL-MIB", "gamSysutilStatusBoardInfoBoardMacAddress"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusBoardInfoBoardID"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusBoardInfoBoardSerial"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusBoardInfoBoardType"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusBoardInfoBoardHwVersion"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusBoardInfoBoardFPGA1Version"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusBoardInfoBoardFPGA2Version"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusBoardInfoBoardNorFlashModel"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusBoardInfoBoardMgmtPhyModel"))
)
if mibBuilder.loadTexts:
    gamSysutilStatusBoardInfoInfoGroup.setStatus("current")

gamSysutilStatusTemperatureMonitorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 2, 2, 10)
)
gamSysutilStatusTemperatureMonitorInfoGroup.setObjects(
      *(("GAM-SYSUTIL-MIB", "gamSysutilStatusTemperatureMonitorSensorId"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusTemperatureMonitorLowAlarm"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusTemperatureMonitorHighAlarm"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusTemperatureMonitorCriticalAlarm"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusTemperatureMonitorTemperature"))
)
if mibBuilder.loadTexts:
    gamSysutilStatusTemperatureMonitorInfoGroup.setStatus("current")

gamSysutilStatusTemperatureSensorsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 2, 2, 11)
)
gamSysutilStatusTemperatureSensorsInfoGroup.setObjects(
      *(("GAM-SYSUTIL-MIB", "gamSysutilStatusTemperatureSensorsSensorId"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusTemperatureSensorsName"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusTemperatureSensorsTemperatureX10"))
)
if mibBuilder.loadTexts:
    gamSysutilStatusTemperatureSensorsInfoGroup.setStatus("current")

gamSysutilStatusFanInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 2, 2, 12)
)
gamSysutilStatusFanInfoGroup.setObjects(
      *(("GAM-SYSUTIL-MIB", "gamSysutilStatusFanFanId"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusFanRPM"))
)
if mibBuilder.loadTexts:
    gamSysutilStatusFanInfoGroup.setStatus("current")

gamSysutilControlRebootInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 2, 2, 13)
)
gamSysutilControlRebootInfoGroup.setObjects(
      *(("GAM-SYSUTIL-MIB", "gamSysutilControlRebootSwitchId"),
        ("GAM-SYSUTIL-MIB", "gamSysutilControlRebootType"))
)
if mibBuilder.loadTexts:
    gamSysutilControlRebootInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

gamSysutilMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 20095, 2001, 24, 2, 1, 1)
)
gamSysutilMibCompliance.setObjects(
      *(("GAM-SYSUTIL-MIB", "gamSysutilCapabilitiesInfoGroup"),
        ("GAM-SYSUTIL-MIB", "gamSysutilConfigSystemInfoInfoGroup"),
        ("GAM-SYSUTIL-MIB", "gamSysutilConfigSystemTimeInfoGroup"),
        ("GAM-SYSUTIL-MIB", "gamSysutilConfigTemperatureMonitorInfoGroup"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusCpuLoadInfoGroup"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusPowerSupplyInfoGroup"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusSystemLedInfoGroup"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusSystemUptimeInfoGroup"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusBoardInfoInfoGroup"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusTemperatureMonitorInfoGroup"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusTemperatureSensorsInfoGroup"),
        ("GAM-SYSUTIL-MIB", "gamSysutilStatusFanInfoGroup"),
        ("GAM-SYSUTIL-MIB", "gamSysutilControlRebootInfoGroup"))
)
if mibBuilder.loadTexts:
    gamSysutilMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GAM-SYSUTIL-MIB",
    **{"GAMSysutilPowerSupplyStateType": GAMSysutilPowerSupplyStateType,
       "GAMSysutilRebootType": GAMSysutilRebootType,
       "GAMSysutilTemperatureMonitorSensorType": GAMSysutilTemperatureMonitorSensorType,
       "gamSysutilMib": gamSysutilMib,
       "gamSysutilMibObjects": gamSysutilMibObjects,
       "gamSysutilCapabilities": gamSysutilCapabilities,
       "gamSysutilCapabilitiesWarmRebootSupported": gamSysutilCapabilitiesWarmRebootSupported,
       "gamSysutilCapabilitiesPostSupported": gamSysutilCapabilitiesPostSupported,
       "gamSysutilCapabilitiesZtpSupported": gamSysutilCapabilitiesZtpSupported,
       "gamSysutilCapabilitiesStackFwChkSupported": gamSysutilCapabilitiesStackFwChkSupported,
       "gamSysutilConfig": gamSysutilConfig,
       "gamSysutilConfigSystemInfo": gamSysutilConfigSystemInfo,
       "gamSysutilConfigSystemInfoHostname": gamSysutilConfigSystemInfoHostname,
       "gamSysutilConfigSystemInfoContact": gamSysutilConfigSystemInfoContact,
       "gamSysutilConfigSystemInfoLocation": gamSysutilConfigSystemInfoLocation,
       "gamSysutilConfigSystemTime": gamSysutilConfigSystemTime,
       "gamSysutilConfigSystemTimeSystemCurTime": gamSysutilConfigSystemTimeSystemCurTime,
       "gamSysutilConfigSystemTimeSystemCurTimeFormat": gamSysutilConfigSystemTimeSystemCurTimeFormat,
       "gamSysutilConfigTemperatureMonitorTable": gamSysutilConfigTemperatureMonitorTable,
       "gamSysutilConfigTemperatureMonitorEntry": gamSysutilConfigTemperatureMonitorEntry,
       "gamSysutilConfigTemperatureMonitorSensorId": gamSysutilConfigTemperatureMonitorSensorId,
       "gamSysutilConfigTemperatureMonitorLowThreshold": gamSysutilConfigTemperatureMonitorLowThreshold,
       "gamSysutilConfigTemperatureMonitorHighThreshold": gamSysutilConfigTemperatureMonitorHighThreshold,
       "gamSysutilConfigTemperatureMonitorCriticalThreshold": gamSysutilConfigTemperatureMonitorCriticalThreshold,
       "gamSysutilConfigTemperatureMonitorHysteresis": gamSysutilConfigTemperatureMonitorHysteresis,
       "gamSysutilStatus": gamSysutilStatus,
       "gamSysutilStatusCpuLoad": gamSysutilStatusCpuLoad,
       "gamSysutilStatusCpuLoadAverage100msec": gamSysutilStatusCpuLoadAverage100msec,
       "gamSysutilStatusCpuLoadAverage1sec": gamSysutilStatusCpuLoadAverage1sec,
       "gamSysutilStatusCpuLoadAverage10sec": gamSysutilStatusCpuLoadAverage10sec,
       "gamSysutilStatusPowerSupplyTable": gamSysutilStatusPowerSupplyTable,
       "gamSysutilStatusPowerSupplyEntry": gamSysutilStatusPowerSupplyEntry,
       "gamSysutilStatusPowerSupplySwitchId": gamSysutilStatusPowerSupplySwitchId,
       "gamSysutilStatusPowerSupplyPsuId": gamSysutilStatusPowerSupplyPsuId,
       "gamSysutilStatusPowerSupplyState": gamSysutilStatusPowerSupplyState,
       "gamSysutilStatusPowerSupplyDescription": gamSysutilStatusPowerSupplyDescription,
       "gamSysutilStatusSystemLedTable": gamSysutilStatusSystemLedTable,
       "gamSysutilStatusSystemLedEntry": gamSysutilStatusSystemLedEntry,
       "gamSysutilStatusSystemLedSwitchId": gamSysutilStatusSystemLedSwitchId,
       "gamSysutilStatusSystemLedDescription": gamSysutilStatusSystemLedDescription,
       "gamSysutilStatusSystemUptime": gamSysutilStatusSystemUptime,
       "gamSysutilStatusSystemUptimeSystemUptime": gamSysutilStatusSystemUptimeSystemUptime,
       "gamSysutilStatusBoardInfo": gamSysutilStatusBoardInfo,
       "gamSysutilStatusBoardInfoBoardMacAddress": gamSysutilStatusBoardInfoBoardMacAddress,
       "gamSysutilStatusBoardInfoBoardID": gamSysutilStatusBoardInfoBoardID,
       "gamSysutilStatusBoardInfoBoardSerial": gamSysutilStatusBoardInfoBoardSerial,
       "gamSysutilStatusBoardInfoBoardType": gamSysutilStatusBoardInfoBoardType,
       "gamSysutilStatusBoardInfoBoardHwVersion": gamSysutilStatusBoardInfoBoardHwVersion,
       "gamSysutilStatusBoardInfoBoardFPGA1Version": gamSysutilStatusBoardInfoBoardFPGA1Version,
       "gamSysutilStatusBoardInfoBoardFPGA2Version": gamSysutilStatusBoardInfoBoardFPGA2Version,
       "gamSysutilStatusBoardInfoBoardNorFlashModel": gamSysutilStatusBoardInfoBoardNorFlashModel,
       "gamSysutilStatusBoardInfoBoardMgmtPhyModel": gamSysutilStatusBoardInfoBoardMgmtPhyModel,
       "gamSysutilStatusTemperatureMonitorTable": gamSysutilStatusTemperatureMonitorTable,
       "gamSysutilStatusTemperatureMonitorEntry": gamSysutilStatusTemperatureMonitorEntry,
       "gamSysutilStatusTemperatureMonitorSensorId": gamSysutilStatusTemperatureMonitorSensorId,
       "gamSysutilStatusTemperatureMonitorLowAlarm": gamSysutilStatusTemperatureMonitorLowAlarm,
       "gamSysutilStatusTemperatureMonitorHighAlarm": gamSysutilStatusTemperatureMonitorHighAlarm,
       "gamSysutilStatusTemperatureMonitorCriticalAlarm": gamSysutilStatusTemperatureMonitorCriticalAlarm,
       "gamSysutilStatusTemperatureMonitorTemperature": gamSysutilStatusTemperatureMonitorTemperature,
       "gamSysutilStatusTemperatureSensorsTable": gamSysutilStatusTemperatureSensorsTable,
       "gamSysutilStatusTemperatureSensorsEntry": gamSysutilStatusTemperatureSensorsEntry,
       "gamSysutilStatusTemperatureSensorsSensorId": gamSysutilStatusTemperatureSensorsSensorId,
       "gamSysutilStatusTemperatureSensorsName": gamSysutilStatusTemperatureSensorsName,
       "gamSysutilStatusTemperatureSensorsTemperatureX10": gamSysutilStatusTemperatureSensorsTemperatureX10,
       "gamSysutilStatusFanTable": gamSysutilStatusFanTable,
       "gamSysutilStatusFanEntry": gamSysutilStatusFanEntry,
       "gamSysutilStatusFanFanId": gamSysutilStatusFanFanId,
       "gamSysutilStatusFanRPM": gamSysutilStatusFanRPM,
       "gamSysutilControl": gamSysutilControl,
       "gamSysutilControlRebootTable": gamSysutilControlRebootTable,
       "gamSysutilControlRebootEntry": gamSysutilControlRebootEntry,
       "gamSysutilControlRebootSwitchId": gamSysutilControlRebootSwitchId,
       "gamSysutilControlRebootType": gamSysutilControlRebootType,
       "gamSysutilMibConformance": gamSysutilMibConformance,
       "gamSysutilMibCompliances": gamSysutilMibCompliances,
       "gamSysutilMibCompliance": gamSysutilMibCompliance,
       "gamSysutilMibGroups": gamSysutilMibGroups,
       "gamSysutilCapabilitiesInfoGroup": gamSysutilCapabilitiesInfoGroup,
       "gamSysutilConfigSystemInfoInfoGroup": gamSysutilConfigSystemInfoInfoGroup,
       "gamSysutilConfigSystemTimeInfoGroup": gamSysutilConfigSystemTimeInfoGroup,
       "gamSysutilConfigTemperatureMonitorInfoGroup": gamSysutilConfigTemperatureMonitorInfoGroup,
       "gamSysutilStatusCpuLoadInfoGroup": gamSysutilStatusCpuLoadInfoGroup,
       "gamSysutilStatusPowerSupplyInfoGroup": gamSysutilStatusPowerSupplyInfoGroup,
       "gamSysutilStatusSystemLedInfoGroup": gamSysutilStatusSystemLedInfoGroup,
       "gamSysutilStatusSystemUptimeInfoGroup": gamSysutilStatusSystemUptimeInfoGroup,
       "gamSysutilStatusBoardInfoInfoGroup": gamSysutilStatusBoardInfoInfoGroup,
       "gamSysutilStatusTemperatureMonitorInfoGroup": gamSysutilStatusTemperatureMonitorInfoGroup,
       "gamSysutilStatusTemperatureSensorsInfoGroup": gamSysutilStatusTemperatureSensorsInfoGroup,
       "gamSysutilStatusFanInfoGroup": gamSysutilStatusFanInfoGroup,
       "gamSysutilControlRebootInfoGroup": gamSysutilControlRebootInfoGroup}
)
