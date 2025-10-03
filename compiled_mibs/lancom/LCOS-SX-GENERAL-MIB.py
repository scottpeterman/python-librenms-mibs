# SNMP MIB module (LCOS-SX-GENERAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\lancom\LCOS-SX-GENERAL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:08:17 2025
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

lcosSXGeneral = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 100)
)
if mibBuilder.loadTexts:
    lcosSXGeneral.setRevisions(
        ("2020-06-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MonitoringSensorType(TextualConvention, Integer32):
    status = "current"
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
        *(("fixed", 1),
          ("removable", 2),
          ("fixedAC", 3),
          ("removableDC", 4),
          ("fixedDC", 5),
          ("removableAC", 6))
    )



class MonitoringModuleStatus(TextualConvention, Integer32):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 1),
          ("operational", 2),
          ("failed", 3),
          ("powering", 4),
          ("nopower", 5),
          ("notpowering", 6),
          ("incompatible", 7),
          ("warning", 8),
          ("present", 9))
    )



class MonitoringTempSensorStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("normal", 1),
          ("warning", 2),
          ("critical", 3),
          ("shutdown", 4),
          ("notpresent", 5),
          ("notoperational", 6))
    )



class LMCStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unpaired", 0),
          ("paired", 1),
          ("disabled", 2),
          ("disabledByWLC", 3),
          ("operating", 4),
          ("httpProtocolError", 5),
          ("httpConnectionError", 6),
          ("dnsError", 7),
          ("memoryError", 8),
          ("notYet", 9),
          ("redirect", 10),
          ("authenticationError", 11),
          ("error", 12),
          ("certificateStorageError", 13),
          ("pairedAndClaimed", 14),
          ("certificateError", 15),
          ("deactivatedNoActivationCode", 16))
    )



# MIB Managed Objects in the order of their OIDs

_LcsNotificationGrp_ObjectIdentity = ObjectIdentity
lcsNotificationGrp = _LcsNotificationGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 100, 0)
)
_LcsTraps_ObjectIdentity = ObjectIdentity
lcsTraps = _LcsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 100, 0, 1)
)
_LcsNotificationVars_ObjectIdentity = ObjectIdentity
lcsNotificationVars = _LcsNotificationVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 100, 0, 2)
)


class _LcsNotificationStateChangeEvent_Type(Integer32):
    """Custom type lcsNotificationStateChangeEvent based on Integer32"""
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
        *(("insertion", 1),
          ("removal", 2),
          ("becomeoperational", 3),
          ("failure", 4),
          ("losepower", 5))
    )


_LcsNotificationStateChangeEvent_Type.__name__ = "Integer32"
_LcsNotificationStateChangeEvent_Object = MibScalar
lcsNotificationStateChangeEvent = _LcsNotificationStateChangeEvent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 0, 2, 100),
    _LcsNotificationStateChangeEvent_Type()
)
lcsNotificationStateChangeEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lcsNotificationStateChangeEvent.setStatus("current")
_LcsNotificationTemperatureStatusCurrent_Type = MonitoringTempSensorStatus
_LcsNotificationTemperatureStatusCurrent_Object = MibScalar
lcsNotificationTemperatureStatusCurrent = _LcsNotificationTemperatureStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 0, 2, 101),
    _LcsNotificationTemperatureStatusCurrent_Type()
)
lcsNotificationTemperatureStatusCurrent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lcsNotificationTemperatureStatusCurrent.setStatus("current")
_LcsNotificationTemperatureStatusPrevious_Type = MonitoringTempSensorStatus
_LcsNotificationTemperatureStatusPrevious_Object = MibScalar
lcsNotificationTemperatureStatusPrevious = _LcsNotificationTemperatureStatusPrevious_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 0, 2, 102),
    _LcsNotificationTemperatureStatusPrevious_Type()
)
lcsNotificationTemperatureStatusPrevious.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lcsNotificationTemperatureStatusPrevious.setStatus("current")
_LcsStatus_ObjectIdentity = ObjectIdentity
lcsStatus = _LcsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1)
)
_LcsMonitoring_ObjectIdentity = ObjectIdentity
lcsMonitoring = _LcsMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1)
)
_LcsMonitoringTempSensorsTable_Object = MibTable
lcsMonitoringTempSensorsTable = _LcsMonitoringTempSensorsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lcsMonitoringTempSensorsTable.setStatus("current")
_LcsMonitoringTempSensorsTableEntry_Object = MibTableRow
lcsMonitoringTempSensorsTableEntry = _LcsMonitoringTempSensorsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 1, 1)
)
lcsMonitoringTempSensorsTableEntry.setIndexNames(
    (0, "LCOS-SX-GENERAL-MIB", "lcsMonitoringTempSensorUnitIndex"),
    (0, "LCOS-SX-GENERAL-MIB", "lcsMonitoringTempSensorIndex"),
)
if mibBuilder.loadTexts:
    lcsMonitoringTempSensorsTableEntry.setStatus("current")


class _LcsMonitoringTempSensorUnitIndex_Type(Unsigned32):
    """Custom type lcsMonitoringTempSensorUnitIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_LcsMonitoringTempSensorUnitIndex_Type.__name__ = "Unsigned32"
_LcsMonitoringTempSensorUnitIndex_Object = MibTableColumn
lcsMonitoringTempSensorUnitIndex = _LcsMonitoringTempSensorUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 1, 1, 1),
    _LcsMonitoringTempSensorUnitIndex_Type()
)
lcsMonitoringTempSensorUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsMonitoringTempSensorUnitIndex.setStatus("current")


class _LcsMonitoringTempSensorIndex_Type(Unsigned32):
    """Custom type lcsMonitoringTempSensorIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_LcsMonitoringTempSensorIndex_Type.__name__ = "Unsigned32"
_LcsMonitoringTempSensorIndex_Object = MibTableColumn
lcsMonitoringTempSensorIndex = _LcsMonitoringTempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 1, 1, 2),
    _LcsMonitoringTempSensorIndex_Type()
)
lcsMonitoringTempSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsMonitoringTempSensorIndex.setStatus("current")
_LcsMonitoringTempSensorDescription_Type = DisplayString
_LcsMonitoringTempSensorDescription_Object = MibTableColumn
lcsMonitoringTempSensorDescription = _LcsMonitoringTempSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 1, 1, 3),
    _LcsMonitoringTempSensorDescription_Type()
)
lcsMonitoringTempSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsMonitoringTempSensorDescription.setStatus("current")
_LcsMonitoringTempSensorType_Type = MonitoringSensorType
_LcsMonitoringTempSensorType_Object = MibTableColumn
lcsMonitoringTempSensorType = _LcsMonitoringTempSensorType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 1, 1, 4),
    _LcsMonitoringTempSensorType_Type()
)
lcsMonitoringTempSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsMonitoringTempSensorType.setStatus("current")
_LcsMonitoringTempSensorState_Type = MonitoringTempSensorStatus
_LcsMonitoringTempSensorState_Object = MibTableColumn
lcsMonitoringTempSensorState = _LcsMonitoringTempSensorState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 1, 1, 5),
    _LcsMonitoringTempSensorState_Type()
)
lcsMonitoringTempSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsMonitoringTempSensorState.setStatus("current")
_LcsMonitoringTempSensorTemperature_Type = Integer32
_LcsMonitoringTempSensorTemperature_Object = MibTableColumn
lcsMonitoringTempSensorTemperature = _LcsMonitoringTempSensorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 1, 1, 6),
    _LcsMonitoringTempSensorTemperature_Type()
)
lcsMonitoringTempSensorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsMonitoringTempSensorTemperature.setStatus("current")
_LcsMonitoringTempUnitTable_Object = MibTable
lcsMonitoringTempUnitTable = _LcsMonitoringTempUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lcsMonitoringTempUnitTable.setStatus("current")
_LcsMonitoringTempUnitEntry_Object = MibTableRow
lcsMonitoringTempUnitEntry = _LcsMonitoringTempUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 2, 1)
)
lcsMonitoringTempUnitEntry.setIndexNames(
    (0, "LCOS-SX-GENERAL-MIB", "lcsMonitoringTempUnitIndex"),
)
if mibBuilder.loadTexts:
    lcsMonitoringTempUnitEntry.setStatus("current")


class _LcsMonitoringTempUnitIndex_Type(Unsigned32):
    """Custom type lcsMonitoringTempUnitIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_LcsMonitoringTempUnitIndex_Type.__name__ = "Unsigned32"
_LcsMonitoringTempUnitIndex_Object = MibTableColumn
lcsMonitoringTempUnitIndex = _LcsMonitoringTempUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 2, 1, 1),
    _LcsMonitoringTempUnitIndex_Type()
)
lcsMonitoringTempUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsMonitoringTempUnitIndex.setStatus("current")
_LcsMonitoringTempUnitState_Type = MonitoringTempSensorStatus
_LcsMonitoringTempUnitState_Object = MibTableColumn
lcsMonitoringTempUnitState = _LcsMonitoringTempUnitState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 2, 1, 2),
    _LcsMonitoringTempUnitState_Type()
)
lcsMonitoringTempUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsMonitoringTempUnitState.setStatus("current")
_LcsMonitoringTempUnitTemperature_Type = Integer32
_LcsMonitoringTempUnitTemperature_Object = MibTableColumn
lcsMonitoringTempUnitTemperature = _LcsMonitoringTempUnitTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 2, 1, 3),
    _LcsMonitoringTempUnitTemperature_Type()
)
lcsMonitoringTempUnitTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsMonitoringTempUnitTemperature.setStatus("current")
_LcsMonitoringFansTable_Object = MibTable
lcsMonitoringFansTable = _LcsMonitoringFansTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 3)
)
if mibBuilder.loadTexts:
    lcsMonitoringFansTable.setStatus("current")
_LcsMonitoringFansTableEntry_Object = MibTableRow
lcsMonitoringFansTableEntry = _LcsMonitoringFansTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 3, 1)
)
lcsMonitoringFansTableEntry.setIndexNames(
    (0, "LCOS-SX-GENERAL-MIB", "lcsMonitoringFanUnitIndex"),
    (0, "LCOS-SX-GENERAL-MIB", "lcsMonitoringFanIndex"),
)
if mibBuilder.loadTexts:
    lcsMonitoringFansTableEntry.setStatus("current")


class _LcsMonitoringFanUnitIndex_Type(Unsigned32):
    """Custom type lcsMonitoringFanUnitIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_LcsMonitoringFanUnitIndex_Type.__name__ = "Unsigned32"
_LcsMonitoringFanUnitIndex_Object = MibTableColumn
lcsMonitoringFanUnitIndex = _LcsMonitoringFanUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 3, 1, 1),
    _LcsMonitoringFanUnitIndex_Type()
)
lcsMonitoringFanUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsMonitoringFanUnitIndex.setStatus("current")


class _LcsMonitoringFanIndex_Type(Unsigned32):
    """Custom type lcsMonitoringFanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_LcsMonitoringFanIndex_Type.__name__ = "Unsigned32"
_LcsMonitoringFanIndex_Object = MibTableColumn
lcsMonitoringFanIndex = _LcsMonitoringFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 3, 1, 2),
    _LcsMonitoringFanIndex_Type()
)
lcsMonitoringFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsMonitoringFanIndex.setStatus("current")
_LcsMonitoringFanDescription_Type = DisplayString
_LcsMonitoringFanDescription_Object = MibTableColumn
lcsMonitoringFanDescription = _LcsMonitoringFanDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 3, 1, 3),
    _LcsMonitoringFanDescription_Type()
)
lcsMonitoringFanDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsMonitoringFanDescription.setStatus("current")
_LcsMonitoringFanType_Type = MonitoringSensorType
_LcsMonitoringFanType_Object = MibTableColumn
lcsMonitoringFanType = _LcsMonitoringFanType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 3, 1, 4),
    _LcsMonitoringFanType_Type()
)
lcsMonitoringFanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsMonitoringFanType.setStatus("current")
_LcsMonitoringFanState_Type = MonitoringModuleStatus
_LcsMonitoringFanState_Object = MibTableColumn
lcsMonitoringFanState = _LcsMonitoringFanState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 3, 1, 5),
    _LcsMonitoringFanState_Type()
)
lcsMonitoringFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsMonitoringFanState.setStatus("current")
_LcsMonitoringFanSpeed_Type = Gauge32
_LcsMonitoringFanSpeed_Object = MibScalar
lcsMonitoringFanSpeed = _LcsMonitoringFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 3, 1, 6),
    _LcsMonitoringFanSpeed_Type()
)
lcsMonitoringFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsMonitoringFanSpeed.setStatus("current")
_LcsMonitoringPSUTable_Object = MibTable
lcsMonitoringPSUTable = _LcsMonitoringPSUTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 4)
)
if mibBuilder.loadTexts:
    lcsMonitoringPSUTable.setStatus("current")
_LcsMonitoringPSUTableEntry_Object = MibTableRow
lcsMonitoringPSUTableEntry = _LcsMonitoringPSUTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 4, 1)
)
lcsMonitoringPSUTableEntry.setIndexNames(
    (0, "LCOS-SX-GENERAL-MIB", "lcsMonitoringPSUUnitIndex"),
    (0, "LCOS-SX-GENERAL-MIB", "lcsMonitoringPSUIndex"),
)
if mibBuilder.loadTexts:
    lcsMonitoringPSUTableEntry.setStatus("current")


class _LcsMonitoringPSUUnitIndex_Type(Unsigned32):
    """Custom type lcsMonitoringPSUUnitIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_LcsMonitoringPSUUnitIndex_Type.__name__ = "Unsigned32"
_LcsMonitoringPSUUnitIndex_Object = MibTableColumn
lcsMonitoringPSUUnitIndex = _LcsMonitoringPSUUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 4, 1, 1),
    _LcsMonitoringPSUUnitIndex_Type()
)
lcsMonitoringPSUUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsMonitoringPSUUnitIndex.setStatus("current")


class _LcsMonitoringPSUIndex_Type(Unsigned32):
    """Custom type lcsMonitoringPSUIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_LcsMonitoringPSUIndex_Type.__name__ = "Unsigned32"
_LcsMonitoringPSUIndex_Object = MibTableColumn
lcsMonitoringPSUIndex = _LcsMonitoringPSUIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 4, 1, 2),
    _LcsMonitoringPSUIndex_Type()
)
lcsMonitoringPSUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsMonitoringPSUIndex.setStatus("current")
_LcsMonitoringPSUDescription_Type = DisplayString
_LcsMonitoringPSUDescription_Object = MibTableColumn
lcsMonitoringPSUDescription = _LcsMonitoringPSUDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 4, 1, 3),
    _LcsMonitoringPSUDescription_Type()
)
lcsMonitoringPSUDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsMonitoringPSUDescription.setStatus("current")
_LcsMonitoringPSUType_Type = MonitoringSensorType
_LcsMonitoringPSUType_Object = MibTableColumn
lcsMonitoringPSUType = _LcsMonitoringPSUType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 4, 1, 4),
    _LcsMonitoringPSUType_Type()
)
lcsMonitoringPSUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsMonitoringPSUType.setStatus("current")
_LcsMonitoringPSUState_Type = MonitoringModuleStatus
_LcsMonitoringPSUState_Object = MibTableColumn
lcsMonitoringPSUState = _LcsMonitoringPSUState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 1, 1, 4, 1, 5),
    _LcsMonitoringPSUState_Type()
)
lcsMonitoringPSUState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsMonitoringPSUState.setStatus("current")
_LcsConfiguration_ObjectIdentity = ObjectIdentity
lcsConfiguration = _LcsConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2)
)
_LcsLMC_ObjectIdentity = ObjectIdentity
lcsLMC = _LcsLMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500)
)
_LcsLMCOperating_Type = Unsigned32
_LcsLMCOperating_Object = MibScalar
lcsLMCOperating = _LcsLMCOperating_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 1),
    _LcsLMCOperating_Type()
)
lcsLMCOperating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcsLMCOperating.setStatus("current")
_LcsLMCConfigViaDHCP_Type = Unsigned32
_LcsLMCConfigViaDHCP_Object = MibScalar
lcsLMCConfigViaDHCP = _LcsLMCConfigViaDHCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 2),
    _LcsLMCConfigViaDHCP_Type()
)
lcsLMCConfigViaDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcsLMCConfigViaDHCP.setStatus("current")
_LcsLMCDomain_Type = DisplayString
_LcsLMCDomain_Object = MibScalar
lcsLMCDomain = _LcsLMCDomain_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 3),
    _LcsLMCDomain_Type()
)
lcsLMCDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcsLMCDomain.setStatus("current")
_LcsLMCAutoRenew_Type = Unsigned32
_LcsLMCAutoRenew_Object = MibScalar
lcsLMCAutoRenew = _LcsLMCAutoRenew_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 4),
    _LcsLMCAutoRenew_Type()
)
lcsLMCAutoRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcsLMCAutoRenew.setStatus("current")
_LcsLMCRolloutProjectID_Type = DisplayString
_LcsLMCRolloutProjectID_Object = MibScalar
lcsLMCRolloutProjectID = _LcsLMCRolloutProjectID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 5),
    _LcsLMCRolloutProjectID_Type()
)
lcsLMCRolloutProjectID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcsLMCRolloutProjectID.setStatus("current")
_LcsLMCRolloutLocationID_Type = DisplayString
_LcsLMCRolloutLocationID_Object = MibScalar
lcsLMCRolloutLocationID = _LcsLMCRolloutLocationID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 6),
    _LcsLMCRolloutLocationID_Type()
)
lcsLMCRolloutLocationID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcsLMCRolloutLocationID.setStatus("current")
_LcsLMCRolloutRole_Type = DisplayString
_LcsLMCRolloutRole_Object = MibScalar
lcsLMCRolloutRole = _LcsLMCRolloutRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 7),
    _LcsLMCRolloutRole_Type()
)
lcsLMCRolloutRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcsLMCRolloutRole.setStatus("current")
_LcsLMCZeroTouchSupport_Type = Unsigned32
_LcsLMCZeroTouchSupport_Object = MibScalar
lcsLMCZeroTouchSupport = _LcsLMCZeroTouchSupport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 50),
    _LcsLMCZeroTouchSupport_Type()
)
lcsLMCZeroTouchSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsLMCZeroTouchSupport.setStatus("current")
_LcsLMCPairingTokenPresent_Type = Unsigned32
_LcsLMCPairingTokenPresent_Object = MibScalar
lcsLMCPairingTokenPresent = _LcsLMCPairingTokenPresent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 51),
    _LcsLMCPairingTokenPresent_Type()
)
lcsLMCPairingTokenPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsLMCPairingTokenPresent.setStatus("current")
_LcsLMCManagementStatus_Type = LMCStatus
_LcsLMCManagementStatus_Object = MibScalar
lcsLMCManagementStatus = _LcsLMCManagementStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 53),
    _LcsLMCManagementStatus_Type()
)
lcsLMCManagementStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsLMCManagementStatus.setStatus("current")
_LcsLMCControlStatus_Type = LMCStatus
_LcsLMCControlStatus_Object = MibScalar
lcsLMCControlStatus = _LcsLMCControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 54),
    _LcsLMCControlStatus_Type()
)
lcsLMCControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsLMCControlStatus.setStatus("current")
_LcsLMCMonitoringStatus_Type = LMCStatus
_LcsLMCMonitoringStatus_Object = MibScalar
lcsLMCMonitoringStatus = _LcsLMCMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 55),
    _LcsLMCMonitoringStatus_Type()
)
lcsLMCMonitoringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsLMCMonitoringStatus.setStatus("current")
_LcsLMCConfigModified_Type = Unsigned32
_LcsLMCConfigModified_Object = MibScalar
lcsLMCConfigModified = _LcsLMCConfigModified_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 57),
    _LcsLMCConfigModified_Type()
)
lcsLMCConfigModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsLMCConfigModified.setStatus("current")
_LcsLMCDeviceID_Type = DisplayString
_LcsLMCDeviceID_Object = MibScalar
lcsLMCDeviceID = _LcsLMCDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 58),
    _LcsLMCDeviceID_Type()
)
lcsLMCDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsLMCDeviceID.setStatus("current")
_LcsLMCStackingStatus_Type = Unsigned32
_LcsLMCStackingStatus_Object = MibScalar
lcsLMCStackingStatus = _LcsLMCStackingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 59),
    _LcsLMCStackingStatus_Type()
)
lcsLMCStackingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsLMCStackingStatus.setStatus("current")
_LcsLMCStatusRTT_Type = Unsigned32
_LcsLMCStatusRTT_Object = MibScalar
lcsLMCStatusRTT = _LcsLMCStatusRTT_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 100),
    _LcsLMCStatusRTT_Type()
)
lcsLMCStatusRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsLMCStatusRTT.setStatus("current")
_LcsLMCTransportStatusTable_Object = MibTable
lcsLMCTransportStatusTable = _LcsLMCTransportStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 101)
)
if mibBuilder.loadTexts:
    lcsLMCTransportStatusTable.setStatus("current")
_LcsLMCTransportStatusTableEntry_Object = MibTableRow
lcsLMCTransportStatusTableEntry = _LcsLMCTransportStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 101, 1)
)
lcsLMCTransportStatusTableEntry.setIndexNames(
    (0, "LCOS-SX-GENERAL-MIB", "lcsLMCTransportStatusTransportNumberIndex"),
)
if mibBuilder.loadTexts:
    lcsLMCTransportStatusTableEntry.setStatus("current")


class _LcsLMCTransportStatusTransportNumberIndex_Type(Integer32):
    """Custom type lcsLMCTransportStatusTransportNumberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcsLMCTransportStatusTransportNumberIndex_Type.__name__ = "Integer32"
_LcsLMCTransportStatusTransportNumberIndex_Object = MibTableColumn
lcsLMCTransportStatusTransportNumberIndex = _LcsLMCTransportStatusTransportNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 101, 1, 1),
    _LcsLMCTransportStatusTransportNumberIndex_Type()
)
lcsLMCTransportStatusTransportNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcsLMCTransportStatusTransportNumberIndex.setStatus("current")
_LcsLMCTransportStatusServiceName_Type = DisplayString
_LcsLMCTransportStatusServiceName_Object = MibTableColumn
lcsLMCTransportStatusServiceName = _LcsLMCTransportStatusServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 101, 1, 2),
    _LcsLMCTransportStatusServiceName_Type()
)
lcsLMCTransportStatusServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsLMCTransportStatusServiceName.setStatus("current")
_LcsLMCTransportStatusHttpRequests_Type = Counter64
_LcsLMCTransportStatusHttpRequests_Object = MibTableColumn
lcsLMCTransportStatusHttpRequests = _LcsLMCTransportStatusHttpRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 101, 1, 3),
    _LcsLMCTransportStatusHttpRequests_Type()
)
lcsLMCTransportStatusHttpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsLMCTransportStatusHttpRequests.setStatus("current")
_LcsLMCTransportStatusHttpRequestsErrors_Type = Counter64
_LcsLMCTransportStatusHttpRequestsErrors_Object = MibTableColumn
lcsLMCTransportStatusHttpRequestsErrors = _LcsLMCTransportStatusHttpRequestsErrors_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 101, 1, 4),
    _LcsLMCTransportStatusHttpRequestsErrors_Type()
)
lcsLMCTransportStatusHttpRequestsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsLMCTransportStatusHttpRequestsErrors.setStatus("current")
_LcsLMCTransportStatusTXBytes_Type = Counter64
_LcsLMCTransportStatusTXBytes_Object = MibTableColumn
lcsLMCTransportStatusTXBytes = _LcsLMCTransportStatusTXBytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 101, 1, 5),
    _LcsLMCTransportStatusTXBytes_Type()
)
lcsLMCTransportStatusTXBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsLMCTransportStatusTXBytes.setStatus("current")
_LcsLMCTransportStatusRXBytes_Type = Counter64
_LcsLMCTransportStatusRXBytes_Object = MibTableColumn
lcsLMCTransportStatusRXBytes = _LcsLMCTransportStatusRXBytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 100, 2, 1500, 101, 1, 7),
    _LcsLMCTransportStatusRXBytes_Type()
)
lcsLMCTransportStatusRXBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcsLMCTransportStatusRXBytes.setStatus("current")

# Managed Objects groups


# Notification objects

lcsTrapsTemperatureStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 100, 0, 1, 100)
)
lcsTrapsTemperatureStateChange.setObjects(
      *(("LCOS-SX-GENERAL-MIB", "lcsMonitoringTempUnitIndex"),
        ("LCOS-SX-GENERAL-MIB", "lcsNotificationTemperatureStatusCurrent"),
        ("LCOS-SX-GENERAL-MIB", "lcsNotificationTemperatureStatusPrevious"))
)
if mibBuilder.loadTexts:
    lcsTrapsTemperatureStateChange.setStatus(
        "current"
    )

lcsTrapsFanStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 100, 0, 1, 101)
)
lcsTrapsFanStateChange.setObjects(
      *(("LCOS-SX-GENERAL-MIB", "lcsMonitoringFanIndex"),
        ("LCOS-SX-GENERAL-MIB", "lcsNotificationStateChangeEvent"))
)
if mibBuilder.loadTexts:
    lcsTrapsFanStateChange.setStatus(
        "current"
    )

lcsTrapsPSUStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 100, 0, 1, 102)
)
lcsTrapsPSUStateChange.setObjects(
      *(("LCOS-SX-GENERAL-MIB", "lcsMonitoringPSUIndex"),
        ("LCOS-SX-GENERAL-MIB", "lcsNotificationStateChangeEvent"))
)
if mibBuilder.loadTexts:
    lcsTrapsPSUStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LCOS-SX-GENERAL-MIB",
    **{"MonitoringSensorType": MonitoringSensorType,
       "MonitoringModuleStatus": MonitoringModuleStatus,
       "MonitoringTempSensorStatus": MonitoringTempSensorStatus,
       "LMCStatus": LMCStatus,
       "lcosSXGeneral": lcosSXGeneral,
       "lcsNotificationGrp": lcsNotificationGrp,
       "lcsTraps": lcsTraps,
       "lcsTrapsTemperatureStateChange": lcsTrapsTemperatureStateChange,
       "lcsTrapsFanStateChange": lcsTrapsFanStateChange,
       "lcsTrapsPSUStateChange": lcsTrapsPSUStateChange,
       "lcsNotificationVars": lcsNotificationVars,
       "lcsNotificationStateChangeEvent": lcsNotificationStateChangeEvent,
       "lcsNotificationTemperatureStatusCurrent": lcsNotificationTemperatureStatusCurrent,
       "lcsNotificationTemperatureStatusPrevious": lcsNotificationTemperatureStatusPrevious,
       "lcsStatus": lcsStatus,
       "lcsMonitoring": lcsMonitoring,
       "lcsMonitoringTempSensorsTable": lcsMonitoringTempSensorsTable,
       "lcsMonitoringTempSensorsTableEntry": lcsMonitoringTempSensorsTableEntry,
       "lcsMonitoringTempSensorUnitIndex": lcsMonitoringTempSensorUnitIndex,
       "lcsMonitoringTempSensorIndex": lcsMonitoringTempSensorIndex,
       "lcsMonitoringTempSensorDescription": lcsMonitoringTempSensorDescription,
       "lcsMonitoringTempSensorType": lcsMonitoringTempSensorType,
       "lcsMonitoringTempSensorState": lcsMonitoringTempSensorState,
       "lcsMonitoringTempSensorTemperature": lcsMonitoringTempSensorTemperature,
       "lcsMonitoringTempUnitTable": lcsMonitoringTempUnitTable,
       "lcsMonitoringTempUnitEntry": lcsMonitoringTempUnitEntry,
       "lcsMonitoringTempUnitIndex": lcsMonitoringTempUnitIndex,
       "lcsMonitoringTempUnitState": lcsMonitoringTempUnitState,
       "lcsMonitoringTempUnitTemperature": lcsMonitoringTempUnitTemperature,
       "lcsMonitoringFansTable": lcsMonitoringFansTable,
       "lcsMonitoringFansTableEntry": lcsMonitoringFansTableEntry,
       "lcsMonitoringFanUnitIndex": lcsMonitoringFanUnitIndex,
       "lcsMonitoringFanIndex": lcsMonitoringFanIndex,
       "lcsMonitoringFanDescription": lcsMonitoringFanDescription,
       "lcsMonitoringFanType": lcsMonitoringFanType,
       "lcsMonitoringFanState": lcsMonitoringFanState,
       "lcsMonitoringFanSpeed": lcsMonitoringFanSpeed,
       "lcsMonitoringPSUTable": lcsMonitoringPSUTable,
       "lcsMonitoringPSUTableEntry": lcsMonitoringPSUTableEntry,
       "lcsMonitoringPSUUnitIndex": lcsMonitoringPSUUnitIndex,
       "lcsMonitoringPSUIndex": lcsMonitoringPSUIndex,
       "lcsMonitoringPSUDescription": lcsMonitoringPSUDescription,
       "lcsMonitoringPSUType": lcsMonitoringPSUType,
       "lcsMonitoringPSUState": lcsMonitoringPSUState,
       "lcsConfiguration": lcsConfiguration,
       "lcsLMC": lcsLMC,
       "lcsLMCOperating": lcsLMCOperating,
       "lcsLMCConfigViaDHCP": lcsLMCConfigViaDHCP,
       "lcsLMCDomain": lcsLMCDomain,
       "lcsLMCAutoRenew": lcsLMCAutoRenew,
       "lcsLMCRolloutProjectID": lcsLMCRolloutProjectID,
       "lcsLMCRolloutLocationID": lcsLMCRolloutLocationID,
       "lcsLMCRolloutRole": lcsLMCRolloutRole,
       "lcsLMCZeroTouchSupport": lcsLMCZeroTouchSupport,
       "lcsLMCPairingTokenPresent": lcsLMCPairingTokenPresent,
       "lcsLMCManagementStatus": lcsLMCManagementStatus,
       "lcsLMCControlStatus": lcsLMCControlStatus,
       "lcsLMCMonitoringStatus": lcsLMCMonitoringStatus,
       "lcsLMCConfigModified": lcsLMCConfigModified,
       "lcsLMCDeviceID": lcsLMCDeviceID,
       "lcsLMCStackingStatus": lcsLMCStackingStatus,
       "lcsLMCStatusRTT": lcsLMCStatusRTT,
       "lcsLMCTransportStatusTable": lcsLMCTransportStatusTable,
       "lcsLMCTransportStatusTableEntry": lcsLMCTransportStatusTableEntry,
       "lcsLMCTransportStatusTransportNumberIndex": lcsLMCTransportStatusTransportNumberIndex,
       "lcsLMCTransportStatusServiceName": lcsLMCTransportStatusServiceName,
       "lcsLMCTransportStatusHttpRequests": lcsLMCTransportStatusHttpRequests,
       "lcsLMCTransportStatusHttpRequestsErrors": lcsLMCTransportStatusHttpRequestsErrors,
       "lcsLMCTransportStatusTXBytes": lcsLMCTransportStatusTXBytes,
       "lcsLMCTransportStatusRXBytes": lcsLMCTransportStatusRXBytes}
)
