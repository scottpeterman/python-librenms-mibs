# SNMP MIB module (UBQS-ENVMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubiquoss\UBQS-ENVMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:17 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(ubiMgmtv2,) = mibBuilder.importSymbols(
    "UBQS-SMI",
    "ubiMgmtv2")


# MODULE-IDENTITY

ubiEnvMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UbiEnvMonState(TextualConvention, Integer32):
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
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3),
          ("shutdown", 4),
          ("notPresent", 5),
          ("notFunctioning", 6))
    )



# MIB Managed Objects in the order of their OIDs

_UbiEnvMonObjects_ObjectIdentity = ObjectIdentity
ubiEnvMonObjects = _UbiEnvMonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1)
)
_UbiEnvMonTemperatureTable_Object = MibTable
ubiEnvMonTemperatureTable = _UbiEnvMonTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ubiEnvMonTemperatureTable.setStatus("current")
_UbiEnvMonTemperatureEntry_Object = MibTableRow
ubiEnvMonTemperatureEntry = _UbiEnvMonTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 1, 1)
)
ubiEnvMonTemperatureEntry.setIndexNames(
    (0, "UBQS-ENVMON-MIB", "ubiEnvMonTemperatureIndex"),
)
if mibBuilder.loadTexts:
    ubiEnvMonTemperatureEntry.setStatus("current")
_UbiEnvMonTemperatureIndex_Type = Integer32
_UbiEnvMonTemperatureIndex_Object = MibTableColumn
ubiEnvMonTemperatureIndex = _UbiEnvMonTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 1, 1, 1),
    _UbiEnvMonTemperatureIndex_Type()
)
ubiEnvMonTemperatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubiEnvMonTemperatureIndex.setStatus("current")


class _UbiEnvMonTemperatureDescr_Type(DisplayString):
    """Custom type ubiEnvMonTemperatureDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UbiEnvMonTemperatureDescr_Type.__name__ = "DisplayString"
_UbiEnvMonTemperatureDescr_Object = MibTableColumn
ubiEnvMonTemperatureDescr = _UbiEnvMonTemperatureDescr_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 1, 1, 2),
    _UbiEnvMonTemperatureDescr_Type()
)
ubiEnvMonTemperatureDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiEnvMonTemperatureDescr.setStatus("current")
_UbiEnvMonTemperatureValue_Type = Gauge32
_UbiEnvMonTemperatureValue_Object = MibTableColumn
ubiEnvMonTemperatureValue = _UbiEnvMonTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 1, 1, 3),
    _UbiEnvMonTemperatureValue_Type()
)
ubiEnvMonTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiEnvMonTemperatureValue.setStatus("current")
if mibBuilder.loadTexts:
    ubiEnvMonTemperatureValue.setUnits("degrees Celsius")
_UbiEnvMonTemperatureHighThreshold_Type = Integer32
_UbiEnvMonTemperatureHighThreshold_Object = MibTableColumn
ubiEnvMonTemperatureHighThreshold = _UbiEnvMonTemperatureHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 1, 1, 4),
    _UbiEnvMonTemperatureHighThreshold_Type()
)
ubiEnvMonTemperatureHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiEnvMonTemperatureHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ubiEnvMonTemperatureHighThreshold.setUnits("degrees Celsius")
_UbiEnvMonTemperatureLowThreshold_Type = Integer32
_UbiEnvMonTemperatureLowThreshold_Object = MibTableColumn
ubiEnvMonTemperatureLowThreshold = _UbiEnvMonTemperatureLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 1, 1, 5),
    _UbiEnvMonTemperatureLowThreshold_Type()
)
ubiEnvMonTemperatureLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiEnvMonTemperatureLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ubiEnvMonTemperatureLowThreshold.setUnits("degrees Celsius")
_UbiEnvMonTemperatureState_Type = UbiEnvMonState
_UbiEnvMonTemperatureState_Object = MibTableColumn
ubiEnvMonTemperatureState = _UbiEnvMonTemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 1, 1, 6),
    _UbiEnvMonTemperatureState_Type()
)
ubiEnvMonTemperatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiEnvMonTemperatureState.setStatus("current")
_UbiEnvMonFanTable_Object = MibTable
ubiEnvMonFanTable = _UbiEnvMonFanTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ubiEnvMonFanTable.setStatus("current")
_UbiEnvMonFanEntry_Object = MibTableRow
ubiEnvMonFanEntry = _UbiEnvMonFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 2, 1)
)
ubiEnvMonFanEntry.setIndexNames(
    (0, "UBQS-ENVMON-MIB", "ubiEnvMonFanIndex"),
)
if mibBuilder.loadTexts:
    ubiEnvMonFanEntry.setStatus("current")
_UbiEnvMonFanIndex_Type = Integer32
_UbiEnvMonFanIndex_Object = MibTableColumn
ubiEnvMonFanIndex = _UbiEnvMonFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 2, 1, 1),
    _UbiEnvMonFanIndex_Type()
)
ubiEnvMonFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubiEnvMonFanIndex.setStatus("current")


class _UbiEnvMonFanDescr_Type(DisplayString):
    """Custom type ubiEnvMonFanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UbiEnvMonFanDescr_Type.__name__ = "DisplayString"
_UbiEnvMonFanDescr_Object = MibTableColumn
ubiEnvMonFanDescr = _UbiEnvMonFanDescr_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 2, 1, 2),
    _UbiEnvMonFanDescr_Type()
)
ubiEnvMonFanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiEnvMonFanDescr.setStatus("current")
_UbiEnvMonFanState_Type = UbiEnvMonState
_UbiEnvMonFanState_Object = MibTableColumn
ubiEnvMonFanState = _UbiEnvMonFanState_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 2, 1, 3),
    _UbiEnvMonFanState_Type()
)
ubiEnvMonFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiEnvMonFanState.setStatus("current")
_UbiEnvMonSupplyTable_Object = MibTable
ubiEnvMonSupplyTable = _UbiEnvMonSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ubiEnvMonSupplyTable.setStatus("current")
_UbiEnvMonSupplyEntry_Object = MibTableRow
ubiEnvMonSupplyEntry = _UbiEnvMonSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 3, 1)
)
ubiEnvMonSupplyEntry.setIndexNames(
    (0, "UBQS-ENVMON-MIB", "ubiEnvMonSupplyIndex"),
)
if mibBuilder.loadTexts:
    ubiEnvMonSupplyEntry.setStatus("current")
_UbiEnvMonSupplyIndex_Type = Integer32
_UbiEnvMonSupplyIndex_Object = MibTableColumn
ubiEnvMonSupplyIndex = _UbiEnvMonSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 3, 1, 1),
    _UbiEnvMonSupplyIndex_Type()
)
ubiEnvMonSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubiEnvMonSupplyIndex.setStatus("current")


class _UbiEnvMonSupplyDescr_Type(DisplayString):
    """Custom type ubiEnvMonSupplyDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UbiEnvMonSupplyDescr_Type.__name__ = "DisplayString"
_UbiEnvMonSupplyDescr_Object = MibTableColumn
ubiEnvMonSupplyDescr = _UbiEnvMonSupplyDescr_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 3, 1, 2),
    _UbiEnvMonSupplyDescr_Type()
)
ubiEnvMonSupplyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiEnvMonSupplyDescr.setStatus("current")
_UbiEnvMonSupplyState_Type = UbiEnvMonState
_UbiEnvMonSupplyState_Object = MibTableColumn
ubiEnvMonSupplyState = _UbiEnvMonSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 3, 1, 3),
    _UbiEnvMonSupplyState_Type()
)
ubiEnvMonSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiEnvMonSupplyState.setStatus("current")


class _UbiEnvMonSupplySource_Type(Integer32):
    """Custom type ubiEnvMonSupplySource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ac", 1),
          ("dc", 2))
    )


_UbiEnvMonSupplySource_Type.__name__ = "Integer32"
_UbiEnvMonSupplySource_Object = MibTableColumn
ubiEnvMonSupplySource = _UbiEnvMonSupplySource_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 3, 1, 4),
    _UbiEnvMonSupplySource_Type()
)
ubiEnvMonSupplySource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiEnvMonSupplySource.setStatus("current")


class _UbiEnvMonExternalAlarmAc_Type(Integer32):
    """Custom type ubiEnvMonExternalAlarmAc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("fail", 2))
    )


_UbiEnvMonExternalAlarmAc_Type.__name__ = "Integer32"
_UbiEnvMonExternalAlarmAc_Object = MibTableColumn
ubiEnvMonExternalAlarmAc = _UbiEnvMonExternalAlarmAc_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 3, 1, 5),
    _UbiEnvMonExternalAlarmAc_Type()
)
ubiEnvMonExternalAlarmAc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiEnvMonExternalAlarmAc.setStatus("current")


class _UbiEnvMonExternalAlarmUnit_Type(Integer32):
    """Custom type ubiEnvMonExternalAlarmUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("fail", 2))
    )


_UbiEnvMonExternalAlarmUnit_Type.__name__ = "Integer32"
_UbiEnvMonExternalAlarmUnit_Object = MibTableColumn
ubiEnvMonExternalAlarmUnit = _UbiEnvMonExternalAlarmUnit_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 3, 1, 6),
    _UbiEnvMonExternalAlarmUnit_Type()
)
ubiEnvMonExternalAlarmUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiEnvMonExternalAlarmUnit.setStatus("current")
_UbiEnvMonSupplyChannelTable_Object = MibTable
ubiEnvMonSupplyChannelTable = _UbiEnvMonSupplyChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ubiEnvMonSupplyChannelTable.setStatus("current")
_UbiEnvMonSupplyChannelEntry_Object = MibTableRow
ubiEnvMonSupplyChannelEntry = _UbiEnvMonSupplyChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 4, 1)
)
ubiEnvMonSupplyChannelEntry.setIndexNames(
    (0, "UBQS-ENVMON-MIB", "ubiEnvMonSupplyIndex"),
    (0, "UBQS-ENVMON-MIB", "ubiEnvMonSupplyChannelType"),
)
if mibBuilder.loadTexts:
    ubiEnvMonSupplyChannelEntry.setStatus("current")


class _UbiEnvMonSupplyChannelType_Type(Integer32):
    """Custom type ubiEnvMonSupplyChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dc_48v_a", 1),
          ("dc_48v_b", 2))
    )


_UbiEnvMonSupplyChannelType_Type.__name__ = "Integer32"
_UbiEnvMonSupplyChannelType_Object = MibTableColumn
ubiEnvMonSupplyChannelType = _UbiEnvMonSupplyChannelType_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 4, 1, 1),
    _UbiEnvMonSupplyChannelType_Type()
)
ubiEnvMonSupplyChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiEnvMonSupplyChannelType.setStatus("current")
_UbiEnvMonSupplyChannelState_Type = UbiEnvMonState
_UbiEnvMonSupplyChannelState_Object = MibTableColumn
ubiEnvMonSupplyChannelState = _UbiEnvMonSupplyChannelState_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 1, 4, 1, 2),
    _UbiEnvMonSupplyChannelState_Type()
)
ubiEnvMonSupplyChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiEnvMonSupplyChannelState.setStatus("current")
_UbiEnvMonMIBNotificationEnables_ObjectIdentity = ObjectIdentity
ubiEnvMonMIBNotificationEnables = _UbiEnvMonMIBNotificationEnables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 2)
)


class _UbiEnvMonEnableTempStatusChange_Type(TruthValue):
    """Custom type ubiEnvMonEnableTempStatusChange based on TruthValue"""
    defaultValue = 2


_UbiEnvMonEnableTempStatusChange_Type.__name__ = "TruthValue"
_UbiEnvMonEnableTempStatusChange_Object = MibScalar
ubiEnvMonEnableTempStatusChange = _UbiEnvMonEnableTempStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 2, 1),
    _UbiEnvMonEnableTempStatusChange_Type()
)
ubiEnvMonEnableTempStatusChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiEnvMonEnableTempStatusChange.setStatus("current")


class _UbiEnvMonEnableFanStatusChange_Type(TruthValue):
    """Custom type ubiEnvMonEnableFanStatusChange based on TruthValue"""
    defaultValue = 2


_UbiEnvMonEnableFanStatusChange_Type.__name__ = "TruthValue"
_UbiEnvMonEnableFanStatusChange_Object = MibScalar
ubiEnvMonEnableFanStatusChange = _UbiEnvMonEnableFanStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 2, 2),
    _UbiEnvMonEnableFanStatusChange_Type()
)
ubiEnvMonEnableFanStatusChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiEnvMonEnableFanStatusChange.setStatus("current")


class _UbiEnvMonEnableSupplyStatusChange_Type(TruthValue):
    """Custom type ubiEnvMonEnableSupplyStatusChange based on TruthValue"""
    defaultValue = 2


_UbiEnvMonEnableSupplyStatusChange_Type.__name__ = "TruthValue"
_UbiEnvMonEnableSupplyStatusChange_Object = MibScalar
ubiEnvMonEnableSupplyStatusChange = _UbiEnvMonEnableSupplyStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 2, 3),
    _UbiEnvMonEnableSupplyStatusChange_Type()
)
ubiEnvMonEnableSupplyStatusChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiEnvMonEnableSupplyStatusChange.setStatus("current")


class _UbiEnvMonEnableSupplyChannelStatusChange_Type(TruthValue):
    """Custom type ubiEnvMonEnableSupplyChannelStatusChange based on TruthValue"""
    defaultValue = 2


_UbiEnvMonEnableSupplyChannelStatusChange_Type.__name__ = "TruthValue"
_UbiEnvMonEnableSupplyChannelStatusChange_Object = MibScalar
ubiEnvMonEnableSupplyChannelStatusChange = _UbiEnvMonEnableSupplyChannelStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 2, 4),
    _UbiEnvMonEnableSupplyChannelStatusChange_Type()
)
ubiEnvMonEnableSupplyChannelStatusChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiEnvMonEnableSupplyChannelStatusChange.setStatus("current")
_UbiEnvMonMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ubiEnvMonMIBNotificationPrefix = _UbiEnvMonMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 3)
)
_UbiEnvMonMIBNotifications_ObjectIdentity = ObjectIdentity
ubiEnvMonMIBNotifications = _UbiEnvMonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 3, 0)
)
_UbiEnvMonMIBConformance_ObjectIdentity = ObjectIdentity
ubiEnvMonMIBConformance = _UbiEnvMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 4)
)
_UbiEnvMonMIBCompliances_ObjectIdentity = ObjectIdentity
ubiEnvMonMIBCompliances = _UbiEnvMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 4, 1)
)
_UbiEnvMonMIBGroups_ObjectIdentity = ObjectIdentity
ubiEnvMonMIBGroups = _UbiEnvMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 4, 2)
)

# Managed Objects groups

ubiEnvMonMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 4, 2, 1)
)
ubiEnvMonMIBGroup.setObjects(
      *(("UBQS-ENVMON-MIB", "ubiEnvMonTemperatureDescr"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonTemperatureValue"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonTemperatureHighThreshold"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonTemperatureLowThreshold"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonTemperatureLastShutdown"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonTemperatureState"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonFanDescr"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonFanState"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonSupplyDescr"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonSupplyState"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonSupplySource"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonSupplyExtChannel"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonSupplyExtChannelState"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonEnableTempStatusChangeNotif"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonEnableFanStatusChangeNotif"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonEnableSuppStatusChangeNotif"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonEnableSuppExtStatusChangeNotif"))
)
if mibBuilder.loadTexts:
    ubiEnvMonMIBGroup.setStatus("current")


# Notification objects

ubiEnvMonTempStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 3, 0, 1)
)
ubiEnvMonTempStatusChange.setObjects(
      *(("UBQS-ENVMON-MIB", "ubiEnvMonTemperatureDescr"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonTemperatureValue"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonTemperatureState"))
)
if mibBuilder.loadTexts:
    ubiEnvMonTempStatusChange.setStatus(
        "current"
    )

ubiEnvMonFanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 3, 0, 2)
)
ubiEnvMonFanStatusChange.setObjects(
      *(("UBQS-ENVMON-MIB", "ubiEnvMonFanDescr"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonFanState"))
)
if mibBuilder.loadTexts:
    ubiEnvMonFanStatusChange.setStatus(
        "current"
    )

ubiEnvMonSupplyStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 3, 0, 3)
)
ubiEnvMonSupplyStatusChange.setObjects(
      *(("UBQS-ENVMON-MIB", "ubiEnvMonSupplyDescr"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonSupplyState"))
)
if mibBuilder.loadTexts:
    ubiEnvMonSupplyStatusChange.setStatus(
        "current"
    )

ubiEnvMonSupplyChannelStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 3, 0, 4)
)
ubiEnvMonSupplyChannelStatusChange.setObjects(
      *(("UBQS-ENVMON-MIB", "ubiEnvMonSupplyDescr"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonSupplyChannelType"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonSupplyChannelState"))
)
if mibBuilder.loadTexts:
    ubiEnvMonSupplyChannelStatusChange.setStatus(
        "current"
    )


# Notifications groups

ubiEnvMonMIBNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 4, 2, 2)
)
ubiEnvMonMIBNotifGroup.setObjects(
      *(("UBQS-ENVMON-MIB", "ubiEnvMonTempStatusChangeNotif"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonFanStatusChangeNotif"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonSuppStatusChangeNotif"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonSuppExtStatusChangeNotif"))
)
if mibBuilder.loadTexts:
    ubiEnvMonMIBNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ubiEnvMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7800, 100, 2, 4, 1, 1)
)
ubiEnvMonMIBCompliance.setObjects(
      *(("UBQS-ENVMON-MIB", "ubiEnvMonMIBGroup"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonMIBNotifGroup"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonMIBGroup"),
        ("UBQS-ENVMON-MIB", "ubiEnvMonMIBNotifGroup"))
)
if mibBuilder.loadTexts:
    ubiEnvMonMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBQS-ENVMON-MIB",
    **{"UbiEnvMonState": UbiEnvMonState,
       "ubiEnvMonMIB": ubiEnvMonMIB,
       "ubiEnvMonObjects": ubiEnvMonObjects,
       "ubiEnvMonTemperatureTable": ubiEnvMonTemperatureTable,
       "ubiEnvMonTemperatureEntry": ubiEnvMonTemperatureEntry,
       "ubiEnvMonTemperatureIndex": ubiEnvMonTemperatureIndex,
       "ubiEnvMonTemperatureDescr": ubiEnvMonTemperatureDescr,
       "ubiEnvMonTemperatureValue": ubiEnvMonTemperatureValue,
       "ubiEnvMonTemperatureHighThreshold": ubiEnvMonTemperatureHighThreshold,
       "ubiEnvMonTemperatureLowThreshold": ubiEnvMonTemperatureLowThreshold,
       "ubiEnvMonTemperatureState": ubiEnvMonTemperatureState,
       "ubiEnvMonFanTable": ubiEnvMonFanTable,
       "ubiEnvMonFanEntry": ubiEnvMonFanEntry,
       "ubiEnvMonFanIndex": ubiEnvMonFanIndex,
       "ubiEnvMonFanDescr": ubiEnvMonFanDescr,
       "ubiEnvMonFanState": ubiEnvMonFanState,
       "ubiEnvMonSupplyTable": ubiEnvMonSupplyTable,
       "ubiEnvMonSupplyEntry": ubiEnvMonSupplyEntry,
       "ubiEnvMonSupplyIndex": ubiEnvMonSupplyIndex,
       "ubiEnvMonSupplyDescr": ubiEnvMonSupplyDescr,
       "ubiEnvMonSupplyState": ubiEnvMonSupplyState,
       "ubiEnvMonSupplySource": ubiEnvMonSupplySource,
       "ubiEnvMonExternalAlarmAc": ubiEnvMonExternalAlarmAc,
       "ubiEnvMonExternalAlarmUnit": ubiEnvMonExternalAlarmUnit,
       "ubiEnvMonSupplyChannelTable": ubiEnvMonSupplyChannelTable,
       "ubiEnvMonSupplyChannelEntry": ubiEnvMonSupplyChannelEntry,
       "ubiEnvMonSupplyChannelType": ubiEnvMonSupplyChannelType,
       "ubiEnvMonSupplyChannelState": ubiEnvMonSupplyChannelState,
       "ubiEnvMonMIBNotificationEnables": ubiEnvMonMIBNotificationEnables,
       "ubiEnvMonEnableTempStatusChange": ubiEnvMonEnableTempStatusChange,
       "ubiEnvMonEnableFanStatusChange": ubiEnvMonEnableFanStatusChange,
       "ubiEnvMonEnableSupplyStatusChange": ubiEnvMonEnableSupplyStatusChange,
       "ubiEnvMonEnableSupplyChannelStatusChange": ubiEnvMonEnableSupplyChannelStatusChange,
       "ubiEnvMonMIBNotificationPrefix": ubiEnvMonMIBNotificationPrefix,
       "ubiEnvMonMIBNotifications": ubiEnvMonMIBNotifications,
       "ubiEnvMonTempStatusChange": ubiEnvMonTempStatusChange,
       "ubiEnvMonFanStatusChange": ubiEnvMonFanStatusChange,
       "ubiEnvMonSupplyStatusChange": ubiEnvMonSupplyStatusChange,
       "ubiEnvMonSupplyChannelStatusChange": ubiEnvMonSupplyChannelStatusChange,
       "ubiEnvMonMIBConformance": ubiEnvMonMIBConformance,
       "ubiEnvMonMIBCompliances": ubiEnvMonMIBCompliances,
       "ubiEnvMonMIBCompliance": ubiEnvMonMIBCompliance,
       "ubiEnvMonMIBGroups": ubiEnvMonMIBGroups,
       "ubiEnvMonMIBGroup": ubiEnvMonMIBGroup,
       "ubiEnvMonMIBNotifGroup": ubiEnvMonMIBNotifGroup}
)
