# SNMP MIB module (LENOVO-ENV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\lenovo\LENOVO-ENV-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:08:24 2025
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

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(network_mibs,) = mibBuilder.importSymbols(
    "LENOVO-SMI-MIB",
    "network-mibs")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

lenovoEnvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11)
)
if mibBuilder.loadTexts:
    lenovoEnvMIB.setRevisions(
        ("2016-09-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class LenovoEnvMibPowerSupplyState(TextualConvention, Integer32):
    status = "current"
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
          ("absent", 2),
          ("outputFault", 3))
    )



class LenovoEnvMibFanState(TextualConvention, Integer32):
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
        *(("ok", 0),
          ("absent", 1),
          ("fault", 2))
    )



class LenovoEnvMibTempSensorState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("fault", 1))
    )



class LenovoEnvMibTempSensorThreshold(TextualConvention, Integer32):
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
        *(("warning", 0),
          ("failure", 1),
          ("ok", 2))
    )



class LenovoEnvMibFanAirFlow(TextualConvention, Integer32):
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
        *(("front2back", 0),
          ("back2front", 1),
          ("notinstalled", 2))
    )



# MIB Managed Objects in the order of their OIDs

_LenovoEnvMibObjects_ObjectIdentity = ObjectIdentity
lenovoEnvMibObjects = _LenovoEnvMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1)
)
_LenovoEnvMibPowerSupplyTable_Object = MibTable
lenovoEnvMibPowerSupplyTable = _LenovoEnvMibPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 1)
)
if mibBuilder.loadTexts:
    lenovoEnvMibPowerSupplyTable.setStatus("current")
_LenovoEnvMibPowerSupplyEntry_Object = MibTableRow
lenovoEnvMibPowerSupplyEntry = _LenovoEnvMibPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 1, 1)
)
lenovoEnvMibPowerSupplyEntry.setIndexNames(
    (0, "LENOVO-ENV-MIB", "lenovoEnvMibPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    lenovoEnvMibPowerSupplyEntry.setStatus("current")
_LenovoEnvMibPowerSupplyIndex_Type = PhysicalIndex
_LenovoEnvMibPowerSupplyIndex_Object = MibTableColumn
lenovoEnvMibPowerSupplyIndex = _LenovoEnvMibPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 1, 1, 1),
    _LenovoEnvMibPowerSupplyIndex_Type()
)
lenovoEnvMibPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMibPowerSupplyIndex.setStatus("current")
_LenovoEnvMibPowerSupplyID_Type = Integer32
_LenovoEnvMibPowerSupplyID_Object = MibTableColumn
lenovoEnvMibPowerSupplyID = _LenovoEnvMibPowerSupplyID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 1, 1, 2),
    _LenovoEnvMibPowerSupplyID_Type()
)
lenovoEnvMibPowerSupplyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMibPowerSupplyID.setStatus("current")
_LenovoEnvMibPowerSupplyDesc_Type = SnmpAdminString
_LenovoEnvMibPowerSupplyDesc_Object = MibTableColumn
lenovoEnvMibPowerSupplyDesc = _LenovoEnvMibPowerSupplyDesc_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 1, 1, 3),
    _LenovoEnvMibPowerSupplyDesc_Type()
)
lenovoEnvMibPowerSupplyDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMibPowerSupplyDesc.setStatus("current")
_LenovoEnvMibPowerSupplyName_Type = SnmpAdminString
_LenovoEnvMibPowerSupplyName_Object = MibTableColumn
lenovoEnvMibPowerSupplyName = _LenovoEnvMibPowerSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 1, 1, 4),
    _LenovoEnvMibPowerSupplyName_Type()
)
lenovoEnvMibPowerSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMibPowerSupplyName.setStatus("current")
_LenovoEnvMibPowerSupplyState_Type = LenovoEnvMibPowerSupplyState
_LenovoEnvMibPowerSupplyState_Object = MibTableColumn
lenovoEnvMibPowerSupplyState = _LenovoEnvMibPowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 1, 1, 5),
    _LenovoEnvMibPowerSupplyState_Type()
)
lenovoEnvMibPowerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMibPowerSupplyState.setStatus("current")
_LenovoEnvMibFanTable_Object = MibTable
lenovoEnvMibFanTable = _LenovoEnvMibFanTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 2)
)
if mibBuilder.loadTexts:
    lenovoEnvMibFanTable.setStatus("current")
_LenovoEnvMibFanEntry_Object = MibTableRow
lenovoEnvMibFanEntry = _LenovoEnvMibFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 2, 1)
)
lenovoEnvMibFanEntry.setIndexNames(
    (0, "LENOVO-ENV-MIB", "lenovoEnvMibFanIndex"),
)
if mibBuilder.loadTexts:
    lenovoEnvMibFanEntry.setStatus("current")
_LenovoEnvMibFanIndex_Type = PhysicalIndex
_LenovoEnvMibFanIndex_Object = MibTableColumn
lenovoEnvMibFanIndex = _LenovoEnvMibFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 2, 1, 1),
    _LenovoEnvMibFanIndex_Type()
)
lenovoEnvMibFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMibFanIndex.setStatus("current")
_LenovoEnvMibFanID_Type = Integer32
_LenovoEnvMibFanID_Object = MibTableColumn
lenovoEnvMibFanID = _LenovoEnvMibFanID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 2, 1, 2),
    _LenovoEnvMibFanID_Type()
)
lenovoEnvMibFanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMibFanID.setStatus("current")
_LenovoEnvMibFanDesc_Type = SnmpAdminString
_LenovoEnvMibFanDesc_Object = MibTableColumn
lenovoEnvMibFanDesc = _LenovoEnvMibFanDesc_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 2, 1, 3),
    _LenovoEnvMibFanDesc_Type()
)
lenovoEnvMibFanDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMibFanDesc.setStatus("current")
_LenovoEnvMibFanName_Type = SnmpAdminString
_LenovoEnvMibFanName_Object = MibTableColumn
lenovoEnvMibFanName = _LenovoEnvMibFanName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 2, 1, 4),
    _LenovoEnvMibFanName_Type()
)
lenovoEnvMibFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMibFanName.setStatus("current")
_LenovoEnvMibFanState_Type = LenovoEnvMibFanState
_LenovoEnvMibFanState_Object = MibTableColumn
lenovoEnvMibFanState = _LenovoEnvMibFanState_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 2, 1, 5),
    _LenovoEnvMibFanState_Type()
)
lenovoEnvMibFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMibFanState.setStatus("current")
_LenovoEnvMibFanAirFlow_Type = LenovoEnvMibFanAirFlow
_LenovoEnvMibFanAirFlow_Object = MibTableColumn
lenovoEnvMibFanAirFlow = _LenovoEnvMibFanAirFlow_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 2, 1, 6),
    _LenovoEnvMibFanAirFlow_Type()
)
lenovoEnvMibFanAirFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMibFanAirFlow.setStatus("current")
_LenovoEnvMibFanModule_Type = Integer32
_LenovoEnvMibFanModule_Object = MibTableColumn
lenovoEnvMibFanModule = _LenovoEnvMibFanModule_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 2, 1, 7),
    _LenovoEnvMibFanModule_Type()
)
lenovoEnvMibFanModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMibFanModule.setStatus("current")
_LenovoEnvMibFanSpeedRPM_Type = Integer32
_LenovoEnvMibFanSpeedRPM_Object = MibTableColumn
lenovoEnvMibFanSpeedRPM = _LenovoEnvMibFanSpeedRPM_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 2, 1, 8),
    _LenovoEnvMibFanSpeedRPM_Type()
)
lenovoEnvMibFanSpeedRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMibFanSpeedRPM.setStatus("current")
_LenovoEnvMibFanSpeedPercent_Type = Gauge32
_LenovoEnvMibFanSpeedPercent_Object = MibTableColumn
lenovoEnvMibFanSpeedPercent = _LenovoEnvMibFanSpeedPercent_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 2, 1, 9),
    _LenovoEnvMibFanSpeedPercent_Type()
)
lenovoEnvMibFanSpeedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMibFanSpeedPercent.setStatus("current")
_LenovoEnvMibTempSensorTable_Object = MibTable
lenovoEnvMibTempSensorTable = _LenovoEnvMibTempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 3)
)
if mibBuilder.loadTexts:
    lenovoEnvMibTempSensorTable.setStatus("current")
_LenovoEnvMibTempSensorEntry_Object = MibTableRow
lenovoEnvMibTempSensorEntry = _LenovoEnvMibTempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 3, 1)
)
lenovoEnvMibTempSensorEntry.setIndexNames(
    (0, "LENOVO-ENV-MIB", "lenovoEnvMibTempSensorIndex"),
)
if mibBuilder.loadTexts:
    lenovoEnvMibTempSensorEntry.setStatus("current")
_LenovoEnvMibTempSensorIndex_Type = PhysicalIndex
_LenovoEnvMibTempSensorIndex_Object = MibTableColumn
lenovoEnvMibTempSensorIndex = _LenovoEnvMibTempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 3, 1, 1),
    _LenovoEnvMibTempSensorIndex_Type()
)
lenovoEnvMibTempSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMibTempSensorIndex.setStatus("current")
_LenovoEnvMibTempSensorID_Type = Integer32
_LenovoEnvMibTempSensorID_Object = MibTableColumn
lenovoEnvMibTempSensorID = _LenovoEnvMibTempSensorID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 3, 1, 2),
    _LenovoEnvMibTempSensorID_Type()
)
lenovoEnvMibTempSensorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMibTempSensorID.setStatus("current")
_LenovoEnvMibTempSensorDesc_Type = SnmpAdminString
_LenovoEnvMibTempSensorDesc_Object = MibTableColumn
lenovoEnvMibTempSensorDesc = _LenovoEnvMibTempSensorDesc_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 3, 1, 3),
    _LenovoEnvMibTempSensorDesc_Type()
)
lenovoEnvMibTempSensorDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMibTempSensorDesc.setStatus("current")
_LenovoEnvMibTempSensorName_Type = SnmpAdminString
_LenovoEnvMibTempSensorName_Object = MibTableColumn
lenovoEnvMibTempSensorName = _LenovoEnvMibTempSensorName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 3, 1, 4),
    _LenovoEnvMibTempSensorName_Type()
)
lenovoEnvMibTempSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMibTempSensorName.setStatus("current")
_LenovoEnvMibTempSensorState_Type = LenovoEnvMibTempSensorState
_LenovoEnvMibTempSensorState_Object = MibTableColumn
lenovoEnvMibTempSensorState = _LenovoEnvMibTempSensorState_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 3, 1, 5),
    _LenovoEnvMibTempSensorState_Type()
)
lenovoEnvMibTempSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMibTempSensorState.setStatus("current")
_LenovoEnvMibTempSensorTemperature_Type = Integer32
_LenovoEnvMibTempSensorTemperature_Object = MibTableColumn
lenovoEnvMibTempSensorTemperature = _LenovoEnvMibTempSensorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 3, 1, 6),
    _LenovoEnvMibTempSensorTemperature_Type()
)
lenovoEnvMibTempSensorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMibTempSensorTemperature.setStatus("current")
_LenovoEnvMibTempSensorThresholds_ObjectIdentity = ObjectIdentity
lenovoEnvMibTempSensorThresholds = _LenovoEnvMibTempSensorThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 4)
)
_LenovoEnvMIBTempSensorWarning_Type = Integer32
_LenovoEnvMIBTempSensorWarning_Object = MibScalar
lenovoEnvMIBTempSensorWarning = _LenovoEnvMIBTempSensorWarning_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 4, 1),
    _LenovoEnvMIBTempSensorWarning_Type()
)
lenovoEnvMIBTempSensorWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMIBTempSensorWarning.setStatus("current")
_LenovoEnvMIBTempSensorShutdown_Type = Integer32
_LenovoEnvMIBTempSensorShutdown_Object = MibScalar
lenovoEnvMIBTempSensorShutdown = _LenovoEnvMIBTempSensorShutdown_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 4, 2),
    _LenovoEnvMIBTempSensorShutdown_Type()
)
lenovoEnvMIBTempSensorShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMIBTempSensorShutdown.setStatus("current")
_LenovoEnvMIBTempSensorSetPoint_Type = Integer32
_LenovoEnvMIBTempSensorSetPoint_Object = MibScalar
lenovoEnvMIBTempSensorSetPoint = _LenovoEnvMIBTempSensorSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 1, 4, 3),
    _LenovoEnvMIBTempSensorSetPoint_Type()
)
lenovoEnvMIBTempSensorSetPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMIBTempSensorSetPoint.setStatus("current")
_LenovoEnvMibNotificationPrefix_ObjectIdentity = ObjectIdentity
lenovoEnvMibNotificationPrefix = _LenovoEnvMibNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 3)
)
_LenovoEnvMibNotifications_ObjectIdentity = ObjectIdentity
lenovoEnvMibNotifications = _LenovoEnvMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 3, 0)
)
_LenovoEnvMibNotificationObjects_ObjectIdentity = ObjectIdentity
lenovoEnvMibNotificationObjects = _LenovoEnvMibNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 3, 1)
)
_LenovoEnvMibTempSensorThreshold_Type = LenovoEnvMibTempSensorThreshold
_LenovoEnvMibTempSensorThreshold_Object = MibScalar
lenovoEnvMibTempSensorThreshold = _LenovoEnvMibTempSensorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 3, 1, 1),
    _LenovoEnvMibTempSensorThreshold_Type()
)
lenovoEnvMibTempSensorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoEnvMibTempSensorThreshold.setStatus("current")

# Managed Objects groups


# Notification objects

lenovoEnvMibPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 3, 0, 1)
)
lenovoEnvMibPowerSupplyFailure.setObjects(
      *(("LENOVO-ENV-MIB", "lenovoEnvMibPowerSupplyID"),
        ("LENOVO-ENV-MIB", "lenovoEnvMibPowerSupplyName"),
        ("LENOVO-ENV-MIB", "lenovoEnvMibPowerSupplyState"))
)
if mibBuilder.loadTexts:
    lenovoEnvMibPowerSupplyFailure.setStatus(
        "current"
    )

lenovoEnvMibPowerSupplyFixed = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 3, 0, 2)
)
lenovoEnvMibPowerSupplyFixed.setObjects(
      *(("LENOVO-ENV-MIB", "lenovoEnvMibPowerSupplyID"),
        ("LENOVO-ENV-MIB", "lenovoEnvMibPowerSupplyName"),
        ("LENOVO-ENV-MIB", "lenovoEnvMibPowerSupplyState"))
)
if mibBuilder.loadTexts:
    lenovoEnvMibPowerSupplyFixed.setStatus(
        "current"
    )

lenovoEnvMibFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 3, 0, 3)
)
lenovoEnvMibFanFailure.setObjects(
      *(("LENOVO-ENV-MIB", "lenovoEnvMibFanID"),
        ("LENOVO-ENV-MIB", "lenovoEnvMibFanName"),
        ("LENOVO-ENV-MIB", "lenovoEnvMibFanState"),
        ("LENOVO-ENV-MIB", "lenovoEnvMibFanRPM"))
)
if mibBuilder.loadTexts:
    lenovoEnvMibFanFailure.setStatus(
        "current"
    )

lenovoEnvMibFanFixed = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 3, 0, 4)
)
lenovoEnvMibFanFixed.setObjects(
      *(("LENOVO-ENV-MIB", "lenovoEnvMibFanID"),
        ("LENOVO-ENV-MIB", "lenovoEnvMibFanName"),
        ("LENOVO-ENV-MIB", "lenovoEnvMibFanState"),
        ("LENOVO-ENV-MIB", "lenovoEnvMibFanRPM"))
)
if mibBuilder.loadTexts:
    lenovoEnvMibFanFixed.setStatus(
        "current"
    )

lenovoEnvMibTempSensorFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 3, 0, 5)
)
lenovoEnvMibTempSensorFailure.setObjects(
      *(("LENOVO-ENV-MIB", "lenovoEnvMibTempSensorID"),
        ("LENOVO-ENV-MIB", "lenovoEnvMibTempSensorName"),
        ("LENOVO-ENV-MIB", "lenovoEnvMibTempSensorState"),
        ("LENOVO-ENV-MIB", "lenovoEnvMibTempSensorTemperature"),
        ("LENOVO-ENV-MIB", "lenovoEnvMibTempSensorThreshold"))
)
if mibBuilder.loadTexts:
    lenovoEnvMibTempSensorFailure.setStatus(
        "current"
    )

lenovoEnvMibTempSensorFixed = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 2, 3, 11, 3, 0, 6)
)
lenovoEnvMibTempSensorFixed.setObjects(
      *(("LENOVO-ENV-MIB", "lenovoEnvMibTempSensorID"),
        ("LENOVO-ENV-MIB", "lenovoEnvMibTempSensorName"),
        ("LENOVO-ENV-MIB", "lenovoEnvMibTempSensorState"),
        ("LENOVO-ENV-MIB", "lenovoEnvMibTempSensorTemperature"),
        ("LENOVO-ENV-MIB", "lenovoEnvMibTempSensorThreshold"))
)
if mibBuilder.loadTexts:
    lenovoEnvMibTempSensorFixed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LENOVO-ENV-MIB",
    **{"LenovoEnvMibPowerSupplyState": LenovoEnvMibPowerSupplyState,
       "LenovoEnvMibFanState": LenovoEnvMibFanState,
       "LenovoEnvMibTempSensorState": LenovoEnvMibTempSensorState,
       "LenovoEnvMibTempSensorThreshold": LenovoEnvMibTempSensorThreshold,
       "LenovoEnvMibFanAirFlow": LenovoEnvMibFanAirFlow,
       "lenovoEnvMIB": lenovoEnvMIB,
       "lenovoEnvMibObjects": lenovoEnvMibObjects,
       "lenovoEnvMibPowerSupplyTable": lenovoEnvMibPowerSupplyTable,
       "lenovoEnvMibPowerSupplyEntry": lenovoEnvMibPowerSupplyEntry,
       "lenovoEnvMibPowerSupplyIndex": lenovoEnvMibPowerSupplyIndex,
       "lenovoEnvMibPowerSupplyID": lenovoEnvMibPowerSupplyID,
       "lenovoEnvMibPowerSupplyDesc": lenovoEnvMibPowerSupplyDesc,
       "lenovoEnvMibPowerSupplyName": lenovoEnvMibPowerSupplyName,
       "lenovoEnvMibPowerSupplyState": lenovoEnvMibPowerSupplyState,
       "lenovoEnvMibFanTable": lenovoEnvMibFanTable,
       "lenovoEnvMibFanEntry": lenovoEnvMibFanEntry,
       "lenovoEnvMibFanIndex": lenovoEnvMibFanIndex,
       "lenovoEnvMibFanID": lenovoEnvMibFanID,
       "lenovoEnvMibFanDesc": lenovoEnvMibFanDesc,
       "lenovoEnvMibFanName": lenovoEnvMibFanName,
       "lenovoEnvMibFanState": lenovoEnvMibFanState,
       "lenovoEnvMibFanAirFlow": lenovoEnvMibFanAirFlow,
       "lenovoEnvMibFanModule": lenovoEnvMibFanModule,
       "lenovoEnvMibFanSpeedRPM": lenovoEnvMibFanSpeedRPM,
       "lenovoEnvMibFanSpeedPercent": lenovoEnvMibFanSpeedPercent,
       "lenovoEnvMibTempSensorTable": lenovoEnvMibTempSensorTable,
       "lenovoEnvMibTempSensorEntry": lenovoEnvMibTempSensorEntry,
       "lenovoEnvMibTempSensorIndex": lenovoEnvMibTempSensorIndex,
       "lenovoEnvMibTempSensorID": lenovoEnvMibTempSensorID,
       "lenovoEnvMibTempSensorDesc": lenovoEnvMibTempSensorDesc,
       "lenovoEnvMibTempSensorName": lenovoEnvMibTempSensorName,
       "lenovoEnvMibTempSensorState": lenovoEnvMibTempSensorState,
       "lenovoEnvMibTempSensorTemperature": lenovoEnvMibTempSensorTemperature,
       "lenovoEnvMibTempSensorThresholds": lenovoEnvMibTempSensorThresholds,
       "lenovoEnvMIBTempSensorWarning": lenovoEnvMIBTempSensorWarning,
       "lenovoEnvMIBTempSensorShutdown": lenovoEnvMIBTempSensorShutdown,
       "lenovoEnvMIBTempSensorSetPoint": lenovoEnvMIBTempSensorSetPoint,
       "lenovoEnvMibNotificationPrefix": lenovoEnvMibNotificationPrefix,
       "lenovoEnvMibNotifications": lenovoEnvMibNotifications,
       "lenovoEnvMibPowerSupplyFailure": lenovoEnvMibPowerSupplyFailure,
       "lenovoEnvMibPowerSupplyFixed": lenovoEnvMibPowerSupplyFixed,
       "lenovoEnvMibFanFailure": lenovoEnvMibFanFailure,
       "lenovoEnvMibFanFixed": lenovoEnvMibFanFixed,
       "lenovoEnvMibTempSensorFailure": lenovoEnvMibTempSensorFailure,
       "lenovoEnvMibTempSensorFixed": lenovoEnvMibTempSensorFixed,
       "lenovoEnvMibNotificationObjects": lenovoEnvMibNotificationObjects,
       "lenovoEnvMibTempSensorThreshold": lenovoEnvMibTempSensorThreshold}
)
